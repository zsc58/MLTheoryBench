# Problem

## Setup

Let \(P\) and \(Q\) be probability distributions on a common measurable space with densities \(p\) and \(q\) relative to a common dominating measure, using finite-valued versions of these densities. Think of \(P\) as the joint distribution and \(Q\) as the product of its two marginals. Classifiers are measurable functions taking values in \([0,1]\). Define the Bayes density-ratio classifier
\[
 b(z)=\frac{p(z)}{p(z)+q(z)}
\]
where \(p(z)+q(z)>0\), with any measurable \([0,1]\)-valued extension elsewhere.

Call a measurable \([0,1]\)-valued classifier \(h\) balanced if
\[
\mathbb E_P[h]=\mathbb E_Q[1-h],
\]
equivalently \(\mathbb E_P[h]+\mathbb E_Q[h]=1\). This definition permits boundary values 0 and 1.

For the ratio inequalities below, assume \(0<h(z)<1\) wherever \(p(z)+q(z)>0\). Their nonnegative expectations are interpreted in \([0,+\infty]\); finite expectations are not assumed. Values of the ratios outside this set may be chosen arbitrarily and measurably, since it is null under both distributions.

## Task

Prove that every balanced classifier \(h\) satisfying this ratio-domain condition obeys the complementary expected-ratio inequalities
\[
\mathbb E_P\!\left[\frac{b}{h}\right]\ge 1,
\qquad
\mathbb E_Q\!\left[\frac{1-b}{1-h}\right]\ge 1.
\]
Also prove that the Bayes classifier \(b\), which may take boundary values 0 or 1, is itself balanced. Conclude that restricting the \([0,1]\)-valued classifier class to balanced classifiers does not exclude the exact Bayes density-ratio solution.
