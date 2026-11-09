# Problem

## Setup

Let X be an input space and let P and Q be probability distributions on X. A finite rooted binary decision tree has internal split nodes C and leaves L. Each leaf l has a fixed real prediction a_l, and the tree function f takes value a_l on inputs reaching l. Write mu_P=E_P[f] and mu_Q=E_Q[f].

For every split node c, let g_{2,c} be the event that an input reaches c and let g_{1,c} be the designated outgoing-branch event at that split. Assume the conditional probabilities p_c=P(g_{1,c}|g_{2,c}) and q_c=Q(g_{1,c}|g_{2,c}) are defined and lie in [0,1]. For each subset S of C, let widehat P_S be the probability distribution on the leaf set L induced by assigning designated-branch probability q_c at node c when c is in S and p_c otherwise. Define

mu_hat_S = sum over l in L of widehat P_S(l) a_l.

For c in C define

phi_c=sum over S subset C minus {c} of |S|!(|C|-|S|-1)!/|C|! times (mu_hat_{S union {c}}-mu_hat_S).

## Task

Prove that the prediction shift is exactly decomposed by these split-node attributions:

sum over c in C phi_c = mu_Q - mu_P.

Your proof must cover the stated mixed-intervention construction and all parameter choices S subset C under the assumptions above.
