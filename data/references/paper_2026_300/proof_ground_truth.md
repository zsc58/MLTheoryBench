# Reference Proof

Write A_m = Cov(Z,X) = Cov(tilde Z,tilde X) and a_m = Cov(Z,Y). Since the variables are centered, the structural equation and E[epsilon | Z]=0 give

    a_m = E[ZY]
        = E[Z X^T] beta* + E[Z epsilon]
        = A_m beta*.

Let barA_m = sqrt(m) A_m. From m A_m^T A_m -> Q, the Frobenius and operator norms of barA_m are bounded.

For a fold of size N_h, define centered scaled errors by

    widehat A_h = A_m + m^(-1/2) E_h,
    widehat A   = A_m + m^(-1/2) E,
    widehat a   = a_m + m^(-1/2) H.

Let P_m denote the possibly randomized fold partition. By assumption, P_m is independent of all observed values. Conditional on P_m, the observations in distinct folds are independent, and the fold errors are centered. Let

    G_m = { min_h N_h/m >= c }

for any fixed c satisfying 0<c<tilde r/(2K). Since N_h/tilde n -> 1/K and tilde n/m -> tilde r, P(G_m)->1. On G_m, every fold size is of order m, uniformly in h.

Conditional on P_m, the covariance formulas are

    Cov(vec(E_h) | P_m) = (m/N_h) Sigma_X,m,
    Cov(vec(E) | P_m)   = (m/tilde n) Sigma_X,m,
    Cov(H)              = (m/n) Sigma_Y,m.

All bounds below involving E_h are first established conditionally on P_m on G_m, with constants uniform over the possible fold sizes there. Since P(G_m)->1, these conditional bounds imply the corresponding unconditional O_p statements.

The covariance-operator assumptions imply that every relevant column block of the conditional covariance of vec(E_h) has operator norm O(m^(-1)), uniformly on G_m. Because d is fixed and barA_m has bounded Frobenius norm, finite-dimensional variance calculations give

    ||barA_m^T E_h||_op = O_p(m^(-1/2)),
    ||barA_m^T E||_op   = O_p(m^(-1/2)),
    ||barA_m^T H||_2    = O_p(m^(-1/2)).

For h != k, conditional independence and centering give, for fixed unit vectors u,v,

    Var(u^T E_h^T E_k v | P_m)
      = tr(Cov(E_h u | P_m) Cov(E_k v | P_m))
      = O(m^(-1)).

Hence, since d and K are fixed,

    ||E_h^T E_k||_op = O_p(m^(-1/2)).

Independence of the first and second samples similarly gives

    ||E_h^T H||_2 = O_p(m^(-1/2)),
    ||E^T H||_2   = O_p(m^(-1/2)).

For example, conditional on E and P_m,

    Var(u^T E^T H | E,P_m)
      <= (m/n) ||Sigma_Y,m||_op ||E u||_2^2,

and E||E||_F^2 is bounded. This proves the stated order. These bounds establish all signal-error, cross-fold, and cross-sample limits used below.

Now consider the scalar case d=1. Let N=tilde n and let U_1,...,U_N be the iid centered first-stage product vectors. Then

    E = sqrt(m)/N sum_i U_i.

Decompose

    E^T E = D_N + R_N,
    D_N = (m/N^2) sum_i ||U_i||_2^2,
    R_N = (m/N^2) sum_{i != j} U_i^T U_j.

Because tr(Sigma_X,m) -> b,

    E[D_N] = (m/N) tr(Sigma_X,m) -> b/tilde r.

The uniform fourth-moment bound gives Var(D_N)=O(m^(-1)). The off-diagonal terms in R_N are uncorrelated unless their unordered index pairs coincide. Thus

    Var(R_N)
      = 2 m^2 (N-1) tr(Sigma_X,m^2) / N^3.

Since tr(Sigma_X,m^2) <= m ||Sigma_X,m||_op^2 = O(m^(-1)) and N is of order m, Var(R_N)=O(m^(-1)). Consequently,

    E^T E ->p b/tilde r.

For the naive estimator, use the finite-valued convention in the task: it equals the ratio when widehat A^T widehat A>0 and equals 0 when that denominator is zero. Using a_m=A_m beta*,

    m widehat A^T widehat a
      = barA_m^T barA_m beta*
        + barA_m^T H
        + E^T barA_m beta*
        + E^T H
      ->p Q beta*.

Also,

    m widehat A^T widehat A
      = barA_m^T barA_m
        + barA_m^T E
        + E^T barA_m
        + E^T E
      ->p Q + b/tilde r.

The limit Q+b/tilde r is strictly positive. Therefore the probability of the zero-denominator event tends to zero, and the finite-valued extension has the same probability limit as the ratio on its complement. Slutsky's theorem yields

    widehat beta_N ->p Q beta* / (Q + b/tilde r).

Because Q>0, b>0, and tilde r is finite and positive, this limit differs from beta* whenever beta* != 0.

For the cross-fold estimator, for h != k,

    m widehat A_h^T widehat A_k
      = barA_m^T barA_m
        + barA_m^T E_k
        + E_h^T barA_m
        + E_h^T E_k.

Averaging the finitely many ordered pairs and applying the conditional-on-partition bounds gives

    C_XX ->p Q.

Moreover,

    C_XY
      = m widehat A^T widehat a
      ->p Q beta*

by the numerator expansion already established.

Since Q is positive definite and C_XX ->p Q, C_XX is nonsingular with probability tending to one. On that event the corrected weighted least-squares objective has the unique minimizer

    (C_XX^T W_N^(-1) C_XX)^(-1)
      C_XX^T W_N^(-1) C_XY.

The minimum-norm convention defines the estimator on the remaining events. Because W_N ->p W_0 and W_0 is positive definite, matrix inversion and multiplication are continuous at (Q,W_0,Q beta*). Hence

    (C_XX^T W_N^(-1) C_XX)^(-1) C_XX^T W_N^(-1)
      ->p (Q^T W_0^(-1) Q)^(-1) Q^T W_0^(-1),

and multiplying by C_XY ->p Q beta* gives

    widehat beta_CF ->p beta*.

This proves both claims.
