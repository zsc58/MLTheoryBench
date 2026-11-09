# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the likelihood objects and the conditional-law-preserving reparameterization to represent the adaptive objective under the fixed law p(theta)q(u). Distinguishes total rollout differentiation from differentiation with observations or designs fixed. The likelihood-ratio objective is already a public definition; deriving it from entropy or proving posterior policy-factor cancellation is not required.
- **3 points:** Differentiates the fixed-base-law adaptive objective under the stated regularity assumptions and applies the chain rule to obtain both marginal score contractions with the correctly oriented rollout Jacobians and the total conditional log-likelihood derivative.
- **2 points:** Proves the deterministic static-design identity. Uses the static rollout's pushforward law to identify its marginal observation density, and uses the permitted differentiation of the normalized marginal integral to cancel the expected fixed-y marginal design score. Retains the conditional observation-path contribution. No inverse reparameterization or injectivity assumption is required.
- **3 points:** Defines or correctly interprets the population score-substituted estimator, subtracts it from the exact adaptive gradient, and bounds its error using Jensen/operator-norm inequalities and the eta/L hypothesis. Justifies the Jacobian bound at every fixed policy parameter where the task assumes differentiability, for example directly by Lipschitz difference quotients. Preserves the common constants and the every-phi conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, an entropy derivation of the already-defined objective, posterior cancellation, an inverse rollout map, or invocation of Rademacher's theorem.

Rademacher's theorem alone establishes differentiability for Lebesgue-almost every policy parameter. A proof using it must still justify the task's every-parameter assertion using the differentiability assumed in the setup; the elementary fact that an existing derivative of an L-Lipschitz map has operator norm at most L suffices.

Deduct substantially for omitting either adaptive marginal score term, replacing the conditional total derivative by a fixed-observation derivative without justification, canceling an adaptive Jacobian-weighted design-score term by static normalization, failing to justify the static cancellation, or proving only an almost-everywhere-in-phi bound while asserting an every-phi conclusion.

The estimator here is a population expectation. Do not require a finite-sample error bound, and do not accept an unsupported claim that every finite-sample Monte Carlo realization has error at most eta.

The likelihood notation denotes the observation-kernel product and its prior integral with fixed design arguments. Do not reinterpret it as ordinary conditioning on an adaptively selected full design sequence.

The public task specifies policy probability kernels, not necessarily Lebesgue densities. The core proof uses their experiment law and its fixed-noise representation and requires no policy-density calculation. A solver need not provide the optional posterior interpretation. If such an interpretation is included, scalar policy-density cancellation is justified only when suitable densities exist; a reference-measure or direct kernel argument handles the general case. An error confined to that optional interpretation should be assessed proportionately and must not be treated as failure of otherwise complete gradient and error-bound derivations.
