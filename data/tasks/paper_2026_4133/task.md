# Problem

## Setup

Consider a discounted controlled Markov model with measurable state space \(\mathcal X\), measurable action space \(\mathcal A\), discount factor \(\gamma\in[0,1)\), transition densities \(p(y\mid x,a)\) with respect to a fixed reference measure denoted by \(dy\), and one-step reward \(r(x,a,y)\). Fix a policy probability kernel \(\pi(da\mid x)\). Its action-value and value functions satisfy
\[
Q^\pi(x,a)=\int p(y\mid x,a)\bigl[r(x,a,y)+\gamma V^\pi(y)\bigr]dy,
\qquad
V^\pi(x)=\int Q^\pi(x,a)\pi(da\mid x).
\]
All functions and kernels used below are measurable. Every integral and expectation displayed in this setup is assumed absolutely integrable for its stated arguments.

Condition on a fixed pre-decision history. At the final available observation time, the real state is a fixed \(x^0\). Replacing only the current observation by \(o\in\mathbb R^d\), while leaving past observations, past controls, and model parameters unchanged, induces a posterior probability measure \(\mu_o\) over \(X\in\mathcal X\). The action is then sampled as \(A\sim\pi(\cdot\mid X)\), with \(X\sim\mu_o\).

Conditional on the fixed history, the predictive observation law is \(\mathcal N(\bar o,S)\), where \(\bar o\in\mathbb R^d\) and \(S\) is a positive-definite \(d\times d\) matrix. The observation must lie in the predictive likelihood ellipsoid
\[
\mathcal E_\rho=\{o\in\mathbb R^d:(o-\bar o)^\top S^{-1}(o-\bar o)\le \rho\},
\qquad \rho\ge0.
\]
The quantities \(\bar o\), \(S\), and \(\rho\) are fixed throughout the optimization.

For every \((x,a)\in\mathcal X\times\mathcal A\), suppose the transition law with density \(p(\cdot\mid x^0,a)\) is absolutely continuous with respect to the law with density \(p(\cdot\mid x,a)\). Define
\[
w(y,a;x^0,x)=\frac{p(y\mid x^0,a)}{p(y\mid x,a)}
\]
where the denominator is positive, and set \(w=0\) where the denominator is zero. Thus \(w\) is a version of the density ratio under the latter transition law.

Define
\[
\Delta_{\mathrm{tr}}(x,a)=\int p(y\mid x,a)(w(y,a;x^0,x)-1)
\bigl[r(x,a,y)+\gamma V^\pi(y)\bigr]dy,
\]
\[
\Delta_{\mathrm{rw}}(x,a)=\int p(y\mid x,a)w(y,a;x^0,x)
\bigl[r(x^0,a,y)-r(x,a,y)\bigr]dy,
\]
and let
\[
\Delta_{\mathrm{tr}}(x)=\int\Delta_{\mathrm{tr}}(x,a)\pi(da\mid x),
\qquad
\Delta_{\mathrm{rw}}(x)=\int\Delta_{\mathrm{rw}}(x,a)\pi(da\mid x).
\]
Finally, define the exact final-time attack objective
\[
J(o)=\mathbb E_{X\sim\mu_o,\,A\sim\pi(\cdot\mid X)}[Q^\pi(x^0,A)],
\qquad o\in\mathcal E_\rho.
\]

## Task

Prove that, for every \(o\in\mathcal E_\rho\),
\[
J(o)=\mathbb E_{X\sim\mu_o}
\left[V^\pi(X)+\Delta_{\mathrm{tr}}(X)+\Delta_{\mathrm{rw}}(X)\right].
\]
Consequently, prove that the constrained final-time attack problem is exactly
\[
\min_{o\in\mathcal E_\rho}\ 
\mathbb E_{X\sim\mu_o}
\left[V^\pi(X)+\Delta_{\mathrm{tr}}(X)+\Delta_{\mathrm{rw}}(X)\right].
\]
