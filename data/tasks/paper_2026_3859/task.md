# Problem

## Setup

Let \(m\geq1\) and \(d\geq2\) be integers. Work on a product measurable space \(\mathcal X=\mathcal X_1\times\cdots\times\mathcal X_d\) with a fixed product reference measure. All component densities are integrable probability densities with respect to that measure. Densities are identified with their associated measures, and density equalities and linear independence are understood up to null sets.

Work in the square mixing case \(L=m\). Let \(p_1,\ldots,p_m\) be the component probability densities, let \(q_i\) be the marginal density of \(p_i\) on \(\mathcal X_1\times\mathcal X_2\), and let \(a_i\) and \(b_i\) be its first and second marginal densities. Define
\[
R_{12}=\{i\in\{1,\ldots,m\}:q_i=a_i\otimes b_i\},
\]
where \((a\otimes b)(x,y)=a(x)b(y)\). For \(l=1,\ldots,L\), the observed pair-marginal density is
\[
U_l=\sum_{i=1}^m\Theta_{li}q_i,
\]
where \(\Theta\in[0,1]^{L\times m}\), \(\Theta\mathbf1_m=\mathbf1_L\), and \(\Theta\) has full column rank. Write \(U=(U_1,\ldots,U_L)^T\), with \(\mathbf1_j\) denoting the all-ones vector in \(\mathbb R^j\).

For a finite signed measure \(Q\) of total mass one on \(\mathcal X_1\times\mathcal X_2\), let \(Q^{(1)}\) and \(Q^{(2)}\) denote its marginal measures and define
\[
\Pi(Q)=Q^{(1)}\otimes Q^{(2)}.
\]
Call \(Q\) product-form when \(Q=\Pi(Q)\). This convention applies both to signed densities and to empirical measures.

Assume that \(\{a_i:i\in R_{12}\}\) and \(\{b_i:i\in R_{12}\}\) are each linearly independent. Assume also that, for every \(\beta\in\mathbb R^m\) satisfying \(\sum_i\beta_i=1\) and \(\beta_j\ne0\) for at least one \(j\notin R_{12}\), the signed density \(\sum_i\beta_iq_i\) is not product-form.

Let \(k\) be a fixed characteristic positive-definite kernel on \(\mathcal X_1\times\mathcal X_2\), with RKHS \(\mathcal H\), and let \(0\leq K<\infty\) satisfy
\[
\sup_{z\in\mathcal X_1\times\mathcal X_2}k(z,z)\leq K^2.
\]
For the finite signed measures used here, write
\[
\mu(Q)=\int k(z,\cdot)\,dQ(z).
\]
These are Bochner integrals. Assume that the feature map \(z\mapsto k(z,\cdot)\) is strongly measurable under each \(U_l\) and each \(U_l^{(1)}\otimes U_h^{(2)}\), for \(1\leq l,h\leq L\). Characteristic means that the mean embedding is injective on probability measures with defined embeddings. Define
\[
\operatorname{MMD}(Q)=\|\mu(Q)-\mu(\Pi(Q))\|_{\mathcal H}.
\]

Fix positive integer sample sizes \(n_1,\ldots,n_L\). Observe mutually independent random pairs \(Z_{lj}\), \(1\leq l\leq L\), \(1\leq j\leq n_l\), with \(Z_{lj}\) distributed according to \(U_l\). The two coordinates within a pair need not be independent. Define
\[
\widehat U_l=\frac1{n_l}\sum_{j=1}^{n_l}\delta_{Z_{lj}},\qquad
\widehat U_r=\sum_{l=1}^L r_l\widehat U_l,
\]
where \(\delta_z\) is the point mass at \(z\). For \(r\) in the affine hyperplane
\[
A=\{r\in\mathbb R^L:\mathbf1_L^Tr=1\},
\]
set
\[
\widehat{\operatorname{MMD}}(\widehat U_r)
=\|\mu(\widehat U_r)-\mu(\Pi(\widehat U_r))\|_{\mathcal H},
\qquad
d(r)=\operatorname{MMD}(r^TU)^2,
\qquad
\widehat d(r)=\widehat{\operatorname{MMD}}(\widehat U_r)^2.
\]
Thus the empirical product-marginal measure uses the two marginals of \(\widehat U_r\) itself.

For \(i=1,\ldots,m\), let \(e_i\) be the \(i\)-th standard basis vector in \(\mathbb R^m\) and set
\[
r_i=\Theta(\Theta^T\Theta)^{-1}e_i.
\]
Fix a finite deterministic constant
\[
\bar r>\max_{1\leq i\leq m}\|r_i\|_1,
\]
and define
\[
\Delta_{\bar r}=\{r\in A:\|r\|_1\leq\bar r\},
\qquad
N_{1/2}=\sum_{l=1}^Ln_l^{-1/2}.
\]
For a real function \(f\) on \(\Delta_{\bar r}\), write
\[
\|f\|_{\infty,\Delta_{\bar r}}=\sup_{r\in\Delta_{\bar r}}|f(r)|.
\]
Assume that the Hessian of \(d\), as a function on \(A\) with tangent space \(T=\{v\in\mathbb R^L:\mathbf1_L^Tv=0\}\), is positive definite at every \(r_i\) with \(i\in R_{12}\).

## Task

Prove the following integrated theorem.

First, for every \(\delta\in(0,1)\), with probability at least \(1-\delta\),
\[
\sup_{r\in\Delta_{\bar r}}
\left|\operatorname{MMD}(r^TU)-\widehat{\operatorname{MMD}}(\widehat U_r)\right|
\leq10\bar r^2K\Bigl(1+\sqrt{\log(2L^2/\delta)}\Bigr)N_{1/2}.
\]

Second, the zeros of \(d\) on \(\Delta_{\bar r}\) are precisely \(\{r_i:i\in R_{12}\}\). There exist deterministic constants \(\varepsilon_0,c_0>0\), depending only on the fixed population function \(d\) and the search domain \(\Delta_{\bar r}\), not on sample sizes or sample realizations, such that for every sample realization and every \(\varepsilon,c\geq0\) satisfying
\[
\|d-\widehat d\|_{\infty,\Delta_{\bar r}}\leq\varepsilon\leq\varepsilon_0,
\qquad
2\varepsilon\leq c\leq c_0,
\]
the empirical sublevel set
\[
\{r\in\Delta_{\bar r}:\widehat d(r)\leq c\}
\]
has exactly \(|R_{12}|\) connected components, each containing exactly one target vector \(r_i\), \(i\in R_{12}\).
