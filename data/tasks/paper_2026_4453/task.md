# Problem

## Setup

Fix a query, an integer L>=2, a temperature tau>0, and a prior distribution pi=(pi_1,...,pi_L), where pi_j>=0 and sum_j pi_j=1. Let s=(s_1,...,s_L) be a vector of real content scores and write a_j=s_j/tau.

Set S={j:pi_j>0} and

Delta(S)={q in R^L: q_j>=0, sum_j q_j=1, and q_j=0 for j not in S}.

Attention probabilities p are defined as the unique minimizer over Delta(S) of

  -sum_j q_j s_j + tau KL(q||pi),

where

  KL(q||pi)=sum_{j in S}q_j log(q_j/pi_j),

with each term having q_j=0 interpreted as zero. All logarithms are natural.

Choose a designated key j* in {1,...,L}, put C={1,...,L}\{j*}, and define the context sensitivity

  Psi(C)=sum_{k in C}p_k=1-p_{j*}.

When all prior coordinates are positive, define K_j=log pi_j and the prior margin

  delta=min_{k in C}(K_{j*}-K_k).

For the sensitivity comparisons below, assume the prior is obtained from a positive periodic weight function w:R->(0,infinity): there is a period T>L such that w(x+T)=w(x) for every real x, and

  pi_j=w(j)/sum_{k=1}^L w(k).

Here T need not be the least positive period. In comparisons across lengths, the prior, weight function, period, and designated key may depend on L, with T>L at each length.

Let d>=1 be an integer, let the context values v_k belong to R^d, and use the Euclidean norm ||.||_2. Define y_C=sum_{k in C}p_k v_k.

## Task

Prove the following integrated theorem.

For every score vector, with omega=max_j a_j-min_j a_j,

  pi_j exp(-omega) <= p_j <= pi_j exp(omega)  for all j.

Consequently, p_j tends to pi_j for every j as omega tends to zero. This assertion is to hold along every sequence of score vectors whose normalized dynamic ranges tend to zero, with L, tau, and pi fixed. All low-signal limits below have this same meaning.

For the sensitivity comparisons:

1. If pi_j=1/L for every j, then

     lim_{omega->0} Psi(C)=(L-1)/L,

   and hence

     lim_{L->infinity} lim_{omega->0} Psi(C)=1.

2. If delta>0, then

     lim_{omega->0} Psi(C) <= (L-1)/(exp(delta)+L-1).

   In particular, for any family of such priors with positive margins delta_L, show that a condition

     delta_L >= log L+b

   for a real constant b independent of L suffices to keep the low-signal limiting sensitivity uniformly bounded away from one, with a bound that may depend on b but not on L.

Finally, for arbitrary scores and any epsilon>=0, hold the scores, temperature, and prior fixed. Prove that replacing each context value by v'_k in R^d with ||v'_k-v_k||_2<=epsilon gives

  ||sum_{k in C}p_k v'_k-y_C||_2 <= epsilon Psi(C).
