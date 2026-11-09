# Reference Proof

## Contract and proof obligations

All current scale parameters are finite and positive. The design and observed response are arbitrary; no rank or nonzero-coordinate assumption is imposed. The updates are exact, undamped, and unclipped. Every quantity on an update's right-hand side is evaluated at the common old iterate. Stationarity refers only to the positive parameter domain.

The obligations are: (step_001) derive the posterior and matrix identities; (step_002) derive and globally minimize the EM scale objective; (step_003) derive the evidence stationarity equations; (step_004) establish the domain and fixed-point meaning of MacKay's quotient and distinguish its numerical map; and (step_005) construct a tight joint-scale Fenchel majorization, derive its ridge and scale steps, and verify boundary cases. Each is closed below without invoking a specialized external optimization theorem.

## step_001: Posterior and matrix identities

Write H=A+Z^T B^{-1}Z and S=H^{-1}. Since A and B are positive definite, so are H, S, C=B+ZA^{-1}Z^T, and P=C^{-1}. The complete-data negative log density, apart from constants and a factor 1/2, is

-log|A|+log|B|+w^T A w+(y-Zw)^T B^{-1}(y-Zw).

Completing the square in w gives posterior N(m,S), with m=SZ^T B^{-1}y. In particular all posterior second moments are finite.

Direct multiplication verifies

P=B^{-1}-B^{-1}ZSZ^T B^{-1},

S=A^{-1}-A^{-1}Z^T PZA^{-1}.

The posterior normal equation Hm=Z^T B^{-1}y gives Am=Z^T B^{-1}(y-Zm). Consequently

Py=B^{-1}(y-Zm),   Z^T Py=Am,

PZ=B^{-1}ZSA,

u_j^T Pu_j=alpha_j(1-alpha_j S_jj),

P_ii=beta_i^{-1}-beta_i^{-2}z_i^T Sz_i.

For example, the last two scalar identities follow by taking the relevant diagonal entries of the two inverse identities. The identity for PZ follows by factoring B^{-1}Z[I-SZ^T B^{-1}Z] and using SH=I.

Evaluating the determinant of the block matrix with blocks A, Z^T, -Z, B by its two Schur complements gives |A||C|=|B||H|. Thus

log|C|=log|H|-log|A|+log|B|.

Woodbury also gives

y^T Py=y^T B^{-1}y-(Z^T B^{-1}y)^T S(Z^T B^{-1}y).

It follows from Gaussian marginalization that L=1/2(log|C|+y^T Py), up to n/2 log(2pi). This is the density of y, not the density of the parameter-dependent projection Z^T B^{-1}y. Dropping the common factor 1/2 is a positive rescaling, not an additive-constant adjustment.

## step_002: Exact EM

Temporarily let all unmarked posterior quantities be computed at the fixed old iterate. Under its posterior,

E(w_j^2|y)=m_j^2+S_jj=:a_j,

E((y_i-z_i^T w)^2|y)=(y_i-z_i^T m)^2+z_i^T Sz_i=:b_i.

These follow by expanding around the posterior mean; the centered cross terms have expectation zero. We have a_j>0 because S_jj>0, and b_i>=0.

For candidate new parameters alpha',beta', twice the expected negative complete-data log likelihood, up to constants independent of these candidate parameters, is

sum_j[-log alpha'_j+alpha'_j a_j]+sum_i[log beta'_i+b_i/beta'_i].

The derivative of -log a+a a_j with respect to a>0 is -1/a+a_j and its second derivative is 1/a^2>0. Its unique global minimizer is a=1/a_j. For b_i>0, the derivative of log b+b_i/b is (b-b_i)/b^2, negative below b_i and positive above it. Its unique global minimizer is b=b_i. Therefore

alpha_j^{new}=1/(m_j^2+S_jj),

beta_i^{new}=r_i^2+z_i^T Sz_i.

If b_i=0, the coordinate objective is log b, which tends to minus infinity as b decreases to zero. There is no positive minimizer; the stated update is a boundary-limit convention. It does not authorize evaluating the positive-definite posterior formulas at a singular B.

## step_003: Evidence stationarity

Differentiating CP=I gives dP=-P(dC)P. Also d log|C|=tr(P dC), as follows by expanding det(C+epsilon D)=det(C)det(I+epsilon P D) to first order.

For a feature precision,

dC/dalpha_j=-alpha_j^{-2}u_j u_j^T,

dP/dalpha_j=+alpha_j^{-2}P u_j u_j^T P.

The plus sign in the second formula is essential. Hence

2 dL/dalpha_j=alpha_j^{-2}[(u_j^T Py)^2-u_j^T Pu_j]

=m_j^2+S_jj-alpha_j^{-1}.

For a noise variance, dC/dbeta_i=e_i e_i^T, so

2 dL/dbeta_i=P_ii-((Py)_i)^2

=beta_i^{-1}-beta_i^{-2}(z_i^T Sz_i+r_i^2).

Because the domain is open and all scale parameters are positive, the gradient vanishes exactly when

alpha_j(m_j^2+S_jj)=1 for every j,

beta_i=r_i^2+z_i^T Sz_i for every i.

No existence of an interior stationary point is asserted. These equations are also exactly the fixed-point equations of the EM moment map wherever it returns positive scales.

## step_004: MacKay representation and its domain

For m_j!=0, the feature stationarity equation rearranges to

alpha_j=(1-alpha_j S_jj)/m_j^2.

Evaluating the right-hand side at the old iterate defines the MacKay map. Its numerator is u_j^T Pu_j/alpha_j. If m_j!=0, the identity u_j^T Py=alpha_j m_j implies u_j!=0, so positive definiteness of P makes this numerator positive.

To compare numerical updates, put M=m_j^2>0 and v=S_jj>0. The difference between MacKay and EM is

(1-alpha_j v)/M-1/(M+v)

=v[1-alpha_j(M+v)]/[M(M+v)].

Thus the two coordinate updates agree exactly when the old coordinate satisfies its stationarity equation. They do not generally agree otherwise. For n=d=1, Z=[1], y=[1], and alpha=beta=1, we have S=1/2 and m=1/2. EM gives alpha^{new}=4/3, whereas MacKay gives alpha^{new}=2.

The domain restriction cannot be discarded. If m_j=0, the original stationarity equation remains meaningful but the quotient does not. At a stationary coordinate with m_j=0, the identity u_j^T Pu_j=alpha_j(1-alpha_j S_jj) forces u_j=0. Conversely, a zero feature column gives m_j=0, S_jj=1/alpha_j, and evidence independent of that alpha_j. The EM map fixes this coordinate, while the displayed MacKay quotient is 0/0. Equivalence of the quotient and stationarity is therefore asserted only on its stated domain.

The chosen noise fixed-point representation is already the EM moment equation.

## step_005: Joint-scale Fenchel MM

First establish the quadratic augmentation rather than equating L with an expression containing an arbitrary free w. Completing the square as above gives, for every positive A,B,

(y-Zw)^T B^{-1}(y-Zw)+w^T A w

=y^T Py+(w-m)^T H(w-m).

Consequently, defining

F(w,A,B)=(y-Zw)^T B^{-1}(y-Zw)+w^T A w-log|A|+log|B|+log|H|,

we have min_w F(w,A,B)=2L(A,B), attained at w=m.

Fix the old iterate and write H_0=A_0+Z^T B_0^{-1}Z and S_0=H_0^{-1}. For any positive definite H,

log|H|<=log|H_0|+tr(S_0(H-H_0)).

For completeness, let the positive eigenvalues of H_0^{-1/2}H H_0^{-1/2} be t_k. Subtracting log|H_0| reduces the inequality to sum_k log t_k<=sum_k(t_k-1). The scalar inequality follows because t-1-log t has derivative 1-1/t and its minimum is zero at t=1. Equality in the matrix inequality holds when H=H_0. Equivalently this is the Fenchel bound log|H|<=tr(S_0 H)-log|S_0|-d.

Replace only log|H| in F by this tangent, obtaining U_0(w,A,B). Then

2L(A,B)<=F(w,A,B)<=U_0(w,A,B).

At (w,A,B)=(m_0,A_0,B_0), both inequalities are equalities. Thus fixing w=m_0 after the ridge step gives a genuine tight majorizer of 2L in the scales.

At the old scales, the w-dependent part of U_0 is

(y-Zw)^T B_0^{-1}(y-Zw)+w^T A_0 w.

Its Hessian is 2H_0, not S_0. Its unique minimizer is w=m_0.

Now hold this w and S_0 fixed while minimizing over candidate new scales. Since

tr(S_0 H)=sum_j alpha_j(S_0)_jj+sum_i beta_i^{-1}z_i^T S_0 z_i,

the scale terms of U_0, up to a constant independent of the candidate scales, are

sum_j[-log alpha_j+alpha_j((m_0)_j^2+(S_0)_jj)]

+sum_i[log beta_i+((y_i-z_i^T m_0)^2+z_i^T S_0 z_i)/beta_i].

These are precisely the scale functions minimized in step_002. Therefore the specified l2-IRLS-MM iteration gives the same finite-iterate moment maps as exact EM. This proof does not regard a gamma-only conjugate as constant while varying beta; it retains the full joint dependence through H.

The source algorithm's alternative forms follow immediately from the inverse identities:

m_0=A_0^{-1}Z^T P_0 y,

(S_0)_jj=(alpha_j^0)^{-1}-(alpha_j^0)^{-2}u_j^T P_0u_j,

z_i^T S_0z_i=beta_i^0-(beta_i^0)^2(P_0)_ii.

Thus this MM construction reproduces the exact source iteration, rather than introducing a different algorithm.

Finally, since S_0 is positive definite, the noise numerator vanishes exactly when z_i=0 and y_i=0. For every other row-response pair it is strictly positive. In the zero case the common scale objective tends to minus infinity as beta_i decreases to zero, giving exactly the public boundary convention. Zero feature columns cause no problem for either EM or MM because their feature second moments remain positive. No rank restriction on Z is needed.

## Source-repair and dependency notes

The proof retains the Gaussian one-half normalization, corrects the sign and rank-one product in the precision derivative, consistently minimizes the negative EM auxiliary function, and uses a minimization identity for the free-weight augmentation. The missing heteroscedastic MM derivation is supplied by the same matrix Fenchel identity already stated in the source. Specialized external convergence analyses are not used; there are no unresolved theorem-critical proof obligations.
