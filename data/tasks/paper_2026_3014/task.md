# Problem

## Setup

Let d>=5 and n>=1 be integers. Let \(\mu\) be a Borel probability measure on \(\mathbb R^d\) with
\[
\sigma^2=\mathbb E_{X\sim\mu}\|X\|^2<\infty,
\]
and let \(S=(X_1,\ldots,X_n)\sim\mu^{\otimes n}\). All norms are Euclidean.

Consider the forward diffusion
\[
dX_t=-\kappa X_t\,dt+\sqrt2\,dB_t,\qquad X_0\sim\mu,
\]
where \(\kappa\ge0\), the Brownian motion is standard and independent of the initial variable, and
\[
\alpha_t=e^{-\kappa t},\qquad
\sigma_t^2=\kappa^{-1}(1-\alpha_t^2)\quad(\kappa>0),\qquad
\sigma_t^2=2t\quad(\kappa=0).
\]
Write \(\mu_t\) for its law and \(\widehat\mu_t\) for the conditional law obtained by starting the same diffusion from \(n^{-1}\sum_{i=1}^n\delta_{X_i}\), with fresh independent diffusion noise. For \(t>0\), use the same symbols for their smooth positive densities.

Let \(b_S(y,t)\in\mathbb R^d\) be a jointly measurable function of \((S,y,t)\); it may depend on the training dataset. With S held fixed, define
\[
\mathcal L_t(b_S)=\mathbb E_{Y\sim\mu_t}\|b_S(Y,t)-\nabla\log\mu_t(Y)\|^2,
\qquad
\widehat{\mathcal L}_t(b_S)=\mathbb E_{Y\sim\widehat\mu_t}\|b_S(Y,t)-\nabla\log\widehat\mu_t(Y)\|^2.
\]
These expectations integrate only over the indicated noised law. For a nonnegative time measure \(\eta\), set
\[
\mathcal L(b_S,\eta)=\int\mathcal L_t(b_S)\,\eta(dt),\qquad
\widehat{\mathcal L}(b_S,\eta)=\int\widehat{\mathcal L}_t(b_S)\,\eta(dt).
\]
Losses may take the value \(+\infty\). The notation \(\mathbb E_S\) denotes expectation over the iid training dataset.

Fix \(0<\epsilon<T<\infty\). Let
\[
\varpi(dt)=\mathbf1_{[\epsilon,T]}(t)w(t)\,dt,
\]
where \(w:[\epsilon,T]\to[0,\infty)\) is finite-valued, nondecreasing, and positive Lebesgue-almost everywhere on \((\epsilon,T)\). For \(a\in[\epsilon,T]\), define
\[
\varpi_{\rm ELBO}^{a}(dt)=\mathbf1_{[a,T]}(t)\,dt.
\]
For \(r\ge0\), define
\[
w^{-}(r)=\inf\{t\in[\epsilon,T]:w(t)\ge r\},\qquad \inf\varnothing=+\infty.
\]
Let \(0\le\varepsilon\le w(T)/32\) and set \(\delta=w^{-}(32\varepsilon)\).

Let \(B(x,r)\) denote the open Euclidean ball and define the lower order-2 Renyi dimension by
\[
\underline d_2(\mu)=\liminf_{r\downarrow0}
\frac{\log\int\mu(B(x,r))\,d\mu(x)}{\log r}.
\]
Use \(\mathrm{KL}(P\|Q)=\int\log(dP/dQ)\,dP\) when \(P\ll Q\), and \(+\infty\) otherwise.

Set
\[
q_0=N(0,\kappa^{-1}I_d)\quad(\kappa>0),\qquad
q_0=N(0,2TI_d)\quad(\kappa=0).
\]
Conditional on S, consider the reverse diffusion
\[
dY_u=[\kappa Y_u+2b_S(Y_u,T-u)]\,du+\sqrt2\,d\widetilde B_u,
\qquad Y_0\sim q_0.
\]
Its initial variable and Brownian motion are independent of S and of each other. Restrict attention to scores for which, for almost every S, this SDE has a unique nonexplosive weak law on each interval \([0,T-a]\), \(a\in(0,T)\). Denote its conditional marginal law by \(q^S_u\).

Assume the horizon satisfies
\[
T\ge\max\left\{1,\ 1+\frac1{2\kappa}\log\bigl(32(\sigma^2+\kappa^{-1}d)\bigr)\right\}
\quad\text{if }\kappa>0,
\qquad
T\ge8\sigma^2\quad\text{if }\kappa=0.
\]

## Task

Prove that if
\[
\mathbb E_S[\widehat{\mathcal L}(b_S,\varpi)]\le\varepsilon,
\]
then any one of the following conditions:

1. \(\mathbb E_S[\mathcal L(b_S,\varpi)]\le\varepsilon\);
2. \(\mathbb E_S[\mathcal L(b_S,\varpi_{\rm ELBO}^{\epsilon})]\le1/32\);
3. \(\mathrm{KL}(\mu_\delta\|q^S_{T-\delta})\le1/32\) for almost every S;

implies, for every real \(d'<\underline d_2(\mu)\) and sufficiently small positive \(\delta\),
\[
n\ge\bigl(8\sqrt d\,\sigma_\delta\bigr)^{-d'/2}.
\]
The small-cutoff threshold may depend on \(\mu,d,\kappa,T,d'\), but not on n or the score. Thus simultaneously small empirical and population score-matching losses, or a small generated-law KL as specified above, require a sample size exponential in the lower Renyi dimension.
