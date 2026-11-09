# Problem

## Setup

Let D and K be positive integers and let
\[
\Delta^{D-1}=\{x\in\mathbb R_{\geq0}^D:\textstyle\sum_i x_i=1\}.
\]
The observed states p_1,...,p_{t+1} take values in this simplex. Write F_t=\sigma(p_{1:t}), and let \phi be a measurable summary of the observed history. Fix a summary value g=\phi(p_{1:t}) and work under its conditional probability law. If the summary event has probability zero, use a specified regular conditional law; the assertions concern summary values where that law and the assumptions below hold, almost surely with respect to the summary distribution.

Let Z\in\{1,...,K\}, with
\[
\pi_z=\Pr(Z=z\mid g)>0,
\qquad
u_z=\mathbb E[p_{t+1}\mid Z=z,g].
\]
Thus \sum_z\pi_z=1. Assume the summary is aliased: the u_z are not all equal.

### Loss Convention

For probability vectors x,q, define ordinary natural-log KL by
\[
\mathrm{KL}(x\Vert q)=\sum_i x_i\log(x_i/q_i),
\]
where a term with x_i=0 is zero, and a term with x_i>0 and q_i=0 is +\infty.

Fix a finite smoothing parameter \varepsilon\geq0 and define
\[
S_\varepsilon(x)_i=\frac{x_i+\varepsilon}{1+D\varepsilon},
\qquad
\mathrm{KL}_\varepsilon(x\Vert q)
=\mathrm{KL}(S_\varepsilon(x)\Vert S_\varepsilon(q)).
\]
The same \varepsilon is used for every target, forecast, and oracle comparison. The choice \varepsilon=0 is the unsmoothed convention; in that case assume every coordinate of every u_z is strictly positive. The choice \varepsilon>0 is the common small-probability smoothing convention.

For any forecast Q taking values in the simplex, define its conditional oracle excess risk by
\[
\mathcal E_g^\varepsilon(Q)
=\mathbb E[\mathrm{KL}_\varepsilon(p_{t+1}\Vert Q)\mid g]
-\sum_z\pi_z\,\mathbb E[\mathrm{KL}_\varepsilon(p_{t+1}\Vert u_z)\mid Z=z,g].
\]
A fixed-summary forecaster outputs a single q(g)\in\Delta^{D-1} at each summary value; it has no additional dependence on Z or on the history within that summary value.

### Successor-Local Class

A successor-local forecaster has the form
\[
a_t=\lambda_t p_t+(1-\lambda_t)r_t,
\qquad
\widehat p_{t+1}=(1-\rho_t)a_t+\rho_t T_ta_t.
\]
Fix 0\leq\rho_{\max}\leq1. The controls satisfy \lambda_t\in[0,1] and \rho_t\in[0,\rho_{\max}], and all choices use only causal information.

A causal representation has the form h_s=E(p_{1:s}). The strictly causal memory at time t consists of pairs
\[
\mathcal M_t=\{(h_s,p_{s+1}):1\leq s<t\}.
\]
Retrieval is a causally chosen convex combination of its stored successor values. Exact convex retrieval or finite-softmax retrieval is allowed. For finite-softmax retrieval the weights are
\[
\alpha_s=\frac{\exp(\ell_s)}{\sum_{j<t}\exp(\ell_j)},\qquad s<t,
\]
with finite scores \ell_s determined from the causal representation and memory. A finite-softmax limit means a limit of such parameterizations; it does not permit access to p_{t+1}. The abstract retrieval capability in this problem allows the causal convex weighting needed for the stipulated anchors and its finite-softmax realization. No particular neural query-key parameterization is imposed.

For ordered coordinates 1,...,D, fix a nonnegative integer support radius b. An admissible local stochastic transport is specified by a kernel P_t(j,k)\geq0 satisfying
\[
\sum_kP_t(j,k)=1,
\qquad P_t(j,k)=0\quad\text{if }|j-k|>b,
\]
and acts by mass pushforward:
\[
(T_tx)_k=\sum_jx_jP_t(j,k).
\]
For unordered supports set \rho_t=0 and take T_t to be the identity.

Assume the following capabilities hold jointly under the fixed conditional law:

1. The causal representation identifies the regime: Z=\psi(h_t) almost surely for a measurable map \psi.
2. There are anchors s_z\in\Delta^{D-1}. For every regime, the memory contains s_z as a successor value, or s_z belongs to the convex hull of its stored successor values. Retrieval can causally select the appropriate anchor s_Z using the allowed convex weights, exactly or through finite-softmax realization.
3. There are regime-specific values \lambda_z\in[0,1], \rho_z\in[0,\rho_{\max}], and admissible T_z such that, almost surely conditional on Z=z and g,
\[
u_z=(1-\rho_z)\bigl[\lambda_zp_t+(1-\lambda_z)s_z\bigr]
+\rho_zT_z\bigl[\lambda_zp_t+(1-\lambda_z)s_z\bigr].
\]
For unordered supports \rho_z=0. The retrieval mechanism, gates, and transport head can jointly implement the regime-dependent choices using the permitted causal information.

## Task

Prove the following integrated theorem. For every aliased summary value satisfying the setup, every fixed-summary forecast has conditional excess risk at least
\[
\mathrm{JS}_\pi^\varepsilon(u_1,...,u_K)
=\sum_z\pi_z\,\mathrm{KL}_\varepsilon(u_z\Vert\bar u),
\qquad
\bar u=\sum_z\pi_z u_z,
\]
and this lower bound is strictly positive when the u_z are not all equal.

Under the stated causal memory and joint realization assumptions, the successor-local class can represent u_Z exactly or as a limit of finite-softmax parameterizations. The exact predictor has zero conditional oracle excess risk; in the finite-softmax case, there is a sequence whose outputs converge almost surely to u_Z and whose conditional oracle excess risks converge to zero.
