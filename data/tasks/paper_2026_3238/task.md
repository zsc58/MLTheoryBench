# Problem

## Setup

Let $d\ge2$ be an integer, and let
\[
O_d=\{W\in\mathbb R^{d\times d}:W^\top W=I_d\}
\]
be the real orthogonal group, where $I_d$ is the identity matrix. Let $S=(S_1,\ldots,S_d)$ have mutually independent real-valued coordinates with $\mathbb E S_k=0$ and $\mathbb E S_k^2=1$; assume that at most one coordinate distribution is Gaussian. Let $W^*\in O_d$ and observe
\[
X=(W^*)^{-1}S.
\]
All laws have finite second moments. Write $\mathcal L(Y)$ for the law of a random variable or vector $Y$, and let $\mathcal P_2(\mathbb R)$ denote the Borel probability laws on $\mathbb R$ with finite second moment. For $\mu,\nu\in\mathcal P_2(\mathbb R)$, define the quadratic Wasserstein distance by
\[
W_2^2(\mu,\nu)=\inf_{\lambda\in\Pi(\mu,\nu)}\int_{\mathbb R^2}|u-v|^2\,d\lambda(u,v),
\]
where $\Pi(\mu,\nu)$ is the set of probability laws on $\mathbb R^2$ with marginals $\mu$ and $\nu$. Write $\gamma=N(0,1)$. For a unit vector $w$, let $\pi_w(x)=w^\top x$ and let $(\pi_w)_\#\mathcal L(X)=\mathcal L(w^\top X)$ be the pushforward law. Define, for $W\in O_d$ with rows $w_1^\top,\ldots,w_d^\top$,
\[
F(W)=\sum_{j=1}^d W_2^2\!\left((\pi_{w_j})_\#\mathcal L(X),\gamma\right).
\]
A signed permutation matrix is an orthogonal matrix having exactly one nonzero entry, equal to $\pm1$, in each row and column.

## Task

Prove that
\[
\operatorname*{arg\,max}_{W\in O_d}F(W)
=\{MW^*:\ M\text{ is a signed permutation matrix}\}.
\]
