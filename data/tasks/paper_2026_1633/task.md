# Problem

## Setup

An experiment consists of a measurable instance space \(\mathcal X\), a measurable hypothesis space \(\mathcal H\) of binary classifiers, a distribution \(D\) on \(\mathcal X\times\{0,1\}\), and a prior probability measure \(\Pi\) on \(\mathcal H\). Prediction evaluation is jointly measurable. The spaces may vary across experiments; the existential lower bound below is not asserted for every fixed hypothesis class.

For each positive integer \(m\), observe \(S=((X_i,Y_i))_{i=1}^m\sim D^m\), with independent identically distributed observations. The prior is fixed independently of \(S\). A posterior is a probability measure on \(\mathcal H\). Define
\[
L_D(Q)=\mathbb E_{h\sim Q,(X,Y)\sim D}[\mathbf 1\{h(X)\ne Y\}],\qquad
L_S(Q)=\frac1m\sum_{i=1}^m\mathbb E_{h\sim Q}[\mathbf 1\{h(X_i)\ne Y_i\}].
\]
All logarithms in entropy and relative entropy are base two. Let
\[
H(q)=-q\log_2 q-(1-q)\log_2(1-q),\qquad 0\le q\le1,
\]
with \(0\log_2 0=0\). Relative entropy is
\[
\mathrm{KL}(Q\Vert\Pi)=\int\log_2\!\left(\frac{dQ}{d\Pi}\right)dQ
\]
when \(Q\ll\Pi\), and is \(+\infty\) otherwise, with the usual extended-value conventions.

For fixed \(\lambda>0\), let \(\widehat Q_\lambda(S)\) be a measurable choice of a minimizer of
\[
mH(L_S(Q))+\lambda\,\mathrm{KL}(Q\Vert\Pi)
\]
over posteriors satisfying \(L_S(Q)\le\tfrac12\). Only experiments for which this constrained minimum is finite and attained \(D^m\)-almost surely, and a measurable minimizing choice exists, for every \(m\ge1\), are considered. The choice uses the sample and the specified prior, not additional information about \(D\). The claims are to hold for any such minimizing choice.

For \(L^*\in(0,1/2)\), let \(\mathcal M(L^*)\) be the set of these experiments, denoted \((\Pi,D)\) with their spaces understood, for which there exists a fixed posterior \(Q^*\) with \(L_D(Q^*)=L^*\) and \(\mathrm{KL}(Q^*\Vert\Pi)\le10\). Define
\[
W_\lambda(L^*)=\sup_{(\Pi,D)\in\mathcal M(L^*)}\limsup_{m\to\infty}\mathbb E_{S\sim D^m}L_D(\widehat Q_\lambda(S)).
\]
For \(0\le q\le1\), set
\[
T_\lambda(q)=\min_{0\le p\le1/2}\{\lambda\,\mathrm{KL}(\operatorname{Bern}(p)\Vert\operatorname{Bern}(q))+H(p)\}.
\]
For \(0<\lambda\le1\), define \(\ell_\lambda(L^*)=1-2^{-H(L^*)/\lambda}\). For \(\lambda>1\) and \(0<q\le1/2\), define
\[
p_\lambda(q)=\left[1+\left(\frac{1-q}{q}\right)^{\lambda/(\lambda-1)}\right]^{-1},\qquad
U_\lambda(q)=\lambda\,\mathrm{KL}(\operatorname{Bern}(p_\lambda(q))\Vert\operatorname{Bern}(q))+H(p_\lambda(q)).
\]
Set \(p_\lambda(0)=0\) and \(U_\lambda(0)=0\) by continuity. Let \(\ell_\lambda(L^*)\) be the inverse value in \((0,1/2)\) satisfying \(U_\lambda(\ell_\lambda(L^*))=H(L^*)\); establishing existence and uniqueness is part of the task.

## Task

Prove that for every fixed \(\lambda>0\) and \(L^*\in(0,1/2)\):

1. **Finite-sample upper bound.** Uniformly over \((\Pi,D)\in\mathcal M(L^*)\),
\[
\mathbb E_{S\sim D^m}L_D(\widehat Q_\lambda(S))\le\ell_\lambda(L^*)+\rho_{m,\lambda,L^*},
\]
where \(\rho_{m,\lambda,L^*}\to0\) as \(m\to\infty\). Supply the PAC-Bayes/KL and sampling rates in the proof. The remainder may depend on \(\lambda,L^*\), but not on the experiment.

2. **Matching lower bound and sharpness.** For every \(L'\) with \(L^*\le L'<\ell_\lambda(L^*)\), there is one experiment \((\Pi,D)\in\mathcal M(L^*)\), fixed independently of \(m\), such that
\[
\liminf_{m\to\infty}\mathbb E_{S\sim D^m}L_D(\widehat Q_\lambda(S))\ge L'.
\]
Consequently \(W_\lambda(L^*)=\ell_\lambda(L^*)\).
