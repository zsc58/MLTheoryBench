# Problem

## Setup

For each m, let Z and tilde Z be R^m-valued, X and tilde X be R^d-valued, and Y be real-valued centered random variables, with fixed d. Assume

    Y = X^T beta* + epsilon,
    E[epsilon | Z] = 0,
    Cov(tilde Z, tilde X) = Cov(Z,X) =: A_m.

Thus, writing a_m = Cov(Z,Y), one has a_m = A_m beta*.

We observe two independent samples: n iid copies of (Z,Y) and tilde n iid copies of (tilde Z,tilde X). The two samples are independent. Since the variables are centered, define

    widehat a = (1/n) sum_{i=1}^n Z_i Y_i,
    widehat A = (1/tilde n) sum_{i=1}^{tilde n} tilde Z_i tilde X_i^T.

Partition the second sample into a fixed number K >= 2 of asymptotically equal folds. The partition is fixed in advance, or is randomized independently of all observed values. If N_h is the size of fold h, then N_h/tilde n -> 1/K. Let widehat A_h denote the same empirical cross-moment computed using fold h.

Let

    U_m = vec(tilde Z tilde X^T - A_m),
    V_m = ZY - a_m,

and define Sigma_X,m = Cov(U_m) and Sigma_Y,m = Cov(V_m). As m -> infinity, assume

    n/m -> r in (0,infinity),
    tilde n/m -> tilde r in (0,infinity),
    m A_m^T A_m -> Q, with Q positive definite,
    ||Sigma_X,m||_op = O(m^(-1)),
    ||Sigma_Y,m||_op = O(m^(-1)),
    sup_m [E||U_m||_2^4 + E||V_m||_2^4] < infinity.

In the scalar case d=1, additionally assume tr(Sigma_X,m) -> b in (0,infinity).

Define

    C_XX = m/[K(K-1)] sum_{h != k} widehat A_h^T widehat A_k,
    C_XY = m widehat A^T widehat a,

and let W_N be a positive-definite d by d matrix sequence such that W_N ->p W_0, where W_0 is positive definite. Define widehat beta_CF to be the minimum-Euclidean-norm minimizer of

    (C_XY - C_XX beta)^T W_N^(-1) (C_XY - C_XX beta).

For d=1, define the naive estimator by

    widehat beta_N = (widehat A^T widehat a)/(widehat A^T widehat A)

when widehat A^T widehat A > 0, and set widehat beta_N=0 when widehat A^T widehat A=0.

## Task

Prove the following integrated high-dimensional result.

- If d=1, then

    widehat beta_N ->p Q beta* / (Q + b/tilde r),

so the naive estimator is asymptotically biased whenever beta* != 0.

- For fixed d, widehat beta_CF ->p beta*.

The minimum-norm convention applies only if the displayed cross-fold minimization has more than one minimizer; with probability tending to one the minimizer is unique.
