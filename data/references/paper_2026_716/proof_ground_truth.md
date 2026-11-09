# Reference Proof

## Proof Structure

1. Use the transient block and one-step absorption vector to obtain the first-entry distribution and normalization.
2. Sum convergent matrix-power series to obtain the generating function and fundamental-matrix moments.
3. Differentiate the log-linear transition kernel, matrix powers, and resolvents to obtain all parameter sensitivities.

## Complete Proof

All graph data, the absorbing set, the starting vertex, and the generating-function argument are fixed under parameter differentiation. Write `1_S=1_{S_y}` and `1_A=1_{A_y}`.

### First-entry law and absorption

Fix `q in S_y`. For absorption at time `t>=1`, the first `t-1` transitions must end in `S_y`, and the next transition must enter `A_y`. Summing over all intermediate transient vertices and the final absorbing vertex gives

`p_theta(t | q)=e_q^T M^(t-1)R`.

For `t=1`, the transient product is `M^0=I`. This argument uses the transition rows before stopping, so it is unchanged if the rows on `A_y` are replaced by absorbing rows.

Row stochasticity on `S_y` gives

`M1_S+R=1_S`, hence `R=(I-M)1_S`.

The standard finite-dimensional Neumann-series result states that if `rho(B)<1`, then `sum_{k>=0}B^k` converges absolutely to `(I-B)^(-1)`. Its hypothesis holds for `B=M`. Therefore

`Z=(I-M)^(-1)=sum_{k>=0}M^k`,

and

`sum_{t>=1}p_theta(t|q)=e_q^T ZR=e_q^T1_S=1`.

Thus absorption occurs almost surely.

### Generating function and moments

For a finite complex scalar `z` satisfying `|z|rho(M)<1`, the same result applies to `B=zM`, since `rho(zM)=|z|rho(M)`. Consequently

`G_q(z)=sum_{t>=1}z^t p_theta(t|q)=z e_q^T(I-zM)^(-1)R`.

This statement also covers `z=0` and `rho(M)=0`; it does not require division by the spectral radius.

To justify the moment sums, choose any real `r` with `rho(M)<r<1`. Finite-dimensional matrix-power estimates give a constant `C` such that `||M^k||<=Cr^k` for all `k>=0`: in Jordan form the powers have polynomial factors times eigenvalue powers, which are bounded by a constant times `r^k`; nilpotent blocks vanish after finitely many powers. Hence the matrix series with coefficients `(k+1)` and `(k+1)^2` converge absolutely, and the first two hitting-time moments are finite.

Cauchy products of the absolutely convergent Neumann series give

`Z^2=sum_{k>=0}(k+1)M^k`,

because there are `k+1` pairs of nonnegative indices with sum `k`, and

`Z^3=sum_{k>=0}((k+1)(k+2)/2)M^k`,

because that is the number of triples with sum `k`. Subtracting coefficients yields

`sum_{k>=0}(k+1)^2 M^k=2Z^3-Z^2`.

It follows that

`mu_q=E_theta[T_y|q]=e_q^T Z^2R=e_q^T Z1_S`,

and

`m2_q=E_theta[T_y^2|q]=e_q^T(2Z^3-Z^2)R=e_q^T(2Z^2-Z)1_S`.

Here we used `ZR=1_S`. Therefore

`Var_theta(T_y|q)=m2_q-mu_q^2=e_q^T(2Z-I)Z1_S-(e_q^T Z1_S)^2`.

The source's main-text series with coefficients `(k+1)(k+2)` instead computes `E[T_y(T_y+1)|q]`; subtracting the first-moment series gives the second-moment expression above, as in the source appendix. This local correction does not change the requested variance.

### Kernel and block derivatives

For an edge `(i,j)`, differentiation gives

`partial_a A_ij=A_ij phi_ij,a`,

and

`partial_a D_ii=sum_{k:(i,k) in E}A_ik phi_ik,a`.

The quotient rule for `P_ij=A_ij/D_ii` therefore gives

`partial_a P_ij=P_ij[phi_ij,a-sum_{k:(i,k) in E}P_ik phi_ik,a]`.

The degree denominator is positive because the graph is connected, has at least two vertices, and has positive edge weights. Every nonedge transition, including each diagonal entry, is identically zero, so its derivative is zero. Thus

`(M_a)_ij=partial_a P_ij` for `i,j in S_y`,

and

`(R_a)_i=sum_{j in A_y}partial_a P_ij` for `i in S_y`,

with nonedge terms interpreted as zero. Differentiating the row-sum identity also gives `R_a=-M_a1_S`.

### Probability and generating-function sensitivities

Repeated use of the finite product rule gives, for `t>=2`,

`partial_a M^(t-1)=sum_{r=0}^{t-2}M^rM_aM^(t-2-r)`.

For `t=1`, the derivative of `M^0=I` is zero, represented by the empty sum. Differentiating the pmf gives

`partial_a p_theta(t|q)=e_q^T[(partial_a M^(t-1))R+M^(t-1)R_a]`.

All kernel entries are smooth functions of the ambient parameter on `R^d`. At any evaluation parameter satisfying the stated spectral-radius inequalities, those inequalities remain strict in a neighborhood by continuity of spectral radius. Thus, for fixed `z`, the generating-function identity holds on a neighborhood and can be differentiated there, even if `Theta` itself has a boundary or is not open. No differentiation through an infinite probability sum is needed.

For `W(z)=(I-zM)^(-1)`, differentiate `(I-zM)W(z)=I` and multiply on the left by `W(z)` to obtain

`partial_a W(z)=zW(z)M_aW(z)`.

It follows that

`partial_a G_q(z)=z e_q^T[zW(z)M_aW(z)R+W(z)R_a]`.

### Moment sensitivities

At `z=1`, the same inverse differentiation gives

`partial_a Z=ZM_aZ`.

The first and second moments have already been identified with smooth finite matrix expressions. Differentiating those expressions, without interchanging derivatives and infinite expectations, yields

`partial_a E[T_y|q]=e_q^T(partial_a Z)1_S`,

`partial_a E[T_y^2|q]=e_q^T[2((partial_a Z)Z+Z(partial_a Z))-partial_a Z]1_S`,

and

`partial_a Var(T_y|q)=partial_a E[T_y^2|q]-2 E[T_y|q] partial_a E[T_y|q]`.

These arguments cover deterministic one-step absorption, zero individual absorption probabilities, periodic walks, and zero spectral radius. No division by an individual hitting probability or absorption-vector entry occurs. The standing identifiability assumption is part of the source contract but is not needed in these algebraic derivations. All requested obligations are closed.
