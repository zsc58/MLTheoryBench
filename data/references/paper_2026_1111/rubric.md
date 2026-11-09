# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Worst-kernel reduction and unichain policy (2 points).** Correctly identifies the state-independent classical gains, establishes or validly invokes an optimal unichain stationary policy under the worst kernel, and obtains its Poisson equation. A randomized admissible policy must be allowed.
2. **Mixture test (3 points).** Derives conditional type-I control via the null mixture supermartingale and a uniform-in-starting-state logarithmic expected rejection bound under a distinguishable alternative. A complete delay argument handles every recurrent class, finite positive divergence using prior mass and return cycles, and zero-null-probability edges. Merely naming a specialized test result is insufficient.
3. **Epoch policy and null-transition bound (3 points).** Specifies epoch-local testing and a fresh RL restart after rejection. Treats every kernel with induced testing matrix P=P0, not solely p*. Groups consecutive stationary-policy periods, counts rejection at the last action time when it starts RL, controls their stopped potential terms and false-alarm costs, and obtains the stated constant for arbitrary horizons and initial distributions.
4. **Distinguishable kernels and optimality (2 points).** Uses the RL guarantee uniformly over starting states and all phase lengths, combines it with O(j) expected testing time per epoch to obtain a positive linear term minus O((log T)^2), and covers all kernels under the stated alternatives. Concludes robust optimality using the classical gain upper bound at p*.

# Evaluator Notes

Accept any complete valid alternative proof. A non-worst kernel may induce exactly P0 under Delta*; it then belongs to the null-transition case and need not have infinite transient value or strictly greater average reward under the constructed policy. Do not award a proof obligation solely for citing a paper-specific theorem or invoking 'standard concentration' without verifying the result needed here.
