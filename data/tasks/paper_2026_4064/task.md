# Problem

## Setup

Fix a nonnegative integer horizon N and positive integers k,d. For n=0,...,N-1, let U_n be a nonempty action set, let A_n:U_n -> R^(k x d) be a matrix-valued map, and let ell_n:U_n x R^k -> R be a loss function. These are deterministic problem data, with the data for round n known before its action is chosen.

Let V in R^(k x k) and Lambda_0 in R^(d x d) be fixed symmetric positive-definite matrices. Let Theta be a fixed convex subset of R^d and let mu_0 belong to Theta. The matrices, Theta, mu_0, and the finite constants c_v>0, c_theta>0, c_r>0, and L_z>=0 are known before the first round. An unknown deterministic parameter theta* belongs to Theta, and

||theta-mu_0||_{Lambda_0}<=c_theta for every theta in Theta.

For a symmetric positive-definite matrix M, write ||x||_M=(x^T Mx)^(1/2).

The available history at round n is I_n=(u_0,y_0,...,u_{n-1},y_{n-1}), with I_0 empty. The action is chosen using only this history and the known problem data, before observing

y_n=A_n(u_n)theta*+v_n.

Randomness enters through the measurement noise. Conditional on (I_n,u_n), v_n has mean zero and is subgaussian with proxy covariance c_v^2 V^(-1): for every a in R^k,

E[exp(a^T v_n) | I_n,u_n] <= exp((c_v^2/2)a^T V^(-1)a)

almost surely.

For 0<=n<N, define the constrained regularized least-squares estimate

mu_n in argmin_{theta in Theta} [ (1/2)||theta-mu_0||_{Lambda_0}^2 + (1/2)sum_{i<n}||y_i-A_i(u_i)theta||_V^2 ].

For 0<=n<=N, define

Lambda_n=Lambda_0+sum_{i<n}A_i(u_i)^T V A_i(u_i),

gamma_n(delta)=[c_theta^2+c_v^2 log det(Lambda_0^(-1)Lambda_n)+2c_v^2 log(1/delta)]^(1/2),

where delta belongs to (0,1) and an empty sum is zero.

For each n<N, define the output set

Z_n={A_n(u)theta : u in U_n, theta in Theta}.

Assume that, for every n<N, u in U_n, and z_1,z_2 in Z_n,

|ell_n(u,z_1)-ell_n(u,z_2)|<=L_z||z_1-z_2||_V.

Define phi_n(u,theta)=ell_n(u,A_n(u)theta), and let u_n* minimize phi_n(u,theta*) over U_n. Assume that

phi_n(u,theta*)-phi_n(u_n*,theta*)<=c_r

for every n<N and every u in U_n. Set

r_n=phi_n(u_n,theta*)-phi_n(u_n*,theta*),
R_N=sum_{n<N}r_n.

For a fixed delta in (0,1), at each round choose a global minimizer (u_n,theta_tilde_n) of

min_{u in U_n, theta in Theta} ell_n(u,A_n(u)theta)
subject to ||theta-mu_n||_{Lambda_n}<=gamma_n(delta).

Assume the minimizers used in these definitions exist. The estimator and selected joint minimizers are measurable functions of the available history and known problem data, with no access to theta* or to observations not yet received; all displayed random quantities are measurable. The oracle action u_n* is only a benchmark and is not supplied to the policy.

## Task

Prove that for every fixed delta in (0,1), the policy run with that delta satisfies, with probability at least 1-delta,

R_N <= max{c_r, 2 L_z gamma_N(delta)} [2 N log det(Lambda_0^(-1) Lambda_N)]^(1/2).
