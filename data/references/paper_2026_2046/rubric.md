# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly differentiates the softmax-composed functional tensor-network map pointwise by the chain rule, with parameter tangent vectors mapped through the ambient differential of tau and the feature contraction.
- **3 points:** Correctly obtains the Fisher-Rao factor `C(f_x)=D sigma(f_x)^T F(sigma(f_x))D sigma(f_x)` from the pointwise metric. Distinguishes Euclidean transpose in this expression from the Fisher-Rao adjoint of the full output differential. Merely naming Fisher information is insufficient.
- **3 points:** Derives the tensor-product feature factorization of the ambient contraction operator with correct adjoints, dimensions, and class/feature mode order. An entrywise proof, a simple-tensor bilinear-form proof, or an equivalent Kronecker calculation is acceptable.
- **2 points:** Integrates to the population operator, derives the exact empirical average with normalization `1/m`, and correctly states both natural-gradient equations and their minimum-norm pseudoinverse solutions. Justifies consistency: the population objective factors through the output map, and the empirical objective depends on the same sampled outputs as the empirical matrix. Handles singular and zero operators without asserting that every positive-semidefinite system is automatically consistent.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation or ordering. The simplification `C(z)=diag(sigma(z))-sigma(z)sigma(z)^T` is optional; a correct use of the defined Fisher sandwich and pointwise metric suffices. No TTN core expansion, horizontal-space construction, basis-invariance argument, convergence theorem, or sampling-independence argument is required.

Penalize treating the target tensor-product formula as an assumption, counting the Fisher metric twice, omitting the feature factorization, or conflating an intrinsic tangent-space adjoint with an unrestricted ambient coefficient transpose. The empirical operator is exactly the pullback for the averaged sample metric; it is not asserted to equal the population operator.

For pseudoinverses, an argument that the right-hand sides annihilate the relevant differential kernels, followed by the range-kernel identity for a finite-dimensional self-adjoint operator, is sufficient. Minimum norm is measured in the Riemannian metric on the parameter tangent space. If the empirical operator is zero, its gradient is zero and the minimum-norm solution is zero; no nondegeneracy assumption on the sample is allowed.
