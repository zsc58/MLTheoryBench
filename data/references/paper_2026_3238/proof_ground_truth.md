# Reference Proof

## Proof Structure

Compare each candidate with the true coordinates through a relative orthogonal matrix. Independent optimal couplings from standard Gaussians to the sources give a weighted Wasserstein upper bound for each unit mixture. Summing these bounds gives a global upper bound. Equality for a mixture with at least two nonzero coefficients would make the induced Gaussian-to-mixture coupling optimal. Uniqueness of that coupling gives an almost-everywhere functional equation. Fubini's theorem reduces it to a two-variable Pexider equation, whose measurable solutions are affine almost everywhere. Two participating sources would therefore be Gaussian, a contradiction. The global equality cases are exactly signed permutations.

## Standard Independent Results Used

1. **One-dimensional quadratic optimal transport (theory_016).** If both probability measures have finite second moments and the first is absolutely continuous with respect to Lebesgue measure, the quadratic optimal coupling exists, is unique, and is induced by a measurable monotone map from the first measure to the second. In particular, for every probability law \(\nu\in\mathcal P_2(\mathbb R)\), there is a measurable map \(T\) such that \(T_\#\gamma=\nu\), and the unique optimal coupling with marginals \(\gamma,\nu\) is the law of \((Z,T(Z))\) for \(Z\sim\gamma\).
2. **Almost-everywhere measurable Pexider theorem (theory_027).** If measurable real-valued functions \(f,g,h\) satisfy \(f(x+y)=g(x)+h(y)\) for Lebesgue-almost every \((x,y)\in\mathbb R^2\), then there exist real constants \(a,b,c\) such that \(g(x)=ax+b\), \(h(y)=ay+c\), and \(f(t)=at+b+c\) almost everywhere. This is the independent functional-equation result explicitly invoked in the source, not an assumption on the ICA model.

## Complete Proof

Write \(\gamma=N(0,1)\) and
\[
c_k=W_2^2(\mathcal L(S_k),\gamma).
\]
These numbers are finite because both marginals have finite second moments. For any \(W\in O_d\), put
\[
A=W(W^*)^{-1}\in O_d,
\]
and denote its rows by \(a_j^\top\). Then \((WX)_j=a_j^\top S\).

### Product-coupling bound

Choose independent standard Gaussians \(Z_1,\ldots,Z_d\). By the optimal-transport result, for each \(k\) there is a measurable map \(T_k\) with \((T_k)_\#\gamma=\mathcal L(S_k)\) and
\[
\mathbb E[(T_k(Z_k)-Z_k)^2]=c_k.
\]
Its hypotheses hold because \(\gamma\) is absolutely continuous and both \(\gamma\) and \(\mathcal L(S_k)\) have finite second moments. The variables \(T_k(Z_k)\) are independent and thus have the same joint law as the independent sources.

For any unit vector \(\alpha\), set
\[
Y=\sum_k\alpha_kT_k(Z_k),\qquad G=\sum_k\alpha_kZ_k.
\]
Then \(G\sim\gamma\), and \(Y\) has the law of \(\sum_k\alpha_kS_k\). The differences \(T_k(Z_k)-Z_k\) are independent and centered. Expanding the square therefore gives
\[
\mathbb E[(Y-G)^2]=\sum_k\alpha_k^2c_k.
\]
Consequently,
\[
W_2^2\!\left(\mathcal L\left(\sum_k\alpha_kS_k\right),\gamma\right)
\leq\sum_k\alpha_k^2c_k. \tag{1}
\]
For every row of \(A\), apply (1), then sum and use the unit norm of each column:
\[
F(W)\leq\sum_{j,k}a_{jk}^2c_k
=\sum_kc_k\sum_ja_{jk}^2
=\sum_kc_k. \tag{2}
\]

### Strictness for a nontrivial mixture

Suppose \(\alpha\) has at least two nonzero coordinates and equality holds in (1). Use the coupling \((G,Y)\) just constructed. Its cost equals the squared Wasserstein distance, so it is optimal. The law of \(Y\) has finite second moment; indeed independence and standardization give \(\mathbb E Y^2=\sum_k\alpha_k^2=1\). Since \(G\sim\gamma\), uniqueness of the Gaussian-origin optimal coupling gives a measurable map \(T\) such that
\[
Y=T(G)\quad\text{almost surely}.
\]
Taking measurable real-valued versions of these maps, we have
\[
T\!\left(\sum_k\alpha_kz_k\right)
=\sum_k\alpha_kT_k(z_k) \tag{3}
\]
for Lebesgue-almost every \(z\in\mathbb R^d\): the joint Gaussian density is strictly positive everywhere, so Gaussian and Lebesgue null sets coincide.

Choose distinct indices \(r,s\) with \(\alpha_r\alpha_s\ne0\). By Fubini's theorem, fix values \(z_{0,k}\) of the remaining coordinates such that (3) holds for almost every \((z_r,z_s)\). If there are no remaining coordinates, this step is unnecessary. Let
\[
c_0=\sum_{k\notin\{r,s\}}\alpha_kz_{0,k},\qquad
c_1=\sum_{k\notin\{r,s\}}\alpha_kT_k(z_{0,k}),
\]
with empty sums equal to zero. The slice equation is
\[
T(\alpha_rz_r+\alpha_sz_s+c_0)
=\alpha_rT_r(z_r)+\alpha_sT_s(z_s)+c_1
\]
for almost every pair. Make the invertible changes of variables \(x=\alpha_rz_r\), \(y=\alpha_sz_s\), and define
\[
f(t)=T(t+c_0)-c_1,\qquad
g(x)=\alpha_rT_r(x/\alpha_r),\qquad
h(y)=\alpha_sT_s(y/\alpha_s).
\]
These functions are measurable, and the invertible changes of variables preserve null sets. Hence \(f(x+y)=g(x)+h(y)\) for Lebesgue-almost every pair. All hypotheses of the stated Pexider theorem are verified. It follows that \(g\) and \(h\) are affine almost everywhere, and therefore \(T_r\) and \(T_s\) are affine almost everywhere.

An almost-everywhere affine map applied to a standard Gaussian is almost surely an affine Gaussian image. Each of \(T_r(Z_r)\) and \(T_s(Z_s)\) has variance one, so its affine slope is nonzero. Thus both \(S_r\) and \(S_s\) have nondegenerate Gaussian laws. This contradicts the assumption that at most one source is Gaussian. The same reduction could be applied to any pair of participating coordinates; two already suffice for the contradiction. Therefore (1) is strict whenever \(\alpha\) has at least two nonzero entries.

### Maximizer characterization

If every row of an orthogonal matrix has only one nonzero entry, row normalization makes each such entry equal to \(\pm1\), and row orthogonality forces their columns to be distinct. Such a matrix is a signed permutation. Hence, if \(A\) is not a signed permutation, at least one row has two or more nonzero entries. The corresponding row inequality in (2) is strict, while every other row satisfies (1), so
\[
F(W)<\sum_kc_k.
\]

If \(A=M\) is a signed permutation, then \(WX=MS\). Reflection of both coordinates of a coupling preserves quadratic cost, and \(\gamma\) is invariant under reflection. Therefore \(W_2^2(\mathcal L(-S_k),\gamma)=c_k\), and permutation of the source coordinates leaves their summed score unchanged. Thus
\[
F(MW^*)=\sum_kc_k.
\]
The upper bound is attained, and equality holds exactly when \(W(W^*)^{-1}\) is a signed permutation. Consequently,
\[
\operatorname*{arg\,max}_{W\in O_d}F(W)
=\{MW^*:M\text{ is a signed permutation matrix}\}.
\]

## Proof-Obligation Closure

The relative-coordinate representation, product-coupling cost, summation over orthogonal columns, and maximizer characterization are derived explicitly. Transport existence and uniqueness use the stated standard-independent result with finite-second-moment and absolute-continuity hypotheses verified. The functional-equation step uses the stated standard-independent almost-everywhere Pexider theorem after an explicit Fubini reduction and null-set-preserving coordinate changes. No theorem-critical obligation remains unresolved.
