# Reference Proof

## Proof Structure

Condition the population KL risk on the covariate. Justify the conditional logarithmic integrals using the inherited Dirichlet family, compute the expected log posterior, and normalize its exponential. The Gibbs variational identity gives an exact nonnegative excess KL. A fixed prior comparator bounds the oracle conditional risk uniformly, making the attainable population minimum finite and establishing the characterization for every minimizer almost everywhere. Finally, sum the concentration parameters and apply the definition of vacuity.

## Complete Proof

### step_001: Conditional objective and integrability

Choose a measurable conditional probability vector
\[
m(x)=(m_1(x),\ldots,m_K(x)),\qquad m_k(x)=P^*_{Y\mid X}(k\mid x).
\]
It lies in \(\Delta^{K-1}\); its values on any exceptional \(P_X^*\)-null set may be chosen arbitrarily in that simplex. Let \(\mu\) denote the coordinate simplex measure from the task. For \(b\in(0,\infty)^K\), write
\[
B(b)=\int_{\Delta^{K-1}}\prod_{k=1}^K p_k^{b_k-1}\,d\mu(p),
\qquad
r_b(p)=\frac{1}{B(b)}\prod_{k=1}^K p_k^{b_k-1}.
\]
The Dirichlet normalizing constant is finite and strictly positive for positive parameters.

For every such \(b\), all coordinate logarithms are absolutely integrable under \(r_b\). Indeed, for \(a>0\), the function \(t^{a/2}|\log t|\) is bounded on \((0,1)\). Consequently, for a finite constant \(C_{b_k}\),
\[
\int r_b(p)|\log p_k|\,d\mu(p)
\le C_{b_k}\frac{B(b-(b_k/2)e_k)}{B(b)}<\infty.
\]
Every parameter in the numerator is still positive. Thus the logarithm of any Dirichlet density with positive parameters is absolutely integrable under any other such Dirichlet law. In particular, the conditional entropy and cross-entropy terms used below are finite for every model predictor at a fixed \(x\). This also applies to the prior and to the candidate oracle laws constructed below. Values of logarithms on the boundary of the simplex do not matter, since that boundary is \(\mu\)-null.

For a Dirichlet density \(q\) with positive parameters, define
\[
\mathcal R_x(q)=\sum_{y=1}^K m_y(x)\operatorname{KL}(q\|\pi_y^\nu).
\]
By conditioning the nonnegative loss,
\[
R^\nu(\phi)=\mathbb E_{P_X^*}[\mathcal R_X(q_X^\phi)].
\]
This identity holds even when a competing predictor has infinite population risk. The conditional risks themselves are finite for each fixed \(x\).

### step_002: Expected log posterior

Set
\[
h_x(p)=\sum_{y=1}^K m_y(x)\log\pi_y^\nu(p).
\]
The justified finite sum of conditional integrals gives
\[
\mathcal R_x(q)=\int q(p)\log q(p)\,d\mu(p)-\int q(p)h_x(p)\,d\mu(p).
\]
Since \(\pi_y^\nu=\operatorname{Dir}(\alpha+\nu e_y)\), its log density on the simplex interior is
\[
\log\pi_y^\nu(p)=-\log B(\alpha+\nu e_y)
+\sum_{k=1}^K(\alpha_k-1+\nu\mathbf 1\{y=k\})\log p_k.
\]
Therefore
\[
h_x(p)=-\sum_{y=1}^K m_y(x)\log B(\alpha+\nu e_y)
+\sum_{k=1}^K(\alpha_k-1+\nu m_k(x))\log p_k.
\]
The label normalizers are constant in \(p\).

### step_003: Variational identity and uniqueness

Let
\[
Z_x=\int e^{h_x(p)}\,d\mu(p),\qquad r_x(p)=e^{h_x(p)}/Z_x.
\]
The preceding expression has Dirichlet exponents with parameters \(\alpha_k+\nu m_k(x)>0\), so \(0<Z_x<\infty\), and \(r_x\) is a Dirichlet density with positive parameters. All logarithmic integrals in the following identity are therefore justified by step_001:
\[
\mathcal R_x(q)=\operatorname{KL}(q\|r_x)-\log Z_x.
\]
This is the Gibbs variational identity in the form needed here.

For completeness, its minimization assertion follows from KL nonnegativity and its equality condition. When \(r>0\) almost everywhere and \(q,r\) are normalized densities, put \(F(t)=t\log t-t+1\), with \(F(0)=1\). The elementary inequality \(F(t)\ge0\), with equality only at \(t=1\), yields
\[
\operatorname{KL}(q\|r)=\int r(p)F(q(p)/r(p))\,d\mu(p)\ge0.
\]
Equality holds exactly when \(q=r\) almost everywhere. All densities used in the conditional comparison are positive on the simplex interior, so these hypotheses hold. Consequently \(r_x\) uniquely minimizes the conditional objective among the positive-parameter Dirichlet laws, and indeed among all densities for which the same variational objective is defined.

### step_004: Identification of the normalized law

Write \(\beta(x)=\alpha+\nu m(x)\). Direct normalization gives
\[
Z_x=B(\beta(x))\exp\!\left(-\sum_{y=1}^K m_y(x)\log B(\alpha+\nu e_y)\right)
\]
and
\[
r_x(p)=\frac{1}{B(\beta(x))}\prod_{k=1}^Kp_k^{\beta_k(x)-1}.
\]
Thus
\[
r_x=\operatorname{Dir}(\alpha+\nu m(x)).
\]
Let
\[
c(x)=-\log Z_x=\mathcal R_x(r_x).
\]
The exact conditional excess-risk identity is
\[
\mathcal R_x(q)=c(x)+\operatorname{KL}(q\|r_x).
\]
Zero entries of \(m(x)\) cause no problem: the corresponding concentration remains \(\alpha_k>0\), and no logarithm of \(m_k(x)\) is taken.

### step_005: Finite attainable population risk and all minimizers

It remains to justify passage from conditional minimization to every population minimizer, without assuming that every competing population risk is finite. Let \(\pi=\operatorname{Dir}(\alpha)\) and define
\[
M=\max_{1\le y\le K}\operatorname{KL}(\pi\|\pi_y^\nu)<\infty.
\]
Finiteness follows from step_001 and the finite number of labels. Conditional optimality and nonnegativity imply
\[
0\le c(x)\le\mathcal R_x(\pi)
=\sum_{y=1}^K m_y(x)\operatorname{KL}(\pi\|\pi_y^\nu)\le M.
\]
The prior is used only as a comparator in the conditional variational problem; it need not be represented by the parameterized model.

The model maps and the chosen conditional probability vector are measurable. The resulting densities, conditional risks, and excess KL terms are measurable as well; for the latter, the nonnegative integral representation using \(F\) above supplies a direct justification. Integrating the conditional identity therefore gives the extended-real identity
\[
R^\nu(\phi)=C+\mathbb E_{P_X^*}\!\left[\operatorname{KL}(q_X^\phi\|r_X)\right],
\qquad C=\mathbb E_{P_X^*}[c(X)]\in[0,M].
\]
There is no subtraction of infinite quantities in this formula.

By simultaneous representability, some \(\phi_0\in\Phi\) satisfies \(q_X^{\phi_0}=r_X\) almost surely. Hence \(R^\nu(\phi_0)=C<\infty\), and the minimum population risk equals \(C\). If \(\phi^*\) is any population minimizer, the identity implies
\[
\mathbb E_{P_X^*}\!\left[\operatorname{KL}(q_X^{\phi^*}\|r_X)\right]=0.
\]
A nonnegative measurable random variable with zero expectation is zero almost surely. The equality condition for KL then gives
\[
q_x^{\phi^*}=r_x=\operatorname{Dir}\!\left(\alpha+\nu P^*_{Y\mid X}(\cdot\mid x)\right)
\]
for \(P_X^*\)-almost every \(x\). Uniqueness is uniqueness of the predicted laws, not necessarily uniqueness of their network parameters.

### step_006: Evidence and uncertainty consequence

For every \(x\) on the full-measure set where the characterization holds,
\[
\sum_{k=1}^K\beta_k(x)=\sum_{k=1}^K\alpha_k+\nu\sum_{k=1}^K m_k(x)=\alpha_0+\nu.
\]
By the definition of vacuity,
\[
u(\beta(x))=\frac{K}{\alpha_0+\nu}.
\]
For fixed \(\alpha\), \(\nu\), and the DGP, these oracle quantities have no dependence on \(n\); in particular, the positive vacuity does not decrease merely because the sample size increases. This conclusion concerns the population optimizer and this specified concentration-based statistic. It neither asserts convergence of empirical minimizers nor identifies predictor values on \(P_X^*\)-null sets.
