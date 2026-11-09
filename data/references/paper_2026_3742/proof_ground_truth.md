# Reference Proof

All almost-sure assertions below concern a fixed choice of $\Theta$. If $K=1$, the sole arm is always drawn and $R(T)=0$, so assume $K\geq2$. Write $N_i(t)$ for counts after $t$ pulls and put
$$
\Lambda_t(j)=\inf_{v\in\Theta_j}\frac12\sum_iN_i(t)(v_i-\widehat\mu_i(t))^2,\quad
\bar\Lambda_t(j)=\inf_{v\in\Theta_j}\frac12\sum_iN_i(t)(v_i-\mu_i)^2,\quad
r_t=\sum_iN_i(t)(\widehat\mu_i(t)-\mu_i)^2.
$$
Both infima are $+\infty$ for an empty hypothesis; products with zero counts are zero. For $t\geq1$, canceling the common factors in the profile likelihood gives $Q_t(j)=e^{-\Lambda_t(j)}/\sum_i e^{-\Lambda_t(i)}$. Thus, for a nonempty hypothesis, $Q_t(j)/Q_t(j^*)=e^{-[\Lambda_t(j)-\Lambda_t(j^*)]}$. This identity is not used to redefine $Q_0$: the first arm is drawn from the uniform prior. An empty hypothesis can be drawn on that first round, but $Q_t(j)=0$ for every $t\geq1$, so its total pull count is at most one.

**Empirical and Population Losses.** For $0<\varepsilon<1$, expanding weighted squares, applying $2|ab|\leq\varepsilon a^2+\varepsilon^{-1}b^2$, and using $\mu\in\Theta_{j^*}$ yield, for every nonempty $\Theta_j$,
$$
(1-\varepsilon)\bar\Lambda_t(j)-2\varepsilon^{-1}r_t
\leq\Lambda_t(j)-\Lambda_t(j^*)
\leq(1+\varepsilon)\bar\Lambda_t(j)+2\varepsilon^{-1}r_t.\tag{1}
$$
The Hartman–Wintner iterated-logarithm law applies to each independent i.i.d. arm sequence of finite, positive variance: for every $C>2$, its first $n$ rewards have an empirical mean satisfying $n(\widehat\mu_{i,n}-\mu_i)^2\leq C\sigma_i^2\log\log n$ eventually, almost surely. A zero-variance arm has constant rewards almost surely. If an arm has been sampled only finitely often, its fixed weighted squared error is eventually bounded by $C\sigma_i^2\log\log t$ when $\sigma_i^2>0$; for zero variance that error is zero. Taking the intersection over finitely many arms therefore gives
$$
r_t\leq C\sum_i\sigma_i^2\log\log t=O(\log\log t)=o(\log t)\quad\text{eventually, almost surely}.\tag{2}
$$

**Universal Upper Bound.** For a nonempty suboptimal hypothesis, every $v\in\Theta_j$ satisfies $v_j\geq v_{j^*}$. Restricting its quadratic loss to those two coordinates and minimizing gives, with $0/0$ interpreted as zero,
$$
\bar\Lambda_t(j)\geq\frac{\Delta_j^2}{2}\frac{N_{j^*}(t)N_j(t)}{N_{j^*}(t)+N_j(t)}.\tag{3}
$$
Because $\Lambda_t(j^*)\leq r_t/2$ and each $e^{-\Lambda_t(i)}\leq1$, (2) implies that, for some finite $A\geq0$,
$$
Q_{t-1}(j^*)\geq [K(\log t)^A]^{-1}\quad\text{eventually}.\tag{4}
$$
Here and below, an event or inequality at round $t$ uses the history through round $t-1$; the finite shift in (2) does not change an eventual bound. Let $p_s=Q_{s-1}(j^*)$. Then $M_t=N_{j^*}(t)-\sum_{s=1}^t p_s$ is a martingale with increments bounded by one. Azuma–Hoeffding gives $\mathbb P(|M_t|\geq2\sqrt{t\log t})\leq2t^{-2}$; Borel–Cantelli and (4) imply, eventually,
$$
N_{j^*}(t)\geq\frac{t}{3K(\log t)^A}.\tag{5}
$$
Fix $j\ne j^*$ with nonempty hypothesis and $\delta>0$. For any $a,b\geq0$ and $0<h<1$, $ab/(a+b)\geq\min\{ha,(1-h)b\}$, again taking $0/0=0$. Apply this to (3), use (1), (2), and (5), and choose $h$ and $\varepsilon$ sufficiently small. There is then $\eta>0$ such that for all sufficiently large $t$,
$$
N_j(t-1)\geq\frac{2+\delta}{\Delta_j^2}\log t
\quad\Longrightarrow\quad
\Lambda_{t-1}(j)-\Lambda_{t-1}(j^*)\geq(1+\eta)\log t.
$$
Consequently $\mathbb P(A_t=j\mid D_{t-1})=Q_{t-1}(j)\leq t^{-(1+\eta)}$ whenever that threshold is crossed. The conditional probabilities of pulls above the threshold are summable, so conditional Borel–Cantelli makes their number finite almost surely. Since counts grow by at most one and the threshold increases to infinity, the count can thereafter exceed the threshold by at most an eventually negligible constant. Let $\delta\downarrow0$ through a countable sequence to obtain
$$
\limsup_{T\to\infty}\frac{N_j(T)}{\log T}\leq\frac{2}{\Delta_j^2}\quad\text{almost surely}.\tag{6}
$$
Empty hypotheses have $N_j(T)\leq1$, as established above. Summing $R(T)=\sum_{j\ne j^*}\Delta_jN_j(T)$ proves the universal regret bound.

**Feasible Alternatives and Lower Counts.** Suppose $v^{(j)}=\mu+\Delta_je_j\in\Theta$. It belongs to $\Theta_j$, and $\bar\Lambda_{t-1}(j)\leq\Delta_j^2N_j(t-1)/2$. Fix $0<\beta<2/\Delta_j^2$. By (1), (2), and (4), choosing $\varepsilon$ sufficiently small gives a number $\eta\in(0,1)$ such that, almost surely for all sufficiently large $t$,
$$
N_j(t-1)\leq\beta\log t
\quad\Longrightarrow\quad
p_t:=\mathbb P(A_t=j\mid D_{t-1})\geq t^{-(1-\eta)}.\tag{7}
$$
Here is a complete pathwise conversion of (7). For a dyadic block $I_m=\{2^m+1,\ldots,2^{m+1}\}$, let $F_m=\{N_j(2^{m+1})<\beta m\log2\}$ and let $G_m$ be the event that the implication (7) holds at every round of that block. Equation (7) makes $G_m$ true eventually on the almost-sure event under consideration. Set $Y_t=\mathbf1\{A_t=j,\,N_j(t-1)\leq\beta\log t\}$ and $q_t=\mathbb E(Y_t\mid D_{t-1})$. On $F_m\cap G_m$, the count stays below $\beta\log t$ throughout $I_m$, so
$$
\sum_{t\in I_m}Y_t<\beta m\log2,
\qquad
\sum_{t\in I_m}q_t\geq2^m(2^{m+1})^{-(1-\eta)}=2^{\eta m+\eta-1}.
$$
Conditional Bernoulli sampling makes $\exp[-\sum_{t\in I_m}Y_t+(1-e^{-1})\sum_{t\in I_m}q_t]$ the terminal value of a nonnegative supermartingale starting at one. Markov's inequality therefore bounds $\mathbb P(F_m\cap G_m)$ by $\exp[\beta m\log2-(1-e^{-1})2^{\eta m+\eta-1}]$, which is summable. Ordinary Borel–Cantelli, together with eventual $G_m$, implies $F_m$ occurs only finitely often. Monotonicity of the counts between dyadic times gives $\liminf_T N_j(T)/\log T\geq\beta$. Let $\beta\uparrow2/\Delta_j^2$ through a countable sequence and combine with (6):
$$
\frac{N_j(T)}{\log T}\longrightarrow\frac{2}{\Delta_j^2}\quad\text{almost surely}.\tag{8}
$$
For $\Theta=\mathbb R^K$, every such $v^{(j)}$ is feasible; summing the limits in (8) proves the unstructured assertion.

**Unimodal Constraint.** If $j$ is an immediate neighbor of $j^*$, raising $\mu_j$ to $\mu_{j^*}$ leaves a unimodal vector. Thus (8) applies to each existing immediate neighbor. Now let $|j-j^*|\geq2$, and define $\ell=j^*-1$ when $j<j^*$ and $\ell=j^*+1$ when $j>j^*$. Crucially, $\ell$ is adjacent to the optimum, not merely adjacent to $j$. Unimodality gives $\mu_j\leq\mu_\ell<\mu_{j^*}$; every $v\in\Theta_j$ satisfies $v_j\geq v_\ell\geq v_{j^*}$. Put $c=v_{j^*}$. If $c\leq\mu_\ell$, nonnegativity suffices; if $c>\mu_\ell$, both $v_j$ and $v_\ell$ are at least $c$, and $\mu_j\leq\mu_\ell$. Hence, pointwise,
$$
N_j(t)(v_j-\mu_j)^2+N_\ell(t)(v_\ell-\mu_\ell)^2
\geq[N_j(t)+N_\ell(t)](c-\mu_\ell)_+^2.
$$
Minimize this bound plus $N_{j^*}(t)(c-\mu_{j^*})^2$ over $c$. The one-sided two-coordinate quadratic calculation yields
$$
\bar\Lambda_t(j)\geq\frac{\Delta_\ell^2}{2}
\frac{[N_j(t)+N_\ell(t)]N_{j^*}(t)}{N_j(t)+N_\ell(t)+N_{j^*}(t)}.\tag{9}
$$
The denominator-zero case is read as zero. By (6), $N_j(t)=O(\log t)$; by (8), $N_\ell(t)/\log t\to2/\Delta_\ell^2$; and (5) makes $N_{j^*}(t)/(N_j(t)+N_\ell(t)+N_{j^*}(t))\to1$. For any $\rho>0$, (9) therefore exceeds $(1+\rho\Delta_\ell^2/2-o(1))\log t$ whenever $N_j(t)\geq\rho\log t$. Using (1) with a sufficiently small fixed $\varepsilon$ and then (2), we obtain some $\eta_\rho>0$ for which $Q_{t-1}(j)\leq t^{-(1+\eta_\rho)}$ eventually whenever $N_j(t-1)\geq\rho\log t$. The same conditional Borel–Cantelli threshold argument used for (6) yields $\limsup_T N_j(T)/\log T\leq\rho$. Let $\rho\downarrow0$ through positive rationals. Every non-neighbor count is $o(\log T)$, so the regret decomposition and the neighbor limits prove the unimodal assertion.
