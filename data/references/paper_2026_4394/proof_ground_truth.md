# Reference Proof

## Proof Structure

Obtain a constant-probability event with at least d unobserved support points. The adversary encodes an unobserved d-set in a repeated auxiliary point. Because voter lists depend only on input length, uniform permutation places that point in a sufficiently large fraction of the subsamples with constant probability. A constructed consistent ERM then returns a common bad hypothesis. For the uniformly random consistent ERM, distinct replicated hypotheses make a contaminated subsample return a bad hypothesis with probability 1000/1001. A bounded-variable estimate gives a strict majority of bad votes without assuming independence between different subsamples.

The proof below closes the unseen-set estimate, the adversary's information and labeling constraints, the permutation calculation, both ERM constructions, both VC claims, strict-majority handling, and the uniform constants.

## Complete Proof

### 1. Quantitative unseen-set estimate (step_001)

It is enough to take c=16. Fix integers d>=1 and n>=16d. Write q=n/d and set

r = ceil(16n/log q).

The elementary inequalities log q <= 2 sqrt(q) and log q < q give

r >= 8d sqrt(q) >= 32d,

and

r <= 17n/log q.

In particular, r is an integer at least 2d. Take distinct points x_1,...,x_r, let D be uniform on them, and let h* be zero on the entire domain in each construction below.

Let I_i indicate that x_i is absent from the n clean draws, and put U=sum_i I_i. Its mean is

mu = E[U] = r(1-1/r)^n.

For distinct i,j,

E[I_i I_j] = (1-2/r)^n <= (1-1/r)^(2n),

so the covariances are nonpositive and Var(U)<=mu. Since r>=2, integrating 1/(1-u)<=2 on 0<=u<=1/r gives log(1-1/r)>=-2/r. Consequently,

mu >= r exp(-2n/r)
   >= 16d q^(7/8)/log q
   >= 8d q^(3/8)
   >= 8d.

If U<d, then |U-mu|>=mu/2. Using the pointwise bound on the indicator of this event,

Pr(U<d) <= 4 Var(U)/mu^2 <= 4/mu <= 1/(2d) <= 1/2.

Thus G={U>=d} has probability at least 1/2. This argument includes d=1 and handles integer rounding explicitly.

### 2. Adversary and permutation calculation (step_002)

Add a distinct point y_S for each d-element subset S of [r]. Fix an ordering of these subsets. For any admissible t, put m=2n/t. On G, the adversary chooses the first d-set T consisting of absent support indices and appends m copies of (y_T,0). On the complement of G, it appends m copies of (x_1,0). This rule is a function of the clean sample and the fixed instance parameters; it does not use the future permutation, test point, or ERM randomness. All labels agree with h*. It is a valid monotone adaptive adversary, and it works simultaneously for all voter list families at this input length.

Fix a clean sample satisfying G. Then T and all appended examples are fixed before the independent uniform permutation. Fix any majority voter at length N=n+m, with K>=1 lists. These lists depend only on N. If a list contains s distinct indices, the probability that it contains no appended entry is zero when s>n. Otherwise it is

binom(n,s)/binom(n+m,s)
  = product_{j=0}^{s-1} (n-j)/(n+m-j)
  <= (n/(n+m))^s
  <= (n/(n+m))^t
  = (1+2/t)^(-t)
  <= 1/3.

The last inequality follows from the binomial expansion (1+2/t)^t >= 1+t(2/t)=3 for integer t>=1. Thus the bound also covers t=1. Repeated indices in a list do not change its set of distinct positions.

Let A count lists avoiding all appended entries, and let C=K-A count contaminated lists. Conditional on the fixed clean sample, E[A]<=K/3. Since E[A]>=b Pr(A>=b) for b>0,

Pr(A<K/2) >= 1/3,

and

Pr(C>51K/100) = Pr(A<49K/100) >= 1-100/147 = 47/147.

No independence among the lists is required. These bounds hold for every clean sample in G, so they can be combined with Pr(G)>=1/2 by conditioning.

### 3. Fixed ERM construction (step_003)

On the domain consisting of the x-points and y-points, let H contain h* and one hypothesis h_S for each d-set S in [r]. Set h_S(x_i)=1 exactly when i belongs to S, and set h_S(y_R)=0 for every R.

To verify VC(H)=d, choose any d of the x-points. Every labeling of them is realized by taking its positive indices and padding them to a d-set using indices outside the chosen set; r>=2d makes this possible. No d+1 x-points can all be labeled one by a member of H. A set containing a y-point cannot be shattered because every hypothesis labels that point zero. Hence the VC dimension is exactly d.

Define a deterministic ERM as follows. On an all-zero-labeled sample, inspect the fixed ordering of d-sets. If there is a set S such that y_S occurs in the sample and no x_i with i in S occurs, output the first such h_S. If there is none, output h*. This resolves inputs containing several eligible witness points. Every output agrees with every sample label: an eligible h_S is zero on all observed x-points and all y-points, while h* is zero everywhere. To define the same ERM on any other H-realizable labeled sample, return the first consistent member of H in a fixed ordering. Thus the ERM is a total consistent rule on its required domain.

On G, every contaminated subsample contains y_T, contains no other y-point, and contains no x_i with i in T. The ERM therefore returns h_T on every contaminated subsample. If A<K/2, strictly more than half the returned hypotheses equal h_T. The majority vote is then one on every x_i with i in T, independently of the tie convention. Its error is at least d/r.

Combining the conditional probability from Section 2 with G gives

E[err] >= (1/2)(1/3)d/r >= d log(n/d)/(102n).

The domain, distribution, target, class, and ERM depend only on d,n, not on t or the voter.

### 4. Uniformly random consistent ERM (step_004)

For this construction, use the same x-points and y-points and add distinct points z_1,...,z_1000. Include h* as the all-zero hypothesis. For every d-set S and j in [1000], include a hypothesis h_{S,j} defined by

- h_{S,j}(x_i)=1 if and only if i belongs to S;
- h_{S,j}(y_R)=0 if R=S, and 1 otherwise;
- h_{S,j}(z_l)=1 if and only if l=j.

These are distinct functions, including when S is fixed and j varies. The distribution remains uniform on the x-points, so all auxiliary points have zero D-mass. The VC upper bound is proved in Section 5.

Use the adversary from Section 2. Fix a clean sample in G and a resulting permutation with C>51K/100 contaminated lists. For each contaminated subsample, the consistent hypotheses are exactly h* and h_{T,1},...,h_{T,1000}. Indeed, y_T excludes every hypothesis indexed by a different d-set; all copies indexed by T are consistent because no observed x-point belongs to T and no z-point was sampled or appended. Therefore each contaminated ERM call returns a copy indexed by T with probability 1000/1001.

Let B count, among all K outputs, those equal to some h_{T,j}. Conditional on the fixed clean sample and permutation, linearity of expectation gives

E[B] >= (1000/1001)C > (510/1001)K.

This uses only the marginal uniform distribution of each call; independence between these outputs is unnecessary. Put p=Pr(B>K/2) under the same conditioning. Because 0<=B<=K,

E[B] <= (K/2)(1-p)+Kp = K/2+(K/2)p.

It follows that

p >= 2E[B]/K-1 > 19/1001.

This proves a strict majority, including for even K; there is no fractional-number-of-lists selection and no unresolved tie case. On B>K/2, the majority vote is one on all of T and has error at least d/r. Consequently,

E[err] >= (1/2)(47/147)(19/1001)d/r
       >= [47*19/(34*147*1001)] d log(n/d)/n.

Again, the instance is fixed before t and the voter. The common adversary used in the proof is stronger than the adversary-existence quantifier required by the public statement.

### 5. VC upper bound for the randomized construction (step_005)

Let W be shattered by the class in Section 4. Write u,v,w for the numbers of x-points, y-points, and z-points in W.

First, u<=d: no hypothesis can label more than d x-points one. Second, w<=1: no hypothesis labels two distinct z-points one. Third, v<=2: on three distinct y-points, a labeling having two zeros and one one cannot be realized. Every non-target hypothesis is zero on exactly one y-point, whereas h* is zero on all of them.

If v=2 and W contains any additional point p, the labeling assigning zero to both y-points and one to p is impossible. A non-target hypothesis cannot be zero at both y-points, and h* cannot be one at p. Thus v=2 forces W to consist of those two points. If v<=1 instead, then

|W|=u+v+w <= d+2.

Since d>=1, both cases give |W|<=d+2. This establishes the required VC upper bound without importing a paper-specific lemma.

### 6. Constants and audit closure

The theorem follows with c=16 and

a = min{1/102, 47*19/(34*147*1001)} > 0.

All constructions are finite. The bounds are uniform in the admissible t, the number of voter lists, their overlap and repeated indices, and the tie convention. All expectations are taken in the public experiment's order.

The source's reciprocal covariance expression and its subsequent exponential estimate are replaced by the direct nonpositive-covariance calculation and the explicit lower bound mu>=8d. Its exponential shortcut for contamination is replaced by the binomial bound valid at t=1. Its half-vote inference is replaced by the strict-majority estimate above. The already-frozen at-most-d+2 formulation is retained; no assertion of an exact-d equivalence for every small d is used. Every theorem-critical obligation for this public task is explicitly derived, and no specialized external dependency remains.
