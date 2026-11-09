# Reference Proof

## Obligations and permitted background

The proof must establish: (1) projection feasibility, attainment, binding and the optimality system; (2) existence and geometry of the normalization path; (3) correct, finitely terminating active-set transitions with quadratic total cost; (4) exact recovery of a nonnegative multiplier, including a constant terminal segment and the endpoint beta=min b; (5) the minimax exchange; (6) the exact projection-sum threshold test; and (7) the accuracy and operation count, including U=0 and large tolerances.

Two standard independent facts are used. First, for a differentiable convex function on all of Euclidean space minimized over a nonempty polyhedron, an attained minimizer satisfies KKT with nonnegative inequality multipliers and free equality multipliers. Conversely, KKT is sufficient. This is the polyhedral normal-cone optimality condition; strict feasibility of the affine inequalities is not required. Second, a continuous bilinear function on two nonempty compact convex sets admits the minimax exchange. The hypotheses of both facts are checked below. No specialized path-construction theorem is taken as a black box.

## 1. Projection optimality

Write D=W^2, a_i=D_{ii}^{-1}, c_i=2D_{ii}q_i, and f(x)=(x-q)^T D(x-q). If beta<min_i b_i, the feasible set is empty. If b^T q<=beta, return q with value zero. These tests cost O(n). Otherwise min_i b_i<=beta<b^T q. The feasible set is a nonempty compact polyhedron, so a minimizer exists; positive definiteness of D makes it unique.

The inequality binds at that minimizer. Indeed, if it were strict, moving a sufficiently small positive distance toward q would preserve feasibility and strictly decrease f, since f((1-t)x+tq)=(1-t)^2f(x).

Apply the polyhedral KKT fact to this differentiable convex objective and its affine constraints. This applies also when beta=min_i b_i. With alpha>=0 for the moment inequality, gamma for normalization, and zeta_i>=0 for -x_i<=0, stationarity is

2D(x-q)+alpha b-gamma 1-zeta=0.

Together with zeta_i x_i=0, this gives

x_i=(a_i/2)[-b_i alpha+gamma+c_i]_+.

Normalization and the binding moment constraint give

sum_i a_i[-b_i alpha+gamma+c_i]_+=2,
sum_i b_i a_i[-b_i alpha+gamma+c_i]_+=2 beta. (1)

Conversely, any alpha>=0 and gamma satisfying (1) produce a feasible x by the displayed formula. Set zeta_i=[b_i alpha-gamma-c_i]_+. Stationarity and complementary slackness then hold. For any feasible y, convexity yields

f(y)-f(x)>=grad f(x)^T(y-x)
=-alpha b^T(y-x)+zeta^T(y-x)>=0,

because b^T x=beta, b^T y<=beta, zeta>=0, and zeta^T x=0. Thus x is the unique projection optimizer.

## 2. Normalization path

For fixed alpha, put H_alpha(gamma)=sum_i a_i[-b_i alpha+gamma+c_i]_+. This function is continuous, is zero for sufficiently negative gamma, tends to infinity, and is strictly increasing wherever positive. Therefore H_alpha(gamma)=2 has a unique solution gamma(alpha).

For every nonempty subset I define

A_I=sum_{i in I}a_i,
m_I=(sum_{i in I}a_i b_i)/A_I,
v_I=(2-sum_{i in I}a_i c_i)/A_I.

A sum of positive parts is the maximum of its subset sums. Consequently H_alpha(gamma)<=2 is equivalent to

gamma<=m_I alpha+v_I for every nonempty I.

The unique level-2 root is therefore

gamma(alpha)=min_{nonempty I}(m_I alpha+v_I). (2)

This finite minimum proves continuity, piecewise affinity, and concavity. Since b>=0, every m_I>=0, so the path is nondecreasing. Formula (2) is only an analytical representation; the algorithm does not enumerate subsets.

On any open interval with active set I={i:-b_i alpha+gamma(alpha)+c_i>0}, normalization gives gamma(alpha)=m_I alpha+v_I. The active set is nonempty.

For this affine formula, multiplying the i-th component by A_I gives

A_I[-b_i alpha+m_I alpha+v_I+c_i]
=sum_{k in I}a_k(b_k-b_i)alpha+2+sum_{k in I}a_k(c_i-c_k).

Condition 2 makes its constant term nonzero, so no such affine component is identically zero. If two distinct components i,j vanished simultaneously, their common alpha would equal delta_ij. Substitution in the preceding expression gives

2+sum_{k in I minus {i}}a_k(b_k-b_i)(delta_ij-delta_ik)=0,

contrary to condition 3. Thus every encountered zero belongs to exactly one coordinate.

## 3. Exact active-set construction

In the nontrivial regime the stated conditions imply q_i>0 for every i. To see this, use condition 2 with I equal to the full coordinate set. Since sum_k a_k c_k=2, its left side becomes c_i sum_k a_k, which cannot vanish. Since c_i>=0, it follows that c_i>0.

Thus gamma(0)=0 and every coordinate is initially active. Start at L=0 with I equal to the full coordinate set. Given the active set on the interval immediately to the right of L, compute A_I,m_I,v_I in O(n). Each component of the affine continuation is

g_i(alpha)=(m_I-b_i)alpha+v_I+c_i.

For each nonzero slope compute its root, retaining only roots strictly greater than L. Constant nonzero components have no root. Choose the smallest retained root R; if none exists, set R=infinity symbolically. This costs O(n).

No component changes sign in (L,R), so the current affine formula satisfies normalization there and agrees with gamma by uniqueness. It remains to justify a transition at finite R. Exactly one index j has g_j(R)=0. Toggle j's membership in I. The new set I' is nonempty: if the only active coordinate were removed, normalization at R would be zero rather than two. Because the toggled summand is zero at R, the old and new affine normalization formulas agree at R. Moreover,

m_{I'}-b_j=(A_I/A_{I'})(m_I-b_j).

Thus the sign of the crossing slope is preserved. The j-th component has the toggled sign immediately to the right of R. Every other component retains its strict sign by continuity and the absence of simultaneous zeros. This proves the transition invariant. Set L=R and repeat.

For termination, each g_i(alpha)=-b_i alpha+gamma(alpha)+c_i is concave, so its strict positivity set is an interval. Since g_i(0)=c_i>0, a coordinate can leave the active set at most once on [0,infinity), and cannot later re-enter. At least one coordinate remains active because normalization is two. There are therefore at most n-1 transitions and at most n pieces, in particular O(n) pieces and no more than 2n breakpoints. With O(n) work per piece, construction costs O(n^2). The same interval-of-positivity argument gives the source's enter-at-most-once and leave-at-most-once bound for a traversal of the whole real line.

All breakpoints used in arithmetic are finite roots of affine equations. Infinity is only a termination marker.

## 4. Moment equation and exact recovery

On a piece with active set I, define

F(alpha)=sum_i b_i a_i[-b_i alpha+gamma(alpha)+c_i]_+.

The stored active set gives

F(alpha)=A alpha+B,
A=sum_{i in I}b_i a_i(m_I-b_i),
B=sum_{i in I}b_i a_i(v_I+c_i).

These coefficients cost O(n) to compute. Continuity of gamma makes F continuous, including at breakpoints.

A finite nonnegative solution of F(alpha)=2 beta exists by the KKT argument in Section 1. There is also a direct endpoint verification. Initially F(0)=2 b^T q. On the final ray, each active component must have nonnegative slope, since otherwise it would have a later zero. Their a-weighted slopes sum to zero, so all active slopes vanish. Pairwise distinctness of b forces the final active set to be a singleton {j}. Every inactive component must have nonpositive slope on this ray, which implies b_j<=b_i for all i. Hence F is identically 2 min_i b_i on the final ray. Continuity therefore covers every target 2 beta in the stated feasible nontrivial interval, including its lower endpoint.

Scan the stored pieces. When A is nonzero, solve alpha=(2 beta-B)/A and check membership in that piece. When A=0, accept a finite point of the piece if B=2 beta, and otherwise continue. Shared endpoints may be assigned to either adjacent piece. On an unbounded final piece, use its finite left endpoint when accepting a constant solution; do not substitute infinity into an arithmetic expression. The scan costs O(n^2).

If a whole-real-line path is used instead, first intersect each piece with [0,infinity), skip empty intersections, and evaluate a singleton {0} directly. For a remaining interval [ell,u], an interior sample is (ell+u)/2 when u is finite and ell+1 when u=infinity. Retaining the active sets, as in the construction above, avoids sampling altogether. This implements and completes the recorded local source repair without changing the path or any admissible root.

Having found alpha, compute gamma from its affine piece and x from the positive-part formula. Section 1 proves exact optimality. Computing x and f(x) costs O(n). Combined with the trivial and infeasible cases, every promised projection is solved in O(n^2). For n=1, the feasible projection is always nominally feasible, so the nontrivial construction is never needed.

## 5. Bellman reduction

Fix an admissible v in [0,U]^n and a state s, and write b_a=r_{sa}+eta v. The policy simplex is nonempty, compact, and convex. The set Q_s is also nonempty, compact, and convex: it contains the nominal rows, is a closed subset of a finite product of simplices, and is defined by a convex quadratic budget inequality. The objective is continuous and bilinear in the policy and the tuple of transition rows. The stated minimax theorem therefore applies and gives

[T(v)]_s=min_{(x_a)_a in Q_s} max_a b_a^T x_a. (3)

The maximum over policies becomes a maximum over actions because a linear function on the policy simplex is maximized at an extreme point.

For theta>=0, the value in (3) is at most theta exactly when rows x_a exist with b_a^T x_a<=theta for every action and total squared deviation at most kappa. Each action-wise feasible set is compact when nonempty, and its minimum deviation is attained. Independence of the rows apart from the sum budget therefore gives the exact equivalence

[T(v)]_s<=theta
if and only if
sum_a P(q_{sa},W_{sa};b_a,theta)<=kappa. (4)

If an action-wise set is empty, both sides of the threshold-feasibility assertion are false, as encoded by its projection value +infinity. For a row with b_a^T q_{sa}=min_i(b_a)_i, every threshold yields either infeasibility or nominal feasibility. Every other row satisfies the explicit nondegeneracy promise at this v. Thus every nontrivial call in (4) is covered by the projection algorithm. One threshold test costs O(mn^2).

## 6. Accuracy and total cost

Let r_max=max_{s,a,i}(r_{sa})_i. Every coordinate of b_a lies in [0,U], since

0<=r_{sai}+eta v_i<=r_max+eta U=U.

Thus every Bellman coordinate lies in [0,U]. If U=0, return zero exactly. If epsilon>=U, returning zero already gives error at most epsilon.

Otherwise bisect [0,U] using (4), retaining an interval containing the Bellman coordinate. Each test halves its length, and after ceil(log_2(U/epsilon)) tests the length is at most epsilon. Returning a point in the final interval has absolute error at most epsilon. No logarithm needs to be evaluated by the algorithm; the stopping rule is the interval-length comparison.

Forming the b vectors and computing U costs O(mn^2), and output costs O(n). Including this work and performing the statewise computations gives

O(mn^3 [1+log(max{1,U/epsilon})]).

The operation bound is uniform in the numerical data in the exact real-arithmetic and comparison model. This proves the entire integrated theorem, with all listed obligations closed.
