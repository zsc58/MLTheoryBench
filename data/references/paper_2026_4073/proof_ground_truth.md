# Reference Proof

## Proof Structure

For a finite test sequence, derive the one-record posterior updates and verify that the two Gaussian laws have the same affine support. Apply the correctly oriented Gaussian Rényi formula. A common-core covariance sandwich and a rank-two perturbation bound control the determinant contribution; an RKHS projection argument controls the mean contribution. Finally, establish directly that a uniform finite-evaluation Rényi bound extends to the canonical cylinder sigma-algebra.

## Complete Proof

Fix an ordered neighboring pair D,D', their common core D_-, and a finite test sequence T. Write the differing records as (z,y) and (z',y'). Set

C=k_{D_-}(T,T), c=k_{D_-}(T,z), c'=k_{D_-}(T,z'), v=k_{D_-}(z,z), v'=k_{D_-}(z',z'),

and let u=mu_D(T), u'=mu_D'(T), K=k_D(T,T), and K'=k_D'(T,T). Throughout, V=V_n(r), Delta=Delta_n(r), and tau=V/r^2.

### 1. Posterior updates and support

To obtain the updates, write the regularized training Gram matrix after appending (z,y) in block form as [[A,b],[b^T,d]], where A=K(X_-,X_-)+r^2 I, b=k(X_-,z), and d=k(z,z)+r^2. Its Schur complement is s=d-b^T A^(-1)b=v+r^2>0. Its inverse has blocks A^(-1)+A^(-1)bb^T A^(-1)/s, -A^(-1)b/s, and 1/s. Substitution in the posterior formulas gives

mu_D=mu_{D_-}+eta k_{D_-}(.,z), eta=(y-mu_{D_-}(z))/(v+r^2),

K=C-cc^T/(v+r^2).

The same calculation gives mu_D'=mu_{D_-}+eta' k_{D_-}(.,z') and K'=C-c'c'^T/(v'+r^2). These formulas also hold for an empty core using the stated conventions. In particular,

g:=mu_D-mu_D'=eta k_{D_-}(.,z)-eta' k_{D_-}(.,z') belongs to H_-.

Positive semidefiniteness of the common-core block covariance [[C,c],[c^T,v]] implies

(a^T c)^2 <= v a^T C a

for every a, by considering its quadratic form on (a,t). This includes v=0, in which case c=0. Thus cc^T<=vC. Also, every a in ker(C) is orthogonal to c, so c belongs to range(C). The same statements hold for c'. Consequently u-u'=eta c-eta'c' belongs to range(C).

### 2. Covariance sandwich and admissibility

The updates imply

r^2 C/(v+r^2)<=K<=C, and r^2 C/(v'+r^2)<=K'<=C.

Since v,v'<=V, put b=r^2/(V+r^2)>0. Then bC<=K,K'<=C. Hence K and K' have the same nullspace as C. For

K_alpha=alpha K'+(1-alpha)K,

we have

K_alpha >= gamma C, gamma=[r^2-(alpha-1)V]/[V+r^2]>0.

K_alpha annihilates ker(C), so its range is also range(C). Both Gaussian evaluation laws therefore have the same affine support u'+range(C), because u-u' belongs to that range. On this range all three covariance matrices are positive definite. If the range has dimension zero, the two laws are the same point mass and their divergence is zero. Otherwise all subsequent inverses and determinants are taken on this range.

### 3. Gaussian Rényi formula

For clarity, the determinant term has the following orientation:

D_alpha(N(u,sigma^2 K)||N(u',sigma^2 K'))
= -[2(alpha-1)]^(-1) log{det(K_alpha)/[det(K)^(1-alpha) det(K')^alpha]}
  + alpha(u-u')^T K_alpha^(-1)(u-u')/(2sigma^2).

Here is a direct verification. Translate and apply sigma^(-1)K'^(-1/2) on the common affine support. The second law becomes N(0,I), and the first becomes N(d,R), where d=sigma^(-1)K'^(-1/2)(u-u') and R=K'^(-1/2)KK'^(-1/2). Define B=alpha I-(alpha-1)R. The quadratic precision in p^alpha q^(1-alpha) is A=alpha R^(-1)-(alpha-1)I=R^(-1)B, which is positive definite. Completing the square in the Gaussian integral gives

integral p^alpha q^(1-alpha)
= det(R)^(-(alpha-1)/2) det(B)^(-1/2)
  times exp{alpha(alpha-1)d^T B^(-1)d/2}.

Indeed the determinant factor follows from det(A)=det(R)^(-1)det(B), and the exponent follows from

-alpha d^T R^(-1)d/2 + alpha^2 d^T R^(-1)A^(-1)R^(-1)d/2
= alpha(alpha-1)d^T B^(-1)d/2.

Taking the logarithm and dividing by alpha-1 proves the formula, using K_alpha=K'^(1/2) B K'^(1/2). This also verifies all hypotheses needed for its use here.

### 4. Determinant contribution

The sandwich implies bK'<=K<=b^(-1)K'. Thus the eigenvalues lambda_j of R lie in [1/(1+tau),1+tau]. Moreover,

K-K'=c'c'^T/(v'+r^2)-cc^T/(v+r^2),

so rank(R-I)<=2. At most two eigenvalues differ from one. The determinant contribution is therefore

sum_j phi_alpha(lambda_j),

where

phi_alpha(lambda)=-log(lambda)/2-log(alpha-(alpha-1)lambda)/[2(alpha-1)].

The logarithms are defined throughout the interval because (alpha-1)tau<1. Also phi_alpha(1)=0 and

phi_alpha''(lambda)=1/(2lambda^2)+(alpha-1)/[2(alpha-(alpha-1)lambda)^2]>0.

Its maximum on the interval occurs at an endpoint. Substitution gives precisely the two expressions defining psi_alpha(tau) in the task. Since the interval contains one, this maximum is nonnegative. At most two summands are nonzero, and the determinant contribution is at most 2psi_alpha(tau).

### 5. RKHS and mean contribution

Let S_T be the span in H_- of the sections k_{D_-}(.,t) for entries t of T. Write delta=g(T)=u-u'. The reproducing property shows delta belongs to range(C): if a is in ker(C), the section combination with coefficients a has squared norm a^T C a=0, and hence a^T delta=0.

Set beta=C^dagger delta and h=sum_i beta_i k_{D_-}(.,t_i). Then h(T)=C beta=delta. Thus g-h is orthogonal to every section in S_T, making h the orthogonal projection of g onto S_T. It follows that

delta^T C^dagger delta=||h||_{H_-}^2<=||g||_{H_-}^2<=Delta^2.

This proof permits repeated test points and singular C. It also shows equality when T includes the differing inputs, since then g belongs to S_T.

Inverting K_alpha>=gamma C on their common range gives

delta^T K_alpha^dagger delta <= gamma^(-1)delta^T C^dagger delta
<= [V+r^2]Delta^2/[r^2-(alpha-1)V].

Combining this with the determinant bound proves, uniformly in the ordered neighboring pair and T,

D_alpha(P_T||Q_T)<=2psi_alpha(V/r^2)
+ [alpha/2][V+r^2]/[r^2-(alpha-1)V](Delta/sigma)^2
=epsilon_alpha.

If V=0, every common-core covariance C is zero, the update sections vanish, and g=0 for every neighboring pair. Thus Delta=0, the evaluation laws agree, and the bound is zero for every alpha>1. The empty test sequence also gives divergence zero.

### 6. Lifting to the canonical cylinder sigma-algebra

We prove the required Rényi lifting rather than infer it from an approximate-DP characterization. Let P,Q be the two path laws, let a=alpha, q=a/(a-1), and M=exp((a-1)epsilon_alpha). The finite-dimensional result implies, by Hölder's inequality, that for every bounded nonnegative function h depending measurably on finitely many evaluations,

E_P h <= M^(1/a)(E_Q h^q)^(1/q).

The algebra of finite-coordinate cylinder events generates the canonical cylinder sigma-algebra. For the finite measure P+Q, every event in this sigma-algebra can be approximated in symmetric-difference measure by events of that algebra. To verify this assertion, the class of approximable events contains the algebra, is closed under complements and finite unions, and is closed under countable unions by first truncating the union and using continuity from below of a finite measure. It is therefore the whole generated sigma-algebra.

Approximating the level sets of bounded nonnegative simple functions, and then approximating a bounded nonnegative measurable h by simple functions, gives uniformly bounded nonnegative finite-coordinate simple functions converging to h in (P+Q)-measure. Each such function depends on finitely many coordinates, by taking the union of its finitely many coordinate sets. Boundedness implies convergence of the relevant integrals, so the displayed Hölder inequality holds for every bounded nonnegative cylinder-measurable h.

Applying it to an indicator of a Q-null event proves P<<Q. Let w=dP/dQ. For N>0 use h=min(w,N)^(a-1) and put A_N=E_Q min(w,N)^a. Then

A_N <= E_Q[w min(w,N)^(a-1)] <= M^(1/a) A_N^((a-1)/a).

Thus A_N<=M, also when A_N=0. Monotone convergence gives E_Q w^a<=M, proving D_a(P||Q)<=epsilon_alpha.

Conversely, a path-law Rényi bound implies the same bound for every finite evaluation: the marginal likelihood ratio is the conditional expectation of w given those evaluations, and Jensen's inequality bounds its a-th moment by E_Q w^a. This proves the asserted equivalence. Uniformity over ordered neighboring pairs establishes the claimed RDP guarantee.

## Obligation Closure

The posterior updates are derived by a Schur complement; support compatibility is verified explicitly; the Gaussian formula is derived by integration; the rank-two and endpoint bounds are established; the RKHS inequality is proved by orthogonal projection; and the path-valued Rényi extension is proved on the cylinder sigma-algebra. No theorem-critical obligation remains unresolved.
