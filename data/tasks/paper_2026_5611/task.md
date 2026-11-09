# Problem

## Setup

Let \(T>0\), let \(d,m\ge 1\) be integers, let \(p\) be a probability density on \(\mathbb R^d\), and let \(U\sim p\). Let \(\varepsilon\sim\mathcal N(0,I_d)\) and \(\eta\sim\mathcal N(0,\tau^2I_m)\), where \(\tau>0\), be independent of \(U\) and of each other. For \(s\in[0,T]\), let \(a_s,b_s\in\mathbb R\) satisfy \((a_0,b_0)=(1,0)\) and \((a_T,b_T)=(0,1)\), and define
\[
 Z_s=a_sU+b_s\varepsilon,\qquad R=HU+\eta,
\]
where \(H\in\mathbb R^{m\times d}\) is known.

Fix \(t\in[0,T]\) such that \(b_t>0\) and
\[
 Q=\frac{a_t^2}{b_t^2}I_d+\tau^{-2}H^\top H
\]
is invertible. Set
\[
 S=Q^{-1},\qquad
 w(z,r)=S\left(\frac{a_t}{b_t^2}z+\tau^{-2}H^\top r\right).
\]

Throughout, conditional densities at specified conditioning values are the density-ratio versions obtained from the joint densities induced by the stated prior and Gaussian noise densities. Conditional means at specified values denote integration against those conditional densities, when absolutely convergent, rather than arbitrary almost-everywhere versions.

For every symmetric positive-definite matrix \(C\in\mathbb R^{d\times d}\), define
\[
 p^C(v)=\int_{\mathbb R^d}\mathcal N(v;u,C)p(u)\,du,
 \qquad
 M_C(v)=\mathbb E[U\mid U+\xi=v],\quad \xi\sim\mathcal N(0,C),
\]
where \(\xi\) is independent of \(U\).

## Task

Prove that, for all \(z\in\mathbb R^d\) and \(r\in\mathbb R^m\),
\[
 \nabla_z\log p_{Z_t\mid R}(z\mid r)
 =\frac{1}{b_t^2}\left(a_t M_S\bigl(w(z,r)\bigr)-z\right).
\]
Moreover, prove the accompanying posterior-mean identity
\[
 M_S\bigl(w(z,r)\bigr)=\mathbb E[U\mid Z_t=z,R=r].
\]
