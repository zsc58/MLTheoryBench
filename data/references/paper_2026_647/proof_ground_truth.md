# Reference Proof

## Proof Structure and Obligations

Write \(F=d_h(\widehat P_n,\widehat Q_m)\) and \(D=d_h(P,Q)\). When \(n,m\ge2\), write \(A=d_h(\widehat P_n^{(1)},\widehat P_n^{(2)})\), \(B=d_h(\widehat Q_m^{(1)},\widehat Q_m^{(2)})\), and \(G=F-A-B\).

The proof closes the following obligations:

1. Establish measurability and the expectation inequality \(D\le\mathbb EF\).
2. Derive the split-sample comparisons, including unequal block sizes, and hence \(\mathbb EG\le D\).
3. Verify the coordinate sensitivities and their squared sums.
4. Apply bounded differences in the appropriate tail for each confidence statement and justify clipping.
5. Handle the one-observation boundary without evaluating any undefined split or margin.

No asymptotic empirical-convergence theorem or Wasserstein convergence rate is needed for these finite-sample claims.

## Complete Proof

### 1. Basic properties and the upper expectation inequality

We use the standard variational representation
\[
d_{\rm TV}(R,S)=\sup_{f:\mathbb R^d\to[0,1]\ \mathrm{measurable}}\left|\int f\,dR-\int f\,dS\right|.
\]
In particular, total variation distance is bounded by one, satisfies the triangle inequality, and is convex jointly in its two arguments. Convolution is linear. For a measurable test function \(f\) valued in \([0,1]\), the function
\[
g(x)=\int f(x+u)\psi_h(u)\,du
\]
is also measurable and valued in \([0,1]\). Applying the variational representation to \(g\) shows that convolution does not increase total variation distance.

All statistics used below are measurable. Indeed, a Borel version of the density may be used without changing any of the convolved probability measures. The empirical convolutions have densities
\[
p_n(z)=\frac1n\sum_{i=1}^n\psi_h(z-X_i),\qquad q_m(z)=\frac1m\sum_{j=1}^m\psi_h(z-Y_j),
\]
and
\[
F=\frac12\int |p_n(z)-q_m(z)|\,dz.
\]
This integral is a measurable function of the observations by Tonelli's theorem. The same argument applies to the split discrepancies and empirical-to-population distances. These distances belong to \([0,1]\), so all expectations used below are finite.

For every fixed measurable \(f:\mathbb R^d\to[0,1]\), linearity of convolution and expectation gives
\[
\mathbb E\int f\,d(\widehat P_n*\psi_h)=\int f\,d(P*\psi_h),
\qquad
\mathbb E\int f\,d(\widehat Q_m*\psi_h)=\int f\,d(Q*\psi_h).
\]
Consequently,
\[
\left|\int f\,d(P*\psi_h)-\int f\,d(Q*\psi_h)\right|
\le \mathbb E\left|\int f\,d(\widehat P_n*\psi_h)-\int f\,d(\widehat Q_m*\psi_h)\right|
\le \mathbb EF.
\]
Taking the supremum over \(f\) yields \(D\le\mathbb EF\). This holds for every \(n,m\ge1\).

### 2. The split-sample expectation comparison

Assume \(n\ge2\), and set \(n_1=\lfloor n/2\rfloor\), \(n_2=n-n_1\), \(H_1=\widehat P_n^{(1)}\), and \(H_2=\widehat P_n^{(2)}\). These two random probability measures are independent, and each has expectation \(P\). Their sample sizes need not be equal.

Conditional Jensen gives
\[
d_h(H_1,P)\le \mathbb E[d_h(H_1,H_2)\mid H_1],
\qquad
d_h(H_2,P)\le \mathbb E[d_h(H_1,H_2)\mid H_2].
\]
For completeness, let \(p(z)=\int\psi_h(z-x)P(dx)\) and let \(p_1,p_2\) be the densities of \(H_1*\psi_h,H_2*\psi_h\). Independence implies \(\mathbb E[p_2(z)\mid H_1]=p(z)\) for almost every \(z\). Thus conditional Jensen for the absolute value, followed by conditional Tonelli, gives
\[
\frac12\int|p_1(z)-p(z)|\,dz
\le \mathbb E\left[\frac12\int|p_1(z)-p_2(z)|\,dz\,\middle|\,H_1\right].
\]
This proves the first conditional inequality; exchanging the blocks proves the second. Taking expectations yields
\[
\mathbb E d_h(H_1,P)\le\mathbb EA,
\qquad
\mathbb E d_h(H_2,P)\le\mathbb EA.
\]
The correctly weighted identity for the full empirical measure is
\[
\widehat P_n=\frac{n_1}{n}H_1+\frac{n_2}{n}H_2.
\]
Convexity therefore gives
\[
\begin{aligned}
\mathbb E d_h(\widehat P_n,P)
&\le\frac{n_1}{n}\mathbb E d_h(H_1,P)+\frac{n_2}{n}\mathbb E d_h(H_2,P)\\
&\le\mathbb EA.
\end{aligned}
\]
The identical argument for the \(Y\)-sample gives \(\mathbb E d_h(\widehat Q_m,Q)\le\mathbb EB\) whenever \(m\ge2\).

The triangle inequality gives pointwise
\[
D\ge F-d_h(\widehat P_n,P)-d_h(\widehat Q_m,Q).
\]
Hence, when \(n,m\ge2\),
\[
\mathbb EF\ge D\ge\mathbb EF-\mathbb EA-\mathbb EB=\mathbb EG.
\]

### 3. Replacement sensitivities

Replacing one observation in an empirical measure based on \(r\) observations changes that measure in total variation by at most \(1/r\). Convolution contraction and the reverse triangle inequality imply that changing an \(X_i\) changes \(F\) by at most \(1/n\), while changing a \(Y_j\) changes \(F\) by at most \(1/m\). Thus its squared-sensitivity sum is bounded by
\[
C_F=n(1/n)^2+m(1/m)^2=\frac1n+\frac1m.
\]

For \(n,m\ge2\), changing an \(X\)-coordinate in block \(r\in\{1,2\}\) changes \(A\) by at most \(1/n_r\) and leaves \(B\) unchanged. Therefore it changes \(G\) by at most \(1/n+1/n_r\). The contribution of the \(X\)-coordinates to the squared-sensitivity sum is
\[
\begin{aligned}
S_n
&=n_1\left(\frac1n+\frac1{n_1}\right)^2+n_2\left(\frac1n+\frac1{n_2}\right)^2\\
&=\frac5n+\frac1{n_1}+\frac1{n_2}\\
&\le\frac5{n-1}+\frac4{n-1}=\frac9{n-1},
\end{aligned}
\]
where both \(n_1,n_2\ge(n-1)/2>0\). The analogous bound is \(S_m\le9/(m-1)\). Consequently, a valid total squared-sensitivity bound for \(G\) is
\[
C_G=9\left(\frac1{n-1}+\frac1{m-1}\right).
\]

### 4. Concentration and confidence coverage

We use the standard bounded-differences inequality: if \(Z_1,\ldots,Z_N\) are independent, \(T=T(Z_1,\ldots,Z_N)\) is a measurable integrable real-valued function, and replacing coordinate \(i\) changes \(T\) by at most the deterministic constant \(c_i\), then, for \(t>0\) and \(C=\sum_i c_i^2>0\),
\[
\Pr\{T-\mathbb ET\ge t\}\le e^{-2t^2/C},
\qquad
\Pr\{T-\mathbb ET\le-t\}\le e^{-2t^2/C}.
\]
A larger positive upper bound on the squared-sensitivity sum may be substituted for \(C\). Here the observations are mutually independent, the statistics are measurable and bounded, and the preceding calculations verify the required deterministic replacement bounds.

Apply the lower-tail inequality to \(F\), with
\[
t=\varepsilon_{n,m,\alpha}=\sqrt{\frac{\log(1/\alpha)}2\left(\frac1n+\frac1m\right)}.
\]
It follows that
\[
\Pr\{F<\mathbb EF-\varepsilon_{n,m,\alpha}\}\le\alpha.
\]
On the complementary event,
\[
D\le\mathbb EF\le F+\varepsilon_{n,m,\alpha}=\widehat U_\alpha.
\]
This proves the upper confidence statement for every \(n,m\ge1\).

For \(n,m\ge2\), apply the upper-tail inequality to \(G\) with
\[
t=3\varepsilon_{n-1,m-1,\alpha}.
\]
Since \(2t^2/C_G=\log(1/\alpha)\),
\[
\Pr\{G>\mathbb EG+t\}\le\alpha.
\]
On the complementary event, \(G-t\le\mathbb EG\le D\). Since also \(0\le D\),
\[
\widehat L_\alpha=\max\{0,G-t\}\le D.
\]
This proves the lower confidence statement for \(n,m\ge2\), regardless of the sign of \(\mathbb EG\).

### 5. Boundary and quantifiers

If \(\min(n,m)=1\), the prescribed lower bound is \(\widehat L_\alpha=0\le D\) deterministically. No split discrepancy or margin with a zero index is evaluated in this case.

All arguments hold for arbitrary permitted \(P,Q,d,\psi,h,n,m,\alpha\). The two coverage conclusions are separate one-sided statements at level \(1-\alpha\); no joint coverage claim at that same level is needed. The displayed statistics require no auxiliary randomness.
