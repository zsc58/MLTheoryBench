# Problem

## Setup

Let \(H\ge1\) and \(N\ge1\) be integers. Let \(\mathcal X_0=\{\perp\},\mathcal X_1,\ldots,\mathcal X_H\) be measurable staged spaces. A reference Markov chain starts at \(X_0=\perp\), uses kernels \(K_h(dx_h\mid x_{h-1})\), and has marginals \(\pi_h\). Let \(r:\mathcal X_H\to[0,\infty)\) be measurable with \(0<Z=\mathbb E_{\pi_H}r<\infty\). Let \(V_h\) be measurable versions of \(\mathbb E[r(X_H)\mid X_h=x]\), with \(V_0(\perp)=Z\) and \(V_H=r\). Define
\[
\pi_h^*(dx)=\frac{V_h(x)}Z\pi_h(dx).
\]
For \(\pi_{h-1}^*\)-almost every parent \(x\), the target transition has density \(V_h(y)/V_{h-1}(x)\) relative to \(K_h(dy\mid x)\); its values at target-null parents are immaterial.

Assume there is a fixed finite constant \(C_{\rm act}\ge1\) such that, for every \(h=1,\ldots,H\) and parent \(x\in\mathcal X_{h-1}\),
\[
V_h(y)\le C_{\rm act}V_{h-1}(x)
\quad\text{for }K_h(\cdot\mid x)\text{-almost every }y.
\]

Fix measurable functions \(\widehat V_h:\mathcal X_h\to[0,\infty)\) satisfying \(\widehat V_H=r\), \(\widehat V_0(\perp)>0\), and
\[
0<\widehat Z_h=\mathbb E_{\pi_h}\widehat V_h<\infty,
\qquad
\widehat\pi_h(dx)=\frac{\widehat V_h(x)}{\widehat Z_h}\pi_h(dx).
\]
All kernels and functions above are fixed inputs, not functions of the particle-filter randomness.

Run the bootstrap particle filter with \(\widehat\nu_0=\delta_\perp\) and \(\widehat W_0=\widehat V_0(\perp)\). At each level \(h\), conditional on the preceding particle history, sample \(N\) iid parents \(A_{h-1}^i\) from \(\widehat\nu_{h-1}\), and independently propagate each parent to a child \(X_h^i\) using \(K_h(\cdot\mid A_{h-1}^i)\). Set
\[
w_h^i=\frac{\widehat V_h(X_h^i)}{\widehat V_{h-1}(A_{h-1}^i)},\qquad
\widehat W_h=\widehat W_{h-1}\frac1N\sum_{i=1}^Nw_h^i,
\qquad
\widehat\nu_h=\frac{\sum_{i=1}^Nw_h^i\delta_{X_h^i}}{\sum_{i=1}^Nw_h^i}.
\]
Assume the filter is non-extinguishing: whenever \(\widehat W_{h-1}>0\), its sampled incremental weights satisfy \(\sum_{i=1}^Nw_h^i>0\) almost surely.

For probability measures \(P,Q\) on the same measurable space, use
\[
D_{\rm TV}(P,Q)=\sup_{B\text{ measurable}}|P(B)-Q(B)|.
\]
If \(P\ll Q\), define \(D_{\chi^2}(P\|Q)=\int(dP/dQ-1)^2\,dQ\), allowing the value \(+\infty\); otherwise set \(D_{\chi^2}(P\|Q)=+\infty\). The expected empirical law is defined by \((\mathbb E\widehat\nu_H)(B)=\mathbb E[\widehat\nu_H(B)]\).

## Task

Prove
\[
D_{\rm TV}(\mathbb E[\widehat\nu_H],\pi_H^*)\le\sqrt{\frac{C_{\rm act}}N}\left(H+\sum_{h=1}^{H-1}\sqrt{D_{\chi^2}(\pi_h^*\|\widehat\pi_h)}\right),
\]
with expectation over particle-filter randomness. The sum is zero when \(H=1\), and an infinite right-hand side is interpreted in the extended sense.
