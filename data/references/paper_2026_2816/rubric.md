# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Identifies the projection kernel and derives or correctly applies Var[Lambda_S(f)] = sum_k ||P_{H^perp}(f Phi_{-j,k})||_2^2.
- **3 points:** Performs local cancellation by subtracting point values (Holder) or local means (Sobolev), explains membership of the subtracted term in the kernel span, and establishes the corresponding local regularity bound on the correct domains.
- **3 points:** Uses support diameter, scaling, and bounded overlap to sum the local bounds; covers fractional Sobolev and s=1 gradient cases with constants independent of s.
- **2 points:** Handles the nonempty-rank scale domain and converts n comparable to 2^{dj} into C|f|_s^2 n^{1-2s/d}, with the indicated seminorm and constant dependence.

# Evaluator Notes

Accept any complete valid alternative proof. Do not award credit for merely naming projection DPPs, wavelets, or Poincare inequalities without carrying out cancellation, local estimates, summation, and scale conversion. In the Sobolev cases the seminorms are over (0,1)^d; no regularity of a zero extension across its boundary is assumed. A missing regularity case, an unjustified local inequality, or unverified dependence of the final constant on s is theorem-critical.
