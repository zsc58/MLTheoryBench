# Problem

## Setup

Let \(d\ge1\), \(R>0\), and let \(\mu,\nu\) be probability measures supported in the Euclidean ball \(B(0,R)\subset\mathbb R^d\). For a unit vector \(\theta\in\mathbb S^{d-1}\), write \(\mu_\theta,\nu_\theta\) for the laws of \(\langle\theta,X\rangle\) under \(X\sim\mu,\nu\), and let their CDFs be \(F_{\mu,\theta},F_{\nu,\theta}\). Define, for \(x\le y\),
\[
\Delta^{(2)}(\theta,x,y)=\big(F_{\mu,\theta}(x)-F_{\nu,\theta}(y)\big)_+ +\big(F_{\nu,\theta}(x)-F_{\mu,\theta}(y)\big)_+ .
\]
Let \(T=\{(u,v):0\le u\le v\le1\}\). For \(k\in(0,1]\), let \(\eta_k\) have density
\[
f_k(u,v)=k(k+1)(v-u)^{k-1}\quad ((u,v)\in T).
\]
For i.i.d. \(\theta_t\) uniform on \(\mathbb S^{d-1}\) and \((U_t,V_t)\) i.i.d. from \(\eta_k\), all independent, define
\[
\widehat S_{2,L,k}^2(\mu,\nu)=\frac1L\sum_{t=1}^L \frac{2(2R)^2\,\Delta^{(2)}(\theta_t,-R+2RU_t,-R+2RV_t)}{f_k(U_t,V_t)}.
\]
Define \(W_\infty(\mu,\nu)\) as the infimum, over couplings of \(\mu,\nu\), of the essential supremum of \(\|X-Y\|\). Assume
\[
W_\infty(\mu,\nu)<2R e^{-1/2}.
\]

## Task

Prove that there exists \(k_0=k_0(R,W_\infty(\mu,\nu))<1\) such that the map
\[
 k\longmapsto \operatorname{Var}\!\left(\widehat S_{2,L,k}^2(\mu,\nu)\right)
\]
is nondecreasing on \([k_0,1]\) (for every integer \(L\ge1\)).
