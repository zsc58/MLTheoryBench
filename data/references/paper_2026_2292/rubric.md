# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points — Population projection and isotonic rate.** Correctly identifies the population projection in the score law, its boundedness and quadratic margin, and proves the squared L2 rate O_p(n^{-2/3}). A localized least-squares proof must state an applicable empirical-process bound, verify its tail and entropy hypotheses, and justify the critical radius. A valid standard theorem may replace this derivation if its relevant statement and hypotheses are supplied and checked.

2. **4 points — Calibration and asymptotic expansion.** Derives empirical residual centering or blockwise calibration, obtains the exact estimator decomposition without assuming the plug-in/AIPW identity, and controls the labeled and unlabeled remainders at the requested orders. Proves E[m_0]=psi_0 or otherwise establishes the mean-zero normalization of the influence pair. Retains rho_n in the sharp expansion and replaces it by rho_0 only at o_p(M^{-1/2}) precision. Defines the two-sample scaling correctly and uses labeled-only fitting for the unlabeled conditional-independence argument.

3. **2 points — Variance and efficiency.** Derives the centered-score AIPW variance decomposition and applies isotonic projection optimality to recentered nondecreasing competitors. Establishes both the full- and reduced-experiment efficiency conclusions using a valid canonical-gradient argument or an explicitly stated applicable standard efficiency result. Minimization over AIPW scores alone, without identifying the semiparametric bound, is insufficient for the efficiency claim.

4. **2 points — Fitted-score oracle.** Uses a fresh population draw conditional on the labeled fit and respects the specified version convention. Proves the oracle calibration-error rate and the first-order estimator equivalence. One valid route derives bounded-variation preservation from ordered level sets and Jordan decomposition, combines empirical and population calibration identities with localized multiplier control, and then bounds the labeled and unlabeled processes of the oracle difference. Interprets no further gain relative to the conditional-mean score-only AIPW benchmark.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions; do not require the reference proof's exact organization or stronger intermediate bounds when another argument proves the requested targets.

Merely naming isotonic regression, calibration, entropy, or concentration does not close the corresponding obligation. Standard independent results may be used when their relevant conclusions and hypotheses are stated and verified. The reference proof contains no unresolved specialized dependency.

Do not demand the false generic localized entropy estimate log N_[ ](epsilon,F_r,L2)=O(r/epsilon). The global O(1/epsilon) entropy bound suffices. In local maximal inequalities, a bound of the form n^{-1/2}r^{1/2}+n^{-1}r^{-1} is valid for the argument; the second term is harmless at and above r=n^{-1/3}. A solver who retains this correction should receive full credit.

Envelope localization is removed using boundedness in probability of the fitted score. Do not credit an assertion that the outcome-tail assumption alone removes this event.

Require correct centering in the variance comparison: an arbitrary monotone competitor need not have mean psi_0, but its recentered version remains admissible and gives the same AIPW estimator.

The oracle is not the conditional mean under a distribution averaging over training samples, nor an empirical conditional mean. Arbitrary modifications on random population-null sets are excluded by the public version convention. Do not add continuity of the score distribution, strict monotonicity, positive score variance, positive limiting estimator variance, or an unstated rate of convergence of rho_n.

The exact oracle estimator difference is (1-rho_n)(P_N^U-P_n^L)(widehat m_0-m_n^*); population integrals cancel. The population residual inner-product identity is used to prove the calibration-error rate, not as an additional estimator remainder.

The final no-gain conclusion concerns the stated oracle benchmark. Do not require or reward an unsupported universal comparison with arbitrary data-dependent, irregular, or superefficient procedures.
