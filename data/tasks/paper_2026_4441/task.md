# Problem

## Setup

Fix an input x. A deterministic scalar-output predictor is evaluated with test-time dropout: \(\theta\sim\pi\), and independent forward passes use iid draws. Let
\[
\mu=\mathbb E[D(x;\theta)],\qquad \mu_2=\mathbb E[(D(x;\theta)-\mu)^2],\qquad \mu_4=\mathbb E[(D(x;\theta)-\mu)^4]<\infty.
\]
For iid draws \(\theta_1,\ldots,\theta_T\), with \(T\ge2\), define
\[
Y_T=T^{-1}\sum_{t=1}^T D(x;\theta_t),\qquad V_T=(T-1)^{-1}\sum_{t=1}^T(D(x;\theta_t)-Y_T)^2.
\]
Choose integers \(2\le T_0<T_1<\cdots<T_L\) such that \(T_\ell-T_{\ell-1}\ge2\) for \(\ell\ge1\), and integers \(M_0,\ldots,M_L\ge2\). For each outer replicate and level \(\ell\ge1\), use a nested sample: the first \(T_{\ell-1}\) draws are reused in the \(T_\ell\)-draw sample, with the remaining draws fresh. At each fixed level, the outer replicates are iid. Set \(\Delta V_\ell=V_{T_\ell}-V_{T_{\ell-1}}\).

Let \(\overline V_0\) and \(\overline{\Delta V}_\ell\) denote averages over \(M_0\) and \(M_\ell\) independent outer replicates, and define
\[
\mathcal V=\overline V_0+\sum_{\ell=1}^L\overline{\Delta V}_\ell.
\]
For each component, let \(\mathcal S^2\) be its unbiased empirical variance across outer replicates, and put
\[
S_V^2=M_0^{-1}\mathcal S_{V_0}^2+\sum_{\ell=1}^LM_\ell^{-1}\mathcal S_{\Delta V_\ell}^2.
\]

## Task

Prove that \(\mathbb E[\mathcal V]=\mu_2\) and
\[
\begin{aligned}
\mathbb E[S_V^2]={}&\frac1{M_0T_0}\left(\mu_4-\frac{T_0-3}{T_0-1}\mu_2^2\right)\\
&+\sum_{\ell=1}^L\frac1{M_\ell}\left(\frac1{T_{\ell-1}}-\frac1{T_\ell}\right)(\mu_4-3\mu_2^2)\\
&+\sum_{\ell=1}^L\frac{2\mu_2^2}{M_\ell}\left(\frac1{T_{\ell-1}-1}-\frac1{T_\ell-1}\right).
\end{aligned}
\]
In particular, when \(\mu_4=3\mu_2^2\), show that this becomes
\[
\mathbb E[S_V^2]=2\mu_2^2\left[\frac1{M_0(T_0-1)}+\sum_{\ell=1}^L\frac1{M_\ell}\left(\frac1{T_{\ell-1}-1}-\frac1{T_\ell-1}\right)\right].
\]
