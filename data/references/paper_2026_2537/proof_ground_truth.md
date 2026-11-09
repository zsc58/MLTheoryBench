# Reference Proof

## Proof Structure

1. Derive the multilabel variance identity and residual properties.
2. Prove the uniform-cardinality common optimizer using simultaneous spectral analysis and the stated ordering hypotheses.
3. Analyze the variable-cardinality trace-difference optimizer, give a valid optimizer-mismatch witness, and compare eigenspaces by a PSD-specialized Davis--Kahan argument.
4. Establish the residual norm estimate.

## Complete Proof

Let z_i = x_i - mu. For each label ell, the usual centered variance decomposition gives

    sum_{i: ell in L_i} (x_i-mu)(x_i-mu)^T
    = sum_{i: ell in L_i} (x_i-mu_ell)(x_i-mu_ell)^T
      + n_ell (mu_ell-mu)(mu_ell-mu)^T.

Summing over the finite label set, each sample i is counted k_i times, so

    T_ml = B + U = sum_i k_i z_i z_i^T.

Hence

    R := T_ml - T = sum_i (k_i-1) z_i z_i^T >= 0.

Because all summands are positive semidefinite, R=0 exactly when (k_i-1)z_i=0 for every i. Also B>=0 and U>=0, so 0<=B<=T_ml=B+U; the assumed U is positive definite.

## Uniform cardinality

Suppose k_i=k for every i. Then

    T_ml = kT,    U = kT-B.

Since B and T are commuting real symmetric matrices, there is a common orthonormal eigenbasis q_1,...,q_d such that

    B q_j = b_j q_j,    T q_j = t_j q_j.

Thus U q_j = u_j q_j, where u_j = k t_j-b_j. Since U is positive definite, u_j>0 for every j; since B is positive semidefinite, b_j>=0.

For any W satisfying W^T W=I_r, let P=WW^T and p_j=q_j^T P q_j. Then 0<=p_j<=1, sum_j p_j=r, and

    tr(W^T B W) = sum_j b_j p_j,
    tr(W^T U W) = sum_j u_j p_j.

Therefore

    TR(W) = (sum_j b_j p_j)/(sum_j u_j p_j).

The feasible vectors p form the hypersimplex {p in [0,1]^d : sum_j p_j=r}, whose vertices are the indicator vectors of r-element subsets. If p is written as a convex combination of vertex indicators, the corresponding fractional-linear value is a denominator-weighted average of the vertex ratios, because all denominators are positive. Consequently the maximum is attained at an r-element coordinate subset. The stated aggregate hypothesis says directly that the coordinate subset I has ratio at least that of every other r-element subset. Hence the span selected by I maximizes TR. No uniqueness conclusion is needed; in particular, strict ordering of the individual ratios alone does not imply strict ordering of all subset trace ratios.

For TD,

    TD(W) = tr(W^T(B-U)W).

In the common eigenbasis, B-U has eigenvalue

    b_j-u_j = 2b_j-k t_j

in direction q_j. Ky Fan's maximum principle, together with the strict boundary separation for these eigenvalues, shows that span{q_i:i in I} maximizes TD.

For RT and DR, consider the generalized symmetric eigenvalue problem for the positive-definite pair (B,U). Its generalized eigenvalues are

    rho_j = b_j/u_j.

For an arbitrary r-dimensional subspace with orthonormal basis W, let theta_1(W)>=...>=theta_r(W) be the generalized eigenvalues of the compressed pair (W^T B W, W^T U W). Generalized Poincare separation gives, after ordering the rho_j decreasingly,

    theta_m(W) <= rho_m,    m=1,...,r.

Therefore

    RT(W) = sum_m theta_m(W) <= sum_{m=1}^r rho_m,

and, because all theta_m(W) and rho_m are nonnegative,

    DR(W) = product_m theta_m(W) <= product_{m=1}^r rho_m.

Taking W to have columns q_i for i in I attains the right-hand sides because I consists of the top generalized eigenvalue directions. The strict ratio separation identifies this top generalized eigenspace. Thus the selected span maximizes RT and DR as well.

## Variable cardinality

Since T_ml=B+U,

    TD(W) = tr(W^T(2B-T_ml)W).

Ky Fan's principle therefore shows that TD is maximized on the top-r eigenspace E_ml of 2B-T_ml.

Let A_0=2B-T and A=2B-T_ml. The variance identity gives

    A = A_0-R,    R>=0.

The RT criterion is governed by the generalized eigenvalues of the pair (B,U), rather than by the ordinary eigenvalues of B-U=2B-T_ml, so the two optimizing subspaces need not coincide. The following valid multilabel data set witnesses this while satisfying the small-residual regime.

Take d=2, r=1, labels a,b,c,d, and label sets

    L_1=L_2={a},   L_3=L_4={b},   L_5={c,d}.

Let alpha=sqrt(5/2), p=sqrt(3), and q=1/sqrt(2), and set

    x_1=(alpha+p, 1/4),
    x_2=(alpha-p, 1/4),
    x_3=(-alpha, 1/4+q),
    x_4=(-alpha, 1/4-q),
    x_5=(0,-1).

The grand mean is zero. Direct calculation gives

    B = diag(10,9/4),
    U = diag(6,1),
    T = diag(16,9/4),
    R=T_ml-T=diag(0,1).

Thus U is positive definite, rank(B)=2, and

    2B-T = diag(4,9/4),
    2B-T_ml = diag(4,5/4).

The reference gap is gamma=4-9/4=7/4, while ||R||_2=1<gamma. Nevertheless RT selects the second coordinate because 9/4>10/6, whereas TD selects the first coordinate because 4>5/4. Hence RT and TD need not have the same eigenspace.

It remains to prove the angle bound. Let Lambda_0 be the diagonal matrix of the top-r eigenvalues of A_0, with orthonormal eigenbasis X_0, and let D be the diagonal matrix of the lower d-r eigenvalues of A, with orthonormal eigenbasis Y. Write

    alpha_0 = lambda_r(A_0),
    a = lambda_{r+1}(A).

Weyl monotonicity and R>=0 imply

    a = lambda_{r+1}(A_0-R) <= lambda_{r+1}(A_0),

so

    delta := alpha_0-a >= gamma.

Also Weyl's lower bound gives

    lambda_r(A)-lambda_{r+1}(A)
    >= lambda_r(A_0)-||R||_2-lambda_{r+1}(A_0)
    = gamma-||R||_2 >0.

Thus E_ml is unambiguously the top-r eigenspace of A. Put H=Y^T X_0. From A=A_0-R, AX_0=X_0 Lambda_0-RX_0, and Y^T A=DY^T, we obtain the Sylvester equation

    D H - H Lambda_0 = -Y^T R X_0.

Its solution is

    H = integral_0^infinity exp(t(D-aI)) (Y^T R X_0)
        exp(-t(Lambda_0-aI)) dt.

All eigenvalues of D-aI are nonpositive, and every eigenvalue of Lambda_0-aI is at least delta. Therefore

    ||H||_2 <= integral_0^infinity ||R||_2 exp(-delta t) dt
             = ||R||_2/delta
             <= ||R||_2/gamma.

The norm ||Y^T X_0||_2 is the operator norm of sin Theta(E_ml,E_0). Consequently,

    ||sin Theta(E_ml,E_0)||_2 <= ||R||_2/gamma
                             = ||T_ml-T||_2/gamma.

Finally, let K={i:k_i>1} and define T^(K)=sum_{i in K} z_i z_i^T. Since k_i-1 <= max_j(k_j-1) on K,

    R <= (max_i(k_i-1)) T^(K).

Taking largest eigenvalues yields

    ||R||_2 <= (max_i(k_i-1)) lambda_max(T^(K)).

If every sample has one label, then K is empty, T^(K)=0, and R=0.
