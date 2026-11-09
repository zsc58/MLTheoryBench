# Reference Proof

Write $V_k=V^{\pi_k}$, $Q_k=Q^{\pi_k}$, $\delta_k=\|V^*-V_k\|_\infty$, and $b_s^\pi=\sum_{a\notin A_s^*}\pi(a\mid s)$. The assumption $\widetilde S\ne\varnothing$ implies $|A|\ge2$. The mirror assumptions imply that $0\in\operatorname{int}(\operatorname{dom}\psi)$, $1\in\operatorname{bd}(\operatorname{dom}\psi)$, and $c_0:=\psi'(0)=\psi'(0+)$ is finite. In particular, zero coordinates have well-defined dual scores; a coordinate equal to one does not belong to the interior domain.

## Preliminary bounds and the update

For any policy $\pi$, put $e^\pi(s)=\sum_a\pi(a\mid s)[V^*(s)-Q^*(s,a)]$. Bellman equations give $V^*-V^\pi=e^\pi+\gamma P^\pi(V^*-V^\pi)$. Since optimal actions contribute zero and $0\le V^*(s)-Q^*(s,a)\le(1-\gamma)^{-1}$, $\Delta b_s^\pi\le e^\pi(s)\le(1-\gamma)^{-1}b_s^\pi$. For the probability measure $d_s^\pi=(1-\gamma)\sum_{t\ge0}\gamma^t(P^\pi)^t(s,\cdot)$, the nonnegative Bellman resolvent therefore yields
\[
\Delta b_s^\pi\le V^*(s)-V^\pi(s)\le(1-\gamma)^{-2}\mathbb E_{x\sim d_s^\pi}b_x^\pi. \tag{1}
\]
This derivation also applies at $\gamma=0$.

At each state the update has a unique maximizer. Its coordinates stay in $\operatorname{int}(\operatorname{dom}\psi)$: zero is already interior, and a maximizer with one coordinate equal to one admits an improving direction toward another coordinate, because $\psi'(t)\to+\infty$ as $t\uparrow1$ while the other coordinate has a finite derivative at zero. Induction starts from the assumed initialization. First-order optimality on the simplex consequently gives, with state-dependent multipliers,
\[
\psi'(\pi_{k+1}(a\mid s))=\psi'(\pi_k(a\mid s))+\eta Q_k(s,a)+\nu_{k,s}+\lambda_{k,s}(a),\quad
\lambda_{k,s}(a)\ge0,\quad\lambda_{k,s}(a)\pi_{k+1}(a\mid s)=0. \tag{2}
\]
In particular, the multiplier vanishes for a positive updated coordinate, but it must not be discarded at a zero coordinate. The same first-order condition and the Bregman three-point identity give, for every $p\in\Delta(A)$,
\[
\eta\langle\pi_{k+1}(\cdot\mid s)-p,Q_k(s,\cdot)\rangle\ge D_h(\pi_{k+1}\|\pi_k)(s)+D_h(p\|\pi_{k+1})(s)-D_h(p\|\pi_k)(s). \tag{3}
\]
All divergences here are finite because their second arguments have interior coordinates.

For completeness, value convergence need not be taken from a PMD-specific citation. Let $J_k(s)=\langle\pi_{k+1}(\cdot\mid s)-\pi_k(\cdot\mid s),Q_k(s,\cdot)\rangle$. Comparing the update with $\pi_k$ gives $\eta J_k(s)\ge D_h(\pi_{k+1}\|\pi_k)(s)\ge0$. Bellman equations then give $V_{k+1}-V_k=(I-\gamma P^{\pi_{k+1}})^{-1}J_k\ge J_k\ge0$; hence $V_k$ and $Q_k$ improve componentwise. Fix an optimal $\pi^*$ and write $d_s^{\pi^*}$ for its discounted visitation measure. The performance-difference identity and (3) imply
\[
\delta_k(s):=V^*(s)-V_k(s)
=\frac{\mathbb E_{x\sim d_s^{\pi^*}}\langle\pi^*(\cdot\mid x)-\pi_k(\cdot\mid x),Q_k(x,\cdot)\rangle}{1-\gamma}
\le\frac{\mathbb E_{x\sim d_s^{\pi^*}}[D_h(\pi^*\|\pi_k)(x)-D_h(\pi^*\|\pi_{k+1})(x)]}{\eta(1-\gamma)}
+\frac{\mathbb E_{x\sim d_s^{\pi^*}}J_k(x)}{1-\gamma}.
\]
The visitation measure is fixed as $k$ varies. Sum from $k=0$ to $n$: the divergence telescopes, while $\sum_{k=0}^nJ_k(x)\le V_{n+1}(x)-V_0(x)\le(1-\gamma)^{-1}$. Because each $\delta_k(s)$ decreases,
\[
\delta_n\le\frac1{n+1}\left(\frac{\max_xD_h(\pi^*\|\pi_0)(x)}{\eta(1-\gamma)}+\frac1{(1-\gamma)^2}\right)\longrightarrow0. \tag{4}
\]
Thus (1) implies $b_s^{\pi_k}\to0$ for every state, and $\|Q^*-Q_k\|_\infty\le\gamma\delta_k$.

## Dual gaps, absorption, and summability

For $s\in\widetilde S$, define
\[
G_k(s)=\min_{a^*\in A_s^*}\psi'(\pi_k(a^*\mid s))-\max_{a'\notin A_s^*}\psi'(\pi_k(a'\mid s)),\qquad
G_k(s,a')=\max_{a^*\in A_s^*}\psi'(\pi_k(a^*\mid s))-\psi'(\pi_k(a'\mid s)).
\]
Fix $0<\sigma<\Delta/2$ and choose $T$ so that $\delta_k\le\sigma$ for $k\ge T$. Compare in (2) the updated optimal coordinate attaining the minimum with the updated positive suboptimal coordinate attaining the maximum. The former multiplier is nonnegative and the latter is zero; comparing their $Q_k$ values with $Q^*$ proves
\[
b_s^{\pi_{k+1}}>0\quad\Longrightarrow\quad G_{k+1}(s)\ge G_k(s)+\eta(\Delta_s-2\sigma). \tag{5}
\]
For fixed $a'\notin A_s^*$, compare instead the updated positive optimal coordinate attaining the maximum with $a'$, whose multiplier is nonnegative. This gives
\[
b_s^{\pi_{k+1}}<1\quad\Longrightarrow\quad G_{k+1}(s,a')\le G_k(s,a')+\eta[V^*(s)-Q^*(s,a')+2\sigma]. \tag{6}
\]
These comparisons remain valid if the fixed suboptimal coordinate is zero.

If $k\ge T$ and $b_s^{\pi_k}=0$, then $b_s^{\pi_{k+1}}=0$. Otherwise a newly positive suboptimal coordinate $a'$ and conservation of total mass supply an optimal coordinate $a^*$ with $\pi_{k+1}(a^*\mid s)<\pi_k(a^*\mid s)$. Strict increase of $\psi'$ makes the change in the dual score of $a^*$ negative and that of $a'$ positive. Subtracting their equations (2), however, says the first change minus the second is at least $\eta(\Delta_s-2\sigma)>0$, a contradiction. Induction proves persistence. If all suboptimal masses are zero, (1) makes the policy optimal. Then $Q_k=Q^*$, and its supported actions maximize $Q^*$; nonnegativity and strict definiteness of $D_h$ show directly from the update that the policy remains unchanged.

Take $\sigma=\Delta/4$. At a nontrivial state, either its suboptimal mass eventually becomes zero, or it stays positive for all $k\ge T$. In the latter case, apply the *per-state* form of (5), including the elementary strengthening missing from the displayed source proof:
\[
G_k(s)\ge G_T(s)+\eta(\Delta_s-\Delta/2)(k-T)
\ge G_T(s)+\eta\Delta_s(k-T)/2. \tag{7}
\]
Every suboptimal score is at least $c_0$. Also each optimal coordinate is at most $1-b_s^{\pi_k}$. Consequently $\chi(b_s^{\pi_k})=\psi'(1-b_s^{\pi_k})\ge c_0+G_k(s)$, and (7) gives, after a finite index at which the inverse argument enters its domain,
\[
b_s^{\pi_k}\le\chi^{-1}\big(c_0+G_T(s)+\eta\Delta_s(k-T)/2\big). \tag{8}
\]
Near zero, $\chi$ is nonnegative, strictly decreasing, and unbounded. Closed convexity and finiteness of $\psi(1)$ give $\int_0^\epsilon\chi(x)\,dx=\psi(1)-\psi(1-\epsilon)<\infty$. The area identity $\int_{\chi(\epsilon)}^\infty\chi^{-1}(y)\,dy=\int_0^\epsilon\chi(x)\,dx-\epsilon\chi(\epsilon)$ and monotonicity of $\chi^{-1}$ show that its values along any positive-slope arithmetic progression are summable. Equation (8) therefore gives $\sum_k b_s^{\pi_k}<\infty$ in either case. Finiteness of $S$ and (1) yield $\sum_k\delta_k<\infty$. This closes the inverse-boundary summability step without assuming a local rate theorem.

## Convergence of policies

For any fixed optimal policy $p$, apply (3) statewise and use $\langle\pi_{k+1}-p,Q^*\rangle\le0$. Since $\|Q^*-Q_k\|_\infty\le\gamma\delta_k$,
\[
D_h(p\|\pi_{k+1})(s)-D_h(p\|\pi_k)(s)\le2\eta\gamma\delta_k. \tag{9}
\]
The divergence is nonnegative, so summability makes its limit exist at every state. Compactness supplies a cluster point $\bar\pi$; (1) and $b_s^{\pi_k}\to0$ show $\bar\pi\in\Pi^*$. Suboptimal coordinates of $\bar\pi$ are zero, and a sole optimal coordinate is one.

For $s\in S_{>1}$, let $M_k(s)$ be the maximum minus the minimum of the optimal-action dual scores. Eventually $b_s^{\pi_k}<1/2$, so an updated action attaining the maximum optimal score is positive. Compare its equation (2) with the equation for an action attaining the minimum, retaining the latter’s nonnegative multiplier. Because both actions have the same $Q^*$ value,
\[
M_{k+1}(s)\le M_k(s)+2\eta\gamma\delta_k.
\]
Thus $\sup_kM_k(s)<\infty$. If an optimal coordinate of $\bar\pi$ equaled one, another optimal coordinate would approach zero along the same subsequence; their dual-score difference would diverge because $\psi'(1-)=+\infty$ and $\psi'(0)$ is finite. Hence every optimal coordinate at such a state is less than one. Since zero is an interior-domain point, all these coordinates belong to $\operatorname{int}(\operatorname{dom}\psi)$.

To turn the cluster point into a full limit, use (9) with $p=\bar\pi$. Along the convergent subsequence $\pi_{k_i}\to\bar\pi$, each scalar divergence $d_\psi(\bar\pi(a\mid s)\|\pi_{k_i}(a\mid s))$ tends to zero. This follows by continuity when the limiting coordinate is below one. At a limiting coordinate equal to one, convexity gives $0\le(1-y)\psi'(y)\le\psi(1)-\psi(y)\to0$ for $y\uparrow1$, which gives the same conclusion. Thus $D_h(\bar\pi\|\pi_{k_i})(s)\to0$; its full limit from (9) is zero. Any other cluster point must equal $\bar\pi$: strict convexity makes scalar divergence to a distinct interior coordinate positive, while for a first argument below one and second arguments tending to one, the divergence tends to infinity. Coordinates whose first argument is one cannot have a distinct interior cluster value either. Compactness now gives $\pi_k\to\bar\pi\in\Pi^*$ with all claimed coordinate properties.

## The two branches

At a multiple-optimal state, the boundedness of $M_k(s)$ and the fact that at least one optimal coordinate is at most $1/2$ bound every optimal dual score above by $\psi'(1/2)+\sup_kM_k(s)$. Each suboptimal probability tends to zero, so its dual score is also bounded above, including the finitely many initial scores. Finiteness of $S,A$ gives a common $\beta<\infty$ for all actions at all states in $S_{>1}$. If a nontrivial multiple-optimal state retained positive suboptimal mass forever, (5) would force $G_k(s)\to\infty$, whereas $G_k(s)\le\beta-c_0$. It therefore reaches zero suboptimal mass in finite time and remains there. If $S_{=1}=\varnothing$, take the maximum of these finitely many stopping times. The resulting policy is optimal and, by the fixed-point argument above, remains unchanged.

Now suppose $S_{=1}\ne\varnothing$. Every such state is nontrivial because $|A|\ge2$. Its unique optimal coordinate is strictly below one at every finite iterate, so its suboptimal mass is positive and finite termination is impossible. Fix $\sigma\in(0,\Delta/2)$ and its entrance time $T$. For each $s\in S_{=1}$, (5), $\Delta_s\ge\Delta_{=1}$, and the lower bound $c_0$ on suboptimal dual scores give
\[
\chi(b_s^{\pi_k})\ge k\eta(\Delta_{=1}-2\sigma)+c_0+G_T(s)-T\eta(\Delta_{=1}-2\sigma).
\]
Let $C_1$ be the minimum of the finite constant terms over $S_{=1}$. For all sufficiently large $k$, inversion yields $b_s^{\pi_k}\le\chi^{-1}(k\eta(\Delta_{=1}-2\sigma)+C_1)$ simultaneously. The preceding bounded-score argument makes every multiple-optimal state’s suboptimal mass zero after a finite time. Equation (1), with $d_s^{\pi_k}$ a probability measure, therefore gives the required upper value-error bound.

For the lower bound choose $s_0\in S_{=1}$ with $\Delta_{s_0}=\Delta_{=1}$ and $a'_0\notin A_{s_0}^*$ with $V^*(s_0)-Q^*(s_0,a'_0)=\Delta_{=1}$. For $k\ge T$, (1) gives $b_{s_0}^{\pi_k}\le\sigma/\Delta<1/2$, so $\psi'(\pi_k(a'_0\mid s_0))\le\psi'(1/2)$. Apply (6) and telescope. Because the unique optimal probability is $1-b_{s_0}^{\pi_k}$, this gives
\[
\chi(b_{s_0}^{\pi_k})\le k\eta(\Delta_{=1}+2\sigma)+C_2,
\quad C_2=\psi'(1/2)+G_T(s_0,a'_0)-T\eta(\Delta_{=1}+2\sigma).
\]
For sufficiently large $k$, its argument is in $[c_0,\infty)$ and inversion gives $b_{s_0}^{\pi_k}\ge\chi^{-1}(k\eta(\Delta_{=1}+2\sigma)+C_2)$. The lower inequality in (1) completes the value-error bound. Choose one finite $K$ exceeding both branch-specific thresholds and both inverse-domain thresholds.
