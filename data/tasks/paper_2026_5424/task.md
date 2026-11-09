# Problem

## Setup

Fix integers \(d\ge2\) and \(m\ge1\), and fix \(\eta\in(0,1)\). For \(x\in\mathbb R^d\), write \(\bar x=(x,1)\in\mathbb R^{d+1}\).

Use the ordered activation dictionary
\[
(\sigma_1,\ldots,\sigma_7)
=(\mathrm{id},R,R^2,L_\eta,\operatorname{GELU},\operatorname{SiLU},\tanh),
\]
where
\[
\mathrm{id}(t)=t,\qquad R(t)=\max\{0,t\},\qquad R^2(t)=R(t)^2,
\]
\[
L_\eta(t)=\begin{cases}t,&t\ge0,\\ \eta t,&t<0,\end{cases}
\qquad \operatorname{GELU}(t)=t\Phi(t),\qquad
\operatorname{SiLU}(t)=\frac{t}{1+e^{-t}},
\]
and \(\Phi\) is the standard normal distribution function.

For \(p,q\in\{1,\ldots,7\}\), define the width-\(m\) fixed-pair class
\[
\mathcal F_{p,q}^{(m)}=
\left\{x\mapsto\sum_{k=1}^m a_k
\sigma_p(w_k^{\mathsf T}\bar x)\sigma_q(u_k^{\mathsf T}\bar x):
 a_k\in\mathbb R,\ w_k,u_k\in\mathbb R^{d+1}\right\}.
\]

Define the width-\(m\) constant-mixture class
\[
\mathcal L^{(m)}=
\left\{x\mapsto\sum_{k=1}^m a_k
\sum_{1\le p\le q\le7}\alpha_{p,q}
\sigma_p(w_k^{\mathsf T}\bar x)\sigma_q(u_k^{\mathsf T}\bar x)
\right\},
\]
where the set ranges over all \(a_k,\alpha_{p,q}\in\mathbb R\) and \(w_k,u_k\in\mathbb R^{d+1}\). The coefficients \(\alpha_{p,q}\) are shared across the \(m\) summands. Within each summand, the vectors \(w_k,u_k\) are shared across all activation-pair branches, as displayed.

Define the width-\(m\) input-adaptive mixture class
\[
\mathcal M^{(m)}=
\left\{x\mapsto\sum_{k=1}^m a_k
\sum_{1\le p\le q\le7}\tanh(v_{p,q}^{\mathsf T}\bar x)
\sigma_p(w_k^{\mathsf T}\bar x)\sigma_q(u_k^{\mathsf T}\bar x)
\right\},
\]
where the set ranges over all \(a_k\in\mathbb R\) and \(w_k,u_k,v_{p,q}\in\mathbb R^{d+1}\). Each \(v_{p,q}\) is shared across the \(m\) summands, and within each summand the vectors \(w_k,u_k\) are shared across all activation-pair branches, as displayed.

## Task

Prove the strict finite-width hierarchy
\[
\bigcup_{p,q=1}^7\mathcal F_{p,q}^{(m)}
\subsetneq \mathcal L^{(m)}
\subsetneq \mathcal M^{(m)}
\]
for every \(d\ge2\) and \(m\ge1\).
