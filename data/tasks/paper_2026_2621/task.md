# Problem

## Setup

Work on $\mathbb R^n$ with $n\ge1$. Let $h$ be any probability density in $L^1(\mathbb R^n)$. Denote by $\varphi_{\Sigma}$ the centered Gaussian density with positive-definite covariance $\Sigma$, and define
\[
\mathcal G=\{\varphi_{\Sigma}*\mu:\ \Sigma\succ0,\ \mu\text{ is a compactly supported probability measure}\}.
\]
Let $\gamma$ be the standard Gaussian density. For an initial density $q$, consider the variance-preserving diffusion
\[
dX_t=-\tfrac12X_t\,dt+dW_t,
\qquad X_t=a(t)X_0+\sigma(t)Z,
\]
with $a(t)=e^{-t/2}$, $\sigma^2(t)=1-e^{-t}$, and $Z\sim\gamma$. Write $q_t$ for its density and $s_t=\nabla\log q_t$ for its score. Its probability-flow ODE is
\[
\dot x=v_t(x),\qquad v_t(x)=-\tfrac12x-\tfrac12s_t(x),
\]
and let $\phi_{0\to T}$ denote its time-$T$ solution map when it exists.

## Task

Prove the following universal expressivity statement: for every $h$ and every $\varepsilon>0$, there exist $q\in\mathcal G$ and $T>0$ such that

1. there is a finite constant $M_T$ with
   \[
   \sup_{0\le t\le T,\,x\in\mathbb R^n}\|\nabla s_t(x)\|\le M_T,
   \]
   equivalently the scores are uniformly Lipschitz in space on $[0,T]$;
2. $\phi_{0\to T}$ is a bi-Lipschitz $C^1$ diffeomorphism of $\mathbb R^n$ and transports $q$ to $q_T$; and
3. the inverse Gaussian pullback approximates $h$ in $L^1$:
   \[
   \bigl\|h-(\phi_{0\to T}^{-1})_\#\gamma\bigr\|_1<\varepsilon.
   \]

Here $\# $ denotes pushforward of measures/densities.
