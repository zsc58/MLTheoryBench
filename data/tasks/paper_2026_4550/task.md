# Problem

## Setup

Let S and A be finite nonempty sets. Consider a discounted Markov decision process with discount `gamma in [0,1)`. For each state-action pair x, let `p_x` be the joint law of a reward R and a next state S'. Assume `|R|<=B` almost surely for a fixed finite constant B, and fix a variance-bound parameter `sigma^2>0` such that `Var(R | x)<=sigma^2` for every x. Reward and next state need not be independent.

For `Q:S x A -> R`, define

`(T*Q)(x)=E_{(R,S')~p_x}[R+gamma max_{a in A}Q(S',a)]`,

and let Q* be its unique fixed point. The initial table `Q_0^(0)` is fixed, deterministic, and finite.

Use deterministic cycle lengths `K_n` chosen before sampling. At inner step k of cycle n, let `F_{n,k}` contain the history before the current sample. Draw a coordinate `X_{n,k}` from an `F_{n,k}`-measurable distribution satisfying

`P(X_{n,k}=x | F_{n,k})>=xi>0`

for every x, almost surely. Conditional on `F_{n,k}` and `X_{n,k}=x`, the reward and next-state sample has law `p_x`. The coordinate distribution may depend on past observations. With the target table frozen at `Q_n^(0)`, perform

`Q_n^(k+1)(x)=Q_n^(k)(x)+1_{X_{n,k}=x} alpha_n^(k)[R_{n,k}+gamma max_a Q_n^(0)(S'_{n,k},a)-Q_n^(k)(x)]`,

for `k=0,...,K_n-1`, and set `Q_{n+1}^(0)=Q_n^(K_n)`. Use

`alpha_n^(k)=2/[xi(k+s)]`, with `s=2/xi`.

Define the expected outer error and conditional squared inner error by

`E_n=E[||Q_n^(0)-Q*||_infinity]`,

`e_n^(k)=E[||Q_n^(k)-T*Q_n^(0)||_2^2 | F_{n,0}]`.

All expectations include the algorithm's sampling randomness. Set

`c1=((2/xi)+1)|S||A|(1+gamma)^2+(16/xi^2+8/xi)gamma^2`,

`c2=(8/xi^2+4/xi)(sigma^2+2gamma^2||Q*||_infinity^2)`,

`mu=(1+gamma)/2`, and `K_min=c1/(mu-gamma)^2`.

## Schedule comparison classes

For an integer `m>=0` and positive real frequencies `k_0,...,k_{m-1}`, define the cost and feasibility certificate

`cost(m,k)=sum_{j=0}^{m-1}k_j`,

`B_m(k)=mu^m E_0+sum_{j=0}^{m-1}mu^(m-1-j)sqrt(c2/k_j)`.

For `m=0`, both sums are empty and `B_0=E_0`. A comparison schedule is feasible at accuracy epsilon if every frequency is at least K_min and `B_m(k)<=epsilon`. The fixed class additionally requires all its frequencies to be equal; the variable class imposes no such equality. These comparison classes allow real frequencies, whereas the algorithm uses integer frequencies.

A family of implemented schedules is quasi-optimal in one of these classes if it is feasible for all sufficiently small positive epsilon and there is a finite constant C, independent of epsilon, such that its cost is at most C times the infimum feasible cost in that class. Thus the benchmark is certificate feasibility, not merely attaining a specified actual stochastic error.

## Task

If `E_0=0`, use the empty schedule `N=0`. Prove that it has zero error and is optimal in both comparison classes.

If `E_0>0`, prove the following for all sufficiently small `epsilon>0`, with

`N=ceil(log(epsilon/(2E_0))/log(mu))`.

1. The fixed schedule

   `K_j=ceil[(4c2/epsilon^2)((1-mu^N)/(1-mu))^2]`, for `j=0,...,N-1`,

   satisfies the frequency floor, has `E_N<=epsilon`, is quasi-optimal in the fixed comparison class, and has cost

   `O(log((1-gamma)^(-1)epsilon^(-1))/((1-gamma)^4 xi^2 log(2/(1+gamma))epsilon^2))`.

2. The variable schedule

   `K_j=ceil[C_epsilon mu^(2(N-1-j)/3)]`, for `j=0,...,N-1`,

   where

   `C_epsilon=(4c2/epsilon^2)((1-mu^(2N/3))/(1-mu^(2/3)))^2`,

   satisfies the same frequency floor, has `E_N<=epsilon`, is quasi-optimal in the variable comparison class, and has cost

   `O(xi^(-2)(1-gamma)^(-5)epsilon^(-2))`,

   with no logarithmic factor in epsilon.

The big-O statements are asymptotic in epsilon. Their multiplicative constants may depend on B and sigma, but not on gamma, xi, |S|, or |A|. The sufficiently-small-epsilon threshold may depend on all fixed setup parameters, including the initialization.
