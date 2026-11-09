# Problem

## Setup

All norms are Euclidean, and \(I_D\) denotes the \(D\times D\) identity matrix. Let \(D,I,J\) be positive integers, \(T>0\), and \(\Delta=T/J\). On a filtered probability space, let \(B\) be a standard \(D\)-dimensional Brownian motion with respect to the filtration, and let \(Y\) be a continuous adapted solution on \([0,T+\Delta]\) of
\[
dY_t=\mu(Y_t)\,dt+\sigma\,dB_t,
\]
where \(\sigma>0\) is known and \(\mu:\mathbb R^D\to\mathbb R^D\) is time-homogeneous and \(L\)-Lipschitz for a finite constant \(L>0\). Assume
\[
m_\mu(t):=\mathbb E\|\mu(Y_t)\|^2<\infty
\qquad (0\le t\le T+\Delta).
\]

The observations consist of \(I\) independent, identically distributed trajectories with the same law as \(Y\), observed at \(t_j=j\Delta\), \(j=0,\ldots,J\). Denote their observed increments by
\[
Z_j^{\mathrm{obs},(i)}:=Y_{t_j}^{(i)}-Y_{t_{j-1}}^{(i)},
\qquad i=1,\ldots,I,\quad j=1,\ldots,J.
\]
For the population assertion below, define instead the forward increment
\[
Z_t:=Y_{t+\Delta}-Y_t,\qquad 0\le t\le T.
\]

Let \(\beta:[0,\infty)\to[0,\infty)\) be measurable and satisfy
\[
0<\int_0^\tau\beta(s)\,ds<\infty
\qquad\text{for every }\tau>0.
\]
Define
\[
\alpha_\tau=\exp\!\left[-\frac12\int_0^\tau\beta(s)\,ds\right],
\qquad
\sigma_\tau=\sqrt{1-\alpha_\tau^2}>0.
\]
For each \(t\in[0,T]\) and \(\tau>0\), define the forward variable
\[
X_{\tau,t}=\alpha_\tau Z_t+\sigma_\tau\epsilon,
\qquad \epsilon\sim N(0,I_D),
\]
where \(\epsilon\) is independent of the entire process \(Y\).

Fix a denoiser \(D_{\theta^*}(\tau,x,y)\in\mathbb R^D\), Borel measurable in \((x,y)\) for each \(\tau>0\). The denoiser is held fixed in all expectations below: for a trained denoiser, the assertion concerns each fixed fitted function satisfying the following conditions, evaluated under the stated population law of \(Y\), rather than an expectation over training randomness. For each \(\tau>0\), suppose there are finite constants \(\varepsilon_{\rm score}(\tau)>0\) and \(L_D(\tau)>0\) such that
\[
\frac1T\int_0^T
\mathbb E\|D_{\theta^*}(\tau,X_{\tau,t},Y_t)-Z_t\|^2\,dt
\le\varepsilon_{\rm score}(\tau),
\]
and
\[
\|D_{\theta^*}(\tau,x,y)-D_{\theta^*}(\tau,x',y)\|
\le L_D(\tau)\|x-x'\|
\qquad (x,x',y\in\mathbb R^D).
\]
The expectation in the denoiser condition is over \(Y\) and the forward noise \(\epsilon\).

Define
\[
a(\tau)=-\frac{\alpha_\tau\sigma^2}{\sigma_\tau^2},\qquad
b_\Delta(\tau)=\frac{\sigma_\tau^2+\alpha_\tau^2\sigma^2\Delta}{\sigma_\tau^2\Delta},
\]
\[
\widehat\mu(\tau,x,y)=a(\tau)x+b_\Delta(\tau)D_{\theta^*}(\tau,x,y).
\]
For an integer \(K\ge1\), let \(G^{(1)},\ldots,G^{(K)}\) be iid \(N(0,I_D)\) random vectors, jointly independent of \(Y\), and set
\[
\bar\mu_K(\tau,y)=\frac1K\sum_{k=1}^K\widehat\mu(\tau,G^{(k)},y),
\qquad
L_{\rm est}(\tau)=|a(\tau)|+b_\Delta(\tau)L_D(\tau).
\]

## Task

Prove that, for every setup just described, every \(\tau>0\), and every integer \(K\ge1\),
\[
\frac1T\int_0^T\mathbb E\big\|\mu(Y_t)-\bar\mu_K(\tau,Y_t)\big\|^2\,dt
\le4\Bigg\{L^2\Big[\frac{\Delta^2}{T}\int_0^{T+\Delta}m_\mu(s)\,ds+\sigma^2D\Delta\Big]+b_\Delta(\tau)^2\varepsilon_{\rm score}(\tau)
\]
\[
+L_{\rm est}(\tau)^2\Big[2\alpha_\tau^2\Big(\frac{\Delta^2}{T}\int_0^{T+\Delta}m_\mu(s)\,ds+\sigma^2D\Delta\Big)+(1-\sigma_\tau)^2D\Big]+\frac{D\,L_{\rm est}(\tau)^2}{K}\Bigg\}.
\]
The expectation on the left is over the population trajectory \(Y\) and the Gaussian samples used in \(\bar\mu_K\), with the denoiser fixed.
