# Reference Proof

## Proof Structure

We first check the normalized aggregate's definition, derive the coordinate variance bound, and explain the attainable boundary envelope. We then establish A0 and A1, compare the uniform simplex law with a vertex mixture to disprove A2, prove strict A3 using the prescribed coupling, and disprove A5 by a feasible translation in every fixed dimension K>=2. All moments used below are population moments.

## Complete Proof

### step_001: Definition and zero-mean coordinates

Let P=(P_1,...,P_K) have law Q on the simplex, with mu_k=E[P_k] and v_k=Var(P_k). Each coordinate lies in [0,1], so all moments needed below are finite. Since P_k>=0, mu_k=0 implies P_k=0 almost surely and hence v_k=0. Thus the zero-mean convention is consistent, and

EU(Q)=(1/2) sum_{k:mu_k>0} v_k/mu_k.

### step_002: Coordinate variance bound

For every x in [0,1], x^2<=x. Therefore

v_k=E[P_k^2]-mu_k^2<=mu_k-mu_k^2=mu_k(1-mu_k).

In particular, raw coordinate variance is forced to zero as its mean approaches either endpoint.

### step_003: Normalized bound and boundary interpretation

For mu_k>0, dividing the preceding bound by 2mu_k gives

C_k(Q)<= (1/2)(1-mu_k).

The right-hand side tends to 1/2 as mu_k approaches zero from above. This is an upper-envelope statement, not a positive lower bound for C_k and not a claim that every family of laws has C_k tending to 1/2.

The envelope is attainable on the simplex. Fix another coordinate j distinct from k and let Q_t assign probability t to the vertex e_k and probability 1-t to the vertex e_j, where e_i denotes the vector with coordinate i equal to one and all other coordinates zero. For 0<t<1, mu_k=t and v_k=t(1-t), so C_k(Q_t)=(1-t)/2. Thus normalized coordinate uncertainty can approach 1/2 while its mean approaches zero. At mean exactly zero the stipulated component is zero; no continuity at that boundary is asserted.

### step_004: A0 and A1

A0 follows because every summand in EU is nonnegative.

If Q is a point mass, every coordinate variance is zero and EU(Q)=0. Conversely, if EU(Q)=0, every nonnegative summand vanishes. For positive-mean coordinates this forces v_k=0, and zero-mean coordinates already have variance zero. Hence each P_k equals mu_k almost surely. Since there are finitely many coordinates, P=mu almost surely, so Q is a point mass. This proves both directions of A1.

### step_005: A2 fails

Let m be the number of positive-mean coordinates. Their means sum to one. Summing the coordinate bounds yields

EU(Q)<= (1/2) sum_{k:mu_k>0}(1-mu_k)=(m-1)/2<=(K-1)/2.

The law V that chooses each vertex e_k with probability 1/K attains the last bound: its means are 1/K and its coordinate variances are (K-1)/K^2. Consequently EU(V)=(K-1)/2.

We compute the value under U, the normalized (K-1)-dimensional volume measure on the simplex. Coordinate permutation symmetry and the simplex constraint give E_U[P_k]=1/K. For 0<=t<1, the region where p_k>=t is the image of the entire simplex under the affine map r -> t e_k+(1-t)r. This map multiplies (K-1)-dimensional volume by (1-t)^(K-1). Hyperplane sections have zero volume, so

Pr_U(P_k>t)=(1-t)^(K-1).

The identity x^2=integral_0^x 2t dt and integration of a nonnegative function give

E_U[P_k^2]=2 integral_0^1 t(1-t)^(K-1) dt
=2(1/K-1/(K+1))=2/[K(K+1)].

It follows that

Var_U(P_k)=2/[K(K+1)]-1/K^2=(K-1)/[K^2(K+1)],

and hence

EU(U)=(K-1)/[2(K+1)]<(K-1)/2=EU(V)

for every K>=2. Thus U is not a maximizer and A2 fails.

### step_006: Strict A3

Let P'=P+Z be a coupling from A3. Both P and P' are simplex-valued, so Z is bounded, and E[Z|P]=0 gives E[Z]=0. Therefore E[P'_k]=mu_k. Moreover,

Cov(P_k,Z_k)=E[(P_k-mu_k)E[Z_k|P]]=0,

and the variance expansion gives

Var(P'_k)=v_k+Var(Z_k).

If mu_k=0, nonnegativity and the common mean imply P_k=P'_k=0 almost surely; thus Z_k=0 almost surely. The zero-mean coordinates contribute nothing to either aggregate. For the other coordinates,

EU(Q')-EU(Q)=(1/2) sum_{k:mu_k>0} Var(Z_k)/mu_k.

By nontriviality, some Var(Z_k)>0. Such a coordinate cannot have zero mean, as just shown. The displayed sum is consequently strictly positive, proving A3.

### step_007: A5 fails for every K>=2

For the arbitrary fixed K>=2, let X take values 1/4 and 3/4 with equal probabilities and define

P=(X,1-X,0,...,0),

d=(1/8,-1/8,0,...,0).

When K=2 there are no trailing coordinates. The two possible values of P+d have first two coordinates (3/8,5/8) and (7/8,1/8), respectively. Thus P'=P+d remains simplex-valued, and this is a nonzero deterministic translation. Every coordinate variance is preserved.

For Q, the first two means are 1/2 and both variances are 1/16, giving EU(Q)=1/8. For Q', the first two means are 5/8 and 3/8, with the same variances. All remaining coordinates have mean zero and contribute zero under the stipulated convention. Therefore

EU(Q')=(1/2)[(1/16)/(5/8)+(1/16)/(3/8)]=2/15 != 1/8.

This disproves A5 in every dimension covered by the task.

Thus EU satisfies A0, A1, and strict A3, but violates A2 and A5. The same inverse-mean weighting that makes the aggregate sensitive to translations also yields the attainable nonvanishing coordinate upper envelope near a zero-mean boundary; it does not force every coordinate score to stay positive there.
