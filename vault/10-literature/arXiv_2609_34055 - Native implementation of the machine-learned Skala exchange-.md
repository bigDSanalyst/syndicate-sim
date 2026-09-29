---
aliases: ["Native implementation of the machine-learned Skala exchange-correlation functional in CP2K: Unified one-centre reconstruction for molecular and condensed-phase calculations"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.34055"
url: "http://arxiv.org/abs/2609.34055v1"
published: "2026-09-28T00:26:04Z"
ingested: "2026-09-29T12:04:08Z"
authors:
  - "Johann Pototschnig"
  - "Franz Pöschel"
  - "Jürg Hutter"
  - "Thomas D. Kühne"
---

# Native implementation of the machine-learned Skala exchange-correlation functional in CP2K: Unified one-centre reconstruction for molecular and condensed-phase calculations

## Abstract

> We implement the machine-learned Skala exchange-correlation (XC) functional natively in CP2K
> using its Gaussian and plane-wave (GPW) and Gaussian and augmented-plane-wave (GAPW) methods. A
> joint one-centre reconstruction of density, density gradients, and kinetic-energy density before
> functional evaluation preserves mixed gradient terms and nonlocal couplings between smooth and
> atom-local contributions in all-electron and pseudopotential calculations. An XC-specific GAPW
> representation resolves rapidly varying local contributions on atom-centred grids, reducing
> plane-wave requirements for pseudopotential calculations. The implementation includes Brillouin-
> zone sampling and point-group symmetry reduction. With sufficiently flexible orbital bases, it
> retains the molecular benchmark accuracy of our earlier GauXC formulation. All-electron
> Skala-D3(BJ) calculations yield a mean absolute error (MAE) of 1.54 kJ mol$^{-1}$ against
> diffusion Monte Carlo for crystalline CO$_2$, NH$_3$, and urea, spanning dispersion, quadrupolar
> electrostatics, and hydrogen bonding. For all thirteen DMC-ICE13 phases, the MAEs are 1.16 kJ
> mol$^{-1}$ for absolute lattice energies and 0.82 kJ mol$^{-1}$ for the twelve relative energies
> to ice Ih. At fixed experimental geometries, all-electron/mixed-core calculations give a band-
> gap MAE of 0.43 eV on a 15-material set, substantially below commonly used semilocal functionals
> and comparable to widely used hybrid functionals. The LC10 benchmark nevertheless reveals
> systematically underestimated equilibrium lattice constants, indicating structural overbinding.
> This framework connects molecular Skala to condensed-phase electronic structure and enables
> future development using periodic many-body reference data.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

