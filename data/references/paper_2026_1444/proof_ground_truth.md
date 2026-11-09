# Reference Proof

## Scope and Obligations

The targets are almost-sure Bayes consistency under distribution-level label alignment and the existence of an observationally indistinguishable pair with incompatible Bayes decisions, one member aligned. The stronger general minimality assertion in the source is not used.

The theorem-critical obligations are: fixed-query concentration for actual neighbor prefixes, local separation almost everywhere, survival of at least one bag-optimal label and removal of every bag-nonoptimal label, conversion to a high-probability risk bound using alignment only where it holds, passage to almost-sure convergence, and an explicit indistinguishable pair with a quantitative risk contradiction. All are closed below.

Write M_eta(x)=argmax_y eta_y(x) and M_q(x)=argmax_y q_y(x). Define the measurable alignment set

G={x:M_eta(x)=M_q(x)}.

Because the label set is finite and the conditional-probability versions are measurable, G is measurable. The public assumption gives P_X(G)=1. No equality of these maximizer sets is assumed outside G. Conditional-probability versions can differ arbitrarily on a null set, so true-posterior pointwise guarantees below are asserted only on G.

## Standard Results Used

We use the following standard independent results, stated in the supplied source.

1. VC mass implication. For an iid sample of size n and a measurable set class of VC dimension d, there is a universal c0>0 such that, with probability at least 1-delta^2/2, simultaneously for its sets B and integers k,
   P_X(B)>=k/n+(c0/n)max{k,d log(n/delta)} implies #_n(B)>=k.

2. VC conditional-frequency concentration. For iid observations from Q and measurable set families of VC dimensions at most d, with probability at least 1-epsilon,
   |Q(A|B)-Q_n(A|B)|<=sqrt(1000[d log(8n)+log(4/epsilon)]/#_n(B))
   simultaneously over their sets with Q(B)>0 and #_n(B)>0.

3. Differentiation. For any Borel probability measure on a finite-dimensional normed space and every bounded measurable f, its averages over positive-mass balls centered at x converge to f(x) for almost every x as the radius decreases to zero. Extend the instance measure by zero outside the Borel instance subset. The functions eta_y are bounded and measurable, so this result applies to all of them on a common full-measure set.

No specialized unstated result is used.

## Fixed-Query Neighborhoods and Concentration

Fix x. Order observations by (||X_i-x||,U_i), where the independent continuous priorities U_i implement the public distance-tie convention. These keys are distinct almost surely. Define

D_x(r,u)={(z,v):||z-x||<r} union {(z,v):||z-x||=r, v<=u}.

For fixed x this is a nested measurable family and therefore has VC dimension at most one. Its intersection with the fixed event {y in S} also has VC dimension at most one. Apply conditional-frequency concentration on the iid product observations (X_i,S_i,U_i), with epsilon=delta^2/(2m), and take a union bound over labels. Choosing c1 above a universal lower bound gives, with probability at least 1-delta^2/2,

|hat eta_j(y|x)-eta_y(D_j)|<=Delta(n,j,delta)/2

for every neighbor prefix j and label y. Here D_j is the distance-priority neighborhood with empirical count exactly j. These sample-selected neighborhoods have positive population mass almost surely for a fixed query. More explicitly, if R=||X-x|| and F is its distribution function, the population mass of the prefix ending at (R,U) is F(R-)+U[F(R)-F(R-)]; the randomized probability transform is uniform on (0,1). Thus zero-mass selected prefixes occur with probability zero.

For example, the source's numerical choice c1>2 sqrt(8000 log 8) suffices: the concentration numerator is 1000[log(8n)+log(8m/delta^2)], which is bounded by (c1^2/4)[log n+log(m/delta)] for n>=1, m>=2, and 0<delta<1. This numerical bound remains private. Choose the public universal lower bound strictly above this numerical value so that every c1 at least that lower bound is covered.

Apply the mass implication separately to the nested closed balls centered at this fixed x, whose VC dimension is at most one. The two events jointly fail with probability at most delta^2. No simultaneous all-query concentration event is asserted.

For use with tied distances, write O=B(x,r) with its boundary removed and C=B(x,r). After integrating out the independent priority, the population measure of D_x(r,u) is the weighted measure (1-u)P_X restricted to O plus u P_X restricted to C. Consequently, its conditional bag frequencies are a convex combination of the positive-mass open- and closed-ball conditional frequencies. At r=0 they equal eta_y(x) whenever x is an atom. Thus bag-independent partial selection from a distance sphere preserves any common separation possessed by the open and closed balls.

## Salience and Positive Advantage

For 0<p<1 let r_p(x)=inf{r>=0:P_X(B(x,r))>=p}. This radius is finite, and the closed ball at r_p has mass at least p. Define eta_y(B) only for positive-mass balls. A salient pair (p,gamma) has 0<p<=A, 0<gamma<=1, and satisfies

eta_i(B(x,r))-eta_j(B(x,r))>gamma

for every pointwise maximizer i in M_eta(x), every j outside M_eta(x), and every positive-mass ball with 0<=r<=r_p(x). Zero-mass balls impose no condition. Define adv_A(x) as the supremum of p gamma^2 over salient pairs, with value zero if there are no salient pairs, and set it to one when M_eta(x) is the whole label set. The endpoint restrictions p<min(A,1) do not change the supremum: approximate p from below. Advantage is measurable; ball integrals and r_p are measurable, and separation infima can be tested using countably many radii with their right-continuous limits and the measurable endpoint r_p. One may equivalently use nonstrict separation infima and then reduce gamma, which gives the same supremum.

At a differentiation point with a nonempty set of nonmaximizers, let d(x)>0 be the minimum pointwise gap between maximizers and nonmaximizers. Finiteness of the label set makes this minimum positive, even when several labels maximize. Choose r0>0 small enough that every positive-mass closed ball of radius at most r0 has all these gaps at least d(x)/2. Choose a radius strictly inside the range supplied by differentiation. Put

p=min{A/2,P_X(B(x,r0))/2}, gamma=d(x)/4.

The query is a support point almost everywhere, so p>0. We have r_p<=r0 and strict separation by gamma. The radius-zero case at an atom agrees with the pointwise conditional probabilities. Therefore adv_A(x)>=p gamma^2>0. If all labels maximize, advantage is one by definition. Hence adv_A(X)>0 almost surely. This positivity argument concerns eta and does not require pointwise alignment at exceptional queries.

Open balls are increasing limits of smaller closed balls. Whenever they have positive mass and radius at most r_p, their gap is at least gamma. The convex-mixture observation above therefore gives gap at least gamma for all positive-mass distance-priority neighborhoods within r_p.

## Adaptive Elimination

Write L=log n+log(m/delta). Let a>0, and suppose adv_A(x)>a. If every label belongs to M_eta(x), every possible output is bag-optimal, without invoking alignment. Otherwise choose a salient pair with p gamma^2>a/2; attainment of the supremum is not assumed. We may take p<min(A,1).

Choose

k=floor(np/[2(1+c0)]).

For each fixed c1 above the universal lower bound there is a constant C depending only on c1 and the universal mass constant such that

na>=C max{2 log n,log(m/delta)}

ensures k>=1, k<=An<=T, np>=2c0 L, and

k>=np/[4(1+c0)], gamma>2 Delta(n,k,delta).

Indeed L<=2 max{2 log n,log(m/delta)}, np gamma^2>na/2, and gamma<=1. Increasing C makes all these elementary inequalities hold. Since

k+c0 max{k,log(n/delta)} <= (1+c0)k+c0 L <= np/2+c0 L <= np,

the mass event guarantees at least k samples in B(x,r_p). Thus every neighbor prefix through k lies within r_p and has population separation at least gamma.

Inductively assume an active pointwise bag maximizer remains at iteration j<=k. Choose one with largest empirical frequency among active bag maximizers. An active nonmaximizer z cannot eliminate it: concentration gives

hat eta_j(z|x)-hat eta_j(i|x)<=-gamma+Delta(n,j,delta)<Delta(n,j,delta).

Another maximizer cannot eliminate the chosen empirical leader. Hence simultaneous removal leaves at least one bag maximizer active. This proves the invariant. If the algorithm stops at a singleton before k, that singleton is a bag maximizer.

At iteration k, any active nonmaximizer is exceeded by an active maximizer by at least gamma-Delta(n,k,delta)>Delta(n,k,delta), and is removed. After this iteration all remaining labels are bag maximizers. Later iterations preserve a nonempty subset of those labels, since an active empirical-frequency leader cannot be removed when the threshold is positive. Therefore any allowed final selection belongs to M_eta(x).

This establishes, for every qualifying fixed query x, a probability at most delta^2 of returning a label outside M_eta(x). At qualifying queries x in G, the equality M_eta(x)=M_q(x) additionally gives

P_training(h(x) not in M_q(x))<=delta^2.

No such true-posterior pointwise claim is made outside G. The argument retains some maximizer, not every maximizer, and requires no agreement with a predetermined Bayes selector.

For completeness, the source's query-specific logarithmic sample-size form is consistent with the same argument. Set v=adv_A(x)>0 and b=log(m/delta). The preceding estimates suffice whenever nv>=C(log n+b), by enlarging C. Let w=max{log(1/v),b}, so w>=log 2. At n0=Kw/v,

log n0+b <= log K+3w.

Choose K large enough that K>=C[log K/log 2+3] and n0>=e. Then n0 v>=C(log n0+b). The ratio (log n+b)/n decreases for n>=n0, so the same inequality holds for all n>=n0. Approximation of the advantage supremum and integer rounding have already been accounted for. The consistency proof below uses only the direct high-advantage condition.

## Risk Bound and Almost-Sure Consistency

For a fixed c1 above the universal lower bound, choose the preceding constant C and set

a_n=(C/n)max{2 log n,log(m/delta_n)}.

If a_n>=1, the low-advantage term is one and the claimed risk bound is trivial. Otherwise let H_n={x:adv_A(x)>a_n}. For every x in H_n intersect G the fixed-query result gives

P_training(hat h_n(x) not in M_q(x))<=delta_n^2.

Training probability includes the independent tie priorities. Tonelli gives

E_training integral_{H_n intersect G} 1{hat h_n(x) not in M_q(x)} dP_X(x)<=delta_n^2.

Since P_X(G^c)=0, for every realized measurable classifier this integral equals the corresponding integral over H_n. Markov consequently bounds the probability that the integral over H_n exceeds delta_n by delta_n. This does not condition on H_n, so it also applies when H_n is empty or null. No bound at an alignment-exception point is needed.

For any realized measurable classifier,

R(h)-R*=integral [max_y q_y(x)-q_{h(x)}(x)] dP_X(x).

The integral identity is unaffected by changes of conditional-probability versions on null sets. The integrand is zero on Bayes-optimal predictions and otherwise at most one. Splitting over H_n and its complement yields, with probability at least 1-delta_n,

R(hat h_n)-R*<=delta_n+P_X(adv_A(X)<=a_n).

Because T_n<=n,

log(1/delta_n)/n <= log(1/delta_n)/T_n ->0.

Thus a_n->0; summability also implies delta_n->0. Positive advantage almost everywhere and bounded convergence imply P_X(adv_A(X)<=a_n)->0. The probabilities of violations of the displayed risk bound are summable. Borel-Cantelli applies on the common probability space of the infinite iid observation-and-priority sequence, without any independence requirement between these violation events. Eventually the bound holds almost surely, and its right side tends to zero. Since excess risk is nonnegative, R(hat h_n)->R* almost surely. The proof applies to every measurable final selection permitted by the public algorithm.

## Explicit Indistinguishability Construction

Use an instance distribution concentrated at one point x0. For two labels 1 and 2, define P1 by

q1=(2/3,1/3),
P1(S={1,2}|Y=1)=2/3,
P1(S={1}|Y=1)=1/3,
P1(S={2}|Y=2)=1.

Define P2 by

q2=(1/3,2/3),
P2(S={1,2}|Y=1)=1/3,
P2(S={1}|Y=1)=2/3,
P2(S={1,2}|Y=2)=1/2,
P2(S={2}|Y=2)=1/2.

Unlisted positive-posterior bag probabilities are zero. Both processes even include their true labels in their bags, although the theorem does not require that restriction. In each process the observable probabilities of {1}, {2}, and {1,2} are respectively 2/9,3/9,4/9. Their observable laws therefore agree. Their bag-inclusion probabilities are eta1=6/9 and eta2=7/9. P2 is aligned with unique Bayes label 2, while P1 has unique Bayes label 1. The Bayes rules differ on the entire instance distribution.

For m>2 give the remaining labels posterior probability zero and never include them in an observed bag. Conditional bag kernels at zero-posterior labels can be chosen arbitrarily. The same construction and alignment conclusion hold.

Couple any observable-only learner, including its internal randomization, to the same observable sample sequence under both processes. Its output label at x0 is then the same in this coupling. Predicting label 1 gives excess risks (0,1/3), predicting label 2 gives (1/3,0), and predicting any additional label gives (2/3,2/3). Thus the sum of the two excess risks is always at least 1/3. Almost-sure convergence of both excess risks to zero is impossible. The same lower bound also rules out simultaneous consistency in probability or in expectation. Hence no such learner is Bayes consistent on the full PLL class or on any class containing this pair.

## Closure

Every theorem-critical obligation of the frozen task is derived above or follows from one of the explicitly stated standard independent results with its hypotheses checked. The query-to-risk argument requires only an almost-everywhere true-posterior guarantee and explicitly excludes the alignment-exception set. There is no unresolved private GT obligation. The source's stronger assertion about arbitrary strictly broader scenario classes is not a target, dependency, or completed rubric step.
