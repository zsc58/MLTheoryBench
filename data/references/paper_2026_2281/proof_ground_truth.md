# Reference Proof

## Proof Structure and Audited External Input

The only specialized external input is the standard-independent dimension-free Harnack inequality recorded in the source. Its needed statement is: on a complete Riemannian manifold, for the conservative diffusion semigroup with generator
\[
L=\Delta_g-\langle\nabla V,\nabla\rangle,
\]
if \(\mathrm{Ric}+\mathrm{Hess}\,V\ge-Kg\), then for every \(q>1\), \(t>0\), bounded nonnegative measurable \(h\), and \(x,y\) at finite geodesic distance,
\[
(P_th(x))^q\le P_t(h^q)(y)
\exp\!\left(\frac{Kq\,d(x,y)^2}{2(q-1)(1-e^{-2Kt})}\right).
\]
At \(K=0\), the exponent is \(q\,d(x,y)^2/[4(q-1)t]\). This is the curvature-to-Harnack implication supplied by theory_004. Here take \(V=0\): its curvature condition becomes exactly the assumed Ricci bound, its generator is the specified \(\Delta_g\), completeness is assumed, and stochastic completeness makes the semigroup conservative. Thus all hypotheses needed for this application are satisfied.

The remaining obligations are to derive the density-integral estimate, apply the sensitivity bound, analyze the signed-parameter expression, and verify calibration including its zero-sensitivity endpoint. They are derived below; no unresolved private proof obligation remains.

## Complete Proof

### 1. Probability laws and the density estimate

Stochastic completeness gives \(\mu_x^t(M)=1\) for every \(x\) and \(t>0\). Fix \(\alpha>1\), \(t>0\), and \(x,y\) at finite distance, and put
\[
P=\mu_x^t,\qquad Q=\mu_y^t,\qquad
c=\begin{cases}
\displaystyle\frac{K\,d(x,y)^2}{2(1-e^{-2Kt})},&K\ne0,\\[4pt]
\displaystyle\frac{d(x,y)^2}{4t},&K=0.
\end{cases}
\]
In every case \(c\ge0\). Choose the Harnack exponent
\[
q=\frac{\alpha}{\alpha-1}>1.
\]
The audited external inequality says
\[
\left(\int h\,dP\right)^q
\le \left(\int h^q\,dQ\right)e^{cq/(q-1)}
\]
for bounded nonnegative measurable \(h\).

If \(Q(A)=0\), applying this inequality to \(h=\mathbf 1_A\) gives \(P(A)=0\). Hence \(P\ll Q\). Write \(r=dP/dQ\). For integers \(n\ge1\), let
\[
h_n=(r\wedge n)^{\alpha-1},\qquad
A_n=\int(r\wedge n)^\alpha\,dQ.
\]
These are admissible bounded test functions and finite integrals. Moreover,
\[
\int h_n^q\,dQ=A_n,
\qquad
\int h_n\,dP
=\int r(r\wedge n)^{\alpha-1}\,dQ\ge A_n.
\]
Because \(\int r\,dQ=1\), we have \(A_n>0\). Consequently,
\[
A_n^q\le A_ne^{cq/(q-1)},
\qquad
A_n\le \exp\!\left(\frac{cq}{(q-1)^2}\right)
=\exp\!\big(c\alpha(\alpha-1)\big).
\]
Monotone convergence now yields
\[
\int r^\alpha\,dQ
\le \exp\!\big(c\alpha(\alpha-1)\big).
\]
In particular this integral is finite, and the divergence definition gives
\[
D_\alpha(\mu_x^t\|\mu_y^t)
\le \alpha c.
\]
The factor \(\alpha-1\) in the integral exponent is essential: it cancels the normalization in the divergence definition. This argument does not require an unqualified positivity claim for the heat kernel across disconnected components.

### 2. Sensitivity and privacy

For any ordered adjacent pair \(D\sim D'\), set \(x=s(D)\) and \(y=s(D')\). The finite sensitivity bound ensures that their geodesic distance is finite and at most \(\Delta\). For \(K\ne0\), the coefficient \(K/[2(1-e^{-2Kt})]\) is positive. The same is true of its value \(1/(4t)\) at \(K=0\). Therefore
\[
D_\alpha(\mathcal M_t(D)\|\mathcal M_t(D'))
\le\begin{cases}
\displaystyle\frac{K\alpha\Delta^2}{2(1-e^{-2Kt})},&K\ne0,\\[4pt]
\displaystyle\frac{\alpha\Delta^2}{4t},&K=0.
\end{cases}
\]
The pair was arbitrary and ordered, so this is the required RDP guarantee. Reversing the pair is covered by the same argument. If there are no adjacent pairs, the guarantee is vacuous.

### 3. Monotonicity and limits

For \(K\ne0\), differentiation gives
\[
\frac{\partial\varepsilon_K}{\partial t}
=-\frac{K^2\alpha\Delta^2e^{-2Kt}}{(1-e^{-2Kt})^2}\le0.
\]
For \(K=0\),
\[
\frac{\partial\varepsilon_0}{\partial t}
=-\frac{\alpha\Delta^2}{4t^2}\le0.
\]
Thus the bound is nonincreasing, and strictly decreasing when \(\Delta>0\). When \(\Delta=0\), it is identically zero.

If \(K<0\), put \(N=-K>0\). Then
\[
\varepsilon_K=\frac{N\alpha\Delta^2}{2(e^{2Nt}-1)}\longrightarrow0
\quad(t\to\infty).
\]
For \(\Delta>0\), its decay is exponential. If \(K>0\), then \(e^{-2Kt}\to0\), so
\[
\varepsilon_K\longrightarrow\frac{K\alpha\Delta^2}{2}.
\]
This is the limit of this upper-bound expression; it is not a claimed lower bound on the actual divergence.

For fixed \(t>0\), the expansion
\[
1-e^{-2Kt}=2Kt+O(K^2)
\]
gives
\[
\lim_{K\to0}\varepsilon_K=\frac{\alpha\Delta^2}{4t}.
\]
The \(K=0\) expression also tends to zero as \(t\to\infty\).

### 4. Calibration

Fix a target budget \(\varepsilon>0\). First suppose \(\Delta>0\). If \(K<0\), the equation \(\varepsilon_K=\varepsilon\) is equivalent to
\[
e^{-2Kt}=1-\frac{K\alpha\Delta^2}{2\varepsilon}>1.
\]
Its solution is
\[
t=\frac{\log(2\varepsilon)-\log(2\varepsilon-K\alpha\Delta^2)}{2K}.
\]
Both logarithms have positive arguments. The numerator and denominator are negative, so \(t>0\); substitution into the established bound proves \((\alpha,\varepsilon)\)-RDP. For \(K=0\), solving the flat bound gives
\[
t=\frac{\alpha\Delta^2}{4\varepsilon}>0,
\]
which likewise provides the requested guarantee.

For fixed \(\alpha,\Delta,\varepsilon\), rewriting the first calibration as
\[
t=-\frac{1}{2K}\log\!\left(1-\frac{K\alpha\Delta^2}{2\varepsilon}\right)
\]
and using \(\log(1+u)=u+o(u)\) shows that its limit as \(K\to0\) is \(\alpha\Delta^2/(4\varepsilon)\).

Finally, if \(\Delta=0\), both displayed calibrations equal \(t=0\). For every adjacent pair, \(d(s(D),s(D'))=0\), so \(s(D)=s(D')\). Their time-zero laws \(\delta_{s(D)}\) and \(\delta_{s(D')}\) are identical. Their Radon–Nikodym derivative is one almost surely under the common law, and their Renyi divergence is zero. Thus the formulas also give the requested privacy guarantee in this endpoint case, without evaluating the positive-time upper-bound expression at zero time.
