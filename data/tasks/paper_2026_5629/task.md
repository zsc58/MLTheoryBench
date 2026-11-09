# Problem

## Setup

Let \(d\ge 2\), let \(\mathbf 1\in\mathbb R^d\) be the all-ones vector, and let
\[
P=I_d-\frac1d\mathbf 1\mathbf 1^\top,\qquad D_\gamma=\operatorname{diag}(\gamma).
\]
When every coordinate of \(\gamma\) is nonzero, write
\[
\gamma^{-1}:=(1/\gamma_1,\ldots,1/\gamma_d)^\top.
\]
For \(i\in\{1,\ldots,d\}\), let \(e_i\) denote the \(i\)-th standard coordinate vector in \(\mathbb R^d\).

For \(\gamma,\beta\in\mathbb R^d\), define
\[
\operatorname{LN}_{\gamma,\beta}(x)=D_\gamma\frac{\sqrt d\,Px}{\|Px\|}+\beta
\]
whenever \(Px\ne0\). For a random vector \(X\) with \(PX\ne0\) almost surely, write \(C_{\mathrm{LN}}=\operatorname{Cov}(\operatorname{LN}_{\gamma,\beta}(X))\).

For a scale vector \(\gamma\) with all coordinates nonzero, define
\[
\operatorname{RMS}_\gamma(x)=D_\gamma\frac{\sqrt d\,x}{\|x\|}
\]
for \(x\ne0\). For a random vector \(Y\ne0\) almost surely with \(\operatorname{Cov}(Y)\succ0\), write \(C_{\mathrm{RMS}}(Y)=\operatorname{Cov}(\operatorname{RMS}_\gamma(Y))\).

## Task

Prove the following integrated theorem. For every admissible LayerNorm input and every scale vector with all coordinates nonzero,
\[
C_{\mathrm{LN}}\gamma^{-1}=0,
\qquad
v_*:=\frac{\gamma^{-1}}{\|\gamma^{-1}\|}
\text{ is a unit kernel direction of }C_{\mathrm{LN}}.
\]
If a LayerNorm scale coordinate \(\gamma_i=0\), then \(C_{\mathrm{LN}}e_i=0\). In contrast, for every all-nonzero \(\gamma\), there is no unit-vector-valued direction \(v(\gamma)\) depending only on \(\gamma\) such that
\[
 v(\gamma)^\top C_{\mathrm{RMS}}(Y)v(\gamma)=0
\]
for every admissible RMSNorm input distribution \(Y\) with positive-definite covariance.
