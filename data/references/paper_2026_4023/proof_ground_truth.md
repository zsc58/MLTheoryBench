# Reference Proof

All states and perturbations below lie on the memory boundary. The assumptions are integers L>=2 and l_0>=0, capacity M>l_0+L, continuous request masses, saturated waiting work, and the execute–evict–admit rule in the problem.

## 1. Boundary dynamics and equilibrium

Write w_j=l_0+1+j and let
\[
Q(x)=\sum_{j=1}^{L-1}w_jx_{j-1}
\]
be post-execution memory. If Q(x)<=M, then
\[
(Fx)_0=(M-Q(x))/w_0,\qquad (Fx)_j=x_{j-1}\quad(1\le j<L).
\]
If Q(x)>M, no mass is admitted, and LPF retains the later stages first, trimming the cutoff stage to make memory exactly M. In particular, for j>=1 the retained mass can be written
\[
(Fx)_j=\min\left\{x_{j-1},\frac{\bigl(M-\sum_{h=j+1}^{L-1}w_hx_{h-1}\bigr)_+}{w_j}\right\},
\]
and (Fx)_0=(M-Q(x))_+/w_0. These formulas show that F is continuous and piecewise affine.

Set
\[
W=\sum_{j=0}^{L-1}w_j=\frac{L(2l_0+L+1)}2,\qquad c_*=M/W.
\]
Then x^*=c_*\mathbf1 is an eviction-free fixed point. Conversely, a fixed point cannot have zero stage-0 mass: since (Fx)_j<=x_{j-1}, fixedness would force all its coordinates to vanish. Positive stage-0 mass implies positive admission and no eviction, so the shift equations force every coordinate to equal c_*. Thus x^* is the unique fixed point.

## 2. Physical-stage amplification and instability of the fixed point

During any eviction-free step,
\[
x'_0=x_{L-1}+\frac{\sum_{j=0}^{L-2}(x_{L-1}-x_j)}{l_0+1},\qquad x'_{j+1}=x_j.
\]
The maximum cannot decrease: a nonfinal maximizing coordinate is copied, while a final-stage maximum is replaced by a value at least as large. Similarly, the minimum cannot increase. Consequently the spread G=max x_j-min x_j cannot decrease.

Here is the quantitative boundedness argument that is needed; repeated strict growth alone would not suffice. Suppose an eviction-free trajectory with G^0>0 persisted forever. Its maximum U_n is nondecreasing and bounded by M/w_0, hence convergent. Put a_n=U_n-x^n_{L-1} and
\[
S_n=\sum_{j=0}^{L-2}(U_n-x_j^n).
\]
If a_n<=G^0/[2(l_0+L)], the final coordinate is not a minimum, so S_n>=G^0. The update gives
\[
x^{n+1}_0-U_n=\frac{S_n-(l_0+L)a_n}{l_0+1}
\ge\frac{G^0}{2(l_0+1)}.
\]
At any sufficiently late time t, choose a coordinate attaining U_t and follow that value until it reaches the final stage, within L-1 shifts. It is copied unchanged until then, even if larger admissions appear. Since U_n converges, the increase of U over this bounded interval tends to zero. Thus the displayed near-maximum hypothesis holds at that late final-stage event, forcing a fixed positive increase of U and contradicting convergence. Every nonfixed eviction-free trajectory therefore encounters an actual overflow in finite time.

For the cascade, the relevant first event is the first loss of a positive relative coordinate. Starting with full support, a strict overflow forces zero admission, and an exactly zero admission can also create a zero without strict overflow. Either event leaves full support. The preceding argument rules out indefinite full-support evolution away from x^*.

Every sufficiently small nonzero boundary perturbation of x^* has positive spread and eventually has a zero coordinate. In the sup norm, such a state is at distance at least c_* from x^*. Taking a fixed escape radius smaller than c_* proves Lyapunov instability. This also covers L=2.

## 3. Relative labels, sampled dynamics, and finite cascade

Label the circular positions so that label r occupies physical stage r+n modulo L at time n. When a final-stage cohort completes, any stage-0 admission inherits its label. A zero label stays zero under shifts. When it reaches the final stage, it releases no memory; all other mass grows, so post-execution memory is M plus the positive total surviving mass. Continuous LPF restores exactly M and leaves no admission slack. Hence the zero label cannot revive. The number of live labels is nonincreasing.

Consider an interval with a fixed live set of size m>=2. Sample states immediately before a live cohort completes. Order the live stages increasingly and write their positive predecessor gaps as g_0,...,g_{m-1}, with sum L. Set S_h=sum_{t=0}^h g_t. The live stages are S_h-1, their masses are y_h, and
\[
M=\sum_{h=0}^{m-1}(l_0+S_h)y_h.
\]
The next live completion is g_{m-1} physical updates away. If support is preserved during that interval, the completing label must receive a positive renewed cohort. This is the youngest cohort until the next sample. LPF cannot reach any older cohort without first exhausting it, which would lose its label. Thus all old nonfinal masses are copied unchanged. The gaps rotate to (g_{m-1},g_0,...,g_{m-2}), and subtracting the two sampled memory equations gives
\[
y'_{h+1}=y_h,\qquad
y'_0=\frac{(l_0+L)y_{m-1}-g_{m-1}\sum_{h=0}^{m-2}y_h}{l_0+g_{m-1}}.
\]
These sample intervals are not generally L-step blocks.

Normalize by u_h=y_h/g_h. Then
\[
u'_{h+1}=u_h,\qquad
u'_0=u_{m-1}+\frac{\sum_{h=0}^{m-2}g_h(u_{m-1}-u_h)}{l_0+g_{m-1}}.
\]
As before, the maximum U cannot decrease and the minimum cannot increase. Suppose a fixed-support trajectory has initial normalized spread G_0>0 and persists forever. Its coordinates are bounded by M/w_0, so U converges. For a sampled step, let a=U-u_{m-1} and S=sum_{h<m-1}g_h(U-u_h). If
\[
a\le\frac{G_0}{2(l_0+L)},
\]
a minimum remains among the copied coordinates and S>=G_0 because every g_h>=1. Hence
\[
u'_0-U=\frac{S-(l_0+L)a}{l_0+g_{m-1}}
\ge\frac{G_0}{2(l_0+L)}.
\]
Follow a maximizing coordinate from any late sample to the oldest slot, within m-1 sampled shifts. It retains its value until that slot, regardless of intervening new maxima. Convergence of U makes it arbitrarily close to the current maximum there, contradicting the fixed positive jump. Therefore support must shrink in finite time whenever the normalized spread is positive.

If instead all normalized coordinates equal c>0, the sampled update preserves this equality and rotates masses and gaps together. The boundary fixes c uniquely. This balanced continuation is physically feasible: during the interval associated with the oldest gap g, the renewed cohort's mass at age t, 0<=t<=g-1, is
\[
a_t=\frac{c\bigl((l_0+L)g-(t+1)(L-g)\bigr)}{l_0+1+t}.
\]
At t=g-1 this equals cg>0. Earlier values are positive and larger; the memory equation shows they decrease as the renewed cohort ages. Thus only the renewed cohort is trimmed during the intervening no-completion steps, and no old cohort is touched. After m sampled transitions the gap and mass vectors return, and the elapsed physical time is sum g_h=L. The balanced state therefore lies on a periodic physical orbit.

Every periodic physical orbit has constant support size, because relative support cannot increase. Its sampled representatives must be balanced, since positive normalized spread would force a support loss. In particular, all intermediate periodic orbits are precisely of the balanced kind relevant to the exceptional set. There are finitely many such orbit states: finitely many support and phase choices, each with its scalar c fixed by memory.

Starting from an arbitrary boundary state, either it is the fixed point, or it leaves full support in finite time, or it already has smaller support. On each subsequent fixed live set, either a balanced representative is reached or support shrinks in finite time. There are at most L-1 strict reductions. If only one coordinate remains, its value at stage j is M/w_j, and the trajectory follows
\[
C_j=\frac{M}{w_j}e_j,\qquad F(C_j)=C_{j+1\bmod L}.
\]
Thus every state is captured in finite time by a nonmaximal periodic orbit or reaches this unique maximal cycle.

For an intermediate cycle with m>=2, choose a sampled phase and arbitrarily small boundary perturbations within its support that make the normalized coordinates unequal. Such perturbations exist because that face has dimension m-1>=1. They force a support loss. The compact set of boundary states with at most m-1 positive coordinates is disjoint from the finite cycle, whose phases all have m positive coordinates; their distance is positive. The perturbed trajectories therefore leave a fixed neighborhood of the cycle. Every intermediate cycle is unstable.

## 4. Facewise measure zero of exact capture

Let B_I be the relative interior of a boundary face with nonempty support I, endowed with (|I|-1)-dimensional Lebesgue measure. For |I|=1 there is no nonmaximal capture.

For larger faces, fix a finite time horizon. The physical updates split states into finitely many polyhedral branch cells, determined by admission versus overflow and, on overflow, the LPF cutoff. On every nondegenerate cell the update is affine and has full rank onto the affine hull of its target support face. We verify this rather than assuming null sets have null preimages.

On a positive-admission branch, a final-stage coordinate must be present: without any completion, starting at memory M produces strictly positive overflow. The other source coordinates shift unchanged. They are independent coordinates on the source boundary face, since the completing mass is determined by its boundary equation. They are also independent target coordinates, since the admitted coordinate is determined by the target boundary. This branch is an affine isomorphism between the corresponding faces.

On an overflow branch, let q be the smallest stage with positive retained mass and put H=J\{q}, where J is the target support. The target coordinates indexed by H are unchanged shifted source coordinates. The remaining target coordinate is
\[
x'_q=\frac{M-\sum_{h\in H}w_hx'_h}{w_q}.
\]
The source coordinates x_{h-1}, h in H, are independent on the source boundary: the source contains the coordinate x_{q-1}, whose strictly positive weight allows it to be eliminated using the source memory equation. Complete the H-coordinates with the other free source coordinates. In these affine charts the branch is a projection (z,eta) -> z, hence a submersion. This also handles a loss caused by zero renewal of the completing label, whether or not an additional old stage is exhausted. If the target is a singleton face, full target rank is the vacuous rank-zero assertion.

The branch-switching equalities are proper affine equalities on every positive-dimensional current support face on which they can occur. For example, exact exhaustion of a cutoff stage requires the weighted sum of the strictly older retained source coordinates to equal M; this sum omits a positive source coordinate and is not identically M on the source face. The no-overflow/overflow equality is likewise proper when a completion is present and impossible when no completion is present. Structural zero coordinates are part of the face definition, not exceptional branch boundaries. Singleton faces follow the maximal cycle and cannot produce nonmaximal capture.

An affine submersion pulls relative null sets back to relative null sets: after affine coordinate changes it is a projection, and Fubini's theorem gives zero measure for the inverse image of a null set on each bounded branch cell. The cells here are bounded subsets of the memory boundary. Affine isomorphisms have the same property. Consequently, by induction over the finite horizon, preimages of the proper switching boundaries are null, and every remaining branch history is a composition of maps with the null-preimage property.

By Section 3, nonmaximal periodic states form a finite set on every positive-dimensional target face. Such a set is relatively null. Its preimage at any fixed time is therefore null in B_I. The set E of states captured at some finite time is the countable union of these null preimages over times 0,1,2,..., so E intersect B_I is null. This proves exactly the facewise measure statement, including empty exceptional intersections with singleton faces.

## 5. Local stability and finite absorption of the maximal cycle

Let C_max={C_0,...,C_{L-1}}. At phase C_r with r<L-1, post-execution memory exceeds M by M/w_r>0. At C_{L-1}, every request completes, so post-execution memory is zero and positive admission restores C_0. These strict inequalities persist in sufficiently small neighborhoods.

Fix epsilon>0 and an initial phase r. Continuity of the finitely many iterates F^k, 0<=k<=L, allows a neighborhood of C_r such that each of its first L iterates is within epsilon of the corresponding cycle phase, and each of its first L transitions has the same overflow-versus-positive-admission status as that phase. Thus, during this circuit, no admission occurs at any nonfinal principal phase, and precisely the final principal transition can admit new mass.

Every cohort present initially completes or is evicted within L updates. During those updates, at most one new cohort was admitted, at the designated principal renewal. It follows that F^L x has a single positive coordinate. Its support is the nominal phase r, so the boundary forces F^L x=C_r. Thereafter the trajectory lies exactly on C_max. Taking the minimum of the neighborhood radii over the finitely many phases proves Lyapunov stability and local finite absorption. In particular it proves the requested asymptotic stability outside E. No residual contraction factor is needed.

## 6. Assembly and dependency check

The unique fixed point is unstable by Section 2. Every intermediate cycle is unstable by Section 3. Section 4 identifies the exact nonmaximal capture set and proves its relative nullity on every support face. The finite support cascade shows that every initial state outside this set reaches C_max in finite time, and Section 5 supplies the local stability quantifiers. Once a trajectory reaches the cycle, its distance to the cycle is zero forever.

The attached worst-throughput result is not needed to replace any of these obligations. Its proof is independently valid: protecting the most-progressed M/(l_0+L) units of mass gives at least that many completions in every L-step window. A nonmaximal cycle has total mass strictly greater than M/(l_0+L) at every phase and a phase with positive completions; protecting a strictly larger mass at that phase yields a strict window inequality. Summing windows gives the throughput lower bound and its equality characterization. Importantly, equality does not mean that all phases have final-stage support: one visit to that phase determines the full maximal cycle, with phase-dependent masses M/w_j.

All theorem-critical obligations are explicitly closed above. The only general measure fact used is the projection/null-preimage consequence of Fubini, whose relevant form and bounded-cell hypotheses are given in Section 4.
