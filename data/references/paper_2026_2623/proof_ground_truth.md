# Reference Proof

Assume throughout that \(p_c>0\), as required for \(P_k\), \(\Delta_+\), and \(\Delta\). If the dirty component has zero retained mixture weight, its contribution below is zero and no \(Q_k\) is needed.

Conditioning \(P^*=(1-\varepsilon)P+\varepsilon Q\) on \(K=1\) gives
\[
R=(1-\widetilde\varepsilon)P_k+\widetilde\varepsilon Q_k,
\qquad \widetilde\varepsilon=\frac{\varepsilon p_d}{(1-\varepsilon)p_c+\varepsilon p_d}.
\]
Consequently, for each real \(a\),
\[
F_R(a)-F_P(a)=(1-\widetilde\varepsilon)(F_{P_k}(a)-F_P(a))
+\widetilde\varepsilon(F_{Q_k}(a)-F_P(a)).
\]
Taking positive parts and suprema yields
\[
d_{R\to P,+}\leq(1-\widetilde\varepsilon)\Delta_+
+\widetilde\varepsilon D_+.
\]
For every real \(q\) with \(F_R(q)\geq1-\alpha\), the definition of this gap gives \(F_P(q)\geq F_R(q)-d_{R\to P,+}\). Substitute the bound and use \(F_P(q)\geq0\) to obtain the first asserted positive-part inequality.

For each real \(a\),
\[
F_{P_k}(a)-F_P(a)
=\frac{E_P[\mathbf1\{A\leq a\}K]-p_c E_P[\mathbf1\{A\leq a\}]}{p_c}
=\frac{\operatorname{Cov}_P(\mathbf1\{A\leq a\},K)}{p_c}.
\]
In particular, \(\Delta=p_c^{-1}\sup_a|\operatorname{Cov}_P(\mathbf1\{A\leq a\},K)|=\rho/p_c\), and \(\Delta_+\leq\Delta\). The corresponding one-sided supremum identity follows by taking positive parts. If \(A\) and \(K\) are independent under \(P\), these distortions vanish.

For \(\lambda\geq0\), the map \(x\mapsto\varepsilon x/((1-\varepsilon)p_c+\varepsilon x)\) is nondecreasing on \([0,\infty)\). Thus \(p_d\leq\lambda p_c\) gives
\[
\widetilde\varepsilon\leq\frac{\varepsilon\lambda}{1-\varepsilon+\varepsilon\lambda}.
\]
Equivalently, \(\widetilde\varepsilon=\varepsilon(p_d/p_c)/(1-\varepsilon+\varepsilon(p_d/p_c))\). Holding \(\varepsilon<1\) fixed, \(p_d/p_c\to0\) therefore implies \(\widetilde\varepsilon\to0\); setting \(p_d=p_c\) gives \(\widetilde\varepsilon=\varepsilon\). These conclusions include \(\varepsilon=0\).

If \(p_c=p_d=r>0\), then \(\mu=r\), \(\widetilde\varepsilon=\varepsilon\), and the covariance identity gives \(\Delta=\rho/r\). Since \(\Delta_+\leq\rho/r\), the first diagnostic implies, for every qualifying \(q\),
\[
P(A\leq q)\geq\left[1-\alpha-(1-\varepsilon)\frac{\rho}{r}-\varepsilon D_+\right]_+.
\]
Thus equal retention probabilities do not lower the retained contamination coefficient. A better diagnostic can arise from the retained dirty score discrepancy and/or reduced clean-side covariance distortion, but not from a coefficient reduction.
