# Problem

## Setup

Let $L,\widetilde L\in\mathbb R^{n\times n}$ be symmetric positive-semidefinite matrices, and let $0<\varepsilon<1$ satisfy
\[
(1-\varepsilon)L\preceq \widetilde L\preceq (1+\varepsilon)L.
\]
Assume $\|L\|_2,\|\widetilde L\|_2\le B_L$. Fix a depth-$K$ network with widths $d_0,\ldots,d_K$, input $X\in\mathbb R^{n\times d_0}$, and weights $W_k\in\mathbb R^{d_k\times d_{k+1}}$ satisfying $\|X\|_F\le B_X$ and $\|W_k\|_2\le B_W$. For each $k=0,\ldots,K-1$, let
\[
p_k(t)=\sum_{r=0}^{d_k^p}a_{k,r}t^r
\]
be a finite-degree real polynomial, and let $\sigma_k:\mathbb R\to\mathbb R$ be applied entrywise and be $L_{\sigma_k}$-Lipschitz. Define
\[
H^{(0)}=\widetilde H^{(0)}=X,\qquad H^{(k+1)}=\sigma_k\!\left(p_k(L)H^{(k)}W_k\right),
\]
\[
\widetilde H^{(k+1)}=\sigma_k\!\left(p_k(\widetilde L)\widetilde H^{(k)}W_k\right),
\]
and set $Z=H^{(K)}$, $\widetilde Z=\widetilde H^{(K)}$. The architecture, polynomial coefficients, widths, Lipschitz constants, and the values $\sigma_k(0)$ are fixed independently of $\varepsilon$.

## Task

Prove that there exist constants $C_2,C_F>0$, independent of $\varepsilon$, such that
\[
\|ZZ^\top-\widetilde Z\widetilde Z^\top\|_2\le C_2\varepsilon
\quad\text{and}\quad
\|ZZ^\top-\widetilde Z\widetilde Z^\top\|_F\le C_F\varepsilon.
\]
Conclude that the sparsifier preserves the final embedding Gram matrix, and hence the representation geometry encoded by its operator and Frobenius norms, up to $O(\varepsilon)$.
