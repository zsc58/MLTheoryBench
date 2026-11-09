# Reference Proof

Write d=K-1 and H=H_d. All limits below are through positive scales. Empty sets have covering number zero.

## Obligations and background

The proof establishes: the center-constrained covering asymptotic for a fixed simplex; affine invariance and the normal-dependent simplex volume; uniformly low-distortion tangent charts; negligible covers of null remainders; and matching global upper and lower bounds. None of these covering assertions is assumed as an external theorem.

We use the standard area formula: for an injective C^1 parametrization F, H_d(F(E))=integral_E sqrt(det(DF^T DF)), and its change-of-variables version for manifold charts. We also use the local graph and half-space charts of a smooth embedded manifold with boundary, including smooth local extensions across its boundary, and continuity of finite measure on decreasing measurable sets. These apply to the compact smooth front and the bounded chart regions used below. Jordan sets are measurable for completed Hausdorff or Lebesgue measure since they differ from their interiors only on null boundaries.

## 1. Periodic density and covering cubes

Temporarily work in R^d with Lebesgue volume |.|. Let Omega be a compact convex body with 0 in its interior. Choose a,R>0 with [-a,a]^d subset Omega subset [-R,R]^d. Write N(E;t Omega) for the least number of translates s+t Omega covering E with all centers s in E.

For a full-rank lattice Lambda and finite set S of representatives modulo Lambda, suppose Omega+S+Lambda covers R^d. Its density is |S||Omega|/det Lambda. Define theta(Omega) to be the infimum of these densities. Redundant representatives may be deleted. A sufficiently fine rectangular lattice gives such a covering, so theta(Omega)<infinity. Integrating the covering multiplicity over a fundamental parallelepiped shows |S||Omega|>=det Lambda. Thus 1<=theta(Omega)<infinity.

We first prove

lim_{t downarrow 0} N(Q;t Omega)t^d = theta(Omega)|Q|/|Omega|

for any cube Q.

For Q=[0,1]^d, a cover with centers S_t subset Q, rescaled by 1/t and repeated with period t^(-1)Z^d, covers all of R^d. Consequently

theta(Omega)<=|S_t||Omega|t^d.

This proves the lower bound. It does not require an optimal density to be attained.

For the upper bound, fix a periodic covering with density less than theta(Omega)+epsilon and consider Q_T=[0,T]^d. Retain all its centers lying in Q_T. If a target point is more than R from the boundary in the infinity norm, every translate covering it has its center in Q_T. Thus the retained centers cover the inner core.

Fix a bounded fundamental parallelepiped P. It contains at most |S| centers modulo its translates. The number of translates of P meeting Q_T is at most (T+2D)^d/det Lambda for a fixed D large enough, because their disjoint interiors lie in a fixed-width enlargement of Q_T. Hence the number of retained centers is at most

(|S|/det Lambda)T^d+O(T^(d-1)).

Cover the remaining fixed-width shell by subdividing it into cubes of side at most a and choosing one point in each nonempty intersection with the shell. These centers belong to Q_T and their translates of Omega cover the shell. Their number is O(T^(d-1)), including O(1) when d=1. We therefore have a cover of the LARGE cube, with all centers in that cube, and

limsup_{T to infinity} N(Q_T;Omega)/T^d <= (theta(Omega)+epsilon)/|Omega|.

Let epsilon decrease to zero and rescale. Translation and dilation prove the assertion for every cube. This argument deliberately does not claim that the retained periodic centers belong to the inner core.

## 2. Extension to Jordan sets, retaining the center restriction

We prove, for every bounded E subset R^d with |boundary E|=0,

lim_{t downarrow 0} N(E;t Omega)t^d = theta(Omega)|E|/|Omega|.       (1)

For the lower bound, given epsilon>0 choose finitely many pairwise disjoint closed cubes Q_1,...,Q_m contained in int(E), with total volume at least |E|-epsilon. Such cubes are obtained from a sufficiently fine inner grid approximation and then shrunk slightly, so they may be chosen with positive mutual separation. This construction is possible because |E\int(E)|=0 and E is bounded.

Let S_t subset E be a minimal cover. For a fixed Q_j, targets more than Rt from its boundary can only be covered by centers in Q_j. Complete S_t intersect Q_j to a cover of Q_j by adding centers in its boundary shell. A grid of side at most at gives such a completion using O_j(t^(-(d-1))) centers, all belonging to Q_j. Hence

|S_t intersect Q_j| >= N(Q_j;t Omega)-O_j(t^(-(d-1))).

Sum over the disjoint cubes, multiply by t^d, and apply the cube limit. The lower limit is at least theta(Omega)(|E|-epsilon)/|Omega|. Let epsilon decrease to zero.

For the upper bound, fix a grid side length h>0 and take the finitely many closed grid cubes wholly contained in E. Their interiors are disjoint. Let Z_h be what remains of E after their union is removed. Then Z_h lies within infinity-distance 2h of boundary E. The union of covers of those cubes and a cover of Z_h is an admissible cover of E.

Choose a maximal at-separated set S in Z_h for the infinity norm. It is finite because Z_h is bounded. Maximality makes S a cover by translates of t Omega. The cubes of radius at/2 about its points have disjoint interiors. For sufficiently small t, these cubes lie in the closed 3h-neighborhood of boundary E. Therefore

|S|t^d <= a^(-d)|{x:dist_infinity(x,boundary E)<=3h}|.

Using the cube limit and that their total volume is at most |E| gives

limsup_{t downarrow 0} N(E;t Omega)t^d <= theta(Omega)|E|/|Omega| + a^(-d)|{dist_infinity(x,boundary E)<=3h}|.

The last volume tends to zero as h decreases to zero, since boundary E is compact and null. This proves (1), also when |E|=0. Every supplementary center in this argument belongs to the set it covers.

## 3. Affine invariance, orientation, and simplex volume

If Omega'=L Omega+b with L invertible, the image of a periodic covering is a periodic Omega'-covering using lattice L Lambda and representatives L S. Indeed, its union is b+L(Omega+S+Lambda). Both the body volume and lattice determinant are multiplied by |det L|, so the density is unchanged. Apply the inverse map to obtain theta(Omega')=theta(Omega). Every full-dimensional d-simplex is affinely equivalent to every other one. Denote their common density by theta_d and set C_K=d! theta_d>0.

For a positive unit vector n in R^K, let T_n={w:n dot w=0}. On this plane set p_n(w)=max_k w_k. A center u covers a target v precisely when p_n(u-v)<=t, or

v in u+t Omega_n,  where Omega_n={w in T_n:w_k>=-1 for every k}.

Thus the covering body is the reflection of {w:p_n(w)<=1}; this orientation is important even though reflection does not change its volume or density.

Put s=sum_k n_k. Translating w by the all-ones vector identifies Omega_n with {z_k>=0, sum_k n_k z_k=s}, whose vertices are (s/n_j)e_j. These are affinely independent, so Omega_n is a d-simplex, with 0 in its relative interior.

Parameterize T_n by

F(u)=(u_1,...,u_d,-sum_{j=1}^d n_j u_j/n_K).

Its Gram matrix is I+bb^T, where b=(n_1,...,n_d)/n_K. Its determinant is 1+|b|^2=1/n_K^2. The area factor is therefore 1/n_K. Under z_j=u_j+1, the parameter preimage of Omega_n becomes

{z_j>=0, sum_{j=1}^d n_j z_j<=s}.

The diagonal change of variables y_j=n_j z_j shows that this set has volume s^d/(d! product_{j=1}^d n_j). Hence

H_d(Omega_n)=s^d/(d! product_{k=1}^K n_k),

theta_d/H_d(Omega_n)=C_K product_k n_k/(sum_k n_k)^d=beta(n).       (2)

Using an orthonormal identification of T_n with R^d, (1) now gives the tangent-plane covering limit beta(n)H_d(E) for every bounded Jordan set E in T_n.

## 4. Smooth geometry and small-set covers

Distinct points of Gamma are incomparable coordinatewise, by the corrected Pareto definition. Thus delta(x,y)>0 when x and y are distinct, and delta(x,y)<=|x-y|_2. It also satisfies the triangle inequality directly from its coordinate formula.

On T_n, positivity of n gives a uniform lower comparison p_n(w)>=c_0|w|_2 with c_0=eta/[K(1+eta)]. To see this, write I={k:w_k>0}. Since n dot w=0 and eta<=n_k<=1,

sum_{k in I} w_k >= eta sum_{k notin I}(-w_k),

so sum_{k in I}w_k>=eta|w|_1/(1+eta), while max_k w_k>=K^(-1)sum_{k in I}w_k.

Near r, use a smooth graph over T_{nu(r)}, with inverse chart written

F_r(u)=r+u+g_r(u)nu(r),  g_r(0)=0, Dg_r(0)=0.

At a boundary point this graph is first taken on a smooth local extension and then restricted to Gamma. Work in a convex parameter neighborhood of the extension. By the mean-value estimate, after shrinking the neighborhood,

|F_r(u)-F_r(v)-(u-v)|_2 <= alpha|u-v|_2,

where alpha is as small as desired. Since taking a coordinate maximum is 1-Lipschitz in the infinity norm, this and the lower bound for p_n yield, for any prescribed 0<epsilon<1/2, charts phi_r=F_r^(-1) satisfying

(1-epsilon)p_{nu(r)}(phi_r(x)-phi_r(y)) <= delta(x,y) <= (1+epsilon)p_{nu(r)}(phi_r(x)-phi_r(y)).       (3)

The differential at r is an isometry. Shrinking again makes the d-dimensional area Jacobian of phi_r lie between 1-epsilon and 1+epsilon. Compactness supplies finitely many such charts, including boundary charts. The positive normal is continuous on the compact front, so beta composed with nu is bounded and uniformly continuous.

These charts also prove global comparability

c_Gamma|x-y|_2 <= delta(x,y) <= |x-y|_2                         (4)

for some c_Gamma>0. Indeed, finitely many smaller chart neighborhoods have a Lebesgue number, so sufficiently close pairs satisfy a uniform local lower bound by (3). For pairs separated by at least that number, delta(x,y)/|x-y|_2 is continuous and positive on a compact set. Its minimum is positive.

We will also need the following consequence of finite graph/half-space charts and the area formula. There are b,r_0>0 such that

H(Gamma intersect B_2(x,r))>=b r^d

for all x in Gamma and 0<r<r_0. In a boundary chart, a fixed fraction of a parameter ball is a half-ball; uniform bi-Lipschitz and Jacobian bounds on a finite atlas give this estimate. Interior charts give the same estimate with a full ball.

Consequently, if Z subset Gamma is compact and H(Z)=0, any E subset Z satisfies

lim_{t downarrow 0} M(t,E)t^d=0.                              (5)

Choose a maximal Euclidean t-separated set S subset E. It is finite and is an admissible Pareto t-cover. The intersections of Gamma with the radius-t/3 balls about S are disjoint and lie in the t-neighborhood of Z. Thus

|S|b(t/3)^d <= H({x in Gamma:dist_2(x,Z)<=t}).

The right-hand side tends to H(Z)=0. This argument controls arbitrary subsets E of Z and always places the centers in E.

For completeness, the auxiliary Euclidean rescaling inequality in the source should read N_2(t,E)<=(1+2/c)^K N_2(t/c,E). A t-separated packing inside a radius-t/c ball, divided by t/c, is c-separated in the unit ball, not 1/c-separated. The proof below does not need this auxiliary estimate.

## 5. A finite partition and the upper bound

Fix epsilon in (0,1/2). Choose finitely many relatively open Euclidean balls B_i covering Gamma, each with compact closure in one of the extended graph charts from (3), and each of diameter at most h_epsilon, where h_epsilon decreases to zero with epsilon. Their relative boundaries can be chosen H-null: for any fixed center, only countably many distance level sets can have positive H-measure, since these levels are disjoint and H(Gamma)<infinity.

Set

U_i=B_i\union_{j<i} closure_Gamma(B_j),

and Z=Gamma\union_i U_i. The U_i are disjoint relatively open sets, their boundaries are null, and Z is a compact null set contained in the union of the ball boundaries. Empty U_i may be omitted. Let phi_i map its containing chart to the plane with normal n_i at that chart's base point, and write b_i=beta(n_i). The base point and U_i lie in the same small ball, so beta(nu(x))-b_i tends uniformly to zero on all U_i as epsilon decreases.

Put A_i=A intersect U_i. Each phi_i(A_i) is a bounded Jordan set in its tangent plane. Indeed, the possible boundary comes from boundary_Gamma(A), boundary_Gamma(U_i), and the manifold boundary; these are H-null, and the smooth charts and their inverses are Lipschitz on the selected compact neighborhoods. The manifold boundary itself is H_d-null by its half-space charts.

Let N_i(q,phi_i(E)) denote the tangent-plane covering number with its centers in phi_i(E). From (3),

N_i(t/(1-epsilon),phi_i(E)) <= M(t,E) <= N_i(t/(1+epsilon),phi_i(E)).       (6)

The tangent limit (1)-(2) and the area formula imply

limsup_{t downarrow 0} M(t,A_i)t^d <= (1+epsilon)^d b_i H(phi_i(A_i)) <= (1+epsilon)^(d+1)b_i H(A_i),

and the analogous lower bound with 1-epsilon.

Taking the union of covers of A_i and a cover of A intersect Z is admissible. By (5), the latter has zero scaled limiting contribution. Hence

limsup_{t downarrow 0} M(t,A)t^d <= (1+epsilon)^(d+1) sum_i b_i H(A_i).       (7)

The extra power beyond d is the area-Jacobian factor. Covering all of Z using centers outside A would not justify this inequality.

## 6. The lower bound and the limit

For a nonempty U_i with nonempty complement define the continuous function

D_i(x)=dist_2(x,Gamma\U_i).

If U_i=Gamma, set D_i=infinity and take its layers to be empty. Choose a sequence s decreasing to zero such that H({D_i=s})=0 for every i. Such a common sequence exists because there are finitely many i and at most countably many positive-measure levels for each i.

Define B_i^s=A intersect U_i intersect {D_i<s}. Its relative boundary is contained in boundary_Gamma(A), boundary_Gamma(U_i), and {D_i=s}, so it is Jordan measurable. Also H(B_i^s) tends to zero as s decreases to zero: every point of U_i has positive distance from its closed complement.

Let S subset A be a minimal Pareto t-cover, with t<c_Gamma s. If y in A_i is covered by x in S outside U_i, (4) implies D_i(y)<=|x-y|_2<=t/c_Gamma<s. Thus any point of A_i not already covered by S intersect U_i lies in B_i^s. Adding a minimal cover of B_i^s, whose centers belong to B_i^s subset A_i, gives

M(t,A_i) <= |S intersect U_i|+M(t,B_i^s).

Summing over disjoint U_i yields

M(t,A) >= sum_i [M(t,A_i)-M(t,B_i^s)].

Use the lower side of (6) on A_i and the upper side on B_i^s, then apply the tangent limits and area bounds. For fixed epsilon and admissible s,

liminf_{t downarrow 0} M(t,A)t^d >= (1-epsilon)^(d+1)sum_i b_i H(A_i) -(1+epsilon)^(d+1)sum_i b_i H(B_i^s).

Let s decrease to zero along the chosen sequence. The finite sum of layer contributions vanishes, giving

liminf_{t downarrow 0} M(t,A)t^d >= (1-epsilon)^(d+1)sum_i b_i H(A_i).       (8)

Finally, since H(A intersect Z)=0 and beta composed with nu is uniformly continuous,

|sum_i b_i H(A_i)-integral_A beta(nu(x)) dH(x)| <= H(Gamma) sup_i sup_{x in U_i}|b_i-beta(nu(x))|,

which tends to zero with epsilon. Let epsilon decrease to zero in (7)-(8). The upper and lower limits agree and equal the required integral.

All positive-scale covering numbers used above are finite, for example by finite Euclidean nets with centers selected in the covered set. For A empty the assertion is immediate. For H(A)=0, its closure is null because its boundary is null, and the same proof, or (5), gives zero. If Gamma is empty the assertion is also immediate. Thus no positive-measure or nonempty-set exception is required.
