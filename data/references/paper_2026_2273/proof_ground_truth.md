# Reference Proof

## Proof Obligations

We establish: (1) well-defined policy values and an optimal deterministic stationary policy attaining the componentwise maximum; (2) the value shift and advantage identities; (3) existence and pointwise characterization of normal rewards; (4) orbit uniqueness; (5) continuity and both inverse identities for the product map; and (6) a continuous, free, fiber-transitive action with an equivariant trivialization. All arguments apply to every fixed discount \(0\leq\gamma<1\).

## Complete Proof

### 1. Policy values and Bellman optimality

For every policy \(\pi\), the matrix \(P_\pi\) is row-stochastic, so its operator norm for the supremum norm is one. The matrix series
\[
 A_\pi=\sum_{k=0}^{\infty}\gamma^kP_\pi^k
\]
converges. Multiplying its finite partial sums by \(I-\gamma P_\pi\) and passing to the limit shows that \(A_\pi=(I-\gamma P_\pi)^{-1}\). Its entries are nonnegative. Consequently
\[
 v_{\pi,r}=A_\pi r_\pi,
 \qquad \|v_{\pi,r}\|_\infty\leq\frac{\|r\|_\infty}{1-\gamma}.
\]
In particular, each policy-value map is linear and continuous in \(r\).

Define, privately for the proof,
\[
 (T_rw)(x)=\max_{u\in U_x}\left(r(u)+\gamma\sum_y p(y\mid u)w(y)\right).
\]
The maxima exist because the action fibers are finite and nonempty. Stochasticity and the elementary inequality for differences of maxima give
\[
 \|T_rw-T_rz\|_\infty\leq\gamma\|w-z\|_\infty.
\]
To see existence of a fixed point directly, start with \(w_0=0\) and set \(w_{k+1}=T_rw_k\). Successive differences are bounded by \(\gamma^k\|w_1-w_0\|_\infty\), so the geometric-series estimate makes the sequence Cauchy. Its limit \(w\) satisfies \(T_rw=w\) by continuity. The same contraction estimate proves uniqueness of this fixed point. This argument includes \(\gamma=0\), when \(T_r\) is constant.

Choose \(\pi^*(x)\) attaining the maximum defining \(T_rw(x)\). Then
\[
 w=r_{\pi^*}+\gamma P_{\pi^*}w,
\]
so \(w=v_{\pi^*,r}\). For any policy \(\pi\), the vector
\[
 d_\pi=w-r_\pi-\gamma P_\pi w
\]
is nonnegative. Hence
\[
 w-v_{\pi,r}=(I-\gamma P_\pi)^{-1}d_\pi\geq0.
\]
Thus one policy attains the componentwise maximum simultaneously at all states, \(w=v_r^*\), and
\[
 T_rv_r^*=v_r^*.
\]
In particular, the advantages of an optimal policy are nonpositive on all actions and zero on its selected actions. Conversely, if a policy has nonpositive advantages, its value is a fixed point of \(T_r\), since its selected-action advantages vanish. It is therefore optimal.

### 2. Transformation identities

Write
\[
 b_\delta(u)=\gamma\sum_y p(y\mid u)\delta(y)-\delta(s(u)),
 \qquad \ell_\delta r=r+b_\delta.
\]
Linearity in \(\delta\) gives \(\ell_0=\mathrm{id}\) and \(\ell_\eta\ell_\delta=\ell_{\eta+\delta}\). The action is jointly continuous.

If \(r'=\ell_\delta r\), then
\[
 r'_\pi=r_\pi-(I-\gamma P_\pi)\delta.
\]
Applying the Bellman inverse gives
\[
 v_{\pi,r'}=v_{\pi,r}-\delta.
\]
Taking the componentwise maximum over the same finite policy set yields
\[
 v_{\ell_\delta r}^*=v_r^*-\delta.
\]
It also follows that the set of optimal policies is unchanged.

Substitution in the definition of advantage gives, for every action,
\[
 \operatorname{adv}_{\pi,r'}(u)
 =r(u)+\gamma\sum_y p(y\mid u)v_{\pi,r}(y)-v_{\pi,r}(s(u))
 =\operatorname{adv}_{\pi,r}(u).
\]
Setting \(\delta=v_{\pi,r}\) in the transformation formula also gives
\[
 \ell_{v_{\pi,r}}r=\operatorname{adv}_{\pi,r}.
\]
These identities are derived here rather than assumed from the nonstandard prior-paper citation.

For completeness, if \(b_\delta=0\), its restriction to any policy gives \((I-\gamma P_\pi)\delta=0\), and therefore \(\delta=0\). Thus the translation action is faithful and, in fact, free.

### 3. Existence and characterization of normal rewards

For any reward \(r\), set \(n=\ell_{v_r^*}r\). The optimal-value shift gives
\[
 v_n^*=v_r^*-v_r^*=0,
\]
so each orbit contains a normal reward. Equivalently, for an optimal policy \(\pi^*\), the advantage identity gives \(n=\operatorname{adv}_{\pi^*,r}\), which is nonpositive and vanishes on the selected actions.

If \(r\) is normal, the Bellman optimality equation at zero reads
\[
 0=(T_r0)(x)=\max_{u\in U_x}r(u)
\]
for every state. Conversely, if all these maxima are zero, every reward is nonpositive and a policy selecting a maximizing action at each state has selected rewards zero and value zero. Every policy value is nonpositive, either by the nonnegative Bellman inverse or by the discounted series. Therefore the componentwise maximum of the policy values is zero, and \(r\) is normal. This proves the claimed characterization of \(N\).

### 4. Orbit uniqueness

If \(n'=\ell_\delta n\) and both rewards are normal, the optimal-value shift immediately gives
\[
 0=v_{n'}^*=v_n^*-\delta=-\delta.
\]
Thus \(\delta=0\) and \(n'=n\).

The corresponding policy-operator argument is also valid: an optimal policy for \(n\) remains optimal for \(n'\), and both of its value vectors and selected-reward vectors are zero. Restricting the transformation to that policy yields \(0=(\gamma P_\pi-I)\delta\), and invertibility gives the same conclusion.

### 5. Product homeomorphism

There are finitely many deterministic stationary policies. Each policy value is linear and continuous in \(r\), so their componentwise maximum \(v_r^*\) is continuous. Therefore
\[
 P(r)=r+b_{v_r^*}
\]
is continuous as a map into \(N\) with its relative topology. It restricts to the identity on \(N\).

Let
\[
 \Phi(r)=(P(r),v_r^*),
 \qquad H(n,\delta)=\ell_{-\delta}n.
\]
Both maps are continuous. The action law gives
\[
 H(\Phi(r))=\ell_{-v_r^*}\ell_{v_r^*}r=r.
\]
Conversely, if \(n\in N\), then the optimal-value shift gives
\[
 v_{H(n,\delta)}^*=v_n^*+\delta=\delta,
 \qquad P(H(n,\delta))=\ell_\delta\ell_{-\delta}n=n.
\]
Hence \(\Phi(H(n,\delta))=(n,\delta)\). These identities establish the asserted homeomorphism and its inverse.

### 6. Principal-bundle structure

For any group parameter \(\eta\), the action law and optimal-value shift imply
\[
 P(\ell_\eta r)=P(r),
 \qquad \Phi(\ell_\eta r)=(P(r),v_r^*-\eta).
\]
Thus the action preserves fibers. In these coordinates it is free, and any two points \((n,\delta_1)\), \((n,\delta_2)\) in one fiber are related by the unique parameter \(\eta=\delta_1-\delta_2\).

To verify equivariance with the standard additive right action, use the sign-reversed global chart
\[
 \Psi(r)=(P(r),-v_r^*).
\]
This is a homeomorphism, and if \(\Psi(r)=(n,a)\), then
\[
 \Psi(\ell_\eta r)=(n,a+\eta).
\]
Since the group is abelian, the stated action is also a right action. The chart is a global equivariant trivialization over \(N\), proving the principal-bundle claim. The sign reversal changes only the equivariant chart, not the homeomorphism or inverse requested in the task.

## Private Source-Proof Repair

The source's quotient proof includes the unnecessary and false assertion that the whole orbit quotient map is closed. The direct finite-policy continuity proof above avoids that assertion. Its intended quotient argument can also be completed locally: if \(A\) is closed in \(N\) and \(r_j=n_j-b_{\delta_j}\) in its saturation converges, then \(\delta_j=v_{r_j}^*\) is bounded by \(\|r_j\|_\infty/(1-\gamma)\). A convergent subsequence of \(\delta_j\) makes \(n_j=r_j+b_{\delta_j}\) converge to a point of \(A\), proving that the saturation is closed. Here \(N\) is closed because it is defined by finitely many continuous statewise-maximum equations. Therefore the restriction of the quotient map to \(N\), not the whole quotient map, is a closed continuous bijection and a homeomorphism.

All theorem-critical obligations are closed; no external specialized result is assumed.
