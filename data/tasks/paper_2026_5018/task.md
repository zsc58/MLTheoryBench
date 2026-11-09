# Problem

## Setup

Let \(\pi_0\) and \(\pi_1\) be probability distributions on \(\mathbb R^d\), and let \(F\) be a flow map. Write \(\mu=F_\#\pi_0\) and \(\nu=\pi_1\). Assume that \(\mu\) and \(\nu\) have strictly positive Lebesgue densities \(p\) and \(q\), respectively. Suppose that for some \(\varepsilon>0\),
\[
D_{\mathrm{KL}}(\mu\|\nu)\le\varepsilon,
\qquad
D_{\mathrm{KL}}(\nu\|\mu)\le\varepsilon.
\]
For \(\delta>0\), define the likelihood-ratio instability set
\[
A_\delta=\left\{x\in\mathbb R^d:\left|\log\frac{p(x)}{q(x)}\right|\ge\delta\right\}.
\]

## Task

Prove that, for every \(\delta>0\),
\[
\Pr_{X\sim F_\#\pi_0}\!\left(\left|\log\frac{p(X)}{q(X)}\right|\ge\delta\right)
\le \frac{2\varepsilon}{\delta(1-e^{-\delta})},
\]
and
\[
\Pr_{Y\sim \pi_1}\!\left(\left|\log\frac{p(Y)}{q(Y)}\right|\ge\delta\right)
\le \frac{2\varepsilon}{\delta(1-e^{-\delta})}.
\]
