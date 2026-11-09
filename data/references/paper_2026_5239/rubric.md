# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the estimator under \(u^\top\beta=0\) and derives the centered decomposition into the linear block \(T_1+T_2\) and quadratic block \(T_3\), with all factors of \(n\) and \(1-\alpha\) correct. An equivalent direct per-client decomposition receives the same credit.
- **3 points:** Computes \(\mathbb E\|T_1+T_2\|^2\), including the nonzero Gaussian cross term and its conversion to \(\beta^\top\Sigma_{rx}\), as well as the phase and trace contributions. Supports the calculation using the uniform-phase moments, Gaussian covariance and applicable independence relations.
- **2 points:** Establishes that the cross moment between the two blocks is zero by a valid independence, conditional-expectation or parity argument. The term containing two phase factors must also be justified; zero phase means alone do not eliminate that term. Merely asserting orthogonality without justification is insufficient.
- **3 points:** Derives the centered quadratic Gaussian block moment, correctly obtaining the \((p+1)\tau^4\) and \(\lambda^2\tau^2/2\) contributions, and combines the block moments into exactly the stated variance identity. Derives or correctly applies a stated Gaussian fourth-moment identity with its hypotheses satisfied. In a row-pair expansion, accounts for both the diagonal fourth moments and the nonzero off-diagonal means before centering; an equivalent covariance calculation is equally acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its named blocks, or its particular derivation of the scalar Gaussian fourth moment. Apply the point allocations to the corresponding mathematical obligations in an alternative proof.

The expectation is conditional on fixed data, with the parameters, coefficient vector and modulation direction fixed before the independent internal randomness is sampled. Do not require a stochastic response model, full-rank design, privacy guarantee, noise-calibration formula, coefficient bound or convergence argument.

The proof must cover all admissible data and coefficients, including zero coefficients or residuals, rank-deficient designs, and \(n=1\). No separate case discussion is required when the argument already applies. For \(p=1\), the existing unit-vector orthogonality assumption forces \(\beta=0\); do not require an impossible direction for nonzero \(\beta\), and do not impose \(p\ge2\). The task uses \(0<\alpha<1\), \(\lambda>0\), \(\omega>0\), and \(\tau>0\); extensions outside that source domain are not required.
