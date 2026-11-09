# Problem

## Setup

Let a parameter be decomposed as \(\theta=(\theta_T,\theta_N)\) with prior density \(p(\theta)\). Fix a positive integer horizon \(K\) and a measurable deterministic policy \(\pi\). Set \(h_0=\varnothing\). A history is
\[
h_k=((u_1,y_1),\ldots,(u_k,y_k)),\qquad u_k=\pi(h_{k-1}).
\]
Assume the induced history densities \(p(h_K\mid\theta,\pi)\), \(p(h_K\mid\theta_T,\pi)\), and \(p(h_K\mid\pi)\) exist with respect to a common measure. Define
\[
p(h_K\mid\theta_T,\pi)=\int p(h_K\mid\theta_T,\theta_N,\pi)\,p(\theta_N\mid\theta_T)\,d\theta_N,
\]
\[
p(h_K\mid\pi)=\int p(h_K\mid\theta,\pi)p(\theta)\,d\theta,
\]
and the targeted sequential expected information gain
\[
I_K^{\mathrm{tgt}}(\pi)=\mathbb E_{p(\theta)p(h_K\mid\theta,\pi)}\left[\log\frac{p(h_K\mid\theta_T,\pi)}{p(h_K\mid\pi)}\right].
\]

Draw \(\theta^{(0)}=(\theta_T^{(0)},\theta_N^{(0)})\sim p(\theta)\), then draw \(h_K\sim p(h_K\mid\theta^{(0)},\pi)\). Draw \(\theta^{(1)},\ldots,\theta^{(L)}\) iid from \(p(\theta)\), independently of \((\theta^{(0)},h_K)\). Conditional on \(\theta_T^{(0)}\), draw \(\widetilde\theta_N^{(1)},\ldots,\widetilde\theta_N^{(M)}\) iid from \(p(\theta_N\mid\theta_T^{(0)})\), independently of \((\theta_N^{(0)},h_K,\theta^{(1)},\ldots,\theta^{(L)})\) given \(\theta_T^{(0)}\). For positive integers \(L,M\), set
\[
\widehat p_M(h_K\mid\theta_T^{(0)},\pi)=\frac1M\sum_{m=1}^M p(h_K\mid\theta_T^{(0)},\widetilde\theta_N^{(m)},\pi),
\]
\[
\widehat p_L(h_K\mid\pi)=\frac1{L+1}\sum_{\ell=0}^{L}p(h_K\mid\theta^{(\ell)},\pi),
\]
and
\[
\widehat{\mathcal L}_K^{\mathrm{tgt}}(\pi,L,M)=\mathbb E\left[\log\frac{\widehat p_M(h_K\mid\theta_T^{(0)},\pi)}{\widehat p_L(h_K\mid\pi)}\right],
\]
where the expectation is over all the stated draws. Assume that every likelihood evaluation in these averages, and the marginal likelihoods \(p(h_K\mid\theta_T^{(0)},\pi)\) and \(p(h_K\mid\pi)\), are positive and finite almost surely under this experiment. Assume that the expectations defining \(I_K^{\mathrm{tgt}}(\pi)\) and \(\widehat{\mathcal L}_K^{\mathrm{tgt}}(\pi,L,M)\) are finite for every positive \(L,M\).

For the convergence claim, assume constants \(0<\kappa_{1,N}\le\kappa_{2,N}<\infty\) and \(0<\kappa_1\le\kappa_2<\infty\) satisfy
\[
\kappa_{1,N}\le \frac{p(h_K\mid\theta_T,\theta_N,\pi)}{p(h_K\mid\theta_T,\pi)}\le\kappa_{2,N},
\qquad
\kappa_1\le \frac{p(h_K\mid\theta,\pi)}{p(h_K\mid\pi)}\le\kappa_2.
\]
These bounds are uniform over parameters in the prior support and histories for which the respective marginal denominator is positive and finite. The constants may depend on the fixed model, horizon, and policy, but not on the parameter, history, \(L\), or \(M\).

## Task

Prove that
\[
\widehat{\mathcal L}_K^{\mathrm{tgt}}(\pi,L,M)\le I_K^{\mathrm{tgt}}(\pi)
\]
for every pair of positive integers \(L,M\), and that
\[
\widehat{\mathcal L}_K^{\mathrm{tgt}}(\pi,L,M)\longrightarrow I_K^{\mathrm{tgt}}(\pi)
\]
when both \(L\) and \(M\) tend to infinity under the stated bounded likelihood-ratio assumptions.
