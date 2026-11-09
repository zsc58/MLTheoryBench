# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly handles the observable-history protocol, latent states, fresh sampling, error counts, and weighted regret. Derives the stationary conditional false-positive identity, or an equivalent valid calculation. If martingale differences contain latent-state indicators, uses an analytical filtration containing those states without granting the procedure additional information.
2. **(2 points)** Proves the positive-threshold-floor lower bound in expectation and the almost-sure liminf. A martingale strong-law argument must establish adaptation, conditional centering, and uniform boundedness; another valid almost-sure argument is equally acceptable.
3. **(3 points)** Proves the stated finite-product bound for the null/alternative experiment for every positive integer n and proves its eventual linear order with a positive coefficient independent of n. Correctly uses the no-rejection envelope as an upper bound on realized thresholds, not as their necessarily exact values. Handles vanishing product factors without invalid conditioning. Summability must give a uniform eventual tail bound, not merely positivity of a different number at each horizon.
4. **(3 points)** Establishes the general impossibility for arbitrary allowed procedures, without assuming that the first two mechanisms exhaust all rules. The reference route couples true discoveries to total expected threshold mass and that mass to false positives. The proof must establish both the impossibility of simultaneous sublinear expected errors and an actual Omega(T) expected weighted-regret lower bound in an admissible environment. An explicit coefficient is sufficient but not required if the positive uniform-in-horizon lower bound is otherwise rigorously established.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's threshold-mass argument, particular product estimate, or presentation choices. Missing one of the requested conclusions is theorem-critical; choosing a different valid method is not.

The states are not observed by the procedure. An enlarged filtration may be used privately for probability arguments only. The source's worst-case envelope need not be attained on a realized history, and no-rejection thresholds need not be deterministic functions of time alone.

The finite product in the public task is a required finite-horizon conclusion. Proving only a weaker infinite-product bound does not by itself establish that display, although the same sequential argument ordinarily supplies both. Small horizons with zero product factors and the case C=0 are allowed. The eventual cutoff may depend on the fixed threshold envelope and L.

A contradiction to simultaneous little-o errors alone does not establish an Omega(T) lower bound for every sufficiently large horizon. The reference proof closes this distinction through a quantitative coupling. No FDR constraint, wealth condition, nonvanishing discovery-rate assumption, or threshold-floor/summability dichotomy may be imposed on the final general claim.

All reference-proof obligations are closed. There is no unresolved GT dependency requiring special scoring treatment.
