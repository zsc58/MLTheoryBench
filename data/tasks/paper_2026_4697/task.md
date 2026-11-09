# Problem

## Setup

Fix integers \(T\ge1\), \(n\ge2\), and dimension \(d\ge1\). Fix known parameters \(\mu\in\mathbb R^d\) and a positive definite covariance matrix \(\Sigma\), a known target \(z^*\in\mathbb R^d\), and a known insertion time \(\tau\in\{1,\ldots,T\}\). The target and insertion time are fixed independently of the sampled data.

Under \(H_0\), draw independent batches \(D_t=(X_{t,1},\ldots,X_{t,n})\), \(t=1,\ldots,T\), with all entries independent and distributed as \(N_d(\mu,\Sigma)\). Under \(H_1^\tau\), first draw the same independent Gaussian batches, then independently select an index uniformly from \(\{1,\ldots,n\}\) and replace that entry of \(D_\tau\) by \(z^*\). In either experiment, \(X_{t,k}\) below denotes the resulting entry, after replacement when applicable.

Define the batch means and cumulative releases by
\[
\bar X_t=\frac1n\sum_{k=1}^nX_{t,k},\qquad
\widehat\mu_t=\frac1{nt}\sum_{j=1}^t\sum_{k=1}^nX_{j,k},\qquad t=1,\ldots,T.
\]
An observer sees \((\widehat\mu_1,\ldots,\widehat\mu_T)\) and knows \(n,T,\tau,z^*,\mu,\Sigma\). Tests are measurable functions of the stated observations and known quantities, with independent randomization allowed. For a test \(A\), let \(\alpha=\Pr_{H_0}[A=1]\) and \(\beta=\Pr_{H_1^\tau}[A=0]\). Let \(\Phi\) denote the standard normal CDF.

## Task

Prove the following integrated theorem.

Let \(\delta=z^*-\mu\), \(c(n)=n/(n-1)\), and \(m^*=\delta^T\Sigma^{-1}\delta\). The Neyman-Pearson-optimal test for \(H_0\) versus \(H_1^\tau\) thresholds the observed log likelihood ratio, which is a function only of \(\bar X_\tau\) and equals
\[
\ell_\tau=\frac d2\log c(n)-\frac{n}{2(n-1)}(\bar X_\tau-\mu)^T\Sigma^{-1}(\bar X_\tau-\mu)+c(n)(\bar X_\tau-\mu)^T\Sigma^{-1}\delta-\frac{m^*}{2(n-1)}.
\]
Here optimality means maximizing power at a fixed Type-I error level. For a real threshold \(\gamma\), use the test that rejects \(H_0\) when \(\ell_\tau>\gamma\).

In the scalar case \(d=1\), set
\[
a=\sqrt{nm^*},\qquad \gamma_{\max}=\tfrac12(m^*+\log c(n)).
\]
If \(\gamma\le\gamma_{\max}\), define
\[
b=\sqrt{(n-1)(m^*+\log c(n)-2\gamma)}.
\]
The errors are then
\[
\alpha=\Phi(a+b)-\Phi(a-b),\qquad
\beta=\Phi\!\left(\frac a{\sqrt{c(n)}}-b\sqrt{c(n)}\right)+\Phi\!\left(-\frac a{\sqrt{c(n)}}-b\sqrt{c(n)}\right).
\]
If \(\gamma>\gamma_{\max}\), then \((\alpha,\beta)=(0,1)\). For each fixed threshold, these errors depend on \(n\) and \(m^*\), but not on \(\tau\) or \(T\).

For comparison, still in the scalar case \(d=1\), suppose that only the final release \(\widehat\mu_T\) is observed, with the same known quantities and the same hypotheses. Define
\[
q=nT,\qquad c_T=\frac q{q-1},\qquad a_T=\sqrt{qm^*},\qquad
\gamma_{\max}^{(T)}=\tfrac12(m^*+\log c_T).
\]
The final-only likelihood-ratio test rejects when its log likelihood ratio exceeds \(\gamma\). If \(\gamma\le\gamma_{\max}^{(T)}\), define
\[
b_T=\sqrt{(q-1)(m^*+\log c_T-2\gamma)}.
\]
Its Type-I and Type-II errors are
\[
\alpha_F=\Phi(a_T+b_T)-\Phi(a_T-b_T),
\]
\[
\beta_F=\Phi\!\left(\frac {a_T}{\sqrt {c_T}}-b_T\sqrt {c_T}\right)+\Phi\!\left(-\frac {a_T}{\sqrt {c_T}}-b_T\sqrt {c_T}\right).
\]
For \(\gamma>\gamma_{\max}^{(T)}\), they are \((\alpha_F,\beta_F)=(0,1)\). Explain why replacing \(n\) by \(nT\) represents dilution of the single inserted target across all observations.
