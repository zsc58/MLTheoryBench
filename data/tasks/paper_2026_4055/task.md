# Problem

## Setup

Let \(\mathcal Z\) be a standard Borel space, and let \((Z_i)_{i\ge1}\) be an infinitely exchangeable sequence in \(\mathcal Z\): for every integer \(k\ge1\) and every permutation \(\pi\) of \(\{1,\ldots,k\}\),
\[
(Z_1,\ldots,Z_k)\stackrel{d}= (Z_{\pi(1)},\ldots,Z_{\pi(k)}).
\]
Let \(\Lambda\) be a directing random probability measure such that, conditional on \(\Lambda\), the \(Z_i\) are iid with common law \(\Lambda\).

Fix an integer \(m\ge1\). Let \(h:\mathcal Z^m\to\mathbb R\) be measurable, and assume that it has finite bounded-difference constants \(d_1,\ldots,d_m\in[0,\infty)\): for each i,
\[
|h(z)-h(z')|\le d_i
\]
whenever \(z,z'\in\mathcal Z^m\) agree in every coordinate other than possibly i. Write \(H=h(Z_1,\ldots,Z_m)\) and define
\[
B_h:=\mathbb E[H\mid\Lambda]-\mathbb EH.
\]
Assume that, for some \(s_{\mathrm{mix}}^2\in[0,\infty)\),
\[
\mathbb E e^{\lambda B_h}\le
\exp\!\left(\frac{\lambda^2s_{\mathrm{mix}}^2}{2}\right)
\qquad\text{for every }\lambda\in\mathbb R.
\]

For the linear-contrast clauses below, suppose additionally that the variables are real-valued and \(\mathbb E|Z_1|<\infty\), and write \(m(\Lambda)=\mathbb E[Z_1\mid\Lambda]\). For an integrable real random variable Y, use the convention
\[
\operatorname{Var}(Y)=\mathbb E[(Y-\mathbb EY)^2]\in[0,\infty].
\]
In the displayed tail bounds, interpret \(\exp(-a/0)=0\) for \(a>0\).

## Task

Prove the following theorem.

The statistic \(H-\mathbb EH\) satisfies, for every \(\lambda\in\mathbb R\),
\[
\mathbb E e^{\lambda(H-\mathbb EH)}
\le \exp\!\left\{\frac{\lambda^2}{2}
\left(\frac14\sum_{i=1}^m d_i^2+s_{\mathrm{mix}}^2\right)\right\}.
\]
Consequently, with \(s_{\mathrm{eff}}^2=\frac14\sum_{i=1}^m d_i^2+s_{\mathrm{mix}}^2\), for every \(t>0\),
\[
\mathbb P(|H-\mathbb EH|\ge t)
\le2\exp\!\left(-\frac{t^2}{2s_{\mathrm{eff}}^2}\right).
\]

Moreover, for every integer \(N\ge1\) and coefficients \(b_1,\ldots,b_N\in\mathbb R\), let \(L=\sum_{i=1}^N b_iZ_i\). Then
\[
\mathbb E[L\mid\Lambda]
=\left(\sum_{i=1}^N b_i\right)m(\Lambda).
\]
Thus, if \(\sum_i b_i=0\), the mixture fluctuation \(\mathbb E[L\mid\Lambda]-\mathbb EL\) is identically zero, so a zero mixture proxy is valid. Conversely, if \(\operatorname{Var}(m(\Lambda))>0\), a zero mixture proxy for this contrast is possible only if \(\sum_i b_i=0\).

Finally, suppose \(\ell,u\in\mathbb R\), \(\ell\le u\), and \(Z_i\in[\ell,u]\) almost surely, and let \(R=u-\ell\). For integers \(1\le n<N\), define
\[
D_{n,N}=\frac1n\sum_{j=1}^n Z_j-\frac1N\sum_{j=1}^N Z_j.
\]
Then, for every \(t>0\),
\[
\mathbb P(|D_{n,N}|\ge t)
\le2\exp\!\left(-\frac{2t^2nN}{R^2(N-n)}\right).
\]
Equivalently, show that with probability at least \(1-\alpha\), for \(0<\alpha<1\),
\[
|D_{n,N}|\le R\sqrt{\frac{N-n}{2nN}\log\frac2\alpha}.
\]
