# Problem

## Setup

Let \(d\) and \(K\) be positive integers. Let \(X=\mathbb R^d\), and let \(\mathbb S^d\) be the real self-adjoint \(d\times d\) operators with Frobenius inner product. Let \(\mathcal V\subseteq\mathbb S^d\) be a linear subspace containing \(I\), closed under \(H F H\) for \(H,F\in\mathcal V\). Let \(\Pi:\mathbb S^d\to\mathcal V\) be the orthogonal projection, and assume \(A\succeq0\Rightarrow\Pi(A)\succeq0\).

For \(v\in X\), write \(\operatorname{rk}(v)=vv^\top\), and define
\[
q(v)=\left\|\sqrt{\Pi(\operatorname{rk}(v))}\right\|_{\mathrm{op}},
\qquad
q_*(v)=\left\|\sqrt{\Pi(\operatorname{rk}(v))}\right\|_{\mathrm{tr}}.
\]
Fix \(R>0\), \(\varepsilon>0\), and arbitrary vectors \(h_0,\ldots,h_{K-1}\in X\). Set \(T_0=\varepsilon^2I\), \(M_{-1}=0\), and for \(k=0,\ldots,K-1\),
\[
M_k=M_{k-1}+h_k,\qquad T_{k+1}=T_k+\Pi(\operatorname{rk}(h_k)),
\]
\[
\Phi_k(z)=R\,\operatorname{tr}\!\left(\sqrt{\Pi(\operatorname{rk}(z))+T_{k+1}}\right),
\qquad y_{k+1}=-\nabla\Phi_k(M_k),
\]
with \(y_0=0\). Define
\[
\mathsf{Reg}_K=\sup_{q(u)\le R}\sum_{k=0}^{K-1}\langle h_k,y_k-u\rangle .
\]

## Task

Prove that there is a universal constant \(C\) such that, for every positive integer \(K\), every sequence \((h_k)\), and every \(\varepsilon>0\),
\[
\mathsf{Reg}_K\le C R\left(\varepsilon d+q_*(h_0)+\operatorname{tr}\sqrt{T_K}\right).
\]
No uniform bound on the vectors \(h_k\) may be assumed. Conclude that the dimension-dependent term can be made arbitrarily small by choosing \(\varepsilon\) arbitrarily small.
