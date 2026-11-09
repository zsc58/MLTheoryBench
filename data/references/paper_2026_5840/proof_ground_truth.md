# Reference Proof

## Proof Structure

1. Use the null conditional independence and the uniform auxiliary coordinates to show that the selected pivot is conditionally Uniform(0,1), hence its negative-log transform is conditionally Exp(1) on the reduced filtration.
2. Compute the conditional exponential moment and normalize each one-step factor.
3. Multiply the factors to obtain the e-process and apply Ville's maximal inequality to the crossing stopping rule.

## Complete Proof

Let $\mathcal G_t=\sigma(Z_1,\ldots,Z_t)$. Since $\mathcal G_{t-1}\subseteq\mathcal F_{t-1}$, it suffices first to work conditionally on $\mathcal F_{t-1}$. Under $H_0$, conditional on $\mathcal F_{t-1}$, the auxiliary vector $(U_{t,j})_{j\in\mathcal V}$ has iid Uniform$(0,1)$ coordinates and $W_t$ is conditionally independent of that vector. Therefore, for every bounded measurable $h$,
\[
\mathbb E[h(Y_t)\mid\mathcal F_{t-1}]
=\sum_{j\in\mathcal V}\mathbb P(W_t=j\mid\mathcal F_{t-1})\,\mathbb E[h(U_{t,j})\mid\mathcal F_{t-1}]
=\int_0^1h(u)\,du,
\]
where $Y_t=U_{t,W_t}$. Thus $Y_t\mid\mathcal F_{t-1}\sim\mathrm{Unif}(0,1)$, and by the tower property the same holds conditionally on $\mathcal G_{t-1}$. Consequently
\[
Z_t=-\log(1-Y_t)\mid\mathcal G_{t-1}\sim\mathrm{Exp}(1).
\]

Fix $\lambda\in(0,1)$ and define $E_t(\lambda)=(1-\lambda)e^{\lambda Z_t}$. For an Exp$(1)$ random variable, direct integration gives
\[
\mathbb E[e^{\lambda Z_t}\mid\mathcal G_{t-1}]
=\int_0^\infty e^{\lambda z}e^{-z}\,dz
=\frac1{1-\lambda}.
\]
Hence $\mathbb E[E_t(\lambda)\mid\mathcal G_{t-1}]=1$ (and therefore it is at most one), so the adapted sequence $E_t(\lambda)$ is sequentially valid under every null distribution.

Set $M_0(\lambda)=1$ and $M_t(\lambda)=\prod_{s=1}^tE_s(\lambda)$. Iterating the conditional expectation relation shows that $(M_t(\lambda))_{t\ge0}$ is a nonnegative e-process (indeed a martingale) on the reduced filtration, and explicitly
\[
M_t(\lambda)=(1-\lambda)^t\exp\!\left(\lambda\sum_{s=1}^tZ_s\right).
\]
Ville's inequality for e-processes therefore yields, for every $\alpha\in(0,1)$,
\[
\sup_{P\in\mathcal P_0}P\!\left(\sup_{t\ge0}M_t(\lambda)\ge\frac1\alpha\right)\le\alpha.
\]
Thus the rule $\tau_\alpha=\inf\{t\ge1:M_t(\lambda)\ge1/\alpha\}$ (with $\inf\varnothing=\infty$) has level at most $\alpha$, regardless of optional stopping or the time at which it is inspected.
