# Reference Proof

## Proof Structure

1. Differentiate the softmax-composed model pointwise and identify the Fisher-Rao pullback with correctly typed adjoints.
2. Compute the ambient coefficient contraction as a tensor product of feature outer products.
3. Integrate to obtain the population operator and use the averaged product metric to obtain the empirical operator.
4. Establish consistency of both normal equations and the minimum-norm pseudoinverse formulas, including singular and zero operators.

## Complete Proof

Fix Theta in M. Put A=tau(Theta), s=bar F(Theta), and f_x=G(A)(x). Write E for the ambient coefficient space and B=D tau(Theta):T_Theta M->E, with the ambient interpretation specified in the problem.

### 1. Pointwise differential and Fisher weighting

Let E_x:E->R^{n_0} be the linear contraction E_x[h]=G(h)(x), and put J_x=D sigma(f_x). The chain rule gives

`D bar F_x(Theta)[zeta]=J_x E_x B[zeta]`.

For completeness, if p=sigma(z), direct differentiation yields

`(D sigma(z))_{jk}=p_j(delta_{jk}-p_k)`.

Thus the differential has zero-sum output, as required for the tangent space of the simplex. Its Euclidean matrix is J=diag(p)-pp^T. The pointwise Fisher-Rao bilinear form is therefore

`<D bar F_x[zeta],D bar F_x[xi]>^FR_{s(x)} = (E_x B[zeta])^T C(f_x)(E_x B[xi])`,

where `C(z)=D sigma(z)^T F(sigma(z))D sigma(z)`.

In particular C is symmetric positive semidefinite. An optional simplification is C(z)=diag(p)-pp^T: indeed J diag(1/p)=I-p 1^T and 1^T J=0, so J diag(1/p)J=J. This simplification is not needed for the requested formula.

The transpose in C is Euclidean. The Fisher weighting has already been inserted explicitly; using a Fisher-Rao adjoint here and inserting F again would count the metric twice.

### 2. Tensor-product contraction

Take ambient simple tensors h=h_0 otimes ... otimes h_d and k=k_0 otimes ... otimes k_d. Then

`E_x[h]=h_0 product_{nu=1}^d (Phi_nu(x_nu)^T h_nu)`.

Consequently,

`(E_x[h])^T C(f_x) E_x[k] = (h_0^T C(f_x)k_0) product_{nu=1}^d [h_nu^T Phi_nu(x_nu)Phi_nu(x_nu)^T k_nu]`.

This is exactly the Euclidean pairing of h with

`[C(f_x) otimes Phi_1(x_1)Phi_1(x_1)^T otimes ... otimes Phi_d(x_d)Phi_d(x_d)^T]k`.

Simple tensors span E, so bilinearity proves the ambient operator identity

`E_x^T C(f_x)E_x = C(f_x) otimes Phi_1(x_1)Phi_1(x_1)^T otimes ... otimes Phi_d(x_d)Phi_d(x_d)^T`.

Composing on the right with B and on the left with B^* gives the pointwise operator on T_Theta M. This calculation uses the ambient extension of G and the ambient differential of tau; it does not incorrectly identify an intrinsic adjoint on T_A T with an unrestricted ambient matrix.

### 3. Population and empirical operators

Let L=D bar F(Theta). By the integrated metric definition, for zeta,xi in T_Theta M,

`<L[zeta],L[xi]>_s = int_X <D bar F_x[zeta],D bar F_x[xi]>^FR_{s(x)} mu(dx)`.

Insert the preceding pointwise calculation. The tangent space is finite dimensional. The diagonal quadratic-form integrals are finite by the stated tangent integrability, and the mixed entries are absolutely integrable by Cauchy-Schwarz. Thus the pointwise operators have a well-defined entrywise integral. The identity of bilinear forms identifies its Riesz representative and proves

`Z(Theta)=D bar F(Theta)^*D bar F(Theta) = int_X B^*[C(f_x) otimes Phi_1(x_1)Phi_1(x_1)^T otimes ... otimes Phi_d(x_d)Phi_d(x_d)^T]B mu(dx)`.

For a fixed sample x^1,...,x^m, let L_m=D bar F_m(Theta). The averaged product metric gives

`<L_m[zeta],L_m[xi]>_{m,bar F_m(Theta)} = (1/m)sum_i <D bar F_{x^i}[zeta],D bar F_{x^i}[xi]>^FR_{s(x^i)}`.

Applying the same pointwise calculation yields

`hat Z_m(Theta)=(1/m)sum_i B^*[C(f_{x^i}) otimes Phi_1(x_1^i)Phi_1(x_1^i)^T otimes ... otimes Phi_d(x_d^i)Phi_d(x_d^i)^T]B`.

This is an exact identity for the empirical operator, not an assertion that it equals the population operator. No sampling independence or convergence argument is needed.

### 4. Normal equations and pseudoinverse solutions

Let `b=grad(R o bar F)(Theta)`. The chain rule and the definitions of Riemannian gradient and adjoint give

`b=L^* grad R(s)`.

Since bar F is a submersion onto the output model, L is surjective. Hence a lift of grad R(s) exists. Applying L^* to the lift equation gives

`Z(Theta)[zeta]=b`.

Conversely, if this normal equation holds, then `L^*(L[zeta]-grad R(s))=0`. Surjectivity of L makes L^* injective, so the normal equation describes precisely the source's natural-gradient lifts.

For the empirical equation, define `r_m(q_1,...,q_m)=m^{-1}sum_i ell_i(q_i)` on S^m. The observation-local definition of R_m gives

`R_m o bar F=r_m o bar F_m`.

Therefore `b_m=grad(R_m o bar F)(Theta)=L_m^* grad r_m(bar F_m(Theta))`, where the gradient of r_m uses the averaged product metric. Equivalently, the differential of R_m o bar F vanishes on ker L_m. Thus b_m is orthogonal to ker L_m.

For either operator Q=L^*L or Q=L_m^*L_m, positivity gives

`<Q[v],v>=||L[v]||^2` or `||L_m[v]||^2`, respectively.

It follows that ker Q is the kernel of the corresponding differential. A self-adjoint operator on a finite-dimensional inner-product space has range equal to the orthogonal complement of its kernel. The preceding gradient identities therefore place b in range Z and b_m in range hat Z_m. Both normal equations are consistent, including when their matrices are singular.

To identify the minimum-norm solution explicitly, choose an orthonormal eigenbasis of Q, with eigenvalues lambda_j>=0. Consistency says the coordinates c_j of the right-hand side vanish whenever lambda_j=0. Every solution has coordinate c_j/lambda_j when lambda_j>0 and an arbitrary coordinate when lambda_j=0. Setting the latter coordinates to zero uniquely minimizes the norm. This is precisely Q^+ applied to the right-hand side.

Consequently the natural-gradient equations and their minimum-norm solutions are

`Z(Theta)[zeta]=grad(R o bar F)(Theta)`,

`zeta_min=Z(Theta)^+ grad(R o bar F)(Theta)`,

`hat Z_m(Theta)[zeta_m]=grad(R_m o bar F)(Theta)`,

`(zeta_m)_min=hat Z_m(Theta)^+ grad(R_m o bar F)(Theta)`.

All norms and pseudoinverses here use the Riemannian metric on T_Theta M. If either operator is zero, compatibility forces its right-hand side to be zero and its minimum-norm solution is zero. This also covers the one-class case and samples at which all output differentials vanish.

## Obligation Closure

The chain rule, Fisher weighting, tensor contraction, integral identification, empirical normalization, range compatibility, and minimum-norm claims have all been explicitly derived. Smooth model geometry and submersion are standing assumptions, not consequences asserted for an arbitrary tensor image. No specialized external result or unresolved proof obligation is used.
