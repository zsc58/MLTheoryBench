# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Schatten and singular-coordinate reduction (3 points).** Establish the fixed-product variational identity, including attainment with the prescribed hidden widths, and justify the two-way correspondence of minimizers. Reduce the matrix objective using von Neumann's inequality to the scalar objectives (s_j-x_j)^2+lambda x_j^q, with no additional target-norm constant. Correctly interpret equality as existence of simultaneous ordered SVDs. For the variational identity, a valid product inequality followed by AM-GM and an attaining embedded SVD factorization is sufficient; accept an equally complete alternative derivation. Handle L=1 directly when needed.
2. **Almost-everywhere end-to-end uniqueness (3 points).** Analyze the scalar objective, establish the stated threshold for L>=3, and handle L=1,2 separately. Prove uniqueness away from the tie, justify that optimal coordinates preserve the target's singular-value ordering, and show that the exceptional set is null. Explain why repeated positive target singular values give no matrix ambiguity and why the optimal matrix vanishes on zero target singular-value subspaces. A nonzero determinant polynomial containing the exceptional set, together with the standard null-zero-set fact, is sufficient for the measure argument.
3. **Invariant factor norms (2 points).** Establish equality of layer norms at each minimizer, for example by a product-preserving first variation proving balancedness or by an equivalent scaling or equality argument. Then use uniqueness of the product and equality of objective values to prove that the common norm is independent of the minimizer. The single-layer case is immediate. Merely citing the paper-specific balancedness result without supplying a valid justification does not close this obligation.
4. **Hessian-trace lower bound (2 points).** Derive the diagonal Hessian blocks or an equivalent exact trace expression, with correctly typed identity matrices for empty products. Use P*=A_iW_iB_i, Frobenius submultiplicativity or Cauchy-Schwarz, and the common layer norm to obtain the stated bound. Divide only when g*>0. For g*=0, use the undivided nonnegative-summand trace expression and the task's zero-term convention. Include the depth-one case either through the general calculation or directly.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its exterior-power proof of the singular-value product bound. Standard independent linear-algebra facts may be used with their relevant statements and hypotheses made clear; in particular, no reproving of the standard von Neumann theorem is required. Its equality condition must not be interpreted as agreement of arbitrary preselected SVD bases.

A proof that merely names the variational reduction, scalar threshold analysis, balancing, or a Hessian calculation without establishing the associated theorem-critical implication should not receive the associated points. Source citations to specialized or paper-specific results are not substitutes for those steps. Minor additive-constant slips that are explicitly immaterial to the minimization should be distinguished from invalid reductions, but a fully correct proof should state the objective identity correctly.

Propagate a failed reduction only when later conclusions actually depend on it. Preserve credit for independently valid norm or Hessian arguments. Do not demand a characterization of minimizers on E, a scalar Hessian spectrum, a zero-collapse regularization theorem, or sharpness/equality of the trace bound: these are not targets of this task.

The replacement reference proof closes every listed obligation; there is no unresolved private GT dependency.
