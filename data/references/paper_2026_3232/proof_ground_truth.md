# Reference Proof

## Proof Structure

Define free-observation continuation values operationally. Establish the first-step recursions, prove a uniform one-step lower bound by a deletion coupling and a probability-preserving swap, and then induct on the horizon. Infima are taken only after the coupling estimate has been made uniform over continuation policies.

## Complete Proof

Fix an admissible posterior \(\mu\). Write
\[
q_i=\Pr_\mu(b^\star=i),\qquad C(q)=\frac{1-\sum_iq_i^2}{2}.
\]
The best arm is measurable: its defining event is a countable intersection of score comparisons, including the prescribed tie rule. Thus \((q_i)\) is a probability distribution. All losses over \(n\) rounds lie in \([0,n]\), so every weighted sum below is finite.

### 1. Free-observation values and first-step recursions

For an integer \(n\ge0\), let
\[
H_i=(U_iL_n^\star)(\mu)
\]
be the infimum of the expected losses of all \(n\)-round policies that first receive and consume \(Y_{i,1}\) for free. Such a policy may use that observation, and future plays of arm \(i\) begin with \(Y_{i,2}\). The free observation is neither a round nor a mistake. Define
\[
K_i=(U_iL_n^{TS})(\mu)
\]
analogously, with Thompson sampling used for the counted rounds. These definitions do not assert that an infimum can be interchanged with a posterior expectation.

Fixing the first arm gives
\[
L_{n+1}^\star(\mu)=\inf_a\{1-q_a+H_a\}.\tag{1}
\]
Indeed, each policy constrained to start with \(a\) has exactly a free-observation continuation of the type defining \(H_a\), and conversely every such continuation can follow an initial play of \(a\). An independently randomized first action gives an average of constrained-policy costs and cannot improve their infimum. No minimizing arm or optimal continuation is required to exist.

Thompson sampling's first action has distribution \((q_i)\) independently of the actual arm data. Its mistake probability is \(1-\sum_iq_i^2\). Consequently,
\[
L_{n+1}^{TS}(\mu)=2C(q)+\sum_iq_iK_i.\tag{2}
\]

### 2. The one-step lower bound

We prove
\[
L_{n+1}^\star(\mu)\ge C(q)+\sum_iq_iH_i.\tag{3}
\]
By (1), it is enough to prove, for every arm \(a\),
\[
C(q)+\sum_iq_iH_i\le1-q_a+H_a.\tag{4}
\]
For \(n=0\), all \(H_i\) vanish, and
\[
1-q_a-C(q)=\frac{(1-q_a)^2}{2}+\frac12\sum_{i\ne a}q_i^2\ge0.
\]
Now suppose \(n\ge1\).

Fix a deterministic \(n\)-round policy \(F\) receiving \(Y_{a,1}\) for free. On a latent draw \(X\sim\mu\), write \(a_1,\ldots,a_n\) for its actions. Set
\[
a_0=a,\qquad R(X)=\{a_0,\ldots,a_n\},\qquad
J_i(X)=\begin{cases}i,&i\in R(X),\\a_n,&i\notin R(X).\end{cases}\tag{5}
\]
In particular, \(J_i(X)\in R(X)\) for every \(i\).

Construct a policy \(F^{(i)}\) receiving \(Y_{i,1}\) for free. Set \(F^{(a)}=F\). For \(i\ne a\), store the free observation without using it in decisions, play \(a\) once, and use the resulting observation to initialize a simulation of \(F\). Follow that simulation until \(n\) actual plays have occurred. If the simulation first selects \(i\) before stopping, insert the stored observation into the simulated history without making an actual play; thereafter continue the simulation normally.

This is an admissible policy. Before the first simulated selection of \(i\), the stored observation is ignored. At that selection it supplies exactly the next observation required by the simulation. Afterward the arm-local observation counts agree, so every subsequent actual observation is the one needed by the simulated policy. No unrevealed observation is used.

The counted actions of \(F^{(i)}\) are the list \(a_0,\ldots,a_n\) with one occurrence of \(J_i\) removed. If \(i=a\), remove \(a_0\). If \(i\ne a\) occurs among \(a_1,\ldots,a_{n-1}\), its first occurrence is supplied for free and removed. Otherwise the policy stops after the first \(n\) actions of the augmented list and removes \(a_n\). This agrees with (5), including when the first occurrence of \(i\) is \(a_n\).

Let \(\ell(F)\) and \(\ell(F^{(i)})\) be the respective counted losses in world \(X\). The action-list comparison gives the pathwise identity
\[
\ell(F^{(i)})-\ell(F)
=\mathbf1\{a\ne b_X^\star\}-\mathbf1\{J_i(X)\ne b_X^\star\}.\tag{6}
\]
Since \(H_i\le\mathbb E\ell(F^{(i)})\), averaging (6) with weights \(q_i\), and introducing an independent latent draw \(W\sim\mu\), yields
\[
\sum_iq_iH_i-\mathbb E\ell(F)
\le1-q_a-\Pr\bigl(J_{b_W^\star}(X)\ne b_X^\star\bigr).\tag{7}
\]
At this stage both \(J\) and the last probability may depend on \(F\); no infimum over \(F\) has been taken.

### 3. A uniform disagreement bound

For the fixed policy \(F\), define
\[
A=\{J_{b_W^\star}(X)\ne b_X^\star\}.
\]
Order pairs by
\[
(j,s)\succ(k,r)\quad\Longleftrightarrow\quad s>r\ \text{or}\ (s=r\text{ and }j<k).
\]
Let \(\theta_j^V\) denote arm \(j\)'s score in world \(V\), and define
\[
E=\{b_X^\star\ne b_W^\star,\ (b_W^\star,\theta_{b_W^\star}^W)\succ(b_X^\star,\theta_{b_X^\star}^X)\}.
\]
The unequal-index condition is essential. On that event the two best pairs are distinct, and exchanging \(X,W\) exchanges the two possible strict orderings. Therefore
\[
\Pr(E)=\frac12\Pr(b_X^\star\ne b_W^\star)=C(q).\tag{8}
\]

Define \(\Phi(X,W)=(X',W')\) by retaining both entire arm vectors for \(j\in R(X)\), and swapping \(X_j,W_j\) for every \(j\notin R(X)\).

We verify that this adaptive swap preserves probability. Let \(\mathcal T\) be the transcript of \(F\), consisting of its free observation and its \(n\) action-observation pairs. Conditional on \(\mathcal T\), the set \(R\) is fixed. The unobserved vectors \(X_j\), \(j\notin R\), retain their original independent arm laws and are conditionally independent of the remaining arm vectors. This follows by exposing the transcript in sequence: the next action is determined by the exposed history, and its observation concerns only its selected arm. Thus no step conditions on data from an arm absent from the final transcript. The independent world \(W\) is unaffected by conditioning on \(\mathcal T\). Hence, conditional on the transcript, the pairs \((X_j,W_j)\), \(j\notin R\), are independent and exchangeable, also independently of the retained vectors. Swapping them preserves the conditional law. For countably many arms, the same assertion follows on every finite-coordinate cylinder and hence on the product sigma-field.

All observed-arm vectors in \(X\) are retained, so the transcript in \(X'\) is again \(\mathcal T\). The set \(R\) is unchanged. Thus a second application swaps exactly the same arms, proving \(\Phi^2=\mathrm{id}\). The map is measurable, since the finite transcript and membership in \(R\) are measurable. It is therefore a probability-preserving involution. The transformed worlds have best arms almost surely because their joint law is unchanged.

Put \(B=E\cap A^c\). On \(B\),
\[
b_W^\star\ne b_X^\star,\qquad J_{b_W^\star}(X)=b_X^\star.
\]
If \(b_W^\star\in R\), (5) would make the second equality force the two best indices to agree. Therefore
\[
b_W^\star\notin R,\qquad b_X^\star=a_n\in R.\tag{9}
\]
Moreover, the best pair in \(W\) strictly exceeds the best pair in \(X\). It thus strictly exceeds every pair in \(X\) and every other pair in \(W\). Its entire arm vector moves to \(X'\), so
\[
b_{X'}^\star=b_W^\star\notin R,
\]
and the best pair in \(X'\) strictly exceeds the best pair in \(W'\). Consequently \((X',W')\notin E\).

The transcript and \(R\) are unchanged, and (5) gives
\[
J_{b_{W'}^\star}(X')\in R.
\]
This recomputed deletion index need not equal the old one, but its membership in \(R\) ensures that it differs from \(b_{X'}^\star\). Thus \((X',W')\in A\). We have proved
\[
\Phi(B)\subseteq A\setminus E.
\]
Since the involution preserves probability, \(\Pr(\Phi(B))=\Pr(B)\). The sets \(E\cap A\) and \(\Phi(B)\) are disjoint subsets of \(A\), whence
\[
\Pr(A)\ge\Pr(E\cap A)+\Pr(\Phi(B))=\Pr(E)=C(q).\tag{10}
\]
This proves the required bound uniformly over deterministic \(F\).

Substituting (10) into (7) gives
\[
C(q)+\sum_iq_iH_i\le1-q_a+\mathbb E\ell(F).
\]
A randomized policy is handled by fixing its independent private seed, applying the deterministic construction and bound, and averaging over that seed. Thus the last inequality holds for every free-observation continuation \(F\). Taking its infimum now gives (4), and then (1) gives (3).

### 4. Horizon induction

The target holds at horizon zero. Assume it holds at horizon \(n\) for every admissible posterior, and fix \(\mu\).

For arm \(i\), let \(\mu^{i,o}\) be the conditional law of the residual arm vectors after revealing and consuming \(Y_{i,1}=o\). It is admissible almost surely. For any \(n\)-round policy \(F\) using that free observation, let \(c_F(o)\) be its conditional expected loss. With \(o\) fixed, this is the cost of an admissible \(n\)-round policy for \(\mu^{i,o}\). The induction hypothesis gives, almost surely,
\[
L_n^{TS}(\mu^{i,o})\le2L_n^\star(\mu^{i,o})\le2c_F(o).
\]
Thompson sampling after the free observation is exactly Thompson sampling under this residual posterior. Integrating the last inequality therefore gives
\[
K_i\le2\mathbb E\ell(F).
\]
Taking the infimum over \(F\) yields \(K_i\le2H_i\). This argument needs neither an optimal policy nor measurable selection of posterior-wise optimizers.

Combining (2) and (3),
\[
\begin{aligned}
2L_{n+1}^\star(\mu)-L_{n+1}^{TS}(\mu)
&\ge2C(q)+2\sum_iq_iH_i-\left(2C(q)+\sum_iq_iK_i\right)\\
&=\sum_iq_i(2H_i-K_i)\ge0.
\end{aligned}
\]
The induction is uniform over admissible posteriors and proves the claim for every finite nonnegative integer horizon. The proof includes countably many arms, tied scores, and the cases where the best-arm distribution is concentrated on a single arm.
