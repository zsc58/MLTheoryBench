# Problem

## Setup

Let $J\ge 2$ and let $(X,Y)$ be distributed with $Y\in\{1,\ldots,J\}$. Write $p_j^*(x)=\Pr(Y=j\mid X=x)$ and assume $p^*(x)$ lies in the interior of the $J$-simplex. A model with parameter $\theta$ outputs a probability vector $p(x;\theta)$ in the simplex interior, with $x\mapsto p(x;\theta)$ measurable for every $\theta$ (for example, via a softmax map).

For $\beta\ge 0$ and $\lambda\in\mathbb R$, define
\[
A=1+\lambda(1-\beta),\qquad B=\beta-\lambda(1-\beta),
\]
and let
\[
\mathcal T=\left\{(\beta,\lambda):0\le\beta<1,\ -\frac{1}{1-\beta}<\lambda<\frac{\beta}{1-\beta}\right\}\cup\left\{(1,\lambda):\lambda\in\mathbb R\right\}.
\]
For every $(\beta,\lambda)\in\mathcal T$, one has $A>0$ and $B>0$. For a one-hot vector $u=e_j$, define
\[
\ell_{\beta,\lambda}(u,p)=\frac1A\sum_{k=1}^J\left[p_k^{1+\beta}-\frac{1+\beta}{B}u_kp_k^B+\frac AB\right].
\]

The clean risk is
\[
R_{\beta,\lambda}(\theta)=\mathbb E\,\ell_{\beta,\lambda}(e_Y,p(X;\theta)).
\]
Under independent uniform label noise with rate $\eta$, the observed label $\widetilde Y$ equals $Y$ with probability $1-\eta$ and otherwise is chosen uniformly from the other $J-1$ classes. Thus
\[
\Pr(\widetilde Y=j\mid X=x)=(1-\eta)p_j^*(x)+\frac{\eta}{J-1}(1-p_j^*(x)).
\]
Define the contaminated risk
\[
R_{\beta,\lambda}^{(\eta)}(\theta)=\mathbb E\,\ell_{\beta,\lambda}(e_{\widetilde Y},p(X;\theta)),
\]
and assume global minimizers $\theta^*_{\beta,\lambda}$ of $R_{\beta,\lambda}$ and $\theta^{\eta}_{\beta,\lambda}$ of $R_{\beta,\lambda}^{(\eta)}$ exist.

## Task

For every $(\beta,\lambda)\in\mathcal T$ and every $0\le\eta<1-1/J$, prove
\[
0\le R_{\beta,\lambda}(\theta^{\eta}_{\beta,\lambda})-R_{\beta,\lambda}(\theta^*_{\beta,\lambda})
\le M_{\beta,\lambda}^{(\eta)},
\]
where
\[
M_{\beta,\lambda}^{(\eta)}=
\frac{\eta}{J-1-J\eta}\,\frac1A
\left[J-J^{1-\beta}+\frac{(1+\beta)\left|1-J^{1-B}\right|}{B}\right].
\]
