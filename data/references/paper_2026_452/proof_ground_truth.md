# Reference Proof

## Proof Structure

We first analyze the magnetization by enumerating configurations with a fixed magnetization and maximizing the resulting mean-field free energy. The class-0 free energy has one negative maximizer, while the zero-field class-1 free energy has two symmetric maximizers. The class-1 field is an order-one exponential tilt of these two phases, which determines their limiting mixture weights. These limits imply informative one-coordinate marginals and consistency of the absolute-magnetization classifier. Finally, the product-marginal classifier is reduced to a threshold in the vote fraction; the assumed ordering places the negative class-1 phase on the class-0 side of that threshold.

## Complete Proof

Write
\[
 H(u)=-u\log u-(1-u)\log(1-u),\qquad
 \Phi_\beta(m)=H\!\left(\frac{1+m}{2}\right)+\frac{\beta m^2}{2}.
\]
If \(M_K=m\), the number of spin configurations is
\(\binom K{K(1+m)/2}\). Consequently, under parameters \((\beta,\eta)\),
\[
 \mathbb P(M_K=m)\ \propto\ 
 \binom K{K(1+m)/2}\exp\left\{K\left(\frac{\beta m^2}{2}+\eta m\right)\right\}.
 \tag{1}
\]
Stirling's bounds, uniformly over the magnetization grid, give
\[
 \log\binom K{K(1+m)/2}
 =K H\!\left(\frac{1+m}{2}\right)+O(\log K).
 \tag{2}
\]
Thus any closed set separated from the maximizers of the relevant free energy has exponentially smaller probability than a grid point approaching a maximizer.

For class 0, set
\[
 \Psi_0(m)=\Phi_{\beta_0}(m)+h_0m.
\]
On \((-1,1)\),
\[
 \Psi_0'(m)=-\operatorname{arctanh}(m)+\beta_0m+h_0,
 \qquad
 \Psi_0''(m)=\beta_0-\frac1{1-m^2}<0.
\]
Hence \(\Psi_0\) is strictly concave and has a unique maximizer. Its stationarity equation is
\(m=\tanh(\beta_0m+h_0)\), so the maximizer is \(m_0\). Since \(h_0<0\), it is negative. The free-energy gap following from strict uniqueness, together with (1)-(2), proves
\[
 M_K\mid(Y=0)\longrightarrow m_0
 \quad\text{in probability}. \tag{3}
\]

For class 1, first consider the same model with zero external field. We have
\[
 \Phi_\beta'(m)=-\operatorname{arctanh}(m)+\beta m,
 \qquad
 \Phi_\beta''(m)=\beta-\frac1{1-m^2}.
\]
For \(\beta_1>1\), the equation \(m=\tanh(\beta_1m)\) has exactly one positive solution \(m_*\): on \((0,1)\), the function \(\tanh(\beta_1m)-m\) starts at zero with positive derivative, is strictly concave, and is negative at \(1\). The derivative of \(\Phi_{\beta_1}\) changes sign at \(m_*\), and symmetry gives exactly two global maximizers, \(-m_*\) and \(m_*\), while zero is a strict local minimum. Applying the same free-energy-gap argument yields
\[
 \mathbb P_0\bigl(\bigl||M_K|-m_*\bigr|>\varepsilon\bigr)
 \le e^{-c_\varepsilon K} \tag{4}
\]
for all sufficiently large \(K\), where \(\mathbb P_0\) denotes the zero-field class-1 law. This law is invariant under global spin reversal. Since (4) makes the mass at zero negligible, its positive and negative phases each have limiting probability \(1/2\).

The actual class-1 field is \(c/K\). Relative to \(\mathbb P_0\), its Radon-Nikodym factor is
\[
 \exp\left\{\frac cK\sum_iX_i\right\}=e^{cM_K}.
\]
For every bounded continuous \(f\), symmetry, (4), and bounded convergence therefore give
\[
 \mathbb E[f(M_K)\mid Y=1]
 =\frac{\mathbb E_0[f(M_K)e^{cM_K}]}{\mathbb E_0[e^{cM_K}]}
 \longrightarrow
 \frac{e^{cm_*}f(m_*)+e^{-cm_*}f(-m_*)}
 {e^{cm_*}+e^{-cm_*}}.
\]
Thus
\[
 M_K\mid(Y=1)\Rightarrow p\,\delta_{m_*}+(1-p)\,\delta_{-m_*},
 \qquad
 p=\frac{e^{cm_*}}{e^{cm_*}+e^{-cm_*}}=\sigma(2cm_*).
 \tag{5}
\]

Exchangeability and \(J_i=(1+X_i)/2\) imply
\[
 a_{y,K}=\frac{1+\mathbb E[M_K\mid Y=y]}2.
\]
Equations (3) and (5) give
\[
 a_{0,K}\to a_0=\frac{1+m_0}{2}<\frac12,
 \qquad
 a_{1,K}\to a_1=\frac{1+(2p-1)m_*}{2}>\frac12. \tag{6}
\]
Therefore every coordinate has both stated class-conditional advantages for all sufficiently large \(K\).

The assumption \((1-m_*)/2<a_0\) is equivalent to \(|m_0|<m_*\), so a threshold \(t\) satisfying \(|m_0|<t<m_*\) exists. By (3), the classifier \(g_{t,K}=\mathbf 1\{|M_K|\ge t\}\) has class-0 error tending to zero. By (5), both class-1 phases have absolute magnetization converging to \(m_*>t\), so its class-1 error also tends to zero. Hence
\[
 R_K(g_{t,K})\to0. \tag{7}
\]
In particular, if \(R_K^*\) is Bayes risk, then \(0\le R_K^*\le R_K(g_{t,K})\), and therefore \(R_K^*\to0\).

It remains to analyze the oracle product-marginal classifier. Let
\(V_K=K^{-1}\sum_iJ_i=(1+M_K)/2\). For all sufficiently large \(K\), (6) gives \(0<a_{0,K}<a_{1,K}<1\). Its log posterior odds, divided by \(K\), are
\[
 \frac1K\log\frac{\pi}{1-\pi}
 +V_K\log\frac{a_{1,K}}{a_{0,K}}
 +(1-V_K)\log\frac{1-a_{1,K}}{1-a_{0,K}}.
\]
Thus the classifier predicts one exactly when \(V_K\ge\tau_K\), up to its immaterial tie convention, where
\[
 \tau_K=
 \frac{\log\frac{1-a_{0,K}}{1-a_{1,K}}-K^{-1}\log\frac\pi{1-\pi}}
 {\log\frac{a_{1,K}(1-a_{0,K})}{a_{0,K}(1-a_{1,K})}}.
 \tag{8}
\]
Let \(\tau\) be the limit obtained by replacing \(a_{y,K}\) with \(a_y\) and deleting the vanishing prior term. The limiting affine log-likelihood function \(L(v)\) satisfies
\[
 L(a_0)=-D(\operatorname{Bern}(a_0)\|\operatorname{Bern}(a_1))<0,
 \quad
 L(a_1)=D(\operatorname{Bern}(a_1)\|\operatorname{Bern}(a_0))>0.
\]
Since \(L\) is strictly increasing, \(a_0<\tau<a_1\). Moreover, with
\(r_-=(1-m_*)/2\) and \(r_+=(1+m_*)/2\), the hypothesis and the fact that \(a_1=pr_++(1-p)r_-\), with \(p\in(1/2,1)\), give the strict ordering
\[
 r_-<a_0<\tau<a_1<r_+. \tag{9}
\]
Because \(\tau_K\to\tau\), (3) and (9) show that the product-marginal classifier predicts zero with probability tending to one under class 0. Equations (5) and (9) show that under class 1 it predicts zero on the negative phase and one on the positive phase. Its limiting conditional error under class 1 is consequently \(1-p\). Hence
\[
 R_K(\widehat g_K)\longrightarrow \pi(1-p). \tag{10}
\]
Combining (7), (10), and \(R_K^*\to0\) proves
\[
 R_K(\widehat g_K)-R_K^*\longrightarrow\pi(1-p)>0,
\]
as required.
