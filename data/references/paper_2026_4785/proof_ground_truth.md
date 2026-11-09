# Reference Proof

## Proof Structure

We justify the trajectory distribution and its terminal marginal, establish a universal shortest-distance lower bound, construct a reward-matching policy attaining it by following shortest-path parents, and then prove the support characterization by comparing excess lengths.

## Complete Proof

### Trajectory probabilities and terminal marginals

Let \(T\) be the number of transitions taken by the reversed walk from \(s_f\) until it first reaches \(s_0\), setting \(T=+\infty\) on nontermination. Since the endpoints are distinct, \(T\ge1\). On termination, \(n_\tau=T-1\), and the same relation holds with the extended-value convention on nontermination. Hence the assumed finite expectation implies \(\mathbb E_B[T]<\infty\). If nontermination had probability \(p>0\), then \(\mathbb E_B[T]\ge mp\) for every positive integer \(m\), a contradiction. The walk therefore terminates almost surely.

There are countably many finite trajectories because the state space is finite. Each finite trajectory corresponds to one stopped reversed-walk event, with probability equal to the product of its backward transition probabilities. These events are disjoint and exhaust the termination event, so their probabilities sum to one. Thus \(\mathbb P_B\) is a probability distribution on finite trajectories.

Write \(q_x=R(x)/Z\). The terminal state of a forward-oriented trajectory is precisely the first state selected after \(s_f\) in the reversed walk. Consequently reward matching gives
\[
\mathbb P_B(s_{n_\tau}=x)=q_x>0\qquad(x\in X).
\]
This includes \(x=s_0\), if \((s_0,s_f)\in E\); that trajectory has \(n_\tau=0\).

### Universal lower bound

Since \(\mathbb E_B[n_\tau]<\infty\), conditioning on the terminal state gives
\[
\mathbb E_B[n_\tau]=\sum_{x\in X}q_x\,\mathbb E_B[n_\tau\mid s_{n_\tau}=x].
\]
Every trajectory ending at \(x\) is a directed walk from \(s_0\) to \(x\), before its final sink transition, so its length is at least \(\operatorname{cl}(x)\). Indeed, deleting any repeated-state portions yields a path no longer than the walk. Therefore
\[
\mathbb E_B[n_\tau\mid s_{n_\tau}=x]\ge\operatorname{cl}(x),\qquad
\mathbb E_B[n_\tau]\ge L_*:=\sum_{x\in X}q_x\operatorname{cl}(x).
\]

### Attainability

For each state \(s\notin\{s_0,s_f\}\), choose a predecessor \(\operatorname{par}(s)\) with an edge \(\operatorname{par}(s)\to s\) and
\[
\operatorname{cl}(s)=\operatorname{cl}(\operatorname{par}(s))+1.
\]
Such a predecessor exists by taking the last edge of a shortest path to \(s\). Its prefix is shortest to the predecessor, since otherwise the path to \(s\) could be shortened. The predecessor cannot be \(s_f\), which has no outgoing edges.

Define a backward policy by \(P_B(x\mid s_f)=q_x\) for \(x\in X\), and, for every \(s'\notin\{s_0,s_f\}\), set \(P_B(s\mid s')=1\) when \(s=\operatorname{par}(s')\) and zero otherwise. Stop the walk when it reaches \(s_0\); no parent or reversed-edge transition is required at \(s_0\). These prescriptions give a single state-dependent policy, even when shortest routes from different terminals share states.

Starting from \(s_f\), the first state is distributed as \(q_x\). If it is \(s_0\), the walk stops immediately. Otherwise, the distance \(\operatorname{cl}\) decreases by one at every subsequent transition until \(s_0\). Thus every realized trajectory ending at \(x\) has length \(\operatorname{cl}(x)\). Since there are finitely many terminal states and each distance is finite, this policy has finite expected length \(L_*\). Hence the minimum possible expectation is exactly \(L_*\).

### Necessity of shortest-path support

Suppose an admissible reward-matching policy gives positive probability to a trajectory \(\tau_*\) ending at \(x\) with \(n_{\tau_*}>\operatorname{cl}(x)\). All trajectories ending there have nonnegative excess length, so
\[
q_x\bigl(\mathbb E_B[n_\tau\mid s_{n_\tau}=x]-\operatorname{cl}(x)\bigr)
\ge \mathbb P_B(\tau_*)\bigl(n_{\tau_*}-\operatorname{cl}(x)\bigr)>0.
\]
All other terminal contributions to the excess over \(L_*\) are nonnegative. Therefore \(\mathbb E_B[n_\tau]>L_*\), and this policy is not minimizing.

### Sufficiency of shortest-path support

Conversely, suppose every trajectory with positive probability is shortest for its terminal state. Because the finite-trajectory space is countable and has total probability one, the length equals the corresponding shortest distance almost surely. Thus
\[
\mathbb E_B[n_\tau\mid s_{n_\tau}=x]=\operatorname{cl}(x)
\]
for every \(x\in X\). Reward matching gives \(\mathbb E_B[n_\tau]=L_*\), so the policy is minimizing. This proves the stated equivalence.
