# Problem

## Setup

Let $\mathcal S$ and $\mathcal A$ be nonempty finite sets, let $n=|\mathcal S||\mathcal A|$, let $r:\mathcal S\times\mathcal A\to\mathbb R$ be bounded, let $p(\cdot\mid s,a)$ be transition probabilities on $\mathcal S$, and fix $\gamma\in(0,1)$. Identify $Q$-functions with vectors in $\mathbb R^n$ and define
\[
(FQ)(s,a)=r(s,a)+\gamma\sum_{s'\in\mathcal S}p(s'\mid s,a)\max_{b\in\mathcal A}Q(s',b).
\]
The operator $F$ has a unique fixed point $Q^\star$, is a $\gamma$-contraction in $\|\cdot\|_\infty$, and satisfies $F(Q+c\mathbf1)=F(Q)+\gamma c\mathbf1$.

For a stochastic stationary policy $\mu$, meaning that $\mu(b\mid s)\ge0$ and $\sum_{b\in\mathcal A}\mu(b\mid s)=1$ for every $s$, define
\[
(B_\mu Q)(s,a)=\sum_{s'}p(s'\mid s,a)\sum_b\mu(b\mid s')Q(s',b),
\qquad A_\mu=\gamma B_\mu.
\]
Each $B_\mu$ is row-stochastic. A deterministic policy is a map $\pi:\mathcal S\to\mathcal A$, identified with $\mu(b\mid s)=\mathbf1_{\{b=\pi(s)\}}$; deterministic policies are the extreme points of this policy family.

For a nonempty bounded family $\mathcal M$ of linear maps on a finite-dimensional Euclidean space $V$, define its joint spectral radius (JSR) by
\[
\rho(\mathcal M)=\lim_{m\to\infty}\left(\sup_{T_1,\ldots,T_m\in\mathcal M}\|T_m\cdots T_1\|_{\mathrm{op},2}\right)^{1/m}.
\]
Here $\|T\|_{\mathrm{op},2}=\sup_{\|v\|_2\le1}\|Tv\|_2$. In particular, on $V=\{0\}$ this norm and the JSR are zero.

Let $\mathbf1\in\mathbb R^n$ be the all-ones vector, $\Pi_\perp=I-(1/n)\mathbf1\mathbf1^T$, and $H=\mathbf1^\perp$. For deterministic policies $\pi$, set $\bar A_\pi=(\Pi_\perp A_\pi\Pi_\perp)|_H$ and define
\[
\bar\rho=\rho(\{\bar A_\pi:\pi\text{ deterministic}\}).
\]
For stochastic $\mu$, set $\bar A_\mu=(\Pi_\perp A_\mu\Pi_\perp)|_H$ and define the row functional and block operator
\[
\ell_\mu=\frac{1}{n(1-\gamma)}\mathbf1^TA_\mu,
\qquad
D_\mu=\begin{bmatrix}0&\ell_\mu|_H\\0&\bar A_\mu\end{bmatrix}:\mathbb R\oplus H\longrightarrow\mathbb R\oplus H.
\]
Let $\rho_{\rm def}$ be the JSR of $\{D_\mu:\mu\text{ stochastic stationary}\}$, using the Euclidean direct-sum space $\mathbb R\oplus H$.

For any initial vector $Q_0\in\mathbb R^n$, define, for integers $k\ge0$,
\[
Q_{k+1}=F(Q_k)+\frac{\gamma}{1-\gamma}\bar r_k\mathbf1,
\qquad \bar r_k=\frac1n\mathbf1^T(F(Q_k)-Q_k).
\]

## Task

Prove that $\rho_{\rm def}=\bar\rho\le\gamma$. Moreover, for every $\varepsilon\in(0,1-\bar\rho)$, with $\beta=\bar\rho+\varepsilon$, prove that there exists $C_\beta>0$, allowed to depend on the fixed model and $\beta$ but independent of $Q_0$ and $k$, such that for every $Q_0\in\mathbb R^n$,
\[
\|Q_k-Q^\star\|_2\le C_\beta\beta^{k-1}\|\Pi_\perp(Q_0-Q^\star)\|_2\quad\text{for all }k\ge1,
\]
and therefore
\[
\limsup_{k\to\infty}\|Q_k-Q^\star\|_2^{1/k}\le\bar\rho.
\]
In particular, the asymptotic rate is strictly below $\gamma$ whenever $\bar\rho<\gamma$.
