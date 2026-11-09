# Problem

## Setup

Let d be a positive integer, let X=R^d with its Euclidean metric and Borel sigma-algebra, let p and q be probability measures on X, and fix theta in X. Write B_r(theta)={x in X: ||x-theta||<r}. Assume p(B_r(theta))>0 and q(B_r(theta))>0 for all sufficiently small r>0. Fix alpha in (0,1).

Let q=q_ac+q_s be the Lebesgue decomposition relative to p, with q_ac absolutely continuous with respect to p and q_s singular to p. For u>=0 define

f_alpha(u)=(u^alpha-alpha u+alpha-1)/(alpha-1).

For a Borel set E define

D_alpha^E(q||p)=integral_E f_alpha(dq_ac/dp) dp + [alpha/(1-alpha)] q_s(E).

For p(E)>0 set Dbar_alpha^E(q||p)=D_alpha^E(q||p)/p(E). Define D_alpha^E(p||q) by interchanging p and q, and for q(E)>0 set Dbar_alpha^E(p||q)=D_alpha^E(p||q)/q(E). Let m_p(r)=p(B_r(theta)) and m_q(r)=q(B_r(theta)).

All asymptotic comparisons below are as r decreases to zero through positive values. For nonnegative functions h and g, h=O(g) means h(r)<=C g(r) for some C>0 and all sufficiently small r; h=Omega(g) means h(r)>=c g(r) for some c>0 and all sufficiently small r.

For the gauge sets below, use the conventions inf(empty set)=+infinity and sup(empty set)=0. Infima and suprema of nonempty sets are taken in the extended real numbers.

For a probability measure mu on X, define

U_pow(mu)={eta>0: mu(B_r(theta))=O(r^(1/eta))},

L_pow(mu)={eta>0: mu(B_r(theta))=Omega(r^(1/eta))}.

Its upper and lower power indices are d inf U_pow(mu) and d sup L_pow(mu), respectively. When they agree, denote their common value by MI_pow(mu,theta), allowing values zero and +infinity.

If MI_pow(mu,theta) exists and 0<MI_pow(mu,theta)<infinity, set a_mu=d/MI_pow(mu,theta) and define

U_log(mu)={eta in R: mu(B_r(theta))=O(r^a_mu(-log r)^eta)},

L_log(mu)={eta in R: mu(B_r(theta))=Omega(r^a_mu(-log r)^eta)}.

The logarithmic gauges are evaluated for 0<r<1. The upper and lower logarithmic indices are inf U_log(mu) and sup L_log(mu), respectively. When these agree, denote their common value by MI_log(mu,theta). The logarithmic index is defined only when the power index is finite and strictly positive.

## Task

Assume MI_pow(p,theta) and MI_pow(q,theta) both exist. Prove:

1. If limsup_{r->0} Dbar_alpha^{B_r(theta)}(q||p)<1, then MI_pow(q,theta)=MI_pow(p,theta). If MI_log(p,theta) exists, then MI_log(q,theta) exists and equals it.

2. If limsup_{r->0} Dbar_alpha^{B_r(theta)}(p||q)<infinity, then MI_pow(q,theta)>=MI_pow(p,theta). If the power indices are equal and both logarithmic indices exist, then MI_log(q,theta)>=MI_log(p,theta).
