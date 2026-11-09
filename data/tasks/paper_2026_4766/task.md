# Problem

## Setup

Fix finite horizons 0<S<=T and a deterministic initial state v_0>0. Let W be a standard Brownian motion, and let F be its completed, right-continuous natural filtration. Let V be the strong solution on [0,T] of

 dV_t=a(V_t,t)dt+c(V_t,t)dW_t,    V_0=v_0.

The functions a,c:R x [0,T]->R are jointly Borel measurable. Assume there are finite constants K,C such that, for every x,z in R and t in [0,T],

 |a(x,t)-a(z,t)|+|c(x,t)-c(z,t)| <= K|x-z|,

 |a(x,t)|+|c(x,t)| <= C(1+|x|).

Assume

 P(V_t>0 for every t in [0,T])=1.

In particular, the continuous intensity path has finite integral on [0,T].

Conditional on the full Brownian path, sample a point process N on [0,S] whose conditional law is that of an inhomogeneous Poisson process with rate t->V_t. Thus the observation is sampled through this Poisson kernel, not by introducing additional information into F. Write

 Y=(r_1,...,r_{N_S}),    0<r_1<...<r_{N_S}<=S,

for its complete event sequence. The event-sequence space is the disjoint union of the empty sequence and the sets of ordered n-tuples in (0,S], n>=1, with their Borel sigma-algebras.

Assume that there is a fixed positive sigma-finite measure eta on this space such that, for every t in [0,T], the conditional law of Y given F_t has a density p_t(omega,y) with respect to eta. Take a jointly measurable version, and assume 0<p_t(omega,y)<infinity for eta-almost every y, almost surely.

For a fixed event sequence y and 0<=t<=S, define

 beta_t(v;y)=E_{t,v}[exp(-integral_t^S V_u du) product_{t<r_i<=S} V_{r_i}],    v>0,

where E_{t,v} is expectation under the prior diffusion with coefficients a,c, initialized at state v at time t. An empty product is one. Assume beta is finite and strictly positive on this domain, is differentiable in v, and that beta and partial_v beta are jointly Borel measurable in (t,v,y). For each fixed y, assume beta is C^{1,2} in (t,v) on every open time interval in (0,S) containing no event time of y, with v>0. No smoothness across an event time is assumed.

Set

 h(v,t,S,y)=partial_v log beta_t(v;y),    0<=t<=S,

and define h(v,t,S,y)=0 for S<t<=T. In particular, beta_S(v;y)=1 and h(v,S,S,y)=0.

Let G be the completed, right-continuous initial enlargement of F by sigma(Y): for t<T, take the completion of

 G_t=intersection_{t<u<=T}(F_u vee sigma(Y)),

and at T take the completion of F_T vee sigma(Y).

## Task

Prove that there exists a G-Brownian motion W-tilde under the joint law such that, on [0,T],

 dV_t=[a(V_t,t)+1_{t<=S}c(V_t,t)^2 h(V_t,t,S,Y)]dt+c(V_t,t)dW-tilde_t,

with V_0=v_0. Explain why this gives the same SDE representation under the conditional law given Y=y for the law of Y-almost every y.

Thus conditioning on the complete point-process observation leaves the diffusion coefficient unchanged and adds exactly the displayed future-observation score drift.
