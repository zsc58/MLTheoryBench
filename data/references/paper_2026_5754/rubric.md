# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: ReLU reduction and canonicalization.** Correctly reduces a continuous K-piece activation to at most (K-1)m ReLU hinges plus an affine term, treating K=1 as the purely affine case. Obtains a domain-wise representation with normalized directions, admissible thresholds, and distinct in-domain kink hyperplanes, accounting for constant units, orientation reversal, out-of-domain hinges, and merging. A mere assertion that piecewise-linear networks are ReLU networks does not earn full credit.

- **3 points: Rigidity and weight-independent entropy.** Uses generic points and transverse restrictions to derive the ball bound |alpha_j| <= 2L and the spherical bound |alpha_j| sqrt(1-t_j^2) <= 2L; controls the affine term; and derives the O(Md log(CMd(2+L)/eta)) uniform entropy bound. Full credit requires handling potentially unbounded spherical coefficients near t=1. For example, negligible-cap deletion and dyadic parameter grids must control both approximation error and cardinality, including the finer direction nets at the smallest retained cap scale and the regime choices. Obtains an internal net without assuming that external grid centers retain the required Lipschitz constant. This is the central bottleneck.

- **2 points: Finite-class noisy fitting law.** Expands around g(x)=E[y|x], converts fitting below sigma^2 into a positive noise multiplier, and combines bounded and dimension-sensitive sub-Gaussian concentration with a union bound. Correctly uses conditional centering rather than assuming label-input independence. Controls the mean multiplier uniformly through |P_n z|, without incorrectly multiplying its exceptional probability by the class size. States the relevant concentration estimates and verifies their hypotheses; incidental numerical constants need not match the reference.

- **3 points: Localization, net reduction, and final balance.** Localizes Gaussian samples to B_2 under the stated dimension condition, derives the value bound, and uses a sample-independent internal uniform net with clipping and nonexpansive projection. Applies the finite-class bound under the original iid law, using localization through event inclusion rather than unjustified conditional concentration. Balances entropy against concentration in both regimes L_* <= sqrt(d)/kappa and L_* > sqrt(d)/kappa, or gives an equivalent unified calculation. Leaves enough concentration exponent after paying for entropy to obtain the stated failure probability from the stated sample-size condition. Produces exactly the public lower bound without additional assumptions or a saturation cap.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the public assumptions. Do not require the reference proof's incidental constants, equation labels, grid choices, or presentation. In particular, a different valid covering argument may replace dyadic grids, and a unified exponent calculation may replace the two-case presentation.

The entropy conclusion alone does not compensate for an unsupported rigidity argument. Merely naming concentration or covering-number methods does not establish a theorem-specific bound: the relevant estimate and its applicable hypotheses must be clear. Routine arithmetic and standard-independent inequalities may be cited in their precise applicable forms.

If an intermediate conclusion is independently proved by another valid argument, score later uses of that conclusion normally. Actual zero-Lipschitz functions and the K=1 case are covered by applying estimates at the strictly positive comparison level L_*; no division by their actual Lipschitz constant is required. No unresolved private proof obligation is being assigned as a completed scoring step.
