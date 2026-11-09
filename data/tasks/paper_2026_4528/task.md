# Problem

## Setup

Work on a complete probability space. Let $\theta_0$ be an initial random element and let $\mathcal F_t=\sigma(\theta_0,g_1,\ldots,g_t)$ be the natural filtration, with $\mathcal F_0=\sigma(\theta_0)$. Fix an integer time $t\ge1$ and dimension $p\ge3$. Let $q_t\in\mathbb R^p$ and $m_{t-1}\in\mathbb R^p$ be $\mathcal F_{t-1}$-measurable. Assume that, conditionally on $\mathcal F_{t-1}$,
\[
g_t=q_t+\varepsilon_t,\qquad \varepsilon_t\sim N(0,\sigma^2I_p),
\]
where $\sigma^2>0$ is a fixed known scalar. For an estimator $\widehat q_t$, define conditional quadratic risk by
\[
R_t(\widehat q_t)=\mathbb E[\|\widehat q_t-q_t\|^2\mid\mathcal F_{t-1}].
\]
For a randomized estimator this expectation also averages over its randomization.

The conditional minimax and admissibility statements refer to the following decision experiment. Hold the historical center fixed at $m\in\mathbb R^p$, and observe $X\sim N(q,\sigma^2I_p)$ with unknown parameter $q$ ranging over all of $\mathbb R^p$. An allowed decision rule is any Borel probability kernel $K(x,dz)$ from the observation space $\mathbb R^p$ to the action space $\mathbb R^p$. Given $X=x$, its output has distribution $K(x,\cdot)$; deterministic measurable estimators are included as point-mass kernels. The rule may use the fixed center $m$ and the known $p,\sigma^2$, but cannot depend on the unknown $q$. Its randomization is parameter-independent conditional on $X$.

Write
\[
r_m(q,K)=\int_{\mathbb R^p}\int_{\mathbb R^p}\|z-q\|^2K(x,dz)\,N(q,\sigma^2I_p)(dx),
\qquad
R_m^*=\inf_K\sup_{q\in\mathbb R^p}r_m(q,K).
\]
A rule is minimax if its supremum risk equals $R_m^*$. It is inadmissible if another allowed rule has no greater risk for every $q$ and strictly smaller risk for at least one $q$.

Let $D_t=\|g_t-m_{t-1}\|^2$ and define
\[
\widehat q_t^{+}=m_{t-1}+\left[1-\frac{(p-2)\sigma^2}{D_t}\right]_+(g_t-m_{t-1}),
\]
where $[x]_+=\max\{x,0\}$ and the multiplier is defined as $0$ when $D_t=0$. In the fixed-center experiment, denote the corresponding deterministic rule by
\[
\delta_m^+(x)=m+\left[1-\frac{(p-2)\sigma^2}{\|x-m\|^2}\right]_+(x-m),
\]
with the same convention at $x=m$. The unrestricted rule is $\delta_0(x)=x$, corresponding to the estimator $g_t$.

## Task

Prove that, for every fixed center $m\in\mathbb R^p$,
\[
R_m^*=p\sigma^2.
\]
Prove that $\delta_m^+$ has risk at most $p\sigma^2$ for every $q\in\mathbb R^p$, with strict inequality whenever $q\ne m$, while $\delta_0$ has constant risk $p\sigma^2$. Conclude that both rules are minimax and that the unrestricted rule is inadmissible.

Finally, prove the corresponding conditional-risk statements almost surely:
\[
R_t(\widehat q_t^+)\le R_t(g_t)=p\sigma^2,
\]
with strict inequality on $\{q_t\ne m_{t-1}\}$. In particular, the conditional-risk inequality is strict almost surely on every positive-probability event contained in this set.
