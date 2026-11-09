# Problem

## Setup

For each integer \(K\ge1\), let \(Y\in\{0,1\}\) have prior \(\mathbb P(Y=1)=\pi\in(0,1)\). Conditional on \(Y=y\), let \(X=(X_1,\ldots,X_K)\in\{-1,1\}^K\) have law
\[
 \mathbb P_K(X=x\mid Y=y)=\frac1{Z_{y,K}}
 \exp\left\{\frac{\beta_y}{2K}\left(\sum_{i=1}^Kx_i\right)^2
 +\eta_{y,K}\sum_{i=1}^Kx_i\right\}.
\]
Define the binary votes \(J_i=(1+X_i)/2\) and magnetization
\[
 M_K=\frac1K\sum_{i=1}^KX_i.
\]
Assume
\[
 0<\beta_0<1,\qquad \eta_{0,K}=h_0<0,
 \qquad \beta_1>1,\qquad \eta_{1,K}=\frac cK
\]
for a fixed \(c>0\). Let \(m_0\in(-1,0)\) be the unique solution of
\[
 m_0=\tanh(\beta_0m_0+h_0),
\]
and let \(m_*\in(0,1)\) be the unique positive solution of
\[
 m_*=\tanh(\beta_1m_*).
\]
Set
\[
 p=\frac1{1+e^{-2cm_*}},\qquad
 a_0=\frac{1+m_0}{2},\qquad
 a_1=\frac{1+(2p-1)m_*}{2},
\]
and assume
\[
 \frac{1-m_*}{2}<a_0.
\]

For a classifier \(g_K:\{0,1\}^K\to\{0,1\}\), write
\(R_K(g_K)=\mathbb P(g_K(J)\ne Y)\), and let \(R_K^*\) denote the Bayes risk under the true joint law.

For each \(K\), define the true one-coordinate marginals
\[
 a_{y,K}=\mathbb P_K(J_1=1\mid Y=y).
\]
The oracle product-marginal classifier \(\widehat g_K\) is the posterior classifier obtained after replacing each true class-conditional joint law by the product of its true one-coordinate marginals; explicitly, it predicts one when
\[
 \pi\prod_{i=1}^K a_{1,K}^{J_i}(1-a_{1,K})^{1-J_i}
 \ge
 (1-\pi)\prod_{i=1}^K a_{0,K}^{J_i}(1-a_{0,K})^{1-J_i}.
\]

## Task

Prove the following integrated asymptotic separation theorem. The marginals satisfy
\[
 a_{0,K}\longrightarrow a_0<\frac12,
 \qquad
 a_{1,K}\longrightarrow a_1>\frac12,
\]
so every vote is conditionally better than random in both classes for all sufficiently large \(K\). For every fixed \(t\) with \(|m_0|<t<m_*\), the dependence-aware classifier
\[
 g_{t,K}(J)=\mathbf 1\{|M_K|\ge t\}
\]
satisfies \(R_K(g_{t,K})\to0\), whereas
\[
 R_K(\widehat g_K)\longrightarrow \pi(1-p).
\]
Consequently \(R_K^*\to0\) and
\[
 R_K(\widehat g_K)-R_K^*\longrightarrow\pi(1-p)>0.
\]
