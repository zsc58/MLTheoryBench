# Problem

## Setup

Let X and Y be compact Polish subsets of Euclidean spaces, let S=XxY, and let mu* be a Borel probability measure on S. For a compact Polish space T, write \(\mathcal P(T)\) for its Borel probability measures, equipped with the topology of weak convergence. Fix a finite real budget \(\varepsilon\ge0\).

Let G range over a class of continuous maps G:Y->X, each with finite nonnegative Lipschitz constant L_G. Define
\[
\ell((x,y),G)=\|x-G(y)\|^2.
\]

For s=(x,y) and r=(x',v), set
\[
c(s,r)=\|x-x'\|^2+\|y-v\|^2.
\]
For each s=(x,y), let
\[
K_s=\{\delta_x\otimes\nu:\nu\in\mathcal P(Y)\}.
\]
An admissible kernel is a mu*-measurable map \(s\mapsto k_s\in\mathcal P(S)\) with \(k_s\in K_s\) for mu*-almost every s. It induces
\[
\pi_k(A)=\int_S k_s(A)\,d\mu^*(s)
\]
for Borel sets \(A\subseteq S\). Assume the feasible set is nonempty, and impose the budget
\[
\int_S\int_S c(s,r)\,dk_s(r)\,d\mu^*(s)\le\varepsilon.
\]
Let \(\Omega_\varepsilon\) be the set of measures \(\pi_k\) induced by at least one admissible kernel satisfying this budget, and define
\[
I_\varepsilon(G)=\sup_{\pi\in\Omega_\varepsilon}\int_S\ell(r,G)\,d\pi(r).
\]

## Task

Prove that, for every G,
\[
I_\varepsilon(G)=\inf_{\lambda\ge0}\left\{\lambda\varepsilon+\int_{X\times Y}\phi_{\lambda,G}(x,y)\,d\mu^*(x,y)\right\},
\]
where
\[
\phi_{\lambda,G}(x,y)=\sup_{v\in Y}\{\|x-G(v)\|^2-\lambda\|y-v\|^2\}.
\]
Moreover, prove
\[
\inf_G I_\varepsilon(G)\le\inf_G\left(\sqrt{\int_{X\times Y}\|G(y)-x\|^2\,d\mu^*(x,y)}+L_G\sqrt\varepsilon\right)^2.
\]
