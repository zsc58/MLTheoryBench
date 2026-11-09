# Problem

## Setup

Fix an integer K>=2 and the probability simplex Delta^{K-1}={p in R^K: p_k>=0, sum_k p_k=1}. Let Q be any probability law on this simplex and let P~Q. Write mu_k=E[P_k] and v_k=Var(P_k). Define

C_k(Q) = v_k/(2 mu_k) when mu_k>0, and C_k(Q)=0 when mu_k=0, and define the aggregate EU(Q)=sum_{k=1}^K C_k(Q). (The zero-mean convention is justified by simplex nonnegativity.)

Use the following axioms for a scalar uncertainty functional on laws over the simplex:

- A0 (non-negativity): EU(Q)>=0.
- A1 (certainty): EU(Q)=0 exactly when Q is a point mass.
- A2 (uniform maximality): the uniform law U on Delta^{K-1} is a maximizer of EU among all such laws.
- A3 (strict mean-preserving-spread monotonicity): whenever Q' admits a coupling P'=P+Z with P~Q, P'~Q', both simplex-valued, E[Z|P]=0, and Z nonzero in variance in at least one coordinate, one has EU(Q')>EU(Q).
- A5 (spread-preserving location-shift invariance): whenever Q' is obtained by a deterministic translation P'=P+d that remains simplex-valued and therefore preserves every coordinate variance, EU(Q')=EU(Q).

## Task

Prove that EU satisfies A0, A1, and A3, while it violates A2 and A5. In addition, establish the coordinate bound C_k(Q)<=1/2(1-mu_k) for mu_k>0 and explain why this bound does not vanish as mu_k approaches 0.
