# Reference Proof

## Proof structure and obligations

We retain the uniform minimax quantifier order of the public lower bound. We prove the hard-family geometry, derive the reduced-transcript KL bound, and complete the testing argument. For the upper bound, we state precisely the standard EXP3-IX regret result used, derive its stochastic-game output consequence, construct the synchronized procedure, verify that its information access satisfies the same reduced-transcript restriction, and establish the displayed constant for all action-set sizes and all times.

Throughout, logarithms are natural, \(p\in(0,2]\), and \(\alpha=1/(2+p)\). For every profile, \(0\leq\operatorname{Gap}\leq1\): the expected payoff of the profile lies between the minimum and maximum in the gap definition.

## 1. Lower bound

Suppose the claimed lower bound fails. Then there is a constant
\[
0<C<c_p:=4^{-1/p}/118
\]
and a deterministic \(T_0\) such that, for all \(t>T_0\) and all \(|\varepsilon|\leq1/12\),
\[
\|\operatorname{Gap}(\mu_t,\nu_t)\|_{\varepsilon,p}\leq Ct^{-\alpha}.
\]
In particular \(C\leq1\). This is a uniform eventual bound, obtained from the public limsup-sup assertion; we do not replace it by a pointwise assertion with game-dependent starting times.

### Geometry

Every game in the family has value \(1/2\). Indeed, the column policy \((1/2,1/2)\) makes both rows equal to \(1/2\), and the row policy with first coordinate \(1/(2-6\varepsilon)\) makes both columns equal to \(1/2\). This coordinate lies in \([0,1]\) throughout the stated parameter interval.

Write \(\nu_t=(1/2+d_t,1/2-d_t)\), where \(|d_t|\leq1/2\). The two row payoffs in the central game are \(1/2+d_t/3\) and \(1/2-d_t/3\), so
\[
\operatorname{Gap}_0(\mu_t,\nu_t)\geq |d_t|/3. \tag{1}
\]
For a horizon \(T\), put
\[
E_T^+=\{\mu_T(1)\leq1/2\},\qquad E_T^-=\{\mu_T(1)\geq1/2\}.
\]
At least one has probability at least \(1/2\) under the central game; choose its sign \(\sigma_T\in\{+,-\}\).

If \(x=\mu_T(1)\leq1/2\), the second-column payoff in \(G_\varepsilon\), for \(\varepsilon\geq0\), is
\[
2/3-(1/3-\varepsilon)x\geq1/2+\varepsilon/2.
\]
If \(x\geq1/2\), the first-column payoff in \(G_{-\varepsilon}\) is
\[
1/3+(1/3+\varepsilon)x\geq1/2+\varepsilon/2.
\]
Consequently, the corresponding signed-game gap is at least \(\varepsilon/2\) on \(E_T^{\sigma_T}\).

### Information bound

Let
\[
\varepsilon_T=(24\sqrt6)^{-1}T^{-\alpha},\qquad
Z_T=(U,a_1,X_1,\ldots,a_T,X_T).
\]
These alternatives belong to the stated family. At the same reduced transcript, both games use the same policy maps and the same conditional law for \(a_t\). Initial randomness also has the same law. Conditional on that transcript and \(a_t=1\), the central and signed alternative loss parameters are
\[
x_t=1/2+d_t/3,\qquad y_t=1/2+d_t/3-2\sigma_T\varepsilon_Td_t.
\]
For \(a_t=2\), the two observation laws coincide. The independent action sampling and the fixed Bernoulli entry laws justify these mixture formulas. Both parameters lie in \([1/4,3/4]\).

The elementary Bernoulli inequality
\[
\operatorname{kl}(x,y)\leq\frac{(x-y)^2}{y(1-y)}
\]
therefore gives \(\operatorname{kl}(x_t,y_t)\leq24\varepsilon_T^2d_t^2\). Applying the KL chain rule with the loss kernel conditioned on both the preceding transcript and the current \(a_t\),
\[
\begin{aligned}
\operatorname{KL}(P_0^{Z_T},P_{\sigma_T\varepsilon_T}^{Z_T})
&\leq24\varepsilon_T^2\mathbb E_0\sum_{t\leq T}|d_t|^2\\
&\leq24\varepsilon_T^2\mathbb E_0\sum_{t\leq T}|d_t|^p\\
&\leq216\varepsilon_T^2\sum_{t\leq T}\|\operatorname{Gap}_0(\mu_t,\nu_t)\|_{0,p}^p.
\end{aligned} \tag{2}
\]
Here \(|d_t|\leq1\), \(p\leq2\), (1), and \(3^p\leq9\) were used.

The assumed rate and the bound on the first \(T_0\) gaps give
\[
\operatorname{KL}(P_0^{Z_T},P_{\sigma_T\varepsilon_T}^{Z_T})
\leq216\varepsilon_T^2\left(T_0+2T^{2\alpha}\right), \tag{3}
\]
since
\[
\sum_{t=1}^Tt^{-p/(2+p)}\leq\int_0^T x^{-p/(2+p)}\,dx
=\frac{2+p}{2}T^{2\alpha}\leq2T^{2\alpha}.
\]

### Testing conclusion

The event \(E_T^{\sigma_T}\) is measurable from the reduced transcript. Pinsker's inequality, \(\operatorname{TV}(P,Q)\leq\sqrt{\operatorname{KL}(P,Q)/2}\), and (3) imply
\[
\liminf_{T\to\infty}P_{\sigma_T\varepsilon_T}(E_T^{\sigma_T})
\geq\frac12-6\sqrt6\limsup_{T\to\infty}\varepsilon_TT^\alpha
=\frac14.
\]
Using the signed-game geometry,
\[
\liminf_{T\to\infty}T^\alpha
\|\operatorname{Gap}(\mu_T,\nu_T)\|_{\sigma_T\varepsilon_T,p}
\geq\frac{4^{-1/p}}{48\sqrt6}
>\frac{4^{-1/p}}{118}.
\]
This contradicts the uniform eventual bound and proves part 1.

## 2. An explicitly justified output bound

Put \(n=A+B\). If \(A=B=1\), the gap is always zero, so assume \(n\geq3\).

### Audited standard regret input

For \(K\geq2\), the quoted anytime EXP3-IX result uses
\[
\eta_i=2\gamma_i=\sqrt{\frac{\log K}{Ki}}
\]
and states that, for every horizon \(s\) and \(\delta\in(0,1)\),
\[
R_K(s)\leq4\sqrt{Ks\log K}
+\left(2\sqrt{\frac{Ks}{\log K}}+1\right)\log(2/\delta)
\tag{4}
\]
with probability at least \(1-\delta\). Here
\[
R_K(s)=\sum_{i=1}^sY_i(I_i)-\min_j\sum_{i=1}^sY_i(j)
\]
is realized external regret for losses in \([0,1]\). The loss vector may depend on past observations and fresh randomness independent of the current arm draw; it must not anticipate that draw. A singleton player uses its unique action and has zero regret, with no evaluation of the displayed parameters.

Run two virtual instances, with the maximizing player minimizing \(1-X_i\). Denote their virtual mixed policies by \(u_i,v_i\), their sampled arms by \(a_i,J_i\), and their average policies after \(s\) rounds by \(\bar u_s,\bar v_s\).

### Stochastic regret-to-gap correction

For analysis, generate a fresh payoff table \(Y_i(a,b)\) each round with entry laws \(\rho_{ab}\), independently of the current arm draws, and observe \(X_i=Y_i(a_i,J_i)\). This realizes precisely the fixed-law observation experiment. The first learner's counterfactual loss vector is \(Y_i(\cdot,J_i)\), and the second learner's is \(1-Y_i(a_i,\cdot)\). Conditional on the virtual past, the opponent's current arm and the fresh payoff table do not anticipate the learner's current arm. Thus (4) applies to both instances.

For each row comparator, \(Y_i(a,J_i)\) has conditional mean \(L(a,v_i)\). For each column comparator, \(Y_i(a_i,b)\) has conditional mean \(L(u_i,b)\).

We use the following elementary bounded-difference estimate. If \(D_i\) is conditionally mean zero and has conditional range of length at most one, then
\[
\mathbb E[e^{\lambda D_i}\mid\text{past}]\leq e^{\lambda^2/8}.
\]
Indeed, convexity bounds the exponential by the endpoint Bernoulli interpolation; the second derivative of the logarithm of that Bernoulli moment-generating function is a variance at most \(1/4\), giving the inequality by integrating twice from zero. Iteration and optimization of the exponential Markov bound yield
\[
P\left(\sum_{i=1}^sD_i\geq h\right)\leq e^{-2h^2/s}.
\]
The same bound holds for the negative sum.

Apply the appropriate one-sided bound to each of the \(n\) comparator coordinates. With probability at least \(1-\delta/3\), all errors needed below are at most
\[
h=\sqrt{\frac{s}{2}\log(3n/\delta)}.
\]
The two realized regrets satisfy the exact cancellation identity
\[
R_A(s)+R_B(s)
=\max_b\sum_{i=1}^sY_i(a_i,b)-\min_a\sum_{i=1}^sY_i(a,J_i).
\]
The preceding concentration event therefore gives
\[
s\operatorname{Gap}(\bar u_s,\bar v_s)
\leq R_A(s)+R_B(s)+2h. \tag{5}
\]
This is the necessary correction: realized regret is not silently identified with mixed-policy regret.

Apply (4) to each non-singleton learner with failure probability \(\delta/3\), and combine it with (5). The total failure probability is at most \(\delta\). The following elementary coefficient estimates are useful:
\[
\frac{4\sum_{K\in\{A,B\},K\geq2}\sqrt{K\log K}}{\sqrt n}\leq4\log n,
\]
\[
\frac{2\sum_{K\in\{A,B\},K\geq2}\sqrt{K/\log K}+m/\sqrt s}{\sqrt n}<4.4,
\]
where \(m\leq2\) is the number of non-singleton players. For the first estimate, concavity of \(x\mapsto\sqrt{x\log x}\), extended continuously to \(x=1\), gives an upper bound \(4\sqrt{2\log(n/2)}\leq4\log n\). For the second, when \(n\geq4\), use \(\log K\geq\log2\), Cauchy--Schwarz, and \(m/\sqrt{ns}\leq1\), giving \(2\sqrt{2/\log2}+1<4.4\). When \(n=3\), there is only one non-singleton player, of size two, and direct substitution gives a smaller bound.

Consequently, for every \(\delta\in(0,1)\),
\[
P\left\{\operatorname{Gap}(\bar u_s,\bar v_s)>
\sqrt{\frac ns}\left[4\log n+4.4\log(6/\delta)
+\sqrt{\frac2n\log(3n/\delta)}\right]\right\}\leq\delta. \tag{6}
\]

### Moment calculation

Let \(E\) have the exponential distribution of mean one. Taking \(\delta=e^{-x}\) in (6) gives stochastic domination by the displayed increasing function of \(E\). Minkowski's inequality in \(L^2\) yields
\[
\begin{aligned}
\|\operatorname{Gap}(\bar u_s,\bar v_s)\|_2
\leq\sqrt{\frac ns}\bigg[&4\log n
+4.4\sqrt{(\log6)^2+2\log6+2}\\
&+\sqrt{\frac2n(\log(3n)+1)}\bigg].
\end{aligned}
\]
The bracket is at most \(11\log(2n)\) for \(n\geq3\). For an explicit loose verification, its last two terms are at most
\[
13.2+\sqrt{\tfrac23(\log(3n)+1)}.
\]
The resulting inequality holds at \(n=3\), and the derivative of \(11\log(2n)-4\log n-13.2-\sqrt{\tfrac23(\log(3n)+1)}\) is positive for \(n\geq3\).

Since \(0<p\leq2\), probability-space norm monotonicity gives the nonincreasing output bound
\[
\|\operatorname{Gap}(\bar u_s,\bar v_s)\|_p
\leq g_s:=11\sqrt{\frac ns}\log(2n),\qquad s\geq1. \tag{7}
\]
For \(n=2\), use the zero gap directly. In particular, (7) is no larger than \(11\sqrt{n/s}\log(4ns^2/p)\). No unsupported treatment of a failure event or small-p root is needed.

## 3. Synchronized procedure and information access

Set
\[
q_t=t^{-p/(2+p)},\qquad S_t=\sum_{i=1}^tq_i,
\]
and take a scheduling seed \(V\) uniform on \([0,1)\), independent of the virtual learners' random tapes and game observations. Define
\[
B_t=\lfloor S_t+V\rfloor-\lfloor S_{t-1}+V\rfloor,\qquad
N_t=\lfloor S_t+V\rfloor.
\]
Since \(0\leq q_t\leq1\), \(B_t\in\{0,1\}\). The identity \(\mathbb E\lfloor x+V\rfloor=x\) proves \(\mathbb E B_t=q_t\), including the endpoints. Telescoping gives \(N_t\geq\lfloor S_t\rfloor\).

On an exploration round, perform one virtual two-learner update. On an exploitation round, play the current virtual average policies and discard that round's actions and loss for purposes of all future updates.

Here is an explicit implementation satisfying the reduced-transcript restriction. Include in initial randomness an auxiliary sequence of independent uniforms for the max player's virtual arm selections, independent of \(V\). At exploration update \(i\), compute the virtual max policy \(v_i\), select its virtual arm \(J_i\) using the next auxiliary uniform, and announce the actual game policy \(e_{J_i}\). The actual sampled game action is then \(J_i\) with probability one. The max player updates using its internally selected \(J_i\) and the observed loss, without receiving the actual sampled \(b_t\). The min player announces \(u_i\), samples its ordinary game action, and updates from that action and the loss.

The auxiliary uniforms are independent of the min player's fresh action draws. The virtual arm/loss experiment is exactly the ordinary two-bandit experiment analyzed above. Replacing the max player's exploration policy by the selected point mass does not affect that experiment. The actual exploration gap is still at most one, which is the only property needed on exploration rounds.

On exploitation rounds, both players use their virtual mixed-policy averages; the sampled \(b_t\) and the loss are ignored. All max-player states can be reconstructed from its auxiliary initial tape, the scheduling seed, and the exploration losses; they do not require an observed \(b_t\) or the min player's action. The min player uses only its own actions, observed exploration losses, and the schedule. Thus the procedure is uncoupled and both policy maps are functions of the public task's reduced transcript. All initial tapes have a game-independent law, and the rule depends only on \(A,B,p\).

## 4. Conditional output bound and final constants

Condition on the scheduling seed \(V\), not on an arbitrary event in the learner's trajectory. The exploration calendar is then deterministic. Because exploitation feedback is ignored and the action-pair observation laws are fixed, the virtual trajectory has exactly its ordinary law conditional on \(V\). The independent auxiliary tapes retain their ordinary distributions. Thus (7) applies conditionally for each deterministic virtual update count.

On \(B_t=0\), the number of already completed updates is \(N_t=N_{t-1}\geq\lfloor S_t\rfloor\). Since \(q_1=1\), this count is at least one whenever exploitation occurs. Therefore
\[
\mathbb E\operatorname{Gap}(\mu_t,\nu_t)^p
\leq q_t+g_{\lfloor S_t\rfloor}^{\,p}.
\]
For every \(p>0\), \((x^p+y^p)^{1/p}\leq2^{1/p}(x+y)\), so
\[
\|\operatorname{Gap}(\mu_t,\nu_t)\|_p
\leq2^{1/p}\left(q_t^{1/p}+g_{\lfloor S_t\rfloor}\right). \tag{8}
\]
No independence of \(B_t\) from the past learner state has been assumed.

For every integer \(t\geq1\),
\[
S_t\geq tq_t=t^{2/(2+p)}\geq1,
\qquad \lfloor S_t\rfloor\geq S_t/2.
\]
Consequently,
\[
g_{\lfloor S_t\rfloor}\leq11\sqrt{2n}\log(2n)t^{-\alpha},
\qquad q_t^{1/p}=t^{-\alpha}.
\]
Since \(\log(4nt^2/p)\geq\log(2n)\), \(\sqrt n\log(4nt^2/p)\geq1\), and \(1+11\sqrt2<17\), equation (8) gives
\[
\|\operatorname{Gap}(\mu_t,\nu_t)\|_p
\leq17\sqrt{A+B}\,2^{1/p}t^{-\alpha}
\log\!\left(\frac{4(A+B)t^2}{p}\right).
\]
This includes \(t=1\) without an unspecified small-time adjustment; singleton players were handled above. The same rule works for every matrix and every collection of fixed entry laws in the public model.

The lower and upper bounds now concern a common reduced-transcript experiment. They establish the stated polynomial minimax rate, up to the displayed logarithmic factor.

## Obligation closure

Hard-family geometry, transcript measurability, KL attenuation, testing constants, stochastic regret-to-gap conversion, moment integration, synchronization, conditional virtual-law preservation, reduced-transcript implementability, and boundary cases have all been derived explicitly. The sole specialized external input is the stated standard EXP3-IX regret theorem, applied after verifying its nonanticipation and bounded-loss hypotheses. No unresolved private proof obligation remains.
