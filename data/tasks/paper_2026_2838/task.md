# Problem

## Setup

For each integer d>=1, let X_d={0,1}^d and let H_d be a class of Boolean functions on X_d. For any Boolean function h:X_d->{0,1}, write supp(h)={x in X_d:h(x)=1}. A finite positive sample is a set S subseteq X_d for which

V(S)={h in H_d:S subseteq supp(h)}

is nonempty.

The sequence H=(H_1,H_2,...) is learnable in the one-sided positive-only membership-query model if there exist a possibly randomized learner L and a polynomial m such that the following holds for every d>=1, every epsilon,delta in (0,1), every target h* in H_d, and every probability distribution D on X_d supported on supp(h*). Given d, epsilon,delta and access to an oracle providing independent samples from D and an oracle returning h*(x) for queried points x in X_d, L makes at most m(d,1/epsilon,1/delta) calls to each oracle. With probability at least 1-delta over the examples and its internal randomness, it outputs a Boolean function h:X_d->{0,1} satisfying

supp(h) subseteq supp(h*) and D({x in X_d:h(x)=0})<=epsilon.

The output need not belong to H_d, and there is no running-time requirement. Queries may depend on the learner's internal randomness and on examples and query answers already observed; the learner is not otherwise given the unknown target or distribution.

For a realizable S, a deterministic adaptive query strategy Sigma_S is a finite rooted binary tree whose internal nodes are labeled by points of X_d and whose two outgoing branches correspond to answers 0 and 1. The tree may depend on d, H_d, and S; its realized path depends on membership answers. A transcript r is the complete response sequence on a root-to-leaf path. It is realizable for S if some h in V(S) induces that path when Sigma_S is run against h. Let

W_Sigma(r)={h in H_d:h induces r when Sigma_S is run against h},

without requiring h to contain S. The strategy is an adaptive-query compression scheme for S if every transcript r realizable for S satisfies

S subseteq intersection_{h in W_Sigma(r)} supp(h).

Its size is its maximum number of queries over all root-to-leaf paths. A tree of depth zero is allowed.

## Task

Prove the following characterization: H is learnable in the one-sided positive-only membership-query model exactly if there exists a polynomial p such that, for every d>=1 and every finite realizable positive sample S subseteq X_d, S admits an adaptive-query compression scheme of size at most p(d).
