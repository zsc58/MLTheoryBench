# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly analyzes the conditional linear SDE, establishes nondegenerate Gaussian conditional laws for every positive time, and obtains the conditional score or an equivalent sufficient density/score analysis. Accounts for the zero initial covariance and continuity toward the sampled initial matrix. Handles zero overlap degrees under the stated inverse convention.
- **3 points:** Derives the empirical-mixture posterior averaging and mixture-score identities, with correct uniform-index weighting, normalization, multiplicities if present, and dependence on the common diffusion coefficient. Derives the stated posterior structural drift and marginal-score expression.
- **3 points:** Establishes square-integrability of the conditional target and uses conditional-expectation orthogonal projection or the explicit squared-error decomposition to prove the state-only minimization claim. Identifies uniqueness modulo marginal null sets and the canonical posterior version. Merely naming conditional expectation or a score-matching method is insufficient.
- **2 points:** Proves exact positive-time reverse marginal laws by a valid localized time-reversal argument or an equivalent reversed-Fokker-Planck argument with justified uniqueness. Checks the relevant coefficient, density, integrability, and solution-class hypotheses on intervals bounded away from the data endpoint, uses the exact terminal marginal as the initial law, and proves weak convergence to the empirical data law.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Require the central posterior-averaging/L2-projection derivation and the exact marginal-law identification; theorem names without relevant statements and hypothesis verification do not earn the corresponding points.

The original latent-conditioned mixture need not be Markovian. Averaging its conditional density equations establishes a one-time marginal Fokker-Planck equation, not equality of path laws with a state-only diffusion. A solution using a Markovian marginal representation must justify that representation, for example by standard SDE/Fokker-Planck uniqueness under verified positive-time coefficient bounds. A direct reverse-density proof is equally acceptable.

Strict positivity and C1 density regularity alone are not a sufficient justification for diffusion reversal or Fokker-Planck uniqueness. In this problem, the finite Gaussian formulas give the stronger positive-time properties needed. Accept standard independent uniqueness or reversal results when their relevant hypotheses are stated and checked; do not demand a proof of those standard results.

Do not require globally Lipschitz posterior drifts, Gaussian finite-horizon initialization, or any score at s=0. Local spatial Lipschitz regularity and uniform linear growth on each compact positive-time interval suffice for the reference route. The conclusion at the singular endpoint is weak convergence of laws, not a claimed density there.

The smooth canonical posterior version is the field used in the reverse SDE. L2 minimizers are unique only up to marginal null sets. Equivalent proofs that explicitly account for this distinction receive full credit.
