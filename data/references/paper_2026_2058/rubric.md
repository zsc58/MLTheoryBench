# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives honest-gradient and honest-momentum dispersion control, aggregation-error control, and a momentum-bias recursion from the conditional oracle, dissimilarity, smoothness, and all-input robustness assumptions. Conditioning and variance factors must be valid.
- **3 points:** Gives a valid Lyapunov or alternative argument for the exact nonconvex inequality. Accounts for stochastic first-round initialization, verifies coefficient bounds under the stepsize and momentum restrictions, and telescopes to the stated constants and heterogeneity floor. The uncorrected claim that the source's original potential has initial value at most 9Delta_0/4 is not valid for a general stochastic first oracle call.
- **2 points:** Proves the exact PL inequality for the specified two-phase schedule, including its initial-gap coefficient, the other three terms, integer horizons, and the constant-objective case. A scalar recursion alone is insufficient unless its initial value and resulting numerical coefficients are justified.
- **3 points:** Constructs valid two-worker quadratic instances and aggregators that satisfy robustness on all input pairs and work for both algorithm variants and the stated schedule families. Establishes a universal positive lower-bound constant uniformly over kappa B^2<1, with the required mu scaling and zero-parameter cases. A stationary construction is acceptable; convergence to a drifted minimizer need not be proved if the constructed trajectory is verified directly.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's potential, parameterization, or presentation. Intermediate constants and inequalities may differ, but the explicit public upper inequalities and schedules must follow as stated; asymptotically equivalent bounds or a different schedule alone do not prove these targets. For the lower bounds any positive universal constant is acceptable.

The lower instance and aggregator must be fixed independently of the horizon and subsequent schedule choice. The robustness condition is an all-input condition, not only a trajectory condition. Merely writing an aggregation formula in terms of an unspecified current point or historical iterates does not verify that condition.

The fixed choice delta=sqrt(3)Bmu/2 and epsilon=G/2, without a further argument or different construction, does not establish a uniform lower bound of order kappa G^2/(1-kappa B^2) throughout kappa B^2<1. Constants depending on kappa B^2 do not meet the universal-constant requirement.

A bare appeal to classical momentum convergence does not close a schedule-dependent lower-bound argument. Either derive the needed convergence with verified parameter hypotheses, or verify another valid trajectory, including a stationary one.

Treat omission of the PL upper bound or either algorithmic lower-bound variant as a major gap. Minor endpoint omissions may receive partial credit when the main proof is valid, but a full-credit solution must cover all stated cases.
