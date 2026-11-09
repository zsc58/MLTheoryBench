# Reference Proof

## Proof Structure

Use the heat-kernel semigroup to express each normalized overlap as a normalized inner product of heat-smoothed kernel sections. Positivity and Cauchy-Schwarz give the similarity bounds and hence the effective-size inequalities. Grouping equal locations proves duplicate-label invariance. Explicit standard Gaussian upper and diagonal lower estimates make normalized overlaps between distinct fixed support points vanish at small time. At large time, mean-zero spectral contraction combined with the semigroup identity gives uniform heat-kernel convergence to the constant density. A connected zero-dimensional manifold is handled directly.

## Audited Standard Inputs

For a compact smooth Riemannian manifold without boundary, the heat kernel is smooth for positive time. In the present connected setting it is symmetric and strictly positive, and satisfies the normalized-volume semigroup identity given in the task. Consequently each section k_t(x,.) belongs to L^2(nu).

For positive dimension, the standard compact-manifold Gaussian upper and diagonal lower bounds invoked in the source have the following sufficient form: there are constants s_0,c,C>0, depending only on M and its normalized-volume convention, such that for all 0<s<=s_0 and all x,y in M,
\[
k_s(x,y)\le C s^{-m/2}\exp\!\left(-\frac{d_g(x,y)^2}{Cs}\right),\qquad
k_s(x,x)\ge c s^{-m/2}.
\]
Here d_g is geodesic distance. Compactness supplies uniform constants, and normalization by volume changes only the multiplicative constants.

The standard spectral input is that on a compact connected positive-dimensional manifold without boundary, -Delta has a positive first nonconstant eigenvalue lambda_1, with constants as its zero eigenspace. If H_u denotes the heat semigroup acting on functions, its spectral representation therefore gives
\[
\|H_u f\|_{L^2(\nu)}\le e^{-\lambda_1u}\|f\|_{L^2(\nu)}
\]
for every mean-zero f in L^2(nu) and every u>=0. The manifold, normalization, and sign convention in the task satisfy all hypotheses of these standard independent results. No paper-specific prior theorem is needed.

## Complete Proof

The normalization of the weights implies n>=1, at least one w_i is positive, and sum_i w_i^2>0. For t>0 put
\[
D_t=\sum_{i,j=1}^n w_iw_j s_t(x_i,x_j),\qquad gESS_w(t)=D_t^{-1}.
\]
Strict positivity makes the diagonal heat-kernel values and the denominator defining s_t positive. Symmetry and the semigroup identity give
\[
k_{2t}(x,y)=\int_M k_t(x,z)k_t(y,z)\,d\nu(z)
=\langle k_t(x,\cdot),k_t(y,\cdot)\rangle_{L^2(\nu)}.
\]
Cauchy-Schwarz yields
\[
k_{2t}(x,y)^2\le k_{2t}(x,x)k_{2t}(y,y).
\]
Thus 0<s_t(x,y)<=1 and s_t(x,x)=1. Since the weights are nonnegative,
\[
\sum_i w_i^2\le D_t\le\sum_{i,j}w_iw_j=1.
\]
In particular D_t>0, so taking reciprocals proves
\[
1\le gESS_w(t)\le\left(\sum_i w_i^2\right)^{-1}=ESS(w).
\]

Partition the labels into equal-location classes I_a, with common locations z_a, and set
\[
\alpha_a=\sum_{i\in I_a}w_i.
\]
Every term with i in I_a and j in I_b has similarity s_t(z_a,z_b). Therefore
\[
D_t=\sum_{a,b}\alpha_a\alpha_b s_t(z_a,z_b).
\]
This is exactly the denominator of the merged representation. It proves invariance under merging any equal-location classes, and also under the inverse operation of splitting their weights among duplicate labels. Zero-mass classes can be retained or discarded without changing any sum. The merged masses are nonnegative and sum to one, so sum_a alpha_a^2>0.

If m=0, compactness and connectedness make M a single point. Its normalized heat kernel is identically one. Consequently every similarity and D_t equal one, gESS_w(t)=1 for every t, and the sole merged mass is one. Both claimed limits follow. Hence assume m>0 for the remaining limit arguments.

For distinct fixed locations z_a and z_b, apply the stated estimates with s=2t. For sufficiently small t,
\[
0<s_t(z_a,z_b)
\le\frac{C}{c}\exp\!\left(-\frac{d_g(z_a,z_b)^2}{2Ct}\right).
\]
Their distance is strictly positive, so this upper bound tends to zero. The diagonal similarities remain identically one. The configuration is fixed and finite; therefore termwise convergence in the merged denominator gives
\[
D_t\longrightarrow\sum_a\alpha_a^2>0\qquad(t\downarrow0).
\]
Continuity of reciprocation on positive numbers proves
\[
\lim_{t\downarrow0}gESS_w(t)=\left(\sum_a\alpha_a^2\right)^{-1}.
\]
When all original locations are distinct, the classes are singletons and this equals ESS(w), including when some original weights vanish. If there is only one positive-mass location, the same argument has no nonzero off-diagonal contribution and the limit is one.

For completeness, derive the uniform large-time heat-kernel convergence from the stated spectral input. Fix a smoothing time a>0 and define
\[
f_x(z)=k_a(x,z)-1.
\]
Normalization makes f_x mean-zero, and the semigroup identity gives
\[
\|f_x\|_2^2=k_{2a}(x,x)-1.
\]
Smoothness and compactness imply
\[
B_a:=\sup_{x\in M}\|f_x\|_2<\infty.
\]
Applying the semigroup identity twice and using symmetry and normalization, for u>=0 one obtains
\[
k_{u+2a}(x,y)-1=\langle f_x,H_u f_y\rangle_{L^2(\nu)}.
\]
For u=0 the identity is interpreted using H_0 as the identity operator. Cauchy-Schwarz and mean-zero spectral contraction imply
\[
\sup_{x,y\in M}|k_{u+2a}(x,y)-1|
\le B_a^2e^{-\lambda_1u}\longrightarrow0.
\]
Taking u=2t-2a for t>=a proves uniform convergence k_{2t}(x,y)->1. In particular the diagonal terms tend uniformly to one and are bounded away from zero for large t. Hence s_t(x,y)->1 uniformly, and the finite weighted denominator satisfies
\[
D_t\longrightarrow\sum_{i,j}w_iw_j=1.
\]
Taking reciprocals proves lim_{t->infinity}gESS_w(t)=1.

## Obligation Closure

The heat-kernel normalization, positive diagonal values, L^2 typing, similarity bounds, and positive gESS denominator are justified above. Duplicate invariance is proved by finite regrouping. The small-time limit follows from explicitly stated standard estimates applied to fixed distinct points, followed by a finite sum and a positive reciprocal limit. The large-time limit follows from the explicitly stated standard spectral contraction and the displayed semigroup argument. Zero weights, a single positive-mass location, and the zero-dimensional connected case are covered. No unresolved theorem-critical obligation remains.
