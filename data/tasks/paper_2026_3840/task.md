# Problem

## Setup

Let \(I=[0,1]\), with Lebesgue measure \(m\), and fix a positive integer \(N\) and a partition \(\{I_i\}_{i=1}^N\) into intervals of positive measure. Set
\[
\Delta_N=\max_{1\le i\le N}m(I_i).
\]
For \(v\in\mathbb R^N\) and \(g\in L^1(I)\), define
\[
(E_Nv)(x)=\sum_{i=1}^N\frac{v_i}{m(I_i)}\mathbf 1_{I_i}(x),
\qquad
(\Pi_Ng)(x)=\sum_{i=1}^N\frac{\int_{I_i}g\,dm}{m(I_i)}\mathbf 1_{I_i}(x).
\]
Use \(\|\cdot\|_1\) for the vector \(\ell^1\) norm or the function \(L^1(I,m)\) norm, according to the argument.

For each regime \(s\in\{0,t\}\), let \((Y_k^{(s)})_{k\ge0}\) be a stationary geometrically ergodic Markov chain on \(\{1,\ldots,N\}\). The two chains are defined on a common probability space. Write \(P_N^{(s)}\) for its row-stochastic transition matrix and \(\pi_N^{(s)}\) for its unique stationary probability row vector. Assume a common lower bound
\[
\pi_N^{(s)}(i)\ge\pi_{\min,N}>0
\qquad(s\in\{0,t\},\ 1\le i\le N).
\]

Fix a noise level \(\delta\ge0\). Let \(h_{\delta,s}\) and \(h_s\) be probability densities on \(I\), representing respectively the observed and noiseless invariant laws in regime \(s\). Set
\[
h_{N,s}=E_N\pi_N^{(s)},
\qquad h_{N,s}=\Pi_Nh_{\delta,s}.
\]
Assume there are constants \(C_A>0\), \(\beta>0\), and a finite-valued function \(\eta:[0,\infty)\to[0,\infty)\) with \(\eta(a)\to0\) as \(a\downarrow0\), such that for both regimes
\[
\|\Pi_Nh_{\delta,s}-h_{\delta,s}\|_1\le C_A\Delta_N^\beta,
\qquad
\|h_{\delta,s}-h_s\|_1\le\eta(\delta).
\]

For states \(a,b\in\{1,\ldots,N\}\), define the indicator functions
\[
f_i(a,b)=\mathbf 1_{\{a=i\}},
\qquad
f_{ij}(a,b)=\mathbf 1_{\{a=i,\ b=j\}},
\]
and let \(\mathcal F_N\) be the collection of these functions for all \(i,j\). Assume there are constants \(C_*,c_*>0\), common to the two regimes, such that for every positive integer \(\ell\), every \(f\in\mathcal F_N\), and every \(0<u<1\),
\[
\mathbb P\!\left(
\left|\frac1\ell\sum_{k=0}^{\ell-1}f(Y_k^{(s)},Y_{k+1}^{(s)})
-\mathbb E f(Y_0^{(s)},Y_1^{(s)})\right|>u
\right)
\le C_*\exp(-c_*\ell u^2).
\]
These constants may depend on the fixed partition and regime laws, but not on \(\ell,u,i,j\).

For deterministic positive integers \(n_0,n_t\), the data in regime \(s\) are \(Y_0^{(s)},\ldots,Y_{n_s-1}^{(s)}\). Define
\[
C_{ij}^{(s)}=\sum_{k=0}^{n_s-2}\mathbf 1_{\{Y_k^{(s)}=i,\ Y_{k+1}^{(s)}=j\}},
\qquad
C_i^{(s)}=\sum_{k=0}^{n_s-2}\mathbf 1_{\{Y_k^{(s)}=i\}},
\]
with empty sums equal to zero. Set \(\widehat P_{n_s}^{(s)}(i,j)=C_{ij}^{(s)}/C_i^{(s)}\) when \(C_i^{(s)}>0\); when \(C_i^{(s)}=0\), assign that row a prescribed probability vector, for example the uniform vector.

Let \(J_N\) have every row equal to \((1/N,\ldots,1/N)\). Fix \(0<\rho<1\), and set
\[
\widehat P_{n_s,\rho}^{(s)}=(1-\rho)\widehat P_{n_s}^{(s)}+\rho J_N,
\qquad
P_{N,\rho}^{(s)}=(1-\rho)P_N^{(s)}+\rho J_N.
\]
Denote their unique stationary probability row vectors by \(\widehat\pi_{n_s,\rho}^{(s)}\) and \(\pi_{N,\rho}^{(s)}\), respectively. Define
\[
S_t=\|\widehat\pi_{n_t,\rho}^{(t)}-\widehat\pi_{n_0,\rho}^{(0)}\|_1,
\qquad
\zeta_{N,s}(\rho)=\|E_N\pi_{N,\rho}^{(s)}-h_{N,s}\|_1.
\]
For \(0<\varepsilon<1\), put
\[
r_s(\varepsilon)=\frac{N(1-\rho)}{\rho}\varepsilon
+\zeta_{N,s}(\rho)+C_A\Delta_N^\beta+\eta(\delta),
\qquad
\tau_t(\varepsilon)=r_0(\varepsilon)+r_t(\varepsilon).
\]

## Task

Prove that there exist constants \(C_0,c_0>0\), depending only on \(C_*,c_*\), common to both regimes and independent of \(n_0,n_t,\rho,\varepsilon\), such that, upon defining
\[
B_s(\varepsilon)=C_0N^2\exp(-c_0n_s\pi_{\min,N}^2\varepsilon^2),
\]
the following statements hold for every \(0<\varepsilon<1\).

For each \(s\in\{0,t\}\),
\[
\mathbb P\!\left(\|E_N\widehat\pi_{n_s,\rho}^{(s)}-h_s\|_1>r_s(\varepsilon)\right)
\le B_s(\varepsilon).
\]
Consequently, if \(h_t=h_0\), then
\[
\mathbb P(S_t>\tau_t(\varepsilon))\le B_0(\varepsilon)+B_t(\varepsilon).
\]
If instead
\[
\|h_t-h_0\|_1>2\tau_t(\varepsilon),
\]
then
\[
\mathbb P(S_t>\tau_t(\varepsilon))\ge1-B_0(\varepsilon)-B_t(\varepsilon).
\]
