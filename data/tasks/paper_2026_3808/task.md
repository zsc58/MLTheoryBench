# Problem

## Setup

Consider a finite-state, finite-action, undiscounted Markov decision process. Let S be its state set, let A_s be the nonempty finite set of admissible actions at state s, and let A be the union of these action sets. There is a unique goal state s^g, whose sole action a^g has zero reward and transitions to s^g with probability one.

For each admissible state-action pair, let p(s'|s,a) be its transition probabilities. For each non-goal admissible pair, let bar r_{s,a} in R be its finite expected reward.

A deterministic stationary policy pi selects pi(s) in A_s at every state. It is proper if, from every starting state s, the probability of being at s^g at time t under pi tends to one as t tends to infinity; otherwise it is improper. A state s is recurrent under pi if, starting at s and following pi, the probability of returning to s at some strictly positive time is one. Assume that at least one improper deterministic stationary policy exists.

Let I = {(s,a): s in S minus {s^g}, a in A_s} and d = |I|. A parameter theta in R^d has one coordinate theta_{s,a} for each pair in I. Define Q_theta(s,a) = theta_{s,a} for (s,a) in I and Q_theta(s^g,a^g) = 0.

For each (s,a) in I, define

 g_{s,a}(theta) = theta_{s,a} - sum_{s' in S minus {s^g}} p(s'|s,a) max_{b in A_{s'}} theta_{s',b}.

A dataset D is a finite list of observations (s,a,r), with (s,a) in I and r in R; repetitions and the empty list are allowed. For epsilon > 0, define

 L_hat_epsilon(theta|D) = product over observations (s,a,r) in D of [(2 pi epsilon^2)^(-1/2) exp(-(r - g_{s,a}(theta))^2/(2 epsilon^2))],

where the empty product is 1.

For a deterministic stationary policy pi, let

 O^pi = {theta in R^d: theta_{s,pi(s)} >= theta_{s,a} for every non-goal s and every a in A_s}.

Let D^full contain exactly one observation (s,a,bar r_{s,a}) for each (s,a) in I. All integrals below use d-dimensional Lebesgue measure.

## Task

Prove that there exist a non-goal state s^r that is recurrent under a deterministic stationary policy, an improper deterministic stationary policy phi, and a nonzero vector u in R^d such that both of the following hold:

1. For every theta in O^phi, every c > 0, every epsilon > 0, and every finite dataset D,

   L_hat_epsilon(theta + c u | D) = L_hat_epsilon(theta | D).

2. For every epsilon > 0 and every finite dataset D,

   integral over O^phi of L_hat_epsilon(theta|D) dtheta = infinity.

Moreover, prove that for every proper deterministic stationary policy mu and every epsilon > 0,

 integral over O^mu of L_hat_epsilon(theta|D^full) dtheta < infinity.
