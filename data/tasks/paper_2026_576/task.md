# Problem

## Setup

Let \(G=(V,E)\) be a connected undirected simple graph with \(n\ge2\) vertices. Let \(A\in\mathbb R^{n\times n}\) be its symmetric adjacency matrix, \(D=\operatorname{diag}(d_i)\) with \(d_i=\sum_jA_{ij}\), and let \(L=D-A\in\mathbb R^{n\times n}\) be the combinatorial Laplacian. Write \(\mathbf 1\in\mathbb R^n\) for the all-ones vector. The eigenvalues of \(L\) satisfy
\[
0=\lambda_1<\lambda_2\le\cdots\le\lambda_n,
\]
and define the projector \(\Pi=\mathbf 1\mathbf 1^T/n\in\mathbb R^{n\times n}\).

For \(s\ge0\), define the heat kernel \(H_s=\exp(-sL)\) and, for any \(Y_0\in\mathbb R^{n\times n}\), the matrix diffusion \(Y_s=H_sY_0H_s\). Fix \(T>0\). Let \(X(t)\in\mathbb R^{n\times n}\) solve the formal reverse equation
\[
\frac{d}{dt}X(t)=T\bigl(LX(t)+X(t)L\bigr),\qquad 0\le t\le1,
\]
with \(X(0)=X_0\in\mathbb R^{n\times n}\). Assume
\[
X_0=\Pi+X_\perp,\qquad X_\perp\in\mathbb R^{n\times n},\qquad \mathbf 1^TX_\perp=0,\qquad X_\perp\mathbf 1=0.
\]
Use the Frobenius norm \(\|M\|_F=(\sum_{i,j}|M_{ij}|^2)^{1/2}\).

## Task

Prove that the terminal state \(X_1=X(1)\) satisfies
\[
X_1=e^{TL}X_0e^{TL}
\quad\text{and}\quad
\|X_1\|_F\ge e^{2T\lambda_2}\,\|X_\perp\|_F.
\]
