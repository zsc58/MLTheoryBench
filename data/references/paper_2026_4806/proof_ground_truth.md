# Reference Proof

## Contract and notation

Use the algorithm and pseudo-regret defined in the public task. All transition laws and rewards are fixed; only past trajectories are used to construct the policy for the next episode. Write \(Z=Z_{\rm eff}\), \(p_z=P_{\rm eff}(\cdot\mid z)\), \(\hat p_z=\widehat P_k(\cdot\mid z)\), and \(n_k(z)=N_k(z)\vee1\). Set
\[
\ell_1=\log\frac{128H^2|Y||Z|K}{\delta},\qquad
\ell_2(z)=\log\frac{128HB(z)|Z|K}{\delta},\qquad
\ell_z=\min\{\ell_1,B(z)\ell_2(z)\},\qquad d_z=B(z)\ell_2(z).
\]
In particular, \(1\le\ell_z\le d_z\). Choose \(c_1=20/3\) and \(c_2=400/9\). The conditional output is \(H\) when \(N_k(z)\le1\); otherwise it is the sum-bonus estimate clipped at \(H\), as specified publicly. In every expectation involving a next-state slice, its argument is \(x\mapsto V_{h+1}(x,y)\).

We close the following obligations: adaptive sampling and simultaneous concentration; optimism; the squared-gap residual inequality; propagation to an episode bound; cumulative optimal-value variance; stale-count visitation control; and the final regret summation. No specialized cited result is assumed without a derivation.

## 1. Simultaneous confidence event

The standard scalar inequalities used here are the following. For iid \(T_i\in[a,b]\), with mean \(\mu\), variance \(v\), empirical mean \(\bar T_n\), and empirical variance \(\hat v_n=n^{-1}\sum_i(T_i-\bar T_n)^2\), the true-variance Bernstein inequality gives
\[
|\bar T_n-\mu|\le\sqrt{2vt/n}+(b-a)t/(3n)
\]
with failure probability at most \(2e^{-t}\). For \(n\ge2\), the empirical-variance version gives
\[
|\bar T_n-\mu|\le2\sqrt{\hat v_n t/n}+14(b-a)t/(3n)
\]
with failure probability at most \(4e^{-t}\). We use these independently of the paper-specific chain.

To justify their use with adaptive visits, realize a transition by first drawing \(y\) from the known marginal, identifying \(z=\phi_Z(s,a,y)\), and then consuming the next unused draw from an iid stream of law \(p_z\). Independent streams and fresh marginal draws realize exactly the stipulated Markov transition law. This is a probabilistic representation, not additional information given to the learner. Every empirical conditional distribution is a prefix of its stream. Union bounds are taken over all deterministic prefix lengths up to \(KH\), not conditional on a random visit count.

Apply the scalar inequalities to every fixed optimal-value slice \(V_{h+1}^*(\cdot,y)\), every context, and every prefix. For arbitrary functions, apply them first to the indicators of the coordinates in the true support of \(p_z\). That support has at most \(B(z)\) elements; its identity need not be known to the learner. Coordinates outside it have both true and empirical mass zero almost surely.

For example, the coordinate true-variance event gives
\[
|\hat p_z(x)-p_z(x)|\le\sqrt{2p_z(x)\ell_2(z)/N}+\ell_2(z)/(3N).
\]
For any function \(f\) of range length at most \(b-a\), center at \(p_zf\), multiply by \(|f(x)-p_zf|\), and sum. Cauchy-Schwarz gives, simultaneously for all such functions,
\[
|(\hat p_z-p_z)f|\le\sqrt{2\operatorname{Var}_{p_z}(f)d_z/N}+(b-a)d_z/(3N).
\tag{1}
\]
Centering instead at \(\hat p_zf\) and using the empirical coordinate event gives
\[
|(\hat p_z-p_z)f|\le2\sqrt{\operatorname{Var}_{\hat p_z}(f)d_z/N}+14(b-a)d_z/(3N).
\tag{2}
\]
These bounds permit data-dependent functions because the coordinate event holds uniformly. They do not remove the factor \(B(z)\) from the square root.

Intersect the four events: fixed-function true and empirical bounds, and coordinate true and empirical bounds. The displayed logarithms and union bounds give failure probability at most \(\delta/2\). Denote the resulting event by \(E_0\). For every fixed optimal-value slice \(g\), taking the better of its fixed-function bound and (1) or (2) yields, when \(N\ge2\),
\[
|(\hat p_z-p_z)g|\le\sqrt{2\operatorname{Var}_{p_z}(g)\ell_z/N}+H\ell_z/(3N),
\tag{3}
\]
\[
|(\hat p_z-p_z)g|\le2\sqrt{\operatorname{Var}_{\hat p_z}(g)\ell_z/N}+14H\ell_z/(3N).
\tag{4}
\]
Counts zero and one are handled by the algorithm's separate branch, not by applying an empirical-variance theorem outside its domain.

## 2. Optimism

Here is the monotonicity needed for the induction. For a probability vector \(p\), \(t>0\), and \(v\in[0,H]^X\), let
\[
F(v)=pv+\max\{a\sqrt{\operatorname{Var}_p(v)t},bHt\},\qquad a=20/3,\ b=400/9=a^2.
\]
In the region where the constant branch is active, \(F\) is coordinatewise nondecreasing. In the square-root-active region, writing \(\sigma^2=\operatorname{Var}_p(v)\), the active condition implies \(\sigma\ge aH\sqrt t\). Its derivative in coordinate \(i\) is
\[
p_i\left(1+a\sqrt t\,\frac{v_i-pv}{\sigma}\right)\ge0,
\]
since \(v_i-pv\ge-H\). Continuity handles the boundary, so \(F\) is coordinatewise nondecreasing throughout the cube. Moreover,
\[
\max\{a\sqrt{\sigma^2t},bHt\}\ge2\sqrt{\sigma^2t}+\frac{14}{3}Ht,
\]
because \(2/a+(14/3)/b<1\).

Suppose \(V_{h+1}^k\ge V_{h+1}^*\). For a conditional estimate with \(N\ge2\), apply (4), the last domination, and monotonicity of \(F\) to obtain
\[
r+p_zV_{h+1}^*(\cdot,y)
\le r+\hat p_zV_{h+1}^k(\cdot,y)
+a\sqrt{\operatorname{Var}_{\hat p_z}(V_{h+1}^k(\cdot,y))\ell_z/N}
+bH\ell_z/N.
\]
The left side is at most \(H\), so clipping preserves this inequality. When \(N\le1\), the output \(H\) is directly optimistic. Averaging over the known marginal and maximizing over actions proves \(V_h^k\ge V_h^*\). Starting from zero terminal values establishes the induction. Also \(0\le V_h^k\le H\).

## 3. Bonus comparison and a squared-gap residual

Fix an episode and suppress its index. At a conditional estimate write \(f=V_{h+1}^k(\cdot,y)\), \(g=V_{h+1}^*(\cdot,y)\), and \(u=f-g\). Optimism gives \(0\le u\le H\). For \(N\ge2\), apply (1) to \((f-p_zf)^2\). Using \(\operatorname{Var}(T)\le H^2ET\) for \(0\le T\le H^2\), followed by Young's inequality, gives
\[
(\hat p_z-p_z)(f-p_zf)^2
\le\tfrac12\operatorname{Var}_{p_z}(f)+\tfrac43H^2d_z/N.
\]
Consequently,
\[
\operatorname{Var}_{\hat p_z}(f)
\le3\operatorname{Var}_{p_z}(g)+3\operatorname{Var}_{p_z}(u)+\tfrac43H^2d_z/N.
\tag{5}
\]
Take square roots, use \(\ell_z\le d_z\), and apply
\[
\sqrt{3\operatorname{Var}_{p_z}(u)\ell_z/N}
\le\frac{3\operatorname{Var}_{p_z}(u)}{160H}+40H\ell_z/N.
\]
The actual bonus therefore satisfies
\[
b_h^k(s,a,y)\le12\sqrt{\operatorname{Var}_{p_z}(g)\ell_z/N}
+\frac{\operatorname{Var}_{p_z}(u)}{8H}+325Hd_z/N.
\tag{6}
\]
Here the actual linear bonus coefficient is \(400/9\), not \(400\).

Split \((\hat p_z-p_z)f\) into its \(g\) and \(u\) parts. Apply (3) to \(g\), (1) to \(u\), and Young's inequality to the latter square root. This yields
\[
(\hat p_z-p_z)f
\le\sqrt{2\operatorname{Var}_{p_z}(g)\ell_z/N}
+\frac{\operatorname{Var}_{p_z}(u)}{8H}+\frac{14Hd_z}{3N}.
\tag{7}
\]
Combining (6) and (7), and allowing for clipping, bounds the conditional residual by
\[
14\sqrt{\operatorname{Var}_{p_z}(g)\ell_z/n_k(z)}
+\frac{\operatorname{Var}_{p_z}(u)}{4H}+330Hd_z/n_k(z).
\tag{8}
\]
This also holds for \(N\le1\): the conditional residual is at most \(H\), whereas the last term is at least \(330H\).

We derive the variance inequality used next rather than invoking a specialized external theorem. For \(0\le f\le c\), \(0\le v\le c\), and \(\mu=Pf\),
\[
\operatorname{Var}_P(f)=P[f^2]-\mu^2
\le P[f^2]-v^2+2c(v-\mu)_+.
\tag{9}
\]
Indeed, \(v^2-\mu^2\le0\) if \(v\le\mu\); otherwise it equals \((v-\mu)(v+\mu)\le2c(v-\mu)\). The law of total variance also gives
\[
E_y\operatorname{Var}_{p_{\phi_Z(s,a,y)}}(f(\cdot,y))\le\operatorname{Var}_{P_{s,a}}(f).
\tag{10}
\]
It is essential that the conditional variance in (10) is averaged over \(y\).

Set \(D_h(s)=V_h^k(s)-V_h^*(s)\), take \(a=\pi_h^k(s)\), and put
\[
e_h(s)=V_h^k(s)-r(s,a)-P_{s,a}V_{h+1}^k,\qquad I=(e_h(s))_+.
\]
Average (8) over \(y\). Since \(V_h^*(s)\ge r(s,a)+P_{s,a}V_{h+1}^*\), we have \(D_h(s)-P_{s,a}D_{h+1}\le e_h(s)\). Equations (9)-(10), applied to \(D\in[0,H]\), therefore bound its averaged conditional variance by
\[
P_{s,a}D_{h+1}^2-D_h(s)^2+2HI.
\]
If
\[
A_h(s)=E_y\left[14\sqrt{\operatorname{Var}_{p_z}(V_{h+1}^*(\cdot,y))\ell_z/n_k(z)}+330Hd_z/n_k(z)\right],
\]
then \(I\le A_h+(P D_{h+1}^2-D_h^2)/(4H)+I/2\). Rearranging gives
\[
e_h(s)\le\frac{P_{s,a}D_{h+1}^2-D_h(s)^2}{2H}
+E_y\left[28\sqrt{\operatorname{Var}_{p_z}(V_{h+1}^*(\cdot,y))\ell_z/n_k(z)}+660Hd_z/n_k(z)\right].
\tag{11}
\]
This is the required residual inequality; merely squaring an optimism-gap recursion would not establish it.

## 4. Per-episode propagation and total variance

For each episode define \(U_{H+1}^k=\widetilde U_{H+1}^k=0\), and, with \(a=\pi_h^k(s)\),
\[
U_h^k(s)=\min\left\{1,E_{s'=(x',y')\sim P_{s,a}}\left[\frac{\ell_z}{n_k(z)}+U_{h+1}^k(s')\right]\right\},
\]
\[
\widetilde U_h^k(s)=\min\left\{1,E_{s'=(x',y')\sim P_{s,a}}\left[\frac{d_z}{n_k(z)}+\widetilde U_{h+1}^k(s')\right]\right\},\qquad z=\phi_Z(s,a,y').
\]
These finite quantities satisfy \(0\le U\le\widetilde U\le1\). Define
\[
W_h^k(s)=E_{\pi^k(\cdot\mid s_h=s)}\sum_{j=h}^H\operatorname{Var}_{p_{z_j}}(V_{j+1}^*(\cdot,y_{j+1})).
\]
Backward induction using (11) proves
\[
V_h^k(s)-V_h^{\pi^k}(s)
\le28\sqrt{W_h^k(s)U_h^k(s)}+660H\widetilde U_h^k(s)-\frac{D_h(s)^2}{2H}.
\tag{12}
\]
Here are the induction details. The terminal case is zero. If \(\widetilde U_h=1\), the right side is at least \(660H-H/2\), while the left side is at most \(H\). Otherwise both uncertainty recursions are unsaturated. Decompose the left side as \(e_h+P(V_{h+1}^k-V_{h+1}^{\pi^k})\). The positive next-stage squared-gap term in (11) cancels the negative term in the induction hypothesis. The linear uncertainty contributions add to \(660H\widetilde U_h\). For the square-root terms use first
\(\sqrt{ab}+\sqrt{cd}\le\sqrt{(a+c)(b+d)}\), and then Cauchy-Schwarz under the next-state expectation. The recursive definitions of \(W\) and \(U\) produce \(28\sqrt{W_hU_h}\), proving (12).

To bound \(W_1\), apply (9)-(10) to \(V^*\). For the action actually chosen,
\(V_h^*(s)-P_{s,a}V_{h+1}^*\ge r(s,a)\ge0\).
Thus, after summing over stages and taking the true trajectory expectation, both differences telescope:
\[
W_1^k(s_1^k)\le-(V_1^*(s_1^k))^2+2HV_1^*(s_1^k)\le H^2.
\tag{13}
\]
Dropping the negative square from (12) yields
\[
V_1^k(s_1^k)-V_1^{\pi^k}(s_1^k)
\le28H\sqrt{U_1^k(s_1^k)}+660H\widetilde U_1^k(s_1^k).
\tag{14}
\]
This is a bound on the optimistic-minus-executed value gap, which upper-bounds regret by optimism.

## 5. Direct stale-count visitation bound

This section closes the visitation obligation without assuming the specialized citation used for the source's Lemma 5. It proves the aggregate order required for the theorem, not that lemma's particular constants.

Fix deterministic weights \(w_z\ge1\), let \(W_0=\sum_z w_z\), and define \(F_{H+1}^k=0\) and
\[
F_h^k(s)=\min\{1,E[w_z/(N_k(z)\vee1)+F_{h+1}^k(s')]\}.
\]
For a realized episode set \(M_h^k(z)=N_k(z)+\sum_{j\le h}\mathbf1\{z_j^k=z\}\). Stop at the first transition \(\tau\) for which \(M_h^k(z_h^k)\ge2N_k(z_h^k)\). In particular, an initially unvisited context triggers stopping on its first occurrence. If no such transition exists, put \(\tau=H+1\). Define the nonnegative episode charge
\[
C_k=\sum_{h<\tau}\frac{w_{z_h^k}}{N_k(z_h^k)\vee1}+\mathbf1\{\tau\le H\}(w_{z_\tau^k}+1).
\]
The Bellman inequality \(F_h\le E[w_z/(N_k(z)\vee1)+F_{h+1}]\) can be iterated up to this finite stopping transition. At that transition, the immediate cost plus the remaining value is at most \(w_z+1\), because \(F\le1\). Consequently, conditional on all previous data and the observed initial state,
\[
F_1^k(s_1^k)\le E[C_k\mid\mathcal F_k].
\tag{15}
\]
The stopping rule may depend on the revealed next Y component; finite conditional iteration over the full transitions justifies (15) without any independence assumption on that rule.

Before stopping, each context with positive initial count contributes fewer than \(N_k(z)\) visits. Hence its episode charge is at most \(w_z\), and \(0\le C_k\le3W_0\). Across all episodes, each nonterminal charged visit satisfies
\[
\frac1{N_k(z_h^k)}\le\frac2{M_h^k(z_h^k)}.
\]
Since the positive within-episode counts enumerate successive occurrences, their total weighted contribution is at most \(2W_0\log(eKH)\). Each terminal charge for a context with positive initial count implies that its count has at least doubled by the next episode. For each context there is at most one zero-count terminal charge and at most \(1+\log_2(KH)\) positive-count terminal charges. Since \(w_z+1\le2w_z\), it follows deterministically that
\[
\sum_k C_k\le C W_0\log(eKH)
\tag{16}
\]
for a universal constant \(C\).

For completeness, the probability conversion is elementary. If \(0\le X\le M\), the chord inequality for the convex function \(e^{-x}\) gives
\[
E[e^{-X/M}\mid\mathcal F]\le1-(1-e^{-1})E[X\mid\mathcal F]/M.
\]
Thus the products of
\(\exp((1-e^{-1})E[X\mid\mathcal F]/M-X/M)\)
form a nonnegative supermartingale. Markov's inequality implies, with probability at least \(1-\eta\),
\[
\sum_k E[C_k\mid\mathcal F_k]
\le\frac{\sum_k C_k+3W_0\log(1/\eta)}{1-e^{-1}}.
\tag{17}
\]
The filtration may include the current observed initial state; the conditional bound holds for every such state and therefore also under the stipulated fixed initial distribution.

Combining (15)-(17), and applying the result separately with \(w_z=\ell_z\) and \(w_z=d_z\), with failure probability \(\delta/4\) each, proves
\[
\sum_k U_1^k(s_1^k)\le C T\sum_z\ell_z,\qquad
\sum_k\widetilde U_1^k(s_1^k)\le C T\sum_z d_z,
\tag{18}
\]
where \(T=\log(eKH)+\log(4/\delta)\). This argument includes zero counts, repeated visits within an episode, and unreachable contexts.

## 6. Final summation

Intersect the visitation events with \(E_0\); the total failure probability is at most \(\delta\). On this event, optimism, (14), Cauchy-Schwarz across episodes, and (18) give
\[
R_K\le C H\sqrt{K T\sum_z\ell_z}+C H T\sum_z B(z)\ell_2(z).
\tag{19}
\]
Let \(m_z=\min\{B(z),\log(e|Y|)\}\) and \(L_0=\log(128H^2|X||Z|K/\delta)\). Since \(B(z)\le|X|\),
\[
\ell_2(z)\le L_0,\qquad
\ell_z\le\min\{\log|Y|+L_0,B(z)L_0\}\le2L_0m_z.
\]
Insert these bounds in (19) and absorb \(T\) and \(L_0\) into logarithmic factors. This is precisely
\[
R_K\le\widetilde O\left(H\sqrt{K\sum_z\min\{B(z),\log(e|Y|)\}}+H\sum_zB(z)\right).
\]
The bounds remain defined for \(H=1\), \(K=1\), singleton component spaces, and support bound one. In particular, the logarithmic floor must not be removed when \(|Y|=1\).

## Source-local repairs and closure status

The source's algorithmic logarithm is synchronized with its Appendix B union bound; the positive logarithmic floor is retained; context-count and zero-count conventions are explicit; the linear bonus uses its actual denominator 9; conditional gap variances are averaged before invoking total variance; the dropped factor in the source harmonic-sum display is corrected; and the true-variance inequality uses its defined population variance. These corrections are recorded in provenance. The source's specialized visitation citation is replaced by the explicit argument in Section 5, and the other specialized-looking auxiliary facts are derived in Sections 2 and 3. All theorem-critical obligations are closed.
