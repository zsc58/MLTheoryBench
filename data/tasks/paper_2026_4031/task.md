# Problem

## Setup

Fix $\alpha>0$, $c_0>1$, horizon $T>0$, observation noise $\sigma>0$, and $\omega\ge c_0\alpha$. Let $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and let $P$ be the path law on $C([0,T];\mathbb R^2)$ of
\[
dX_t=(-\alpha I_2+\omega J)X_t\,dt+dW_t,
\qquad X_0\sim p_0=N(\mu_0,V_0),
\]
where $\mu_0\in\mathbb R^2$ and the symmetric positive-definite matrix $V_0\in\mathbb R^{2\times2}$ are fixed, and $W$ is a standard two-dimensional Brownian motion independent of $X_0$.

For a positive integer $N$, observe $Y_n=X_{t_n}+\varepsilon_n$ at fixed times $0<t_1<\cdots<t_N\le T$, where $\varepsilon_n\stackrel{\rm iid}{\sim}N(0,\sigma^2I_2)$ independently of the latent process. Condition on fixed $y=(y_1,\ldots,y_N)\in(\mathbb R^2)^N$. Write $Q^*$ for the resulting posterior path law and $p(y)$ for the prior marginal density of the observations evaluated at $y$.

A candidate law $Q$ is a diffusion path law with Gaussian marginals $N(m(t),S(t))$, where $m:[0,T]\to\mathbb R^2$ and $S:[0,T]\to\mathbb R^{2\times2}$ are continuously differentiable and $S(t)$ is symmetric positive definite for every $t$. It has unit diffusion, initial law $N(m(0),S(0))$, and actual drift
\[
b_Q(x,t)=\dot m(t)+B(t)(x-m(t)).
\]
Its covariance therefore obeys $\dot S=BS+SB^{\mathsf T}+I_2$. The symmetric gauge chooses the symmetric solution $B=B^{\mathsf T}$; the square-root gauge, with $L=S^{1/2}$ the principal square root, chooses
\[
B=\dot L\,L^{-1}-\tfrac12S^{-1}.
\]

## Task

Prove that every such $Q$ in either gauge family satisfies
\[
\operatorname{KL}(Q\|Q^*)
\ge
\min\!\left\{\frac18,\frac{1-1/(2c_0)}{2\sqrt2}\right\}T\omega
-\frac1{2\sqrt2}+C_{\rm OU},
\]
where $C_{\rm OU}=\log p(y)+N\log(2\pi\sigma^2)$. Moreover, under stationary initialization $p_0=N(0,(2\alpha)^{-1}I_2)$, prove that $C_{\rm OU}$ is bounded below by a constant independent of $\omega$, for fixed $\alpha,\sigma,T,\{t_n\},N,y$.
