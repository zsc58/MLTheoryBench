# Problem

## Setup

Let \(n,p\) be positive integers. Fix data \((x_i,y_i)_{i=1}^n\) with \(x_i\in\mathbb R^p\) and \(y_i\in\mathbb R\), and fix \(\beta\in\mathbb R^p\). Let \(X\in\mathbb R^{n\times p}\) have rows \(x_i^\top\), let \(y=(y_1,\ldots,y_n)^\top\), and define
\[
r=X\beta-y,\qquad R^2=\frac{\|r\|^2}{n},\qquad
\Sigma_x=\frac{X^\top X}{n},\qquad
\Sigma_{rx}=\frac{X^\top r}{n}.
\]

Fix \(\alpha\in(0,1)\), \(\lambda>0\), \(\omega>0\), and \(\tau>0\). Fix \(u\in\mathbb R^p\) satisfying \(\|u\|=1\) and \(u^\top\beta=0\). Independently for each \(i\), sample
\[
\theta_i\sim\operatorname{Unif}[0,2\pi],\qquad
\varepsilon_i\sim\mathcal N(0,\tau^2 I_p),
\]
with all phases and Gaussian vectors mutually independent. Define
\[
z_i=(1-\alpha)x_i+\lambda\cos(\omega\langle x_i,u\rangle+\theta_i)u+\varepsilon_i.
\]
Set
\[
\widehat S=\frac{1}{(1-\alpha)^2}
\left[\frac1n\sum_{i=1}^n z_i z_i^\top-\frac{\lambda^2}{2}uu^\top-\tau^2I_p\right],
\qquad
\widehat b=\frac{1}{n(1-\alpha)}\sum_{i=1}^n y_i z_i,
\]
and \(H=\widehat S\beta-\widehat b\). Finally, let
\[
L(\beta)=\frac{1}{2n}\sum_{i=1}^n(x_i^\top\beta-y_i)^2.
\]

## Task

Prove the exact identity
\[
\mathbb E\|H-\nabla L(\beta)\|^2
=
\frac{R^2(\lambda^2/2+p\tau^2)+2\tau^2\beta^\top\Sigma_{rx}+\tau^2\|\beta\|^2\operatorname{tr}(\Sigma_x)}{n(1-\alpha)^2}
+\frac{\|\beta\|^2\left[\lambda^2\tau^2/2+(p+1)\tau^4\right]}{n(1-\alpha)^4},
\]
where the expectation is over the phases and Gaussian vectors, conditional on the fixed data.
