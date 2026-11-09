# Problem

## Setup

Let (S,A,P,r,gamma) be a finite discounted Markov decision process with nonempty state and action sets S and A: 0 <= gamma < 1, r:S x A -> R is bounded, and P(.|s,a) is a probability distribution on S. For a bounded value function V:S -> R, define

(TV)(s) = max_{a in A} [ r(s,a) + gamma sum_{s' in S} P(s'|s,a)V(s') ].

Write ||.||_infty for the sup norm on the relevant finite state space, and let V* be the fixed point of T.

Choose finite abstract sets Sbar and Abar and stochastic kernels nu_S(sbar|s), nu_A(abar|s,a), eta_S(s|sbar), eta_A(a|sbar,abar). Define the joint encoder and decoder by

nu(sbar,abar|s,a) = nu_S(sbar|s) nu_A(abar|s,a),
eta(s,a|sbar,abar) = eta_S(s|sbar) eta_A(a|sbar,abar).

For each sbar in Sbar, define

Abar(sbar) = { abar in Abar : there exist s in S and a in A with nu(sbar,abar|s,a) > 0 }.

Define the induced abstract reward and transition by

rbar(sbar,abar) = sum_{s,a} r(s,a) eta(s,a|sbar,abar),
Pbar(sbar'|sbar,abar) = sum_{s,a,s'} nu_S(sbar'|s') P(s'|s,a) eta(s,a|sbar,abar).

Define lifting and grounding by

(LV)(sbar) = sum_s V(s) eta_S(s|sbar),
(Gamma Vbar)(s) = sum_sbar Vbar(sbar) nu_S(sbar|s).

Let V be a collection of bounded functions on S. A pseudometric d_V on S x A is Bellman-compatible with V if, for every V0 in V and all (s,a),(u,b) in S x A,

 d_V((s,a),(u,b)) >= | r(s,a) + gamma sum_{s' in S} P(s'|s,a)V0(s') - r(u,b) - gamma sum_{u' in S} P(u'|u,b)V0(u') |.

Fix a pseudometric d_V on S x A that is Bellman-compatible with V.

Define the deformed abstract operator

(Tbar_dagger Vbar)(sbar) = sum_s eta_S(s|sbar) (T Gamma Vbar)(s).

The encoder-decoder state round trip is

kappa_S(u|s) = sum_sbar eta_S(u|sbar) nu_S(sbar|s).

For s,u in S define

D_H(s,u) = max { sup_{a in A} inf_{b in A} d_V((s,a),(u,b)), sup_{b in A} inf_{a in A} d_V((s,a),(u,b)) },

Delta_H(kappa_S;d_V) = sup_{s in S} sum_{u in S} kappa_S(u|s) D_H(s,u).

## Task

Prove that for every bounded abstract value function Vbar such that Gamma Vbar belongs to V,

||Gamma Vbar - V*||_infty <= 1/(1-gamma) [ ||Tbar_dagger Vbar - Vbar||_infty + Delta_H(kappa_S;d_V) ].
