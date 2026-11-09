# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly models the stationary Gaussian OU lag pairs and derives the exact orthogonal-rotation/Wishart-difference representation with the correct coefficients c_+ and c_-. The argument must check that the rotation is deterministic and preserves joint Gaussian independence. A direct sum/difference construction or another valid exact derivation is equally acceptable.
- **3 points:** Uses the correctly normalized Marchenko-Pastur law and an applicable almost-sure asymptotic-freeness result to establish the proportional-limit free convolution for tau>0. Checks Gaussian entries, independence and the proportional regime, and derives the stated R-transform using scaling, reflection and additivity.
- **3 points:** Derives the correct Stieltjes cubic, identifies the analytic physical branch with Im G<0 and zG(z)->1, and obtains the unnormalized absolutely continuous density by almost-everywhere inversion. Establishes that the discriminant is quartic and characterizes boundaries of the continuous support using physical-branch selection. Handles a possible boundary at zero despite degree loss, or gives an equivalent argument covering that case. Does not identify an isolated zero atom as a discriminant boundary or assume that every real discriminant root is an endpoint.
- **2 points:** Correctly applies the exact atom rule for tau>0, obtaining mass max(0,1-2/gamma), no other atoms, and continuous mass min(1,2/gamma). Handles tau=0 separately as sigma^2 MP_gamma with zero atom max(0,1-1/gamma). Verifies the subsequent infinite-lag law limit and upper-edge convergence, and derives the closed form sigma^2(sqrt(1+4gamma)+3)^(3/2)sqrt(sqrt(1+4gamma)-1)/8, or a demonstrably equivalent expression valid for every gamma>0, including gamma=2.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Standard Marchenko-Pastur, specialized Gaussian Wishart asymptotic-freeness, R-transform, Stieltjes-inversion and free-convolution atom results may be invoked without reproving them, provided their relevant hypotheses and conventions are checked. Award no credit for merely naming free probability, asymptotic freeness, or a Wishart decomposition without carrying out the corresponding derivation and checking coefficients.

The theorem concerns the independent simple-pair estimator only. It does not claim an exact law for overlapping trajectory averages, estimated-score dynamics, or nonlinear embeddings. Sigma and each finite lag are fixed during the proportional limit; the infinite-lag limit is taken afterward at fixed sigma and gamma.

The density is that of the full absolutely continuous part, not its conditional normalization. Its inversion formula is interpreted almost everywhere and does not recover an atom as an ordinary density value. Continuous-support boundary selection must use the physical branch. Do not require a blanket one-interval claim for gamma<=2, and do not penalize a correct proof for rejecting such a claim. Merely observing that a cubic discriminant vanishes at finite double roots does not cover degree loss at zero. Equivalent local algebraic or spectral arguments are acceptable.

An infinite-lag critical-point calculation alone does not establish convergence of the finite-lag upper edges. A valid continuity argument, such as bounded free realization and operator-norm convergence, is required for full credit. The original rational expression for t_gamma has a removable singularity at gamma=2; accept it only with its continuous value 1/3 or an equivalent nonsingular parametrization.
