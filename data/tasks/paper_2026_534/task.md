# Problem

## Setup

Let \(K\ge 2\) be an integer, let \(d,n\ge 1\) be integers, let \(X\in\mathbb R^d\), and let \(Y\in\{1,\ldots,K\}\). Assume \((Y_i,X_i)_{i=1}^n\) are iid from
\[
P^*_{Y,X}=P^*_{Y\mid X}P_X^*,
\]
where \(P_X^*\) is absolutely continuous with respect to Lebesgue measure. Write \(P^*_{Y\mid X}(\cdot\mid x)\) for a measurable version of the conditional probability vector, and let
\[
\Delta^{K-1}=\{p\in[0,1]^K:\textstyle\sum_k p_k=1\}.
\]
All simplex densities are taken with respect to coordinate Lebesgue measure in \((p_1,\ldots,p_{K-1})\), with \(p_K=1-\sum_{k=1}^{K-1}p_k\).

Fix \(\alpha\in(0,\infty)^K\) and \(\nu>0\). For \(y\in\{1,\ldots,K\}\), define the tempered posterior density on \(\Delta^{K-1}\) by
\[
\pi_y^\nu(p)\propto \operatorname{Dir}(p;\alpha)\,p_y^\nu,
\]
so equivalently \(\pi_y^\nu=\operatorname{Dir}(\alpha+\nu e_y)\), where \(e_y\) is the \(y\)-th standard basis vector.

Let \(\Phi\) be a class of neural-network parameters. Each \(\phi\in\Phi\) determines a Borel-measurable map \(g^\phi:\mathbb R^d\to[0,\infty)^K\), with finite coordinates, and the predictor
\[
q_x^\phi=\operatorname{Dir}\!\left(\alpha+g^\phi(x)\right).
\]
Define
\[
\ell^\nu(\phi;y,x)=\operatorname{KL}(q_x^\phi\|\pi_y^\nu),
\qquad
R^\nu(\phi)=\mathbb E_{P^*_{Y,X}}[\ell^\nu(\phi;Y,X)]\in[0,\infty].
\]
Assume the model class represents the distribution-valued function
\[
x\longmapsto\operatorname{Dir}\!\left(\alpha+\nu P^*_{Y\mid X}(\cdot\mid x)\right)
\]
by a single parameter in \(\Phi\), up to a \(P_X^*\)-null set, and that the population minimum of \(R^\nu\) is attained.

For a Dirichlet law with concentration vector \(b\in(0,\infty)^K\), its total evidence, including the prior pseudo-counts, means \(\sum_{k=1}^K b_k\). Define its concentration-based uncertainty statistic, called vacuity, by
\[
u(b)=\frac{K}{\sum_{k=1}^K b_k}.
\]

## Task

Prove that every population-risk minimizer \(\phi^*\) satisfies, for \(P_X^*\)-almost every \(x\),
\[
q_x^{\phi^*}=\operatorname{Dir}\!\left(\alpha+\nu P^*_{Y\mid X}(\cdot\mid x)\right),
\]
where equality is equality of probability laws, equivalently equality of densities almost everywhere on the simplex.

Consequently, writing \(\alpha_0=\sum_{k=1}^K\alpha_k\), prove that for \(P_X^*\)-almost every \(x\), the optimal law has total evidence \(\alpha_0+\nu\) and vacuity
\[
u\!\left(\alpha+\nu P^*_{Y\mid X}(\cdot\mid x)\right)=\frac{K}{\alpha_0+\nu}.
\]
Thus, with \(\alpha\), \(\nu\), and the data-generating distribution fixed, these oracle quantities are independent of the sample size \(n\), while their values remain controlled by the externally chosen temperature \(\nu\).
