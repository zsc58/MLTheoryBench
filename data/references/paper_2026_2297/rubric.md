# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Lower-bound construction and information argument (3 points):** Constructs an admissible decreasing Gaussian epoch family with a separately chosen designated arm in each epoch; verifies both the range and variation inequalities; proves the information comparison; and obtains the stated numerical constant. Handles integer epoch counts and the regime where the epoch count saturates at T. A merely asymptotic Omega statement does not establish the requested constant. The zero-noise target is handled directly.

2. **Adaptive-window comparisons (3 points):** Establishes concentration under adaptive sampling without asserting that conditional sub-Gaussianity implies independence. Derives the RAW-UCB comparison using the fact that past means are at least current means. For the specified geometric implementation, controls the number of refreshed statistics and derives the arbitrary-last-window comparison from the stored blocks and monotonicity. Naming the efficient method or claiming a constant-factor transfer without its necessary comparison argument does not close this step.

3. **Batch regret decomposition (2 points):** Correctly separates initialization, favorable first pulls, later pulls, and failures. Proves the telescoping O(KV_T) charge, the O_alpha(sigma min(MK,T)sqrt(log T)) first-pull confidence cost, the V_T T/M decay bound, and the O_alpha(sigma sqrt(MKT log T)) later-pull confidence cost. Sums over arms actually pulled in each batch and uses variation transitions only through T-1. Failure probabilities are applied after initialization.

4. **Optimization and algorithmic scope (2 points):** Optimizes the integer batch count with endpoint cases, absorbs the mixed first-pull term into the leading cube-root term plus KV_T, and proves the stated bound for both algorithms. Handles V_T=0 and sigma=0 without undefined divisions. Makes clear that batching is only for analysis and that algorithmic constants may depend on fixed alpha, while the algorithms require neither T nor V_T.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation, partition, or presentation. An alternative argument need not reproduce the reference's particular intermediate constants, but must obtain the target's lower-bound constant and its full parameter range.

The budget is an upper bound, not realized variation. The geometric algorithm refreshes level j>=1 first at pull 2^j and then every 2^{j-1} pulls. Only initialized levels participate in its index, and confidence radii use the current calendar time. Do not evaluate a different refresh schedule as though it were the specified source algorithm.

Do not accept a batch-confidence bound proportional to M sqrt(KT) as sufficient for the claimed optimization. Do not suppress KV_T inside a remainder that vanishes when sigma=0. Theorem-critical missing arguments remain major gaps. No private ground-truth obligation is being left open.
