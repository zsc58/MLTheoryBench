# Problem

## Setup

Let \(G\in\mathbb R^{d\times d}\) be positive definite, with eigenvalues
\[
 \lambda_1\geq\cdots\geq\lambda_d>0,
 \qquad \kappa=\lambda_1/\lambda_d.
\]
Fix an integer minibatch size \(m\geq1\). At every iteration, draw independently \(x_1,\ldots,x_m\sim N(0,G)\), and write
\[
 \bar X=\frac1m\sum_{j=1}^m x_jx_j^\top.
\]
For parameters \(\gamma>0\) and \(\mu\in[0,1)\), consider the two-step error recursion
\[
 e_{t+1}=(1+\mu)e_t-\mu e_{t-1}-\gamma(1-\mu)\bar X_t e_t.
\]
With \(z_t=(e_t,e_{t-1})\), define
\[
 M(X)=\begin{pmatrix}
 (1+\mu)I-\gamma(1-\mu)X&-\mu I\\
 I&0
 \end{pmatrix},
 \qquad
 \mathcal T_{G,\gamma,\mu,m}(S)=\mathbb E[M(\bar X)SM(\bar X)^\top]
\]
for symmetric \(2d\)-by-\(2d\) matrices \(S\). Let \(\rho(\mathcal T)\) denote the spectral radius of this linear operator, and define
\[
 s_\star(G,m)=\inf_{\gamma>0,\,\mu\in[0,1)}
 \rho(\mathcal T_{G,\gamma,\mu,m}).
\]

## Task

Prove that
\[
 s_\star(G,m)\geq
 1-8\min\left\{
 \frac{m\lambda_d}{\operatorname{tr}(G)},
 \sqrt{\frac{\lambda_d}{\lambda_1}}
 \right\}.
\]
Moreover, show that the two terms inside the minimum are equal at
\[
 m_{\mathrm{crit}}
 =\frac{\operatorname{tr}(G)}{\sqrt{\lambda_1\lambda_d}}
 =\frac{\operatorname{tr}(G)\sqrt\kappa}{\lambda_1}.
\]
