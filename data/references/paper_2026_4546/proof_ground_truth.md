# Reference Proof

## Proof Structure and Obligations

1. Establish gauge regularity, identify the feasible and interior sublevel sets, and obtain local Lipschitzness of q and p.
2. Prove the exact scalar range on every ray, including rays with infinite boundary distance.
3. Establish strict interior feasibility and bijectivity, then verify the hypotheses of Invariance of Domain.
4. Apply Rademacher's theorem to obtain almost-everywhere differentiability.
5. At an arbitrary differentiability point of p, justify the product rule and all additional differentiability used in the exterior calculation.
6. Prove invertibility in the interior and strict exterior, and account for boundary points.

All six obligations are closed below. The external results used are the standard gauge properties indexed by theory_021, Rademacher's theorem indexed by theory_007, and Invariance of Domain indexed by theory_019. Their relevant statements and hypotheses are given below. Euler's identity, indexed by theory_022, is derived directly. Almost-everywhere differentiability of a finite convex gauge, indexed by theory_023, is valid background but is not used to substitute for the pointwise obligation.

## Complete Proof

The anchor is already zero. If the zero-dimensional Euclidean space is allowed, the claim is immediate: C={0}, p is the unique map on this space, and its derivative is the invertible linear map on the zero vector space. Hence consider n>=1.

### 1. Gauge regularity and local Lipschitzness

For each u, continuity of a->au, closedness of C, convexity, and 0 in C imply that {a in [0,1]:au in C} is a nonempty closed interval [0,alpha(u)]. Thus q(u) belongs to C.

Choose delta>0 with B(0,delta) contained in C, and define

gamma(x)=inf{t>0:x in tC}.

The standard gauge theorem says that for a convex set containing a neighborhood of zero, this gauge is finite, nonnegative, positively homogeneous, and subadditive. Its hypotheses hold here. The interior ball gives gamma(x)<=||x||/delta. Subadditivity in both orders therefore gives

|gamma(x)-gamma(y)|<=||x-y||/delta.

In particular gamma is continuous, including at directions where it vanishes.

We also have C={x:gamma(x)<=1}. One inclusion follows immediately from the definition. For the converse, the set of positive t with x in tC is nonempty and upward closed, since 0 in C and C is convex. Consequently, if gamma(x)<=1, then x/(1+1/k) belongs to C for every positive integer k. Closedness gives x in C.

Moreover, Int(C)={x:gamma(x)<1}. The strict sublevel set is open and contained in C, so it is contained in Int(C). Conversely, if x is a nonzero interior point, then (1+epsilon)x belongs to C for some epsilon>0. Homogeneity gives gamma(x)<=1/(1+epsilon)<1. At x=0, gamma(0)=0. It follows also that boundary points have gauge one.

Define H(0)=1 and H(t)=min(1,1/t) for t>0. Homogeneity and the feasible-sublevel characterization imply

alpha(x)=H(gamma(x)).

The function H is 1-Lipschitz on [0,infinity): it is constant on [0,1], and on [1,infinity) its derivative has absolute value at most one; the same bound across the junction follows by splitting the interval at 1. Thus alpha is globally Lipschitz with constant 1/delta. If ||x||,||y||<=M, then

||q(x)-q(y)||<=||x-y||+||y|| |alpha(x)-alpha(y)|<=(1+M/delta)||x-y||.

Hence q is locally Lipschitz. The scalar function S(x)=r(||x||^2) is C1 and locally Lipschitz, so p=S q is locally Lipschitz as well. At zero the C1 assertion is understood with the one-sided C1 regularity of r on [0,infinity); the derivative of S at zero is zero. Also S(x)>=r(0)>0 everywhere.

### 2. Ray ranges

For a unit vector v define

b(v)=sup{t>=0:tv in C}.

Then b(v)>0, and the gauge characterization gives b(v)=1/gamma(v), with 1/0=infinity. In particular b is continuous into the extended interval (0,infinity]; at a direction where gamma vanishes, nearby reciprocal values tend to infinity in that topology.

For t>=0,

q(tv)=min(t,b(v))v,

p(tv)=psi_v(t)v,

psi_v(t)=r(t^2)min(t,b(v)).

Here min(t,infinity)=t. On the portion t<=b(v), the scalar derivative is

r(t^2)+2t^2r'(t^2)>0,

including at zero, where it equals r(0). If b(v)<infinity, the portion t>b(v) equals b(v)r(t^2), is strictly increasing, and agrees with the first formula at the junction. Its limit is b(v), and all its finite values are below b(v). Therefore its full range is [0,b(v)). If b(v)=infinity, then psi_v(t)=r(t^2)t>=r(0)t tends to infinity, so the range is [0,infinity). Thus every psi_v is continuous, strictly increasing, and has exactly the claimed range.

### 3. Homeomorphism

Strict interior feasibility follows explicitly from q(u) in C, homogeneity, and r(||u||^2)<1:

gamma(p(u))=r(||u||^2)gamma(q(u))<=r(||u||^2)<1.

Thus p(u) belongs to Int(C).

For u!=0, alpha(u)>0 and r(||u||^2)>0, so p(u)!=0 and p(u) has the same unit direction as u. Also p(0)=0. If two outputs agree and are nonzero, their inputs lie on the same ray, and strict increase of psi_v forces the input radii to agree. A zero output has only the zero input. Hence p is injective.

If x is a nonzero interior point, write x=s v with s=||x|| and v=x/||x||. The interior gauge characterization gives s<b(v). The scalar range result supplies a unique t with psi_v(t)=s, so p(tv)=x. The zero point has preimage zero. Hence p maps onto Int(C).

The map p is continuous by local Lipschitzness. Invariance of Domain states that a continuous injective map from an open subset of R^n into R^n is open. Apply it to the open domain R^n and the continuous injection p. Since p is also a bijection onto Int(C), openness implies continuity of its inverse. Thus p is a homeomorphism onto Int(C).

### 4. Differentiability and the pointwise product rule

Rademacher's theorem states that a locally Lipschitz map between finite-dimensional Euclidean spaces is differentiable almost everywhere with respect to Lebesgue measure. Applying it to p gives the asserted almost-everywhere differentiability.

Now fix an arbitrary point u where p is differentiable. Since S is C1 and strictly positive, q=p/S is differentiable at u. Set rho=||u||^2, R=r(rho), and R'=r'(rho). The product rule gives

J_p(u)=R J_q(u)+2R' q(u)u^T.

This formula is therefore justified at every differentiability point under consideration, not merely on a previously selected full-measure set.

### 5. Interior points

If u belongs to Int(C), q is the identity in a neighborhood of u. Therefore

J_p(u)=R I+2R'uu^T.

At u=0 this equals r(0)I and is invertible. At nonzero u, its eigenvalue in the radial direction is R+2R'||u||^2, while the eigenvalue on directions orthogonal to u is R. Both are positive by the assumptions. This includes the one-dimensional case, in which there are no nonzero orthogonal directions.

### 6. Strict exterior points

Suppose u is outside C. By continuity of gamma and gamma(u)>1, the identity q(x)=x/gamma(x) holds throughout a neighborhood of u. In that neighborhood x is nonzero and x^T q(x)>0, so

gamma(x)=||x||^2/(x^T q(x)).

Because q is differentiable at the selected u, this identity proves differentiability of gamma there. This closes the pointwise implication that cannot be replaced by almost-everywhere differentiability of gamma.

Write g=gamma(u)>1 and a=grad gamma(u). Differentiating gamma(tu)=t gamma(u) at t=1 gives Euler's identity a^T u=g. Differentiating the local formula for q gives

J_q(u)h=h/g-u(a^T h)/g^2.

Decompose an arbitrary vector h as h=h_W+beta u, where beta=(a^T h)/g and a^T h_W=0. Then J_q(u)h=h_W/g, and

J_p(u)h=(R/g)h_W+(2R'/g)u(u^T h).

If J_p(u)h=0, applying a^T gives 2R' u^T h=0. Here u!=0 and R'>0, so u^T h=0. The vector equation then gives h_W=0 because R/g>0. Thus h=beta u, and u^T h=beta||u||^2=0 forces beta=0. The kernel is trivial, proving invertibility.

### 7. Boundary points

Suppose u belongs to the boundary of C. Then u!=0 and gamma(u)=1. For sufficiently small s, homogeneity and the formula for alpha imply

q((1+s)u)=(1+s)u when s<0,

q((1+s)u)=u when s>0.

The left derivative of this curve at s=0 is u, whereas the right derivative is zero. Thus q is not differentiable at u. Since differentiability of p would imply differentiability of q=p/S, p is not differentiable there either. Consequently no boundary point is an omitted case in the everywhere-it-exists assertion.

The interior and strict exterior arguments cover every differentiability point. Together with Rademacher's theorem, they establish both differential claims.

## Source-Repair Note

The source's exterior proof uses gauge differentiability almost everywhere and includes boundary points when differentiating the exterior representation. The local completion recorded under theory_011 recovers gauge differentiability at each exterior differentiability point of p and excludes boundary differentiability. No public hypothesis or conclusion is changed.
