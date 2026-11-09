# Reference Proof

## Proof Structure

Derive and globally verify the KL-prior optimizer, bound its normalizer after a score shift, and then take the low-signal limit with the prior and sequence length fixed. Analyze the uniform and positive-margin cases separately, quantify the length-uniform consequence, and prove the fixed-weight value-perturbation inequality.

## Contract and Source Dependencies

The scores in the stability analysis are temperature-normalized: a_j=s_j/tau. The source's earlier Shannon-regularized calculation is the optimizer dependency used by the KL-prior calculation; both are covered explicitly below, with no external theorem left to invoke. The sensitivity comparisons retain the source's condition L<T for a period T of positive prior weights. The period and prior may vary between different lengths. No period enters the algebraic estimates, but the proof applies in particular to all instances satisfying that condition. A designated key in the uniform comparison need not be a strict logit maximizer.

## Complete Proof

### 1. The optimizer, including boundary cases

Let S={j:pi_j>0}. This set is nonempty because the prior has total mass one. For a feasible distribution q supported on S, write

F(q)=-sum_{j in S}q_j s_j+tau sum_{j in S}q_j log(q_j/pi_j),

using 0 log(0/pi_j)=0. Expanding gives

F(q)=tau sum_{j in S}q_j log q_j-tau sum_{j in S}q_j(a_j+log pi_j).

At a positive stationary point, a multiplier lambda for the mass constraint gives

-s_j+tau(log(q_j/pi_j)+1)+lambda=0.

Solving these equations and normalizing produces the candidate

r_j=pi_j exp(a_j)/Z for j in S,

where Z=sum_{k in S}pi_k exp(a_k), and r_j=0 outside S. Since the scores are finite and S is nonempty, Z is finite and strictly positive, and r is feasible and positive on S.

We verify global optimality rather than assuming that a minimizer is interior. For every feasible q,

F(q)-F(r)=tau sum_{j in S}q_j log(q_j/r_j).

For a fixed r>0, the function g(x)=x log(x/r)-x+r for x>0 has derivative log(x/r), decreases up to x=r, and increases afterwards. Its continuous extension at zero is g(0)=r. Hence g(x)>=0 for every x>=0, with equality only at x=r. Summing this inequality with r=r_j and using sum q_j=sum r_j=1 proves F(q)>=F(r), with equality only when q=r. Thus the optimizer exists, is unique, and equals r, including when S has one element.

For a uniform prior, the KL objective differs from the Shannon-regularized objective by the constant tau log L. The same calculation therefore also establishes the earlier Shannon optimizer used in the source dependency chain.

### 2. Multiplicative bounds and collapse

Shift the normalized scores by their minimum: a'_j=a_j-min_k a_k. Then 0<=a'_j<=omega. The optimizer formula is unchanged because the common exponential factor cancels. Its shifted normalizer satisfies

1<=Z'=sum_k pi_k exp(a'_k)<=exp(omega),

and its numerator satisfies

pi_j<=pi_j exp(a'_j)<=pi_j exp(omega).

Combining these bounds gives

pi_j exp(-omega)<=p_j<=pi_j exp(omega).

For a zero prior coordinate both bounds and p_j are zero. At fixed L, tau, and pi, the squeeze theorem gives p_j->pi_j along every score sequence for which omega->0. In particular, because the sum defining context sensitivity is finite,

lim_{omega->0}Psi(C)=1-pi_{j*}.

### 3. Uniform-prior comparison and order of limits

For each fixed L, a uniform prior has pi_{j*}=1/L. Therefore

lim_{omega->0}Psi(C)=(L-1)/L.

Taking the length limit afterwards gives

lim_{L->infinity} lim_{omega->0}Psi(C)=1.

These are limiting identities, not assertions that arbitrary nonconstant scores give uniform attention. The periodicity condition is compatible with this family: constant weights have every positive T as a period, so for each L a period T>L may be used.

### 4. Positive prior margin

Assume all prior coordinates are positive, and let delta=min_{k in C}(K_{j*}-K_k)>0 with K_j=log pi_j. Then

pi_{j*}=1/[1+sum_{k in C}exp(K_k-K_{j*})]

and each summand in the denominator is at most exp(-delta). Consequently,

pi_{j*}>=1/[1+(L-1)exp(-delta)].

Taking its complement and using the fixed-length low-signal limit yields

lim_{omega->0}Psi(C)<= (L-1)/(exp(delta)+L-1).

Normalization of periodic weights changes their log weights by a common constant, so it does not alter this margin. No further property of the weight function is needed for the inequality.

### 5. Length-uniform meaning of logarithmic growth

Consider a family of admissible positive priors with positive margins delta_L and suppose delta_L>=log L+b, where b is independent of L. Then exp(delta_L)>=L exp(b), so

lim_{omega->0}Psi(C)<= (L-1)/(L exp(b)+L-1)<=1/(1+exp(b))<1.

The last upper bound depends on b but not on L. Thus the limiting sensitivity is uniformly separated from one. Increasing b makes this upper bound arbitrarily small. This is a sufficiency statement, not a necessity claim and not a claim that every positive constant multiple of log L suffices.

### 6. Fixed-weight value perturbations

Hold scores, temperature, prior, and hence attention weights fixed. For epsilon>=0 and context values in R^d satisfying ||v'_k-v_k||_2<=epsilon, the triangle inequality and nonnegativity of p_k give

||sum_{k in C}p_k v'_k-y_C||_2
=||sum_{k in C}p_k(v'_k-v_k)||_2
<=sum_{k in C}p_k||v'_k-v_k||_2
<=epsilon sum_{k in C}p_k
=epsilon Psi(C).

This holds at every score vector, not only in the low-signal limit. All theorem-critical obligations are closed.
