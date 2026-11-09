# Problem

## Setup

For each dimension \(p\) along an asymptotic sequence, let \(s=s_p\) be an integer with \(1\le s<p\), and let \(n_1,n_2\) be nonnegative integers with \(n_2>n_1\) and \(n=n_1+n_2\). The sample sizes and noise variances below are deterministic and may depend on \(p\). Let \(X\in\mathbb R^{n\times p}\) have independent standard Gaussian entries. Fix an unknown deterministic signal
\[
\theta^\star\in\mathcal C_{p,s}:=\{\theta\in\{0,1\}^p:\|\theta\|_0=s\}.
\]
Observe \((X,Y)\), where
\[
Y=X\theta^\star+Z,
\qquad
Z\sim N\!\left(0,\operatorname{diag}(\tau_1^2 I_{n_1},\tau_2^2 I_{n_2})\right)
\]
and \(Z\) is independent of \(X\), with \(0<\tau_1^2<\tau_2^2\). Here \(I_k\) is the \(k\times k\) identity matrix, and a block of size zero is omitted. The agnostic exhaustive estimator is any measurable choice, based only on \((X,Y)\) and \(s\), of
\[
\widehat\theta\in\arg\min_{\theta\in\mathcal C_{p,s}}\|Y-X\theta\|_2^2.
\]
For a vector \(v\), write \(\operatorname{supp}(v)\) for its support. Fix \(\delta\in(0,1)\) and \(\varepsilon>0\). Let
\[
N_*=
\begin{cases}
2s\log(p/s),& s=o(p),\ s\to\infty,\\
2h(\alpha)p,& s=\alpha p\text{ for fixed }\alpha\in(0,1),
\end{cases}
\]
where \(h(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)\) and all logarithms are natural. In the second regime, the dimensions are taken along a sequence for which \(\alpha p\) is an integer.

## Task

Prove that if
\[
n_1\log\!\left(1+\frac{\delta(2\tau_2^2-\tau_1^2)s}{2\tau_2^4}\right)
+n_2\log\!\left(1+\frac{\delta s}{2\tau_2^2}\right)
\ge (1+\varepsilon)N_*,
\]
then, as \(p\to\infty\) in either regime,
\[
\Pr_{X,Z}\!\left(\left|\operatorname{supp}(\widehat\theta)\triangle\operatorname{supp}(\theta^\star)\right|<2\delta s\right)
\ge 1-\exp\!\left(-\frac{\varepsilon+o(1)}{2}N_*\right),
\]
where \(\triangle\) denotes symmetric difference and the \(o(1)\) term is along the corresponding asymptotic sequence. In particular, the probability tends to one.
