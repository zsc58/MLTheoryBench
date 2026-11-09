# Problem

## Setup

Let \(d\geq1\) be an integer, and let \(P\) and \(Q\) be Borel probability measures on \(\mathbb R^d\). Let \(X\sim P\) and \(Y\sim Q\) be independent with finite second moments, and define
\[
D=Y-X,\qquad M=(X+Y)/2,\qquad v(m)=\mathbb E[D\mid M=m].
\]
Let \(P_M\) denote the law of \(M\). Assume the null implication that \(P=Q\) entails \(v(M)=0\) almost surely.

Use an independent training sample, with sigma-field \(\mathcal G\), to construct a measurable vector field \(\psi:\mathbb R^d\to\mathbb R^d\) depending only on the training data. Assume that, almost surely with respect to training,
\[
\int\|\psi(m)\|^2\,P_M(dm)<\infty.
\]
Conditional on the training data, regard \(\psi\) as fixed. The evaluation pairs \((X_i,Y_i)_{i\geq1}\) are iid copies of \((X,Y)\) and are independent of \(\mathcal G\). The distributions \(P,Q\) and the trained field are held fixed as the evaluation sample size \(n\) tends to infinity.

For \(n\geq2\), set
\[
M_i=(X_i+Y_i)/2,\qquad D_i=Y_i-X_i,\qquad
S_i=\langle\psi(M_i),D_i\rangle,
\]
\[
\bar S_n=\frac1n\sum_{i=1}^n S_i,\qquad
\widehat\sigma_n^2=\frac1{n-1}\sum_{i=1}^n(S_i-\bar S_n)^2,\qquad
\widehat\sigma_n=\sqrt{\widehat\sigma_n^2}.
\]
Define the conditional population quantities
\[
T=\mathbb E[S_i\mid\mathcal G],\qquad
\sigma^2=\operatorname{Var}(S_i\mid\mathcal G),
\]
and assume \(0<\sigma^2<\infty\) almost surely with respect to training. Write \(\sigma=\sqrt{\sigma^2}\) and \(\mathrm{SNR}=T/\sigma\).

Define \(Z_n=\sqrt n\,\bar S_n/\widehat\sigma_n\) when \(\widehat\sigma_n>0\), and set \(Z_n=0\) otherwise. Also interpret the centered studentized ratio in the task below as zero when \(\widehat\sigma_n=0\). Let \(\Phi\) be the standard normal cumulative distribution function, fix \(\alpha\in(0,1)\), and set \(z_{1-\alpha}=\Phi^{-1}(1-\alpha)\).

## Task

Prove that, for almost every training realization, conditionally on the training data,
\[
\frac{\sqrt n(\bar S_n-T)}{\widehat\sigma_n}\Rightarrow N(0,1).
\]
Under \(H_0:P=Q\), prove that \(Z_n\Rightarrow N(0,1)\) under the same conditional law.

Under any fixed alternative \(P\ne Q\), prove that, for almost every training realization with \(T>0\), the one-sided test rejecting when \(Z_n>z_{1-\alpha}\) has conditional power
\[
\Pr(Z_n>z_{1-\alpha}\mid\mathcal G)
=1-\Phi\!\left(z_{1-\alpha}-\sqrt n\,\mathrm{SNR}\right)+o(1)
\]
as \(n\to\infty\), and that this power converges to one. The \(o(1)\) is taken for each such fixed training realization.
