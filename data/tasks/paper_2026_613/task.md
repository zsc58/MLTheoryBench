# Problem

## Setup

Fix a positive integer feature dimension $d$. For each prompt, draw a latent vector $m\in\mathbb R^d$ from a distribution absolutely continuous with respect to $d$-dimensional Lebesgue measure, and draw an independent scalar $\zeta$ with mean $0$, variance $1$, and an atomless law. Let
\[
\underline m=\operatorname*{ess\,inf}\|m\|^2,
\qquad
\overline m=\operatorname*{ess\,sup}\|m\|^2,
\]
with $\underline m<\overline m<\infty$. Conditional on $(m,\zeta)$, generate an infinite sequence using mutually independent $u_i\sim N(0,1)$ and $\mu_i\sim N(0,I_d)$, and set
\[
x_i=u_i m+\mu_i,\qquad y_i=\zeta u_i.
\]
For each positive integer context length $L$, write $X=[x_1,\ldots,x_L]\in\mathbb R^{d\times L}$ and $y=(y_1,\ldots,y_L)^\top$. A query $(x_q,y_q)$ is generated in the same way, independently of the context sequence conditional on $(m,\zeta)$. Use the first $L$ context pairs and hold this query and the latent variables fixed as context length and depth vary. Define
\[
\Lambda=I_d+mm^\top,
\qquad
w=\frac{\zeta m}{1+\|m\|^2},
\qquad
y_q^{\mathrm{Bayes}}=w^\top x_q.
\]
The in-context criterion is almost-sure convergence of the query prediction to $y_q^{\mathrm{Bayes}}$ as the test-context length $L\to\infty$.

For the single-layer baseline, form
\[
E_X=\begin{pmatrix}X&x_q\\ y^\top&0\end{pmatrix}
\]
and, for fixed matrices $W^{PV},W^{KQ}\in\mathbb R^{(d+1)\times(d+1)}$, define
\[
\operatorname{LSA}(E_X)=E_X+W^{PV}E_X\left(E_X^\top W^{KQ}E_X/L\right).
\]
Its query prediction is the bottom-right entry.

For the deep linearized architecture, let $T$ be a positive integer, let $F_0=0\in\mathbb R^{d\times L}$, and for $t=1,\ldots,T$ define
\[
F_t=F_{t-1}+\alpha X+\beta(XX^\top/L)F_{t-1},
\]
where the same scalars $(\alpha,\beta)$ are used at every layer. The query readout is
\[
\widehat y_{L,T,\alpha,\beta}=\frac1L y^\top F_T^\top x_q.
\]
Restrict to one parameter by setting $\beta=-\alpha$. For each depth $T$, define the limiting population loss by
\[
\ell_T(\alpha)=\lim_{L\to\infty}\mathbb E\!\left[\left(\widehat y_{L,T,\alpha,-\alpha}-y_q\right)^2\right],
\]
where the expectation is over the prompt latent variables, the context, and the query. Existence and finiteness of this limit for every real $\alpha$ are part of the claim below. Train $\alpha$ by gradient flow $\dot\alpha_s=-\ell_T'(\alpha_s)$ from an arbitrary real initialization, and denote its limiting value by $\alpha_T^*$ when the limit exists.

## Task

Prove the following integrated theorem.

1. For every fixed choice of $W^{PV},W^{KQ}$, the single-layer predictor fails the in-context criterion:
\[
\mathbb P\!\left(\lim_{L\to\infty}\operatorname{LSA}(E_X)_{d+1,L+1}=y_q^{\mathrm{Bayes}}\right)=0.
\]

2. For the one-parameter deep architecture, $\ell_T$ is finite and differentiable on $\mathbb R$ for every positive integer $T$. Gradient flow exists for all $s\ge0$ and converges for every initialization to the unique minimizer $\alpha_T^*$ of $\ell_T$; moreover
\[
\alpha_T^*\longrightarrow \alpha_\infty^*
=\frac{2}{2+\underline m+\overline m},
\]
and the trained predictor is Bayes optimal in the sequential limits
\[
\lim_{T\to\infty}\lim_{L\to\infty}
\widehat y_{L,T,\alpha_T^*,-\alpha_T^*}
=y_q^{\mathrm{Bayes}}
\quad\text{almost surely}.
\]
