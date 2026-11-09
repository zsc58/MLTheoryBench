# Reference Proof

## Obligations and Background Results

The proof must establish: compactness and continuity of the recursive dictionaries; both directions of the integral representation and its norm formula; existence for penalized fitting; an at-most-N atomic optimizer, including for initially nonatomic measures; recursive replacements that stay in the appropriate unit balls; the stated width count; and the feasible interpolation conclusion.

We use the following standard independent results. On a compact Hausdorff space D, Riesz-Markov-Kakutani identifies C(D)^* isometrically with finite signed Radon measures, with dual norm equal to total variation. Banach-Alaoglu makes each bounded closed dual ball weak-* compact. The dual norm is weak-* lower semicontinuous, since it is the supremum over the continuous functions mu -> |integral phi dmu| for ||phi||_infinity<=1. A nonempty compact convex subset of a Hausdorff locally convex space has an extreme point by Krein-Milman. The weak-* topology of a dual space is Hausdorff and locally convex. Below, every measure parameter space is compact metric, so these hypotheses hold. The remaining compactness and perturbation arguments are derived explicitly.

## 1. Compact Dictionaries and Continuous Atom Maps

The map (w,b) -> (x -> w^T x+b) from W times I into C(Omega) is continuous because

||w_n^T x+b_n-(w^T x+b)||_infinity <= ||w_n-w||_2 sup_{x in Omega}||x||_2+|b_n-b|.

Thus B_1 is compact. It is absolutely convex because W times I is convex and symmetric and the map is linear in its parameters.

For every activation in the public list, the normalized functions have the stated compact-uniform limits at zero and infinity. Here are direct checks of the endpoint behavior, kept private. Homogeneous activations are independent of scale. For a differentiable activation vanishing at zero, sigma(st)/s -> sigma'(0)t uniformly on bounded t-intervals by differentiability at zero. At a possible corner at zero, the same argument applies separately on the positive and negative half-intervals. This gives the linear zero-scale limits for the smooth centered activations and the hard saturating activations, and the corresponding piecewise-linear zero-scale limits for ELU and SELU.

For GELU, SiLU, and Mish, sigma(u)-u_+ is bounded on R and tends to zero at the relevant tails, so division by s gives the ReLU infinity-scale limit uniformly on bounded t-intervals. For ELU, CELU, and centered softplus, the difference from u_+ is bounded; their infinity-scale limit is also ReLU. For SELU the limit is kappa times ReLU. For bent identity, use ||st|-sqrt(s^2t^2+1)|<=1 to obtain the limit t+|t|/2. The remaining nonhomogeneous activations are bounded, giving the zero infinity-scale limit. The hard saturating activations are exactly linear near zero. These arguments also verify continuity of every endpoint function. They do not require particular numerical values of the positive SELU parameters.

Write S=[0,infinity], with compatible metric d_S(s,t)=|q(s)-q(t)|, where q(s)=s/(1+s) for finite s and q(infinity)=1. Suppose B_{r-1} is compact and let C=sup_{g in B_{r-1}}||g||_infinity. At a finite positive scale, continuity of (s,t) -> sigma_s(t) on bounded rectangles gives continuity of (s,g) -> sigma_s o g in C(Omega). At an endpoint e, use

||sigma_s o g-sigma_e o h||_infinity <= sup_{|t|<=C}|sigma_s(t)-sigma_e(t)|+||sigma_e o g-sigma_e o h||_infinity.

Compact-uniform convergence and uniform continuity of sigma_e on [-C,C] make the right side tend to zero as (s,g) -> (e,h). Consequently the atom map Phi_r on D_r=S times B_{r-1} is continuous and has compact image.

For completeness, the closed absolutely convex hull of a compact set A in a Banach space is compact. Choose a finite epsilon-net a_1,...,a_m for A. Every absolutely convex combination of points of A lies within epsilon of an absolutely convex combination of these a_j. The latter set is the continuous image of the compact finite-dimensional coefficient ball {c:sum_j|c_j|<=1}, hence compact and totally bounded. This proves total boundedness of absconv(A), and its closure is compact by completeness.

Endpoint atoms are limits of positive-scale atoms, so their inclusion does not change the closed absolutely convex hull. Induction therefore proves that each B_r is compact and each Phi_r is continuous. This recovers the compactness support used by the source without assuming its conclusion publicly.

## 2. Integral Representation and Norm Formula

For mu in M(D_r), define

(T_r mu)(x)=integral_{D_r} sigma_s(g(x)) dmu(s,g).

The continuous atom map has bounded compact image in C(Omega). A finite Borel partition on which that map oscillates by at most epsilon gives a uniform simple-function approximation. Thus the integral exists as a C(Omega)-valued integral and its scalar evaluations have the displayed pointwise form.

Let ||mu||_TV<=1. Choose such a partition E_1,...,E_m and representative atoms Phi_r(z_j). Then

f_epsilon=sum_j mu(E_j)Phi_r(z_j),

sum_j|mu(E_j)|<=||mu||_TV<=1,

and ||T_r mu-f_epsilon||_infinity<=epsilon||mu||_TV.

Each representative atom belongs to B_r, including at the endpoints. Hence f_epsilon belongs to B_r and closedness gives T_r mu in B_r. Alternatively, replacing the finitely many endpoint representatives by nearby positive-scale atoms gives finite positive-scale approximants with the same coefficient bound.

Conversely, let f in B_r and choose finite positive-scale absolutely convex sums f_n -> f uniformly. Associate to each sum its finitely supported signed measure mu_n. Repeated atoms may be merged; in every case ||mu_n||_TV<=1. By Riesz-Markov-Kakutani and Banach-Alaoglu, a subnet converges weak-* to some mu with ||mu||_TV<=1. For every x in Omega, the function (s,g) -> sigma_s(g(x)) is continuous on D_r. Therefore T_r mu_n(x) -> T_r mu(x), while uniform convergence of f_n gives the same limit f(x). Thus f=T_r mu.

We have proved

B_r={T_r mu:||mu||_TV<=1}.

Scaling gives V_r=T_r M(D_r) and

||f||_{V_r}=inf_{T_r mu=f}||mu||_TV.

Indeed any representing mu places f in ||mu||_TV B_r, and membership in cB_r supplies a representing measure of total variation at most c. For f=0 use the zero measure. A sequence of representing measures whose variations tend to the infimum lies in a fixed dual ball; a weak-* convergent subnet still represents f, and lower semicontinuity proves attainment of the infimum.

When sigma is homogeneous of degree q and normalized by s^q, all normalized activations, including their endpoints, equal sigma. Pushing a representing measure forward to B_{r-1} removes the scale coordinate without increasing variation. Conversely a measure on B_{r-1} can be lifted at any fixed positive scale with unchanged variation. Thus the scale-free infimum is the same.

## 3. Existence for Penalized Fitting

Let A_r mu=((T_r mu)(x_i))_{i=1}^N. Each coordinate of A_r is weak-* continuous. Set

H(mu)=sum_i ell(y_i,(A_L mu)_i)+lambda||mu||_TV.

The loss is finite-valued, so H(0)<infinity. A minimizing sequence can be chosen with H(mu_n)<=H(0)+1. Nonnegativity bounds ||mu_n||_TV by (H(0)+1)/lambda. A subnet has a weak-* limit mu_*. Lower semicontinuity of each loss and of total variation gives H(mu_*)<=liminf H(mu_n), so mu_* minimizes H.

The integral representation and norm formula imply that inf_mu H(mu)=inf_f J(f): every measure gives J(T_L mu)<=H(mu), and every f has a norm-attaining representing measure with H(mu)=J(f). Consequently f_*=T_L mu_* minimizes J, and ||mu_*||_TV=||f_*||_{V_L}; otherwise replacing its measure by a lower-variation representation would improve H.

Only the finitely many evaluation integrands are needed here. No unproved assertion that arbitrary weak-* convergence produces uniform convergence is used.

## 4. At Most N Atoms in a Minimal Prediction Fiber

Fix any feasible prediction vector z and put

t=inf{||mu||_TV:A_r mu=z}.

A bounded minimizing sequence and the same weak-* argument give attainment. The set

C_z={mu:A_r mu=z,||mu||_TV<=t}

is nonempty, convex, and weak-* compact. Every member has variation exactly t. If t=0, the zero measure is the sole member and already has no atoms. Otherwise choose an extreme point mu of C_z.

Suppose supp|mu| contains more than N points. Choose N+1 pairwise disjoint open neighborhoods E_j of distinct support points, each with |mu|(E_j)>0. Let mu_j be the restriction of mu to E_j. These are nonzero signed measures with disjoint supports. The N+1 vectors A_r mu_j in R^N are linearly dependent. Choose real a_j, not all zero, with sum_j a_j A_r mu_j=0 and define nu=sum_j a_j mu_j. Disjointness ensures nu!=0, and A_r nu=0.

For |epsilon| sufficiently small that 1+epsilon a_j>0 for every j,

||mu+epsilon nu||_TV=||mu||_TV+epsilon sum_j a_j||mu_j||_TV.

If the slope were nonzero, one sign of epsilon would lower variation while preserving z, contrary to the definition of t. The slope therefore vanishes. Both mu+epsilon nu and mu-epsilon nu belong to C_z and are distinct, while their midpoint is mu. This contradicts extremality.

Thus supp|mu| has at most N points. Because D_r is compact metric, it has a countable base. The complement of the support is a countable union of open |mu|-null sets and is null. Hence mu is a sum of at most N point masses, with total variation equal to the sum of the absolute merged coefficients. This argument covers nonatomic measures as well as finite atomic ones.

Apply this result to the optimal prediction vector z of f_*. Its least possible total variation equals ||f_*||_{V_L}, since a smaller value would give the same loss and strictly improve J. We obtain an optimal outer expansion

f(x)=sum_{j=1}^{n}c_j sigma_{s_j}(g_j(x)),

with n<=N, g_j in B_{L-1}, and sum_j|c_j|=||f_*||_{V_L}.

## 5. Inward Replacement and Widths

For each g in B_r with r>=2, consider the feasible prediction fiber with values (g(x_i))_i. A norm-attaining representation of g has total variation ||g||_{V_r}<=1. The least-variation atomic measure in this fiber therefore has at most N atoms and total variation at most one. It gives

h=sum_{j=1}^{n_g}b_j sigma_{t_j}(u_j),

where n_g<=N, u_j in B_{r-1}, sum_j|b_j|<=1, h in B_r, and h(x_i)=g(x_i) for every i.

Replace each outer input g_j by such an h. The outer predictions remain unchanged because its inputs agree at every sample point. The resulting function still has V_L norm at most sum_j|c_j|. Its norm cannot be smaller than the minimum for that prediction vector, so it is another optimizer.

Repeat this replacement for every constituent input at every lower level r>=2. Each new inner linear combination has coefficient sum at most one and therefore remains in the appropriate B_r. At r=1 stop: B_1 already consists of affine functions, and no nonexistent V_1 measure theorem is invoked.

This procedure produces a finite tree. Realize it as a layered network by placing the separate subtrees side by side and using zero connections between unrelated subtrees. The outermost hidden level has at most N neurons. Each neuron needs at most N neurons one level inward. Therefore, with the public indexing,

K_l<=N^{L-l},  l=1,...,L-1.

For L=2 this is K_1<=N. Vanishing branches can be discarded; the zero function permits empty widths.

For homogeneous activations every normalized neuron uses sigma itself. At a finite positive scale for a nonhomogeneous activation, sigma_s(u)=sigma(su)/s, so incoming parameters and outgoing coefficients can absorb the scale and normalization without changing widths. Endpoint neurons use the allowed limiting functions. Thus the finite normalized architecture has the network interpretation claimed in the task.

## 6. Feasible Interpolation

For the public interpolation target, choose any feasible f_0 and a finite representing measure. Minimize total variation over A_L mu=y in the ball with radius ||f_0||_{V_L}. The fiber is weak-* closed, the ball is weak-* compact, and total variation is weak-* lower semicontinuous, giving a minimum. The norm formula identifies this minimum with the minimum V_L norm of an interpolant.

Apply Sections 4 and 5 to obtain a finite minimum-norm interpolant with the same widths. Duplicate-input consistency follows necessarily from feasibility. The proof actually works for any feasible fiber, including with a linear activation; it in particular proves the nonlinear case requested publicly. It does not need to establish feasibility for every consistent dataset, and therefore has no unresolved universal-approximation dependency.

All theorem-critical obligations of the public task are closed.
