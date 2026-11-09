# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Distributional identifiability.** Correctly characterizes union-DAG sources by variance one versus strictly larger variance, recursively obtains a common topological order by conditioning identified sources to zero, and uses the conditional linear mean and quadratic variance to identify every entry of both parameter matrices. Justifies the conditional-law interpretation at zero, for example through the continuous positive densities supplied by the model. Merely asserting generic DAG identifiability does not earn this step.
- **2 points: Population and parameter consistency.** Establishes the cluster likelihood/KL identity on the DAG-feasible set and unique population minimization through identifiability. Justifies finite observation moments and uniform empirical-loss and Hessian convergence on compact subsets of the ambient nonnegative-variance domain. Derives local strong convexity by a segment argument in that ambient domain, consistency of every global penalized minimizer, and absence of false negatives from fixed positive minimum signals. A correct compact-class uniform-LLN theorem with verified hypotheses is sufficient; the reference proof's finite-net derivation is not mandatory.
- **3 points: Restricted expansion and feasible inactive control.** Constructs the true-support restricted estimator and derives its active first-order equations. Justifies zero active population gradient and finite-variance centered score fluctuations, then obtains \(\widetilde\theta_T-\theta_{0,T}=-\lambda_{1m}H_{TT}^{-1}(s_A,r_m\mathbf1)^{\mathsf T}+o_p(\lambda_{1m})\). For inactive coordinates whose addition preserves acyclicity, derives strict two-sided fixed-effect and one-sided nonnegative-variance inequalities using the respective irrepresentability assumptions. For fixed coordinates, two-sided feasible optimality gives zero population derivative. For variance coordinates, it suffices to retain a nonnegative population right derivative plus centered sampling error. Naming a support-recovery method without these derivations is insufficient.
- **2 points: Exact support recovery.** Uses the no-false-negative event and feasibility to eliminate inactive coordinates whose addition creates a cycle. Compares an arbitrary unrestricted global minimizer to the restricted estimator using local strong convexity, the penalty subgradient inequality, active first-order equations, and strict inequalities on the remaining inactive coordinates. Shows that global optimality forces equality and therefore no false positives in either component graph.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular notation for the acyclicity-preserving inactive sets. Do not withhold a downstream point when its required conclusion has been established independently by another valid argument.

The ambient loss formula is not a normalized likelihood for arbitrary cyclic parameter matrices. It is therefore incorrect to infer that every coordinate of its gradient at the truth has mean zero. In particular, cycle-creating fixed-coordinate population derivatives can be nonzero. Such coordinates need no strict-dual inequality because feasibility excludes their activation once all true edges are retained. A proof relying on universal ambient score centering must repair this distinction before earning full credit for inactive control.

At zero variance coordinates, population minimization directly provides a nonnegative right derivative, not necessarily a zero derivative. Accept a stronger zero-derivative claim only if it is independently justified for the coordinates used. The nonnegative-derivative argument in the reference proof suffices.

The observations are generally not jointly Gaussian after integrating out random coefficients. Their finite moments follow from the finite polynomial representation furnished by acyclicity. A valid proof may use that fact without reproducing every polynomial-envelope calculation.

The variance-one recursion and simultaneous control of fixed and nonnegative random coordinates are core mechanisms of the reference route, but another complete identification or support-recovery argument is acceptable. A proof establishing only parameter consistency, without exact recovery, cannot receive the last five points. No specialized external support-recovery theorem is presumed applicable without its statement and hypotheses being verified.
