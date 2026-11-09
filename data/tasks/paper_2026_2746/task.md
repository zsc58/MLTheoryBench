# Problem

## Setup

Let m,d >= 1 be integers, let A in R^(m x d) and b in R^m, and let x^star in R^d satisfy A x^star = b. Consider an affine first-degree iterative method with step maps

P_j(z)=G_j z+f_j,   G_j in R^(d x d), f_j in R^d.

Fix an iteration index i, and write the cumulative map as P=P_i o ... o P_1, so that P(z)=Gz+f with G in R^(d x d), f in R^d, and x_i=P(x_0) for x_0 in R^d. Assume the source fixed-point property: P(y)=y for every exact solution y in R^d satisfying Ay=b. In particular, this holds when every step map fixes every exact solution.

The initial belief is x^star~N(x_0,Sigma_0), where Sigma_0 in R^(d x d) is symmetric positive definite. In the calibration experiment, the sampled x^star is the exact truth from the setup, so the fixed-point identity P(x^star)=x^star holds almost surely.

The iterate belief is the affine pushforward

mu_i=N(x_i,Sigma),   Sigma=G Sigma_0 G^T.

Let r=rank(Sigma). Let R in R^(d x r) have columns forming a basis of range(Sigma), and let N in R^(d x (d-r)) have columns forming a basis of ker(Sigma). Here I_r denotes the r x r identity, and M^(-1/2) denotes the symmetric inverse square root of a positive-definite matrix M.

Use the standard empty-space convention when r=0 or d-r=0: zero-dimensional vectors and matrices have their unique empty meanings, I_0 is the 0 x 0 identity, N(0,I_0) is the unique Gaussian law on R^0, and the inverse square root of the 0 x 0 matrix is the unique 0 x 0 matrix.

Strong calibration means that, when x^star is sampled from the initial Gaussian,

(R^T Sigma R)^(-1/2) R^T(x_i-x^star) ~ N(0,I_r),

N^T(x_i-x^star)=0 almost surely.

## Task

Prove that every affine probabilistic iterative method satisfying the fixed-point property above is strongly calibrated at iteration i.
