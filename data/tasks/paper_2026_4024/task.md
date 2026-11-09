# Problem

## Setup

For each n, let A and Z be independent symmetric Gaussian Wigner matrices: their diagonal entries are independent N(0,2/n), their upper-triangular off-diagonal entries are independent N(0,1/n), and the lower triangles are filled by symmetry.  Let P be a uniformly random permutation matrix, independent of A and Z, and define

$B=P^T(A+sigma Z)P$.

Let

$B_n={X in R^{n x n}: X_{ij}>=0, sum_j X_{ij}=1, sum_i X_{ij}=1}$

be the doubly stochastic polytope, and let

$H_n={X in [0,1]^{n x n}: sum_{i,j}X_{ij}=n}$.

For either choice C_n in {B_n,H_n}, let X* be any minimizer of

$min_{X in C_n} ||A X-X B||_F$.

All logarithms are natural.  Suppose sigma=sigma_n>=0 is deterministic and satisfies

$sigma_n=o(n^{-1/2}/(log n)^4)$.

For a matrix X, define its row-wise argmax rounding by choosing, in each row i, any index attaining max_j X_{ij}.

## Task

Prove that there is a universal constant C such that, with probability tending to one as n tends to infinity, simultaneously for C_n=B_n and C_n=H_n and for every minimizer X*,

$||X*-P||_F^2 <= C sigma_n n^(3/2)(log n)^4=o(n).$

Also prove that the row-wise argmax rounding of every such X* agrees with the hidden permutation on all but o(n) rows.
