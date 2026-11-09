# Problem

## Setup

Let \(P_0\) and \(P_1\) be probability distributions with densities \(p_0,p_1\) with respect to a common measure, and assume common support with density ratio
\[
r(x)=p_1(x)/p_0(x),\qquad 0<c\le r(x)\le C<\infty\quad(P_0\text{-a.e.}).
\]
Let \(r_n\) be a density-ratio estimator trained on data independent of an evaluation sample \(X_1,\ldots,X_n\stackrel{\mathrm{iid}}\sim P_0\). Assume the estimator is clipped so that \(c\le r_n(x)\le C\) and is consistent: for \(P_0\)-almost every \(x\), \(r_n(x)\to r(x)\) in probability with respect to the training randomness.

Define Chernoff Information by
\[
C(P_0,P_1)=-\inf_{0<u<1}\log\int p_0(x)^{1-u}p_1(x)^u\,dx.
\]
Define the CINE estimate
\[
\widehat C_n=\sup_{u\in[0,1]}\left[-\log\left(\frac1n\sum_{i=1}^n r_n(X_i)^u\right)\right].
\]

## Task

Prove that \(\widehat C_n\to C(P_0,P_1)\) in probability as \(n\to\infty\).
