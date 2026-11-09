# Problem

## Setup

Let \(\mathcal X\) and \(\mathcal Y\) be measurable prompt and response spaces. Let \(\rho\) and \(\rho_{\rm label}\) be probability laws on \(\mathcal X\), and let \(\pi_\theta\) and \(\pi_{\rm ref}\) be probability kernels from \(\mathcal X\) to \(\mathcal Y\). A deployment prompt has law \(\rho\); conditional on \(x\), responses are sampled from \(\pi_\theta(\cdot\mid x)\). The training and deployment joint laws are
\[
P(dx,dy)=\rho_{\rm label}(dx)\pi_{\rm ref}(dy\mid x),\qquad
Q(dx,dy)=\rho(dx)\pi_\theta(dy\mid x).
\]
Assume \(Q\ll P\). Define the chi-square divergence by
\[
\chi^2(Q\|P)=\int\left(\frac{dQ}{dP}-1\right)^2\,dP,
\]
and assume it is finite.

For the policy likelihood ratio, use the conditional Radon–Nikodym derivative
\[
\frac{\pi_\theta(y\mid x)}{\pi_{\rm ref}(y\mid x)}
:=\frac{d\pi_\theta(\cdot\mid x)}{d\pi_{\rm ref}(\cdot\mid x)}(y).
\]
Assume this derivative exists for \(\rho\)-almost every \(x\) and admits a jointly measurable version. In a discrete model this is the ratio of probability masses; when conditional densities are used, it is their ratio. Define
\[
\ell_\theta(x,y)=\log\frac{\pi_\theta(y\mid x)}{\pi_{\rm ref}(y\mid x)},\qquad
\ell_\theta^\tau(x,y)=\max\{-\tau,\min\{\ell_\theta(x,y),\tau\}\},
\]
for \(\tau>0\). Set \(\ell_\theta=0\) on the exceptional \(Q\)-null set where the likelihood ratio is not positive and finite. Let \(r^*\) and \(\widehat r_\phi\) be measurable functions on \(\mathcal X\times\mathcal Y\) satisfying \(0\le r^*,\widehat r_\phi\le1\). Assume \(\mathbb E_Q|\ell_\theta|<\infty\) and define
\[
L_{\rm train}^{(2)}(\phi)=\mathbb E_P[(\widehat r_\phi-r^*)^2],\qquad
C(\theta)=\sqrt{1+\chi^2(Q\|P)}.
\]
For a fixed \(\beta>0\), define
\[
J^*=\mathbb E_Q[r^*-\beta\ell_\theta],\quad
J^\phi=\mathbb E_Q[\widehat r_\phi-\beta\ell_\theta],\quad
J^{\phi,\tau}=\mathbb E_Q[\widehat r_\phi-\beta\ell_\theta^\tau].
\]
Let \(n,K\) be positive integers. Draw \(X_1,\ldots,X_n\) independently from \(\rho\). Conditional on the entire prompt vector, draw the \(nK\) responses independently, with \(Y_{ij}\sim\pi_\theta(\cdot\mid X_i)\) for \(1\le i\le n\) and \(1\le j\le K\). Set
\[
\widehat J_{n,K}^{\phi,\tau}=\frac1{nK}\sum_{i=1}^n\sum_{j=1}^K\bigl[\widehat r_\phi(X_i,Y_{ij})-\beta\ell_\theta^\tau(X_i,Y_{ij})\bigr].
\]

## Task

Prove that for every fixed \(\theta,\phi\), every fixed \(\tau>0\), and every \(\delta\in(0,1)\), with probability at least \(1-\delta\) over the prompt and rollout sampling,
\[
\left|\widehat J_{n,K}^{\phi,\tau}-J^*\right|
\le (1+2\beta\tau)\left[\sqrt{\frac{\log(4/\delta)}{2n}}+\sqrt{\frac{\log(4/\delta)}{2nK}}\right]
+C(\theta)\sqrt{L_{\rm train}^{(2)}(\phi)}
+\beta\,\mathbb E_Q\!\left[|\ell_\theta-\ell_\theta^\tau|\right].
\]
