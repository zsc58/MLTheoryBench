# Problem

## Setup

Let `d>=2` and `T>=1` be integers, let `[d]={1,...,d}`, and let `log` denote the natural logarithm.

Fix an arbitrary deterministic adversary strategy. On each round `t`, it privately specifies a loss vector `ell_t in [0,1]^d` and a directed graph `G_t` on `[d]`. These choices may be functions of the earlier actions `I_1,...,I_{t-1}`, but not of the learner's current or future random draws. Every vertex has a self-loop.

Before acting, the learner has access only to its earlier actions and previously revealed feedback, not to the current graph or loss vector. It samples an arm `I_t` from its distribution `p_t`. After acting, it observes the entire graph `G_t` and the loss `ell_{t,i}` for every edge `(I_t,i)` of `G_t`.

Define the expected regret by

`R_T=max_{a in[d]} E[sum_{t=1}^T (ell_{t,I_t}-ell_{t,a})]`,

where the expectation is over the learner's random draws under the fixed adversary strategy.

Let `alpha_t` be the independence number of the underlying undirected graph obtained from `G_t` by ignoring edge directions and self-loops.

Consider Algorithm A. Set `L=log d` and `hat_L_{0,i}=0`. On round `t`, using the quantities `Q_s` computed on earlier rounds, set

`eta_t=gamma_t=sqrt(L/(d+sum_{s=1}^{t-1}Q_s))`,

`w_{t,i}=exp(-eta_t hat_L_{t-1,i})`,

`p_{t,i}=w_{t,i}/sum_{j=1}^d w_{t,j}`,

and sample `I_t` from `p_t`.

After observing the feedback, compute

`o_{t,i}=sum_{j:(j,i) in G_t} p_{t,j}`,

`Q_t=sum_{i=1}^d p_{t,i}/(o_{t,i}+gamma_t)`.

Define

`hat_ell_{t,i}=ell_{t,i}/(o_{t,i}+gamma_t)` if `(I_t,i) in G_t`, and `hat_ell_{t,i}=0` otherwise,

and update

`hat_L_{t,i}=hat_L_{t-1,i}+hat_ell_{t,i}`.

## Task

Prove that, for every adversary strategy described above, Algorithm A satisfies

`R_T <= 4 E[sqrt((d+2 sum_{t=1}^T (H_t alpha_t+1)) log d)]`,

where

`H_t=log(1+(ceil(d^2 sqrt(td/log d))+d)/alpha_t)`.
