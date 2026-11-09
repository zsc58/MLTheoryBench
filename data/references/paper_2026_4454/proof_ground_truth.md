# Reference Proof

This is a proof conditional on the PU primitive explicitly assumed in the problem. No independent proof of that specialized external guarantee is asserted.

## 1. Lower-bound construction and VC dimension

Fix n>=2, d>=2, and alpha in (1/2,1). Write e_1 for the first coordinate vector in R^(d-1). Put probability 1/n at 0 and probability (1-1/n)/2 at each of -e_1 and e_1. Take the target h*(x)=1{x_1>=1/2}. Its labels on these three points, in increasing first-coordinate order, are (0,0,1).

The class of affine halfspaces in R^(d-1), including constants, has VC dimension d. For completeness, d affinely independent points can be assigned arbitrary real scores of signs prescribed by any binary labeling, using an affine function, so they are shattered. Conversely, any d+1 points have a nonzero affine dependence sum_i a_i x_i=0 and sum_i a_i=0. Its nonzero coefficients include both signs. Label points with positive coefficients one and those with negative coefficients zero. A realizing affine score would make sum_i a_i(<w,x_i>+b)>0, since positive coefficients multiply nonnegative scores and negative coefficients multiply strictly negative scores. This contradicts the affine dependence. Thus d+1 points cannot be shattered.

Let E be the event that the initial sample contains both outer points and no middle point. Then

Pr(E)=(1-1/n)^n(1-2^(1-n))>=1/8.

Indeed, (1-1/n)^n is increasing for n>=2 and equals 1/4 at n=2; this monotonicity follows by differentiating x log(1-1/x), whose derivative is -log(1+1/(x-1))+1/(x-1)>=0. The other factor is at least 1/2.

On E, the observed labels at -e_1 and e_1 are zero and one. For any nonzero w, their minimum normalized signed margin is

(w_1-|b|)/||w||<=1.

Equality requires b=0 and w a positive multiple of e_1. Hence every maximum-margin choice labels 0 as one, incorrectly. This explicitly accounts for the public convention that points on the boundary receive label one.

## 2. Random-walk persistence

Enumerate future visits to 0 and expose their independent label-source coins. Let W_s be the number of model-source coins minus natural-source coins among the first s such visits. These coins are independent of E and have the stated alpha-biased walk law. Let F={W_s>=1 for every s>=1}.

On E intersect F, induction over complete rounds proves that every deployed classifier has support labels (0,1,1). The base case was just proved. If no middle point has appeared by a later round, all accumulated labels are the correct outer labels and maximum-margin selection again has this pattern. Otherwise, the induction hypothesis implies that every outer observation has its correct label, regardless of its source, while the middle point has strictly more labels one than zero. The pattern (0,1,1) is realizable by an affine halfspace and attains the separate minimum empirical error at each support point. Any classifier changing an outer label or the strict-majority middle label has strictly larger total empirical error. Thus every empirical-risk minimizer has that pattern, even if contradictory middle labels make the accumulated sample nonseparable. This induction uses the classifier from the previous round to generate every label in the current batch; it does not update within a batch.

We also verify c_alpha=Pr(F)>0. The probability of a return to zero at time 2s is binom(2s,s)alpha^s(1-alpha)^s<=[4alpha(1-alpha)]^s, and returns at odd times are impossible. The sum is finite. The first Borel-Cantelli lemma therefore implies finitely many returns almost surely. If the probability of a first return were one, independent increments, equivalently the strong Markov property at successive return times, would imply infinitely many returns almost surely. Thus the probability of no return is positive.

To justify its positive-side contribution without comparing individual infinite paths, fix a finite horizon m. Reflection pairs paths staying strictly negative through m with paths staying strictly positive through m. A positive path has u>v positive and negative increments, so its probability alpha^u(1-alpha)^v is at least the reflected probability alpha^v(1-alpha)^u. Summing over the finite path sets and then taking decreasing-event limits gives Pr(stays positive forever)>=Pr(stays negative forever). These two events partition no return. Therefore c_alpha is at least half the positive no-return probability.

Consequently, for every round t>=0,

E[L(h_t)]>=Pr(E)Pr(F)/n>=c_alpha/(8n),

which implies the required liminf statement.

## 3. An implementable fixed-classifier update

For recovery write beta=1-alpha>0. First suppose d>=1. Condition on all history up to the deployment of a fixed binary classifier g. It need not belong to H. Hold it fixed throughout the collection of the observations used in this update.

For each observation set Z=Y xor g(X). With q=L(g), acceptance Z=1 has probability beta q. If q>0, the conditional law of an accepted covariate is P conditioned on (g xor h*)(X)=1. Conditional on the acceptance indicator vector, the accepted covariates are independent and have this same law. In particular, conditional on obtaining at least p accepted observations, the first p accepted covariates are i.i.d. from that conditional distribution. Reserve a separate, predetermined block of u fresh covariates; it remains independent and i.i.d. from P, including after conditioning on the acceptance-count event.

On every finite set of points, XOR with g is a bijection on the possible label vectors. Hence the class g xor H has VC dimension d and contains target g xor h*.

Fix 0<e<=1/2 and 0<delta<1. Let

p=m_P(e,delta/2),  u=m_U(e,delta/2),

m=ceil(8p log(2/delta)/(beta e)).

Use the first m observations for acceptance and the next u only as unlabeled covariates. If at least p acceptances occur, invoke the PU primitive on the first p accepted covariates and the u reserved covariates for class g xor H, obtaining a binary classifier a, and return a xor g. Otherwise return g. The algorithm branches only on an observed count; it never queries L(g).

The following two cases are solely for analysis. If q<=e, retention already succeeds, while a PU invocation fails with probability at most delta/2. If q=0, acceptance never occurs and no conditional positive distribution is needed. If q>e, the acceptance count N is binomial with mean mu=m beta q>=m beta e. Since p<=mu/2, the standard multiplicative Chernoff inequality gives

Pr(N<p)<=Pr(N<=mu/2)<=exp(-mu/8)<=exp(-p log(2/delta))<=delta/2.

Here the audited inequality is: for independent Bernoulli variables of common parameter r and mean sum mu, Pr(sum<=(1-gamma)mu)<=exp(-gamma^2 mu/2), 0<=gamma<=1. Its independence hypotheses hold conditionally on the fixed history. We may take the primitive's sufficient sample counts to be positive integers, increasing them to one if necessary.

On invocation, the primitive succeeds with conditional probability at least 1-delta/2. Pointwise,

(a xor g)(x)!=h*(x) if and only if a(x)!=(g xor h*)(x).

Thus the update has loss at most e with probability at least 1-delta in either case, without any hypothesis on the incoming loss q.

## 4. A uniform sufficient budget

Set delta=e. From the assumed sample bounds and integer rounding, there is a universal constant K>=1 such that, for every dyadic e<=1/2, the integer budget

R(e)=ceil(K d log^2(4/e)/(beta e^2))

is at least m+u for the preceding update. Extra observations can simply be ignored. Every such update has expected loss at most e+delta=2e. Conditional guarantees given the incoming history imply the same unconditional bound.

We choose this explicit upper-budget function, not an unspecified minimal sample-complexity function. It is increasing as e decreases, and its unrounded value grows by a factor greater than four when e is halved.

## 5. Initialization from the available natural batch

Choose a fixed a_0 in H, independently of the unknown P and h*. If there is a dyadic e in {1/2,1/4,...} with R(e)<=n, let e_0 be the smallest such e. Otherwise set e_0=1.

If e_0=1, let g_0=a_0. Otherwise initialize using the update above with incoming classifier a_0, error target e_0, and only the initial true-labeled batch. To reproduce its input law, independently draw Bernoulli(beta) variables B_i and use acceptance indicators B_i(Y_i xor a_0(X_i)); reserve the prescribed disjoint covariate block. These are exactly the accepted-positive and unlabeled distributions required by the preceding update. This is an implementable use of known true labels from round zero, not access to the target elsewhere. It uses at most R(e_0)<=n observations.

In both cases E[L(g_0)]<=2e_0, with the trivial bound one covering e_0=1. Output h_0=g_0. No extra data have been supplied.

## 6. Epoch timing, batching, and the all-round rate

For k>=1 set e_k=e_0 2^(-k), r_k=ceil(R(e_k)/n), T_0=0, and T_k=sum_{j=1}^k r_j. For rounds T_{k-1}+1 through T_k, collect observations generated by g_{k-1}. Output g_{k-1} after every nonfinal round of this block. After receiving the final batch at T_k, apply the update to this block and output g_k. Thus h_t=g_{k-1} for T_{k-1}<=t<T_k, and h_{T_k}=g_k. In particular, every batch used in an update was generated by the very classifier used in that update's XOR transformation.

The update guarantee gives E[L(g_k)]<=2e_k for every k>=0. By the definition of e_0, every subsequent R(e_k)>n. Hence r_k<=2R(e_k)/n; rounding does not introduce an uncontrolled additive number of rounds.

Write A(e)=K d log^2(4/e)/(beta e^2). Since A(e)>=1, R(e)<=2A(e). For j<=k, A(e_j)<=4^{j-k}A(e_k). Therefore

T_k<=2 sum_{j=1}^k R(e_j)/n<=4 sum_{j=1}^k A(e_j)/n<=16 A(e_k)/(3n).

Fix t>=1 and choose k with T_{k-1}<=t<T_k. Then

E[L(h_t)]<=2e_{k-1}=4e_k,

and t<=T_k<=C d log^2(4/e_k)/(beta n e_k^2). It follows that

E[L(h_t)]<=C' log(4/e_k) sqrt(d/(beta nt)).

The logarithm is uniformly controlled. If k>=2, the preceding completed epoch gives R(e_{k-1})<=nT_{k-1}<=nt. Thus 1/e_k=2/e_{k-1}<=2sqrt(beta nt/(Kd))<=2sqrt(nt). The same estimate holds for k=1 when initialization used R(e_0)<=n. In the remaining case k=1 and e_0=1, e_k=1/2 and the logarithm is constant. Consequently log(4/e_k)<=C'' log(e nt) in all cases, proving the requested tilde-O bound with universal constants. An endpoint t=T_k is included by using the next block's index.

Finally, if d=0, any two members of the nonempty class H agree at every point: otherwise that point would be shattered. Outputting any fixed member of H therefore has loss zero at every round. This proves the stated zero-dimensional bound as well.

## Obligation closure

The construction, event probability, margin choice, empirical-majority induction, random-walk survival, XOR-class dimension, conditional sampling laws, observable fallback, initialization, information timing, integer batching, uniform all-round estimate, and d=0 case have all been derived above. The only specialized learning guarantee used is the public PU assumption. The independent probability facts used for walk survival are recorded in theory_017, and the fully stated Chernoff inequality is recorded as standard_independent in theory_016. There are no unresolved conditional proof obligations.
