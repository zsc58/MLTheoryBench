# Reference Proof

## Proof Structure and Dependencies

The eight obligations below establish the two frozen claims. The concentration argument uses the standard-independent Hoeffding inequality recorded as theory_015. The converse uses the standard-independent Bernoulli sampling lower bound recorded as theory_014. Their relevant statements and hypotheses are given below. All other obligations are derived explicitly from the public definitions and policy. There are no unresolved proof obligations.

## Complete Proof

### step_001: Simultaneous confidence control

Fix the instance and an integer horizon \(T\ge K\ge2\). The needed specialization of Hoeffding's inequality is: if \(V_1,\ldots,V_n\) are i.i.d. random variables in \([0,1]\) with mean \(v\), then
\[
\Pr\left(\left|n^{-1}\sum_{r=1}^nV_r-v\right|>\sqrt{\frac{2\log T}{n}}\right)\le2T^{-4}.
\]
This is the standard-independent result theory_015, used in the source at L000594–L000599.

For each arm \(a\), objective \(j\), and latent prefix length \(1\le n\le T\), apply this inequality to \(Y_{a,1,j},\ldots,Y_{a,n,j}\). These are i.i.d. bounded scalar variables, even though different coordinates of a reward vector need not be independent. A union bound over the \(KdT\) triples gives probability at most \(2KdT^{-3}\) that any such prefix mean violates its bound.

Define
\[
\Omega_T=\left\{\left|\widehat\mu_{a,j}(t-1)-\mu_{a,j}\right|\le\beta_a(t)\quad\text{for all }K<t\le T,\ a,j\right\}.
\]
The empirical mean after \(N_a(t-1)\) pulls is exactly the mean of that arm's first \(N_a(t-1)\) latent samples. The warm start ensures that these counts are positive. Thus the event controlling all latent prefixes implies \(\Omega_T\), despite adaptive sampling, and
\[
\Pr(\Omega_T^c)\le2KdT^{-3}.
\]
If \(T=K\), the defining range of rounds is empty and \(\Omega_T\) is the whole sample space. On \(\Omega_T\), whenever the indices are used,
\[
\mu_{a,j}\le U_{a,j}\le\mu_{a,j}+2\beta_a,
\qquad
\mu_{a,j}-2\beta_a\le L_{a,j}\le\mu_{a,j}.
\]

### step_002: Coordinate deficits control Pareto gaps

For every arm \(a\) and objective \(j\),
\[
0\le\Delta_a^P\le m_j-\mu_{a,j}.
\]
Indeed, if \(\varepsilon>m_j-\mu_{a,j}\), then the \(j\)-th coordinate of \(\mu_a+\varepsilon\mathbf1\) exceeds every arm's \(j\)-th mean. Consequently no arm dominates that shifted vector. Taking the infimum proves the inequality. In particular, \(\Delta_{\max}^P\le1\). Also \(0<g^\dagger\le1\) under the upper-bound assumptions.

This argument does not use the false converse that every zero-Pareto-gap arm is Pareto-optimal.

### step_003: Certification is valid, including its first round

Suppose an objective \(j\) certifies with leader \(b=b_j(t)\) and runner-up \(c=c_j(t)\). On \(\Omega_T\), for every \(a\ne b\), the top-two UCB ordering and the strict certification inequality give
\[
\mu_{a,j}\le U_{a,j}\le U_{c,j}<L_{b,j}\le\mu_{b,j}.
\]
Thus \(b\) is the unique objective-\(j\) maximizer. No other arm can dominate it, since every other arm is strictly worse in coordinate \(j\). Hence \(b\in A^\star\) and \(\Delta_b^P=0\).

Let \(\tau\) be the first certification round after the warm start, with \(\tau=T+1\) if no certification occurs by the horizon. The policy pulls the stored arm starting at round \(\tau\). Therefore every round \(t\ge\tau\) has zero Pareto regret on \(\Omega_T\). This establishes the source's certification implication directly; it does not assume that the certifying objective must maximize \(g_j\).

### step_004: Charge each non-certifying pull to its radius

Work on \(\Omega_T\) at a round \(K<t<\tau\). Let \(j\) be the selected objective, with top-two UCB arms \(b,c\). Suppress the round and objective indices in this paragraph. A true objective maximizer has UCB at least \(m_j\), so
\[
m_j\le U_b\le\mu_{b,j}+2\beta_b.
\]
If the policy samples \(b\), step_002 gives
\[
\Delta_b^P\le m_j-\mu_{b,j}\le2\beta_b\le4\beta_b.
\]
If it samples \(c\), use the exact identity \(U_b=L_b+2\beta_b\) and non-certification \(L_b\le U_c\) to obtain
\[
m_j\le U_b=L_b+2\beta_b\le U_c+2\beta_b
\le\mu_{c,j}+2\beta_c+2\beta_b.
\]
The selected endpoint has the larger radius, so in this case \(\beta_c\ge\beta_b\). Therefore
\[
\Delta_c^P\le m_j-\mu_{c,j}\le4\beta_c.
\]
This runner-up argument applies whether or not \(b\) is a true objective maximizer. In either case,
\[
\Delta_{A_t}^P\le4\beta_{A_t}(t).
\]

### step_005: An unresolved positive-gap objective forces a width floor

Let \(a^\dagger\) be the unique maximizer of objective \(j^\dagger\). At a non-certifying round, write \(b=b_{j^\dagger}(t)\), \(c=c_{j^\dagger}(t)\), and \(g=g^\dagger\).

If \(b=a^\dagger\), then
\[
\mu_{a^\dagger,j^\dagger}-2\beta_b
\le L_{b,j^\dagger}
\le U_{c,j^\dagger}
\le\mu_{a^\dagger,j^\dagger}-g+2\beta_c.
\]
Thus \(\beta_b+\beta_c\ge g/2\).

If \(b\ne a^\dagger\), then
\[
\mu_{a^\dagger,j^\dagger}
\le U_{a^\dagger,j^\dagger}
\le U_{b,j^\dagger}
\le\mu_{a^\dagger,j^\dagger}-g+2\beta_b,
\]
so \(\beta_b\ge g/2\), again implying \(\beta_b+\beta_c\ge g/2\).

The policy selects a pair of maximal radius sum across objectives and then the endpoint with larger radius. Consequently, on every non-certifying round,
\[
\beta_{A_t}(t)\ge g^\dagger/4.
\]
Other objectives may have ties and gap zero; no positivity assumption on those objectives is used.

### step_006: Count pulls, sum charges, and take expectations

Let \(m_a\) be the number of pulls of arm \(a\) after the warm start and strictly before \(\tau\). These counts are nonnegative integers and may be zero. If \(t_{a,s}\) is the \(s\)-th such pull, then all prior post-warm-start pulls of this arm were also before certification. Hence
\[
N_a(t_{a,s}-1)=s,\qquad
\beta_a(t_{a,s})=\sqrt{\frac{2\log T}{s}}.
\]
The width floor implies, for every \(1\le s\le m_a\),
\[
s\le\frac{32\log T}{(g^\dagger)^2}.
\]
Taking \(s=m_a\) when \(m_a>0\) gives
\[
m_a\le\frac{32\log T}{(g^\dagger)^2},
\]
which also holds for \(m_a=0\). There is no extra-pull correction: these are post-warm-start pull counts, whose successive pre-pull counts start at one.

For \(m\ge1\), integration gives
\[
\sum_{s=1}^m s^{-1/2}\le1+\int_1^m x^{-1/2}\,dx\le2\sqrt m.
\]
For \(m=0\), both sides are zero. Combining the warm start, steps_003–005, and this inequality gives on \(\Omega_T\)
\[
\begin{aligned}
R_T^P
&\le K\Delta_{\max}^P+
4\sqrt{2\log T}\sum_{a=1}^K\sum_{s=1}^{m_a}s^{-1/2}\\
&\le K\Delta_{\max}^P+
8\sqrt{2\log T}\sum_{a=1}^K\sqrt{m_a}\\
&\le K\Delta_{\max}^P+64\frac{K\log T}{g^\dagger}.
\end{aligned}
\]
The same argument covers \(T=K\) and no certification before the horizon by the conventions already given.

On every outcome, \(R_T^P\le T\Delta_{\max}^P\). Thus
\[
\begin{aligned}
\mathbb E[R_T^P]
&=\mathbb E[R_T^P\mathbf1_{\Omega_T}]+\mathbb E[R_T^P\mathbf1_{\Omega_T^c}]\\
&\le K\Delta_{\max}^P+64\frac{K\log T}{g^\dagger}
+T\Delta_{\max}^P\Pr(\Omega_T^c)\\
&\le K\Delta_{\max}^P+64\frac{K\log T}{g^\dagger}
+2Kd\Delta_{\max}^P T^{-2}.
\end{aligned}
\]
For each fixed instance, the warm-start term and the failure contribution are lower order than \(K\log T/g^\dagger\), proving the asserted asymptotic order. This does not assert that the displayed dimension-dependent tail can be omitted uniformly over arbitrary choices of \(d=d(T)\).

### step_007: Establish the scalar experiment and its goodness condition

Fix \(K,d\), and restrict a full-model policy to the family of instances
\[
Y_{a,n}=Z_{a,n}\mathbf1,\qquad Z_{a,n}\sim\operatorname{Bernoulli}(\theta_a),
\qquad \theta\in(0,1)^K,
\]
with independent scalar samples across arms and pulls. Feeding each observed scalar to the vector policy as a duplicated vector defines a scalar policy with the same actions and pull counts. Conversely, the scalar is recovered from any coordinate of the vector. The history contains no additional samples or information from the other coordinates. The information restriction and instance-independent decision rules ensure that this is one non-anticipatory scalar policy across the entire Bernoulli family.

For any such \(\theta\), put \(\theta_* = \max_a\theta_a\). In the duplicated instance,
\[
A^\star=\{a:\theta_a=\theta_*\}.
\]
Therefore full-model uniform goodness implies, for every \(\theta\in(0,1)^K\), every \(\alpha>0\), and each arm with \(\theta_a<\theta_*\),
\[
\mathbb E_\theta[N_a(T)]=o(T^\alpha).
\]
Because there are finitely many arms,
\[
\mathbb E_\theta\left[\sum_{t=1}^T(\theta_*-\theta_{A_t})\right]
=\sum_{a:\theta_a<\theta_*}(\theta_*-\theta_a)\mathbb E_\theta[N_a(T)]
=o(T^\alpha).
\]
This also holds when several or all arms are optimal, since optimal arms contribute zero. Thus the source's scalar uniform-goodness assumption holds for every Bernoulli mean vector, including alternatives changing the identity of the best arm. It is not inferred merely from performance at the displayed instance.

Now specialize to \(\theta_1=1/2+\Delta_{\rm sc}\) and \(\theta_a=1/2\) for \(a\ge2\). Arm 1 strictly dominates every other arm and uniquely maximizes every objective, so
\[
A^\star=\{1\},\qquad g_j=g^\dagger=\Delta_{\rm sc}.
\]
In particular, this instance satisfies marginal-Pareto consistency and the upper bound's positive-gap condition. For \(a\ge2\), a shift smaller than \(\Delta_{\rm sc}\) is still dominated by arm 1, whereas at shift \(\Delta_{\rm sc}\) the vectors coincide and strict domination ceases. Hence
\[
\Delta_1^P=0,\qquad\Delta_a^P=\Delta_{\rm sc}\ (a\ge2),\qquad
R_T^P=\Delta_{\rm sc}\sum_{a=2}^K N_a(T).
\]

### step_008: Apply the audited sampling lower bound and evaluate its constant

The relevant standard-independent Bernoulli form of the Lai–Robbins sampling lower bound is as follows. For a non-anticipatory policy with no access to the unknown means, suppose that for every \(\theta\in(0,1)^K\) and every \(\alpha>0\), its expected scalar regret is \(o(T^\alpha)\). At any such instance, for each arm with \(\theta_a<\theta_*\),
\[
\liminf_{T\to\infty}\frac{\mathbb E_\theta[N_a(T)]}{\log T}
\ge\frac{1}{\inf_{q\in(\theta_*,1)}\operatorname{kl}(\theta_a,q)},
\]
where
\[
\operatorname{kl}(p,q)=p\log\frac pq+(1-p)\log\frac{1-p}{1-q}.
\]
This is theory_014, invoked and specialized in the source at L000794–L000805. Step_007 verifies the policy and uniform-goodness hypotheses, and the independent Bernoulli sampling model is exactly the required observation experiment.

Here \(\theta_a=1/2\) for \(a\ge2\) and \(\theta_*=1/2+\Delta_{\rm sc}\le3/4<1\), so the alternative interval is nonempty. For \(q>1/2\),
\[
\frac{\partial}{\partial q}\operatorname{kl}(1/2,q)=\frac{q-1/2}{q(1-q)}>0.
\]
Continuity at \(q=1/2+\Delta_{\rm sc}\) therefore gives
\[
\inf_{q\in(1/2+\Delta_{\rm sc},1)}\operatorname{kl}(1/2,q)
=\operatorname{kl}(1/2,1/2+\Delta_{\rm sc}).
\]
It is finite and positive because \(0<\Delta_{\rm sc}\le1/4\). Applying the lower bound to each inferior arm and using the finite-sum liminf inequality yields
\[
\liminf_{T\to\infty}\frac{\mathbb E[R_T^P]}{\log T}
\ge (K-1)\frac{\Delta_{\rm sc}}{\operatorname{kl}(1/2,1/2+\Delta_{\rm sc})}.
\]
Finally,
\[
\operatorname{kl}(1/2,1/2+\Delta_{\rm sc})=-\tfrac12\log(1-4\Delta_{\rm sc}^2).
\]
For \(0\le x<1\), integration gives
\[
-\log(1-x)=\int_0^x\frac{du}{1-u}\le\frac{x}{1-x}.
\]
Taking \(x=4\Delta_{\rm sc}^2\le1/4\), we obtain
\[
\operatorname{kl}(1/2,1/2+\Delta_{\rm sc})
\le\frac{2\Delta_{\rm sc}^2}{1-4\Delta_{\rm sc}^2}
\le\tfrac83\Delta_{\rm sc}^2.
\]
Consequently,
\[
\liminf_{T\to\infty}\frac{\mathbb E[R_T^P]}{\log T}
\ge\frac38\frac{K-1}{\Delta_{\rm sc}}.
\]
Since \(K-1\ge K/2\) and \(g^\dagger=\Delta_{\rm sc}\), this supplies the claimed full-model order obstruction. It is an obstruction on a subclass, not a lower bound on every multi-objective geometry. No assertion that the upper-bound policy is uniformly good on all instances with \(g^\dagger=0\) is needed.
