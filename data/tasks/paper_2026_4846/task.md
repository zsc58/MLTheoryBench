# Problem

## Setup

Let \(S\) be a finite set of size \(n\), and let \(P\) be the transition matrix of an irreducible, aperiodic Markov chain on \(S\). Let \(\pi\) be its stationary distribution, let \(W=\operatorname{diag}(\pi)\), and define
\[
\langle f,h\rangle_W=f^TWh,\qquad \|f\|_W=\sqrt{\langle f,f\rangle_W}.
\]
For a linear map \(B\), write \(\|B\|_{W\to W}=\sup_{f\ne0}\|Bf\|_W/\|f\|_W\). Let
\[
P^\dagger=W^{-1}P^TW,
\qquad
H=I-\frac{P+P^\dagger}{2}.
\]
Let \(r\in\mathbb R^S\), set \(\rho=\pi^Tr\) and \(g=r-\rho\mathbf 1\), and let \(v\) be the unique solution of
\[
 v=g+Pv,\qquad \pi^Tv=0.
\]

Let \(q_1,\ldots,q_n\) be a \(W\)-orthonormal eigenbasis of \(H\), with corresponding ordered eigenvalues
\[
0=\lambda_1\le\lambda_2\le\cdots\le\lambda_n.
\]
Fix \(1\le k<n\) such that \(\lambda_{k+1}>\lambda_k\). Suppose \(\widehat q_1,\ldots,\widehat q_k\) are \(W\)-orthonormal and, for some \(\epsilon>0\), satisfy
\[
\sum_{i=1}^k \widehat q_i^TWH\widehat q_i-\sum_{i=1}^k\lambda_i<\epsilon.
\]
Let \(\widehat U=\operatorname{span}\{\widehat q_1,\ldots,\widehat q_k\}\), and let \(\widehat v\) be the \(W\)-orthogonal projection of \(v\) onto \(\widehat U\).

## Task

Prove that
\[
\|v-\widehat v\|_W
\le
\frac{\|g\|_W}{\sqrt{\lambda_2\lambda_{k+1}}}
+
\|v\|_W\sqrt{\frac{2\epsilon}{\lambda_{k+1}-\lambda_k}}.
\]
