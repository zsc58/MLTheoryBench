# Problem

## Setup

Let \(d\ge1\). Let \(P,Q\) be arbitrary Borel probability distributions on \(\mathbb R^d\). Let \(\psi\) be any probability density on \(\mathbb R^d\), let \(h>0\), and define \(\psi_h(u)=h^{-d}\psi(u/h)\). For probability measures \(R,S\), define
\[
d_h(R,S):=d_{\rm TV}(R*\psi_h,S*\psi_h),
\]
where \(d_{\rm TV}\) is total variation distance.

Observe independent samples \(X_1,\ldots,X_n\sim P\) and \(Y_1,\ldots,Y_m\sim Q\), with \(n,m\ge1\), and write
\[
\widehat P_n=\frac1n\sum_{i=1}^n\delta_{X_i},\qquad
\widehat Q_m=\frac1m\sum_{j=1}^m\delta_{Y_j}.
\]
For \(n\ge2\), split the \(X\)-sample into its first \(n_1=\lfloor n/2\rfloor\) observations and its remaining \(n_2=n-n_1\) observations, and denote the corresponding empirical measures by \(\widehat P_n^{(1)},\widehat P_n^{(2)}\). Define \(\widehat Q_m^{(1)},\widehat Q_m^{(2)}\) analogously when \(m\ge2\). Set
\[
A=d_h(\widehat P_n^{(1)},\widehat P_n^{(2)}),\qquad B=d_h(\widehat Q_m^{(1)},\widehat Q_m^{(2)}).
\]
For \(\alpha\in(0,1)\), let
\[
\varepsilon_{r,s,\alpha}=\sqrt{\frac{\log(1/\alpha)}2\left(\frac1r+\frac1s\right)}.
\]
A randomized statistic \(L\) is a distribution-free lower confidence bound for \(D=d_h(P,Q)\) at level \(1-\alpha\) if \(\Pr\{D\ge L\}\ge1-\alpha\) for every \(P,Q\) (and analogously for an upper bound).

## Task

Prove the following theorem. For every \(d\ge1\), every \(P,Q\), every probability density \(\psi\), every \(h>0\), every \(n,m\ge1\), and every \(\alpha\in(0,1)\), define
\[
\widehat U_\alpha=d_h(\widehat P_n,\widehat Q_m)+\varepsilon_{n,m,\alpha}.
\]
If \(\min(n,m)\ge2\), define
\[
\widehat L_\alpha=\max\left\{0,\ d_h(\widehat P_n,\widehat Q_m)-A-B-3\varepsilon_{n-1,m-1,\alpha}\right\},
\]
and if \(\min(n,m)=1\), define \(\widehat L_\alpha=0\). Then both statistics are distribution-free confidence bounds:
\[
\Pr\{d_h(P,Q)\le\widehat U_\alpha\}\ge1-\alpha,
\qquad
\Pr\{d_h(P,Q)\ge\widehat L_\alpha\}\ge1-\alpha.
\]
The probabilities are over the joint samples (and any auxiliary randomness, if used).
