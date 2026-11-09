# Reference Proof

## Proof Structure

Construct the two trajectories using independent policy randomization and common independent arm-reward stacks. Establish the arm-specific stopping-time property and the required martingales. Prove both ordinary marginal laws and the joint replay law by matching conditional action and reward kernels, including the fresh-reward case after replay is exhausted. Obtain stopped moments and the cross-policy covariance at the minimum count. Finally, expand cumulative-reward covariances and bound every nonleading contribution.

## Complete Proof

Fix a positive integer horizon $T$. Independently generate $X_{a,k}\sim P_a$ for $1\le a\le K$, $1\le k\le T$, and uniforms $\eta_{i,r}$ for $i\in\{0,1\}$, $1\le r\le T$, all mutually independent. Realize each policy's action kernel by inverse-CDF sampling with its current uniform and its own history. In this construction, the $k$th pull of arm $a$ by either policy receives $X_{a,k}$. Stack positions are counted separately for each policy; a position used by one policy remains available to the other.

Write $H_{i,r}$ for the resulting history, $A_{i,r}$ and $R_{i,r}$ for the action and reward, and $n_{i,a}(r)$ for the number of pulls of arm $a$ through round $r$. These lowercase counts denote the stack construction, rather than the ordinary-run counts in the problem. Set $n_{i,a}=n_{i,a}(T)$ and $Z_{a,k}=X_{a,k}-\mu_a$.

### 1. Stopping times and martingales

For a fixed arm $a$, let $\mathcal F^a_m$ reveal all other-arm stacks, all policy uniforms, and the first $m$ entries of stack $a$, for $0\le m\le T$. To decide whether $n_{i,a}(r)\le m$, simulate the policy up to round $r$ with this information. Either the simulation finishes using at most $m$ entries of arm $a$, or it requests the $(m+1)$st entry. In the latter case the event is false before that entry's value is needed. This is a finite measurable procedure, so $\{n_{i,a}(r)\le m\}\in\mathcal F^a_m$. Thus every count is a stopping time bounded by $T$.

The same simulation proves that $H_{i,r}$ is measurable with respect to $\mathcal F^a_{n_{i,a}(r)}$. The next action is also measurable with respect to that stopped sigma-field, since all uniforms are included. Minima and maxima of these counts are bounded stopping times. Here, for a stopping time $U$, $\mathcal F^a_U$ consists of events $D$ such that $D\cap\{U\le m\}\in\mathcal F^a_m$ for each $m$.

For a Borel set $B\subseteq\mathbb R$, define, for $0\le m\le T$,
\[
I_{a,m}(B)=\sum_{k=1}^m(\mathbf1\{X_{a,k}\in B\}-P_a(B)),\qquad W_{a,m}=\sum_{k=1}^m Z_{a,k},\qquad V_{a,m}=W_{a,m}^2-m\sigma_a^2.
\]
All three start at zero. They are adapted and integrable. Since $Z_{a,m+1}$ is independent of $\mathcal F^a_m$, has mean zero, and has second moment $\sigma_a^2$, the increments of $I$ and $W$ have conditional mean zero. Moreover,
\[
V_{a,m+1}-V_{a,m}=2W_{a,m}Z_{a,m+1}+Z_{a,m+1}^2-\sigma_a^2
\]
has conditional mean zero. Thus these are martingales. In particular, $I$ counts centered reward-membership indicators, not centered arm pulls, and $W$ is a time-indexed process rather than a single stopped sum.

We use bounded discrete-time optional sampling: if $M$ is an integrable martingale and $U\le V\le T$ are stopping times, then $\mathbb E[M_V\mid\mathcal F_U]=M_U$. For completeness, expand $M_V-M_U$ as the finite sum $\sum_{k=1}^T\mathbf1\{U<k\le V\}(M_k-M_{k-1})$. For $D\in\mathcal F_U$, each event $D\cap\{U<k\le V\}$ belongs to $\mathcal F_{k-1}$, so every summand has zero expectation against $\mathbf1_D$. This proves the asserted conditional identity. All stopping times below are bounded, and the integrability hypotheses were just verified.

### 2. Ordinary marginal laws

The current uniform $\eta_{i,r}$ is independent of $H_{i,r-1}$, so the conditional action kernel is the prescribed policy kernel. Fix arm $a$ and Borel set $B$, and put $Q=n_{i,a}(r-1)$, $R=n_{i,a}(r)$. These are ordered bounded stopping times, and
\[
I_{a,R}(B)-I_{a,Q}(B)=\mathbf1\{A_{i,r}=a\}\bigl(\mathbf1\{R_{i,r}\in B\}-P_a(B)\bigr).
\]
This equality is globally defined, even if the arm has not been pulled. The history and selected action are measurable with respect to $\mathcal F^a_Q$. Optional sampling and the tower property therefore give zero conditional expectation for the displayed increment given $(H_{i,r-1},A_{i,r})$. On $\{A_{i,r}=a\}$ this says that the reward has conditional law $P_a$. Induction over rounds proves that each stack trajectory has the ordinary trajectory law.

### 3. Joint replay law

The control stack trajectory has the required phase-one law by Step 2. In treatment round $r$, the uniform $\eta_{1,r}$ is independent of $(H_{0,T},H_{1,r-1})$: the control uses no treatment uniforms, and the treatment history uses only earlier ones. Hence, conditional on these two histories, the action has the treatment policy's kernel based only on $H_{1,r-1}$.

Fix arm $a$ and set $q=n_{1,a}(r-1)$ and $c=n_{0,a}(T)$. On $\{A_{1,r}=a,q<c\}$, the reward $X_{a,q+1}$ is exactly the recorded $(q+1)$st control reward of arm $a$. Thus the replay branch agrees pathwise.

For the other branch, define the stopping times
\[
U=n_{1,a}(r-1)\vee n_{0,a}(T),\qquad V=n_{1,a}(r)\vee n_{0,a}(T).
\]
They satisfy $U\le V\le T$. Also,
\[
\mathcal G=\sigma(H_{0,T},H_{1,r-1},A_{1,r})\subseteq\mathcal F^a_U,
\]
by Step 1 and monotonicity of stopped sigma-fields. For every Borel $B$,
\[
I_{a,V}(B)-I_{a,U}(B)=\mathbf1\{A_{1,r}=a,q\ge c\}\bigl(\mathbf1\{R_{1,r}\in B\}-P_a(B)\bigr).
\]
Indeed, the maximum increases by one precisely on this event. Optional sampling gives conditional expectation zero given $\mathcal F^a_U$, and hence given $\mathcal G$. The event in the indicator is $\mathcal G$-measurable. Consequently, on the exhausted-replay branch, the conditional reward law given both histories and the action is $P_a$, exactly the fresh-reward kernel of the experiment.

Both reward branches and the action kernel therefore agree with the replay experiment. Induction over treatment rounds establishes equality of the full paired trajectory laws. Together with Step 2, this transfers the ordinary count assumptions to the stack counts:
\[
\mathbb E n_{i,a}=o(T),\qquad \operatorname{Var}(n_{i,a})=o(T)\quad(a\ne a^*).
\]

### 4. Stopped moments and cross-policy covariance

Write $S_{i,a}=W_{a,n_{i,a}}$. Optional sampling of $W$ and $V$ gives
\[
\mathbb E S_{i,a}=0,\qquad \mathbb E S_{i,a}^2=\sigma_a^2\mathbb E n_{i,a}.
\]
The same formulas hold with any bounded stopping time in place of $n_{i,a}$, in particular its minimum with another count. All stopped sums are square-integrable: pointwise, $|W_{a,U}|^2\le T\sum_{k=1}^T Z_{a,k}^2$ for $U\le T$.

For $i,j\in\{0,1\}$, put $U=n_{i,a}\wedge n_{j,a}$ and $V=n_{i,a}\vee n_{j,a}$. Pathwise, $S_{i,a}S_{j,a}=W_{a,U}W_{a,V}$. Since $\mathbb E[W_{a,V}\mid\mathcal F^a_U]=W_{a,U}$,
\[
\operatorname{Cov}(S_{i,a},S_{j,a})=\mathbb E[W_{a,U}W_{a,V}]=\mathbb E W_{a,U}^2=\sigma_a^2\mathbb E(n_{i,a}\wedge n_{j,a}).
\]
The multiplication inside conditional expectation is justified by square-integrability, or by truncating $W_{a,U}$ and passing to the limit using Cauchy--Schwarz.

### 5. Sublinear covariance contributions

Since the number of arms is fixed,
\[
\mathbb E n_{i,a^*}=T-\sum_{a\ne a^*}\mathbb E n_{i,a}=T-o(T).
\]
Furthermore,
\[
\operatorname{Var}(n_{i,a^*})\le\left(\sum_{a\ne a^*}\sqrt{\operatorname{Var}(n_{i,a})}\right)^2=o(T).
\]
Thus every arm-count variance is $o(T)$. This includes $K=1$, when the empty sum is zero and the sole count is identically $T$.

For all arms and both policies, Cauchy--Schwarz gives
\[
|\operatorname{Cov}(n_{i,a},n_{j,b})|\le\sqrt{\operatorname{Var}(n_{i,a})\operatorname{Var}(n_{j,b})}=o(T),
\]
and
\[
|\operatorname{Cov}(n_{i,a},S_{j,b})|\le\sqrt{\operatorname{Var}(n_{i,a})\sigma_b^2\mathbb E n_{j,b}}\le\sqrt{\sigma_b^2T\operatorname{Var}(n_{i,a})}=o(T).
\]
The reversed mixed covariance has the same bound with indices exchanged. If $a$ is suboptimal, then
\[
|\operatorname{Cov}(S_{i,a},S_{j,b})|\le\sqrt{\sigma_a^2\sigma_b^2\mathbb E n_{i,a}\mathbb E n_{j,b}}\le\sqrt{\sigma_a^2\sigma_b^2T\mathbb E n_{i,a}}=o(T).
\]
By symmetry this covers every centered-sum covariance with at least one suboptimal arm. These estimates require no positivity of any variance.

For the optimal arm,
\[
T-\sum_{a\ne a^*}(n_{0,a}+n_{1,a})\le n_{0,a^*}\wedge n_{1,a^*}\le T,
\]
so its expected minimum is $T-o(T)$. Step 4 now gives
\[
\frac{\operatorname{Cov}(S_{i,a^*},S_{j,a^*})}{T}\longrightarrow\sigma_{a^*}^2
\]
for all $i,j$, including the diagonal cases.

### 6. Cumulative-reward covariances and the targets

Let $Y_i^s=\sum_a(\mu_a n_{i,a}+S_{i,a})$ and $C_{ij}=\operatorname{Cov}(Y_i^s,Y_j^s)$. The exact expansion is
\[
C_{ij}=\sum_{a,b}\left[\operatorname{Cov}(S_{i,a},S_{j,b})+\mu_a\mu_b\operatorname{Cov}(n_{i,a},n_{j,b})+\mu_a\operatorname{Cov}(n_{i,a},S_{j,b})+\mu_b\operatorname{Cov}(S_{i,a},n_{j,b})\right].
\]
In particular, the count-count coefficient is $\mu_a\mu_b$. Because $K$, the means, and the variances are fixed, Step 5 shows that all terms except the optimal-arm centered-sum covariance are $o(T)$. Hence $C_{00}/T$, $C_{11}/T$, and $C_{01}/T$ all converge to $\sigma_{a^*}^2$.

By the ordinary marginal laws and independence of the two ordinary runs,
\[
\operatorname{Var}(\widehat\theta_{\mathrm{ind}}(T))=C_{11}+C_{00}.
\]
By the joint replay law,
\[
\operatorname{Var}(\widehat\theta_{\mathrm{cpl}}(T))=C_{11}+C_{00}-2C_{01}.
\]
Divide by $T$ and pass to the limit to obtain $2\sigma_{a^*}^2$ and $0$, respectively. This also covers $\sigma_{a^*}^2=0$; no strict linear-growth claim is needed.
