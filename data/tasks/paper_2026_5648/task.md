# Problem

## Setup

Fix `p in (1,2)`. Let `beta_1,beta_2 in [0,1)` be fixed parameters, write `rho_i=1-beta_i`, and assume

`beta_1^2<beta_2` and `0<rho_2<=1/2`.

Let `(alpha_t)_(t>=1)` be an arbitrary deterministic sequence of finite nonnegative real step sizes. The schedule is fixed before the oracle randomness is sampled; it cannot depend on the oracle outcomes.

For a differentiable function `F:R->R` and a noise sequence `(xi_t)_(t>=1)`, consider the one-dimensional iteration with zero weight decay and zero denominator offset (`lambda=0`, `epsilon_t=0`):

`y_1=0`, `a_0=b_0=0`,

`g_t=F'(y_t)+xi_t`,

`a_t=beta_1 a_(t-1)+(1-beta_1)g_t`,

`b_t=beta_2 b_(t-1)+(1-beta_2)g_t^2`,

`y_(t+1)=y_t-alpha_t a_t/sqrt(b_t)`.

The ratio is defined as zero when numerator and denominator are both zero. Define

`C_beta=(1-beta_1)/sqrt((1-beta_2)(1-beta_1^2/beta_2))`.

Let `H_0` be the trivial sigma-field and `H_t=sigma(xi_1,...,xi_t)`. Thus the history before oracle call `t` is `H_(t-1)`.

## Task

Prove that there are universal positive constants `c,c_0,C_K,C_p` such that the following holds. For every `mu,R,sigma>0` and `delta in (0,1/2)`, define

`q=c_0 rho_2 log(1/delta)`, `M=sigma q^(-1/p)`, and `K=ceil(C_K/rho_2)`,

where `log` denotes the natural logarithm, and suppose

`q<=1/2` and `M>=2mu`.

One can choose a `C^2` lower-bounded function `F:R->R` and a noise sequence such that, for every `t`, `xi_t` is independent of `H_(t-1)` and

`E[xi_t | H_(t-1)]=0`,

`E[|xi_t|^p | H_(t-1)]<=2sigma^p` almost surely.

For this same function and oracle, for every integer `T>K`, the condition

`sum_(t=1)^K alpha_t C_beta/R + sum_(t=K+1)^T (alpha_t/R)[ C_p (mu/sigma + rho_1^((p-1)/p)) rho_2^((2-p)/(2p)) (log(1/delta))^(1/p) + C_beta delta ] <= c`

implies

`(1/T) sum_(t=1)^T E[|F'(y_t)|] >= mu/2`.

The same instance must satisfy, with

`L=sup_(y in R) |F''(y)|` and `Delta=F(0)-inf_(y in R) F(y)`,

that `L` is comparable to `mu/R`, `Delta` is comparable to `mu R`, and hence `Delta L` is comparable to `mu^2`.

Comparability means two-sided bounds by positive numerical multiples. All constants in the assertion and comparisons are independent of `p`, the other parameters, the step-size sequence, and `T`.
