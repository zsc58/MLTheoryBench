# Problem

## Setup

Consider the discrete-time linear system
\[
x_{k+1}=Ax_k+Bu_k,
\]
with positive integer state and input dimensions $n$ and $m$, where $A\in\mathbb R^{n\times n}$ and $B\in\mathbb R^{n\times m}$. Fix an integer horizon $N\ge1$. Let $y\in\mathbb R^{Nm}$ stack the planned inputs and let $E\in\mathbb R^{m\times Nm}$ select its first block, so the applied input is $Ey$.

Let the safe set be the polyhedron
\[
X_0=\{x\in\mathbb R^n:Gx\le c\},
\]
where $G\in\mathbb R^{r\times n}$ and $c\in\mathbb R^r$. Here $r$ is a nonnegative integer. Let $P\in\mathbb R^{Nm\times Nm}$ be symmetric positive definite. Fix learned matrices $H\in\mathbb R^{s\times Nm}$, $W\in\mathbb R^{s\times n}$ and vector $b\in\mathbb R^s$, where $s$ is a nonnegative integer. For each state $x_0\in\mathbb R^n$ and reference input $\hat u\in\mathbb R^m$, assume the following QP is feasible and its optimum is attained, and denote its optimizer by $y^*(x_0,\hat u)$:
\[
\min_y\;\frac12y^\top Py-(E^\top\hat u)^\top y
\quad\text{subject to}\quad Hy+Wx_0+b\ge0.
\]
The learned safety-filter policy is $\pi(x_0,\hat u)=Ey^*(x_0,\hat u)$. Persistent safety means
\[
Ax_0+B\pi(x_0,\hat u)\in X_0
\quad\text{for every }x_0\in X_0\text{ and every }\hat u\in\mathbb R^m.
\]

For variables $x_0\in\mathbb R^n$, $\hat u\in\mathbb R^m$, $v\in\mathbb R^r$, $y\in\mathbb R^{Nm}$ and $\mu\in\mathbb R^s$, define the optimal value of the following QCQP as the extended-real infimum
\[
\begin{aligned}
z^*=\inf\;&-v^\top\bigl(G(Ax_0+BEy)-c\bigr)\\
\text{s.t. }&Gx_0\le c,\quad v\ge0,\quad \mathbf1^\top v=1,\\
&Py-E^\top\hat u-H^\top\mu=0,\\
&Hy+Wx_0+b\ge0,\quad \mu\ge0,\\
&\mu^\top(Hy+Wx_0+b)=0.
\end{aligned}
\]
The infimum of an empty feasible set is $+\infty$, and an objective unbounded below has value $-\infty$. Empty-vector sums and inner products are zero. Products in the complementarity constraint make this a generally nonconvex QCQP. Let $z_{\mathrm{SDP}}$ denote any certified SOS/semidefinite-relaxation lower bound satisfying $z_{\mathrm{SDP}}\le z^*$.

## Task

Prove that if $z^*\ge0$, then the learned safety-filter policy is persistently safe. Also prove that the practical certificate $z_{\mathrm{SDP}}\ge0$ is sufficient for persistent safety.
