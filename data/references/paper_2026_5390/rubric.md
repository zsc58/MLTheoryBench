# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the schedule-free displacement relation and the polar-alignment inequality, with the correct norm factors. The alignment argument must remain valid when the gradient and polar direction have negative inner product and when the momentum matrix is rank deficient or zero.
- **3 points:** Establishes the momentum tracking bound by separately controlling population-gradient drift and stochastic EMA noise. Accounts for the initialization M_0=G_0 and its geometric transient, and justifies vanishing cross terms using conditional unbiasedness and past measurability. Merely naming momentum tracking is insufficient; independence beyond the stated conditional assumptions must not be imposed.
- **3 points:** Applies Frobenius smoothness, controls all displacement and alignment-error terms, telescopes, and obtains the stated explicit finite-time bound with its dependence on T, eta, mu, beta, B, and r. The argument must cover T=1 and mu=0, with the initial gap outside expectation justified by fixed initialization.
- **2 points:** Gives admissible horizon-dependent parameters and verifies both noisy and noiseless rates, including the log-free beta=0 specialization. Removes harmonic drift from both descent and tracking in that specialization. Covers Delta=0 without requiring eta=0 or mu=1, and keeps asymptotic constants independent of T under the stated uniform boundedness hypothesis.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its exact parameter constants. In particular, order-based choices valid for all nonnegative initial gaps are acceptable in place of separate exact optimization and boundary-case calculations.

A proof that omits the stochastic tracking calculation, the explicit finite-time bound, or an entire required rate conclusion has a theorem-critical gap. An otherwise complete proof whose only omission is the readily repairable Delta=0 tuning case should be treated under the 8-9 category rather than as failure of the entire argument. Full credit requires an admissible construction or another valid argument for that boundary.

Do not accept the claim that initial optimality alone forces subsequent gradients to vanish in the presence of stochastic noise. An unspecified limit eta down to zero is not by itself a construction of the positive horizon-dependent steps required by the task. Choosing mu=0 must precede dropping deterministic momentum-tracking terms in a noiseless bound.

The rate conclusions are conditional on the assumed bounds holding with the same constants across the tuned runs. Solvers are not required to prove boundedness of the unprojected dynamics, introduce projection or weight decay, assume independent batches, or prove results for a different averaging recursion.
