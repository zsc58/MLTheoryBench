# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Stochastic-to-deterministic domination (2 points).** Establishes that the deterministic recursion is PSD and proves E||Delta_t||_{bar M}^2 <= Delta_0^T N_t Delta_0 <= ||N_t|| ||Delta_0||^2. Conditioning must respect chronological order and must remain valid for independent contractions with possibly different distributions and the same mean. Derives the needed bound on E[M N M] from 0<=M<=I and N>=0.

2. **Upper polynomial decay (4 points).** Derives the scalar eigenvalue recursion, positivity, and monotonicity of its maximum. Proves a sufficiently quantitative convolution estimate for exponent 0.751, including a valid discrete-to-continuous comparison, treatment of rho=1/2, and rigorous control of the continuous envelope. If using the one-point criterion, checks its calibrated point, not an arbitrary nearby point, and supplies explicit slack sufficient for the discrete time shift and initial term. Handles rho>1/2 using a correct two-step argument or a valid alternative, treats rho=0 and rho=1, and verifies all finite base times and all thresholds introduced by reindexing. Concludes the stated shifted stochastic upper bound with an absolute constant.

3. **Lower construction and deterministic barrier (3 points).** For the prescribed finite spectra, proves the lower convolution comparison and a rigorous strict certificate L_{0.753}(3/4)>1, or valid equivalent estimates. Establishes a finite initial-time constant independent of T and uses a correctly calibrated available coordinate, such as k=t, to prove the lower bound for every 0<=t<=T. Also justifies exclusion of the endpoint p=0.753: the displayed Omega((t+1)^(-0.753)) bound alone excludes only larger exponents. One valid completion uses continuity of the strict integral certificate in the exponent and the same induction at a slightly smaller fixed exponent. The impossibility result concerns uniform bounds on the deterministic recursion; stochastic lower bounds are neither requested nor supplied by majorization.

4. **Parameter and quantifier fidelity (1 point).** Keeps constants independent of the dimension, mean matrix, contraction laws, initial vector, and horizon as applicable. Retains the full spectral interval, integer time domains, prescribed T-dimensional construction, and all requested conclusions. For the deterministic barrier, fixes p before considering K and rules out K uniformly over dimensions, mean matrices, and times.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental constants, rational truncation choices, or presentation. Elementary calculus and convergence theorems may be used with their hypotheses verified; the paper-specific convolution estimate cannot simply be assumed.

An incorrect two-step identity, an unproved global envelope bound, a nonuniform lower-bound initialization, an incorrect spectral-coordinate calibration, or omission of the endpoint argument is a substantive omission, not a completed proof step. A lower bound for the deterministic majorant does not establish a lower bound for the stochastic process. Correcting the source's harmless strict-supremum comparison or enlarging the finite induction base must not be penalized.
