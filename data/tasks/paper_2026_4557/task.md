# Problem

## Setup

Let (A,T,S) be jointly distributed on Polish spaces \(\mathcal A,\mathcal T,\mathcal S\), respectively, equipped with their Borel sigma-algebras. A deterministic predictor is a measurable map \(g:\mathcal A\times\mathcal S\to\mathcal T\), with output \(V_g=g(A,S)\). A revealed randomized predictor has output \(\widetilde V=(R,G(A,S,R))\), where R is Uniform[0,1] and independent of (A,T,S), and \(G:\mathcal A\times\mathcal S\times[0,1]\to\mathcal T\) is jointly measurable. R is revealed as part of the output, so \(\widetilde V\) takes values in \([0,1]\times\mathcal T\).

For either kind of output V, define \(q(V)=I(V;T)\) and \(d(V)=I(V;S\mid T)\), interpreting mutual information and conditional mutual information through relative entropy. A predictor is admissible when both quantities are finite.

Let

\[
D=\{(d(V_g),q(V_g)):g\text{ is measurable and admissible}\},
\]

and let Rset be the analogous set of pairs for admissible revealed randomized outputs. Closures below are taken in the Euclidean topology of \(\mathbb R^2\). For \(v\geq0\), define

\[
\phi_R(v)=\sup\{q:(d,q)\in\overline{\mathrm{Rset}},\ d\leq v\}.
\]

For any \(E\subseteq\mathbb R^2\), write

\[
\phi_E(v)=\sup\{q:(d,q)\in E,\ d\leq v\},
\]

with suprema in the extended reals and \(\sup\varnothing=-\infty\).

## Task

Prove that, with \(C=\overline{\operatorname{conv}(D)}\),

\[
\operatorname{conv}(D)\subseteq\mathrm{Rset}\subseteq C,
\]

so \(\overline{\mathrm{Rset}}=C\) and \(\phi_R(v)=\phi_C(v)\) for every \(v\geq0\). Prove also that \(\phi_R\) is concave as a \([0,+\infty]\)-valued function on \([0,+\infty)\), and that, for every \(v\geq0\) with finite \(\phi_R(v)\) and every \(\epsilon>0\), there are admissible deterministic predictors \(g_1,g_2\) and \(\lambda\in[0,1]\) satisfying

\[
\lambda d(V_{g_1})+(1-\lambda)d(V_{g_2})\leq v+\epsilon
\]

and

\[
\lambda q(V_{g_1})+(1-\lambda)q(V_{g_2})\geq\phi_R(v)-\epsilon.
\]

Thus arbitrary revealed randomization gives the concave closure of the deterministic frontier, with at most two deterministic predictors sufficient for frontier approximation.
