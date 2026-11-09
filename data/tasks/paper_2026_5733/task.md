# Problem

## Setup

Let $n,r$ be integers with $1\le r\le n$, and define
$$
\operatorname{St}(n,r)=\{U\in\mathbb R^{n\times r}:U^{\mathsf T}U=I_r\},
$$
whose tangent space at $U$ is
$$
T_U\operatorname{St}(n,r)=\{E\in\mathbb R^{n\times r}:U^{\mathsf T}E+E^{\mathsf T}U=0\}.
$$
Let $A\in\mathbb R^{r\times r}$ be symmetric positive definite, with an orthogonal eigendecomposition
$$
A=R\operatorname{diag}(d_1,\ldots,d_r)R^{\mathsf T},
\qquad R^{\mathsf T}R=I_r,
\qquad d_i>0.
$$
Write $A^{1/2}$ for its principal positive-definite square root, and define
$$
\Psi(U,A)=UA^{1/2}.
$$
Fix $\bar U\in\operatorname{St}(n,r)$ and put $\bar M=\Psi(\bar U,A)$. For each $i\in\{1,\ldots,r\}$, suppose that $E_i\in T_{\bar U}\operatorname{St}(n,r)$ and $e_i\in\mathbb R^n$ satisfy
$$
\|E_i\|_F=1,
\qquad E_i r_j=0\ (j\ne i),
\qquad E_i r_i=e_i,
\qquad \|e_i\|_2=1,
$$
where $r_i$ is the $i$th column of $R$. Define
$$
Z_i=d_i^{-1/2}D_U\Psi(\bar U,A)[E_i].
$$

Let $\ell:\mathcal V\to\mathbb R$ be twice continuously differentiable on an open matrix-space neighborhood $\mathcal V$ of $\bar M$. Define the fixed-$A$ objective
$$
g_A(U)=\ell(UA^{1/2})
$$
wherever $UA^{1/2}\in\mathcal V$. Assume that $\bar U$ is a local minimizer of $g_A$ on $\operatorname{St}(n,r)$, and that the matrix-space Hessian satisfies
$$
\nabla^2\ell(\bar M)[Z_i,Z_j]=h_i\,\delta_{ij},
\qquad h_1\ge\cdots\ge h_r>0.
$$
Define
$$
m_A=\min_i d_i h_i,
\qquad L_A=\max_i d_i h_i,
\qquad K_A=\frac{L_A}{m_A},
\qquad K_0=\frac{h_1}{h_r}.
$$

Fix a smooth local coordinate parametrization $\varphi:\Omega\to\mathcal N$, which is a diffeomorphism onto a neighborhood $\mathcal N$ of $\bar U$ in $\operatorname{St}(n,r)$. Here $\Omega$ is an open convex neighborhood of $0$ in $\mathbb R^q$, with $q=\dim T_{\bar U}\operatorname{St}(n,r)$, and $\varphi(0)=\bar U$. The chart is adapted to the given tangent directions: for an orthonormal family $\varepsilon_1,\ldots,\varepsilon_r\in\mathbb R^q$,
$$
D\varphi(0)[\varepsilon_i]=E_i,
\qquad i=1,\ldots,r.
$$
Assume that $UA^{1/2}\in\mathcal V$ for every $U\in\mathcal N$. Set
$$
\widetilde g(x)=g_A(\varphi(x)),\qquad x\in\Omega,
$$
and assume that $\widetilde g$ is $m_A$-strongly convex and $L_A$-smooth on $\Omega$, with respect to its Euclidean coordinates.

Starting from $x_0\in\Omega$, consider the deterministic iteration
$$
x_{t+1}=x_t-\frac1{L_A}\nabla\widetilde g(x_t),
\qquad t=0,1,\ldots,
$$
where the gradient is the Euclidean coordinate gradient. Assume that every iterate belongs to $\Omega$. Let
$$
U_t=\varphi(x_t),\qquad g_*=g_A(\bar U).
$$

## Task

Prove that, for every integer $T\ge0$,
$$
g_A(U_T)-g_*
\le
\left(1-K_A^{-1}\right)^T\bigl(g_A(U_0)-g_*\bigr).
$$
For $T=0$, a contraction factor raised to the zeroth power is interpreted as $1$, including when the factor is zero.

Moreover, prove that if there are finite constants $0<a\le b$ such that
$$
\frac{a}{h_i}\le d_i\le\frac{b}{h_i}
\qquad\text{for every }i,
$$
then $K_A\le b/a$. Conclude that if $b/a\le K_0$, the resulting contraction factor is no worse than the factor associated with $K_0$.
