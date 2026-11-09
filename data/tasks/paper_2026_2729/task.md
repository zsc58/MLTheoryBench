# Problem

## Setup

Let \(Y\in\{0,1\}\), let \(X\) take values in a measurable space \(\mathcal X\), and let \(P\) be the joint law of \((X,Y)\). Write \(\pi_+=P(Y=1)\), assume \(0<\pi_+<1\), and set \(\pi_-=1-\pi_+\). Let \(P_+\), \(P_-\), and \(P_X=\pi_+P_++\pi_-P_-\) denote the positive, negative, and marginal laws of \(X\). Let \(C\) be a nonempty class of measurable functions \(c:\mathcal X\to[0,1]\), and let \(W\) be a finite nonempty class of measurable functions \(w:[0,1]\to[-1,1]\). A predictor is a measurable function \(f:\mathcal X\to[0,1]\). Define
\[
R_{c,w}(f)=\mathbb E[c(X)w(f(X))(Y-f(X))],\qquad MC_{C,W}(f)=\sup_{c\in C,w\in W}|R_{c,w}(f)|.
\]
A predictor is \((C,W,\epsilon)\)-multicalibrated when \(MC_{C,W}(f)\le\epsilon\).

Represent the clean source vector \(B=(P_+,P_-)^\top\) and a finite vector \(\bar P\) of observable source laws on \(\mathcal X\) by a known linear contamination relation \(\bar P=M_{\rm corr}B\). A correction \(M_{\rm corr}^{\dagger}\) is a known measurable matrix of coefficients, possibly depending on \(x\), satisfying
\[
B(dx)=M_{\rm corr}^{\dagger}(x)\bar P(dx)
\]
componentwise as a signed-measure identity. In the constant-matrix case its argument is omitted. Assume every component of each corrected integrand below is integrable under its corresponding observable source law. Define
\[
L_{c,w}(x;f)=\big(\pi_+c(x)w(f(x))(1-f(x)),\,-\pi_-c(x)w(f(x))f(x)\big)^\top.
\]

In the PU model, \(\bar P=(P_+,P_X)^\top\),
\[
M_{\rm PU}=\begin{pmatrix}1&0\\\pi_+&\pi_-\end{pmatrix},
\]
and the supplied value \(\pi_+\) is the true class prior. It and the witness classes are fixed before sampling. Any preprocessing is separate from the PU batches; the assertions below use this true prior, not a different frozen estimate. Given an i.i.d. sample of size \(n_+\ge1\) from \(P_+\) and an independent i.i.d. sample of size \(n_u\ge1\) from \(P_X\), define
\[
\widehat R_{c,w}^{PU}(f)=\frac{\pi_+}{n_+}\sum_{i=1}^{n_+}c(X_i^+)w(f(X_i^+))-\frac1{n_u}\sum_{j=1}^{n_u}c(X_j^u)w(f(X_j^u))f(X_j^u),
\]
and \(\widehat{MC}^{PU}_{C,W}(f)=\sup_{c,w}|\widehat R_{c,w}^{PU}(f)|\).

For \(\eta>0\), let \(N_\infty(\eta,W)\) be the minimum cardinality of a subset \(W_\eta\subseteq W\) such that every \(w\in W\) is within \(\eta\) in sup norm of an element of \(W_\eta\). Define the expected Rademacher complexity by
\[
\mathfrak R_n(C;Q)=\mathbb E_{X_1,\ldots,X_n\sim Q^n,\,\sigma}\left[\sup_{c\in C}\frac1n\sum_{i=1}^n\sigma_i c(X_i)\right],
\]
where the \(\sigma_i\) are independent uniform signs, independent of the sample. There is no absolute value inside this supremum. Assume all suprema, expectations, selection events, and random predictors appearing in the problem are measurable; random predictors are jointly measurable in the observed randomness and \(x\).

Fix \(\epsilon>0\), \(\delta\in(0,1)\), \(C_R\ge0\), and \(d_C\ge0\). Assume
\[
\mathfrak R_{n_+}(C;P_+)\le C_R\sqrt{d_C\log n_+/n_+},\qquad \mathfrak R_{n_u}(C;P_X)\le C_R\sqrt{d_C\log n_u/n_u}.
\]
The sample sizes are positive integers. All logarithms are natural.

Fix a measurable initial predictor \(f_0\) before and independently of all PU batches, and regard it as fixed in the following probability assertions. Let \(f^*(x)=\mathbb E[Y\mid X=x]\) be a measurable version with values in \([0,1]\), and set
\[
D_0=\mathbb E_{P_X}[(f_0(X)-f^*(X))^2],\qquad \lambda=\epsilon/2,\qquad K_\epsilon=\lceil4D_0/\epsilon^2\rceil.
\]
Run the following procedure with fresh independent PU batches of sizes \(n_+,n_u\) at every search call. At round \(t\), search for \(\tau\in\{-1,1\}\), \(c\in C\), and \(w\in W\) with
\[
\tau\widehat R_{c,w}^{PU}(f_t)>3\epsilon/4.
\]
If a witness exists, choose one and set
\[
f_{t+1}(x)=\Pi_{[0,1]}\!\left(f_t(x)+\lambda\tau c(x)w(f_t(x))\right),
\]
where \(\Pi_{[0,1]}(z)=\min\{1,\max\{0,z\}\}\). Otherwise stop and output \(f_t\). The search and witness choice are measurable rules using only the initial predictor, fixed parameters, already observed batches, the current batch, and, optionally, independent auxiliary randomness. They have no access to future batches. Conditional on the observed past, each current batch has the stated product law and is independent of the current predictor. No computational-efficiency claim about the search is required.

## Task

Prove that:

1. For every measurable predictor \(f\) and every \((c,w)\),
\[
R_{c,w}(f)=\int L_{c,w}(x;f)^\top M_{\rm corr}^{\dagger}(x)\,d\bar P(x),
\]
so \(MC_{C,W}(f)\) equals the supremum of the absolute values of these observable weak-supervision moments. In particular, in PU,
\[
R_{c,w}(f)=\pi_+\mathbb E_{P_+}[c(X)w(f(X))]-\mathbb E_{P_X}[c(X)w(f(X))f(X)].
\]
For each fixed \(f,c,w\) independent of the estimating PU samples, \(\widehat R_{c,w}^{PU}(f)\) is unbiased for this moment.

2. For every fixed \(f\) independent of the PU samples and every \(\eta\in(0,1]\), with probability at least \(1-\delta\),
\[
\big|\widehat{MC}^{PU}_{C,W}(f)-MC_{C,W}(f)\big|\le2\sum_{s=1}^2\pi_s\left[\mathfrak R_{n_s}(C;P_s)+\eta+\sqrt{\frac{2\log N_\infty(\eta,W)+\log(4/\delta)}{n_s}}\right],
\]
where \((P_1,n_1,\pi_1)=(P_+,n_+,\pi_+)\) and \((P_2,n_2,\pi_2)=(P_X,n_u,1)\).

3. There is a constant \(C_0>0\), depending only on \(C_R\), such that, if
\[
n_+\ge C_0\,\frac{\pi_+^2(d_C\log n_++L)}{\epsilon^2},\qquad n_u\ge C_0\,\frac{d_C\log n_u+L}{\epsilon^2},\qquad L=\log\frac{4|W|(K_\epsilon+1)}{\delta},
\]
then with probability at least \(1-\delta\) the procedure stops after at most \(K_\epsilon\) successful updates, returns an \((C,W,\epsilon)\)-multicalibrated predictor, and uses at most \((K_\epsilon+1)n_+\) positive and \((K_\epsilon+1)n_u\) unlabeled examples in total.
