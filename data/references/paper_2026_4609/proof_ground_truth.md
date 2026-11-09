# Reference Proof

## Proof Structure

1. Establish the upper bound, attainment, and almost-everywhere optimizer characterization for the symmetrized population variational objective.
2. Compute the Gaussian log density ratio, whiten both views, and use the singular-value decomposition of the whitened cross-covariance to obtain the canonical quadratic expression.
3. Construct explicit separable encoders in dimension `K+2` reproducing the bilinear and both self-quadratic terms.
4. Construct separable-augmented encoders in dimension `K` with correctly scaled quadratic matrices, including the case `K=0`.

## Complete Proof

### 1. Population optimization

Let `P` be the joint law and `Q=P_A tensor P_B`. Positive definiteness of `Sigma` implies that both laws have strictly positive densities everywhere. Let

`ell(a,b)=log[p_AB(a,b)/(p_A(a)p_B(b))]`.

The Gaussian density formula shows that `ell` is a quadratic polynomial plus a finite constant. Hence `E_P[|ell|]<infinity`, and `I(A;B)=E_P[ell]` is finite. Moreover,

`integral exp(ell(a,b)) p_B(b) db=1`

for every `a`, and the analogous identity holds with the two views exchanged. Thus `ell+c` is admissible for every finite real constant `c`.

For an arbitrary admissible critic `T`, define `Z_B(a)` and `Z_A(b)` as in the task. For marginal-almost every `a`, the function

`r_T(b|a)=exp(T(a,b)) p_B(b)/Z_B(a)`

is a probability density. Its conditional relative entropy satisfies

`D_KL(p_(B|A=a) || r_T(.|a))`

`=E_(B|A=a)[ell(a,B)-T(a,B)+log Z_B(a)]`.

The integrability assumptions and `E_P[|ell|]<infinity` justify averaging this identity. It gives

`G_A := E_A[D_KL(p_(B|A) || r_T(.|A))]`

`=I(A;B)-E_P[T]+E_A[log Z_B(A)] >= 0`.

Define similarly

`s_T(a|b)=exp(T(a,b)) p_A(a)/Z_A(b)`.

Then

`G_B := E_B[D_KL(p_(A|B) || s_T(.|B))]`

`=I(A;B)-E_P[T]+E_B[log Z_A(B)] >= 0`.

Here nonnegativity and its equality condition follow directly from `x-1-log x >= 0`: for positive probability densities `p,r`, integration of this inequality with `x=r/p` gives `D_KL(p||r)>=0`, with equality precisely when `p=r` almost everywhere.

Consequently,

`I(A;B)-L(T)=(G_A+G_B)/2 >= 0`.

For `T=ell+c`, both partition functions equal `exp(c)`, so `L(ell+c)=I(A;B)`. Thus the maximum is attained.

If `T` attains this maximum, both nonnegative gaps vanish. Equality of the conditional densities yields

`T(a,b)-ell(a,b)=log Z_B(a)=log Z_A(b)`

for `P`-almost every `(a,b)`. Because `P` and `Q` have strictly positive densities, this also holds `Q`-almost everywhere. A function of `a` equal to a function of `b` almost everywhere under a product probability measure must be constant almost everywhere: by Fubini, choose one `b` whose section has full `P_A` measure to show the function of `a` is constant, and then apply Fubini again to the other sections. Therefore `T=ell+c` almost everywhere for a finite real constant `c`. This proves the optimizer characterization.

### 2. Gaussian and canonical forms

Writing `z=(a,b)`, substitution of the Gaussian densities gives

`ell(a,b)=c_0 + (1/2)a^T Sigma_AA^(-1)a + (1/2)b^T Sigma_BB^(-1)b - (1/2)z^T Sigma^(-1)z`,

where

`c_0=(1/2)log[(det Sigma_AA)(det Sigma_BB)/(det Sigma)]`.

Whiten the two views. Their joint covariance becomes

`[[I,C],[C^T,I]]`.

Complete the columns of the thin SVD matrices `U,V` to orthonormal bases of their respective ambient spaces. Rotating the whitened views into these bases gives, after reordering coordinates, the covariance blocks

`[[1,rho_i],[rho_i,1]]`, for `i=1,...,K`,

and an identity block on the remaining coordinates. Indeed, each marginal covariance is the identity and the cross-covariance has only the displayed diagonal singular values. Positive definiteness implies `1-rho_i>0`; the active singular values are positive by their definition. Thus `0<rho_i<1`.

The transformed Gaussian density factors over these blocks. The residual coordinates have the same independent standard Gaussian density under `P` and `Q`, so their factors cancel in the density ratio. Each correlated block has inverse

`(1-rho_i^2)^(-1) [[1,-rho_i],[-rho_i,1]]`.

Subtracting its joint quadratic exponent from the two marginal quadratic exponents gives

`-(u_i^2-2rho_i u_i v_i+v_i^2)/(2(1-rho_i^2))+(u_i^2+v_i^2)/2`

`=alpha_i u_i v_i+beta_i(u_i^2+v_i^2)`,

where

`alpha_i=rho_i/(1-rho_i^2)`,

`beta_i=-rho_i^2/(2(1-rho_i^2))`.

Hence, for the representative displayed in the task,

`T*(a,b)=sum_(i=1)^K [alpha_i u_i v_i+beta_i(u_i^2+v_i^2)]`,

we have `ell=T*+c_0`. Since an additive constant preserves admissibility and the objective value, `T*` is admissible and optimal. The preceding characterization shows that every optimizer equals `T*` plus a constant almost everywhere.

### 3. Separable representation

For `K>0`, define the measurable polynomial encoders

`f(a)=(sqrt(alpha_1)u_1,...,sqrt(alpha_K)u_K, sum_i beta_i u_i^2, 1)`,

`h(b)=(sqrt(alpha_1)v_1,...,sqrt(alpha_K)v_K, 1, sum_i beta_i v_i^2)`.

They take values in `R^(K+2)`. Their dot product is

`f(a)^T h(b)=sum_i alpha_i u_i v_i+sum_i beta_i u_i^2+sum_i beta_i v_i^2=T*(a,b)`

for every `(a,b)`. In particular, the resulting critic is admissible because it equals `T*`.

### 4. Separable-augmented representation

For `K>0`, set

`f_0(a)=(sqrt(alpha_i)u_i)_(i=1)^K`,

`h_0(b)=(sqrt(alpha_i)v_i)_(i=1)^K`,

and choose the symmetric matrices

`Gamma_A=Gamma_B=diag(beta_i/alpha_i)=diag(-rho_i/2)`.

Then

`f_0(a)^T h_0(b)=sum_i alpha_i u_i v_i`,

`f_0(a)^T Gamma_A f_0(a)=sum_i beta_i u_i^2`,

`h_0(b)^T Gamma_B h_0(b)=sum_i beta_i v_i^2`.

Adding the three identities gives `T*` pointwise. The division by `alpha_i` is legitimate because only nonzero singular values are indexed. The resulting critic is again admissible.

### 5. Zero rank

If `K=0`, the cross-covariance is zero and the Gaussian joint density factors into its marginals. Thus `ell=0`, `I(A;B)=0`, and `T*=0`. For the width-two separable representation take `f(a)=(0,1)` and `h(b)=(1,0)`. For the width-zero augmented representation take the unique maps into `R^0` and the empty `0 by 0` coefficient matrices. Both critics are identically zero. This also agrees with the empty-sum versions of the constructions above.

All claims concern existence at the stated widths; no claim of minimality of either width is required.
