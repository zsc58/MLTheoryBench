# Reference Proof

## Source Contract and Proof Obligations

The source explicitly defines `W'_s` as an aggregate of marginal Wasserstein distances. It is not Wasserstein distance between joint laws under a product metric. In particular, `W'_s` vanishes between any two couplings of the same endpoint pair. This distinction is essential to the admissibility hypothesis and both stability statements.

The theorem-critical obligations are: finiteness and optimizer well-definedness; the two graph-coupling bounds; normalization by `tau`; normalized value stability; normalized coupling stability with the precise factor `2^(1/r-1/p)`; and substitution of the quantization errors, including infinite-exponent and zero-constant cases. All are derived below. The specialized statements recorded as theory_010 and theory_011 are not treated as independent audited black boxes: their printed versions are proved directly.

## Complete Proof

### 1. Finiteness

Each `nu_i` has finite support, so belongs to `P_p(R^d)`. Let `M_i=max_{a in B_i} ||a||`. Since

`||x-R_i(x)|| <= ||x||+M_i`,

the assumed moment condition makes `e_i` finite when `p<infinity`; bounded support makes it finite when `p=infinity`. Hence `E_p` is finite.

Apply admissibility to the point masses at `(x_0,x_1)` and `(0,0)`. By the definition of the marginal aggregate,

`|h(x_0,x_1)-h(0,0)| <= lambda (||x_0||^p+||x_1||^p)^(1/p)`

for finite `p`, with the maximum replacing the right-hand norm for `p=infinity`. In either case,

`0 <= h(x_0,x_1) <= h(0,0)+lambda(||x_0||+||x_1||)`.

All measures in `P_p(R^d)` have finite first moment, also when `p=infinity`. Thus the cost integral is finite for every coupling of every endpoint pair appearing in the assumptions. No extra integrability assumption is needed.

### 2. Graph Couplings and the Marginal Perturbation

Define

`delta_p = (W_p(mu_0,nu_0)^p + W_p(mu_1,nu_1)^p)^(1/p)`

when `p<infinity`, and

`delta_p = max{W_infinity(mu_0,nu_0),W_infinity(mu_1,nu_1)}`

when `p=infinity`.

For each `i`, consider `eta_i=(id,R_i)#mu_i`. Measurability of `R_i` makes this a well-defined probability measure. Its first marginal is `mu_i`, and its second is `nu_i`. Consequently, for finite `p`,

`W_p(mu_i,nu_i)^p <= integral ||x-R_i(x)||^p dmu_i(x) = e_i^p`.

For `p=infinity`, the same coupling gives

`W_infinity(mu_i,nu_i) <= ess sup_{x~mu_i} ||x-R_i(x)|| = e_i`.

These prove both endpoint conclusions and imply `delta_p<=E_p`.

### 3. Normalization and Optimizer Well-Definedness

Set `g=h/tau` and `A=lambda/tau`, and define

`bar E_g(alpha,beta) = inf_{gamma in Pi(alpha,beta)} [integral g dgamma + KL(gamma || alpha tensor beta)]`.

Since `tau>0`,

`E_tau(alpha,beta)=tau bar E_g(alpha,beta)`,

and the two objectives have exactly the same minimizers. Dividing the admissibility inequality by `tau` shows that `g` has admissibility constant `A`.

Fix any `alpha,beta in P_p(R^d)` and write `Q=alpha tensor beta`. For every `gamma in Pi(alpha,beta)`, the source definition gives `W'_p(gamma,Q)=0`. Admissibility therefore implies

`integral g dgamma = integral g dQ`.

For completeness, relative entropy is nonnegative: when `gamma` has density `f` with respect to `Q`, the pointwise inequality `t log t >= t-1` for `t>=0` gives

`integral f log f dQ >= integral (f-1) dQ = 0`.

The pointwise inequality has equality only at `t=1`, so zero relative entropy implies `gamma=Q`. A measure not absolutely continuous with respect to `Q`, or having infinite entropy, cannot minimize the objective because `Q` has finite cost and zero entropy.

It follows that the normalized objective has the unique optimizer `Q`, and

`bar E_g(alpha,beta)=integral g d(alpha tensor beta)`.

This also establishes existence, uniqueness, and finite optimal values for the original objectives. These facts are derived consequences of the printed admissibility condition, not extra public assumptions.

### 4. Derivation of the Printed Normalized Value-Stability Statement

For any two endpoint pairs `(alpha_0,alpha_1)` and `(beta_0,beta_1)` in `P_p(R^d)`, form their product couplings. Their `W'_p` is exactly the aggregate `delta_p` of their endpoint Wasserstein distances. Applying admissibility to those products and using the preceding value formula yields

`|bar E_g(alpha_0,alpha_1)-bar E_g(beta_0,beta_1)| <= A delta_p`.

This proves the version of theory_010 printed in the supplied source; no unproved external stability theorem is being invoked.

For the endpoint pairs in the task, multiply by `tau` and substitute `A=lambda/tau` and `delta_p<=E_p` to obtain

`|E_tau(mu_0,mu_1)-E_tau(nu_0,nu_1)| <= tau A delta_p = lambda delta_p <= lambda E_p`.

### 5. Derivation of the Printed Normalized Coupling-Stability Statement

For any plans `gamma in Pi(mu_0,mu_1)` and `gamma' in Pi(nu_0,nu_1)`, the definition gives

`W'_r(gamma,gamma') = (W_r(mu_0,nu_0)^r + W_r(mu_1,nu_1)^r)^(1/r)`.

For a probability coupling `eta` and `r<=p<infinity`, the power-mean inequality gives

`(integral ||x-y||^r deta)^(1/r) <= (integral ||x-y||^p deta)^(1/p)`.

For `p=infinity`, the left side is bounded by `ess sup_eta ||x-y||`. Taking infima over the same coupling set proves `W_r<=W_p` for each endpoint, including `p=infinity`.

Put `a_i=W_p(mu_i,nu_i)`. If `p<infinity`, concavity of `t^(r/p)` gives

`a_0^r+a_1^r <= 2^(1-r/p)(a_0^p+a_1^p)^(r/p)`.

Taking the `r`th root therefore yields

`W'_r(gamma,gamma') <= 2^(1/r-1/p) delta_p`.

If `p=infinity`, each endpoint `W_r` is at most `delta_p`, so

`W'_r(gamma,gamma') <= 2^(1/r) delta_p`,

which is the same formula under `1/infinity=0`.

These bounds hold for all such plans, hence in particular for the two optimizers. Adding the nonnegative quantity `kappa(2A delta_p)^(1/(2r))` establishes the printed normalized statement of theory_011:

`W'_r(gamma_{mu_0,mu_1},gamma_{nu_0,nu_1}) <= 2^(1/r-1/p) delta_p + kappa(2A delta_p)^(1/(2r))`.

The transport assumption causes no further obligation under the printed definition: for plans with the same marginals, its left side is zero, and its right side is nonnegative whenever the relative entropy is finite. Infinite-relative-entropy comparisons are vacuous under the stated convention. A proof need not use this redundant assumption nontrivially.

### 6. Final Substitution and Boundary Cases

The normalized and original optimizers agree. Substituting `A=lambda/tau` and using monotonicity of the two nonnegative functions of `delta_p` gives

`W'_r(gamma^tau_{mu_0,mu_1},gamma^tau_{nu_0,nu_1})`

`<= 2^(1/r-1/p) delta_p + kappa(2lambda delta_p/tau)^(1/(2r))`

`<= 2^(1/r-1/p) E_p + kappa(2lambda E_p/tau)^(1/(2r))`.

All quantities in this final expression are finite. The proof covers `lambda=0`, `kappa=0`, and `E_p=0` without division by any of these quantities. The positive exponent `1/(2r)` makes the corresponding zero-power evaluations unambiguous. Both `p=infinity` and `r=p<infinity` were handled explicitly. Nonempty anchors are already required for nearest-anchor maps to exist; zero-mass anchor cells play no role.

Together with the graph-coupling and value bounds, this completes all three claims. There are no unresolved reference-proof obligations. This proof concerns the marginal aggregate defined in the source and does not establish a replacement theorem for product-space Wasserstein distance between joint laws.
