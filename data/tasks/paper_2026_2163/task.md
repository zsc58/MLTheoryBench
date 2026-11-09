# Problem

## Setup

Fix a positive integer \(t\), observations \(x_{1:t}\), and a concentration parameter \(\alpha>0\) in a Dirichlet-process mixture model. Observations are distinguished by their indices, even if their values coincide. A clustering \(z\) is a partition of \(\{1,\ldots,t\}\); write \(K(z)\) for its number of blocks. For a nonempty block \(B\), let
\[
\ell(B)=\int\prod_{i\in B}f(x_i\mid\theta)\,dG_0(\theta),
\]
where \(f(\cdot\mid\theta)\) is the component sampling density or mass function and \(G_0\) is the fixed common component-parameter prior. Assume these integrals are well-defined and finite. Let \(P\) denote the posterior probability distribution on clusterings, with mass proportional to
\[
\alpha^{K(z)}\prod_{B\in z}\Gamma(|B|)\,\ell(B),
\]
and assume the sum of these weights over all clusterings is strictly positive.

Let \(\{E^1,\ldots,E^m\}\) be a partition of \(\{1,\ldots,t\}\) into nonempty sets, with \(m\geq2\). Let \(O\) be the event that every cluster is contained entirely in one partition element. Assume \(P(O)>0\), and write \(P_O=P(\cdot\mid O)\).

For a finite set \(A\), let \(\mathcal Z(A)\) be the set of its partitions. Identify a tuple in \(\prod_{r=1}^m\mathcal Z(E^r)\) with the clustering obtained by taking the union of its blocks. For \(z\in O\), let \(z^r\) denote its restriction to \(E^r\), and let \(p_r\) be the marginal distribution of \(z^r\) under \(P_O\). Distributions on this product space are regarded as distributions on all clusterings by assigning zero mass outside \(O\).

For probability distributions \(a,b\) on the same finite space, define
\[
\mathrm{KL}(a\Vert b)=\sum_z a(z)\log\frac{a(z)}{b(z)},
\]
where terms with \(a(z)=0\) are zero and a term with \(a(z)>0=b(z)\) is \(+\infty\).

Let \(q\) be any probability distribution on the product space satisfying \(\operatorname{supp}(q)\subseteq\operatorname{supp}(P_O)\). Write \(q_r\) for its coordinate marginals and \(q^*=\bigotimes_{r=1}^m q_r\). A particle approximation here means a probability distribution represented by finitely many clusterings with nonnegative weights summing to one.

## Task

Prove that conditioning on \(O\) makes the posterior factorize:
\[
P_O(z)=\prod_{r=1}^m p_r(z^r),\qquad z\in O.
\]

Moreover, prove that \(q^*\) minimizes reverse KL among all probability distributions on \(\prod_{r=1}^m\mathcal Z(E^r)\) having the prescribed marginals \(q_r\), both for the conditional posterior and for the full posterior. In particular, prove
\[
\mathrm{KL}(q\Vert P_O)\geq\mathrm{KL}(q^*\Vert P_O),
\qquad
\mathrm{KL}(q\Vert P)\geq\mathrm{KL}(q^*\Vert P),
\]
with equality in either comparison exactly when \(q=q^*\) as probability distributions.

Conclude that replacing any particle approximation supported on \(O\cap\operatorname{supp}(P)\) by the product of its subproblem marginals cannot increase reverse KL to the full Dirichlet-process posterior.
