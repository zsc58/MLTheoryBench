# Problem

## Setup

Fix an integer depth \(L\ge1\), dimensions \(d_0,\ldots,d_L\) with each hidden width \(d_i\ge r:=\min(d_0,d_L)\), a regularization parameter \(\lambda>0\), and a target matrix \(X\in\mathbb R^{d_L\times d_0}\). For factors \(W_i\in\mathbb R^{d_i\times d_{i-1}}\), define
\[
F(W_1,\ldots,W_L)=\|X-W_L\cdots W_1\|_F^2+\frac{\lambda}{L}\sum_{i=1}^L\|W_i\|_F^2.
\]
Let \(\Omega=\operatorname*{argmin}F\), let \(N=\sum_{i=1}^L d_id_{i-1}\), and write the singular values of \(X\) in nonincreasing order as \(\sigma_1(X)\ge\cdots\ge\sigma_r(X)\ge0\). Put \(q=2/L\). If \(L\ge3\), define
\[
\tau=\Bigl(1-\frac q2\Bigr)\lambda^{1/(2-q)}(1-q)^{(q-1)/(2-q)},
\qquad E=\bigcup_{j=1}^r\{X:\sigma_j(X)=\tau\};
\]
if \(L=1\) or \(2\), set \(E=\varnothing\). For \(W\in\Omega\), write \(P(W)=W_L\cdots W_1\).

## Task

Prove the following integrated theorem. The exceptional set \(E\) has Lebesgue measure zero. For every \(X\notin E\), there is a unique matrix \(P^*\) such that
\[
\{P(W):W\in\Omega\}=\{P^*\}.
\]
Moreover, there is a number \(g^*\ge0\), independent of \(W\in\Omega\), such that \(\|W_i\|_F=g^*\) for every minimizer \(W\) and every layer \(i\). For every \(W\in\Omega\), with the convention that \(\|P^*\|_F^2/(g^*)^2:=0\) when \(g^*=0\), prove
\[
\operatorname{tr}\!\left(\nabla^2F(W)\right)
\ge \frac{2\lambda}{L}N+\frac{2L\|P^*\|_F^2}{(g^*)^2}.
\]
