---
aliases: ["Machine-learned active spaces enable quantum calculations of spin-state energetics of transition-metal complexes on quantum hardware"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.19049"
url: "http://arxiv.org/abs/2611.19049v1"
published: "2026-11-14T00:44:57Z"
ingested: "2026-11-17T15:27:16Z"
authors:
  - "Muhammad Arsalan Ali Akbar"
  - "Thomas D. Kühne"
  - "Sabre Kais"
  - "Werner Dobrautz"
---

# Machine-learned active spaces enable quantum calculations of spin-state energetics of transition-metal complexes on quantum hardware

## Abstract

> Multireference calculations on transition-metal complexes, on classical or quantum hardware,
> depend on the choice of active space. The orbitals that belong in it are those that are strongly
> entangled in the correlated wavefunction, but measuring this entanglement requires the very
> correlated calculation that the active space is meant to make affordable. Here we present
> SpinAware, a machine-learning model that predicts density-matrix renormalization group (DMRG)
> single-orbital entropies and orbital-pair mutual information from the unrestricted Hartree-Fock
> (UHF) solution of each spin state, without any correlated calculation. Each of the 20 highest
> occupied and 20 lowest unoccupied orbitals is described by 60 descriptors computed from the UHF
> solution, among them the differences between its alpha and beta occupations and energies, its
> metal-d and ligand character, and its exchange coupling to the other orbitals, and a transformer
> predicts the entropy of each orbital in the context of all others. Trained on 3454 spin-pure
> DMRG calculations on mononuclear Cr-Ni complexes, the model transfers to experimentally
> characterized complexes with ligands, binding topologies, oxidation states and metals absent
> from training. Over 11 spin states it reproduces the DMRG entropy profiles with a mean absolute
> error of 0.027, and combining the predicted entropies with the predicted mutual information
> gives a candidate pool that contains 99% of the DMRG-active orbitals of the benchmark spin
> states while keeping, on average, only 15 of the 40 orbitals. Natural-orbital occupation scans
> then select compact active spaces from this pool for a nickel and a cobalt complex. Sample-based
> quantum diagonalization with samples from IBM quantum processors reproduces the exact CASCI
> energies of these spaces to within 0.3 kcal/mol and their spin-state gaps to within 0.10
> kcal/mol for up to 32 qubits.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

