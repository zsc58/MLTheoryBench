# Problem

## Setup

Let k be a known positive integer. Let C in {1,...,k} be a latent class, let T in {0,1} be treatment, let Y^{(0)},Y^{(1)} be real-valued potential outcomes, and observe Y=Y^{(T)}. Let Z in R^{d_z} and X in R^{d_x} be reference and target proxies, where d_z and d_x are positive integers. Assume
\[
\mathbb E|Z_i|<\infty\quad(1\leq i\leq d_z),\qquad
\mathbb E|X_j|<\infty\quad(1\leq j\leq d_x),\qquad
\mathbb E|Y^{(t)}|<\infty\quad(t\in\{0,1\}).
\]
Assume also:

- $Z\perp (X,Y)\mid(T,C)$;
- $X\perp (Y,T)\mid C$;
- $Y^{(t)}\perp T\mid C$ for $t=0,1$;
- $\Pr(T=t)>0$ and $\Pr(C=u\mid T=t)>0$ for every $u$ and $t$;
- $d_z,d_x\ge k$, and the matrices $A_t\in\mathbb R^{d_z\times k}$ and $B\in\mathbb R^{d_x\times k}$, defined by $A_t[:,u]=\mathbb E[Z\mid C=u,T=t]$ and $B[:,u]=\mathbb E[X\mid C=u]$, have full column rank $k$;
- $X_1=1$ almost surely;
- the latent effects $\theta_u:=\mathbb E[Y^{(1)}\mid C=u]-\mathbb E[Y^{(0)}\mid C=u]$ are pairwise distinct.

For $t\in\{0,1\}$ define
\[
S_t=\mathbb E[ZX^\top\mid T=t],\qquad H_t=\mathbb E[ZX^\top Y\mid T=t].
\]

## Task

First prove that the vertically stacked matrix
\[
\begin{bmatrix}S_0\\S_1\end{bmatrix}\in\mathbb R^{2d_z\times d_x}
\]
has rank $k$.

Having established this, let $V\in\mathbb R^{d_x\times k}$ be any matrix with orthonormal columns spanning its row space. Define
\[
K_t=(S_tV)^\dagger(H_tV),\qquad L=K_1-K_0,
\]
where $\dagger$ is the Moore-Penrose pseudoinverse. Let $e_1\in\mathbb R^{d_x}$ be the first coordinate vector, $a^\top=\mathbb E[X]^\top V$, and $c=V^\top e_1$.

Prove that there is an invertible $R\in\mathbb R^{k\times k}$ with $B^\top=RV^\top$, and that
\[
K_t=R^{-1}G_tR,\qquad L=R^{-1}\operatorname{diag}(\theta_1,\dots,\theta_k)R,
\]
where $G_t=\operatorname{diag}(\mathbb E[Y\mid C=1,T=t],\dots,\mathbb E[Y\mid C=k,T=t])$. Consequently, the eigenvalues of $L$ are exactly the multiset $\{\theta_u\}_{u=1}^k$.

Show further that choosing one nonzero left eigenvector for each eigenvalue of $L$, in a fixed order, lifting the rows by multiplication by $V^\top$, and normalizing each lifted row by its first coordinate recovers the rows of $B^\top$ up to the corresponding permutation. Prove that these normalization denominators are nonzero and that the latent proportion vector $p=(\Pr(C=1),\dots,\Pr(C=k))^\top$ is uniquely recovered from $Bp=\mathbb E[X]$, with the same latent-label permutation.

Finally prove, for every integer $\ell\ge0$,
\[
a^\top L^\ell c=\mathbb E[\theta_C^\ell],
\]
and, for every $z\in\mathbb C$ satisfying $|z|\,\|L\|_2<1$,
\[
a^\top(I_k-zL)^{-1}c=\sum_{\ell\ge0}z^\ell\mathbb E[\theta_C^\ell],
\]
where $I_k$ is the $k\times k$ identity matrix and $\|\cdot\|_2$ is the Euclidean operator norm.
