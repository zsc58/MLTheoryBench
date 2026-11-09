# Reference Proof

## Proof Structure

First establish that the procedure is well-defined under the stated assumptions, without assuming separately that the action sets are finite. Use the M-convex local-exchange characterization and symmetric exchange to establish uniqueness for objectives with distinct coordinates. Distinguish the exact centroid from its coordinate-tie-broken estimate. On a mistake, an exchange reversed by the estimate is weakly reversed by the centroid, permitting an exact centroid cut. Every version space contains the order simplex associated with the hidden coordinate ordering. Combining its volume with geometric shrinkage bounds the number of mistakes, and bounded objective gaps give the stated regret bound.

## Complete Proof

### 1. Structural facts and existence of action maximizers

We use the following standard independent local-optimality result, stated in the source: for a nonempty M-convex set X contained in Z^d, x in X, and w in R^d,

`x in argmax_{y in X}<w,y>` if and only if `w(i)>=w(j)` for every distinct pair with `x-e_i+e_j in X`.

Its hypotheses hold for every action set in the task.

Two distinct points of an M-convex set cannot be coordinatewise comparable. Indeed, applying the exchange axiom to the larger point and a coordinate of strict inequality would require a coordinate with the opposite strict inequality. Thus, for distinct x,y, there is a coordinate i with x(i)>y(i), and symmetric exchange supplies j with x(j)<y(j), together with both x-e_i+e_j and y+e_i-e_j in X.

Fixing x and replacing y by y+e_i-e_j reduces its integer l1-distance to x by two. Repetition reaches x in finitely many steps. In particular, all points of X have the same coordinate sum.

For d=1, nonempty M-convex sets are therefore singletons. Suppose d>=2 and define

`delta=min_{i!=j}|w*(i)-w*(j)|>0`.

For a fixed round, let x=x_t be the stipulated optimizer for w*. During the preceding exchange procedure from an arbitrary y in X_t toward x, feasibility of x-e_i+e_j and optimality of x imply w*(i)>=w*(j); distinctness makes the difference at least delta. Each replacement of y therefore increases its true objective by at least delta. Consequently,

`delta * ||x-y||_1/2 <= <w*,x-y> <= B`.

Thus X_t lies in a finite integer l1-ball around x. Every linear objective attains its maximum on X_t. This also covers B=0: then every X_t is a singleton.

For any objective w with pairwise distinct coordinates, its maximizer is unique. If distinct x and y were both maximizers, choose a symmetric exchange pair as above. If w(i)>w(j), then y+e_i-e_j improves on y; if w(i)<w(j), then x-e_i+e_j improves on x. Either case contradicts optimality.

More generally, the strict-local-inequality consequence used by the original reference proof is valid, but not for its stated path reason: if all feasible nontrivial exchanges from x have w(i)>w(j), local optimality first makes x a maximizer. Any other maximizer y would admit the same symmetric exchange, and y+e_i-e_j would improve on y. No assertion that all exchanges along a path from x decrease the objective is needed.

The constant-sum fact also explains the public normalization of w*: adding a common constant to all weights does not change objective gaps, and positive scaling scales both gaps and B. Any finite vector with distinct coordinates can therefore be normalized into the unit box without changing the content of the bound.

### 2. Version spaces and coordinate tie-breaking

Every arc (i,j) added after round s belongs to E_s(x_s). Optimality of x_s gives

`w*(i)>=w*(j)`,

and distinctness gives strict inequality. Let pi order the hidden coordinates from largest to smallest. The set

`S_pi={w in [0,1]^d:w(pi(1))>=...>=w(pi(d))}`

is contained in every P_t. It has nonempty interior in R^d. Hence every P_t is a compact convex body with positive volume, and its centroid c_t exists.

For each (i,j) in A_t, the function w(i)-w(j) is nonnegative on P_t and strictly positive on a nonempty open subset of S_pi. Integration therefore gives c_t(i)>c_t(j). Similarly, 0<c_t(i)<1 for every coordinate. Consequently a sufficiently small perturbation of c_t can make all coordinates distinct while remaining in P_t and preserving every strict coordinate comparison of c_t. For example, use c_t+epsilon(1,2,...,d) with epsilon>0 small enough to preserve the finitely many strict comparisons and box inequalities. Equal coordinates of c_t then separate. This choice can depend only on P_t and a fixed rule, so it uses no current or future feedback.

The recommended maximizer exists and is unique by the structural facts above. The full update A_{t+1}=A_t union E_t(x_t) is consequently well-defined.

### 3. A mistake produces a centroid-compatible cut

Suppose x_t!=hat x_t. Because hat w_t has distinct coordinates, hat x_t is its unique maximizer. Thus x_t is not optimal for hat w_t. By the local-exchange characterization, some (i,j) in E_t(x_t) satisfies

`hat w_t(i)<hat w_t(j)`.

The coordinate tie-breaking preserves every strict comparison of c_t. Therefore c_t(i)>c_t(j) is impossible, and

`c_t(i)<=c_t(j)`.

This pair was not already in A_t, since the centroid strictly satisfies every existing arc. It is included in A_{t+1} by the full feedback update.

Set

`H={w in R^d:w(i)>=w(j)}`,

`G={w in R^d:w(i)-w(j)<=c_t(i)-c_t(j)}`.

The boundary of G passes through the exact centroid c_t. We use the following standard independent centroid theorem: for a compact convex body K with nonempty interior, either closed halfspace bounded by a hyperplane through its centroid contains at least Vol(K)/e of its volume. All hypotheses were verified for P_t above, so

`Vol(P_t intersect G)>=Vol(P_t)/e`.

Because c_t(i)-c_t(j)<=0, the intersection G intersect H is empty or contained in the hyperplane w(i)=w(j), which has zero d-dimensional volume. Also P_{t+1} is contained in P_t intersect H. Hence

`Vol(P_{t+1})<=(1-1/e)Vol(P_t)`.

On a round without a mistake, the full feedback update can still add arcs, but always P_{t+1} is contained in P_t. Thus volume never increases. Notice that the exact centroid theorem was applied to c_t, not to its perturbation.

### 4. Volume floor and mistake count

The d! coordinate orderings partition the unit cube apart from equality hyperplanes. Coordinate permutations preserve volume and map the corresponding order simplices onto each other. Each such simplex therefore has volume 1/d!. Since S_pi is contained in every version space,

`Vol(P_t)>=1/d!`.

Initially P_1=[0,1]^d has volume one. If m mistakes occur in rounds 1 through T, geometric shrinkage on those rounds and monotonicity on all other rounds give

`1/d! <= Vol(P_{T+1}) <= (1-1/e)^m`.

Taking logarithms yields

`m <= log(d!)/[-log(1-1/e)]`.

The final index is T+1 because the last observation updates A_T to A_{T+1}.

### 5. Regret conversion and boundary cases

Every round has nonnegative regret because x_t is a true optimizer. A correct recommendation has zero regret, and every mistaken recommendation has regret at most B. Therefore

`R_T <= Bm <= B log(d!)/[-log(1-1/e)]`.

For d>=2, log(d!)<=d log d<=d log(d+1), giving the claimed universal-constant O(B d log(d+1)) bound. For d=1, every action set is a singleton, so R_T=0, agreeing with log(1!)=0. For B=0 all objective gaps vanish, and the bound also holds. No constant depends on T.

## Source-Audit Notes

The source algorithm adds every feasible exchange arc after every round, not just one arc on a mistaken round. Its coordinate perturbation is interpreted as genuine tie-breaking, preserving comparisons that were already strict. The source's centroid-cut proof is locally completed by using the unperturbed centroid and allowing equality there. Its displayed final volume ratio requires P_{T+1} rather than P_T. These repairs retain the same target and proof architecture. All theorem-critical obligations are closed; no nonstandard external dependency remains unresolved.
