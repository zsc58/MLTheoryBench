# Reference Proof

## Proof Structure

1. Check the local domains of the predictive quantities and Gaussian expectations.
2. Differentiate the inverse-based and auxiliary preconditioners, keeping the auxiliary matrix fixed.
3. Match predictive values and differentials, including direct likelihood-hyperparameter dependence.
4. Compare every term in the two objective penalties.
5. Give an admissible example in which the naive objective has a different ordinary gradient.

## Complete Proof

Write A=K_{uu} and K=A+S. Fix an ordinary-parameter point xi_0 and set T_0=K(xi_0)^{-1}. Throughout differentiation, T=T_0 is constant; it is not recomputed as xi varies.

### Domains

A, S, K, and T are positive definite, so all displayed matrix logarithms and inverses exist. The kernel Gram matrix on the inducing inputs and one observation is positive semidefinite. Adding S to its inducing block preserves positive semidefiniteness. Evaluating its quadratic form at (-K^{-1}k_{un},1) gives

sigma_n^2(P_inv)=k_{nn}-k_{nu}K^{-1}k_{un} >= 0.

For symmetric T,

K^{-1}-(2T-TKT)=(T-K^{-1})K(T-K^{-1}),

which is positive semidefinite. Consequently sigma_n^2(P_free)>=sigma_n^2(P_inv)>=0. This identity is used only here in the private domain check, not assumed in the public task.

The naive substitution is also locally meaningful at the matching point. Since S is positive definite, A^{-1}-(A+S)^{-1} is positive definite: conjugating by A^{1/2} reduces this assertion to I-(I+A^{-1/2}SA^{-1/2})^{-1}>0. Thus A(xi)^{-1}-T_0 remains positive definite near xi_0. The kernel Gram inequality gives k_{nn}-k_{nu}A^{-1}k_{un}>=0, and hence k_{nn}-k_{nu}T_0k_{un}>=0 locally. Zero variances are interpreted as point masses. The public local finiteness and relative differentiability conditions make the likelihood chain rule valid at such boundary points as well.

### Preconditioners

Differentiating K K^{-1}=I gives

(dK)K^{-1}+K d(K^{-1})=0,

and therefore

dP_inv=-K^{-1}(dK)K^{-1}.

Because dT=0,

dP_free=d(2T-TKT)=-T(dK)T.

At xi_0 and T=T_0,

P_free=2K^{-1}-K^{-1}KK^{-1}=K^{-1}=P_inv,

and

dP_free=-K^{-1}(dK)K^{-1}=dP_inv.

These identities apply to every allowed variation, including variations of the diagonal entries of S.

### Predictive and likelihood terms

For either preconditioner, product differentiation gives

dmu_n=(dk_{nu})Pm+k_{nu}(dP)m+k_{nu}P(dm),

and

d(sigma_n^2)=dk_{nn}-(dk_{nu})Pk_{un}-k_{nu}(dP)k_{un}-k_{nu}P(dk_{un}).

At the comparison point, both predictive values and both displayed differentials agree.

The expected log-likelihood is F_n(mu_n,sigma_n^2,eta), not merely a function of the first two arguments. Its differential is

dF_n=(partial_a F_n)dmu_n+(partial_v F_n)d(sigma_n^2)+(D_eta F_n)deta.

All coefficients are evaluated at the same (mu_n,sigma_n^2,eta) in the two objectives. The first two differential arguments agree, and the direct eta contribution is identical. Thus every expected-likelihood differential agrees. This is an ordinary finite-dimensional chain rule; no differentiation under an integral is required beyond the explicitly assumed differentiability of F_n.

### Complete penalty terms

Let

B_inv=-tr(P_inv A)+m^T P_inv A P_inv m+log|K|-log|S|,

B_free=-tr(P_free A)+m^T P_free A P_free m+tr(KT)-M-log|T|-log|S|.

The objectives subtract B_inv/2 and B_free/2, respectively. For a common symbolic P,

d[-tr(PA)]=-tr((dP)A+P(dA)),

and

d[m^T P A P m]
 = (dm)^T P A P m
 + m^T(dP)A P m
 + m^T P(dA)P m
 + m^T P A(dP)m
 + m^T P A P(dm).

Every term in these two differential formulas agrees when P and dP agree. The -log|S| term is common, including under the allowed diagonal variations.

For completeness, the determinant polynomial gives det(I+epsilon H)=1+epsilon tr(H)+o(epsilon). Applying this to det(K+epsilon dK)=det(K)det(I+epsilon K^{-1}dK) yields

d log|K|=tr(K^{-1}dK).

On the auxiliary side, T and M are fixed, so

d[tr(KT)-M-log|T|]=tr(T dK).

At T=K^{-1}, these differentials agree. Thus dB_inv=dB_free, and the complete objective differentials agree. Equality for every ordinary-parameter variation proves the claimed equality of gradients in psi, eta, Z, m, and the diagonal coordinates of S.

### Failure of the naive substitution

A nonzero difference in dP alone would not rule out cancellation in the objective. We therefore give an explicit example for the public definition, which replaces every occurrence of P_free by T.

Take D=M=1, the inducing input z=0, and any positive integer N observations with x_n=0 and y_n=0. Use the differentiable kernel k_psi(x,z)=psi exp(-(x-z)^2/2), evaluated at psi=1, and the Gaussian likelihood p(y|t;eta)=N(y;t,eta), evaluated at eta=1. Set m=2 and S=s>0. Vary only s, and evaluate at s=1 with T=1/2 held fixed. Then A=k_{nu}=k_{nn}=1 and K=1+s. All required covariance matrices, likelihood expectations, and derivatives are well-defined.

For the inverse objective put p=(1+s)^{-1}. Its mean and variance are mu=2p and v=1-p. At s=1,

p=1/2, p'=-1/4, mu=1, mu'=-1/2, v=1/2, v'=1/4.

Here F_n(mu,v,1)=-log(2*pi)/2-(mu^2+v)/2, so each expected-likelihood derivative is

-mu mu'-v'/2=3/8.

The inverse penalty is

B_inv/2 = [-p+4p^2+log(1+s)-log s]/2,

whose derivative at s=1 is

[-p'+8pp'+1/(1+s)-1/s]/2=-5/8.

Consequently

partial_s J_inv=(3N+5)/8.

In the naive objective P=T=1/2 is constant, so its predictive mean, predictive variance, trace term, and quadratic mean term are constant under this s variation. Its penalty derivative is

[T-1/s]/2=-1/4.

It follows that

partial_s J_naive=1/4,

and hence

partial_s J_inv-partial_s J_naive=3(N+1)/8>0.

This proves failure in general, without asserting failure for every dataset, parameter point, or direction. The source's narrower interpretation of using T only to precondition the inducing mean also fails in the same example: retaining P_free in the variance and trace gives partial_s J_naive=(1-N)/8, again different from (3N+5)/8. The public task retains its original all-occurrences substitution.

## Closure Note

All theorem-critical obligations are derived above using elementary matrix differentiation and the explicitly stated regularity of F_n. The variational-bound interpretation, natural-gradient update, randomized trace estimators, and stopping theorem are not additional premises needed to compare these explicitly defined objectives. There are no unresolved proof obligations.
