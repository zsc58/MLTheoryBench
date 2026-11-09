# Problem

## Setup

Let \(\Omega\subset\mathbb R^d\) be open, with \(d\ge 1\). Let \(s:\Omega\to\mathbb R\) be C1 and define the lifted map
\[
\Phi(x)=(x,s(x))\in\mathbb R^{d+1}.
\]
For a length scale \(\ell>0\), let \(\rho:[0,\infty)\to\mathbb R\) be a radial covariance profile with \(\rho(0)=1\), continuous at zero, and define
\[
K_\ell(x,x')=\rho\!\left(\frac{\|\Phi(x)-\Phi(x')\|_2}{\ell}\right).
\]
For signal standard deviation \(\sigma_f>0\), noise variance \(\sigma_n^2\ge 0\), and \(\delta_{xx'}=1\) if \(x=x'\) and 0 otherwise, set
\[
C_{\ell,f,n}(x,x')=\sigma_f^2K_\ell(x,x')+\sigma_n^2\delta_{xx'}.
\]

## Task

Prove that, as \(x'\to x\) and with \(h=x'-x\),
\[
C_{\ell,f,n}(x,x')
=\sigma_f^2\rho\!\left(\frac{\sqrt{h^T\bar G(x,x')h}}{\ell}\right)
+\sigma_n^2\delta_{xx'}+o(1),
\]
where
\[
\bar G(x,x')=I_d+\tfrac12\left(\nabla s(x)\nabla s(x)^T+\nabla s(x')\nabla s(x')^T\right).
\]
