# Problem

## Setup

Let T be a positive integer. Let Theta and X be nonempty standard Borel decision and instance spaces, and let ell: Theta x X -> [0,1] be measurable. Fix an arbitrary multiset M of T instances before the experiment, and present its occurrences in a uniformly random order, independently of the learner's randomization. Write x_t for the round-t instance, X_t for the prefix multiset, and X_0 for the empty multiset.

For every nonempty finite multiset Y, assume that theta -> sum_{x in Y} ell(theta,x) attains its minimum. Define

`OPT(Y)=min_{theta in Theta} sum_{x in Y} ell(theta,x)`,

`OPT(empty)=0`, `OPT_t=OPT(X_t)`.

Assume that Y -> OPT(Y) is measurable on multisets of each fixed size, equipped with the quotient sigma-algebra from tuples. All multiset sums and deletions count occurrences, so Y minus {x} removes exactly one occurrence.

Let {A_epsilon}_{epsilon in (0,1]} be randomized offline algorithms with output in Theta. Their output laws form a jointly measurable probability kernel in (epsilon,Y) on finite multisets, including the empty multiset, on which a fixed measurable convention is used. The family may depend on the known horizon T.

For probability measures on Theta, define

`TV(P,Q)=sup_{B measurable} |P(B)-Q(B)|`.

For an input multiset Y of size t>=1, the average sensitivity of A_epsilon is

`(1/t) sum_{x in Y} TV(A_epsilon(Y),A_epsilon(Y minus {x}))`.

Let phi:[0,infinity) -> [0,infinity] be proper and lower-semicontinuous, with nonempty effective domain

`dom(phi)={epsilon>=0: phi(epsilon)<infinity} subset (0,1]`,

and assume `lim_{epsilon down to 0} phi(epsilon)=infinity`. The function phi may depend on T.

Let c>=0 be finite and independent of T, t, epsilon, and Y, although it may depend on fixed problem parameters. For every 1<=t<=T, every multiset Y of size t, and every epsilon in (0,1], assume

`(1/t) E_{theta~A_epsilon(Y)}[sum_{x in Y} ell(theta,x)] <= (1+epsilon)OPT(Y)/t+c/T`,

and assume the average sensitivity is at most `phi(epsilon)/(2t)`.

For u>0, define

`phi*(u)=inf_{epsilon>=0} {u epsilon+phi(epsilon)}`,

and let epsilon_min(u) be a minimizer chosen by a fixed deterministic tie-breaking rule. Fix lambda>0 before the random permutation and define, for every finite multiset Y,

`epsilon_Y=epsilon_min(OPT(Y)+lambda)`.

Suppose there is a finite constant C_pc>=0 such that, for every multiset Y with |Y|>=2,

`(1/|Y|) sum_{x in Y} TV(A_{epsilon_Y}(Y minus {x}),A_{epsilon_{Y minus {x}}}(Y minus {x}))`

`<= (C_pc epsilon_Y/(2|Y|)) sum_{x in Y}[OPT(Y)-OPT(Y minus {x})]`.

The constant C_pc may depend on T, lambda, and problem parameters, but not on Y.

The online learner chooses a fixed arbitrary theta_1 in Theta before observing x_1. At round t it plays theta_t, then observes x_t and incurs ell(theta_t,x_t). For t<T, after this observation it draws

`theta_{t+1} ~ A_{epsilon_{X_t}}(X_t)`

using fresh learner randomness independent of the permutation. Thus the round-t prediction cannot depend on x_t before x_t is revealed. Define its expected regret by

`R_T=E[sum_{t=1}^T ell(theta_t,x_t)-OPT_T]`.

## Task

Prove

`R_T <= H_T phi*(OPT_T/H_T+lambda) + C_pc[phi*(OPT_T+lambda)-phi*(lambda)] + O(1)`,

where `H_T=sum_{t=1}^T 1/t`. The additive constant is independent of T and M when c is fixed. The expectation is over the uniform random order and learner randomness.
