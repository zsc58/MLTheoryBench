# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **First-order perturbation and differentiation (2 points):** Correctly derives \(W'(0)=W_0P^TEP\) from the orthogonal path and obtains the loss directional derivative from differentiability of \(L\) at \(W_0\).
2. **Skew-gradient identification (3 points):** Uses trace cyclicity and orthogonality of symmetric and skew-symmetric parts to prove that the derivative equals \(\langle PFP^T,E\rangle_F\), identifying the Frobenius first-variation gradient and its squared norm. The normalization must match the Frobenius metric on \(\operatorname{Skew}(r)\).
3. **Sharp spectral compression bound (3 points):** Applies or proves a valid compression inequality, verifies its applicability to a row-orthonormal compression, accounts for the duplicated singular values of a real skew-symmetric matrix, and derives \(2\sum_{j=1}^{\lfloor r/2\rfloor}\mu_j^2\). The argument must remain valid with zero padding, repeated magnitudes, and odd \(r\).
4. **Attainment by an optimal support (2 points):** Chooses the leading \(\min\{q,\lfloor r/2\rfloor\}\) nonzero invariant planes and verifies that orthogonal completion to dimension \(r\) attains equality. The verification must cover both the one-direction odd-r extension when enough pairs exist and the additional completion directions needed when the positive spectrum is exhausted.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

A standard singular-value min-max or Hermitian compression theorem may be used without reproving it, provided its relevant implication and hypotheses are correctly applied. Merely naming a variational principle without establishing the required bound does not earn the spectral-bound points.

An argument that does not cover odd \(r\) has a theorem-critical omission. A separate odd-r paragraph is not required if a unified argument covers it. Likewise, zero matrices, rank deficiency, ties, \(r=1\), \(d=1\), and \(r=d\) may be covered by a general argument rather than individual case discussions.

Do not require full invariance of an attaining odd-dimensional support: the additional single direction can lie anywhere in the orthogonal complement of the selected invariant planes. Do not impose nonzero-gradient, full-rank, or simple-spectrum assumptions.

The requested gradient is the Frobenius representative of the stated first variation. Do not require joint differentiability of a parameterization not assumed in the task, and do not accept an unexplained factor-of-two change arising from a different coordinate metric.
