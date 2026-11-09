# Problem

## Setup

Let \(M\ge1\) be an integer, and let \(X_1,\ldots,X_M\) be iid real-valued observations with probability density \(g\in L^1(\mathbb R)\cap L^\infty(\mathbb R)\). Define
\[
\varphi(\eta)=\int_{\mathbb R}e^{i\eta x}g(x)\,dx,
\qquad
\widehat\varphi_M(\eta)=M^{-1}\sum_{m=1}^Me^{i\eta X_m}.
\]
Assume that \(\varphi\) is Lipschitz on every finite interval.

Fix nonnegative integers \(K,L\) with \(K+L\ge1\), a finite location bound \(H\ge0\), and finite scale bounds
\[
0<\sigma_-\le\sigma_+<\infty,
\qquad 0<b_-\le b_+<\infty.
\]
Let \(\Theta\) be the set of parameters \(\theta=(\beta^G,\mu,\sigma,\beta^L,\nu,b)\) satisfying
\[
\beta_k^G,\beta_\ell^L\ge0,
\quad \sum_{k=1}^K\beta_k^G+\sum_{\ell=1}^L\beta_\ell^L=1,
\]
\[
|\mu_k|,|\nu_\ell|\le H,
\qquad \sigma_-\le\sigma_k\le\sigma_+,
\qquad b_-\le b_\ell\le b_+.
\]
Empty component sums are interpreted as zero. Define the normalized positive mixture density
\[
\widehat g(x;\theta)=\sum_{k=1}^K\beta_k^G\frac{e^{-(x-\mu_k)^2/(2\sigma_k^2)}}{\sqrt{2\pi}\sigma_k}
+\sum_{\ell=1}^L\beta_\ell^L\frac{e^{-|x-\nu_\ell|/b_\ell}}{2b_\ell},
\]
whose characteristic function is
\[
\Phi_\theta(\eta)=\sum_{k=1}^K\beta_k^G e^{i\eta\mu_k-\sigma_k^2\eta^2/2}
+\sum_{\ell=1}^L\beta_\ell^L\frac{e^{i\eta\nu_\ell}}{1+b_\ell^2\eta^2}.
\]
Let \(\Theta_{\mathrm{fit}}\subseteq\Theta\) be a fixed nonempty feasible search set, independent of the sample.

For a deterministic truncation radius \(T>0\), consider a deterministic partition with an integer \(P\ge1\),
\[
-T=\xi_0<\xi_1<\cdots<\xi_P=T.
\]
Choose deterministic training nodes \(\eta_p\in[\xi_{p-1},\xi_p]\), and set
\[
\Delta_p=\xi_p-\xi_{p-1},\qquad
\Delta_{\min}=\min_p\Delta_p,\qquad
\Delta_{\max}=\max_p\Delta_p.
\]
Assume
\[
\Delta_{\min}=\frac{c_0}{P},\qquad
\Delta_{\max}=\frac{c_1}{P},
\]
where \(c_0,c_1>0\) are finite deterministic constants, independent of \(P\); they may depend on \(T\).

For residuals \(r_p(\theta)=\widehat\varphi_M(\eta_p)-\Phi_\theta(\eta_p)\), set
\[
\mathrm{MSE}_{M,P}(\theta)=P^{-1}\sum_p|r_p(\theta)|^2,
\quad
R_{M,P}(\theta)=P^{-1}\sum_p\bigl(|\Re r_p(\theta)|+|\Im r_p(\theta)|\bigr),
\]
and
\[
\mathrm{Loss}_{M,P}(\theta)=\mathrm{MSE}_{M,P}(\theta)+\lambda R_{M,P}(\theta),
\qquad \lambda\ge0,
\]
with deterministic \(\lambda\). For the chosen window and grid, let \(\widehat\theta\) be a measurable sample-based choice of a minimizer of this loss over \(\Theta_{\mathrm{fit}}\). Assume that such a choice is available and that, for a deterministic \(\varepsilon_1>0\),
\[
\mathrm{Loss}_{M,P}(\widehat\theta)\le\varepsilon_1
\quad\text{almost surely}.
\]

Define
\[
V_P=P^{-1}\sum_p\bigl(1-|\varphi(\eta_p)|^2\bigr),
\qquad
W_P=P^{-1}\sum_p\sqrt{1-|\varphi(\eta_p)|^2}.
\]

## Task

Prove that for every \(\varepsilon>0\), there exists a deterministic truncation radius \(T>0\) and a finite constant \(C'(T)>0\), independent of \(P\), \(\theta\), and the sample, such that every grid and associated estimator satisfying the setup for that window obey
\[
\mathbb E\!\left[\int_{\mathbb R}|g(x)-\widehat g(x;\widehat\theta)|^2\,dx\right]
<\frac1{2\pi}\left[4\varepsilon+c_1\left(2\varepsilon_1+\frac{2V_P}{M}+\lambda\sqrt{\frac2M}\,W_P\right)+\frac{C'(T)c_1^2}{P}\right].
\]
The constant may depend on \(g\), \(T\), and the fixed parameter bounds. The expectation is unconditional over the iid sample; it is not conditioned on a realized training-loss event.
