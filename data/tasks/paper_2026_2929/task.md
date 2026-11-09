# Problem

## Setup

Let `N>=1` and `d>=1` be integers. On a common probability space with probability measure `P`, there are `N` calibration units and a fixed target unit indexed by `N+1`. At each round `t=1,2,...`, let `X_{k,t} in R^d` and `Y_{k,t} in R` be the feature and response of unit `k`. Let `R_t in {0,1}` indicate whether the target response from round `t` is revealed in the next round. Set `R_0=0` and `Y_{N+1,0}=0`.

The observation batch at round `t` is

`O_t=((X_{k,t},Y_{k,t})_{k=1}^N, X_{N+1,t}, R_{t-1}, R_{t-1}Y_{N+1,t-1})`.

Define `F_0={emptyset,Omega}`, `F_t=sigma(O_1,...,O_t)`, and

`F_t^+=F_t join sigma(R_t,R_tY_{N+1,t})`.

Prediction sets at round `t` are `F_t`-measurable and use no current target response. Conditional probabilities and conditional laws below are regular conditional probabilities and laws under `P`.

Let `s:R^d x R->[0,infinity)` be a fixed measurable, finite-valued score function, common to all units. Any fitted predictor used in this function is treated as fixed throughout the analysis. For `t>=2`, define the running feature means

`hat mu_{k,t-1}=(1/(t-1)) sum_{r=1}^{t-1} X_{k,r}`.

Let `mu_k in R^d` be fixed latent profiles and let `h>0` be a fixed finite bandwidth. Define, for `k=1,...,N`,

`hat omega_k^(t)=exp(-||hat mu_{k,t-1}-hat mu_{N+1,t-1}||_2^2/(2h^2))/(1+sum_{j=1}^N exp(-||hat mu_{j,t-1}-hat mu_{N+1,t-1}||_2^2/(2h^2)))`,

and let `hat omega_{N+1}^(t)` be the reciprocal of the same denominator.

Let `alpha_t` be any finite real-valued `F_{t-1}^+`-measurable level and set `bar alpha_t=min(1,max(0,alpha_t))`. Write `S_{k,t}=s(X_{k,t},Y_{k,t})` for the actual score, including the unobserved target score. The augmented calibration vector is

`tilde S_t=(S_{1,t},...,S_{N,t},+infinity)`.

With `overline R=R union {-infinity,+infinity}`, define

`q_t=inf{q in overline R: sum_{k=1}^{N+1} hat omega_k^(t) 1{(tilde S_t)_k<=q} >= 1-bar alpha_t}`,

where the infimum of an empty set is `+infinity`. The deployed prediction set is

`C_t(X_{N+1,t})={y in R:s(X_{N+1,t},y)<=q_t}`.

Thus clipped level 0 gives the full real line, and clipped level 1 gives the empty set.

Let `P_t` be the conditional law of the actual score vector `(S_{1,t},...,S_{N+1,t})` given `F_{t-1}^+`. Let `P_{t,k}^{swap}` be the conditional law of that vector after swapping coordinates `k` and `N+1`. These laws do not replace the target score by the sentinel. For probability laws `Q,Q'` on `R^{N+1}`, define

`d_TV(Q,Q')=sup_{A Borel in R^{N+1}} |Q(A)-Q'(A)|`.

Assume that for every `delta in (0,1)` and each `t>=2`, there is a finite nonnegative deterministic tolerance `epsilon_{t,delta}` such that

`P(max_{1<=k<=N+1}||hat mu_{k,t-1}-mu_k||_2<=epsilon_{t,delta})>=1-delta`.

Assume also that there is a fixed nondecreasing function `phi:[0,infinity)->[0,1]` such that, for every round `t>=1` and calibration index `k`, almost surely,

`d_TV(P_t,P_{t,k}^{swap})<=phi(||mu_k-mu_{N+1}||_2)`.

Define

`D_mu=max_{1<=k<=N}||mu_k-mu_{N+1}||_2`,

`phi_max=max_{1<=k<=N}phi(||mu_k-mu_{N+1}||_2)`,

and the oracle peer weights

`omega_k^circ=exp(-||mu_k-mu_{N+1}||_2^2/(2h^2))/(1+sum_{j=1}^N exp(-||mu_j-mu_{N+1}||_2^2/(2h^2)))`.

## Task

Prove that for every fixed `t>=2` and `delta in (0,1)`, on an event of probability at least `1-delta`,

`P(Y_{N+1,t} notin C_t(X_{N+1,t}) | F_{t-1}^+) <= bar alpha_t + sum_{k=1}^N omega_k^circ phi(||mu_k-mu_{N+1}||_2) + (8N phi_max/h^2)(D_mu epsilon_{t,delta}+epsilon_{t,delta}^2)`.
