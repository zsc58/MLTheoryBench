# Problem

## Setup

Fix integers \(d\ge2\) and \(K\ge2\), and numbers \(R,T>0\). Let
\[
D_R=[-R,R]^d.
\]
Let \(Q_1,\ldots,Q_K\subset D_R\) be pairwise disjoint compact convex sets, and let \(y_1,\ldots,y_K\in\mathbb R^d\) be pairwise distinct. Write \(B(y,\eta)=\{z\in\mathbb R^d:\|z-y\|_2<\eta\}\) and \((s)_+=\max\{s,0\}\).

A width-\(p\) semi-autonomous ReLU neural ODE is
\[
\dot z(t)=\sum_{i=1}^{p}u_i\bigl(\alpha_i\cdot z(t)+\beta_i t+\gamma_i\bigr)_+,
\qquad z(0)=x,
\quad 0\le t\le T,
\]
with time-independent parameters \(u_i,\alpha_i\in\mathbb R^d\) and \(\beta_i,\gamma_i\in\mathbb R\). Denote its time-\(t\) flow by \(\Phi_t\).

## Task

Prove that there exist constants
\[
C=C\bigl(d,T,R,(y_k)_{k=1}^K,(Q_k)_{k=1}^K\bigr)>0,
\quad M=M\bigl(d,T,R,(y_k)_{k=1}^K\bigr)>0,
\quad \eta_0\in(0,1],
\]
such that, for every \(0<\eta\le\eta_0\) and every integer \(p\) satisfying
\[
p\ge C\,\eta^{-2-C}(1-\log\eta)^2,
\]
there are parameters defining a width-\(p\) semi-autonomous ReLU neural ODE whose flow obeys
\[
\Phi_T(Q_k)\subset B(y_k,\eta)\quad\text{for all }k=1,\ldots,K,
\qquad
\sup_{x\in D_R}\|\Phi_T(x)\|_2\le M.
\]
