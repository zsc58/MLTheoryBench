# Problem

## Setup

Fix parameters `beta>1`, `gamma>0`, and `s>0`. Fix a Lebesgue-measurable profile `zeta:[0,1]->[0,1]`, independent of the horizon and the peak rate, with `zeta(0)=1` and

`m=integral_0^1 zeta(x)dx>0`.

All integrals are Lebesgue integrals. Assume there are fixed constants `delta in (0,1)` and `c_-,c_+>0` such that

`c_-(1-x)^gamma <= zeta(x) <= c_+(1-x)^gamma`, for `delta<=x<=1`.

For each positive integer horizon N and peak rate eta_0, define

`eta_N(z)=eta_0 zeta(z/N)`, for `0<=z<=N`.

Its intrinsic clock and total intrinsic horizon are

`Gamma_N(z)=integral_0^z eta_N(u)du`, `T_N=Gamma_N(N)=eta_0 N m`.

For `0<t<=T_N`, set

`z_N(t)=inf{z in [0,N]:Gamma_N(z)>=t}`,

and set `z_N(0)=0`. Define the intrinsic learning rate by

`phi_N(t)=eta_N(z_N(t))`, for `0<=t<=T_N`.

Fix a stability cap `eta_max>0` and restrict `0<eta_0<=eta_max`. Let `E_N(eta_0)` be a nonnegative deterministic loss quantity, interpreted as expected final excess loss. Assume the following functional scaling law: with

`K(u)=(1+u)^(-(2-1/beta))`, for `u>=0`,

there are fixed constants `C_1,C_2>0` and `T_0>=2` such that, whenever `T_N>=T_0`,

`C_1 [(1+T_N)^(-s)+integral_0^{T_N} K(T_N-t)phi_N(t)dt] <= E_N(eta_0) <= C_2 [(1+T_N)^(-s)+integral_0^{T_N} K(T_N-t)phi_N(t)dt]`.

This is the assumed loss model in a fixed label-noise-dominated regime, with fixed noise standard deviation `sigma>=1` and a sufficiently small fixed stability cap. No derivation of the scaling law from stochastic dynamics is requested.

An admissible peak-rate sequence is a sequence `eta_0=eta_0(N)` satisfying `0<eta_0(N)<=eta_max` and `T_N->infinity`. All asymptotic statements concern `N->infinity`. The notation `asymp` means comparison above and below by positive constants. Constants may depend on the fixed parameters, profile, tail constants, stability cap, and assumed scaling-law constants, but not on N or the varying peak rate. Comparisons in terms of T_N are to hold uniformly once T_N exceeds a fixed threshold.

Optimality is understood in order: `E_N^* asymp R_N` means that every admissible sequence has `E_N(eta_0(N))>=c R_N` eventually, with a positive constant c independent of the sequence, and some admissible sequence has `E_N(eta_0(N))<=C R_N` eventually. The starting horizon may depend on the sequence. Write `eta_0^*` for an admissible sequence attaining this optimal order; an exact finite-N minimizer is not required.

## Task

Prove the following integrated theorem. Define

`alpha=min{beta,gamma+1}`.

1. For every admissible peak-rate sequence, the final loss satisfies

`E_N(eta_0) asymp T_N^(-s)+eta_0 T_N^(-(1-1/alpha)) (log T_N)^{1{beta=gamma+1}}`,

with the uniformity specified above.

2. If `s<1-1/alpha`, an order-one admissible peak rate is optimal and

`E_N^* asymp N^(-s)`.

If `s>=1-1/alpha` and `beta!=gamma+1`, an order-optimal peak rate and the optimal loss order satisfy

`eta_0^* asymp N^(-(s-1+1/alpha)/(s+1/alpha))`,

`E_N^* asymp N^(-s alpha/(s alpha+1))`.

If `s>=1-1/alpha` and `beta=gamma+1`, they satisfy

`eta_0^* asymp N^(-(s-1+1/alpha)/(s+1/alpha)) (log N)^(-1/(s+1/alpha))`,

`E_N^* asymp N^(-s alpha/(s alpha+1)) (log N)^(s alpha/(s alpha+1))`.

Here `1{beta=gamma+1}` is one when the equality holds and zero otherwise.
