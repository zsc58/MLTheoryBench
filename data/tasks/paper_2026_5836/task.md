# Problem

## Setup

Let \(Z\) and \(X\) be measurable spaces equipped with fixed reference measures, and let \(q(x\mid z)\) be a jointly measurable conditional probability density defining a Markov kernel from \(Z\) to \(X\). A prior density is a nonnegative measurable density on \(Z\) with integral one. All induced observation laws below admit densities with respect to the reference measure on \(X\); displayed ratios and posteriors are understood almost everywhere on the support where their denominators are positive, with the usual Radon-Nikodym/KL conventions.

For any prior density \(\pi\) on \(Z\), define its induced observation density
\[
m_\pi(x)=\int \pi(z)q(x\mid z)\,dz.
\]
There is a population prior \(\pi^\star\), and the population observation law is its induced marginal \(m^\star=m_{\pi^\star}\) (realizability). For a current prior \(\pi_t\), write \(m_t=m_{\pi_t}\) and define the posterior
\[
\pi_t(z\mid x)=\frac{\pi_t(z)q(x\mid z)}{m_t(x)}.
\]
Starting from a prior \(\pi_0\), the oracle iteration is
\[
\pi_{t+1}(z)=\int m^\star(x)\,\pi_t(z\mid x)\,dx,\qquad t=0,1,2,\ldots.
\]
Assume the simulator is \(\lambda\)-strongly prior-identifiable for some fixed \(\lambda\in(0,1]\): for every pair of prior densities \(\pi_a,\pi_b\) on \(Z\),
\[
\mathrm{KL}(\pi_a\|\pi_b)\le \frac1\lambda\,\mathrm{KL}(m_{\pi_a}\|m_{\pi_b}).
\]
Assume also \(\mathrm{KL}(\pi^\star\|\pi_0)<\infty\).

## Task

Prove that, for every integer \(t\ge0\),
\[
\mathrm{KL}(\pi^\star\|\pi_t)\le (1-\lambda)^t\,\mathrm{KL}(\pi^\star\|\pi_0),
\]
and simultaneously
\[
\mathrm{KL}(m^\star\|m_t)\le (1-\lambda)^t\,\mathrm{KL}(\pi^\star\|\pi_0).
\]
Here integer powers use \(a^0=1\), including when \(a=0\).
