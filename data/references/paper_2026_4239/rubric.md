# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Oracle ordering and metric stability.** Uses the assumed alignment of the restricted population minimizers to establish their common oracle AUROC. Derives the parameter-to-AUROC bound from score Lipschitzness and anti-concentration. Handles margins beyond t0 by a trivial bound and respects half-credit ties. Strict propriety alone does not establish restricted-class alignment.
- **3 points — Raw and augmented upper bounds.** Establishes empirical-gradient concentration and local empirical curvature under the stated independent stratified experiment, then justifies localization of the global ERM using convexity. Obtains the stochastic terms with sample sizes n and N. Derives the actual-versus-ideal augmented population displacement using the Wasserstein gradient bound and the separate constants mu and L_alpha. Combines events to obtain simultaneous probability at least 1-delta. Respects the sufficiently-large-sample qualification and the case ntilde=0.
- **3 points — Local packing, regret separation, and KL.** Constructs an exponentially large angular packing within both local radii. Derives a tie-aware AUROC excess representation and uses the exact weighted disagreement and measure-domination assumptions to prove incompatibility of small regrets for distinct alternatives. Derives classwise KL control from density differentiability, information moments, and density comparability, and then the stratified product-experiment KL bound. Ranking disagreement does not imply separation of the numerical oracle AUROC values.
- **2 points — Testing reduction and minimax expectation.** Defines a valid measurable finite-hypothesis decoder, proves that a decoding error forces regret of order h, and applies Fano with h=a sqrt(d/n). Checks sufficiently large dimension, the two radius conditions, and constant dependencies. Converts the testing lower bound into the expected worst-case regret bound for every estimator, including independently randomized estimators.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its numerical constants. Fixed numerical factors inside log(kd/delta) may be absorbed into the multiplicative constant when justified. A named concentration or Fano argument receives credit only when its relevant hypotheses and its connection to the claimed regret bound are verified.

Do not demand a proof of population alignment from strict propriety: alignment is an explicit assumption. Conversely, do not accept an assertion that strict propriety alone guarantees alignment in a restricted class.

The synthetic-bias dependence is L_s L_g/sqrt(mu L_alpha), not L_s/lambda unless an additional relation between constants is proved from the stated assumptions. No such relation is assumed.

The lower bound concerns the specified class-stratified experiment and parameter-specific evaluation distributions. It does not permit extra parameter-dependent side information. Its central obligation is joint regret incompatibility, not distinct scalar oracle AUROC values.

The conclusions match the n^{-1/2} dependence at fixed dimension and fixed regularity constants. Do not require or award an unsupported claim of an exact dimension-uniform sharp sqrt(d/n) rate: the upper bound retains a logarithmic dimension factor, and the family constants can depend on dimension. A uniform comparison over the local family additionally requires uniform validity of the upper assumptions on that family.

The reference proof has no outstanding theorem-critical obligations.
