# Problem

## Setup

Let \(M\) be a compact space equipped with a full-support reference measure \(\mu\). Let \(p_0:M\to(0,\infty)\) be a continuous prior density with \(\int_M p_0\,d\mu=1\). Let \(G:M\to\mathbb{R}\) be continuous and bounded below, and let \(\tau>0\). For any probability density \(p\) with respect to \(\mu\), define
\[
\mathrm{KL}(p\|p_0)=\int_M p(m)\log\frac{p(m)}{p_0(m)}\,d\mu(m)
\]
(with value \(+\infty\) when appropriate), and define
\[
J(p)=\int_M p(m)G(m)\,d\mu(m)+\tau\,\mathrm{KL}(p\|p_0).
\]

## Task

Prove that the variational problem \(\inf_p J(p)\), over all probability densities \(p\) with respect to \(\mu\), has a unique minimizer, and that its density is
\[
 p_\tau(m)=\frac{e^{-G(m)/\tau}p_0(m)}{\displaystyle\int_M e^{-G(u)/\tau}p_0(u)\,d\mu(u)}.
\]
