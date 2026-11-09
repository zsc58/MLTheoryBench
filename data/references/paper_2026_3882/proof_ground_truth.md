# Reference Proof

## Theorem-Critical Obligations

1. Establish family-wise control for the specified testing rule and convert correct directional rejections into coverage of the entire task-level rank set.
2. Verify the endpoint indices and justify the common distribution of the observed and auxiliary future-task endpoints from the complete task-data sampling law.
3. Derive both finite-sample order-statistic inequalities, allowing arbitrary ties.
4. Establish the final event inclusion and combine the three error probabilities without assuming their independence.

All four obligations are closed below. No unsupplied rank-confidence or specialized conformal theorem is required.

## Step 1: Task-Level Coverage

Fix a model j and a task configuration t. First consider any one of its two testing families. Write K=M-1, beta=alpha_task/2, and let I_0 be the set of true null hypotheses in this family, with m_0=|I_0|.

If m_0=0, no false rejection is possible. Otherwise, suppose a true null is rejected, and let i be the position of the first true null in the sorted testing order. Because it is rejected, the procedure has reached this position and

q_(i) <= beta/(K-i+1).

All m_0 true null hypotheses occur at this position or later, so K-i+1 >= m_0. Consequently, a false rejection implies

min_{h in I_0} p_h <= beta/m_0.

For this fixed task configuration, super-uniformity and the union bound give

Q_t(any false rejection in this family)
<= sum_{h in I_0} Q_t(p_h <= beta/m_0)
<= m_0 beta/m_0 = beta.

This argument does not require independence among p-values and applies to the exact step-down rule in the task.

Apply the bound to both directional families. With Q_t-probability at least 1-alpha_task, neither family makes a false rejection. On this event, every k in W_j(t) satisfies mu_k(t)<mu_j(t), because its rejected null was mu_k(t)>=mu_j(t). Similarly, every k in B_j(t) satisfies mu_j(t)<mu_k(t). Therefore

L_j(t) <= l_j(t),
U_j(t) >= u_j(t),

and hence r_j(t) is contained in [L_j(t),U_j(t)]. Equality of true scores belongs to both relevant nulls, so this establishes coverage of the entire rank set even when scores tie. Averaging over the task distribution preserves the error bound alpha_task.

## Step 2: Sampling and Index Admissibility

For the proof only, augment the unseen task t* with an evaluation record D* sampled from Q_{t*}, independently of the observed records conditional on t*. This does not change the joint law of the observed records and t*, or any event involving the reported leaderboard interval and r_j(t*). The record D* is not available to the leaderboard construction.

Apply the same fixed testing rule to D* and write its task-level endpoints as L_j* and U_j*. The N observed complete task-data records and the augmented future record are iid. Consequently, for the fixed model, the N+1 lower endpoints are exchangeable, and the N+1 upper endpoints are exchangeable. Lower and upper endpoints need not be independent of one another.

Let a=(N+1)alpha_leader/2. The parameter range gives 1<=a<(N+1)/2. Thus k_l=floor(a)>=1, and

k_u=ceil(N+1-a)=N+1-floor(a)=N+1-k_l<=N.

Also k_l<=k_u, so both selected ascending order statistics are defined. At alpha_leader=2/(N+1), the indices are exactly k_l=1 and k_u=N. No endpoint-padding convention is needed in the public parameter range.

## Step 3: Order-Statistic Bounds with Ties

We derive the required elementary bound. Let Z_1,...,Z_m be exchangeable real random variables, with m=N+1, and fix 1<=k<=m-1. For each i, let Z^(-i)_(k) be the k-th ascending order statistic of the m-1 values other than Z_i. Define

A_i={Z_i<Z^(-i)_(k)},
B_i={Z_i>Z^(-i)_(k)}.

On A_i, at most k-1 of the other values are less than or equal to Z_i. Therefore Z_i is among the first k positions of the full sorted list, regardless of how equal values are ordered. Pathwise, at most k labels satisfy A_i.

On B_i, at least k of the other values are strictly smaller than Z_i. Therefore Z_i occupies one of the last m-k positions of the full sorted list. Pathwise, at most m-k labels satisfy B_i.

The leave-one-out events are permutation-equivariant. By exchangeability all A_i have the same probability, and all B_i have the same probability. Taking expectations of the two pathwise counts gives

P(A_m)=(1/m) E[sum_i 1_{A_i}] <= k/m,
P(B_m)=(1/m) E[sum_i 1_{B_i}] <= (m-k)/m.

Taking Z_m as the future value and the other values as the observed sample proves

P(Z*<Z_(k)) <= k/(N+1),
P(Z*>Z_(k)) <= (N+1-k)/(N+1).

These are strict-error inequalities. They remain valid with discrete values and arbitrary ties; no uniformity of unrandomized ranks is assumed. When there are no ties, the pathwise counts equal k and m-k, respectively.

Apply the first inequality to the lower endpoints at k=k_l:

P(L_j*<L_j) <= k_l/(N+1) <= alpha_leader/2.

Apply the second inequality to the upper endpoints at k=k_u:

P(U_j*>U_j) <= (N+1-k_u)/(N+1) <= alpha_leader/2.

## Step 4: Final Coverage

Define

E_0={r_j(t*) is not contained in [L_j*,U_j*]},
E_L={L_j*<L_j},
E_U={U_j*>U_j}.

Step 1 gives P(E_0)<=alpha_task. Step 3 bounds P(E_L) and P(E_U) by alpha_leader/2 each.

Outside their union,

L_j <= L_j* <= l_j(t*) <= u_j(t*) <= U_j* <= U_j.

Thus failure of the reported interval to contain r_j(t*) is contained in E_0 union E_L union E_U. The union bound yields

P(r_j(t*) is not contained in [L_j,U_j])
<= P(E_0)+P(E_L)+P(E_U)
<= alpha_task+alpha_leader.

The target event does not depend on the auxiliary D*, so this is exactly the probability in the public task. Taking complements proves the required guarantee for each fixed model j.

## Boundary and Interpretation Checks

The proof covers M=2, tied true scores, tied endpoint values, zero true nulls in a testing family, and the permitted equality alpha_leader=2/(N+1). It does not assert that the produced interval must be narrower than [1,M]. Under the usual set interpretation of [a,b], inverted endpoints on an error event give an empty interval; the event-inclusion argument remains valid and requires no additional coherence assumption on opposite-direction p-values. If alpha_task+alpha_leader>=1, the same calculation proves the stated, possibly vacuous, lower bound. No independence of the three error events, simultaneous guarantee across models, post-selection guarantee, or conditional-on-observed-data guarantee is asserted.
