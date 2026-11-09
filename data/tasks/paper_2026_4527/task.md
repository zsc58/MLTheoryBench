# Problem

## Setup

Let `d` and `T` be positive integers, let `[d]={1,...,d}`, and let `e_i` denote the `i`th standard basis vector of `R^d`. Inner products are the usual Euclidean inner products, and `log` denotes the natural logarithm.

For each round `t=1,2,...,T`, a nonempty action set `X_t subseteq Z^d` is revealed. Assume every `X_t` is M-convex: for any `x,y in X_t` and any coordinate `i` with `x(i)>y(i)`, there exists `j` with `x(j)<y(j)` such that `x-e_i+e_j` and `y+e_i-e_j` both belong to `X_t`.

There is an unknown vector `w* in [0,1]^d` whose coordinates are pairwise distinct. The agent plays an action `x_t in argmax_{x in X_t}<w*,x>`. The learner recommends an action `hat x_t` before observing `x_t`. Assume a constant `0<=B<infinity`, independent of `t`, bounds every objective gap:

`|<w*,x-y>| <= B`

for all rounds `t` and all `x,y in X_t`.

For an action `x in X_t`, define

`E_t(x)={(i,j) in [d] x [d]: i!=j and x-e_i+e_j in X_t}`.

The learner maintains

`A_1=emptyset`,

`P_t={w in [0,1]^d: w(i)>=w(j) for every (i,j) in A_t}`.

Let `Vol` denote `d`-dimensional Lebesgue measure. At round `t`, let `c_t` be the center of gravity of `P_t`, namely

`c_t = (1/Vol(P_t)) integral_{P_t} w dw`.

The learner chooses `hat w_t in P_t` with pairwise distinct coordinates by breaking the coordinate ties of `c_t` without reversing any strict coordinate comparison: for all `i,j`,

`c_t(i)>c_t(j) implies hat w_t(i)>hat w_t(j)`.

The estimate and this coordinate tie-breaking use only the past observations `{(X_s,x_s):s<t}` and a fixed rule, not `X_t` or the current action `x_t`. The learner then recommends a tie-broken maximizer

`hat x_t in argmax_{x in X_t}<hat w_t,x>`.

After observing `x_t`, it updates on every round by

`A_{t+1}=A_t union E_t(x_t)`.

Regret is

`R_T=sum_{t=1}^T <w*,x_t-hat x_t>`.

## Task

Prove that the procedure is well-defined and that, for every `T`, it satisfies

`R_T <= B * log(d!)/[-log(1-1/e)]`,

and hence `R_T=O(B d log(d+1))`, with a universal implied constant and a bound independent of `T`.
