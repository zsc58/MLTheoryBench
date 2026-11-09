# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Update and preliminary bounds (2 points).** Handles zero-coordinate KKT multipliers correctly; establishes the value/suboptimal-mass comparison, monotone value improvement and value convergence; and derives both dual-gap recurrences and post-entrance persistence. A citation to a PMD-specific convergence theorem alone does not close this step.
2. **Summability and policy convergence (3 points).** Obtains the per-state gap growth and inverse-boundary summability, then proves full policy convergence by controlling optimal-action dual scores and Bregman distances. Includes the correct interior-domain conclusion at multiple-optimal states.
3. **Finite-time branch (2 points).** Bounds dual scores at multiple-optimal states, proves finite absorption of their suboptimal masses, and establishes stationarity once the policy is optimal.
4. **Unique-optimal branch (3 points).** Rules out finite termination and proves both eventual value-error bounds with the correct $\chi$, slopes, constants, and inverse-domain conditions.

# Evaluator Notes

Accept any complete valid alternative proof, including one that derives value convergence differently. Do not discard nonnegative simplex multipliers at zero coordinates. Do not require strict positivity of an optimal coordinate at a multiple-optimal state: $0$ may belong to $\operatorname{int}(\operatorname{dom}\psi)$. The argument must cover $\gamma=0$ and states where every action is optimal.
