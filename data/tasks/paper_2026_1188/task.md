# Problem

## Setup

Let N = {1,2,...}. A charge on N is a finitely additive probability measure defined on every subset of N. It is diffuse if every singleton has charge zero. For A subset of N, its asymptotic density, when it exists, is

 d(A) = lim_{m→∞} |A intersect {1,...,m}|/m.

A diffuse charge is a frequency charge if it assigns d(A) to every set A whose asymptotic density exists. Every frequency charge is translation invariant: phi(A)=phi(A+1), where A+1={a+1:a in A}.

Fix any frequency charge phi. Let Delta^f be the space of all probability charges on N, equipped with the topology of pointwise convergence on subsets of N; assume this space is compact Hausdorff.

Let E_0={2k-1:k>=1} be the odd stages and, for n>=1, let E_n={2^n k:k>=1}. For every A subset of N, define

mu_0(A)=2 phi(A intersect E_0),
mu_n(A)=2^n phi(A intersect E_n) for n>=1.

Choose any tail accumulation point mu_* of (mu_n)_{n>=1}, meaning a pointwise limit of a subnet whose indices tend to infinity, and set mu=(mu_0+mu_*)/2. All these charges are diffuse.

For a charge lambda and a simple function s=sum_{i=1}^m c_i 1_{A_i}, where {A_1,...,A_m} is a finite partition of N, define

integral s d lambda = sum_{i=1}^m c_i lambda(A_i).

For any bounded real function f on N, define integral f d lambda as the supremum of integral s d lambda over all simple functions s<=f.

Consider the infinite-horizon deterministic MDP with states {1,2,3}, initial state 1, and actions T and B in state 1 and a single action in states 2 and 3. From state 1, T gives reward 1 and moves to state 2, while B gives reward 0 and moves to state 3. The unique action in state 2 gives reward 0 and returns to state 1; the unique action in state 3 gives reward 1 and returns to state 1. Thus decisions occur at odd stages.

A history at stage t is a finite sequence (s_1,a_1,...,s_{t-1},a_{t-1},s_t), starting with s_1=1, with each action available in its state. A behavioral strategy assigns to every history a probability distribution on the actions available in the current state; pure strategies are the degenerate case. For a strategy sigma, let q_t=E_sigma[r_t] be its expected reward at stage t. Its payoff is

u_mu(sigma) = integral q_t d mu,

and the value is v_mu = sup_sigma u_mu(sigma), with the supremum over all behavioral strategies. An optimal strategy attains this supremum.

## Task

Prove that for this MDP and aggregation charge mu, v_mu=1, but no behavioral strategy, pure or randomized, attains the value.
