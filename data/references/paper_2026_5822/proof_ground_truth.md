# Reference Proof

## Proof Obligations

1. Verify that the Gaussian suprema are measurable and integrable, establish the elementary width properties used below, and handle zero-width sets.
2. Prove commuting-metric log-convexity using a comparison of square-root operators, the audited Gaussian increment comparison theorem, and an explicit endpoint-width optimization.
3. Specialize to the reciprocal pair at the midpoint and obtain the claimed product inequality.
4. Exhibit equality with positive width to establish optimality of the universal constant.

## Standard-Independent Comparison Result

The relevant part of theory_022 is the finite-index Sudakov–Fernique comparison theorem: if \((X_i)_{i=1}^m\) and \((Y_i)_{i=1}^m\) are centered Gaussian vectors and
\[
\mathbb E(X_i-X_j)^2\leq\mathbb E(Y_i-Y_j)^2
\quad\text{for every }i,j,
\]
then
\[
\mathbb E\max_{1\leq i\leq m}X_i\leq\mathbb E\max_{1\leq i\leq m}Y_i.
\]
No equality of pointwise variances is required. The source invokes this increment comparison at L000095–L000102 and L000426–L000431. Below, its extension to our compact index set is justified directly by finite approximation and dominated convergence. No paper-specific result is treated as an unproved external theorem.

## Complete Proof

### 1. Well-definedness and degenerate cases

For a fixed matrix \(M\), the function \(t\mapsto\langle g,Mt\rangle\) is continuous on \(T\). Choose a countable dense subset \(D\subset T\). Its supremum equals the supremum over \(T\), so this supremum is measurable. If \(R=\sup_{t\in T}\|t\|_2\), then
\[
\sup_{t\in T}|\langle g,Mt\rangle|
\leq R\|M\|_{\mathrm{op}}\|g\|_2,
\qquad
\mathbb E\|g\|_2\leq\sqrt d.
\]
Thus all Gaussian suprema used below are integrable. The corresponding processes are centered and have continuous sample paths on a separable index set.

For any fixed \(t_0\in T\), the supremum is at least \(\langle g,Mt_0\rangle\), whose expectation is zero. Consequently all widths under consideration are nonnegative. Translation invariance and nonnegative homogeneity follow directly from
\[
\sup_{t\in T}\langle g,M(t+a)\rangle
=\sup_{t\in T}\langle g,Mt\rangle+\langle g,Ma\rangle
\]
and from pulling a nonnegative scalar outside the supremum.

If \(T\) is a singleton, every weighted width is zero and the product inequality is immediate. Conversely, if \(u,v\in T\) are distinct and \(A\) is positive definite, let \(U=\langle g,A^{1/2}u\rangle\) and \(V=\langle g,A^{1/2}v\rangle\). Then
\[
w_A(T)\geq\mathbb E\max(U,V)
=\frac12\mathbb E|U-V|>0.
\]
The last inequality holds because \(U-V\) is a centered Gaussian with strictly positive variance \(\|A^{1/2}(u-v)\|_2^2\). Hence every positive-definite weighted width is strictly positive when \(T\) is not a singleton.

### 2. Commuting interpolation

Let \(A,B\) be commuting symmetric positive-definite matrices, and define
\[
C_\theta=A^{1-\theta}B^\theta.
\]
Matrix powers are defined spectrally. At \(\theta=0,1\), the interpolation assertion is simply equality at the corresponding endpoint. Singleton sets have already been handled, so assume \(T\) has at least two points and \(0<\theta<1\).

Put
\[
H_0=A^{1/2},\qquad H_1=B^{1/2},\qquad
H_\theta=C_\theta^{1/2}=H_0^{1-\theta}H_1^\theta.
\]
The last identity follows by simultaneous orthogonal diagonalization of the commuting symmetric matrices. For \(r>0\), set
\[
L_r=(1-\theta)rH_0+\theta r^{-(1-\theta)/\theta}H_1.
\]
In the common eigenbasis, let \(h_{0i},h_{1i}>0\) be the eigenvalues of \(H_0,H_1\). Weighted AM-GM gives
\[
(1-\theta)r h_{0i}+\theta r^{-(1-\theta)/\theta}h_{1i}
\geq (r h_{0i})^{1-\theta}
\bigl(r^{-(1-\theta)/\theta}h_{1i}\bigr)^\theta
=h_{0i}^{1-\theta}h_{1i}^\theta.
\]
These are positive coordinatewise inequalities in the same eigenbasis. Squaring them therefore gives, for every \(h\in\mathbb R^d\),
\[
\|L_rh\|_2^2\geq\|H_\theta h\|_2^2.
\]
This squaring is justified by simultaneous diagonalization, not by a general assertion that matrix squaring preserves positive-semidefinite order.

Define the centered Gaussian processes
\[
X_t=\langle g,H_\theta t\rangle,
\qquad
Y_t=\langle g,L_rt\rangle,
\qquad t\in T.
\]
For \(s,t\in T\),
\[
\mathbb E(X_s-X_t)^2
=\|H_\theta(s-t)\|_2^2
\leq\|L_r(s-t)\|_2^2
=\mathbb E(Y_s-Y_t)^2.
\]
Apply the stated finite-index comparison to increasing finite subsets of a countable dense subset of \(T\). Continuity identifies the limiting suprema with those over \(T\), and the integrable bounds from Step 1 justify passing expectations to the limit by dominated convergence. Thus
\[
w_{C_\theta}(T)\leq\mathbb E\sup_{t\in T}Y_t.
\]
Crucially, the endpoint terms in \(Y_t\) use the same Gaussian vector:
\[
Y_t=(1-\theta)r\langle g,H_0t\rangle
+\theta r^{-(1-\theta)/\theta}\langle g,H_1t\rangle.
\]
Pointwise subadditivity of the supremum, followed by expectation, gives
\[
w_{C_\theta}(T)
\leq(1-\theta)r\,w_A(T)
+\theta r^{-(1-\theta)/\theta}w_B(T).
\]
Let \(a=w_A(T)>0\) and \(b=w_B(T)>0\). Choose
\[
r=(b/a)^\theta.
\]
Both rescaled endpoint quantities then equal \(a^{1-\theta}b^\theta\), and the bound becomes
\[
w_{A^{1-\theta}B^\theta}(T)
\leq w_A(T)^{1-\theta}w_B(T)^\theta.
\]
This choice also minimizes the displayed endpoint bound: weighted AM-GM bounds it below by \(a^{1-\theta}b^\theta\), with equality at the chosen \(r\). This proves the interpolation statement, including the previously separated endpoint and singleton cases without division by zero or reliance on an undefined \(0^0\).

### 3. Reciprocal midpoint

Take \(A=G\), \(B=G^{-1}\), and \(\theta=1/2\). The matrices commute, and spectral calculus gives
\[
A^{1/2}B^{1/2}=G^{1/2}G^{-1/2}=I_d.
\]
The interpolation inequality yields
\[
w(T)=w_{I_d}(T)
\leq\sqrt{w_G(T)w_{G^{-1}}(T)}.
\]
All quantities are nonnegative, so squaring gives
\[
w_G(T)w_{G^{-1}}(T)\geq w(T)^2.
\]

### 4. Sharpness

For every \(\lambda>0\), let \(G=\lambda I_d\). Homogeneity gives
\[
w_G(T)=\sqrt\lambda\,w(T),
\qquad
w_{G^{-1}}(T)=\lambda^{-1/2}w(T).
\]
Their product is exactly \(w(T)^2\). To verify optimality rather than only a zero-width equality, take \(T=\{-e_1,e_1\}\), where \(e_1\) is the first coordinate vector. Then \(w(T)=\mathbb E|g_1|>0\). Thus no universal constant larger than one can replace one on the right-hand side. Singleton sets also satisfy equality, but are not needed to establish optimality.

## Audit Closure

All four obligations are closed. Step 2 reconstructs the source argument at L000417–L000437; Step 3 is its reciprocal midpoint specialization at L000443–L000466; Step 4 uses the scalar family at L000467–L000470. The former independent-endpoint covariance interpolation is not used: coefficients in a covariance sum become square roots in an independent-process sum and cannot directly supply the required linear endpoint-width bound. No unresolved proof dependency remains.
