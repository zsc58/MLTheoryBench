# Problem

## Setup

Let \(\mathcal Y\) be a discrete completion space, let \(r:\mathcal Y\to\{0,1\}\) be a binary verifier, and define the correct set
\[
S=\{y\in\mathcal Y:r(y)=1\}.
\]
Assume that \(S\) is finite and nonempty. Let \(p\) range over probability distributions on \(\mathcal Y\) satisfying
\[
Z:=p(S)=\sum_{y\in S}p(y)>0.
\]
Define the conditional distribution on correct completions and the uniform distribution on the correct set by
\[
q(y)=\frac{p(y)}{Z},\qquad u(y)=\frac1{|S|},\qquad y\in S.
\]
For distributions on \(S\), let
\[
D_{\mathrm{KL}}(u\|q)=\sum_{y\in S}u(y)\log\frac{u(y)}{q(y)},
\]
with the value \(+\infty\) if \(q(y)=0\) for some \(y\in S\). Fix \(\tau>0\), and consider
\[
F(p)=\log Z-\tau D_{\mathrm{KL}}(u\|q).
\]

## Task

Prove that \(F\) has the unique maximizer \(p^\star\) given by
\[
p^\star(y)=
\begin{cases}
\frac1{|S|}, & y\in S,\\
0, & y\notin S.
\end{cases}
\]
