# Reference Proof

## Proof Structure

1. Calculate the conditional Gaussian likelihood ratio and establish uniform second- and absolute third-moment estimates.
2. Aggregate the moment estimates and use the assumed orthogonality.
3. Apply Taylor expansion separately to the product increment and the individual increments, explicitly controlling both generator tails and quadratic tails.
4. Use conditional expectation to identify the local terms with the stated objective.

## Index Scope

Throughout this proof every step index, sum, product, and maximum ranges over I_T={2,...,T}. The Gaussian posterior comparison concerns the nonendpoint reverse steps. This is the source-local endpoint correction: the actual posterior at the first reverse step is a point mass and is not a nonsingular Gaussian member of the family. No endpoint reconstruction term is included or asserted to be negligible. The abstract product-to-sum argument applies to the T-1 retained increments without change.

## Complete Proof

All expectations below, unless a conditioning-pair marginal is explicitly indicated, are under the auxiliary local construction. Its conditioning variables have the forward law specified in the task. The local evaluation variables are the additional variables v_t, not forward-trajectory coordinates. We work for sufficiently large T, which suffices for the asymptotic assertion. The normalization a_T is deterministic and positive.

### 1. Conditional likelihood ratio and uniform moments

Conditional on (y_0,y_t), put
\[
\Delta_t=\Sigma_t^{-1/2}(\widetilde\mu_t-\mu_{\theta,t}),\qquad
m_t=\tfrac12\|\Delta_t\|^2,\qquad
Z_t=\Sigma_t^{-1/2}(v_t-\mu_{\theta,t}).
\]
The conditional law of Z_t is N(0,I). Expanding the two Gaussian densities gives
\[
\log r_t
=-\tfrac12\|Z_t-\Delta_t\|^2+\tfrac12\|Z_t\|^2
=\Delta_t^\top Z_t-\tfrac12\|\Delta_t\|^2.
\]
Consequently, conditional on (y_0,y_t), log r_t has law N(-m_t,2m_t), including the degenerate law at m_t=0. Thus r_t has conditional law U_{m_t}.

Completing the square in the standard normal density gives E exp(bZ)=exp(b^2/2). Hence, for fixed m>=0 and real k,
\[
\mathbb E U_m^k=\exp((k^2-k)m).
\]
In particular,
\[
\mathbb E U_m=1,\qquad
\mathbb E(U_m-1)^2=e^{2m}-1=2m+O(m^2).
\]
For the absolute third moment, compute
\[
\mathbb E(U_m-1)^4=e^{12m}-4e^{6m}+6e^{2m}-3=O(m^2).
\]
The constant and linear Taylor coefficients cancel. The second- and fourth-moment estimates have uniform constants for 0<=m<=1. Cauchy-Schwarz therefore gives
\[
\mathbb E|U_m-1|^3
\leq\bigl(\mathbb E(U_m-1)^2\bigr)^{1/2}
       \bigl(\mathbb E(U_m-1)^4\bigr)^{1/2}
\leq C m^{3/2}.
\]
At m=0, U_0=1 and all these centered moments vanish.

Since c_T->0, eventually every m_t lies in [0,1] almost surely. The constants are independent of t and sufficiently large T. Conditioning gives
\[
\mathbb E[\delta_t\mid y_0,y_t]=0,
\qquad
\mathbb E[\delta_t^2\mid y_0,y_t]=2m_t+O(m_t^2),
\qquad
\mathbb E[|\delta_t|^3\mid y_0,y_t]\leq C m_t^{3/2}.
\]

### 2. Aggregation and orthogonality

Taking expectations and summing over I_T yields
\[
\sum_t\mathbb E\delta_t^2
=2a_T+O\!\left(\sum_t\mathbb E m_t^2\right)
=2a_T+o(a_T),
\qquad
\sum_t\mathbb E|\delta_t|^3
\leq C\sum_t\mathbb E m_t^{3/2}=o(a_T).
\]
The assumed cross-moment equalities imply
\[
\mathbb E S_T^2
=\sum_t\mathbb E\delta_t^2
  +2\sum_{s<t}\mathbb E[\delta_s\delta_t]
=\sum_t\mathbb E\delta_t^2=O(a_T).
\]
No independence assumption is used.

### 3. Taylor expansion with both types of tails

Because G is C^3 near zero and has the stated normalization, choose fixed eta in (0,1) and C_G<infinity such that
\[
|G(x)-x^2/2|\leq C_G|x|^3\qquad (|x|\leq\eta).
\]
For a random variable V taking values in [-1,infinity), splitting into |V|<=eta and |V|>eta gives, whenever the indicated quantities are finite,
\[
\left|\mathbb E G(V)-\tfrac12\mathbb E V^2\right|
\leq C_G\mathbb E|V|^3
+\mathbb E\bigl[|G(V)|\mathbf1_{\{|V|>\eta\}}\bigr]
+\tfrac12\mathbb E\bigl[V^2\mathbf1_{\{|V|>\eta\}}\bigr].
\]
The quadratic-tail term satisfies
\[
\mathbb E\bigl[V^2\mathbf1_{\{|V|>\eta\}}\bigr]
\leq\eta^{-1}\mathbb E|V|^3.
\]
The same split first establishes integrability of G(V) when the second and third moments and the generator-tail expectation are finite. The task's assumptions ensure the needed finiteness for sufficiently large T.

Set X_T=S_T+B_T=R_T-1. Since all r_t are positive, X_T>-1. The assumed third-moment bounds give
\[
\mathbb E|X_T|^3
\leq4\bigl(\mathbb E|S_T|^3+\mathbb E|B_T|^3\bigr)
=o(a_T).
\]
Its second moment is finite by the bounds on S_T and B_T. The truncation inequalities and aggregate generator-tail condition yield
\[
\mathbb E G(X_T)=\tfrac12\mathbb E X_T^2+o(a_T).
\]
Moreover,
\[
\left|\mathbb E X_T^2-\mathbb E S_T^2\right|
\leq2\mathbb E|S_TB_T|+\mathbb E B_T^2=o(a_T).
\]
Consequently,
\[
\mathbb E G(R_T-1)=\tfrac12\mathbb E S_T^2+o(a_T).
\]

Apply the same truncation inequalities to each delta_t and sum over I_T. The summed absolute third moments are o(a_T), and
\[
\sum_t\mathbb E\bigl[\delta_t^2\mathbf1_{\{|\delta_t|>\eta\}}\bigr]
\leq\eta^{-1}\sum_t\mathbb E|\delta_t|^3=o(a_T).
\]
Together with the summed generator-tail condition, this proves
\[
\sum_t\mathbb E G(\delta_t)
=\tfrac12\sum_t\mathbb E\delta_t^2+o(a_T).
\]
Using the quadratic identity from Step 2 gives
\[
\mathbb E G(R_T-1)=\sum_t\mathbb E G(\delta_t)+o(a_T).
\]

### 4. Identification of the local objective

Convexity and G(0)=G'(0)=0 imply G(x)>=0 on [-1,infinity). Thus the defining integrals and conditional expectations are meaningful as nonnegative extended expectations before finiteness is established. The conditional distribution from Step 1 gives
\[
\mathbb E[G(\delta_t)\mid y_0,y_t]=h_G(m_t).
\]
The auxiliary construction retains the forward pair marginals, so the tower property gives
\[
\mathbb E_{\mathrm{loc}}G(\delta_t)
=\mathbb E_{\nu_{T,t}}h_G(m_t).
\]
Step 3 ensures finiteness of the relevant sums for sufficiently large T. Summing over I_T and substituting proves
\[
\mathbb E_{\mathrm{loc}}G(R_T-1)
=\sum_{t\in I_T}\mathbb E_{\nu_{T,t}}h_G(m_t)+o(a_T)
=L_G+o(a_T).
\]
All constants used in the estimates are independent of the timestep and of sufficiently large T. Individual zero mismatches are allowed; positivity is required only of the aggregate normalization a_T.
