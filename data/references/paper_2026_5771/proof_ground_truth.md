# Reference Proof

## Proof Structure

Derive suffix-uniform canonical mixing, extract canonical blocks from adaptive exploration, and establish simultaneous confidence bounds under adaptive sampling. Use these facts to prove correctness of every certified stop and a deterministic upper bound on stopping. Bound navigation conditional on the actual stopping history and combine costs through pseudo-regret. Finally repeat the count argument with the assumed gain coefficients and compare all near-bottleneck arms.

## Complete Proof

Write
\[
L=\log(4nT/\delta),\qquad g(i^\star)=\Delta_{\min},\qquad g(i)=\Delta_i\quad(i\ne i^\star).
\]
The unique optimum and bounded rewards imply \(0<g(i)\le1\) for every arm. A good undirected snapshot is connected: otherwise its canonical kernel has eigenvalue one with multiplicity at least two and absolute gap zero. Its stationary distribution is strictly positive. Since a good snapshot exists and all kernels share \(\pi\), we have \(\pi_{\min}>0\).

Structural estimates below can be proved after conditioning on a realized graph sequence and then averaged over that sequence. This is permitted by obliviousness and independence of the learner's fresh randomness. We do not condition the assumed gain inequality on the full graph sequence: that inequality is used only with its stated pre-block history.

### 1. Uniform canonical-walk mixing

For a distribution \(\nu\), write its density relative to \(\pi\) as \(f\). Reversibility makes the action of a kernel \(P_t\) on densities self-adjoint in \(L^2(\pi)\). On mean-zero functions its operator norm is the largest absolute nontrivial eigenvalue. Hence it is at most one always and at most \(1-\gamma\le e^{-\gamma}\) on a good round. This follows by expanding a mean-zero function in an orthonormal eigenbasis of the reversible operator.

Partition an interval of length \(\ell\) into \(\lfloor\ell/W\rfloor\) complete windows and a remainder. The number of good rounds is at least
\[
\lfloor\ell/W\rfloor\lceil\rho W\rceil\ge\rho(\ell-W).
\]
For a point mass at any starting state, the initial mean-zero density norm is at most \(\pi_{\min}^{-1/2}\). Cauchy–Schwarz gives total variation at most one half of this density norm. Therefore, uniformly over every starting state and time,
\[
\left\|\delta_xP_{s+1}\cdots P_{s+\ell}-\pi\right\|_{\rm TV}
\le \frac{1}{2\sqrt{\pi_{\min}}}e^{-\rho\gamma(\ell-W)}.
\tag{1}
\]
At \(\ell=h_0\), the right side is at most \(\pi_{\min}^{3/2}/2\le\pi_{\min}/2\). At \(\ell=h_1\), it is at most \(e^{-\rho\gamma}\pi_{\min}/4\le\pi_{\min}/2\). No ordering between \(h_0\) and \(h_1\) is needed. Thus, for either \(h=h_0\) or \(h=h_1\), a canonical walk satisfies
\[
\Pr(Y_{s+h}=i\mid Y_s=x,\text{graph sequence})\ge\pi_i/2.
\tag{2}
\]
The estimate is uniform in the graph realization satisfying the assumptions, the starting time, and the starting state.

### 2. Adaptive canonical blocks

When \(\varepsilon_0<1\), write
\[
M_t=\varepsilon_0P_t+(1-\varepsilon_0)Q_t,
\qquad
Q_t=\frac{(\varepsilon_t-\varepsilon_0)P_t+(1-\varepsilon_t)q_t}{1-\varepsilon_0}.
\]
The coefficients are nonnegative and sum to one, so \(Q_t\) is a local stochastic kernel, possibly depending on previous rewards. Realize this decomposition using independent Bernoulli mixture coins of success probability \(\varepsilon_0\), fresh at each transition and independent of graphs, rewards, and transition draws. If \(\varepsilon_0=1\), every transition is canonical and no residual kernel is needed.

Conditional on the history before a block of length \(h\), its mixture coins all choose the canonical component with probability \(\varepsilon_0^h\). Conditional also on the graph sequence and this coin event, the block follows the canonical kernels throughout. Equation (2), followed by averaging over graph realizations, therefore yields for perpetual exploration
\[
\Pr(\widetilde X_{s+h}=i\mid\widetilde{\mathcal F}_s)
\ge\frac{\varepsilon_0^h}{2}\pi_i.
\tag{3}
\]
This holds for both block lengths. The fresh coins are only a proof construction; they do not change the law or information available to the algorithm.

### 3. Confidence under adaptive sampling

The fresh conditional reward law permits an observationally equivalent construction using, for each arm, an infinite i.i.d. table with distribution \(D_i\), independent of graph and learner randomness. Each pull reveals the next unused entry of that arm's table. We apply concentration to fixed table prefixes, not to an empirical mean conditional on a reward-dependent sample count.

For independent \([0,1]\)-valued variables of mean \(\mu_i\), Hoeffding's inequality states
\[
\Pr\left(\left|\frac1r\sum_{k=1}^rY_{i,k}-\mu_i\right|>a\right)
\le2e^{-2ra^2}.
\]
All its hypotheses hold for each fixed table prefix. Taking \(a=\sqrt{L/(2r)}\) and summing over \(nT\) arm/prefix pairs gives failure probability at most \(2nTe^{-L}=\delta/2\). Consequently there is an event \(E\), of probability at least \(1-\delta/2\), on which
\[
|\widehat\mu_s(i)-\mu_i|\le w_s(i)
\tag{4}
\]
for all observed prefixes through time \(T\), including those of the perpetual process and its stopped coupling. At zero observations, (4) holds deterministically because the empirical mean is zero, the width is one, and \(\mu_i\in[0,1]\).

On \(E\), any certificate must name the optimal arm. Indeed, if a certified leader \(b\ne i^\star\) existed, then
\[
\mu_b\ge\operatorname{LCB}(b)
\ge\operatorname{UCB}(i^\star)\ge\mu_{i^\star},
\]
contradicting uniqueness. This rules out an incorrect earlier stop, not merely an incorrect leader at the nominal time.

### 4. Adapted count concentration and worst-case stopping

Here is the adapted lower-tail estimate needed below. Let \(Z_j\in\{0,1\}\) be adapted and satisfy \(\mathbb E[Z_j\mid\mathcal H_{j-1}]\ge p\). For \(a>0\),
\[
\mathbb E[e^{-aZ_j}\mid\mathcal H_{j-1}]
\le1-p(1-e^{-a})\le e^{-p(1-e^{-a})}.
\]
Iteration and Markov's inequality, with \(a=\log2\), imply
\[
\Pr\left(\sum_{j=1}^mZ_j<mp/2\right)
\le \exp\left[-mp\left(\frac12-\frac{\log2}{2}\right)\right]
\le e^{-mp/8}.
\tag{5}
\]
Thus no independence between different block indicators is required.

Set \(p_i=\vartheta_0\pi_i\) and
\[
m_0=\left\lceil64\max_i\frac{L}{p_i g(i)^2}\right\rceil.
\]
Apply (5) to \(Z_j=\mathbf1\{\widetilde X_{jh_0}=i\}\), using (3). For every arm, \(m_0p_i\ge64L/g(i)^2\). A union bound shows that, except with probability at most
\[
\sum_i e^{-m_0p_i/8}\le ne^{-8L}\le\delta/2,
\]
all endpoint counts, and hence all observation counts at time \(h_0m_0\), are at least \(32L/g(i)^2\). This argument is used only when \(h_0m_0\le T\).

These counts imply \(w(i)\le g(i)/8\). On \(E\), for each \(i\ne i^\star\),
\[
\operatorname{LCB}(i^\star)-\operatorname{UCB}(i)
\ge\Delta_i-2w(i^\star)-2w(i)
\ge\Delta_i-\frac{\Delta_{\min}+\Delta_i}{4}
\ge\Delta_i/2>0.
\tag{6}
\]
In particular, the empirical leader is uniquely \(i^\star\) and its certificate holds at that time.

Couple the actual procedure and perpetual exploration using identical randomness until the actual procedure stops. If the actual procedure has not stopped earlier, (6) forces it to stop by \(h_0m_0\); if it has stopped earlier, (4) proves its certificate was correct. The endpoint event and \(E\) together have probability at least \(1-\delta\). Thus the first claim holds with the universal choice \(C=64\), or any larger universal constant. Since each realized learning-round regret is at most one,
\[
R_{\rm learn}=\sum_{t=1}^{\sigma}(\mu_{i^\star}-r_t)\le\sigma\le T_0
\]
on this event. This also covers certification at the horizon itself.

### 5. Navigation and expected regret

Condition on any actual stopping history that commits to \(i^\star\). If the learner is already there, its navigation time is zero. Otherwise start a canonical comparison walk at the same state and time. Until the first round in which the target is locally available, use identical canonical transitions for the two processes. On that round navigation moves directly to the target. If the comparison walk reaches the target, the target was locally available on that transition, so navigation reaches it no later than the comparison walk.

By (2), after any additional \(h_0\) canonical steps the endpoint is \(i^\star\) with conditional probability at least \(p=\pi_{i^\star}/2\), uniformly in the intervening history. This remains true on the random suffix: prove it conditional on a graph realization and the stopping state and time, and then average. If \(H\) is the comparison hitting time, iteration gives
\[
\Pr(H>kh_0\mid\mathcal F_\sigma)\le(1-p)^k,
\qquad
\mathbb E[H\mid\mathcal F_\sigma]\le\frac{h_0}{p}=\frac{2h_0}{\pi_{i^\star}}.
\tag{7}
\]
Horizon truncation can only reduce navigation cost. Conditional on any such stopping history, the expected post-exploration pseudo-regret is therefore at most
\[
B_0=\frac{2\Delta_{\max}h_0}{\pi_{i^\star}}.
\tag{8}
\]
Once the target is reached its pseudo-regret is zero.

To combine this with high-probability learning, use pseudo-regret rather than conditioning realized reward noise on a confidence event. Define
\[
D_T=\sum_{t=1}^T\Delta_{X_t},\qquad
D_{\rm post}=\sum_{t=\sigma+1}^T\Delta_{X_t},\qquad
S=\{\sigma\le T_0,\ b_\sigma=i^\star\}.
\]
Fresh reward sampling gives \(\mathbb E R(T)=\mathbb E D_T\). The preceding result gives \(\Pr(S^c)\le\delta\), and \(S\) is measurable at the actual stopping time. Since pseudo-regret is nonnegative and each gap is at most one,
\[
D_T\le T_0+\mathbf1_S D_{\rm post}+T\mathbf1_{S^c}.
\]
By (8) and conditioning on \(\mathcal F_\sigma\),
\[
\mathbb E[\mathbf1_S D_{\rm post}]\le B_0.
\]
Thus
\[
\mathbb E R(T)\le T_0+B_0+T\delta.
\]
Taking \(\delta=T^{-2}\) proves the asserted bound with \(+1\). For fixed problem parameters, \(T_0=O(\log T)\), so the horizon condition holds for all sufficiently large \(T\), and \(\mathbb E R(T)=o(T)\).

### 6. Post-burn-in stopping

Use the perpetual process and exactly the filtration \(\mathcal G_{j-1}=\widetilde{\mathcal F}_{s_j}\) in the public gain assumption. For \(i\in B\), that assumption gives the conditional endpoint lower bound \(\kappa_i\). For \(i\notin B\), equation (3), with \(h=h_1\), gives the bound \(\kappa_i=\vartheta_1\pi_i\) with respect to the same filtration. No extra conditioning on future graphs is imposed on the gain assumption.

Set
\[
m_g=\lceil64\Psi_g(\delta)\rceil.
\]
Under \(T\ge t_g+h_1m_g\), all these blocks are applicable. In particular there is at least one applicable block, so the assumed probability bounds imply \(\kappa_i\le1\) on \(B\); the same bound holds by definition outside \(B\).

Apply (5) with \(p=\kappa_i\). Exactly as before, except with probability at most \(\delta/2\), every arm has at least \(32L/g(i)^2\) endpoint observations by \(t_g+h_1m_g\). Burn-in observations can only increase the counts. Intersect with \(E\), apply (6), and use the stopped/perpetual coupling and correctness of every earlier certificate. With probability at least \(1-\delta\),
\[
b_\sigma=i^\star,\qquad \sigma\le T_g,\qquad R_{\rm learn}\le T_g.
\]
Thus the same universal \(C=64\) works in both parts.

### 7. Global gain and rounding

If \(i\in H_\zeta\), then
\[
\frac1{\kappa_i g(i)^2}
\le\frac{\Lambda_i}{(1+\zeta)\vartheta_1}
\le\frac{\Lambda_{\max}}{(1+\zeta)\vartheta_1}.
\]
If \(i\notin H_\zeta\), then \(\Lambda_i<\Lambda_{\max}/(1+\zeta)\), and \(\kappa_i\ge\vartheta_1\pi_i\) gives the same strict upper bound. Therefore
\[
\Psi_g(\delta)\le A:=\frac{L\Lambda_{\max}}{(1+\zeta)\vartheta_1}.
\tag{9}
\]
Under the horizon condition, the preceding probability argument gives \(\kappa_i\le1\), while \(g(i)\le1\). Consequently \(\Psi_g\ge L>1\), so \(A>1\). The ceiling is therefore harmless:
\[
T_g=t_g+h_1\lceil C\Psi_g\rceil
\le t_g+(C+1)h_1A.
\]
This proves the claimed big-O estimate with an absolute implicit constant. Relative to the same-block-length baseline \(\kappa_i=\vartheta_1\pi_i\), whose complexity is \(L\Lambda_{\max}/\vartheta_1\), equation (9) reduces the leading learning term by the claimed factor. This comparison does not assert that \(h_1\) equals or exceeds \(h_0\), or that burn-in and integer rounding are reduced by that factor.
