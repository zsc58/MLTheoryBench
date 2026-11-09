# Reference Proof

Let
\[
\mathcal R_\mu:=\left\{r:\mathcal X\to[0,\infty)\text{ measurable}:\int r\,d\mu=1\right\}.
\]
Set
\[
g_\tau(x)=p(x)^\tau q(x)^{1-\tau},\qquad F=F(\tau)=\int g_\tau\,d\mu>0,
\]
and define
\[
\rho_\tau(x)=\frac{g_\tau(x)}{F}.
\]
Then \(\rho_\tau\in\mathcal R_\mu\).

For \(r\in\mathcal R_\mu\), write
\[
J_\tau(r)=\frac1\tau D_{\mathrm{KL}}(r\|q)+\frac1{1-\tau}D_{\mathrm{KL}}(r\|p).
\]
Both KL divergences are understood as extended nonnegative values. If \(r\not\ll\rho_\tau\), then \(r\) gives positive mass to a set on which either \(p=0\) or \(q=0\), because \(\rho_\tau=0\) there. Consequently at least one of \(D_{\mathrm{KL}}(r\|p)\) and \(D_{\mathrm{KL}}(r\|q)\) is \(+\infty\), so \(J_\tau(r)=+\infty\). Also \(D_{\mathrm{KL}}(r\|\rho_\tau)=+\infty\), and the desired identity holds in the extended reals.

It remains to consider \(r\ll\rho_\tau\), hence \(r\ll p\) and \(r\ll q\). On the set where \(r>0\), define
\[
A=\log\frac rq,\qquad B=\log\frac rp,\qquad C=\log\frac r{\rho_\tau}.
\]
Since \(\rho_\tau=p^\tau q^{1-\tau}/F\), pointwise
\[
C=(1-\tau)A+\tau B+\log F,
\]
and therefore
\[
\frac1\tau A+\frac1{1-\tau}B
=\frac1{\tau(1-\tau)}(C-\log F).
\]
If both KL divergences on the left are finite, integrating gives
\[
\begin{aligned}
J_\tau(r)
&=\frac1{\tau(1-\tau)}\int r\log\frac r{p^\tau q^{1-\tau}}\,d\mu\\
&=\frac1{\tau(1-\tau)}D_{\mathrm{KL}}(r\|\rho_\tau)
-\frac{\log F}{\tau(1-\tau)}.
\end{aligned}
\]
If either of those KL divergences is infinite, the same pointwise relation still gives the extended-value identity: the negative part of each log-ratio under \(r\) is integrable for probability densities, so an infinite positive KL term cannot be canceled by the other term. Hence in that case \(D_{\mathrm{KL}}(r\|\rho_\tau)=+\infty\) as well, and both sides equal \(+\infty\).

Using
\[
\mathcal S_\tau(P\|Q)=-\frac{\log F}{\tau(1-\tau)},
\]
we have, for every \(r\in\mathcal R_\mu\),
\[
J_\tau(r)=\mathcal S_\tau(P\|Q)+\frac1{\tau(1-\tau)}D_{\mathrm{KL}}(r\|\rho_\tau).
\]
KL nonnegativity yields \(J_\tau(r)\ge \mathcal S_\tau(P\|Q)\). At \(r=\rho_\tau\), the remainder is zero, so the minimum is attained and equals \(\mathcal S_\tau(P\|Q)\). Equality holds exactly when \(D_{\mathrm{KL}}(r\|\rho_\tau)=0\), equivalently when \(r=\rho_\tau\) \(\mu\)-almost everywhere. Thus the minimizer is unique up to \(\mu\)-null sets.
