# Reference Proof

## Proof Structure

Apply one-dimensional Wasserstein duality, truncate projected one-Lipschitz functions, control the truncated class through product coverings and the bracketing maximal inequality, and balance the stochastic and tail errors. Finally, invert the rates, treating all positive tolerances and all positive integer sample sizes explicitly.

## 1. Domains, moments, and measurability

Write \(P f=\int f\,d\mu\), \(P_n f=n^{-1}\sum_{j=1}^n f(X_j)\), and \(G_n f=\sqrt n(P_n-P)f\). In this proof, \(Z_n(\mathcal A)=\sup_{f\in\mathcal A}|G_n f|\) is a random variable; expectations are written explicitly.

Let \(R=|X|\) and \(B=\|1+R\|_2\). Tail integration gives
\[
\mathbb E R^2=2\int_0^\infty t\psi_\mu(t)\,dt
\le
\begin{cases}
2C_0/((\beta-1)(\beta-2)),&\text{polynomial tails},\\
2C_0/\delta^2,&\text{exponential tails}.
\end{cases}
\]
Thus \(1\le B\le1+(\mathbb E R^2)^{1/2}\), with a bound depending only on the relevant tail parameters.

For any finite-first-moment probability measure \(\rho\), coupling the two projections of the same point gives
\[
W_1(\rho^v,\rho^w)\le |v-w|\int |x|\,d\rho(x).
\]
The triangle inequality therefore makes the basis objective continuous on the compact set of orthonormal bases. Its maximum exists. For empirical measures the objective is measurable in the sample and continuous in the basis, so its maximum equals a supremum over a countable dense set and is measurable.

For each fixed \(M\), the normalized one-Lipschitz functions on \([-M,M]\) form a compact, separable class in the uniform metric. Together with the compact sphere, this gives a separable parameter space for the truncated class below. The displayed parameter inequality in Section 3 implies continuity of both empirical and population evaluations, using \(P(1+R)<\infty\). Its process supremum is consequently measurable. This verifies the measurability hypothesis of the empirical-process inequality used below.

## 2. Duality and truncation

The one-dimensional Kantorovich–Rubinstein theorem states that, for finite-first-moment probability measures \(\rho,\sigma\),
\[
W_1(\rho,\sigma)=\sup_{g\in\operatorname{Lip}_1(\mathbb R),\ g(0)=0}
\left|\int g\,d(\rho-\sigma)\right|.
\]
The normalization is valid because subtracting a constant does not change the difference of integrals. All projections here have finite first moments.

Let
\[
\mathcal F=\{x\mapsto g(v\cdot x):v\in S^{d-1},\ g\in\operatorname{Lip}_1(\mathbb R),\ g(0)=0\}.
\]
Duality and the fact that a basis has \(d\) unit vectors give the pathwise bound
\[
d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le d\sup_{f\in\mathcal F}|(P_n-P)f|.
\]
For \(M\ge1\), define \(\pi_M(t)=\operatorname{sgn}(t)\min\{|t|,M\}\), and let
\[
\mathcal F_M=\{x\mapsto g(\pi_M(v\cdot x)):v\in S^{d-1},\ g\in\operatorname{Lip}_1([-M,M]),\ g(0)=0\}.
\]
The exact clipping estimate is
\[
|g(t)-g(\pi_M(t))|\le (|t|-M)_+.
\]
Since \(|v\cdot x|\le|x|\), replacing each projected test function by its clipped version shows
\[
\mathbb E d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le \frac d{\sqrt n}\mathbb E Z_n(\mathcal F_M)
 +2d\,\mathbb E(R-M)_+.
\tag{1}
\]
This also proves the coarser bound with \(2d\mathbb E[R\mathbf1_{\{R>M\}}]\). For later use,
\[
\mathbb E(R-M)_+=\int_M^\infty\psi_\mu(t)\,dt.
\tag{2}
\]
In particular, the sharper remainder avoids incorrectly dropping the factor \(M\) from
\[
\mathbb E[R\mathbf1_{\{R>M\}}]
=M\psi_\mu(M)+\int_M^\infty\psi_\mu(t)\,dt.
\]

## 3. Audited entropy tools and their application

We use brackets whose endpoints are measurable ambient \(L^2(P)\) functions, not necessarily members of the indexed class. A bracket \([a,b]\) contains functions \(f\) with \(a\le f\le b\), and its width is \(\|b-a\|_2\).

The standard bracketing maximal inequality used here is: for a pointwise measurable class \(\mathcal A\) with envelope \(H\in L^2(P)\),
\[
\mathbb E Z_n(\mathcal A)
\le C\|H\|_2\int_0^1
\sqrt{1+\log N_{[]}(u\|H\|_2,\mathcal A,L^2(P))}\,du.
\tag{3}
\]
The constant is universal. Its sample hypothesis is i.i.d. sampling. The moment and measurability hypotheses for our class were verified in Section 1.

For completeness, the covering-to-bracketing implication needed here follows directly: if \(|f_s-f_t|\le d_T(s,t)H\), a parameter ball of radius \(c\) around \(t\) yields the bracket \([f_t-cH,f_t+cH]\), of width \(2c\|H\|_2\). Thus
\[
N_{[]}(2c\|H\|_2,\mathcal A,L^2(P))\le N(c,T,d_T).
\tag{4}
\]
This explains why the endpoints cannot be required to lie in \(\mathcal A\).

Parameterize \(\mathcal F_M\) by \(T=S^{d-1}\times\mathcal G_M\), where \(\mathcal G_M\) is the normalized one-Lipschitz class on \([-M,M]\), and use
\[
d_T((v,g),(w,h))=|v-w|+\|g-h\|_\infty.
\]
Because clipping is one-Lipschitz,
\[
|g(\pi_M(v\cdot x))-h(\pi_M(w\cdot x))|
\le |v-w||x|+\|g-h\|_\infty
\le d_T((v,g),(w,h))(1+|x|).
\tag{5}
\]
Also \(|g(\pi_M(v\cdot x))|\le |x|\), so \(H(x)=1+|x|\) is an envelope as well as a parameter modulus.

We need two covering estimates. First, for every \(d\ge1\) and \(0<\eta\le1\),
\[
N(\eta,S^{d-1},|\cdot|)\le(1+2/\eta)^d.
\tag{6}
\]
Indeed, a maximal \(\eta\)-separated subset gives a cover. The disjoint ambient balls of radius \(\eta/2\) around its points lie in the ball of radius \(1+\eta/2\); volume comparison gives (6), including \(d=1\).

Second, the normalized Lipschitz class satisfies
\[
\log N(\eta,\mathcal G_M,\|\cdot\|_\infty)\le CM/\eta
\qquad(0<\eta\le M).
\tag{7}
\]
One elementary justification is to use a grid containing zero with mesh at most \(\eta/8\), and round function values to multiples of \(\eta/8\). The rounded value at zero is fixed, and consecutive rounded values have only a fixed number of possibilities because the functions are one-Lipschitz. There are \(O(M/\eta)\) grid intervals. Two functions with the same rounded code differ by at most \(\eta\) everywhere, by their Lipschitz bounds between grid points. Selecting one class member for each nonempty code gives at most \(\exp(CM/\eta)\) covering centers. This verifies the required entropy estimate without any distributional hypothesis.

To cover the sum product metric at radius \(u/2\), cover each factor at radius \(u/4\). Equations (4), (6), and (7) imply, for \(0<u\le1\),
\[
\log N_{[]}(uB,\mathcal F_M,L^2(P))
\le d\log(1+8/u)+CM/u.
\tag{8}
\]
Using (3), splitting the square root, and integrating gives
\[
\begin{aligned}
\mathbb E Z_n(\mathcal F_M)
&\le CB\left(1+\sqrt d\int_0^1\sqrt{\log(1+8/u)}\,du
+\sqrt M\int_0^1u^{-1/2}\,du\right)\\
&\le CB(1+\sqrt d+\sqrt M)
\le CB\sqrt{dM}.
\end{aligned}
\tag{9}
\]
The first integral is finite since \(\log(1+8/u)\le\log 9+\log(1/u)\); the second equals 2. The last inequality uses \(d,M\ge1\), with a changed universal constant. Absorbing the tail-parameter bound for \(B\), (1) becomes
\[
\mathbb E d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le A d^{3/2}\sqrt{M/n}+2d\int_M^\infty\psi_\mu(t)\,dt,
\tag{10}
\]
where \(A\) depends only on the relevant tail parameters.

## 4. Polynomial-tail rate

Under the polynomial assumption, for \(M\ge1\),
\[
\int_M^\infty\psi_\mu(t)\,dt
\le\frac{C_0}{\beta-1}(1+M)^{1-\beta}
\le\frac{C_0}{\beta-1}M^{1-\beta}.
\]
Set \(M=n^\theta\). Equation (10), and \(d\le d^{3/2}\), give
\[
\mathbb E d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le A' d^{3/2}\left(n^{(\theta-1)/2}+n^{-\theta(\beta-1)}\right).
\]
The exponents agree for \(\theta=1/(2\beta-1)\). This choice has \(M\ge1\) for every \(n\ge1\), and proves
\[
\mathbb E d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le\kappa d^{3/2}n^{-(\beta-1)/(2\beta-1)}.
\]
Solving this inequality proves the polynomial sample-size consequence for every \(\varepsilon>0\).

## 5. Exponential-tail rate

Under the exponential assumption, (2) gives
\[
\int_M^\infty\psi_\mu(t)\,dt\le\frac{C_0}{\delta}e^{-\delta M}.
\]
Choose
\[
M=\max\{1,\delta^{-1}\log(en)\}.
\]
Then \(e^{-\delta M}\le(en)^{-1}\), and \(M\le(1+\delta^{-1})\ell(n)\), where \(\ell(n)=1+\log n\) for \(n\ge1\). Equation (10) yields
\[
\mathbb E d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le A' d^{3/2}\sqrt{\ell(n)/n}+A''d/n
\le A_0d^{3/2}\ell(n)n^{-1/2}.
\tag{11}
\]
All constants depend only on \(C_0,\delta\). This includes \(n=1\).

## 6. Exponential sample-size consequence for every tolerance

A simple bound handles large tolerances. For any basis, coupling through zero and then using Cauchy–Schwarz gives
\[
\sum_{i=1}^d W_1(\hat\mu_n^{v_i},\mu^{v_i})
\le(P_n+P)\sum_{i=1}^d|v_i\cdot x|
\le\sqrt d\,(P_n+P)|x|.
\]
Consequently,
\[
\mathbb E d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le2\sqrt d\,\mathbb E R\le2B\sqrt d.
\tag{12}
\]
If \(\varepsilon\ge2B\sqrt d\), every positive integer sample size already suffices.

Otherwise, put
\[
q=d/\varepsilon,\qquad L=\ell(q),\qquad t=d^{3/2}/\varepsilon.
\]
The inequality \(\varepsilon<2B\sqrt d\) implies \(q>\sqrt d/(2B)\), and hence
\[
\log d\le2\log(2B)+2\log_+q,
\qquad
\log t\le\log(2B)+2\log_+q.
\tag{13}
\]
Choose \(K\ge2eB\), depending only on the tail parameters, and set \(n_0=(KtL)^2\). Since \(t>d/(2B)\ge1/(2B)\), we have \(n_0\ge e^2\). Also \(L\ge1\), \(\log L\le L\), and (13) give
\[
\ell(n_0)=1+2\log K+2\log t+2\log L
\le\bigl(7+2\log K+2\log(2B)\bigr)L.
\tag{14}
\]
The function \((1+\log x)/\sqrt x\) is nonincreasing for \(x\ge e\). For every integer \(n\ge n_0\), equations (11) and (14) therefore imply
\[
\mathbb E d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)
\le\varepsilon\,\frac{A_0\bigl(7+2\log K+2\log(2B)\bigr)}K.
\]
Take \(K\) large enough that the final factor is at most one; this is possible because \(\log K/K\to0\). Together with (12), this proves the stated exponential sufficient sample size for every \(\varepsilon>0\). Enlarging the regime-specific constant once more allows the same symbol \(\kappa\) in its rate and sample-size statements.

## Closure

All critical obligations are closed: the metric maximum and relevant suprema are measurable; moment and constant dependencies are explicit; duality has its finite-moment hypotheses; the standard bracketing inequality is stated and its hypotheses verified; covering-to-bracketing, sphere entropy, Lipschitz entropy, integration, truncation, both rate choices, and both sample-size implications are derived. No specialized unresolved dependency remains.
