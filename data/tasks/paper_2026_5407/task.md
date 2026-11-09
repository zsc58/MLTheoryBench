# Problem

## Setup

Let \((\Omega,\mathcal F)\) be a measurable path space. Let \(\Gamma\) be a finite nonzero measure, set
\[
Z=\Gamma(\Omega),\qquad \Pi=\Gamma/Z,
\]
and let \(P\) be a current proposal probability law on this space. Assume that \(P\) and \(\Pi\) are mutually absolutely continuous and that
\[
R=\frac{d\Pi}{dP}>0\quad P\text{-almost surely}.
\]
Thus \(d\Gamma/dP=ZR\) and \(\mathbb E_P[R]=1\).

Assume
\[
R\in L^2(P)
\quad\text{and}\quad
\mathbb E_P\!\big[R^\tau|\log R|^2\big]<\infty
\quad\text{for every }\tau\in[0,1].
\]
For probability measures \(Q,S\) on \((\Omega,\mathcal F)\), define the extended relative entropy by
\[
D_{\mathrm{KL}}(Q\|S)=
\begin{cases}
\displaystyle\int f\log f\,dS,&Q\ll S,\quad f=dQ/dS,\\
+\infty,&Q\not\ll S,
\end{cases}
\]
with \(0\log0=0\). Given \(\varepsilon>0\), suppose the problem
\[
q_\varepsilon^*\in\mathop{\arg\min}_{q}
D_{\mathrm{KL}}(q\|\Pi)
\quad\text{subject to}\quad
D_{\mathrm{KL}}(q\|P)\le\varepsilon,
\]
where \(q\) ranges over probability measures on \((\Omega,\mathcal F)\), has a solution.

For \(\tau\in[0,1]\), define the escort path
\[
q_\tau(dx)=
\frac{R(x)^\tau}{\mathbb E_P[R^\tau]}
P(dx).
\]
Also define
\[
\chi^2(\Pi\|Q)=
\int\left(\frac{d\Pi}{dQ}-1\right)^2dQ
\]
when \(\Pi\ll Q\) and the integral is finite, and let \(W_\tau=d\Gamma/dq_\tau\).

## Task

Prove the following integrated theorem.

The escort path satisfies \(q_0=P\) and \(q_1=\Pi\), and the exact constrained update is \(q_\varepsilon^*=q_{\tau_*}\) for some \(\tau_*\in(0,1]\). More precisely:

- If \(0<\varepsilon<D_{\mathrm{KL}}(\Pi\|P)\), then \(\tau_*\) is the unique point of \((0,1)\) such that
  \[
  D_{\mathrm{KL}}(q_{\tau_*}\|P)=\varepsilon.
  \]
- If \(\varepsilon\ge D_{\mathrm{KL}}(\Pi\|P)\), then one may take \(\tau_*=1\), and \(q_\varepsilon^*=\Pi\).

Along the whole path, \(\tau\mapsto D_{\mathrm{KL}}(q_\tau\|P)\) is nondecreasing and \(\tau\mapsto D_{\mathrm{KL}}(q_\tau\|\Pi)\) is nonincreasing. If \(P\ne\Pi\), these two maps are respectively strictly increasing and strictly decreasing.

Finally, for every \(\tau\in[0,1]\),
\[
Z^{-2}\operatorname{Var}_{q_\tau}(W_\tau)
=
\chi^2(\Pi\|q_\tau).
\]
This common quantity is nonincreasing in \(\tau\), and it is strictly decreasing on the escort path whenever \(P\ne\Pi\).
