# Problem

## Setup

Let \(C\) be a causal setting with observed-data law \(P_{\mathrm{obs}}\), interventional law \(P_{\mathrm{int}}\), and an identified estimand \(\theta=\bar Q(P_{\mathrm{obs}})=Q(P_{\mathrm{int}})\in\Theta\), where \(\Theta\) is open in \(\mathbb R^d\) and \(d\geq1\). Observe i.i.d. \(O_1,\ldots,O_n\sim P_{\mathrm{obs}}\). Let \(\eta\) belong to a normed nuisance space, with truth \(\eta_0\), and let \(\ell(O;u,\eta)\) be a measurable loss. For a fixed nuisance value define
\[
L_n(u;\eta)=\frac1n\sum_{i=1}^n\ell(O_i;u,\eta),\qquad
L(u;\eta)=E_{P_{\mathrm{obs}}}[\ell(O;u,\eta)].
\]
Let \(\theta^\star=\theta\) be a population minimizer of \(L(\cdot;\eta_0)\), and let \(V_0=\nabla_{uu}L(\theta^\star;\eta_0)\) be positive definite.

For the cross-fitted loss, split the indices into folds \(I_1,\ldots,I_K\) independently of the observed values. Let \(\hat\eta^{(-k)}\) be estimated using only observations outside \(I_k\), and write \(\hat\eta=(\hat\eta^{(-1)},\ldots,\hat\eta^{(-K)})\). Set
\[
L_n(u;\hat\eta)=\frac1n\sum_{k=1}^K\sum_{i\in I_k}\ell(O_i;u,\hat\eta^{(-k)}),
\qquad r_n=\max_{1\leq k\leq K}\|\hat\eta^{(-k)}-\eta_0\|.
\]
Thus \(L_n(u;\eta_0)\) is the same empirical loss evaluated with the true nuisance in every fold. Fix \(\omega>0\) and a prior density \(\pi\) on \(\Theta\). For either \(\eta=\eta_0\) or \(\eta=\hat\eta\), assume the following normalizing constant is positive and finite, and define the posterior density
\[
q_n(u;\eta)=\frac{e^{-\omega nL_n(u;\eta)}\pi(u)}{\int_\Theta e^{-\omega nL_n(v;\eta)}\pi(v)\,dv}.
\]
Set \(q_{n,\mathrm{or}}=q_n(\cdot;\eta_0)\) and \(q_{n,\mathrm{fe}}=q_n(\cdot;\hat\eta)\), and choose measurable corresponding empirical minimizers \(\hat\theta_{\mathrm{or}}\) and \(\hat\theta_{\mathrm{fe}}\). For total-variation comparisons, regard these posteriors as measures on \(\mathbb R^d\) assigning zero mass outside \(\Theta\).

Assume:

(A1) Both posteriors satisfy Bernstein-von Mises approximations in total variation,
\[
d_{\mathrm{TV}}\!\left(q_{n,j},\mathcal N\!\left(\hat\theta_j,(n\omega V_0)^{-1}\right)\right)=o_P(1),\quad j\in\{\mathrm{or},\mathrm{fe}\}.
\]

(A2) The loss is Neyman-orthogonal at \((\theta^\star,\eta_0)\): for every admissible target and nuisance direction, the mixed derivative \(D_\eta D_u L_n(\theta^\star;\eta_0)\) applied to those directions vanishes.

(A3) \(r_n\to0\) in probability, and the empirical centers satisfy
\[
\|\hat\theta_{\mathrm{fe}}-\hat\theta_{\mathrm{or}}\|=O_P(r_n^2).
\]

## Task

Prove
\[
d_{\mathrm{TV}}(q_{n,\mathrm{fe}},q_{n,\mathrm{or}})=O_P(\sqrt n\,r_n^2)+o_P(1).
\]
In particular, prove that if \(r_n=o_P(n^{-1/4})\), then \(d_{\mathrm{TV}}(q_{n,\mathrm{fe}},q_{n,\mathrm{or}})\to0\) in probability and the feasible posterior inherits the oracle Bernstein-von Mises asymptotic uncertainty with its feasible center.
