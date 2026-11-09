# Problem

## Setup

Let \(L:\mathbb R^d\to\mathbb R\) be \(C^2\) and bounded below by \(L_{\inf}\). Fix \(\eta>0\), and let
\[
x_{k+1}=x_k-\eta\nabla L(x_k),\qquad s_k=x_{k+1}-x_k.
\]
For \(K\ge1\), set \(E_K=\sum_{k<K}\|s_k\|^2\). For each \(k\) with \(s_k\ne0\), define
\[
u_k=\frac{s_k}{\|s_k\|},\qquad
\widetilde H_k=2\int_0^1(1-t)\nabla^2L(x_k+t s_k)\,dt,
\qquad
\rho_k=u_k^\top\widetilde H_k u_k.
\]
For a symmetric matrix \(H\), let \(\lambda_{\max}(H)\) denote its largest eigenvalue. All sums involving \(\rho_k\) below range only over indices with \(s_k\ne0\).

## Task

Prove the following integrated claim. For every nonzero step \(s_k\), there is a \(\theta_k\in(0,1)\) such that
\[
\rho_k=u_k^\top\nabla^2L(x_k+\theta_k s_k)u_k.
\]
Moreover, for every \(K\) with \(E_K>0\),
\[
\frac{\sum_{k<K,\ s_k\ne0}\|s_k\|^2\rho_k}{E_K}
=\frac2\eta-\frac{2(L(x_0)-L(x_K))}{E_K},
\]
so that
\[
\max_{\substack{k<K\\s_k\ne0}}\rho_k
\ge\frac2\eta-\frac{2(L(x_0)-L_{\inf})}{E_K}.
\]
The same interior points satisfy
\[
\sum_{\substack{k<K\\s_k\ne0}}\|s_k\|^2
\left[\frac2\eta-\lambda_{\max}\!\left(\nabla^2L(x_k+\theta_k s_k)\right)\right]
\le2(L(x_0)-L(x_K)),
\]
and consequently
\[
\max_{\substack{k<K\\s_k\ne0}}
\lambda_{\max}\!\left(\nabla^2L(x_k+\theta_k s_k)\right)
\ge\frac2\eta-\frac{2(L(x_0)-L_{\inf})}{E_K}.
\]
Finally, if \(L(x_k)\) is bounded above along the trajectory and \(E_K\to\infty\), prove that the displayed weighted average of \(\rho_k\) converges to \(2/\eta\).
