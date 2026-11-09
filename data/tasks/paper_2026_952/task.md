# Problem

## Setup

Let d>=3 be an integer, and let S^{d-1} be the unit sphere in R^d. An unknown parameter u and all normalized iterates w_t lie in S^{d-1}. The link h is known.

Let F_t denote the information available before the exploration draw and observation at round t; w_t is F_t-measurable. Choose alpha_t>0 and rho_t in [0,1] before this draw. Conditionally on F_t, draw Z_t uniformly from the unit sphere in the subspace orthogonal to w_t and play

`a_t=sqrt(1-rho_t^2) w_t+rho_t Z_t`.

Observe

`y_t=h(<u,a_t>)+xi_t`,

where, conditionally on F_t, xi_t is independent of Z_t, has mean zero, and satisfies

`E[exp(lambda xi_t)|F_t]<=exp(lambda^2/2)`

for every real lambda. In particular, `E[xi_t|F_t,Z_t]=0`.

The link `h:[-1,1]->[-1,1]` is nondecreasing. There are fixed constants `0<gamma_0<=0.1` and `0<gamma_1<=gamma_2` such that h is differentiable on `[1-gamma_0,1]` and

`gamma_1<=h'(x)<=gamma_2`

there. Derivatives at endpoints are understood one-sided. Define `q_t=<u,w_t>`.

The half-step and normalization are

`w_{t+1/2}=w_t+alpha_t rho_t h'(sqrt(1-rho_t^2))(y_t-h(<w_t,a_t>))Z_t`,

`w_{t+1}=w_{t+1/2}/||w_{t+1/2}||`.

An admissible schedule evaluates h' only where that derivative exists and is finite. The schedules whose existence is requested below may be deterministic functions of the known link, its fixed constants, d, and the specified accuracy and confidence parameters. They cannot depend on u or on unobserved correlations.

Write `x wedge y=min{x,y}`. The notation `O~` and `Theta~` suppresses polylogarithmic factors in d and `1/delta`, additionally in `1/epsilon` for the accuracy bound and in T for the regret bound. Constants may depend only on the fixed link constants, including c_0 when it is assumed. Durations are integer-rounded. The initial iterate is indexed by 1, so a final index T corresponds to T-1 updates.

The burn-in conclusions use one of these additional conditions:

- **(A)** h is differentiable on `[0,1]`, with `h'(x)>=c_0>0` throughout that interval, for a fixed constant c_0.
- **(B)** h is convex on `[0,1]`.

Under (B), derivatives in integrals mean the almost-everywhere derivative. Define the extended nonnegative integral

`I_d(h)=integral_{1/(2sqrt(d))}^{1-gamma_0/4} m/h'(m)^2 dm`,

with the integrand interpreted as positive infinity wherever h' is zero. Values at the null set of nondifferentiability do not affect the integral. A finite-time bound expressed using this integral is asserted when `I_d(h)<infinity`; when the integral is infinite, that bound gives no finite-time conclusion.

## Task

Prove the following integrated theorem.

First assume `q_1>=1-gamma_0/4`.

1. For every `epsilon,delta>0`, there is an admissible schedule with

   `alpha_t=Theta~((d/t) wedge (1/d))`, `rho_t^2=Theta(1)`,

   and a final index `T=1+O~(d^2/epsilon)` such that, with probability at least `1-delta T`,

   `q_T>=1-epsilon`.

   If the requested accuracy is already guaranteed by the initial condition, no update is needed.

2. For every `delta>0`, there is an admissible schedule with

   `alpha_t=Theta~((1/sqrt(t)) wedge (1/d))`,

   `rho_t^2=Theta~((d/sqrt(t)) wedge 1)`,

   such that for every fixed integer horizon `T>=1`, with probability at least `1-delta T`,

   `sum_{t=1}^T [h(1)-h(q_t)] = O~(d sqrt(T))`.

Next assume only `q_1>=1/sqrt(d)`. For every `delta>0`, prove both of the following complementary conclusions.

3. Under (A), there is an admissible schedule with

   `alpha_t=Theta~(1/d)`, `rho_t^2=Theta(1)`,

   which reaches `q_T>=1-gamma_0/4` with probability at least `1-delta T` at a final index `T=1+O~(d^2)`.

4. Under (B), when `I_d(h)<infinity`, there is an admissible learning-rate schedule with `rho_t^2=Theta(1)` which reaches the same threshold with probability at least `1-delta T` at a final index

   `T=1+O~(d^2 I_d(h))`.

Construct schedules establishing these conclusions.
