# Reference Proof

## Proof Structure

Control the instability set by combining the two directional KL divergences into a symmetric KL integral. Partition the set according to the sign of the log density ratio, derive pointwise lower bounds for the integrand in terms of each density on both parts, and integrate to obtain simultaneous probability bounds.

## Complete Proof

Let \(\mu=F_\#\pi_0\) and \(\nu=\pi_1\), with strictly positive densities \(p\) and \(q\). Define
\[
J:=D_{\mathrm{KL}}(\mu\|\nu)+D_{\mathrm{KL}}(\nu\|\mu)
 =\int_{\mathbb R^d}(p-q)\log\frac pq\,dx.
\]
The assumptions give \(J\le 2\varepsilon\).

Fix \(\delta>0\), write \(r(x)=\log(p(x)/q(x))\), and partition
\[
A_\delta=S_+\sqcup S_-,\qquad S_+=\{r\ge\delta\},\quad S_-=\{r\le-\delta\}.
\]
Set \(c=\delta(1-e^{-\delta})\). On \(S_+\), \(p\ge e^\delta q\), so
\[
(p-q)r\ge \delta(1-e^{-\delta})p=c p,
\]
and also \((p-q)r\ge \delta(e^\delta-1)q\ge c q\). On \(S_-\), \(q\ge e^\delta p\) and \(-r\ge\delta\), hence
\[
(p-q)r=(q-p)(-r)\ge \delta(e^\delta-1)p\ge c p,
\]
and likewise \((p-q)r\ge\delta(1-e^{-\delta})q=cq\). Therefore, throughout \(A_\delta\), the integrand is at least both \(cp\) and \(cq\). Integrating yields
\[
J\ge c\int_{A_\delta}p\,dx=c\,\mu(A_\delta),\qquad
J\ge c\int_{A_\delta}q\,dx=c\,\nu(A_\delta).
\]
Consequently,
\[
\max\{\mu(A_\delta),\nu(A_\delta)\}
 \le \frac{J}{\delta(1-e^{-\delta})}
 \le \frac{2\varepsilon}{\delta(1-e^{-\delta})}.
\]
Since \(\mu=F_\#\pi_0\) and \(\nu=\pi_1\), these are exactly the two asserted probability bounds.
