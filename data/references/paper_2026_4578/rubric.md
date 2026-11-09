# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Concentration and suboptimal-pull control (2 points).** Establishes valid control of adaptively observed empirical means and proves that total suboptimal pulls are negligible relative to the horizon. For the reference route, derives the uniform deterministic-time expected-count bound by separating empirical errors, index overshoots, and losses of an optimal comparator. A fixed-confidence bound alone is not a probability-tending-to-one event, and an adaptive count must not be treated as independent of its observed rewards.

2. **Optimal-arm stability (3 points).** Establishes the winner-map dot-product drift and controls empirical perturbations strongly enough for the full allowed regime of arbitrarily slowly diverging variance inflation. For the reference route, proves the weighted exponential-moment and inverse-proportion recursions, closes them by Hölder inequalities, obtains uniform optimal empirical-error moments, and then derives and sums the calendar-time stopped Lyapunov recursion. Handles one optimal arm directly and two optimal arms using the constant winner probabilities and the resulting Lyapunov drift, not nonexistent strict monotonicity. Also covers the all-optimal case.

3. **Sharp selection probabilities (3 points).** Obtains matching exponential rates for a fixed suboptimal arm in an explicitly justified time and count window. For the reference route, controls the lower tail of the maximum optimal index, uses a sufficient winning event involving every competitor for the lower selection bound, and retains or validly absorbs the Gaussian-tail prefactor and the deterministic competitor-loss factor. Proves that the latter has logarithm negligible relative to log(T/sigma_T). Does not infer uniform index localization from terminal allocation convergence or require sigma_T/log log T to diverge.

4. **Waiting times and matching count asymptotics (2 points).** Establishes negligible time to the count cutoff, controls how many pulls occurred before calendar-time burn-in, and gives valid two-sided waiting-time comparisons with horizon truncation. For the reference route, constructs independent uniform blocks before restricting to good events, handles any block straddling burn-in, and proves the geometric-sum logarithmic law including its log sigma_T term. Derives both integer count brackets, treats rounding errors correctly, and takes the slack limits to obtain the sharp constant 2/Delta_a^2. Checks divergence of the deterministic stability normalizers.

# Evaluator Notes

Accept a complete valid alternative proof; the specific winner-map, moment-recursion, or geometric-coupling presentation is not mandatory. Allocate the corresponding points to alternative arguments that establish the same conclusions under the full stated assumptions.

For a proof using the reference architecture, merely naming a paper-specific moment lemma, Lyapunov method, or geometric-sum law does not close the relevant obligation. The replacement reference derives these ingredients explicitly. Standard normal-tail and time-uniform sub-Gaussian inequalities may be used with a correct statement and verified hypotheses.

The source-local corrections do not change the task: the optimal-index tail comparison is an inequality, the lower selection bound is valid before calendar-time burn-in as well as after it, and the terminal brackets retain floor and ceiling errors. Equivalent correct treatments receive full credit.

Do not demand independence after conditioning on the global good event. Unconditional independent geometric variables combined with pathwise comparisons on that event are sufficient. A lower selection bound must ensure victory against all arms, while an upper selection bound can use a necessary comparison with the optimal arms.

Propagate an earlier gap only when a later conclusion genuinely depends on it. In particular, a pathwise iterated-logarithm bound does not alone justify vanishing optimal-arm perturbations for every allowed inflation sequence, and omission of the log sigma_T contribution can change the claimed suboptimal normalization.
