# Problem

## Setup

Fix alpha in (0,1), an integer k >= 1, a feature domain X contained in R^d for an integer d >= 1, and group-membership functions h_j:X -> [0,1], which may overlap. An arbitrary sequence (X_t,Y_t), with X_t in X and Y_t in R, is observed online. The predictor function f_t:X -> R depends on the data only through time t-1, and its prediction at the current feature is hat Y_t=f_t(X_t). Define the score s_t=|Y_t-hat Y_t| and the interval [hat Y_t-tau_t, hat Y_t+tau_t], interpreted as empty when tau_t<0.

Let h_t=(h_1(X_t),...,h_k(X_t)). The online procedure starts with V_{0,j}=1/k. Let mu be the probability measure on (0,1) with density

mu(du)=du/[pi sqrt(u(1-u))].

At round t, for every j, define from past returns

R_{t-1,j}(u)=prod_{i=1}^{t-1}[u p_{i,j,1}+(1-u)p_{i,j,2}],

where an empty product equals 1, and set

lambda_{t,j}=[integral_0^1 u R_{t-1,j}(u) mu(du)]/[integral_0^1 R_{t-1,j}(u) mu(du)].

This specifies the two-asset universal-portfolio rule with Jeffreys prior. Set

theta_{t,j}=V_{t-1,j}(lambda_{t,j}-alpha)/(alpha(1-alpha)),   tau_t=<theta_t,h_t>.

After observing s_t, set I_t=1{s_t<=tau_t} and define

a_{t,j}=(I_t-(1-alpha))h_{t,j},

p_{t,j,1}=1-a_{t,j}/alpha,   p_{t,j,2}=1+a_{t,j}/(1-alpha),

V_{t,j}=V_{t-1,j}[lambda_{t,j}p_{t,j,1}+(1-lambda_{t,j})p_{t,j,2}].

Let D>0 and q>=0 be constants such that s_t<=D t^q for all t>=1. For a horizon T, let n_j=sum_{t=1}^T h_{t,j}. At horizons for which n_j>0 for every j, define

Err_T(j)=|sum_{t=1}^T a_{t,j}|/n_j.

## Task

Prove that for every integer T>=1 for which all n_j are positive, and every group j,

Err_T(j) <= [U_T(k)+sqrt(2 n_j alpha(1-alpha) U_T(k))]/n_j,

where

U_T(k)=ln(1+(1-alpha)D (T+1)^(q+1)/(q+1)) + 0.5 ln(pi(T+1)) + ln k.

The guarantee is deterministic and holds for arbitrary data streams satisfying the stated conditions.
