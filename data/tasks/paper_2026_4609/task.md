# Problem

## Setup

Let `A in R^(d_A)` and `B in R^(d_B)` be jointly zero-mean Gaussian, where `d_A,d_B` are positive integers, with nonsingular block covariance

`Sigma=[[Sigma_AA,Sigma_AB],[Sigma_BA,Sigma_BB]]`.

Write `p_AB,p_A,p_B` for their joint and marginal densities. Use natural logarithms and define mutual information by

`I(A;B)=D_KL(p_AB || p_A p_B)`.

For a measurable real-valued critic `T:R^(d_A) x R^(d_B) -> R`, put

`Z_B(a)=integral exp(T(a,b)) p_B(b) db`,

`Z_A(b)=integral exp(T(a,b)) p_A(a) da`.

Call `T` admissible when `E_(p_AB)[|T|]<infinity`, both partition functions are finite and strictly positive marginal-almost everywhere, and

`E_(p_A)[|log Z_B(A)|]<infinity`,

`E_(p_B)[|log Z_A(B)|]<infinity`.

Consider the population variational objective on admissible critics

`L(T)=E_(p_AB)[T]-(1/2)(E_(p_A)[log Z_B(A)]+E_(p_B)[log Z_A(B)])`.

Critics that agree `p_AB`-almost everywhere up to an additive real constant are identified when describing population optimizers.

Let

`C=Sigma_AA^(-1/2) Sigma_AB Sigma_BB^(-1/2)`

have rank `K`, and take its thin singular-value decomposition

`C=U diag(rho_1,...,rho_K) V^T`,

where `U in R^(d_A x K)` and `V in R^(d_B x K)` have orthonormal columns and `0<rho_i<1`. The inverse square roots are the symmetric positive definite ones. For the columns `U_i,V_i`, define

`u_i=U_i^T Sigma_AA^(-1/2) a`,

`v_i=V_i^T Sigma_BB^(-1/2) b`.

For a nonnegative integer `m`, a separable critic with bottleneck width `m` has the form

`T_sep(a,b)=f(a)^T h(b)`,

where `f:R^(d_A)->R^m` and `h:R^(d_B)->R^m` are measurable maps. A separable-augmented critic has the form

`T_aug(a,b)=f(a)^T h(b)+f(a)^T Gamma_A f(a)+h(b)^T Gamma_B h(b)`,

where `Gamma_A,Gamma_B` are symmetric real `m by m` matrices. The case `K=0` is allowed: sums indexed by `1,...,K` are empty, `R^0` is the zero-dimensional vector space, and its dot products and quadratic forms are zero.

## Task

Prove that the admissible population-optimal critics are, up to the almost-everywhere additive-constant equivalence above, represented by

`T*(a,b)=sum_(i=1)^K [rho_i/(1-rho_i^2) u_i v_i-rho_i^2/(2(1-rho_i^2))(u_i^2+v_i^2)]`.

Also prove that:

1. There exist separable encoders with bottleneck width `K+2` whose dot-product critic equals the displayed representative `T*` for every `(a,b)`.
2. There exist separable-augmented encoders with bottleneck width `K` and symmetric coefficient matrices whose critic equals the displayed representative `T*` for every `(a,b)`.
