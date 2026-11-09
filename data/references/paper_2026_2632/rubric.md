# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Constructs, for every `a` in `(0,s^2)`, independent Gaussian signal and noise variables whose sum has the fixed `N(m,s^2)` law, and concludes non-identifiability of the variance split.
- **2 points:** Conditions the privileged-supervision objective on `(x_*,D)` and correctly explains why positive weights and joint model richness permit separate minimization of the two heads. Justifies that the jointly attainable conditional minimizers have finite population risk and that every population minimizer must agree with them almost everywhere, by a nonnegative excess-risk argument or an equivalent valid argument.
- **2 points:** Derives that the latent categorical cross-entropy is uniquely minimized by `pi_j^(f)=P(B(F_*)=j|x_*,D)` for every bin, including bins with zero conditional probability.
- **3 points:** Derives the squared-log-variance minimizer `log sigma_hat^2=E[log S_*|x_*,D]`, exponentiates correctly, and states the almost-everywhere population-consistency conclusion and its latent/aleatoric interpretation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that merely names cross-entropy or squared-loss optimality without applying it to the conditioned objective does not earn the corresponding derivation points.

A solver may invoke standard categorical log-loss optimality and conditional-mean squared-loss optimality after stating or correctly applying their relevant hypotheses. Do not require the exact KL-divergence notation or the reference proof's particular integrability estimate. A briefly omitted routine finite-risk or zero-probability justification is a readily repairable omission, not evidence that the target is false; substantial failure to justify the conclusion for every population minimizer is an important missing step.

The first claim is pointwise. Do not require the solver to construct one coherent prior or process realizing all alternative splits across inputs. The second claim concerns the auxiliary objective only. Do not require consistency for the full training objective, continuous-signal variance recovery, or exact recovery of the noisy posterior predictive. The noise-head conclusion is a conditional geometric-mean summary; replacing it by the conditional arithmetic mean of `S_*` is incorrect.
