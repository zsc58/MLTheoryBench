# Reference Proof

## Proof Structure

Use an independent Bernoulli retention scheduler and importance weights. Condition on the scheduler randomization when proving the delayed weighted bandit estimate, so that its weights are deterministic while the bandit directions remain independent. Derive the estimate from ball smoothing, the stated FTRL inequality, minimizer stability, and a weighted martingale calculation. Bound the joint weight-backlog terms and optimize separately in the convex and strongly convex cases. Clipped smoothing, zero backlog, and the one-round horizon are handled explicitly.

All expectations below concern learner randomization. The losses and delays are fixed before the game. Write
\[
d=\operatorname{diam}(\mathcal X),\qquad \kappa=\rho n.
\]
Thus \(0<2r\le d\le D\). Because \(r\mathbb B_2^n\subseteq\mathcal X\), every \(u\in\mathcal X\) satisfies \(\|u\|_2+r\le d\): for nonzero \(u\), compare it with \(-ru/\|u\|_2\), and treat \(u=0\) directly. Bounded gradients imply that every loss is \(G\)-Lipschitz on \(\mathcal X\).

## 1. Backlog bookkeeping — step_001

The source restriction \(0\le\tau_s\le T-s\) gives
\[
\sum_{t=1}^T|A_t|=\sum_{s=1}^T\tau_s,
\qquad |A_t|\le b.
\]
Indeed, index \(s\) belongs to the pending sets at precisely the times \(s+1,\ldots,s+\tau_s\). In particular, \(b\) is a nonnegative integer. If \(b=0\), no earlier index is pending at any prediction time.

## 2. Capacity scheduler and reduction — step_002

Set
\[
p=\min\left\{1,\frac{m}{8(b+1)}\right\},\qquad q=p^{-1}.
\]
Since \(m\ge1\),
\[
q\le8\left(1+\frac bm\right).
\tag{1}
\]
Independently draw \(Z_t\sim\operatorname{Bernoulli}(p)\), independently also of all bandit directions. After predicting at round \(t\), admit the current round exactly when \(Z_t=1\) and fewer than \(m\) earlier rounds are tracked. Keep every admitted round until its feedback arrives. This rule is capacity-feasible and needs no individual delay in advance.

Let \(S_t\subseteq A_t\) be the tracked set immediately before the admission decision, and put \(J_t=\mathbf1_{\{|S_t|=m\}}\). The scheduler uses only its own draws and delay expirations, not loss values or directions. Its weight vector is therefore a function solely of \((Z_s)_{s=1}^T\) and the fixed delays. Define
\[
w_t=qZ_t(1-J_t).
\tag{2}
\]
A positive-weight observation is eventually received, and a zero-weight item may simply be ignored by the base learner.

For
\[
N_t=\sum_{s\in A_t\cup\{t\}}Z_s,
\]
we have \(|S_t|\le N_t\) and \(\mu_t=\mathbb E N_t\le m/8\). Independence gives
\[
\mathbb E8^{N_t}
=\prod_{s\in A_t\cup\{t\}}(1+7p)
\le e^{7\mu_t}.
\]
Markov's inequality consequently yields
\[
\Pr(J_t=1)\le\Pr(N_t\ge m)
\le e^{7\mu_t-m\log8}
\le e^{m(7/8-\log8)}\le e^{-m}.
\tag{3}
\]
If \(b=0\), the stronger conclusion \(J_t=0\) holds identically, because \(S_t\subseteq A_t=\varnothing\).

Conditionally on the history before the current scheduler draw, including the current prediction, the exact moment identities are
\[
\mathbb E[w_t\mid\text{that history}]=1-J_t,
\qquad
\mathbb E[w_t^2\mid\text{that history}]=q(1-J_t).
\tag{4}
\]
In particular, \(\mathbb E w_t\le1\) and \(\mathbb E w_t^2\le q\). For distinct indices the required pairwise bound is unconditional:
\[
w_tw_s\le q^2Z_tZ_s
\quad\Longrightarrow\quad
\mathbb E[w_tw_s]\le1.
\tag{5}
\]
No conditional pairwise bound by one is asserted.

For \(\Delta_t=f_t(x_t)-f_t(u)\), we have \(|\Delta_t|\le Gd\). Since the current scheduler draw is independent of the prediction and of the preceding tracking state, (4) implies
\[
\mathbb E\operatorname{Reg}_T(u)
\le\mathbb E\operatorname{Reg}_T^w(u)
 +Gd\sum_{t=1}^T\Pr(J_t=1),
\qquad
\operatorname{Reg}_T^w(u)=\sum_{t=1}^Tw_t\Delta_t.
\tag{6}
\]
This penalty is at most \(GdTe^{-m}\le Gd/e\), and is exactly zero when \(b=0\).

## 3. Delayed weighted learner, smoothing, and FTRL — step_003

Choose deterministic nonincreasing sequences \(a_t\in(0,1]\) and \(\eta_t>0\), and set
\[
\delta_t=ra_t,\quad \eta_0=\eta_1,\quad
\alpha_1=\eta_1^{-1},\quad
\alpha_t=\eta_t^{-1}-\eta_{t-1}^{-1}\quad(t\ge2).
\]
Initialize \(y_1=0\). With \(O_t=\{s<t:s+\tau_s<t\}\), use
\[
y_t=\arg\min_{y\in\mathcal X}
\left\{\left\langle\sum_{s\in O_t}w_s\widehat g_s,y\right\rangle
 +\sum_{s<t}\frac{\alpha_s}{2}\|y_s-y\|_2^2\right\}
\quad(t\ge2).
\tag{7}
\]
Only delivered positive-weight estimators are needed in this update. Draw independent uniform sphere directions \(V_t\), independent of the scheduler, and play
\[
z_t=(1-a_t)y_t,\qquad x_t=z_t+\delta_tV_t.
\]
Convexity and the inner-ball inclusion imply \(x_t\in\mathcal X\). On delivery of a positive-weight observation form
\[
\widehat g_t=\frac n{\delta_t}f_t(x_t)V_t.
\tag{8}
\]
For analysis the same expression can be defined on unobserved rounds, where its weight is zero. The learner does not need their loss values.

### Conditioning and the smoothing result

Condition temporarily on all scheduler draws, denoting expectation over sphere directions by \(\mathbb E_V\). The weights are then deterministic, the loss and delay sequences remain fixed, and the directions remain independent and uniform. The actual centers and the fictitious centers defined below are measurable functions of preceding directions. This conditioning is an analysis device, not advance disclosure of the scheduler draws or delays to the learner.

The standard smoothing result supplied in the source is the following relevant statement. For a convex \(G\)-Lipschitz loss on this domain and \(0<\delta\le r\), define the **ball average**
\[
f^\delta(z)=\mathbb E_{U\sim\operatorname{Unif}(\mathbb B_2^n)}f(z+\delta U).
\]
On \((1-\delta/r)\mathcal X\), it preserves convexity and strong convexity, satisfies \(|f^\delta-f|\le G\delta\), and has
\[
\nabla f^\delta(z)=\frac n\delta
\mathbb E_{V\sim\operatorname{Unif}(\mathbb S^{n-1})}[f(z+\delta V)V],
\qquad \|\nabla f^\delta(z)\|_2\le G.
\tag{9}
\]
The hypotheses hold here: the losses are differentiable, convex, bounded and Lipschitz; the perturbation balls remain in the domain; and the radii are positive and at most \(r\). In particular,
\[
g_t:=\mathbb E_V[\widehat g_t\mid V_1,\ldots,V_{t-1}]
=\nabla f_t^{\delta_t}(z_t),
\quad \|g_t\|_2\le G,
\quad \|\widehat g_t\|_2\le\frac{nM}{\delta_t}.
\tag{10}
\]
At \(a_t=1\), the contracted domain is a singleton. The conditional mean in (10) is still defined by the sphere integral, and its norm bound follows by taking radii increasing to \(r\) in (9), using Lipschitz continuity. The contracted-point comparison below then has identical points on its two sides. Thus no differentiability assertion on a singleton is needed.

Let \(u_t^a=(1-a_t)u\). Pointwise Lipschitz and smoothing comparisons give
\[
f_t(x_t)-f_t(u)
\le f_t^{\delta_t}(z_t)-f_t^{\delta_t}(u_t^a)
 +3G\delta_t+Ga_t\|u\|_2.
\]
Since \(3r+\|u\|_2\le2d\), the last two terms are at most \(2Gda_t\). Treat ordinary convexity as curvature \(\lambda=0\) in the next display. Strong convexity of the smoothed loss gives
\[
\begin{aligned}
f_t(x_t)-f_t(u)
&\le(1-a_t)\langle g_t,y_t-u\rangle
 -\frac\lambda2(1-a_t)^2\|y_t-u\|_2^2+2Gda_t\\
&\le\langle g_t,y_t-u\rangle
 -\frac\lambda2\|y_t-u\|_2^2
 +(3Gd+\lambda d^2)a_t.
\end{aligned}
\tag{11}
\]
The last step uses \(\|g_t\|\le G\), \(\|y_t-u\|\le d\), and \(2a_t-a_t^2\le2a_t\). This proves the stated smoothing coefficient without imposing any relation between the supplied outer radius \(R\) and \(D/2\).

### Explicit FTRL application

Put
\[
\Psi_0(y)=\frac{\|y-y_1\|_2^2}{2\eta_1},\qquad
\Psi_t(y)=\sum_{s=1}^t\frac{\alpha_s}{2}\|y_s-y\|_2^2.
\]
Define \(\widetilde y_1=y_1\) and
\[
\widetilde y_{t+1}=\arg\min_{y\in\mathcal X}
\left\{\Psi_t(y)+\left\langle\sum_{s=1}^tw_s\widehat g_s,y\right\rangle\right\}.
\tag{12}
\]
These fictitious centers are used only for analysis.

The supplied standard FTRL inequality states that, on a compact convex set, for differentiable \((1/\eta_t)\)-strongly convex regularizers \(\Psi_t\), nonincreasing positive \(\eta_t\), an initial minimizer with \(\Psi_0(\widetilde y_1)=0\), and updates (12) with loss vectors \(c_t\),
\[
\sum_t\langle c_t,\widetilde y_t-u\rangle
\le\Psi_T(u)+\sum_t\left[
 \frac{\eta_{t-1}}2\|c_t\|_2^2
 +\Psi_{t-1}(\widetilde y_{t+1})-\Psi_t(\widetilde y_{t+1})\right].
\tag{13}
\]
Here compactness follows from the closed bounded domain. The regularizers have the required curvature because \(\sum_{s\le t}\alpha_s=1/\eta_t\), and \(\Psi_1=\Psi_0\). All later increments are nonnegative. Hence (13), with \(c_t=w_t\widehat g_t\), gives
\[
\sum_t\langle w_t\widehat g_t,\widetilde y_t-u\rangle
\le\sum_t\frac{\alpha_t}{2}\|y_t-u\|_2^2
 +\frac12\sum_t\eta_{t-1}w_t^2\|\widehat g_t\|_2^2.
\tag{14}
\]
All minimizers are unique. Their dependence on the linear coefficients and previous centers is continuous by the stability argument below, so the required measurability holds.

For completeness, if two objectives have the same \(\mu\)-strongly convex regularizer and linear coefficients \(c,c'\), their constrained minimizers \(v,v'\) satisfy, by adding the two strong-convexity minimizer inequalities,
\[
\mu\|v-v'\|_2^2\le\langle c-c',v'-v\rangle.
\]
Consequently \(\|v-v'\|_2\le\|c-c'\|_2/\mu\). Applying this to (7) and (12), whose missing linear terms are precisely the pending estimators, gives
\[
\|y_t-\widetilde y_t\|_2
\le\eta_{t-1}\left\|\sum_{s\in A_t}w_s\widehat g_s\right\|_2.
\tag{15}
\]
At \(t=1\) both centers coincide and the pending sum is zero.

## 4. Pending estimators and the weighted regret bound — step_004

Continue to condition on the scheduler draws. Let \(\xi_s=\widehat g_s-g_s\). For a deterministic nonempty index set \(A\) and \(\delta_* =\min_{s\in A}\delta_s\), the martingale-difference property gives
\[
\mathbb E_V\left\|\sum_{s\in A}w_s\xi_s\right\|_2^2
=\sum_{s\in A}w_s^2\mathbb E_V\|\xi_s\|_2^2
\le\left(\frac{nM}{\delta_*}\right)^2\sum_{s\in A}w_s^2.
\tag{16}
\]
In the expansion the cross terms include the factors \(w_sw_{s'}\). For \(s<s'\), conditioning on \(V_1,\ldots,V_{s'-1}\) makes the mean of \(\xi_{s'}\) zero while \(\xi_s\) is measurable. The diagonal bound follows from conditional variance being at most the conditional second moment of \(\widehat g_s\). Thus
\[
\mathbb E_V\left\|\sum_{s\in A}w_s\widehat g_s\right\|_2
\le G\sum_{s\in A}w_s+rac{nM}{\delta_*}\sqrt{\sum_{s\in A}w_s^2}.
\tag{17}
\]
For \(A=\varnothing\), both sums are zero and no minimum radius is needed. For \(A=A_t\), nonincreasing radii allow replacing \(\delta_*\) by \(\delta_t\).

Split \(\langle g_t,y_t-u\rangle\) at \(\widetilde y_t\). Conditional unbiasedness and adaptedness replace the fictitious-center term by \(\langle\widehat g_t,\widetilde y_t-u\rangle\) in expectation. The other term is bounded by \(G\|y_t-\widetilde y_t\|\). Combining (11), (14), (15), and (17), and then averaging over the scheduler, proves
\[
\begin{aligned}
\mathbb E\operatorname{Reg}_T^w(u)
\le{}&\frac{D^2}{2\eta_T}
 +2G^2\sum_t\eta_{t-1}\mathbb E B_t
 +3GD\sum_ta_t\mathbb E w_t,
\\
B_t={}&\frac{\kappa^2}{a_t^2}w_t^2
 +\frac{\kappa}{a_t}w_t\sqrt{\sum_{s\in A_t}w_s^2}
 +w_t\sum_{s\in A_t}w_s.
\end{aligned}
\tag{18}
\]
Indeed, in the convex case \(\sum_t\alpha_t\|y_t-u\|^2/2\le D^2/(2\eta_T)\). The factor two in (18) safely dominates the diagonal and drift coefficients derived above.

Under strong convexity, summing the two strong-convexity inequalities with exchanged arguments gives
\[
\lambda\|x-y\|_2^2
\le\langle\nabla f_t(x)-\nabla f_t(y),x-y\rangle
\le2G\|x-y\|_2.
\]
Thus \(d\le2G/\lambda\); this does not assert that a loose supplied \(D\) satisfies that inequality. Using \(3Gd+\lambda d^2\le10G^2/\lambda\), the corresponding bound is
\[
\mathbb E\operatorname{Reg}_T^w(u)
\le\frac12\sum_t\mathbb E[(\alpha_t-\lambda w_t)\|y_t-u\|_2^2]
 +2G^2\sum_t\eta_{t-1}\mathbb E B_t
 +\frac{10G^2}{\lambda}\sum_ta_t\mathbb E w_t.
\tag{19}
\]
Equations (18) and (19) have now been derived, not assumed as specialized external results.

## 5. Joint moments and the convex regime — step_005

Let \(I_t=\mathbf1_{\{w_t=q\}}\). Equations (4)-(5) imply
\[
\mathbb E I_t\le q^{-1},\qquad
\mathbb E I_tI_s\le q^{-2}\quad(s\ne t).
\]
Cauchy-Schwarz, retaining the current indicator, gives
\[
\begin{aligned}
\mathbb E\left[w_t\sqrt{\sum_{s\in A_t}w_s^2}\right]
&=q^2\mathbb E\left[I_t\sqrt{\sum_{s\in A_t}I_s}\right]\\
&\le q^2\sqrt{\mathbb E I_t\;
 \mathbb E\left[I_t\sum_{s\in A_t}I_s\right]}
\le\sqrt{q|A_t|}.
\end{aligned}
\tag{20}
\]
Also \(\mathbb E[w_t\sum_{s\in A_t}w_s]\le|A_t|\). Write
\[
Q=q\kappa^2>0.
\]
The middle term in the expected bracket is at most the geometric mean of \(Q/a_t^2\) and \(|A_t|\). Therefore
\[
\mathbb E B_t\le\frac32\left(\frac Q{a_t^2}+|A_t|\right).
\tag{21}
\]

For the convex guarantee choose
\[
a_t=\min\{1,Q^{1/4}t^{-1/4}\},\qquad
H=\sqrt{Tb}+Q^{1/4}T^{3/4},\qquad
\eta_t=\frac D{GH}.
\tag{22}
\]
These schedules are admissible and depend only on known quantities.

If \(Q\ge T\), then \(Q^{1/4}T^{3/4}\ge T\), and the deterministic bound \(\operatorname{Reg}_T(u)\le GdT\le GDT\) already proves the desired bound for the same strategy.

Suppose henceforth that \(Q<T\). Including all initially clipped indices, we have
\[
\frac Q{a_t^2}=\max\{Q,\sqrt Q\sqrt t\}\le\sqrt Q\sqrt T.
\]
Consequently
\[
\sum_t\mathbb E B_t
\le\frac32(Tb+\sqrt Q\,T^{3/2})\le\frac32H^2.
\tag{23}
\]
Moreover, comparison with the integral of \(x^{-1/4}\) yields
\[
\sum_{t=1}^Ta_t\le Q^{1/4}\sum_{t=1}^Tt^{-1/4}
\le\frac43Q^{1/4}T^{3/4}.
\tag{24}
\]
Substituting (22)-(24) and \(\mathbb E w_t\le1\) into (18) gives
\[
\mathbb E\operatorname{Reg}_T^w(u)\le C GD H
\]
for a numerical constant \(C\). If \(b\ge1\), the penalty in (6) is absorbed because \(H\ge\sqrt{Tb}\ge1\). If \(b=0\), that penalty is zero, so no positive lower bound on \(\rho\) is needed. Finally, (1) converts \(Q^{1/4}=q^{1/4}\sqrt{\rho n}\) to the required capacity dependence.

## 6. Strongly convex regime and boundary cases — step_006

Use
\[
a_t=\min\left\{1,\left(\frac{Q\log(t+1)}t\right)^{1/3}\right\},
\qquad \eta_t=\frac1{\lambda t},\quad \eta_0=\eta_1.
\tag{25}
\]
The function \(\log(t+1)/t\) is decreasing for \(t>0\), so the radii are nonincreasing. Every \(\alpha_t=\lambda\), and \(\eta_{t-1}\le2/(\lambda t)\).

The curvature residual in (19) is not discarded. The center \(y_t\) is determined before the current scheduler draw, so (4) gives the exact identity
\[
\frac\lambda2\sum_t\mathbb E[(1-w_t)\|y_t-u\|_2^2]
=\frac\lambda2\sum_t\mathbb E[J_t\|y_t-u\|_2^2]
\le\frac{2G^2}{\lambda}\sum_t\Pr(J_t=1).
\tag{26}
\]
It is zero when \(b=0\); otherwise it is at most \(2G^2Te^{-m}/\lambda\). The reduction penalty (6) is at most the same quantity because \(Gd\le2G^2/\lambda\).

Put
\[
\ell=\log(eT),\qquad L=(QT^2\ell)^{1/3}.
\]
If \(a_T=1\), then \(Q\log(T+1)\ge T\), and \(\ell\ge\log(T+1)\) implies \(L\ge T\). Hence the deterministic bound
\[
\operatorname{Reg}_T(u)\le GdT\le\frac{2G^2}{\lambda}T
\]
proves the desired rate, without attempting an unclipped variance substitution.

Now suppose \(a_T<1\). Monotonicity gives \(a_t\ge a_T\). Using the harmonic bound \(\sum_{t=1}^T1/t\le\ell\) and \(\log(T+1)\ge\ell/2\),
\[
\sum_{t=1}^T\frac1t\frac Q{a_t^2}
\le\frac{Q\ell}{a_T^2}
=\frac{Q^{1/3}T^{2/3}\ell}{\log(T+1)^{2/3}}
\le2^{2/3}L.
\tag{27}
\]
This bound includes any earlier clipped indices. Thus (21) implies
\[
\sum_t\frac1t\mathbb E B_t\le C(b\ell+L).
\tag{28}
\]
Also,
\[
\sum_ta_t
\le Q^{1/3}\log(T+1)^{1/3}\sum_{t=1}^Tt^{-1/3}
\le\frac32L.
\tag{29}
\]
Substitute (26)-(29) into (19), then apply (6). If \(b\ge1\), the two saturation terms are absorbed by \(b\ell\), since \(Te^{-m}\le1/e\) and \(b\ell\ge1\). If \(b=0\), both are exactly zero. Therefore
\[
\mathbb E\operatorname{Reg}_T(u)
\le C\frac{G^2}{\lambda}\left[b\log(eT)+(q(\rho n)^2T^2\log(eT))^{1/3}\right].
\]
Using (1) proves the strongly convex guarantee with a universal constant.

Every displayed schedule remains defined at \(T=1\). Empty pending sets were treated explicitly, no division by zero occurs because \(M,G,r>0\), and no assumption such as \(\rho n\ge1\) was used. The same constructed strategy in each regime works for every fixed comparator, without depending on that comparator or on unrevealed losses or individual delays. All theorem-critical obligations are closed.
