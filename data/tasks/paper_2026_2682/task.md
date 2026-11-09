# Problem

## Setup

Let \(X_1,X_2,\ldots\) be IID with law \(P^*\) supported on \([0,1]\), mean \(\mu^*\in(0,1)\), and variance \(\sigma^2>0\). Set \(\mathcal F_0=\{\varnothing,\Omega\}\), \(\mathcal F_n=\sigma(X_1,\ldots,X_n)\), and, for \(n\ge1\),
\[
P_n=\frac1n\sum_{i=1}^n\delta_{X_i},\qquad
\bar X_n=\frac1n\sum_{i=1}^nX_i,\qquad
s_n^2=\frac1n\sum_{i=1}^n(X_i-\bar X_n)^2.
\]
For probability measures \(P,Q\) on \([0,1]\), let \(W_1(P,Q)\) be the infimum of \(\int |x-y|\,\xi(dx,dy)\) over all joint probability measures \(\xi\) with marginals \(P,Q\).

Fix \(c\in(0,1)\). For a candidate mean \(\mu\in(0,1)\), set
\[
I_{\mu,c}=\left[-\frac{c}{1-\mu},\frac{c}{\mu}\right].
\]
For any sequence \(\lambda_n(\mu)\in I_{\mu,c}\) with \(\lambda_n(\mu)\) measurable with respect to \(\mathcal F_{n-1}\), define
\[
W_n(\mu)=\prod_{i=1}^n[1+\lambda_i(\mu)(X_i-\mu)],\qquad W_0(\mu)=1.
\]
Define
\[
M(\lambda,\mu)=\mathbb E_{P^*}\log(1+\lambda(X_1-\mu)),
\]
let \(\lambda^*(\mu)\) be a maximizer on \(I_{\mu,c}\), and put
\[
W_n^*(\mu)=\prod_{i=1}^n[1+\lambda^*(\mu)(X_i-\mu)].
\]

Let \(\pi\) be a fixed probability density on \([0,1]\). Assume there exist constants \(a_0>0\) and \(r>0\) such that
\[
(\mu^*-r,\mu^*+r)\subset(0,1),\qquad
\pi(\mu)\ge a_0\quad\text{for Lebesgue-almost every }\mu\in(\mu^*-r,\mu^*+r).
\]
Let \((\tau_n)_{n\ge1}\) be a fixed sequence of finite nonnegative numbers with \(\tau_n=o(n)\). Let \(\mu\mapsto H_\mu\), for \(\mu\in(0,1)\), be a fixed Borel probability kernel on \([0,1]\): for each Borel set \(A\subseteq[0,1]\), the map \(\mu\mapsto H_\mu(A)\) is Borel measurable. Assume that the convex hull of the support of each \(H_\mu\) is \([0,1]\). These inputs do not depend on the observations. Set
\[
P_{n,\mu}=\frac{n}{n+\tau_n}P_n+\frac{\tau_n}{n+\tau_n}H_\mu.
\]

For \(n\ge1\) and \(\mu\in(0,1)\), a fit is used when the finite exponential-tilt equation has a solution; when \(\tau_n=0\), a fit is used only if
\[
\min_{1\le i\le n}X_i<\mu<\max_{1\le i\le n}X_i.
\]
On this fitting domain, let \(\gamma_{n,\mu}\) be the unique finite solution of the mean constraint and define
\[
A_{n,\mu}=\int e^{\gamma_{n,\mu}(z-\mu)}P_{n,\mu}(dz),\qquad
\frac{d\widetilde P_{n,\mu}}{dP_{n,\mu}}(z)
=\frac{e^{\gamma_{n,\mu}(z-\mu)}}{A_{n,\mu}},\qquad
\int z\,\widetilde P_{n,\mu}(dz)=\mu.
\]
The weight of the labelled empirical component corresponding to \(X_i\), excluding any regularizer mass at that location, is
\[
w_{n,i}(\mu)=\frac{e^{\gamma_{n,\mu}(X_i-\mu)}}{(n+\tau_n)A_{n,\mu}}.
\]
Define the rescaled empirical-likelihood factor by
\[
L_n(\mu)=\prod_{i=1}^n n\,w_{n,i}(\mu).
\]
Where no fit is used, set \(L_n(\mu)=0\), \(\gamma_{n,\mu}=0\), and \(\widetilde P_{n,\mu}=\delta_0\).

Let
\[
D_n=\int_{(0,1)}L_n(v)\pi(v)\,dv.
\]
If \(D_n>0\), define
\[
\Pi_n(d\mu)=\frac{L_n(\mu)\pi(\mu)d\mu}{D_n};
\]
if \(D_n=0\), define \(\Pi_n(d\mu)=\pi(\mu)d\mu\). In both cases set
\[
Q_{n+1\mid n}=\int_{(0,1)}\widetilde P_{n,\mu}\,\Pi_n(d\mu).
\]
Take \(Q_{1\mid0}=\delta_0\). All parameter integrals are over \((0,1)\); the density prior assigns no mass to the endpoints.

For each candidate \(\mu\), choose an \(\mathcal F_{n-1}\)-measurable maximizer
\[
\widehat\lambda_n(\mu)\in\arg\max_{\lambda\in I_{\mu,c}}
\int\log(1+\lambda(x-\mu))\,Q_{n\mid n-1}(dx),
\]
using a measurable selection in case of ties, and use \(\widehat\lambda_n(\mu)\) in \(W_n(\mu)\).

## Task

Prove that, for every \(\varepsilon>0\),
\[
\Pi_n(|\mu-\mu^*|>\varepsilon)\to0,
\qquad
\Pi_n(|\gamma_{n,\mu}|>\varepsilon)\to0
\]
in probability under the true sampling law, and that
\[
W_1(Q_{n+1\mid n},P^*)\to0
\]
in probability. Deduce that for every fixed candidate \(\mu\in(0,1)\),
\[
\frac1n\log W_n(\mu)\to M(\lambda^*(\mu),\mu)
\quad\text{in probability},
\qquad
\frac1n\mathbb E_{P^*}\log W_n(\mu)\to M(\lambda^*(\mu),\mu).
\]
If \(W_1(Q_{n\mid n-1},P^*)\to0\) almost surely, also prove almost-sure convergence of the realized normalized log wealth.
