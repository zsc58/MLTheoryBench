# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Calibration and softmax margin reduction (2 points):** Derives the ECE-to-mean-gap inequality, bounds the gap by $1-p_Y$, and proves the exponential upper bound and the nonnegative-margin lower bound in terms of the true margin. Handles nonempty bins correctly; zero-probability and empty bins contribute nothing.
2. **Population robust-tail bounds (3 points):** Uses the feasibility of the zero perturbation to compare the clean and robust exponential moments and proves both population ECE and Gauss–Newton top-eigenvalue upper bounds. Supplies a valid logit-Hessian spectral argument, Jacobian composition bound, and expectation comparison. The bounded Jacobian makes the matrix expectation finite even when an exponential moment is infinite.
3. **Interpolating empirical ECE equivalence and two-sided control (3 points):** Uses strictly positive sample margins to establish correct classification, identifies empirical ECE with mean true-class misconfidence, and proves $K^{-1}Q_D\le\operatorname{ECE}_M\le(K-1)Q_D\le(K-1)e^{-\gamma}$.
4. **Empirical curvature coupling (2 points):** Under the sample Jacobian bound, proves the requested Gauss–Newton upper bound by $Q_D$ and the resulting curvature–ECE inequality. Obtains the divided lower bound only when $C_J>0$, retaining the undivided bounds at $C_J=0$.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, a particular spectral theorem name, or a particular sequence of intermediate estimates. Award partial credit for independently correct inequalities even if another dependent step is missing; theorem-critical unsupported conclusions receive the corresponding deduction.

The dataset is arbitrary and nonempty, not necessarily sampled from the population distribution or sampled independently. The population claim requires no separability assumption, and the selected robust comparison requires no input-Lipschitz condition. Do not require optimization dynamics, asymptotic margin growth, or a Jacobian bound uniform over parameters.

Population exponential moments may be infinite. A proof must not impose their finiteness as an additional theorem hypothesis. At $C_J=0$, the Jacobian bound forces the relevant Gauss–Newton matrix to vanish; the stated nonnegative-product convention governs infinite moments, and division by $C_J^2$ is not permitted. Population ties are allowed under the fixed tie rule, whereas the strictly positive empirical margins eliminate ties. Concise arguments covering these cases are sufficient; redundant case-by-case exposition is not required.
