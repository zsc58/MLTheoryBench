# Reference Proof

## Proof Structure

Use spherical concentration with the source's sufficiently small exponential sample-size constant to make all normalized input pair probabilities nearly uniform. Compare a global minimizer with the collapsed embedding, and apply Pinsker together with the total-variation triangle inequality. Prove the resulting planar concentration conclusion by a quantitative annulus-counting argument. Finally, use the stationary equation for a bounded extreme point and a finite endpoint comparison for an unbounded extreme point.

## Complete Proof

All asymptotic statements below are for fixed delta, sigma, c, and the specified sequence r. Put D=d^{2delta}, m=binom(n,2), and let U be the uniform distribution on the m unordered pairs. For distributions on these pairs, define TV(A,B)=(1/2) sum |a_ij-b_ij|. We use the audited standard Pinsker inequality 2 TV(A,B)^2<=D(A||B). All probabilities appearing here are strictly positive, so the divergences and differentiations are well defined.

### 1. The sampling event and the growth constant

The standard spherical concentration result invoked in the source gives a constant a>0 such that, for sufficiently large d and independent uniform sphere points X,V,

Pr(|<X,V>|>d^{-1/2+delta}) <= 2 exp(-a d^{2delta}).

Its hypotheses hold for every sampled pair: conditional on one point, the other is uniform and independent. Choose c_*=a/4. For every fixed 0<c<c_* and n=floor(exp(cD)), a union bound gives

Pr(E^c) <= 2m exp(-aD) <= 2 exp(-(a/2)D),

where E is the event that every distinct pair has |<x_i,x_j>|<=d^{-1/2+delta}. Thus E has probability at least 1-exp(-Omega(D)), with exponent constants not depending on c, d, or n.

Work on E. Since ||x_i-x_j||^2=2-2<x_i,x_j>, the common factor exp(-1/sigma^2) cancels from each conditional row. With t=d^{-1/2+delta}, fixed positive sigma gives

exp(<x_i,x_j>/sigma^2)=1+O(t).

The correctly indexed row denominator is (n-1)(1+O(t)). Consequently

(n-1)p_{j|i}=1+O(t),

mp_ij=((n-1)/2)(p_{j|i}+p_{i|j})=1+O(t).

Write epsilon=max_{i<j}|mp_ij-1|. Then epsilon=O(t). The condition r=omega(d^{-1/6+delta/3}) implies epsilon=o(r^3). Also, the polynomial lower scale for r and the exponential growth of n imply rn tends to infinity; in particular 1/n=o(r).

### 2. Objective comparison and total variation

For positive finite distributions A,B, log z<=z-1 gives

D(A||B)<=sum a(a/b-1)=sum (a-b)^2/b=chi^2(A||B).

Thus

D(P||U)<=chi^2(P||U)=(1/m) sum (mp_ij-1)^2<=epsilon^2.

The embedding with all points coinciding has Q=U. Therefore every global minimizer Y satisfies D(P||Q(Y))<=epsilon^2. Pinsker, separately for P,Q and P,U, and the triangle inequality give

TV(U,Q)<=TV(U,P)+TV(P,Q)<=sqrt(D(P||U)/2)+sqrt(D(P||Q)/2)<=sqrt(2) epsilon=o(r^3).

This triangle-inequality step is essential: a divergence bound involving P cannot directly be substituted into a result stated for U.

### 3. The quantitative planar argument

We first establish a fixed annulus-counting fact. There is a fixed e>0 such that, for every sufficiently large n and every a>0, at most 0.9m pairs of planar points have distances in [(1-e)a,(1+e)a].

Here is the geometric fact behind the count. Scale a to 1 and put two centers at (0,0) and (s,0), where |s-1|<=e. If z=(u,v) is within the annulus of radii 1-e and 1+e about both centers, subtraction of the two squared-distance equations gives

u=s/2+(||z||^2-||z-(s,0)||^2)/(2s).

For e<=1/1000 this yields |u-1/2|<=3e, and then |v^2-3/4|<=6e. Hence z is within distance 8e of one of (1/2,sqrt(3)/2) and (1/2,-sqrt(3)/2). Two points in the annulus intersection therefore have distance at most 16e or at least sqrt(3)-16e. Both alternatives lie outside [1-e,1+e]. Fix such an e.

Suppose more than 0.9m pairs have distances in the indicated annulus, and call them edges. Some vertex i has more than 0.9(n-1) neighbors; let A be those neighbors. Removing every edge incident to a vertex outside A removes at most (n-|A|)(n-1) edges. Thus there remain more than 0.7m-O(n) edges within A. Averaging their degrees supplies j in A with at least (0.7-o(1))n neighbors within A. Let T be these neighbors. The centers y_i,y_j have distance in the annulus, and every point indexed by T lies in both annuli. By the geometric fact, no pair within T is an edge. This produces at least (0.49-o(1))m nonedges, contradicting the assumed fewer than 0.1m nonedges. The counting fact follows, uniformly over a and the point configuration.

Now sort the m pair distances and let a be the distance of rank k=ceil((1-r)m). If a<r, at least (1-r)m pairs have distance at most a. Averaging gives a vertex with at least (1-r)(n-1) such neighbors. Its open radius-r ball contains those neighbors and the vertex itself, hence at least (1-r)n points.

Suppose a>=r. At most rm pairs have distance greater than a. By the counting fact, at least 0.1m distances lie outside [(1-e)a,(1+e)a]. Therefore at least (0.1-r)m distances are less than (1-e)a. For sufficiently small r, this is at least rm. Also, the rank definition guarantees at least rm distances greater than or equal to a, including ties: m-k+1>=rm.

Let L be the pairs of distance less than (1-e)a and H the pairs of distance at least a. Both have U-mass at least r. Set w(s)=(1+s^2)^-1, h=w(a), l=w((1-e)a), and gamma=l/h. The function (1+a^2)/(1+(1-e)^2a^2) is increasing for a>=0, so

gamma >= (1+r^2)/(1+(1-e)^2r^2).

Put eta=(gamma-1)/(gamma+1). For r<1, eta>=b r^2 for a fixed b>0 depending only on e. Write bar_w=(1/m)sum w_ij, so mq_ij=w_ij/bar_w. If h/bar_w<=1-eta, then every pair in H has mq_ij<=1-eta and U(H)-Q(H)>=r eta. Otherwise every pair in L has mq_ij>gamma(1-eta)=1+eta and Q(L)-U(L)>=r eta. In either case,

TV(U,Q)>=r eta>=b r^3,

contradicting Section 2. Hence an open radius-r ball contains at least (1-r)n points. This argument is uniform over embeddings and thus applies simultaneously to all global minimizers on E.

### 4. Normalization and the stationary small-norm comparison

Fix any global minimizer. Translate the center of the ball just obtained to zero, and let I={j:||y_j||<r}, so |I|>=(1-r)n. Let k maximize ||y_k||, and put x=||y_k||. Define w_ij=(1+||y_i-y_j||^2)^-1 and Z=sum_{i<j}w_ij. Pairs within I give

Z >= binom(|I|,2)/(1+4r^2)=m(1-O(r)),

using 1/n=o(r), while Z<=m. Thus m/Z=1+O(r), uniformly in x.

For clarity, differentiating the actual unordered-pair objective gives

C(Y)=sum_{i<j}p_ij log p_ij+sum_{i<j}p_ij log(1+||y_i-y_j||^2)+log Z,

and therefore

grad_{y_k} C=2 sum_{j!=k}(p_kj-q_kj)w_kj(y_k-y_j).

At a global minimizer this gradient is zero.

If x<2r there is nothing to prove. Suppose 2r<=x<=3/2, set u=y_k/x, and put v_j=<y_k-y_j,u>. Maximality of x gives 0<=v_j<=2x for every j. Also k is outside I, and for j in I,

x-r<=v_j<=x+r,  x-r<=||y_k-y_j||<=x+r.

Define A_I=sum_{j in I}w_kj v_j and B_I=sum_{j in I}w_kj^2 v_j. Since x<=3/2 and r is small, the interior weights are bounded below by a numerical constant. Thus both A_I and B_I are at least a fixed positive constant times nx. Their corresponding exterior sums are at most 2rnx, since at most rn points are outside I and w<=1. Consequently the full sums A and B satisfy A=(1+O(r))A_I and B=(1+O(r))B_I.

Projecting the zero-gradient equation onto u and multiplying by m gives

sum_{j!=k}(mp_kj)w_kj v_j=(m/Z)sum_{j!=k}w_kj^2 v_j.

Every summand in A is nonnegative, so its left side is (1+O(epsilon))A. Since epsilon=o(r^3), the equation implies A_I<=(1+Kr)B_I for a fixed K. But every interior weight is at most (1+(x-r)^2)^-1, whence

B_I <= A_I/(1+(x-r)^2).

Since A_I>0, it follows that (x-r)^2<=Kr. Thus x<=r+sqrt(Kr)=O(sqrt(r)).

### 5. The finite endpoint comparison for a large extreme point

It remains to rule out x>=3/2. Keep every other point fixed and replace y_k by zero. Let primes denote the resulting weights and normalization. Write L=log(1+x^2).

For j in I, the old distance is at least x-r and the new distance is less than r. Because the derivative of log(1+s^2) is at most 1 for s>=0,

log(1+||y_j||^2)-log(1+||y_k-y_j||^2) <= -L+Kr.

For j outside I and different from k, the same logarithmic change is at most L, because the new distance is at most x and the old logarithm is nonnegative. Using mp_kj=1+O(epsilon), |I|>=(1-r)n, and at most rn exterior points, the change in the pair-log part of C is at most

(2/n)(-(1-Kr)L+Kr),

after increasing a fixed K and taking n sufficiently large. In this estimate the O(r)L term is retained: L is not assumed bounded.

Only pairs containing k change their weights. Before the move every such distance is at most 2x, so w_kj>=(1+4x^2)^-1, whereas every new weight is at most 1. Therefore

Z'-Z <= (n-1)(1-(1+4x^2)^-1).

Using log(1+t)<=t, positivity of Z', and the lower bound on Z gives

log Z'-log Z <= (2/n)(1+O(r))(1-(1+4x^2)^-1) <= 2.2/n

for sufficiently small r. Thus

C(Y')-C(Y) <= (2/n)(-(1-Kr)L+Kr+1.1).

For x>=3/2, L>=log(13/4)>1.1. The last display is strictly negative for sufficiently small r, uniformly over all such x. This contradicts global minimality. Notice that this is an endpoint comparison; no monotonicity along the entire segment is asserted or required.

Hence x<3/2, and Section 4 gives x=O(sqrt(r)). Every point belongs to a ball of that radius about the translated origin.

### 6. Conclusion

On the single sampling event E, every global minimizer has the required open radius-r ball and a containing ball of radius O(sqrt(r)). Section 1 gives the required probability. Constants in the concentration rate and geometric bounds can be chosen independently of c in (0,c_*), d, and n; the allowed dependencies on sigma and delta are preserved. This proves the stated target. All theorem-critical obligations have been closed.
