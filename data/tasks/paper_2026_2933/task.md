# Problem

## Setup

Let \(N\ge 2\) be an integer denoting the number of reconstruction levels, and let \(X\sim\mathcal N(0,\sigma^2)\) with \(\sigma>0\). A scalar quantizer is defined by sorted thresholds \(t_0,\ldots,t_N\) and reconstruction levels \(l_0,\ldots,l_{N-1}\), with
\[
\mathsf q(x)=l_k\quad\text{for }t_k<x\le t_{k+1},\qquad k=0,\ldots,N-1.
\]
For a uniform quantizer, use
\[
l_k=sk+z\quad(k=0,\ldots,N-1),\qquad
t_j=s(j-\tfrac12)+z\quad(j=1,\ldots,N-1),
\]
with spacing \(s>0\), offset \(z\), and outer thresholds \(t_0=-\infty\), \(t_N=\infty\). Choose the offset or equivalent indexing so that the quantizer is symmetric, with endpoint reconstruction levels \(-C\) and \(C\) for some \(C>0\); thus \(s=2C/(N-1)\), and samples with \(|X|>C\) saturate to the corresponding endpoint level.

Use an additive error-power model: its clipping contribution is the mean-square error from saturating \(X\) to \([-C,C]\), and its stepping contribution is stipulated to be \(s^2/12\), corresponding to a uniform stepping-error model on \([-s/2,s/2]\). Denote the total modeled error power by \(E(C)\). Define \(\operatorname{SNR}(C)\) as input mean-square power divided by total modeled error power.

Define
\[
\phi(u)=(2\pi)^{-1/2}e^{-u^2/2},\qquad
Q(a)=\int_a^\infty\phi(u)\,du.
\]

## Task

Prove that the modeled quantization mean-square error is
\[
E(C)=2(\sigma^2+C^2)Q(C/\sigma)-2C\sigma\phi(C/\sigma)+\frac{C^2}{3(N-1)^2},
\]
where the first two terms are the Gaussian clipping contribution and the last term is the stepping contribution. Consequently, show that
\[
\operatorname{SNR}(C)=\frac{\sigma^2}{E(C)},
\]
and that any numerical maximizer \(C^*\in\arg\max_{C>0}\operatorname{SNR}(C)\) (equivalently, a minimizer of \(E(C)\)) defines the normal-optimal symmetric uniform quantizer for this modeled objective via \(s^*=2C^*/(N-1)\), the corresponding symmetry-compatible offset or indexing, midpoint thresholds, and endpoint levels.
