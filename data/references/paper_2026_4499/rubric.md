# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly represents the probit comparison by an equivalent Gaussian half-space observation model and establishes the joint Gaussian moments of the noisy queried difference and \(f(x)\), including the outcome probabilities.
- **4 points:** Derives the half-space-truncated Gaussian conditional mean, including the correct inverse-Mills-ratio factor and covariance/variance normalization. Gaussian regression followed by a one-dimensional integral is sufficient; a valid ESN argument or another complete derivation is equally acceptable.
- **2 points:** Obtains both look-ahead posterior-mean formulas, with the reverse outcome having the correct sign and \(\Phi(-t)\) denominator.
- **2 points:** Substitutes the two conditional means and predictive outcome probabilities into the defining knowledge-gradient expectation, preserving the maximum-after-conditioning order and the subtraction of \(V(m)\), to obtain the exact asserted expression.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

All calculations are conditional on fixed current data under the stipulated Gaussian surrogate. Do not require a proof that the exact posterior from historical preference data is Gaussian. The one-step update here is exact under the stipulated current law, not an approximate-inference refit after the new observation.

A Gaussian-noise construction need only reproduce the joint law of the surrogate and the preference outcome; it need not identify an auxiliary event with an already realized event on the original probability space.

The proof must remain valid for singular Gaussian laws, including zero latent-difference variance and deterministic function evaluations. An argument dividing only by \(v_d+1\), and by the strictly positive Gaussian outcome probabilities, already covers these cases and need not list them separately. An argument dividing by \(v_d\) or using a nondegenerate density must address the relevant zero-variance cases.

The task assumes finite attained maxima only for its KG assertion. Do not require the solver to prove compactness, continuity, or existence of maximizers from GP assumptions. The maximum of a conditional mean must not be replaced by the conditional expectation of a sample-path maximum.

The exact acquisition expression retains spatial maximizations through \(V\). Full credit does not require analytic maximizers, a spatial optimization algorithm, or a claim that numerical maximization is unnecessary. A bare citation to a specialized distribution's moments is not a substitute for stating and correctly applying the needed result.
