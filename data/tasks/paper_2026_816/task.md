# Problem

## Setup

Let \(d,k\) be positive integers. Let \(D\) be a distribution on \(\mathbb R^d\). An unknown parameter \(w^\star\in\mathbb R^d\) generates responses by
\[
y=\langle w^\star,x\rangle+\xi,\qquad x\sim D,\quad \xi\sim N(0,1),
\]
with \(x\) and \(\xi\) independent. A measurable survival set \(S^\star\subseteq\mathbb R\) is unknown, and a pair \((x,y)\) is observed only when \(y\in S^\star\); the available data are iid draws from this conditional joint distribution. Let \(D_{\rm obs}=\mathcal L(x\mid y\in S^\star)\).

For a scalar random variable \(Z\), define
\[
\|Z\|_{\psi_2}=\inf\{t>0:\mathbb E\exp(Z^2/t^2)\le2\}.
\]
Here \(D\) is called \(\sigma\)-sub-Gaussian if
\[
\|\langle u,x-\mathbb E_Dx\rangle\|_{\psi_2}\le\sigma
\quad\text{for every unit vector }u\in\mathbb R^d.
\]

Assume the following finite numerical bounds are supplied to the algorithm: \(\alpha\in(0,1]\), \(\sigma,\beta,R_w\ge0\), and \(\rho,\Lambda,M>0\). They satisfy:

- \(\Pr[y\in S^\star]\ge\alpha\).
- \(D\) is \(\sigma\)-sub-Gaussian, \(\|\mathbb E_Dx\|_2\le\beta\), and \(\|w^\star\|_2\le R_w\).
- \(\mathbb E_{D_{\rm obs}}[xx^\top]\succeq\rho^2I_d\).
- \(\mathbb E_D[xx^\top]\preceq\Lambda^2I_d\) and \(\mathbb E_D\langle u,x\rangle^4\le M^4\|u\|_2^4\) for every \(u\in\mathbb R^d\).
- \(S^\star\) is a union of at most \(k\) intervals, which may be unbounded; \(k\) is supplied to the algorithm.

## Task

Prove that for every \(\varepsilon,\delta\in(0,1/2)\), there is a randomized algorithm which, given these numerical bounds, \(\varepsilon,\delta\), and iid samples from the conditional distribution above, uses at most
\[
n=\operatorname{poly}\!\bigl(d,R_w,k,\varepsilon^{-1},\log(1/\delta)\bigr)^{\operatorname{poly}(\sigma,\beta,\rho^{-1},\alpha^{-1},\Lambda,M)}
\]
samples, runs in time polynomial in this resource bound, and outputs \(\widehat w\) satisfying
\[
\Pr\bigl(\|\widehat w-w^\star\|_2\le\varepsilon\bigr)\ge1-\delta.
\]
The polynomials are universal and do not depend on the unknown instance. The algorithm must work without knowing \(D\), \(S^\star\), or \(w^\star\), and without access to unobserved pairs.
