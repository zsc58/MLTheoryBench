# Problem

## Setup

Let n and T_max be positive integers, and let alpha be in (0,1). A task x is drawn from a distribution P_X. At each integer time t>=1, a generator produces an output C_t and a black-box verifier returns a real score S_t. Define H_0=x, G_0=sigma(x), and, for t>=1,

H_t=(x,C_1,S_1,...,C_t,S_t),   G_t=sigma(H_t).

Let F in {0,1} denote pipeline feasibility, where F=0 is the failure/infeasible case. Assume P(F=0)>0, so that probabilities and expectations conditional on F=0 are defined.

Before the workflow, an indexed reference pool R=(R_1,...,R_n) of real scores is available and is held fixed throughout the workflow; repeated values are retained. Write A_t=sigma(R) joined with G_t for t>=0. Under F=0, assume that for every integer t>=1 and every real threshold s,

P(S_t>=s | A_{t-1},F=0) <= (1/n) sum_{i=1}^n 1{R_i>=s} almost surely.

Equivalently, conditional on R, an independent draw from the empirical distribution on R has an upper tail at least as large as the conditional upper tail of S_t. Define the empirical upper-tail p-value

p_t=(1+sum_{i=1}^n 1{R_i>=S_t})/(n+1).

For each t, let f_t be a possibly random function from [0,1] to [0,infinity) satisfying: for every u in [0,1], f_t(u) is A_{t-1}-measurable; for every outcome, u -> f_t(u) is nonincreasing; and integral_0^1 f_t(u) du <=1 almost surely, where the integral is with respect to Lebesgue measure. Define

E_0=1,   E_t=product_{s=1}^t f_s(p_s),

tau_alpha=inf{t>=1:E_t>=1/alpha},

with inf(empty set)=infinity. Set the wrapper's terminal release indicator to be D=1{tau_alpha<=T_max}.

## Task

Prove the following integrated theorem: under the stated dominance assumption, for every integer t>=1 and u in [0,1],

P(p_t<=u | A_{t-1},F=0)<=u almost surely;

moreover, (E_t) is a nonnegative supermartingale with respect to (A_t) under the conditional law given F=0, and the resulting release rule satisfies

P(D=1 | F=0)<=alpha.
