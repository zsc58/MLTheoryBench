# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the root-scaled particle normalizer and weighted empirical measures and proves weighted unbiasedness, including the terminal identity. Justifies any cancellation at zero potentials using the existing assumptions or another valid argument. The reference proof derives reference-marginal PRM positivity jointly with unbiasedness from conditional iid sampling and non-extinction; that particular presentation is not required.
- **2 points:** Derives the bound on total variation of the expected terminal empirical law by the normalized expected absolute normalizer error. The quantity in the task is D_TV(E[nuhat_H],pi_H^*), not E[D_TV(nuhat_H,pi_H^*)]. A correct stronger bound may be accepted if independently established.
- **4 points:** Constructs an integrable ratio-normalizer martingale with endpoints Z and What_H, telescopes its increments, and quantitatively derives the conditional iid variance and weighted Cauchy–Schwarz bound. Uses action-level coverage together with the conditional-value identity to obtain K_h(V_h^2)<=C_act V_{h-1}^2, retaining sqrt(C_act) rather than C_act. Naming a martingale or citing the desired increment bound without derivation earns little credit. Global square-integrability of the normalizer is not required.
- **2 points:** Derives the correctly normalized identity Zhat_j integral V_j^2/Vhat_j d pi_j=Z^2(1+D_chi2(pi_j^*||piHat_j)), or an equivalent valid conversion, and sums the levels to obtain the stated sqrt(C_act/N)(H+sum sqrt(D_chi2)) rate. Handles infinite divergences and the empty intermediate sum when H=1. A stronger bound with an additional factor 1/2 is fully acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The score should reflect established mathematical achievements; a missing theorem-critical martingale or quantitative increment bound is a major gap.

Do not require a new strict-positivity assumption, a common-support assumption, Z=1, bounded PRM ratios, or additional moment assumptions. Such conditions must follow from the given hypotheses if used. The product of two target expectations involving Vhat/V and V/Vhat needs support justification; the direct normalized-density identity avoids that issue. Preserve the distinction between conditional second moments used levelwise and an unsupported global second-moment bound on the product normalizer.

The source's intermediate normalization errors are corrected in the reference proof and are not requirements a solver must reproduce.
