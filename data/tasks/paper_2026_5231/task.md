# Problem

## Setup

Let \(a>0\). For each individual, let \(D\) be a latent drift satisfying \(|D|\le M\) almost surely, where \(M\in[0,\infty)\) is a known finite constant, and let \(B\) be a standard Brownian motion starting at zero and independent of \(D\). Define
\[
 X_t=B_t+Dt,\qquad S=\inf\{t>0:|X_t|=a\},
\]
and let \(Y=1\) if \(X_S=a\) and \(Y=-1\) if \(X_S=-a\). The observed pairs \((Y_i,S_i)\), \(i=1,\ldots,n\), are i.i.d. copies of \((Y,S)\). Write \(\mu=\mathbb E[D]\).

For a fixed \(d\in\mathbb R\), let \(\mathbb E_d\) denote expectation in the same Brownian model with deterministic drift \(d\) and boundary \(a\), regardless of whether \(d\) belongs to the support of \(D\).

For \(\beta>0\), put \(c_k(\beta)=(2k+1)\beta\), \(k\ge0\), and define, for \(t>0\),
\[
 w_\beta(t)=
 \frac{\displaystyle\sum_{k=0}^{\infty}
 \left(\frac{c_k(\beta)^2}{t}-1\right)
 \exp\!\left(-\frac{c_k(\beta)^2}{2t}\right)}
 {\displaystyle\sum_{k=0}^{\infty}(-1)^k c_k(\beta)
 \exp\!\left(-\frac{c_k(\beta)^2}{2t}\right)}.
\]

For \(\lambda>0\), set
\[
 \ell_n(\lambda)=\frac1n\sum_{i=1}^n e^{-\lambda S_i},
 \qquad L_a(\lambda)=\mathbb E[e^{-\lambda S}].
\]
Let \((\lambda_n)_{n\ge1}\) be a deterministic sequence of strictly positive numbers such that \(\lambda_n\to\infty\) and \(\sqrt{\lambda_n}=o(\log n)\). Define
\[
 \widehat a_n^{(1)}=-\frac{\log\ell_n(\lambda_n)}{\sqrt{2\lambda_n}},
 \qquad
 \widetilde a_n=
 \frac{\log\ell_n(\lambda_n)-\log\ell_n(4\lambda_n)}
 {\sqrt{2\lambda_n}},
\]
and
\[
 \widehat\mu_n(a)=\frac1n\sum_{i=1}^nY_iw_a(S_i),
 \qquad
 \widehat\mu_n^{\rm PI}=\frac1n\sum_{i=1}^nY_iw_{\widetilde a_n}(S_i).
\]

## Task

Prove the following integrated claim.

1. If the boundary \(a\) is known, then \(\mathbb E[\widehat\mu_n(a)]=\mu\). Moreover, among smooth functions \(g:(0,\infty)\to\mathbb R\) satisfying \(\mathbb E_d[|g(S)|]<\infty\) for every \(d\in\mathbb R\), \(w_a\) is the unique function such that
\[
 \mathbb E_d[Yg(S)]=d\qquad\text{for every }d\in\mathbb R.
\]

2. With unknown common boundary,
\[
 \widehat a_n^{(1)}\xrightarrow{p}a,
 \qquad \widetilde a_n\xrightarrow{p}a.
\]
The population two-scale analogue has bias \(O(\lambda^{-1})\):
\[
 \frac{\log L_a(\lambda)-\log L_a(4\lambda)}{\sqrt{2\lambda}}-a
 =O(\lambda^{-1})\qquad(\lambda\to\infty).
\]
In contrast,
\[
 \left|-\frac{\log L_a(\lambda)}{\sqrt{2\lambda}}-a\right|
 =\Omega(\lambda^{-1/2}).
\]
Finally, \(\widehat\mu_n^{\rm PI}\xrightarrow{p}\mu\).
