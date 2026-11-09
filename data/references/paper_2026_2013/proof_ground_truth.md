# Reference Proof

## Proof Structure and Obligations

The proof closes six obligations: label alignment and separation geometry; an additive squared-loss merge comparison; its balance-dependent counting bound; deletion estimates and squared-loss positivity; the one-dimensional merge and counting estimates giving absolute-loss positivity; and explicit finite configurations proving the two necessity orders. All collections below are indexed, so repeated locations are counted with their multiplicities. Empty subcollections have cost zero.

## 1. Alignment and Geometry

Relabel the benchmark, if necessary, so that n_1<=n_2, hence b=n_1/n. Align the candidate partition's labels to maximize overlap with the benchmark. Define

q_1=|C_1^* intersect C_2|, q_2=|C_2^* intersect C_1|, t=q_1+q_2.

Swapping candidate labels changes t to n-t, so 0<=t<=n/2. The candidate differs from the benchmark up to labels exactly when t>0.

Let A_j be the points of benchmark cluster j retained in candidate cell j, and B_j the points of benchmark cluster j placed in the other cell. Thus |A_j|=n_j-q_j, |B_j|=q_j, C_1=A_1 union B_2, and C_2=A_2 union B_1. These unions refer to disjoint index sets.

The triangle inequality gives distance at least m=S-2R between any two points in different benchmark balls. More importantly for squared loss, the mean of any nonempty subgroup stays in its benchmark ball: its distance from the anchor is at most the average distance of its members, hence at most R. Means of subgroups from different benchmark balls are therefore at distance at least m.

## 2. Squared-Loss Merge Comparison

Write Q(E)=min_z sum_{i in E}||x_i-z||^2, with Q(empty)=0. For a nonempty finite collection E with mean mu_E, expansion and sum_{i in E}(x_i-mu_E)=0 give

sum_{i in E}||x_i-z||^2=sum_{i in E}||x_i-mu_E||^2+|E|||z-mu_E||^2.

Thus its mean attains Q(E). Applying this identity to two disjoint nonempty collections E,F and their union gives

Q(E union F)=Q(E)+Q(F)+|E||F|/(|E|+|F|)||mu_E-mu_F||^2.

Indeed, the union mean is (|E|mu_E+|F|mu_F)/(|E|+|F|), and substitution gives the displayed coefficient. This additive identity, rather than a cross-pair bound alone, preserves the subgroup costs needed for comparison with the benchmark.

Apply the identity to A_1,B_2 and A_2,B_1. If a subgroup is empty, the merge contribution is zero and the corresponding inequality is immediate. Dropping Q(B_1),Q(B_2)>=0 gives

V_{r^2}(C)>=Q(A_1)+Q(A_2)+M m^2,

where

M=((n_1-q_1)q_2)/(n_1-q_1+q_2)+((n_2-q_2)q_1)/(n_2-q_2+q_1).

A term with an empty subgroup is interpreted as zero.

## 3. Squared-Loss Counting Bound

We prove M>=bt. For t=0 this is immediate. Otherwise fix t and put u=q_1, so q_2=t-u. Because t<=n/2<=n_2, the feasible interval is 0<=u<=min(n_1,t). Define

f(u)=((n_1-u)(t-u))/(n_1+t-2u)+((n_2-t+u)u)/(n_2-t+2u).

The first term is z_1/4-d_1^2/(4z_1), with z_1=n_1+t-2u and d_1=n_1-t. The second is z_2/4-d_2^2/(4z_2), with z_2=n_2-t+2u and d_2=n_2-t. For positive z, the second derivative of z/4-d^2/(4z) is -d^2/(2z^3)<=0. Composition with an affine function preserves concavity. Where a denominator vanishes at an endpoint, both subgroup sizes vanish, d=0, and the continuous endpoint value is zero. Consequently f is concave on the closed feasible interval and is bounded below by the smaller endpoint value.

At u=0,

f(0)=n_1t/(n_1+t)>=n_1t/n,

because t<=n_2. If t<=n_1, the other endpoint is u=t and

f(t)=n_2t/(n_2+t)>=n_1t/n;

after multiplication by positive denominators this is equivalent to n_2^2>=n_1t, which follows from t<=n_1<=n_2. If t>n_1, the other endpoint is u=n_1 and

f(n_1)=n_1(n-t)/(n+n_1-t)>=n_1t/n.

This is equivalent to (n-t)^2>=n_1t. Both n_1 and t are at most n/2, while n-t>=n/2, so it holds. Hence M=f(q_1)>=bt.

## 4. Deletion Estimates and Squared-Loss Positivity

For any benchmark cluster E and removed subset T, suppose first that E\T is nonempty. Its mean lies in the benchmark ball, so every point of T is at distance at most 2R from that mean. Evaluating the objective of E at that mean gives

Q(E)<=Q(E\T)+4R^2|T|.

If E\T is empty, evaluate E at its anchor instead: Q(E)<=R^2|E|<=4R^2|T|, so the same inequality holds. This includes R=0.

Applying the estimate to both benchmark clusters yields

Q(A_1)+Q(A_2)>=V_{r^2}(C^*)-4R^2t.

Together with Sections 2 and 3,

V_{r^2}(C)-V_{r^2}(C^*)>=t(bm^2-4R^2).

Under bm^2>4R^2, this is strictly positive whenever t>0. Thus the benchmark partition is the unique minimizer up to labels. This asserts uniqueness of the partition, not a separate claim about prototype uniqueness.

## 5. Absolute Loss on the Line

Write F(E)=min_z sum_{i in E}|x_i-z|, with F(empty)=0. For a nonempty finite collection, clipping z to the interval from its smallest to its largest point cannot increase the objective; continuity on that compact interval gives a minimizer. Ordering the points shows that the slope between consecutive locations is the number of points to the left minus the number to the right. Thus the minimizers are medians, and a minimizing center can be chosen in the collection's containing interval.

First establish the merge inequality. Let E lie in a left interval with right endpoint alpha and F lie in a right interval with left endpoint beta, where beta-alpha=m. Put e=|E| and f=|F|. Empty groups are immediate. Suppose e>=f. For z>alpha, replacing z by alpha decreases the E contribution by e(z-alpha), while increasing the F contribution by at most f(z-alpha), by the triangle inequality. Hence a minimizing center z_* can be chosen with z_*<=alpha. At that center the E contribution is at least F(E), and the contribution of the right subgroup is at least

sum_{i in F}(x_i-alpha)=sum_{i in F}(x_i-beta)+fm>=F(F)+fm.

Here F(F) denotes the optimal absolute-loss cost of the subgroup named F. Reversing left and right proves the other case. Therefore, for any two such separated subgroups,

F(E union F)>=F(E)+F(F)+m min(e,f).

The same inequality applies regardless of which benchmark cluster is leftmost. Applying it in both candidate cells and dropping nonnegative removed-subgroup costs gives

V_r(C)>=F(A_1)+F(A_2)+mP,

where

P=min(n_1-q_1,q_2)+min(n_2-q_2,q_1).

Since n_2>=n/2>=t, we have n_2-q_2>=q_1. Consequently

P=q_1+min(n_1-q_1,q_2)=min(n_1,t).

If t<=n_1, then P=t>=2bt because b<=1/2. If t>n_1, then P=n_1=bn>=2bt because t<=n/2. Thus P>=2bt. The relevant split is t<=n_1 versus t>n_1, not merely the comparison of q_1 and q_2.

For deletion, choose a minimizing center of a nonempty retained subgroup inside its benchmark interval. Each deleted point is at distance at most 2R from this center, giving

F(E)<=F(E\T)+2R|T|.

If the retained subgroup is empty, use the anchor to obtain F(E)<=R|T|<=2R|T|. Summing over the benchmark clusters gives

F(A_1)+F(A_2)>=V_r(C^*)-2Rt.

It follows that

V_r(C)-V_r(C^*)>=mP-2Rt>=2t(bm-R).

Under bm>R, every t>0 gives strict positivity, proving uniqueness up to labels. No uniqueness of a median is required. The argument also covers R=0.

## 6. Explicit Necessity Constructions

We prove the quantified necessity statement with universal constants c=1/4 and b_0=1/16. Fix a rational b in (0,b_0], R>0, and a positive margin m in the range for the loss under consideration. Choose positive integers n_1,n_2 with n_1/(n_1+n_2)=b and n_2 even; multiplying a rational representation by two ensures the latter. Put S=2R+m.

Take anchors a_1=0 and a_2=S. Put all n_1 benchmark-cluster-1 observations at 0, and put n_2/2 benchmark-cluster-2 observations at each of S-R and S+R. The radius bound is R, the anchor separation is S>2R, and the balance is exactly b.

For squared loss, the benchmark centers 0,S are the means, so

V_{r^2}(C^*)=n_2R^2.

For absolute loss, 0 is the first cluster's median and every point of [S-R,S+R] is a median of the equally weighted second cluster. Therefore

V_r(C^*)=n_2R.

Consider the alternative partition joining the points at 0 with those at S-R, while assigning the points at S+R to its other cell. Both cells are nonempty and this partition is not the benchmark up to labels. The feasible centers S-R,S+R give

V_{r^2}(C)<=n_1(S-R)^2=n_1(R+m)^2,

V_r(C)<=n_1(S-R)=n_1(R+m).

These are feasible-center upper bounds; the competing squared-loss centers need not be optimal.

If 0<m<=R/(4sqrt(b)), then

b(1+m/R)^2<=(sqrt(b)+1/4)^2<=1/4<1-b.

Since n_2/n_1=(1-b)/b, this proves n_1(R+m)^2<n_2R^2. Thus the benchmark is not a squared-loss minimizer.

If 0<m<=R/(4b), then

b(1+m/R)<=b+1/4<=5/16<1-b.

Hence n_1(R+m)<n_2R, so the benchmark is not an absolute-loss minimizer. These constructions establish the respective b^{-1/2} and b^{-1} orders with constants independent of the balance, sample size, and radius.

All theorem-critical obligations have now been explicitly closed. No nonstandard external result is assumed.
