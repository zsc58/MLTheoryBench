# Problem

## Setup

Fix a positive integer horizon \(T\), a bound \(B>0\), and costs \(b,h>0\). A latent demand distribution \(P\), a probability measure on \([0,B]\), is drawn from a prior. Conditional on \(P\), the demand vector \(D_{1:T}\) has a fixed joint law on \([0,B]^T\), with every coordinate marginal equal to \(P\). This demand vector is exogenous: its law is independent of the policy's randomization and is the same for all policies. Conditional independence of demand coordinates is not required.

At round \(t\), a policy chooses \(X_t\in[0,B]\) using only the observed history and fresh randomization independent of the latent variables. It observes
\[
O_t=(S_t,C_t),\qquad S_t=\min\{D_t,X_t\},\qquad C_t=\mathbf 1\{D_t\le X_t\},
\]
and incurs loss
\[
\ell(x,d)=h(x-d)_+ + b(d-x)_+.
\]
Write \(H_t=(X_1,O_1,\ldots,X_t,O_t)\), with \(H_0\) empty. Let
\[
f_P(x)=\mathbb E_{D\sim P}\ell(x,D),\qquad
x_P^*\in\arg\min_{x\in[0,B]}f_P(x),\qquad
r_t=f_P(X_t)-f_P(x_P^*).
\]
Use a measurable choice of \(x_P^*\). For a policy \(\nu\), define
\[
\operatorname{Reg}_T(\nu)=\mathbb E_\nu\sum_{t=1}^T r_t,
\]
where the expectation includes the prior, demand, and policy randomness.

Let \(\gamma=b/(b+h)\). Define \(A:[0,B]^T\to[0,B]\) to be the left empirical \(\gamma\)-quantile, or equivalently the smallest minimizer of total empirical loss.

For every \(t\) and history \(h\), let \(Q_t^0(\cdot\mid h)\) be the true Bayesian conditional law of \(D_{1:T}\) given that history, and let \(\widehat Q_t(\cdot\mid h)\) be another measurable probability kernel on \([0,B]^T\). The latter is censoring-consistent: for each past \(s<t\), it is supported on \(d_s=S_s\) when \(C_s=1\), and on \(d_s>X_s\) when \(C_s=0\). Fix measurable versions of all conditional kernels, assigning arbitrary versions on impossible histories. Define the action kernels
\[
K_t^0(\cdot\mid h)=A_\#Q_t^0(\cdot\mid h),
\qquad
K_t(\cdot\mid h)=A_\#\widehat Q_t(\cdot\mid h),
\]
where \(A_\#M(E)=M(A^{-1}(E))\). Denote the corresponding ideal and deployed policies by \(\pi_0\) and \(\pi\). Let \(\mathbb Q\) and \(\mathbb P\) be their full joint laws of \((P,D_{1:T},H_T)\), respectively. They have the same prior and demand law; conditional on a history and action, they use the same true observation kernel.

For a fixed \((t,h)\), order completion coordinates as
\[
(D_t,D_1,\ldots,D_{t-1},D_{t+1},\ldots,D_T).
\]
Let \(q^0_{t,s}\) and \(\widehat q_{t,s}\) be the conditional kernels of the \(s\)-th coordinate in this order, given \(h\) and all preceding coordinates. Write \(D_{<s}^{(t)}\) for that preceding-coordinate vector. Define
\[
d_t(h)=\mathrm{KL}(q^0_{t,1}(\cdot\mid h)\|\widehat q_{t,1}(\cdot\mid h))
\]
and, for \(s\ge2\),
\[
\delta_{t,s}(h)=\mathbb E_{Q_t^0(\cdot\mid h)}
\mathrm{KL}\!\left(q^0_{t,s}(\cdot\mid h,D_{<s}^{(t)})\|\widehat q_{t,s}(\cdot\mid h,D_{<s}^{(t)})\right).
\]

Let \(P^{\rm obs}_{t,h,x}\) and \(\widehat P^{\rm obs}_{t,h,x}\) be the laws obtained by pushing the respective current-demand marginals through
\[
d\longmapsto(\min\{d,x\},\mathbf 1\{d\le x\}).
\]
Define the on-policy observed predictive mismatch
\[
\Delta_T^{\rm obs}
=\sum_{t=1}^T\mathbb E_{H_{t-1}\sim\mathbb P}
\mathbb E_{X_t\sim K_t(\cdot\mid H_{t-1})}
\mathrm{KL}\!\left(P^{\rm obs}_{t,H_{t-1},X_t}\|\widehat P^{\rm obs}_{t,H_{t-1},X_t}\right).
\]
Assume that \(P^{\rm obs}_{t,h,x}\ll\widehat P^{\rm obs}_{t,h,x}\) for almost every \((h,x)\) under the deployed interaction, for each \(t\).

To specify predictive log-loss for arbitrary, possibly atomic demand laws, use the common dominating kernel
\[
\mu_{t,h,x}=P^{\rm obs}_{t,h,x}+\widehat P^{\rm obs}_{t,h,x}.
\]
Let \(p^0_{t,h,x}\) and \(\widehat p_{t,h,x}\) be the respective densities with respect to \(\mu_{t,h,x}\). With \(-\log0=+\infty\), define
\[
\mathcal L_T(p^0;\pi)=\mathbb E_{\mathbb P}\sum_{t=1}^T-\log p^0_{t,H_{t-1},X_t}(O_t),
\qquad
\mathcal L_T(\widehat p;\pi)=\mathbb E_{\mathbb P}\sum_{t=1}^T-\log\widehat p_{t,H_{t-1},X_t}(O_t).
\]

Assume there are finite constants \(L>0\), \(V\ge1\), \(\rho\in(0,1]\), \(a\ge0\), and \(u\in\mathbb R\) such that:

1. Under \(\mathbb Q\), almost surely \(r_t\in[u,u+L]\) for all \(t\), and for every \(t\),
\[
\mathbb E_{\mathbb Q}[r_t\mid H_{t-1}]=\mathbb E_{\mathbb Q}r_t
\quad\mathbb Q\text{-almost surely}.
\]
2. For every \(t\), every history \(h\), and every measurable event \(F\subseteq[0,B]^T\),
\[
\widehat Q_t(\cdot\mid h)\ll Q_t^0(\cdot\mid h),
\qquad
\widehat Q_t(F\mid h)\le VQ_t^0(F\mid h).
\]
3. For every \(t\) and \(\mathbb P\)-almost every history \(h\),
\[
K_t(\{B\}\mid h)\ge\rho.
\]
4. For every \(t\), \(\mathbb P\)-almost every history \(h\), and every \(s=2,\ldots,T\),
\[
\delta_{t,s}(h)\le\frac as d_t(h).
\]

KL divergences may be infinite. In nonnegative products use the convention \(0\cdot(+\infty)=0\).

## Task

Prove the integrated deployment guarantee
\[
\boxed{
\operatorname{Reg}_T(\pi)
\le\operatorname{Reg}_T(\pi_0)
+L\sqrt{\frac{T(2+\log V)(1+a\log T)}{2\rho}\,\Delta_T^{\rm obs}}
}.
\]
Also establish that the defined true population log-loss is finite and that
\[
\Delta_T^{\rm obs}=\mathcal L_T(\widehat p;\pi)-\mathcal L_T(p^0;\pi).
\]
Thus the deployed policy's excess regret over the ideal benchmark is controlled explicitly by its on-policy excess censored predictive log-loss.
