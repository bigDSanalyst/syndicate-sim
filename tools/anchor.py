#!/usr/bin/env python3
"""Continuous priority anchoring for the syndicate vault.

In a no-custody protocol, provable priority IS the enforcement layer
(Consortium Agreement, section 7.4). A defecting member leaves with
unanchored work; the team keeps a Bitcoin-attested record of everything
that existed and when. Gaps in that record are what backdating attacks
feed on, so the cadence is a heartbeat, not an event.

Each run writes a manifest (canonical JSON of git HEAD, tree hash, and
sha256 of every ledger file) and appends one entry to
ledger/anchors/log.jsonl - an append-only hash chain. The manifest is
submitted to OpenTimestamps calendars; the .ots attestation lands in
Bitcoin within ~1-2 hours and is upgraded on later runs.

The prev field of each entry holds the hash of the previous entry
immutable core (seq, ids, hashes, created). Status fields are mutable
bookkeeping and are deliberately excluded from the chain. Every Bitcoin
stamp retroactively covers all earlier entries: tamper with any past
manifest and every later stamp stops matching.

Commands:
  run~~~~~~~~~~~~~~~~~~~~~~anchor current HEAD (no-op if already anchored)
  upgrade~~~~~~~~~~~~~~~~~~retry submissions + pull Bitcoin confirmations
  verify~~~~~~~~~~~~~~~~~~~recompute digests, check chain, read attestations
  milestone~~--tag~T~-m~M~~~anchor + annotated git tag for a human milestone

verify proves structure and digest integrity without a Bitcoin node and
works on a bare file export of the repo (a Zenodo snapshot). Full
independent confirmation of an attestation is the ots verify command
from opentimestamps-client against a local node. Anchors reflect
committed state - commit before running milestone locally.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from opentimestamps.calendar import RemoteCalendar
    from opentimestamps.op import OpSHA256
    from opentimestamps.timestamp import DetachedTimestampFile
    try:
        from opentimestamps.bitcoin import BitcoinAttestation
    except ImportError:
        BitcoinAttestation = None
    HAVE_OTS = True
except ImportError:
    HAVE_OTS = False

CALENDARS = [
    "https://btc.calendar.opentimestamps.org",
    "https://bob.btc.calendar.opentimestamps.org",
    "https://finney.calendar.eternitywall.com",
]
STALE_DAYS = 14
CORE_FIELDS = ["seq", "anchor_id", "git_head", "git_tree", "manifest", "manifest_sha256", "prev", "created"]


def sh(*args, cwd):
    r = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if r.returncode != 0:
        sys.exit("ERROR: git command failed: " + r.stderr.strip())
    return r.stdout.strip()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    return sha256_bytes(p.read_bytes())


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def core_hash(entry):
    """Hash of the immutable fields only - statuses may change, cores never."""
    return sha256_bytes(canonical({k: entry[k] for k in CORE_FIELDS}).encode())


def load_log(log_path):
    if not log_path.exists():
        return []
    return [json.loads(ln) for ln in log_path.read_text().splitlines() if ln.strip()]


def rewrite_log(log_path, entries):
    log_path.write_text("".join(canonical(e) + "\n" for e in entries))


def repo_state(repo):
    head = sh("git", "rev-parse", "HEAD", cwd=repo)
    tree = sh("git", "rev-parse", "HEAD^{tree}", cwd=repo)
    ledger = []
    for p in sorted((repo / "ledger").rglob("*")):
        if p.is_file() and "anchors" not in p.relative_to(repo).parts:
            ledger.append({"path": p.relative_to(repo).as_posix(), "sha256": sha256_file(p)})
    return {"git_head": head, "git_tree": tree, "ledger_files": ledger}


def make_anchor(repo, anchors_dir, log_path):
    entries = load_log(log_path)
    state = repo_state(repo)
    head = state["git_head"]

    if any(e["git_head"] == head for e in entries):
        last = max(e["seq"] for e in entries if e["git_head"] == head)
        print("⏭️  HEAD " + head[:12] + " already anchored (#" + format(last, "04d") + ") - skipping")
        return None

    prev = entries[-1] if entries else None
    seq = (prev["seq"] + 1) if prev else 1
    anchor_id = format(seq, "04d") + "-" + datetime.now(timezone.utc).strftime("%Y-%m-%d")
    state["anchor_id"] = anchor_id
    manifest_path = anchors_dir / (anchor_id + ".json")
    manifest_path.write_bytes(canonical(state).encode())

    entry = {
        "seq": seq,
        "anchor_id": anchor_id,
        "git_head": head,
        "git_tree": state["git_tree"],
        "manifest": "ledger/anchors/" + anchor_id + ".json",
        "manifest_sha256": sha256_file(manifest_path),
        "prev": core_hash(prev) if prev else None,
        "status": "unsubmitted",
        "created": now(),
    }
    with log_path.open("a") as f:
        f.write(canonical(entry) + "\n")
    print("✅ anchor #" + format(seq, "04d") + " " + anchor_id + ": head " + head[:12] + ", " + str(len(state["ledger_files"])) + " ledger files")
    return entry


def _load_ots(path):
    with path.open("rb") as f:
        return DetachedTimestampFile.from_file(f)


def _save_ots(detached, path):
    with path.open("wb") as f:
        writer = getattr(detached, "write", None) or detached.to_file
        writer(f)


def _has_bitcoin(detached):
    if BitcoinAttestation is None:
        return False
    try:
        return any(isinstance(a, BitcoinAttestation) for a in detached.timestamp.attestations)
    except Exception:
        return False


def _digest_hex(detached):
    """python-opentimestamps returns file_digest as bytes; normalize to hex."""
    d = getattr(detached, "file_digest", None)
    if isinstance(d, bytes):
        return d.hex()
    if d is not None:
        return str(d)
    return ""


def ensure_stamps(repo, log_path):
    """Submit anything unsubmitted; sync submitted entries toward confirmation."""
    if not HAVE_OTS:
        print("⚠️  python-opentimestamps not installed - entries recorded, stamps deferred")
        return
    entries = load_log(log_path)
    changed = False
    for e in entries:
        manifest = repo / e["manifest"]
        ots = Path(str(manifest) + ".ots")
        if not manifest.exists():
            print("❌ #" + format(e["seq"], "04d") + ": manifest file missing")
            continue
        if not ots.exists():
            detached = DetachedTimestampFile.from_bytes(OpSHA256(), manifest.read_bytes())
            ok = 0
            for url in CALENDARS:
                try:
                    RemoteCalendar(url).commit(detached.timestamp)
                    ok += 1
                except Exception as ex:
                    print("⚠️  " + url + ": " + str(ex))
                if not ok:
                    continue
                _save_ots(detached, ots)
                e["status"] = "pending"
                changed = True
                print("📤 #" + format(e["seq"], "04d") + " submitted to " + str(ok) + " calendar(s)")
        elif e["status"] != "confirmed":
            detached = _load_ots(ots)
            if _has_bitcoin(detached):
                e["status"] = "confirmed"
                e["confirmed_at"] = now()
                changed = True
                print("⛓️  #" + format(e["seq"], "04d") + " confirmed in Bitcoin")
            else:
                for url in CALENDARS:
                    try:
                        RemoteCalendar(url).sync_timestamp(detached.timestamp)
                    except Exception:
                        pass
                if _has_bitcoin(detached):
                    _save_ots(detached, ots)
                    e["status"] = "confirmed"
                    e["confirmed_at"] = now()
                    changed = True
                    print("⛓️  #" + format(e["seq"], "04d") + " confirmed in Bitcoin")
    if changed:
        rewrite_log(log_path, entries)


def stale_unsubmitted(log_path):
    bad = []
    for e in load_log(log_path):
        if e["status"] == "unsubmitted":
            age = (datetime.now(timezone.utc) - datetime.fromisoformat(e["created"].replace("Z", "+00:00"))).days
            if age > STALE_DAYS:
                bad.append(e["seq"])
    return bad


def milestone(repo, anchors_dir, log_path, tag, message):
    entries = load_log(log_path)
    head = sh("git", "rev-parse", "HEAD", cwd=repo)
    entry = None
    for e in entries:
        if e["git_head"] == head:
            entry = e
    if entry:
        print("⏭️  HEAD already anchored as #" + format(entry["seq"], "04d") + " - tagging existing anchor")
    else:
        entry = make_anchor(repo, anchors_dir, log_path)
        if entry is None:
            sys.exit("❌ could not anchor HEAD")
    tag_msg = ("milestone: " + message + "\n" + "anchor: " + entry["anchor_id"] + "\n" + "manifest_sha256: " + entry["manifest_sha256"] + "\n" + "git_head: " + entry["git_head"])
    sh("git", "tag", "-a", tag, "-m", tag_msg, head, cwd=repo)
    print("🏷️  " + tag + " -> " + head[:12] + " (anchor #" + format(entry["seq"], "04d") + ")")


def verify(repo, log_path):
    entries = load_log(log_path)
    if not entries:
        print("no anchors yet")
        return True
    ok = True
    prev_hash = None
    for e in entries:
        if e.get("prev") != prev_hash:
            print("❌ #" + format(e["seq"], "04d") + ": chain broken (prev mismatch)")
            ok = False
        prev_hash = core_hash(e)
        m = repo / e["manifest"]
        if not m.exists():
            print("❌ #" + format(e["seq"], "04d") + ": manifest missing")
            ok = False
            continue
        if sha256_file(m) != e["manifest_sha256"]:
            print("❌ #" + format(e["seq"], "04d") + ": manifest digest mismatch - tampered?")
            ok = False
        ots = Path(str(m) + ".ots")
        if e["status"] != "unsubmitted" and not ots.exists():
            print("❌ #" + format(e["seq"], "04d") + ": status " + e["status"] + " but no .ots file")
            ok = False
        if ots.exists() and HAVE_OTS:
            detached = _load_ots(ots)
            digest = _digest_hex(detached)
            if digest and digest != e["manifest_sha256"]:
                print("❌ #" + format(e["seq"], "04d") + ": .ots stamps different bytes than the log claims")
                ok = False
            if _has_bitcoin(detached):
                for a in detached.timestamp.attestations:
                    if isinstance(a, BitcoinAttestation):
                        print("  ⛓️  #" + format(e["seq"], "04d") + " attested at Bitcoin block " + str(a.height))
    n_conf = 0
    for e in entries:
        if e["status"] == "confirmed":
            n_conf += 1
    print(str(len(entries)) + " anchor(s), " + str(n_conf) + " Bitcoin-confirmed - " + ("OK" if ok else "FAILURES PRESENT"))
    return ok


def main():
    ap = argparse.ArgumentParser(description="Continuous priority anchoring for the syndicate vault.")
    ap.add_argument("command", choices=["run", "upgrade", "verify", "milestone"])
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--tag", help="tag name for milestone (e.g. v0.1-preprint)")
    ap.add_argument("--message", "-m", help="milestone description")
    args = ap.parse_args()

    repo = args.repo.resolve()
    anchors_dir = repo / "ledger" / "anchors"
    anchors_dir.mkdir(parents=True, exist_ok=True)
    log_path = anchors_dir / "log.jsonl"

    if args.command == "run":
        make_anchor(repo, anchors_dir, log_path)
        ensure_stamps(repo, log_path)
    elif args.command == "upgrade":
        ensure_stamps(repo, log_path)
    elif args.command == "milestone":
        if not (args.tag and args.message):
            sys.exit("milestone requires --tag and --message")
        milestone(repo, anchors_dir, log_path, args.tag, args.message)
        ensure_stamps(repo, log_path)
    elif args.command == "verify":
        return 0 if verify(repo, log_path) else 1

    stale = stale_unsubmitted(log_path)
    if stale:
        print("❌ anchors " + str(stale) + " unsubmitted for >" + str(STALE_DAYS) + " days - calendars unreachable?")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
