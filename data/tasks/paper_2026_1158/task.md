# Problem

## Setup

Let \((\mathcal X,\mathcal F,\mu)\) be a measure space. Let \(P\) and \(Q\) be probability measures dominated by \(\mu\), with densities \(p=dP/d\mu\) and \(q=dQ/d\mu\). Fix \(\tau\in(0,1)\), and assume
\[
F(\tau):=\int_{\mathcal X}p(x)^\tau q(x)^{1-\tau}\,d\mu(x)>0.
\]
Define
\[
\mathcal S_\tau(P\|Q):=-\frac{\log F(\tau)}{\tau(1-\tau)}.
\]

Let
\[
\mathcal R_\mu:=\left\{r:\mathcal X\to[0,\infty)\text{ measurable}:\int_{\mathcal X}r\,d\mu=1\right\}
\]
denote the set of all probability densities with respect to \(\mu\). For \(r\in\mathcal R_\mu\), define the extended KL divergences by
\[
D_{\mathrm{KL}}(r\|p):=\int r\log(r/p)\,d\mu,
\]
with \(0\log(0/a)=0\) for \(a\ge 0\), \(b\log(b/0)=+\infty\) for \(b>0\), and the usual extended-integral convention; define \(D_{\mathrm{KL}}(r\|q)\) analogously.

## Task

Prove that, for every \(\tau\in(0,1)\),
\[
\mathcal S_\tau(P\|Q)=\min_{r\in\mathcal R_\mu}\left\{\frac{1}{\tau}D_{\mathrm{KL}}(r\|q)+\frac{1}{1-\tau}D_{\mathrm{KL}}(r\|p)\right\}.
\]
Show that the minimizer is unique up to \(\mu\)-null sets and is
\[
\rho_\tau(x)=\frac{p(x)^\tau q(x)^{1-\tau}}{F(\tau)}.
\]
Moreover, establish the decomposition, for every \(r\in\mathcal R_\mu\),
\[
\frac{1}{\tau}D_{\mathrm{KL}}(r\|q)+\frac{1}{1-\tau}D_{\mathrm{KL}}(r\|p)
=\mathcal S_\tau(P\|Q)+\frac{1}{\tau(1-\tau)}D_{\mathrm{KL}}(r\|\rho_\tau).
\]
