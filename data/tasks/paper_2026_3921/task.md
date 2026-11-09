# Problem

## Setup

Fix positive integers $L,d_x,d_k,c$. Let $H_x\subset\mathbb R^{d_x}$ and $H\subset\mathbb R^{d_\theta}$ be nonempty compact sets, where $d_\theta=4d_xd_k$. Let $X=(x_1,\ldots,x_L)^\top$ have a fixed probability distribution supported on $H_x^L$, and let each $Y_l:H_x^L\to\mathbb R^c$ be a measurable one-hot label function.

Fix a matrix $W_{\rm out}\in\mathbb R^{d_x\times c}$. The head parameter is
\[
\theta=(W_Q,W_K,W_V,W_O),\qquad
W_Q,W_K,W_V\in\mathbb R^{d_x\times d_k},\quad
W_O\in\mathbb R^{d_k\times d_x},
\]
identified with a vector in $\mathbb R^{d_\theta}$. The matrix $W_{\rm out}$ is not a coordinate of $\theta$. All parameter gradients below are ambient Euclidean gradients with respect to these four head matrices.

Define
\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V,
\]
and let
\[
M_{rs}=\begin{cases}0,&s\le r,\\-\infty,&s>r.\end{cases}
\]
For a finite vector $a$, set $\operatorname{softmax}_j(a)=e^{a_j}/\sum_i e^{a_i}$. Row-wise softmax with the mask uses $e^{-\infty}=0$, so each row is normalized over its unmasked entries. Define
\[
A_\theta(X)=\operatorname{softmax}_{\rm row}\!\left(QK^\top/\sqrt{d_k}+M\right),\qquad
\Psi(X;\theta)=A_\theta(X)XW_VW_OW_{\rm out},
\]
and write $\psi_l(X;\theta)\in\mathbb R^c$ for its $l$th row.

Let $\mathcal P(H)$ denote the Borel probability measures supported on $H$. All parameter measures below belong to $\mathcal P(H)$. Equip this space with
\[
W_1(\rho,\nu)=\inf_{\pi\in\Pi(\rho,\nu)}\int_{H\times H}\|\theta-\eta\|\,\pi(d\theta,d\eta),
\]
where $\Pi(\rho,\nu)$ is the set of couplings with marginals $\rho$ and $\nu$.

For $\rho\in\mathcal P(H)$, set
\[
z_l^\rho(X)=\int_H\psi_l(X;\theta)\,\rho(d\theta),
\]
\[
\ell(y,z)=\log\!\sum_{j=1}^c e^{z_j}-y^\top z,\qquad
\mathcal E(\rho)=\mathbb E_X\left[\frac1L\sum_{l=1}^L\ell\bigl(Y_l(X),z_l^\rho(X)\bigr)\right].
\]
Define
\[
\Phi(\theta;\rho)=\mathbb E_X\left[\frac1L\sum_{l=1}^L
\left\langle\operatorname{softmax}(z_l^\rho(X))-Y_l(X),\psi_l(X;\theta)\right\rangle\right],
\]
\[
\mathcal I(\rho)=\int_H\|\nabla_\theta\Phi(\theta;\rho)\|^2\,\rho(d\theta).
\]

Let $\zeta:[0,\infty)\to[0,\infty)$ be bounded and Lipschitz, with
\[
\int_0^\infty\zeta(t)\,dt=\infty.
\]
Let $t\mapsto\rho_t\in\mathcal P(H)$ be a $W_1$-continuous weak solution of the ambient equation
\[
\partial_t\rho_t=2\zeta(t)\,\operatorname{div}_\theta\!\left(\rho_t\nabla_\theta\Phi(\theta;\rho_t)\right).
\]
Here weak solution means that, for every $f\in C^1(\mathbb R^{d_\theta})$ and every $0\le a\le b<\infty$,
\[
\int_H f\,d\rho_b-\int_H f\,d\rho_a
=-2\int_a^b\zeta(t)\int_H
\left\langle\nabla f(\theta),\nabla_\theta\Phi(\theta;\rho_t)\right\rangle\rho_t(d\theta)\,dt.
\]
Assume that $\{\rho_t:t\ge0\}$ is precompact in $W_1$.

A measure $\bar\rho\in\mathcal P(H)$ is called stationary if the constant curve $\rho_t\equiv\bar\rho$ is a weak solution of this equation. Let $\mathsf{Stat}$ be the set of stationary measures, and define
\[
\Omega=\left\{\bar\rho\in\mathcal P(H):\text{there exist }t_n\to\infty\text{ with }W_1(\rho_{t_n},\bar\rho)\to0\right\}.
\]

## Task

Prove the following integrated theorem.

1. The risk $\mathcal E(\rho_t)$ is non-increasing and has a finite limit, and $\mathcal I(\rho_t)\to0$.
2. For every $\bar\rho\in\mathcal P(H)$,
\[
\bar\rho\in\mathsf{Stat}
\quad\Longleftrightarrow\quad
\nabla_\theta\Phi(\theta;\bar\rho)=0\quad\bar\rho\text{-almost surely},
\]
which is also equivalent to
\[
\operatorname{supp}\bar\rho\subseteq
\{\theta\in H:\nabla_\theta\Phi(\theta;\bar\rho)=0\}.
\]
3. The set $\Omega$ is nonempty, compact, connected, and contained in $\mathsf{Stat}$.
4. If $\Omega\cap\mathsf{Stat}$ is totally disconnected, in particular if it is finite, then there is a single $\rho_\infty\in\mathsf{Stat}$ such that $W_1(\rho_t,\rho_\infty)\to0$ as $t\to\infty$.
