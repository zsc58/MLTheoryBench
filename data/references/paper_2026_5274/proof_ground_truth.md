# Reference Proof

## Proof Structure

We first derive the blockwise performance identity and the resulting directional-derivative formula. The limiting occupancy measure in the derivative calculation is justified explicitly by a finite-block mixture argument. The block occupancy is close to the initial distribution, which yields the approximate gradient-dominance bound. We then establish the Bregman mirror-descent inequalities, combine them with gradient dominance to control the last blockwise value, and finally compare that value with the expected value of a single deterministic policy drawn from the last mixture.

## Complete Proof

Write \(a=\gamma^k\), \(V_{\max}=c_{\max}/(1-\gamma)\), and \(f(q)=J^{q,k}(\mu)\). Every discounted value considered below has absolute value at most \(V_{\max}\), because the absolute discounted cost sum is bounded by \(\sum_{j\geq0}\gamma^j c_{\max}=V_{\max}\).

For the proof, let \(J_q(s)\) denote the blockwise value starting at \(s\). For distributions \(q,r\), let \(Q_q(s,r)\) be the expected discounted cost obtained by drawing a policy from \(r\) for the first block of \(k\) steps and then using blockwise distribution \(q\). All subsequent policy draws use fresh randomization, as in the blockwise rollout definition. Put
\[
 A_q(s,r)=Q_q(s,r)-J_q(s),\qquad
 d_\mu^{r,k}=(1-a)\sum_{m\geq0}a^m\operatorname{Law}(S_{mk}\mid\mu,r).
\]
Here the trajectory in the occupancy is run by resampling from \(r\) at every block boundary. The coefficients in this occupancy sum are nonnegative and sum to one.

For a finite signed measure \(\xi\), write
\[
 \|\xi\|_1=\sup_{u\text{ measurable},\ |u|\leq1}\left|\int u\,d\xi\right|.
\]
This is the total variation norm, equal to the sum of absolute masses in the discrete setting; the distance between two probability measures in this norm is at most \(2\). This measure norm is separate from the optimization norm in the problem.

### Blockwise performance and directional derivatives

The one-block Bellman expansion gives
\[
 J_r(s)-J_q(s)=A_q(s,r)+a\,\mathbb E[J_r(S_k)-J_q(S_k)\mid S_0=s,\text{ first block drawn from }r].
\]
Iterating for \(M\) blocks and averaging over \(S_0\sim\mu\) gives
\[
 f(r)-f(q)=\sum_{m=0}^{M-1}a^m\mathbb E_r[A_q(S_{mk},r)]
 +a^M\mathbb E_r[J_r(S_{Mk})-J_q(S_{Mk})].
\]
The final term has absolute value at most \(2a^M V_{\max}\), which tends to zero. Also \(|A_q(s,r)|\leq2V_{\max}\), so the series converges absolutely. Consequently
\[
 f(q)=f(r)-\frac{1}{1-a}\mathbb E_{S\sim d_\mu^{r,k}}[A_q(S,r)]. \tag{1}
\]

Conditioning on the policy drawn for the first block shows that \(Q_q(s,\cdot)\) is affine, and the blockwise Bellman identity gives \(Q_q(s,q)=J_q(s)\). Fix \(q,r\) and let \(r_\varepsilon=(1-\varepsilon)q+\varepsilon r\), with \(0<\varepsilon<1\). Equation (1) therefore yields the exact identity
\[
 \frac{f(r_\varepsilon)-f(q)}{\varepsilon}
 =\frac{1}{1-a}\mathbb E_{S\sim d_\mu^{r_\varepsilon,k}}[Q_q(S,r)-J_q(S)].
\]
To justify passage to the limit, realize each draw from \(r_\varepsilon\) by independently choosing the \(r\)-branch with probability \(\varepsilon\) and the \(q\)-branch otherwise. Among the first \(m\) blocks the probability of at least one \(r\)-branch is \(1-(1-\varepsilon)^m\leq m\varepsilon\). Conditional on no such branch, the state at time \(mk\) has exactly its law under \(q\). Thus
\[
 \left\|\operatorname{Law}_{r_\varepsilon}(S_{mk})-\operatorname{Law}_q(S_{mk})\right\|_1
 \leq2m\varepsilon,
\]
and hence
\[
 \|d_\mu^{r_\varepsilon,k}-d_\mu^{q,k}\|_1
 \leq2\varepsilon(1-a)\sum_{m\geq0}ma^m
 =\frac{2\varepsilon a}{1-a}\longrightarrow0.
\]
Because \(|Q_q(s,r)-J_q(s)|\leq2V_{\max}\), the expectation also converges. Differentiability of \(f\) now gives
\[
 \langle\nabla f(q),r-q\rangle
 =\frac{1}{1-a}\mathbb E_{S\sim d_\mu^{q,k}}[Q_q(S,r)-J_q(S)]. \tag{2}
\]
Only the one-sided feasible limit \(\varepsilon\downarrow0\) is used, so zero mixture weights and boundary points cause no additional restriction.

### Approximate gradient dominance

Splitting off the initial term of the occupancy series gives
\[
 d_\mu^{q,k}=(1-a)\mu+a\nu,\qquad
 \nu=(1-a)\sum_{m=1}^{\infty}a^{m-1}\operatorname{Law}_q(S_{mk}).
\]
The measure \(\nu\) is a probability measure. Therefore
\[
 \|d_\mu^{q,k}-\mu\|_1\leq2a. \tag{3}
\]
Let \(h(s)=Q_q(s,r)-J_q(s)\). Since \(|h(s)|\leq2V_{\max}\), equation (3) implies
\[
 \mathbb E_{d_\mu^{q,k}}h\leq\mathbb E_\mu h+4aV_{\max}. \tag{4}
\]
The first \(k\) steps in \(Q_q(s,r)\) and \(J_r(s)\) have the same law. More explicitly,
\[
 Q_q(s,r)-J_r(s)
 =a\,\mathbb E[J_q(S_k)-J_r(S_k)\mid S_0=s,\text{ first block drawn from }r].
\]
Their continuation values therefore differ by at most \(2aV_{\max}\), and
\[
 \mathbb E_\mu Q_q(S,r)\leq f(r)+2aV_{\max}.
\]
Combining this with (2) and (4), retaining the factor \((1-a)^{-1}\) on both error contributions, proves
\[
 \begin{aligned}
 \langle\nabla f(q),r-q\rangle
 &\leq\frac{f(r)-f(q)+2aV_{\max}}{1-a}
       +\frac{4aV_{\max}}{1-a}\\
 &=\frac{f(r)-f(q)}{1-a}+\frac{6a}{1-a}V_{\max}.
 \end{aligned} \tag{5}
\]
This is the required approximate gradient-dominance estimate for every feasible \(q,r\).

### Mirror-descent inequalities

Let \(g_t=\nabla f(q_t)\). For any feasible \(q\), the segment from the minimizer \(q_{t+1}\) to \(q\) is feasible. Differentiating the update objective along this segment at its minimum gives
\[
 \left\langle\eta g_t+\nabla\Phi(q_{t+1})-\nabla\Phi(q_t),q-q_{t+1}\right\rangle\geq0.
\]
Expanding the three Bregman divergences from their definition gives
\[
 \begin{aligned}
 &\langle\nabla\Phi(q_t)-\nabla\Phi(q_{t+1}),q_{t+1}-q\rangle\\
 &\qquad=D_\Phi(q,q_t)-D_\Phi(q,q_{t+1})-D_\Phi(q_{t+1},q_t).
 \end{aligned}
\]
It follows that
\[
 \langle g_t,q_{t+1}-q\rangle
 \leq\frac1\eta\left[D_\Phi(q,q_t)-D_\Phi(q,q_{t+1})-D_\Phi(q_{t+1},q_t)\right]. \tag{6}
\]

Taking \(q=q_t\) in (6), using \(D_\Phi(x,y)\geq(\lambda/2)\|x-y\|^2\) for both directed divergences, and then applying smoothness gives
\[
 \begin{aligned}
 f(q_{t+1})-f(q_t)
 &\leq\langle g_t,q_{t+1}-q_t\rangle+\frac\beta2\|q_{t+1}-q_t\|^2\\
 &\leq-\left(\frac\lambda\eta-\frac\beta2\right)\|q_{t+1}-q_t\|^2\\
 &=-\frac\lambda{2\eta}\|q_{t+1}-q_t\|^2\leq0,
 \end{aligned} \tag{7}
\]
where \(\eta=\lambda/\beta\). Thus \(f(q_t)\) is nonincreasing.

For the comparison distribution \(q^*\), decompose
\[
 -\langle g_t,q^*-q_t\rangle
 =\langle g_t,q_{t+1}-q^*\rangle-\langle g_t,q_{t+1}-q_t\rangle.
\]
Apply (6) to the first term with \(q=q^*\). Smoothness bounds the second term by
\[
 -\langle g_t,q_{t+1}-q_t\rangle
 \leq-[f(q_{t+1})-f(q_t)]+\frac\beta2\|q_{t+1}-q_t\|^2.
\]
Strong convexity changes the final quadratic term into at most \((\beta/\lambda)D_\Phi(q_{t+1},q_t)=\eta^{-1}D_\Phi(q_{t+1},q_t)\). This cancels the corresponding negative term from (6), so
\[
 -\langle g_t,q^*-q_t\rangle
 \leq\frac1\eta\left[D_\Phi(q^*,q_t)-D_\Phi(q^*,q_{t+1})\right]
 -[f(q_{t+1})-f(q_t)]. \tag{8}
\]
Averaging and telescoping, using nonnegativity of the terminal Bregman divergence, yields
\[
 \frac1T\sum_{t=0}^{T-1}-\langle g_t,q^*-q_t\rangle
 \leq\frac\beta{\lambda T}D_\Phi(q^*,q_0)
 -\frac1T\sum_{t=0}^{T-1}[f(q_{t+1})-f(q_t)]. \tag{9}
\]

### Last-iterate bound and output comparison

Because \(q^*\) always selects \(\pi^*\), its blockwise and deterministic rollouts coincide, giving \(f(q^*)=J^{\pi^*}(\mu)\). Apply (5) with \(r=q^*\), rearrange, average over \(t\), and use (9). This gives
\[
 \frac1T\sum_{t=0}^{T-1}\left[
 \frac{f(q_t)-f(q^*)}{1-a}+f(q_{t+1})-f(q_t)
 \right]
 \leq\frac\beta{\lambda T}D_\Phi(q^*,q_0)+\frac{6a}{1-a}V_{\max}. \tag{10}
\]
For each \(t\),
\[
 \begin{aligned}
 &\frac{f(q_t)-f(q^*)}{1-a}+f(q_{t+1})-f(q_t)\\
 &\qquad=\frac{f(q_{t+1})-f(q^*)}{1-a}
 +\frac{a}{1-a}[f(q_t)-f(q_{t+1})]\\
 &\qquad\geq\frac{f(q_{t+1})-f(q^*)}{1-a},
 \end{aligned}
\]
by (7). Again by monotonicity, \(f(q_T)\leq f(q_{t+1})\) for \(0\leq t<T\). Consequently
\[
 \begin{aligned}
 f(q_T)-J^{\pi^*}(\mu)
 &\leq6aV_{\max}+(1-a)\frac\beta{\lambda T}D_\Phi(q^*,q_0)\\
 &\leq6aV_{\max}+\frac\beta{\lambda T}D_\Phi(q^*,q_0).
 \end{aligned} \tag{11}
\]
The last relaxation uses \(1-a\leq1\) and nonnegativity of the divergence. This argument does not assume that \(q^*\) minimizes the blockwise objective or that any blockwise objective gap is nonnegative.

Finally, compare the blockwise rollout from \(q_T\) with a deterministic rollout obtained by drawing its initial policy \(\pi\sim q_T\) once and retaining it forever. The two rollout laws agree for the first \(k\) steps, including their initial-state law. Each remaining discounted tail has absolute value at most \(aV_{\max}\). Therefore
\[
 \mathbb E_{\pi\sim q_T}J^\pi(\mu)-f(q_T)\leq2aV_{\max}.
\]
Combining this inequality with (11) proves, for every integer \(T\geq1\),
\[
 \mathbb E_{\pi\sim q_T}J^\pi(\mu)-J^{\pi^*}(\mu)
 \leq\frac{8\gamma^k c_{\max}}{1-\gamma}
 +\frac\beta{\lambda T}D_\Phi(q^*,q_0).
\]
All denominators are positive because \(0<\gamma<1\) and \(k\geq1\). No division by \(c_{\max}\), a policy weight, or an objective gap occurs, so zero costs, singleton policy classes, and boundary iterates satisfying the stated differentiability and update definitions are covered.

## Private Source-Audit Notes

The source occupancy-index correction recorded under theory_009 is retained. In addition, the continuation-error term at source L000703 must retain the multiplier \((1-\gamma^k)^{-1}\) from L000701. Equation (5) above explicitly uses this corrected coefficient, yielding the unchanged final constant 6. The limiting occupancy calculation above closes the source's passage from its mixture expression to the directional derivative without appealing to a separate policy-gradient theorem or a support-positivity assumption.

The proof requires only monotonicity of the objective sequence, not convergence of the policy vectors. Bounded monotonicity also establishes convergence of the scalar objective values, but it must not be represented as a proof that the policy iterates themselves converge. Policy-vector convergence is not a claim in the frozen public task. There are no unresolved proof obligations for the requested finite-T inequality.
