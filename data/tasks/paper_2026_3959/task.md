# Problem

## Setup

Let \(d,m,N\) be positive integers, and let \(x_i\in\mathbb R^d\), \(u_i\in\mathbb R^m\), and \(\dot x_i\in\mathbb R^d\) be given for \(i=1,\ldots,N\). All spaces are real. For a self-adjoint operator, \(\succeq0\) denotes positive semidefiniteness.

Let \(\mathcal H_h\) be a scalar RKHS on \(\mathbb R^d\) with a twice continuously differentiable kernel \(h\). Put \(V=\mathbb R^{d\times m}\), equipped with its Frobenius inner product, and let \(\mathcal G\) be a \(V\)-valued RKHS on \(\mathbb R^d\) with kernel \(g(x,y)\in\mathscr B(V)\). Thus \(B\in\mathcal G\) takes values in matrices acting on \(u\in\mathbb R^m\).

Let \(\mathcal W\) be a real separable Hilbert space and let \(\psi(x)\in\mathscr B(\mathbb R^d,\mathcal W)\) be a fixed feature map. Put
\[
 k(x,y)=\psi(x)^*\psi(y),\qquad D(x)=\psi(x)^*Q\psi(x),
\]
where \(Q\) is Hilbert--Schmidt and satisfies \(Q+Q^*\succeq0\). Neither \(Q\) nor \(D(x)\) is required to be self-adjoint; the constraint gives \(D(x)+D(x)^\top\succeq0\).

Consider models
\[
 \dot x=-D(x)\nabla E(x)+B(x)u.
\]
For \(\alpha,\beta,\gamma>0\), minimize over \(Q,E,B\) in the domains just specified:
\[
 \sum_{i=1}^N\|\dot x_i+D(x_i)\nabla E(x_i)-B(x_i)u_i\|^2
 +\alpha\|Q\|_{\rm HS}^2+\beta\|E\|_{\mathcal H_h}^2+\gamma\|B\|_{\mathcal G}^2.
\tag{I}
\]

Use the following finite-dimensional notation. Let \(\mathbf K=[k(x_i,x_j)]_{i,j}\in\mathbb R^{dN\times dN}\). Set
\[
 \ell_j(x)=\nabla_2h(x,x_j),\qquad
 E_a(x)=\sum_{j=1}^N\ell_j(x)^\top a_j,
 \qquad a=(a_1,\ldots,a_N)\in(\mathbb R^d)^N.
\]
Let \(\mathbf L\in\mathbb R^{dN\times dN}\) have blocks with entries
\[
 (\mathbf L_{ij})_{rs}=\partial_{1,r}\partial_{2,s}h(x_i,x_j),
 \qquad 1\leq r,s\leq d,
\]
and write \(L_i\) for its \(i\)-th block row. Let \(\mathbf R=[g(x_i,x_j)]_{i,j}\) act on \(V^N\), and let
\[
 K_i=[k(x_i,x_1)\ \cdots\ k(x_i,x_N)].
\]
For \(\Lambda\in\mathbb R^{dN\times dN}\), with blocks \(\Lambda_{rs}\in\mathbb R^{d\times d}\), and \(b=(b_1,\ldots,b_N)\in V^N\), define
\[
 Q_\Lambda=\sum_{r,s=1}^N\psi(x_r)\Lambda_{rs}\psi(x_s)^*,
 \qquad
 D_\Lambda(x)=\sum_{r,s=1}^N k(x,x_r)\Lambda_{rs}k(x,x_s)^\top,
\]
\[
 B_b(x)=\sum_{j=1}^N g(x,x_j)b_j,
 \qquad \mathcal U_i b=B_b(x_i)u_i.
\]
All finite product spaces have their Euclidean or Frobenius product inner products. In particular, write \(\langle b,\mathbf Rb\rangle\) for the quadratic form on \(V^N\).

Define the finite program
\[
 \begin{aligned}
 \min_{\Lambda+\Lambda^\top\succeq0,\ a\in\mathbb R^{dN},\ b\in V^N}\quad
 &\sum_{i=1}^N\|\dot x_i+K_i\Lambda K_i^\top L_i a-\mathcal U_i b\|^2\\
 &+\alpha\operatorname{tr}(\mathbf K\Lambda\mathbf K\Lambda^\top)
 +\beta a^\top\mathbf L a+\gamma\langle b,\mathbf Rb\rangle.
 \end{aligned}
\tag{P}
\]
Let \(J(\Lambda,a,b)\) denote its objective and \(\mathcal C\) its feasible coefficient set. A point \(z^*\in\mathcal C\) is called stationary for (P) if
\[
 \langle\nabla J(z^*),z-z^*\rangle\geq0
 \quad\text{for every }z\in\mathcal C,
\]
where the gradient uses the product inner product.

For the iteration below, introduce \(p\in\mathbb R^N\) and write
\[
 f(p,\Lambda,a,b)=p^\top p+\alpha\operatorname{tr}(\mathbf K\Lambda\mathbf K\Lambda^\top)
 +\beta a^\top\mathbf L a+\gamma\langle b,\mathbf Rb\rangle.
\]
For each \(i\), define \((d+1)\)-by-\((d+1)\) block matrices
\[
 X_i(\Lambda)=\begin{bmatrix}K_i\Lambda^\top K_i^\top&0\\0&0\end{bmatrix},\quad
 Y_i(a)=\begin{bmatrix}0&L_i a\\0&0\end{bmatrix},\quad
 Z_i(b)=\begin{bmatrix}0&\dot x_i-\mathcal U_i b\\(\dot x_i-\mathcal U_i b)^\top&0\end{bmatrix},
\]
\[
 \mathsf A_i(\Lambda,a)=X_i(\Lambda)^\top X_i(\Lambda)+Y_i(a)^\top Y_i(a),
 \qquad
 \mathsf B_i(\Lambda,a)=(X_i(\Lambda)-Y_i(a))^\top(X_i(\Lambda)-Y_i(a)).
\]
For \(\theta=(p,\Lambda,a,b)\) in
\(\mathbb R^N\times\mathbb R^{dN\times dN}\times\mathbb R^{dN}\times V^N\), let
\[
 \mathsf A_i^\theta(\Lambda',a')=-\mathsf A_i(\Lambda,a)
 +X_i(\Lambda')^\top X_i(\Lambda)+X_i(\Lambda)^\top X_i(\Lambda')
 +Y_i(a')^\top Y_i(a)+Y_i(a)^\top Y_i(a').
\]
Let \(C(\theta)\) be the set of \(\theta'=(p',\Lambda',a',b')\) in the same product space satisfying
\[
 \Lambda'+\Lambda'^\top\succeq0,
 \qquad
 \mathsf B_i(\Lambda',a')-\mathsf A_i^\theta(\Lambda',a')-Z_i(b')-p'_iI_{d+1}\preceq0
 \quad(1\leq i\leq N).
\]
When \(f\) has a unique minimizer over \(C(\theta)\), denote it by \(S(\theta)\). Under the invertibility assumption in part 2, consider the iteration \(\theta^{t+1}=S(\theta^t)\), initialized at
\[
 \Lambda^0=I_{dN},\qquad a^0=b^0=0,\qquad p_i^0=\|\dot x_i\|^2+1.
\]

## Task

Prove the following integrated theorem.

1. Problem (I) has a global minimizer of the form \((Q,E,B)=(Q_\Lambda,E_a,B_b)\), with \(\Lambda+\Lambda^\top\succeq0\) and induced field \(D=D_\Lambda\). Its optimal value equals that of (P), and every minimizer of (P) reconstructs a global minimizer of (I) by these formulas.

2. If \(\mathbf K\), \(\mathbf L\), and \(\mathbf R\) are invertible on their respective finite-dimensional spaces, then \(f\) has a unique minimizer over \(C(\theta)\) for every base point \(\theta\). The generated sequence either converges to a tuple whose coefficient component \((\Lambda,a,b)\) is stationary for (P), or its accumulation points form a nonempty compact connected nonsingleton set, every member of which has a coefficient component stationary for (P).
