# Reference Proof

## Audited Obligations and Standard Results

The obligations are: establish the relationship between minimum global sufficiency and reachable decision directions for the closed ellipsoid; prove lift feasibility and decision/loss preservation; identify the fixed-intercept classes and their equal risk infima; verify the compressed complexity and the actual finite-label SPO inequality; prove cumulative certification, independence, reconstruction, and stability; derive the numerical OLS radius; and transfer these events to candidate disagreement and learned-class excess risk. All are closed below.

The following standard independent results are used in their source-invoked forms.

1. A multiclass linear decision class with a fixed feature map in R^r and fixed label ordering has Natarajan dimension at most r.
2. For a vertex-valued decision class with K labels and Natarajan dimension at most r, iid contextual observations with true costs in C, and SPO loss bounded by omega, with probability at least 1-delta, simultaneously
   R_SPO(f) <= Rhat_SPO(f) + 2 omega sqrt(2r log(n K^2)/n) + omega sqrt(log(1/delta)/(2n)).
3. For a measurable, realizable stable sample-compression rule on iid examples, with observed compression size k and sample size N, with probability at least 1-delta its binary population risk is at most (4/N)(6k+log(e/delta)). Stability requires deletion of uncompressed examples to preserve the compressed reconstruction. In this application deletion also preserves the hard subsequence itself, with its inherited order.
4. For independent PSD matrices Y_i bounded above by I, with sum E[Y_i] >= N kappa I_p, matrix Chernoff gives
   P(lambda_min(sum Y_i)<N kappa/2) <= p exp(-N kappa/8).
5. The sphere in R^p has a 1/2-net of cardinality at most 5^p, and any g satisfies ||g|| <= 2 max_{u in the net}|u^T g|.

The hypotheses needed for each invocation are verified below. The specialized global-sufficiency characterization is not treated as a standard independent black box.

## 1. Global Sufficiency and the Closed Ellipsoid

Let V_C be the finite set of vertices optimal for some cost in C, and write W_0=span{x-y:x,y in V_C}. First, W_0 is globally sufficient. Indeed, if c,c' in C have equal W_0 measurements, their objective differences on every pair of vertices in V_C agree. Both optimal faces have vertices in V_C, so their minimizing vertices, and hence their entire optimal faces, agree.

We show that every globally sufficient subspace W contains W_0. Put N=W^perp. Fix a in C and let F be its optimal face. For any vector v, finiteness of the vertex set implies that, for all sufficiently small h>0, the optimal face at a+hv is the face of F minimizing v^T x: vertices outside F have a strictly positive objective gap at a.

If a is interior to C, then a+hv is feasible for every v in N and sufficiently small h. Global sufficiency gives the same optimal face F at a and a+hv. Thus v^T x is constant on F for every v in N, and every difference between vertices of F lies in W.

Suppose a is on the ellipsoid boundary and set g=Sigma^(-1)(a-c0), which is nonzero. If the restriction of g to N is nonzero, every v in N with g^T v<0 gives a+hv in C for sufficiently small positive h. Equal W measurements again force v^T x to be constant on F. These v form a relatively open half-space in N, so every difference between vertices of F annihilates all of N and lies in W.

If instead g annihilates N, then g lies in W. For each v in N, both a-hg and a+h(-g+v) belong to C for sufficiently small h>0: their first-order ellipsoid changes are negative. They have equal W measurements. Consequently the faces of F minimizing -g and -g+v agree. Pick a vertex x_0 minimizing -g over F. For every vertex x of F and every v in N, equality of these minimizing faces implies
   (-g+v)^T(x-x_0) >= 0.
Replacing v by any real multiple of itself forces v^T(x-x_0)=0. Thus every face direction again lies in W.

Finally, directions within optimal faces span W_0. To see this, join costs making any two reachable vertices optimal by a segment in C. Along that segment each vertex objective is affine in the segment parameter, so the lower envelope has finitely many pieces. Adjacent minimizing vertices are simultaneously optimal at a transition cost; endpoint choices also belong to their endpoint optimal faces. Telescoping their differences expresses the difference of the two original vertices as a sum of directions within optimal faces. Hence W_0 is contained in W.

Therefore W_0 is the unique minimum-dimensional globally sufficient subspace, and W_star=W_0. This establishes the identification needed here directly for the closed ellipsoid, rather than invoking an open-prior necessity statement.

## 2. Canonical Lift and Equality of Risk Infima

For a full-column-rank V with positive column dimension, minimize
   (1/2)(v-c0)^T Sigma^(-1)(v-c0)
subject to V^T(v-c0)=s. Stationarity gives v-c0=Sigma V lambda and lambda=(V^T Sigma V)^(-1)s. Strict convexity proves uniqueness, and substitution gives the stated L_V(s), its coordinate identity, and quadratic norm s^T(V^T Sigma V)^(-1)s. If s=pi_V(c) for c in C, the minimum is no greater than the feasible value at c, so L_V(s) lies in C. For zero columns, the unconstrained minimum is c0, exactly the stipulated empty-span lift.

For V=U, c and L_U(pi_U(c)) have equal measurements on W_star and both belong to C. Global sufficiency therefore gives identical optimal faces; fixed vertex ordering gives identical selected decisions. Consequently their induced SPO losses agree for every true cost in C. This is preservation of the prediction decision and its loss, not an assertion that true objective values at different costs are identical.

If f(z)=c0+Mz belongs to F_aff, its compressed version is
   f^c(z)=L_U(U^T(f(z)-c0))=c0+Sigma U(U^T Sigma U)^(-1)U^T Mz.
It belongs to F_star, is C-valued almost surely, and has identical risk. Conversely every member of F_star belongs to F_aff. Taking infima in both directions proves equality without assuming attainment.

## 3. Complexity and Uniform Generalization

Write J_U=Sigma U(U^T Sigma U)^(-1). Enlarge the compressed scores to predictors b c0+J_U Bz, with scalar b. For each vertex x define
   Psi(z,x)=(vec((J_U^T x)z^T), c0^T x) in R^(d_star p+1).
Their objective score is the inner product of Psi(z,x) with (vec(B),b). Thus their decisions belong to the fixed-feature multiclass linear class of dimension d_star p+1. The first audited standard result bounds its Natarajan dimension; restriction to b=1 and then to C-valued predictors cannot increase it.

There are K finite vertex labels. The oracle uses a fixed ordering, observations are iid, all decision/loss maps are measurable, and for every prediction decision x in X and true cost c in C,
   0 <= ell(c,x) <= omega_X(C).
The second standard result therefore gives exactly the task's uniform generalization inequality. No deletion of the K term or replacement by the previous label-independent expression is justified. The source inequality is defined for every n>=1, so no ambiguous large-dimension convention is needed. If X is a singleton, every loss is zero and the conclusion is immediate.

## 4. Cumulative Procedure and Compression

For a cost v in C and current query set D, the fibre is compact and nonempty. The anchor v has a selected optimal vertex and, by full row rank and nondegeneracy, a unique associated feasible basis B0. The displayed reduced-cost inequalities describe its optimality cone.

When all facet minima are nonnegative, the fibre is contained in that cone, so one vertex is optimal for every cost in the fibre. This is pointwise sufficiency. If a negative minimum is found, the chosen witness is in the fibre. Along the segment from the anchor to that witness, the first-hit rule gives a point a in the fibre at which the chosen reduced cost is zero while every other reduced cost is nonnegative.

The direction q=delta(B0,j_star) is an edge direction at the nondegenerate vertex x(B0). Because the polytope is bounded, the edge has another endpoint y=x(B0)+tau q for some tau>0. At the hit cost a, both endpoints are optimal: x(B0) is optimal and a^T q=0. Hence q lies in span(V_C-V_C)=W_star. This directly proves the relevance needed in the chain without relying on the external convex-prior characterization.

A new q cannot lie in the current query span. Otherwise its inner product would be constant throughout the fibre, but it is nonnegative at the anchor and negative at the witness. Every augmentation therefore increases rank by one, and all cumulative queries lie in W_star. Starting from the empty set yields at most d_star augmentations and termination of every run. If there are no nonbasic indices, containment is vacuous and the procedure stops.

Each processed sample is certified upon its run's completion, and subsequent fibre shrinkage preserves its certification. Thus the final set has zero empirical pointwise-sufficiency loss. Each hard sample adds at least one independent direction, so |T|<=|hat D|<=d_star.

All updates are deterministic functions of the current query set and current sample. Removing any non-hard sample removes an identity update. Inductively, the states at all remaining samples, their hard/non-hard statuses, and their query updates are unchanged. Consequently the hard subsequence reconstructs the output, and deleting any collection of uncompressed samples preserves that subsequence and the reconstruction. The measurable binary rule is the indicator of pointwise-sufficiency failure. This verifies realizability and stability for the third standard result.

Conditional on the regression sample, discovery contexts are iid and independent of that sample, so their pseudo-costs hat_mu(Z_j) are iid under the pushforward law of the fixed regression function. The complete range assumption makes these pseudo-costs C-valued. The compression result therefore gives, conditionally with probability at least 1-delta,
   P_Z(hat D is not pointwise sufficient at hat_mu(Z))
   <= beta := 4(6|T|+log(e/delta))/n_disc.
The probability on the left is over a fresh context with the learned objects held fixed.

## 5. Numerical OLS Radius

Let N=n_mu, let H have rows Z_i^T, and let G=H^T H. Since ||Z_i||<=1 and E[Z_i Z_i^T]>=kappa I, the matrix Chernoff statement gives
   P(lambda_min(G)<N kappa/2) <= p exp(-N kappa/8) <= delta_mu/2.
Thus the centered OLS design is invertible on an event of probability at least 1-delta_mu/2. The specified minimum-norm least-squares convention only defines the estimator outside this event and does not change it on the event.

For response coordinate j, write
   g_j=G^(-1/2)H^T epsilon^(j).
Conditional on all contexts, noises from different observations remain independent. For a unit u in R^p, set a=HG^(-1/2)u. Then ||a||=1, and conditional moment generating functions give
   E[exp(lambda u^T g_j)|H] <= exp(lambda^2 sigma^2/2).
Here coordinatewise subgaussianity follows from the stated directional assumption; independence across response coordinates is not required.

A 1/2-net of size at most 5^p, two-sided subgaussian tails, and the net inequality show, with conditional failure probability at most delta_j,
   ||g_j|| <= 2 sigma sqrt(2(p log 5+log(2/delta_j)))
            <= 4 sigma sqrt(p+log(2/delta_j)).
Take delta_j=delta_mu/(2d) and union over responses. With conditional failure probability at most delta_mu/2 this bound holds for every j. On its intersection with the Gram event,
   ||hat beta_j-beta_j||
   <= ||g_j||/sqrt(lambda_min(G))
   <= 4sqrt(2)sigma/sqrt(kappa) sqrt((p+log(4d/delta_mu))/N).
Sum the squared row bounds to obtain ||hat M_mu-M_mu||_F<=r_{mu,delta_mu}. Then, for every ||z||<=1,
   ||hat_mu(z)-mu(z)|| <= ||hat M_mu-M_mu||_F ||z|| <= r_{mu,delta_mu}.
The combined regression event has probability at least 1-delta_mu.

## 6. Transfer to Decisions and Risk

The canonical lift tilde_mu is C-valued almost surely and has the same learned measurements as hat_mu. Fix eta>0. On the events that hat D is pointwise sufficient at hat_mu(Z), regression error is at most eta, and dist(mu(Z),B_X)>eta, the mean and regression estimate have the same unique optimizer. Pointwise sufficiency supplies a common optimizer for hat_mu and tilde_mu. The complete source assumption that tilde_mu avoids B_X almost surely makes its optimum unique as well. Hence both selected decisions equal the mean's decision. A union bound yields
   P_Z(x^star(tilde_mu(Z)) != x^star(mu(Z)))
   <= P_Z(pointwise-sufficiency failure at hat_mu(Z))
      + P_Z(||hat_mu(Z)-mu(Z)||>eta) + C_marg eta^alpha.
On the regression event, choose eta=r if r>0. The tail vanishes, so intersection with the discovery certificate event gives beta+C_marg r^alpha. The joint event has probability at least 1-delta_mu-delta by conditional probability and a union bound.

If sigma=0, then r=0 and the regression event gives exact estimation. Apply the transfer inequality for every eta>0 and let eta decrease to zero. Since alpha>0, its margin term tends to zero. Thus the same displayed conclusion holds without applying an eta>0 lemma at eta=0. The margin assumption also implies P_Z(mu(Z) in B_X)=0 by continuity from above.

Because hat_mu(z)-c0=hat M_mu z, the candidate tilde_mu is a member of F_hat; its almost-sure C-valuedness was established above. Conditional expectation gives, for any fixed measurable predictor f,
   R_SPO(f)-R_SPO(mu)
   = E_Z[mu(Z)^T x^star(f(Z))-min_{x in X}mu(Z)^T x] >= 0.
The integrand is bounded by omega_X(C), and vanishes when the candidate and mean decisions agree. Since mu belongs to F_aff, R_SPO^aff=R_SPO(mu), the Bayes risk. Therefore
   inf_{f in F_hat} R_SPO(f)-R_SPO^aff
   <= R_SPO(tilde_mu)-R_SPO(mu)
   <= omega_X(C)[beta+C_marg r^alpha].
Every population risk minimizer in F_hat, if the infimum is attained, satisfies the same inequality. The lower bound zero follows from Bayes optimality. Replacing |T| by d_star is justified by the cumulative rank bound. No inference from excess risk to a risk minimizer's disagreement probability is made: the disagreement assertion concerns the explicitly defined candidate tilde_mu.
