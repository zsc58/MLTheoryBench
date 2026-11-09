# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Regret-to-wealth comparison.** Correctly uses the pathwise regret inequality against the fixed witness `u_*` to show that the learner's log wealth is at least the comparator's cumulative log wealth minus `r_T`.
- **3 points: Predictable drift decomposition.** Proves the logarithmic quadratic lower bound and decomposes comparator log wealth into the martingale sum `S_T` and cumulative edge `A_T`. Correctly derives `A_T >= kappa T-2(t_0-1)` from the uniform edge condition and the pre-`t_0` lower bound.
- **3 points: Concentration and finite-time crossing.** Verifies the martingale-difference and conditional support-length properties, derives an adequate one-sided exponential concentration bound, and combines it with the definition of `N_gamma(r)` to prove `Q(sigma_gamma>T) <= exp(-kappa^2 T/2)` for every `T>=N_gamma(r)`. Merely citing concentration without verifying its hypotheses or connecting failure to cross with a martingale lower-tail event does not earn full credit.
- **2 points: Stopping-time consequences.** Correctly obtains almost-sure finite crossing and applies the tail-sum formula and a valid geometric-series estimate to prove `E_Q[sigma_gamma] <= N_gamma(r)+4/kappa^2`.

# Evaluator Notes

Accept any complete alternative proof under exactly the stated assumptions. Small improvements to constants are acceptable if they imply all stated bounds. Do not double-penalize later steps when an earlier conclusion is independently established by a valid argument. A proof that establishes only eventual detection, without the requested finite-time probability or expected-time guarantees, is materially incomplete.
