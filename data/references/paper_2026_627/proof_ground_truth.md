# Reference Proof

## Proof Structure

1. Establish scale invariance and handle singleton feasible sets.
2. Derive the geometric inequality relating objective gap, distance to degeneracy, and decision distance.
3. Obtain the normalized-direction loss bound with constant L.
4. Establish conditional unbiasedness and bounded conditional ranges for active-pair importance-weighted excess losses.
5. Construct fixed-hypothesis martingales with predictable stopping and obtain a simultaneous deviation event.
6. Prove retention of h* by induction and derive the risk bound for every retained hypothesis, including after stopping.

## Source Reconciliation

The positive-round slack is the explicit sequence stated in the source's risk proof, r_t=2gamma L sqrt(log(2t|H|/delta)/t). The printed algorithm recursion omits the factors |H|/delta inside its logarithms and does not initialize r_1. Its forward reference to H_t in the sampling step is read as H_{t-1}. These source-local repairs are recorded in provenance. The source's individual-loss unbiasedness claim is replaced by active-pair excess-loss unbiasedness, which is the only unbiasedness needed. The risk comparison applies to the post-update set H_t. No external geometric theorem is assumed without proof below.

## Complete Proof

Write m=|H|, Delta=Delta(S), and rho=rho(C). The sets H_t are nonempty whenever defined: an empirical minimizer exists in the finite nonempty preceding set and is retained because r_t>=0. The empirical losses are finite, since only selected indices with positive sampling probabilities are used. For every prediction and label, 0<=ell(u,c)<=rho Delta, so all population risks exist. In particular, c^T w*(c)=min_{w in S}c^T w is a continuous function of c; the risk definition does not require any additional regularity of a label-dependent optimizer selection.

### 1. Scale invariance and geometry

For alpha>0, multiplying the linear objective by alpha preserves its minimizing set. Consistent tie breaking therefore gives w*(alpha u)=w*(u), and consequently ell(alpha u,c)=ell(u,c).

If Delta=0, S is a singleton, every SPO loss is zero, and the conclusion holds deterministically. Assume henceforth that Delta>0.

A nonempty bounded polyhedron is the convex hull of finitely many vertices. If a linear objective has a unique minimizer, that minimizer is one of these vertices. Its strict objective gaps to the other finitely many vertices show that it remains the unique minimizing vertex in a neighborhood of the objective. Thus the minimizing vertex is locally constant on the set of nondegenerate objectives. Along a segment containing no degenerate objective it is constant, since a locally constant map from an interval into a finite set is constant.

Let u satisfy nu_S(u)>0, and let w in S. Set w_u=w*(u) and d=w-w_u. Since S is not a singleton, zero is a degenerate cost vector, so nu_S(u) is finite. For epsilon>0 set q=nu_S(u)d/(Delta+epsilon). Since ||d||<=Delta, we have ||q||<nu_S(u). Every objective on the segment from u to u-q is at distance less than nu_S(u) from u, and therefore is nondegenerate. By the preceding local-constancy argument, w_u minimizes the objective u-q. Hence

(u-q)^T d>=0,

so

u^T(w-w*(u)) >= [nu_S(u)/(Delta+epsilon)]||w-w*(u)||^2.

Letting epsilon decrease to zero proves

u^T(w-w*(u)) >= [nu_S(u)/Delta]||w-w*(u)||^2.

This proves the required instance of the quoted geometric dependency directly.

### 2. Directional loss bound

Fix h_1,h_2 in H and a pool point x. Put v_j=h_j(x), u_j=v_j/||v_j||, and w_j=w*(v_j). Each v_j is nonzero and has positive distance to degeneracy by the margin assumption.

Apply the geometric inequality to (v_1,w_2) and (v_2,w_1), divide by ||v_1|| and ||v_2|| respectively, and use the margin assumption. The resulting inequalities are

u_1^T(w_2-w_1)>=(eta/Delta)||w_2-w_1||^2,

u_2^T(w_1-w_2)>=(eta/Delta)||w_1-w_2||^2.

Adding gives the correctly signed inequality

(2eta/Delta)||w_1-w_2||^2 <= (u_1-u_2)^T(w_2-w_1).

If w_1=w_2 the desired bound is immediate. Otherwise Cauchy-Schwarz and division by ||w_1-w_2|| give

||w_1-w_2|| <= [Delta/(2eta)]||u_1-u_2||.

Consequently, for every c in C,

|ell(h_1(x),c)-ell(h_2(x),c)|
=|c^T(w_1-w_2)|
<=L||h_1(x)/||h_1(x)||-h_2(x)/||h_2(x)||||.

This also holds in the previously separated singleton case.

Put B=gamma L. If B=0, the directional bound implies that every pair of hypotheses has identical loss at every pool point and every label: when gamma=0 all directional disagreements vanish, and when L=0 the displayed loss bound is zero directly. Thus every hypothesis has the same risk and the theorem holds deterministically. Assume B>0 for the remainder.

### 3. Active-pair importance weighting

Fix a population minimizer h* independently of the sequential observations. Write d_h=R_SPO(h)-R_SPO(h*)>=0 for each fixed h in H. Let F_{s-1} contain the observations and algorithmic choices through the preceding round. The confidence set, disagreement scores, and sampling probabilities at round s are F_{s-1}-measurable.

Suppose sampling is active and h,h* belong to H_{s-1}. Define

Y_s(h)=[mu_{I_s}/pi_{s,I_s}][ell(h(x_{I_s}),C_s)-ell(h*(x_{I_s}),C_s)].

For any selected index i, the directional bound gives

|Y_s(h)| <= [mu_i/pi_{s,i}]L p_{s,i}=mu_i P_s L<=gamma L=B.

Here mu_i<=1 and P_s<=gamma because H_{s-1} is a subset of H. If p_{s,i}=0, the two normalized predictions coincide, so their decisions and losses coincide. Therefore omitted sampling indices contribute zero to this pair's population risk difference. Using the specified fresh conditional label law,

E[Y_s(h)|F_{s-1}]
=sum_{i:p_{s,i}>0} mu_i E[ell(h(x_i),C)-ell(h*(x_i),C)|x_i]
=d_h.

No unbiasedness assertion for either individual weighted loss is needed. The equality holds even when mu_i=0 or some sampling probabilities vanish.

### 4. Globally defined stopped martingales

The preceding bounds cannot be applied globally by assuming in advance that h* survives. Instead, for each fixed h define the predictable indicator A_s(h) to equal one exactly when the procedure has not stopped, P_s>0, and h,h* both belong to H_{s-1}. Define

D_s(h)=Y_s(h)-d_h if A_s(h)=1,

D_s(h)=0 if A_s(h)=0.

The second branch does not require drawing an observation after stopping. Extend the filtration by recording no further observations after stopping.

On the active branch the conditional expectation calculation gives E[D_s(h)|F_{s-1}]=0; on the inactive branch this is immediate. Thus M_t(h)=sum_{s=1}^t D_s(h) is a martingale for every fixed h, with no prior retention assumption.

On the active branch D_s(h) lies in [-B-d_h,B-d_h], an interval of length 2B. On the inactive branch it lies in the singleton {0}. The endpoints of these intervals are F_{s-1}-measurable.

We use the following standard conditional-range Azuma-Hoeffding inequality. If martingale differences D_s lie in predictable intervals of lengths at most deterministic c_s, then

P(|sum_{s=1}^t D_s|>=u)<=2 exp(-2u^2/sum_{s=1}^t c_s^2).

All its hypotheses have just been verified with c_s=2B. In particular, it is interval width, not an unjustified absolute centered-increment bound B, that gives

P(|M_t(h)|>t r_t)
<=2 exp(-t r_t^2/(2B^2))
=delta^2/(2t^2 m^2).

Take a union bound over the m fixed hypotheses and all integer t>=1. Since sum_{t>=1}t^{-2}<2, the failure probability is at most

[delta^2/(2m)] sum_{t>=1}t^{-2}<delta^2/m<=delta.

Let E be the resulting event on which |M_t(h)|<=t r_t for every h and every t. It has probability at least 1-delta.

### 5. Retention and risk comparison

Work on E. Initially h* belongs to H_0. Suppose the procedure reaches an active round t and h* belongs to H_{t-1}. For every h in H_{t-1}, nestedness implies h,h* belonged to H_{s-1} at every earlier sampled round s<=t. Hence all the relevant indicators A_s(h) equal one, and

M_t(h)/t=hat R_t(h)-hat R_t(h*)-d_h.

Thus, simultaneously for all h in H_{t-1},

|hat R_t(h)-hat R_t(h*)-d_h|<=r_t.

Apply this to the empirical minimizer hhat_t. Since d_{hhat_t}>=0,

hat R_t(hhat_t)-hat R_t(h*)>=-r_t.

Therefore h* satisfies the retention inequality and belongs to H_t. This completes the induction without conditioning the martingale concentration on a future survival event.

For any h in H_t, empirical minimization and the definition of H_t give

hat R_t(h)<=hat R_t(hhat_t)+r_t<=hat R_t(h*)+r_t.

Combining this with the same excess-loss deviation inequality yields

R_SPO(h)-R_SPO(h*)=d_h<=2r_t
=4gamma L sqrt(log(2t|H|/delta)/t).

The argument holds on the single event E for every active round and every member of its retained set.

If the algorithm stops before round t, its current set H_{t-1} contains h* by the induction, including the immediate-stop case H_0. All directional disagreements in that set are zero. Consequently all its members have identical decisions at every pool point and the same risk as h*. Keeping that set thereafter gives excess risk zero for every subsequent horizon. The desired simultaneous statement follows.

## Obligation Closure

Scale invariance, geometric stability, the geometric inequality, the directional loss bound, support-aware conditional unbiasedness, predictable stopping, the concentration constants and all-time union bound, optimal-hypothesis retention, the final risk comparison, and the zero/stopping cases have all been established. The only concentration result invoked without proof is the standard independent inequality stated above, whose hypotheses are explicitly verified. There is no unresolved nonstandard dependency.
