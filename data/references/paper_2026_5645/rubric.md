# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes $L^*\succeq0$ under the stated singular-value conditions, including zero incidence matrices. The reference route expands the quadratic form and applies an SVD to each adjacent-rank contribution. Infers $C\succeq0$, which also justifies the inverse $C+\epsilon I$ for every $\epsilon>0$.
- **3 points:** Proves $\ker(C)\subseteq\ker(X)$. In the reference route, uses the nonnegative decomposition and correctly treats $\beta_1>0$, $\beta_1=0$ with $B_1\ne0$, and $B_1=0$. Uses the full, correctly sized coupling matrix, or its action on higher-rank vectors. A complete general PSD block-matrix argument earns the same credit without these route-specific cases.
- **3 points:** Removes the kernel contribution from the regularized inverse and derives the explicit operator-norm bound $\epsilon\|X\|_2^2/[\lambda_+(\lambda_++\epsilon)]$. In the spectral route, justifies the orthogonal decomposition and bounds the largest surviving coefficient.
- **2 points:** Correctly handles the no-positive-eigenvalue case, proves convergence as $\epsilon\downarrow0$, and identifies the nonsingular specialization with the ordinary Schur complement. The argument also covers an empty higher-rank space, including $K=0$, without invoking undefined first-higher-rank coordinates or weights.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, kernel annihilation can be derived from positive semidefiniteness of the full block matrix rather than from the individual adjacent-rank terms. An empty-space case may be handled explicitly or by an argument whose maps and formulas remain well-defined on the zero space. Do not award or withhold points merely for naming a particular method. A proof that merely names PSD, kernel inclusion, or spectral comparison without deriving or validly justifying the corresponding claims should not receive credit for those steps. The zero-incidence convention imposes no additional restriction on the corresponding coupling weight. Do not require $C$ to be positive definite, require strictly positive weights, or exclude equality in the singular-value conditions.
