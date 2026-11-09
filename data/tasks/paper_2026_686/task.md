# Problem

## Setup

Fix an integer n>=1. Consider a process in R^n satisfying

  x_{t+1}=Abar x_t+w_t+v_t,    t=0,1,2,...,

where Abar is an n by n real matrix with spectral radius less than one. Write

  F_t=sigma(x_0,...,x_t).

Fix p in (0,1/2). The variables delta_{t,i}, for t>=0 and 1<=i<=n, are mutually independent Bernoulli(p) variables. The entire indicator array is independent of the initial state and noise sequence. The noise variables are independent across time and independent of x_0. Each noise variable has mean zero and a symmetric distribution, meaning that w_t and -w_t have the same law. Each noise law is absolutely continuous with respect to Lebesgue measure on R^n, and there is a finite B such that ||w_t||_2<=B almost surely for every t.

At time t, the attack v_t is a measurable function of x_0,...,x_t, the indicators delta_0,...,delta_t, and the previously selected attacks v_0,...,v_{t-1}. It is selected before the fresh noise w_t. Here delta_t=(delta_{t,1},...,delta_{t,n}). The attack must satisfy

  v_{t,i}=0 whenever delta_{t,i}=0.

Assume uniform sub-Gaussian bounds on the initial state, noise, and conditional attack distributions. Explicitly, there are finite positive constants sigma_v and sigma_w such that, for every unit vector u in R^n and every t>=0,

  E[exp((u^T x_0)^2/sigma_v^2)] <= 2,
  E[exp((u^T w_t)^2/sigma_w^2)] <= 2,
  E[exp((u^T v_t)^2/sigma_v^2) | F_t] <= 2 almost surely.

Assume also that, for some lambda>0,

  E[x_t x_t^T | F_{t-1}] >= lambda^2 I_n almost surely,    t>=1,

where the matrix inequality denotes positive semidefinite ordering.

For a finite convex loss phi:R^n -> [0,infinity) that is even and coercive, and for a finite radius R>0, define the residual estimator from the observed trajectory (x_0,...,x_T) by choosing any minimizer

  A_T in argmin_{||A||_F<=R} (1/T) sum_{t=0}^{T-1} phi(x_{t+1}-Ax_t),

for each positive integer T. Here ||.||_F is the Frobenius norm, evenness means phi(z)=phi(-z), and coercivity means phi(z)->infinity as ||z||_2->infinity.

## Task

Prove that for every such loss phi, every finite R>0, and every prescribed p in (0,1/2), there exists a system instance and an attack process satisfying the setup, with stable true matrix Abar=0, for which the empirical minimizers are inconsistent in the following simultaneous sense:

There is an event of probability one on which no sequence A_T of empirical minimizers converges to Abar.

The instance and attack process must be fixed for all trajectory lengths T. The noise law, initial-state law, attack process, and finite constants in the setup may depend on n, phi, R, and p.
