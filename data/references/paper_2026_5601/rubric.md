# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the spectral iterate \(\widehat f_m=(I_n-(I_n-\rho K)^m)r\), including the zero-step case, and expresses the population-minus-empirical evidence difference as a centered Gaussian quadratic form. The argument must respect \(0<1-\rho\lambda_i\leq1\), permit singular kernels, and keep all covariance inverses well-defined.
- **3 points:** Establishes the Gaussian exponential-moment bound and a valid finite-class high-probability bound for the selected horizon, with the stated complexity and confidence terms. A change-of-measure proof must supply its event construction or state an applicable standard result precisely and verify its hypotheses. The temperature used for the point-mass uniform-prior bound is deterministic in the conditional experiment. An equivalent Chernoff-and-union-bound proof earns the same credit. The first conclusion must hold for arbitrary positive-definite \(\Sigma_*\), without imposing alignment.
- **3 points:** Under the aligned model, derives the Bayes estimator and proves the covariance-KL-to-normalized-Bayes-gap transfer with the constant \(4\sigma^2\), including the Gaussian KL/cross-entropy identity and correct KL orientation. Justifies the scalar control used in the transfer. Merely asserting that KL control implies prediction control earns no credit for this step. The risk is computed at each fixed horizon and only then evaluated at the selected index.
- **2 points:** Establishes or precisely states and correctly applies the fixed-comparator Gaussian upper-tail inequality with both its square-root and operator-norm terms, intersects the two events without assuming independence, and derives the displayed bound. Justifies convergence in probability by using fixed confidence levels, the asymptotic assumptions, and the fixed noise scale.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The source candidate domain includes zero. Arguments that automatically cover zero horizons, singleton sets, and nullspaces need not discuss them separately; an unsupported positive-rank or strictly positive-horizon restriction is not a complete proof of the task.

The selected-gap target is the deterministic fixed-horizon risk function evaluated at a random index. It is not \(n^{-1}\mathbb E[\|\widehat f_{\widehat m(r)}(r)-f_{\rm B}(r)\|^2\mid K]\), and a proof must not interchange these quantities.

The finite-class event may depend on the fixed confidence level and deterministic temperature. Do not accept optimization of a fixed-temperature event over arbitrary data-dependent temperatures without an additional valid uniform argument. For the stated uniform-prior point-mass problem, choosing the displayed deterministic temperature in advance resolves this issue completely.

A standard Gaussian conditioning or quadratic-form concentration result may be used without reproving it if its relevant statement and hypotheses are explicit and its application is correct. A bare citation to a paper-specific transfer lemma is not a substitute for the transfer argument requested here.

The probability statement is for each dimension. Do not require, or infer, an almost-sure conclusion or a common event across all dimensions. There are no unresolved reference-proof obligations.
