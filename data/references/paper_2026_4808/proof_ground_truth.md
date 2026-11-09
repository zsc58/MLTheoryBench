# Reference Proof

## Proof Obligations

1. Identify the restricted native-space smoothness using the standard restriction result, and explain the scope of the intrinsic fill-distance interpolation guarantee.
2. Use the explicit H^1 reconstruction premise and the bounded linear target operator.
3. Expand the section error, apply the uniform guarantee, and identify the permitted constant dependencies.

## Standard Background and Reconstruction Accuracy

The standard trace/restriction result used here is the following: if a kernel on R^d has native space norm-equivalent to H^s(R^d), and M is a smooth compact embedded m-dimensional manifold in the stated regime t=s-(d-m)/2>m/2, then its restricted kernel has native space norm-equivalent to H^t(M). This is standard independent background recorded in theory_004 and reported in the source's restriction discussion. The public hypotheses explicitly provide the ambient norm equivalence, manifold setting, and smoothness inequality, so this result applies with t=\widetilde s. Positive definiteness alone would not identify a Sobolev order.

For precision, the quantitative manifold interpolation result reported in the source has an additional spectral hypothesis. Suppose k(x,y)=Phi(x-y), with a fixed shape parameter absorbed into Phi, where Phi is continuous and integrable and there are constants a,b>0 such that
\[
a(1+\|\omega\|^2)^{-s}\le \widehat\Phi(\omega)\le b(1+\|\omega\|^2)^{-s}.
\]
For an integer order mu in the range 0<=mu<=ceil(\widetilde s)-1, its statement gives constants C>0 and h_M>0 such that, whenever h_{X,M}<=h_M, the restricted-kernel interpolant s_f satisfies
\[
\|f-s_f\|_{H^\mu(M)}\le C h_{X,M}^{\widetilde s-\mu}\|f\|_{H_{k_M}(M)}.
\]
The constants are for the fixed manifold, kernel, and smoothness/order parameters, not for a particular f or node set. This is the audited standard independent interpolation result in theory_004. Its spectral hypothesis is not assumed for every kernel in the public operator-extension problem, so this particular result is used to explain reconstruction rates within its stated class, not asserted to apply unconditionally to every public instance.

In that class, taking mu=1 is permitted precisely when ceil(\widetilde s)>=2, equivalently \widetilde s>1. The estimate then reads
\[
\|f-s_f\|_{H^1(M)}\le C h_{X,M}^{\widetilde s-1}\|f\|_{H_{k_M}(M)}.
\]
Thus smaller intrinsic fill distance provides a smaller reconstruction-error bound, and the codimension loss reduces the exponent available for derivative approximation. For f nonzero, choosing sufficiently small h_{X,M} makes this upper bound less than any prescribed positive tolerance. For f=0, the zero interpolant has zero error, so no division by its native-space norm is needed. Intrinsic fill distance measures coverage on the manifold; a node set missing a connected component does not have small intrinsic fill distance.

The public assumptions allow \widetilde s<=1 in low dimensions. The cited estimate then does not supply an H^1 reconstruction guarantee. Also, g is an arbitrary chosen expansion satisfying the explicit reconstruction premise, not necessarily the interpolant s_f. Neither the spectral hypothesis nor the stronger condition \widetilde s>1 is needed below. The discussion of interpolation must not replace the given reconstruction premise by an unsupported universal availability claim.

## Extension-Error Estimate

Write q_i=k_M(\cdot,x_i). All q_i and learned section outputs belong to H^1(M) by the stated domain conditions. Hence g, T[g], and the finite extended output belong to H^1(M).

By definition,
\[
\mathcal N^e_\theta[g]=\sum_{i=1}^n\alpha_i\mathcal N_\theta[q_i].
\]
Insert and subtract T[g]. The triangle inequality and linearity give
\[
\|\mathcal N^e_\theta[g]-T[f]\|_{H^1(M)}
\le \|\mathcal N^e_\theta[g]-T[g]\|_{H^1(M)}+\|T[g-f]\|_{H^1(M)}.
\]
Boundedness of T and the reconstruction assumption imply
\[
\|T[g-f]\|_{H^1(M)}\le \|T\|_{H^1(M)\to H^1(M)}\,\varepsilon.
\]
Linearity of T, the extension definition, and the section guarantee at the nodes imply
\[
\begin{aligned}
\|\mathcal N^e_\theta[g]-T[g]\|_{H^1(M)}
&=\left\|\sum_{i=1}^n\alpha_i\bigl(\mathcal N_\theta[q_i]-T[q_i]\bigr)\right\|_{H^1(M)}\\
&\le\sum_{i=1}^n|\alpha_i|\,\|\mathcal N_\theta[q_i]-T[q_i]\|_{H^1(M)}\\
&\le\delta\sum_{i=1}^n|\alpha_i|.
\end{aligned}
\]
The learned operator itself need not be linear: only its values on the sections and the defined finite linear combination are used.

Consequently, the choices
\[
C_1=\|T\|_{H^1(M)\to H^1(M)},\qquad C_2=\sum_{i=1}^n|\alpha_i|
\]
give
\[
\|\mathcal N^e_\theta[g]-T[f]\|_{H^1(M)}\le C_1\varepsilon+C_2\delta.
\]
These nonnegative constants depend only on T and the fixed expansion, respectively, not on the tolerances or the learned section outputs. Non-strict inequalities remain valid when T=0 or all coefficients vanish. If different expansions are selected as epsilon changes, their values of C2 may change or grow; no uniform-in-expansion bound or automatic two-parameter convergence follows without further control.

## Source-Repair Accounting

The existing repair of theory_002 is retained. The explicit reconstruction assumption closes the estimate even where the source's attempted use of the interpolation theorem at mu=1 is inadmissible. The interpolation explanation above also checks its spectral hypothesis rather than silently adding it to the operator-extension theorem. No theorem-critical proof obligation remains unresolved.
