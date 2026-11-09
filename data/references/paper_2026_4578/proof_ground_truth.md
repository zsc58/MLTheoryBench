# Reference Proof

## Contract and proof obligations

The bandit instance and common reward-noise law are fixed as the horizon varies. Write \(\sigma=\sigma_T\), \(L=\log(T/\sigma)\), and \(r=|S^*|\). All constants below are independent of the horizon and time; unless called universal, they may depend on the fixed instance and explicitly fixed slack parameters. We work at sufficiently large horizons. Then \(\sigma\to\infty\), \(L\to\infty\), \(L-2\log\log T\to\infty\), and \(\sigma L^2/T\to0\).

The theorem-critical obligations are: (1) valid concentration and suboptimal expected-count control; (2) full-bandit moment control for optimal empirical errors; (3) the winner-map and perturbation inequalities; (4) the calendar-time stopped Lyapunov closure; (5) two-sided suboptimal selection bounds with their correct prefactors and domains; (6) cutoff attainment and unconditional uniform-block coupling; and (7) the variance-scale geometric-sum law and both integer count brackets. Each is proved below. No paper-specific lemma is taken as an unexplained external result.

## 1. Concentration and expected suboptimal counts

Pre-generate each arm's reward stream, and let \(S_a(n)=\sum_{s=1}^n\varepsilon_{a,s}\). At any time with count \(n\), its empirical error is \(S_a(n)/n\). Thus fixed-count events can be bounded using the unconditionally generated stream, without conditioning its distribution on the adaptive count. The sub-Gaussian assumption gives
\[
 \Pr\{S_a(n)\ge nx\},\ \Pr\{S_a(n)\le-nx\}\le e^{-nx^2/2},\qquad x\ge0.
\]

We use the following standard time-uniform concentration statement from the supplied source: if \(X_s\) are conditionally mean-zero and satisfy \(\mathbb E(e^{\lambda X_s}\mid\mathcal H_{s-1})\le e^{\lambda^2/2}\), and \(I_s\in\{0,1\}\) are predictable, then, with probability at least \(1-\delta\), simultaneously for \(V_n=\sum_{s\le n}I_s\ge3\),
\[
 \left|\sum_{s\le n}I_sX_s\right|\le c\sqrt{V_n\{\log\log V_n+\log(1/\delta)\}}.
\]
Apply this separately in each pull-indexed reward stream with \(I_s=1\) and \(\delta=(\log T)^{-2}\). The hypotheses hold by independence and the sub-Gaussian moment bound. Control counts one and two by the fixed-count tails. Since \(K\) is fixed, for a sufficiently large fixed \(B\), the event
\[
 E_T=\left\{|S_a(n)|\le\sqrt{Bn\log\log T}\text{ for all }a\text{ and }1\le n\le T\right\}
\]
has probability tending to one. In particular it controls every adaptively observed empirical mean. We do not assert a fresh conditional concentration bound for the accumulated mean after an arbitrary stopping time.

Here are the normal-tail facts used below, with \(\phi\) and \(\Phi\) the standard normal density and distribution function:
\[
 \Phi(-x)=1-\Phi(x),\qquad
 \frac{x}{1+x^2}\phi(x)\le1-\Phi(x)\le\frac{\phi(x)}x\quad(x>0),
 \qquad1-\Phi(x)\le e^{-x^2/2}\quad(x\ge0).
\]
These are standard independent results, used only in their displayed domains.

Fix a suboptimal arm with gap \(d>0\), an optimal arm labeled 1, and a deterministic \(u\le T\). For \(u<K\), its count is at most one. Otherwise split its post-initialization pulls into: I, empirical mean exceeding \(\mu_a+d/3\); II, empirical mean at most this threshold but index exceeding \(\mu^*-d/3\); and III, the remaining pulls.

Each pre-pull count can occur at most once at a pull of that arm. Hence
\[
 I\le\sum_{n\ge1}e^{-nd^2/18}\le C/d^2.
\]
For II set \(b=\lfloor18\sigma d^{-2}\log(1+ud^2/\sigma)\rfloor\). Counts at most \(b\) contribute at most \(b\). At larger counts the conditional index-tail probability is at most \(e^{-nd^2/(18\sigma)}\le\sigma/(\sigma+ud^2)\). Summing this probability over calendar time gives
\[
 II\le b+\sigma/d^2.
\]

For III put \(Q_t=\Pr(\theta_{1,t+1}>\mu^*-d/3\mid\mathcal F_t)\). Conditional on all indices except that of arm 1, if arm \(a\) wins below the threshold, then the maximum competing index is below that threshold. The probability that arm 1 loses is at most \(1-Q_t\), whereas its probability of winning on this same configuration is at least \(Q_t\). Consequently
\[
 \Pr(\text{III at }t+1\mid\mathcal F_t)
 \le\frac{1-Q_t}{Q_t}\Pr(A_{t+1}=1\mid\mathcal F_t).
\]
At optimal-arm count \(n\), define
\[
 X_n=\sqrt{n/\sigma}\{S_1(n)/n+d/3\},\qquad R_n=\Phi(-X_n)/\Phi(X_n).
\]
Grouping the last bound by successive pulls of arm 1 gives \(III\le\sum_{n\ge1}\mathbb ER_n\). For \(z\ge0\), the fixed-count tail gives \(\Pr(( -X_n)_+>z)\le e^{-\sigma z^2/2}\). Mills' bound gives \(R_n^2\le C(1+(-X_n)_+^2)e^{(-X_n)_+^2}\), so tail integration yields \(\mathbb ER_n^2\le C\) for \(\sigma\ge4\), uniformly in \(n\). On \(S_1(n)/n\ge-d/12\), \(X_n\ge d\sqrt{n/\sigma}/4\), so \(R_n\le2e^{-nd^2/(32\sigma)}\). The complementary event has probability at most \(e^{-nd^2/288}\); Cauchy–Schwarz therefore gives
\[
 \mathbb ER_n\le2e^{-nd^2/(32\sigma)}+Ce^{-nd^2/576}.
\]
Summing proves, uniformly over deterministic \(u\le T\),
\[
 \mathbb EN_{a,u}\le1+C\frac{\sigma}{d^2}\left\{1+\log\left(1+\frac{ud^2}{\sigma}\right)\right\}. \tag{1}
\]
Let \(N_{\rm sub}(t)\) and \(N_{\rm opt}(t)\) denote the total suboptimal and optimal counts. The finite number of fixed gaps gives
\[
 \mathbb EN_{\rm sub}(T)=O(\sigma L),\qquad
 \Pr(\Omega_T^c)=O(1/L),\qquad
 \Omega_T=\{N_{\rm sub}(T)\le\sigma L^2\}.
 \tag{2}
\]
Empty suboptimal sums are zero. In particular \(N_{\rm opt}(T)/T\to1\) in probability.

## 2. Full-bandit moments of optimal empirical errors

We prove the moment estimate rather than infer it from the pathwise iterated-logarithm event. Put \(x_{i,t}=N_{i,t}/t\) and \(W_{i,t}=S_i(N_{i,t})/\sqrt{N_{i,t}}\) for optimal arms.

For any mean-zero 1-sub-Gaussian \(\xi\), the Gaussian integral identity and its moment-generating-function bound give
\[
 \mathbb E e^{s\xi+\lambda\xi^2}
 \le(1-2\lambda)^{-1/2}\exp\{s^2/[2(1-2\lambda)]\},\qquad0\le\lambda<1/2.
\]
Indeed, represent \(e^{\lambda\xi^2}\) as the expectation of \(e^{\sqrt{2\lambda}Z\xi}\) over an independent standard normal \(Z\), and then integrate the sub-Gaussian bound. Applied to \(W'=(\sqrt n\,w+\xi)/\sqrt{n+1}\), this shows that universal positive constants \(\kappa_0,\kappa_1,\kappa_2\), with \(\kappa_0\) sufficiently small, satisfy
\[
 \mathbb E e^{\kappa_0(W')^2}
 \le\left(1+\frac{\kappa_2}{n+1}\right)
 e^{\kappa_0w^2-\kappa_1w^2/(n+1)}. \tag{3}
\]
The next reward is independent of the selected action and past, so this inequality applies conditionally when the arm is pulled.

If arm \(i\) is not pulled, \(x_i e^{\kappa_0W_i^2}\) is multiplied by \(t/(t+1)\). If it is pulled, (3) bounds its conditional expectation by
\[
 \frac{n+1+\kappa_2}{t+1}e^{\kappa_0w^2-\kappa_1w^2/(n+1)}.
\]
Subtracting \(n e^{\kappa_0w^2}/(t+1)\), a positive difference requires
\((n+1+\kappa_2)e^{-\kappa_1w^2/(n+1)}>n\), which implies \(w^2\le C\). Its positive part is therefore at most \(C/(t+1)\). Taking expectations and iterating yields
\[
 \sup_{i\in S^*}\sup_{K\le t\le T}\mathbb E[x_{i,t}e^{\kappa_0W_{i,t}^2}]\le C. \tag{4}
\]
Initialization has the required finite moment by the same Gaussian integral bound.

For each suboptimal arm \(j\), put
\[
 D_{j,t}=\bigl(S_j(N_{j,t})/\sqrt{N_{j,t}}-\Delta_j\sqrt{N_{j,t}}\bigr)_+.
\]
A union bound over the pre-generated counts gives
\[
 \Pr\left(\sup_{t\le T}D_{j,t}>z\right)
 \le\sum_{n\ge1}e^{-(\Delta_j\sqrt n+z)^2/2}
 \le C_j e^{-z^2/2}.
\]
Thus for a fixed sufficiently small \(\lambda_*>0\), \(\sup_{j,t}\mathbb E e^{\lambda_*D_{j,t}^2}<\infty\). With no suboptimal arms, take \(\lambda_*=1\) and omit these terms.

Set \(\gamma=\kappa_0/(4r)\). For sufficiently large \(\sigma\), normal-tail lower bounds give, for every optimal arm,
\[
 p_{i,t}:=\Pr(A_{t+1}=i\mid\mathcal F_t)
 \ge c\exp\left[-\gamma\left(\sum_{\ell\in S^*}W_{\ell,t}^2+\sum_{j\notin S^*}D_{j,t}^2\right)\right]. \tag{5}
\]
To see this, shift \(\mu^*\) to zero. Require \(W_i+\sqrt\sigma Z_i\ge1\), require \(W_\ell+\sqrt\sigma Z_\ell\le0\) for other optimal arms, and require \(\sqrt{N_j}(\widehat\mu_j-\mu^*)+\sqrt\sigma Z_j\le0\) for suboptimal arms. This event makes arm \(i\) win. Each probability is bounded below by the corresponding factor \(c e^{-\gamma W^2}\) or \(c e^{-\gamma D^2}\): for negative thresholds the probability is at least one half, and for positive thresholds Mills' bound applies, with its polynomial factor absorbed by the fixed slack between \(\gamma\) and \(1/(2\sigma)\). Multiply using conditional independence.

Choose \(0<\alpha\le1\) so that \(2\alpha\gamma(K-r)<\lambda_*\) when there are suboptimal arms. The two possible count updates give
\[
 \mathbb E[x_{i,t+1}^{-\alpha}\mid\mathcal F_t]
 \le x_{i,t}^{-\alpha}+t^{-1}\{Cx_{i,t}^{-\alpha}-cx_{i,t}^{-\alpha-1}p_{i,t}\}.
\]
Writing \(H_t=\sum_{\ell\in S^*}W_{\ell,t}^2+\sum_{j\notin S^*}D_{j,t}^2\), (5) and the elementary inequality \(Cz^\alpha-cz^{\alpha+1}\le C'-c'z^\alpha\) imply
\[
 \mathbb E[x_{i,t+1}^{-\alpha}\mid\mathcal F_t]
 \le(1-c/t)x_{i,t}^{-\alpha}+(C/t)e^{\alpha\gamma H_t}. \tag{6}
\]
Let \(M_t=\max_{i\in S^*}\mathbb E[1+x_{i,t}^{-\alpha}]\). Cauchy–Schwarz separates optimal from suboptimal terms in \(\mathbb Ee^{\alpha\gamma H_t}\). The suboptimal factor is bounded by Hölder and the choice of \(\alpha\). For the optimal factor, set \(b=2r\alpha\gamma=\alpha\kappa_0/2\). By (4) and Hölder,
\[
 \mathbb Ee^{bW_{i,t}^2}
 =\mathbb E[(x_{i,t}e^{\kappa_0W_{i,t}^2})^{b/\kappa_0}x_{i,t}^{-b/\kappa_0}]
 \le C M_t^{1-\alpha/2},
\]
because \(b/(\kappa_0-b)=\alpha/(2-\alpha)\le\alpha\). Hölder over the \(r\) optimal arms, followed by the square root from Cauchy–Schwarz, gives
\[
 \mathbb Ee^{\alpha\gamma H_t}\le C M_t^{(2-\alpha)/4}.
\]
Consequently (6) gives
\[
 M_{t+1}\le(1-c/t)M_t+(C/t)M_t^q+C/t,\qquad q=(2-\alpha)/4<1.
\]
Decrease \(c\) to be at most one. Choose a constant \(M\) above the initialization value with \(CM^q+C\le cM\). The right-hand side is increasing in \(M_t\), so induction gives \(M_t\le M\) for all relevant times.

Finally choose \(0<\kappa<\kappa_0\) with \(\kappa/(\kappa_0-\kappa)\le\alpha\). Applying Hölder to (4) and the inverse-moment bound proves
\[
 \sup_{i\in S^*,\ K\le t\le T}\mathbb Ee^{\kappa W_{i,t}^2}\le C,
 \qquad \sup_{K\le t\le T}\sum_{i\in S^*}\mathbb E|W_{i,t}|\le C. \tag{7}
\]
This also covers the equal-means process, where the suboptimal sums are empty.

## 3. Winner map and perturbations

For a positive probability vector \(x\) of length \(r\ge2\), define \(g_i(x)=\Pr(Z_i/\sqrt{x_i}=\max_jZ_j/\sqrt{x_j})\). All encountered vectors are positive because of initialization. For scales \(s_i=x_i^{-1/2}\), write
\[
 \Gamma_i(s)=\int_{\mathbb R}\phi(z)\prod_{j\ne i}\Phi(s_i z/s_j)\,dz.
\]
Differentiation is justified locally in the positive scale domain by Gaussian integrable envelopes. Pairing \(z\) and \(-z\), each term of the own-scale derivative is a positive weight times
\[
 \prod_{q\ne i,j}\Phi(s_i z/s_q)-\prod_{q\ne i,j}\Phi(-s_i z/s_q),\qquad z>0.
\]
For \(r\ge3\) this is strictly positive. The derivative in a competitor scale has the opposite sign by the same pairing. Swapping two scales and using exchangeability therefore shows \(x_i>x_j\Rightarrow g_i(x)<g_j(x)\). For \(r=2\), symmetry of a centered Gaussian difference gives \(g_1=g_2=1/2\); there is no strict monotonicity.

Using the opposite ordering and \(\sum_i x_i=\sum_i g_i=1\),
\[
 r\sum_i x_i g_i-1=\sum_{i<j}(x_i-x_j)(g_i-g_j)\le0.
\]
Thus, with \(V(x)=\sum_i(x_i-1/r)^2\),
\[
 \sum_i x_i g_i(x)-\sum_i x_i^2\le-V(x). \tag{8}
\]
This supplies contraction even for \(r=2\).

If \(p_i(x,\rho)\) is the winner probability for \((Z_i+\rho_i)/\sqrt{x_i}\), couple perturbed and unperturbed winners using the same normals. A changed winner requires a pairwise ordering change. The difference for pair \(i,j\) has variance \((x_i+x_j)/(x_ix_j)\), so its bounded Gaussian density gives
\[
 \Pr(\text{pair changes})\le C\frac{|\rho_i\sqrt{x_j}-\rho_j\sqrt{x_i}|}{\sqrt{x_i+x_j}}
 \le C(|\rho_i|+|\rho_j|).
\]
A union bound and the coupling inequality yield
\[
 \sum_i x_i|p_i(x,\rho)-g_i(x)|\le C_r\sum_i|\rho_i|. \tag{9}
\]
For competition among optimal arms, \(\rho_i=W_{i,t}/\sqrt\sigma\). By (7), the expectation of (9) is \(O(\sigma^{-1/2})\). No assumption that \(\sigma\) dominates \(\log\log T\) is used.

## 4. Optimal allocation in calendar time

If \(r=1\), (2) already proves the optimal-arm conclusion. Suppose \(r\ge2\). Define \(y_{i,t}=N_{i,t}/N_{\rm opt}(t)\) and \(V_t^*=\sum_{i\in S^*}(y_{i,t}-1/r)^2\). Let \(\pi_{i,t}\) be the winner probability among optimal arms only, \(p_{i,t}\) the global selection probability, and \(q_t=\Pr(A_{t+1}\notin S^*\mid\mathcal F_t)\). Then \(0\le p_{i,t}\le\pi_{i,t}\) and \(\sum_i(\pi_{i,t}-p_{i,t})=q_t\).

On a suboptimal pull \(y\) is unchanged. On an optimal pull of arm \(i\), its increment is \((e_i-y)/(N_{\rm opt}+1)\). Expanding the square, using (8), (9), and \(\|e_i-y\|^2\le2\), gives
\[
 \mathbb E[V_{t+1}^*\mid\mathcal F_t]
 \le V_t^*-\frac{2V_t^*}{N_{\rm opt}(t)+1}
 +\frac{C\sum_{i\in S^*}|W_{i,t}|}{(N_{\rm opt}(t)+1)\sqrt\sigma}
 +\frac{Cq_t}{N_{\rm opt}(t)+1}+\frac{C}{(N_{\rm opt}(t)+1)^2}. \tag{10}
\]
In detail, replacing \(p\) by \(\pi\) in the first-order term changes \(\sum y_i p_i-(\sum p_i)\sum y_i^2\) by at most \(2q_t\), since both \(y_i\) and \(\sum y_i^2\) lie in \([0,1]\).

Set \(t_0=\lceil2\sigma L^2\rceil\) and \(\zeta=\inf\{t\ge K:N_{\rm sub}(t)>\sigma L^2\}\). By (2), \(\Pr(\zeta\le T)=O(1/L)\). On \(\{\zeta>t\}\), for \(t\ge t_0\), \(N_{\rm opt}(t)\ge t/2\). Since \(\{\zeta>t+1\}\subseteq\{\zeta>t\}\) and \(V^*\ge0\), (7) and (10) imply, for \(v_t=\mathbb E[V_t^*1_{\{\zeta>t\}}]\),
\[
 v_{t+1}\le(1-2/(t+1))v_t+C/(t\sqrt\sigma)+(C/t)\mathbb Eq_t+C/t^2.
\]
Multiply by \(t+1\), bound \((t-1)v_t\le tv_t\), and telescope. Since \(0\le V^*\le1\),
\[
 v_T\le t_0/T+C/\sqrt\sigma+C\mathbb EN_{\rm sub}(T)/T+C\log T/T\longrightarrow0.
\]
Together with the stopping probability, this proves \(V_T^*\to0\) in probability. Multiplication by \(N_{\rm opt}(T)/T\to1\) gives \(N_{i,T}/T\to1/r\) for every optimal arm. This includes the all-optimal case.

## 5. Sharp selection bounds for a suboptimal arm

Fix a suboptimal arm \(a\), write \(d=\Delta_a\), and fix \(0<\eta<d/8\). Put
\[
 \alpha_+=(d-3\eta)^2/2,\qquad \alpha_-=(d+3\eta)^2/2,
\]
\[
 R_T=C\left[1+\frac{\log\log T}{\sigma}+\log\left(1+\frac{\log\log T}{\sigma}\right)\right].
\]
Choose the fixed constant \(C\) large enough for the competitor bound below. Then \(R_T=o(L)\): if \(\sigma\le\sqrt{\log\log T}\), \(L\sim\log T\); otherwise \(R_T=O(\sqrt{\log\log T})\), whereas \(L-2\log\log T\to\infty\).

Let \(h_T=\sqrt L+R_T+\log L\), and define
\[
 k_0=\max\left\{\left\lceil4B\log\log T/\eta^2\right\rceil,
 \left\lceil\frac{\sigma h_T}{4(d+3\eta)^2}\right\rceil\right\}.
\]
Then \(k_0/\sigma\to\infty\), \(k_0/\sigma=O(h_T)=o(L)\), and \(k_0=o(\sigma L)\). On \(E_T\), counts at least \(k_0\) give empirical error at most \(\eta/2\).

On \(E_T\cap\Omega_T\), at every \(t\ge t_0\) some optimal arm \(i\) has \(N_{i,t}\ge t/(2r)\ge\sigma L^2/r\) and \(\widehat\mu_{i,t}\ge\mu^*-\eta\). Consequently
\[
 \Pr(\max_{i\in S^*}\theta_{i,t+1}<\mu^*-2\eta\mid\mathcal F_t)
 \le\Phi\bigl((\mu^*-2\eta-\widehat\mu_{i,t})\sqrt{N_{i,t}/\sigma}\bigr)
 \le e^{-c\eta^2L^2}. \tag{11}
\]
The middle Gaussian tail is bounded by, not generally equal to, \(\Phi(-\eta\sqrt{N_{i,t}/\sigma})\).

If \(k=N_{a,t}\ge k_0\), selection of arm \(a\) requires either its index to exceed \(\mu^*-2\eta\) or the exceptional event in (11). Mills' upper bound therefore gives, for
\(k\le4\sigma L/(d-3\eta)^2\),
\[
 \Pr(A_{t+1}=a\mid\mathcal F_t)\le p^+_{k,T}:=C\sqrt{\sigma/k}\,e^{-\alpha_+k/\sigma}. \tag{12}
\]
Indeed the displayed main term is at least a constant times \(L^{-1/2}e^{-2L}\) throughout this window, so it absorbs the error in (11).

For a lower bound require \(\theta_a\ge\mu^*+2\eta\) and \(\theta_b\le\mu^*+\eta\) for every \(b\ne a\). On \(E_T\),
\[
 \frac{\mu^*+\eta-\widehat\mu_{b,t}}{\sqrt{\sigma/N_{b,t}}}
 \ge-\sqrt{B\log\log T/\sigma}.
\]
Mills' lower bound, with the bounded-argument case handled by positivity of \(\Phi(-1)\), shows that the product of all competitor probabilities is at least \(e^{-R_T}\). The selected arm's overshoot probability is at least \(c\sqrt{\sigma/k}e^{-\alpha_-k/\sigma}\). Thus
\[
 \Pr(A_{t+1}=a\mid\mathcal F_t)\ge p^-_{k,T}:=c e^{-R_T}\sqrt{\sigma/k}\,e^{-\alpha_-k/\sigma}. \tag{13}
\]
Importantly, (13) holds on \(E_T\) at every initialized time \(t\ge K\) when \(k\ge k_0\), without \(\Omega_T\) or \(t\ge t_0\). This follows directly from its all-competitor event and resolves waiting blocks that straddle \(t_0\). The parameters in (12) and (13) lie in \((0,1)\) on the relevant window for all sufficiently large horizons.

For \(k<k_0\), on \(E_T\),
\[
 \frac{\mu^*+2\eta-\widehat\mu_{a,t}}{\sqrt{\sigma/k}}
 \le(d+2\eta)\sqrt{k/\sigma}+\sqrt{B\log\log T/\sigma}
 \le(d+3\eta)\sqrt{k_0/\sigma}.
\]
The same competitor event therefore yields a common lower bound \(p^-_{k_0,T}\) while the count is below \(k_0\).

## 6. Cutoff attainment and geometric coupling

Let \(T_a(k)\) denote the time of the \(k\)-th pull, with value infinity if it is not reached by the horizon. Construct independent arrays of uniforms \(U_{k,s}\), one row for each pre-pull count \(k\), before restricting to any good event. During a waiting block realize the indicator of selecting \(a\) by comparison of the next unused uniform with its actual history-dependent conditional selection probability. Conditional on this indicator, generate the selected competitor using its residual conditional law, and generate the next reward independently. This reproduces the observed-history law of the algorithm.

For any deterministic probability \(p_k\), the first uniform in row \(k\) at most \(p_k\) defines a positive-integer geometric variable. These variables are independent over \(k\) unconditionally; no independence conditional on \(E_T\) or \(\Omega_T\) is claimed. Pathwise comparisons of the thresholds give comparisons of first-success times, truncated at the remaining horizon plus one.

The bound below \(k_0\) compares its attainment time, on \(E_T\), with initialization plus a sum of at most \(k_0\) independent geometric variables of parameter \(p^-_{k_0,T}\). Its expectation is bounded by
\[
 Ck_0\sqrt{k_0/\sigma}\exp\{R_T+\alpha_-k_0/\sigma\}
 =\sigma e^{o(L)}=o(T).
\]
Markov's inequality and \(\Pr(E_T^c)\to0\) prove
\[
 T_a(k_0)/T\xrightarrow{p}0. \tag{14}
\]
For counts \(k\ge k_0\), let \(G_k^-\) and \(G_k^+\) be the geometric variables formed from the same row using (13) and (12). On \(E_T\), (13) bounds every waiting time above by \(G_k^-\), with horizon truncation, including blocks before or straddling \(t_0\). On \(E_T\cap\Omega_T\), (12) bounds a waiting time below by \(G_k^+\) whenever that block begins after \(t_0\) and its count is in the stated window. These comparisons are used only where their time and count hypotheses hold.

## 7. Geometric sums and terminal brackets

We first prove the required log law. Suppose independent positive-integer geometric variables \(G_{k,T}\), for \(m_T\le k\le n_T\), satisfy
\[
 n_T=\Theta(\sigma L),\qquad m_T=o(n_T),\qquad m_T/\sigma\to\infty,
\]
\[
 -\log p_{k,T}=\alpha k/\sigma+O(1+\log(k/\sigma)+R_T),\qquad \alpha>0,
\]
with \(R_T=o(L)\) and a uniform error bound. This error is uniformly \(o(L)\). Since \(\mathbb EG=1/p\), summing a geometric progression gives
\[
 \mathbb E\sum_{k=m_T}^{n_T}G_{k,T}\le C\sigma\exp\{\alpha n_T/\sigma+o(L)\}.
\]
Markov's inequality proves the upper logarithmic bound with an arbitrary positive multiple of \(L\) as slack.

For the lower bound fix \(\delta>0\). If \(\log\sigma\le\delta L/2\), then \(\Pr(G_{n_T,T}\le x)\le xp_{n_T,T}\), with \(x=e^{\alpha n_T/\sigma-\delta L/2}\), tends to zero. This last variable alone is at least \(e^{\log\sigma+\alpha n_T/\sigma-\delta L}\) with probability tending to one. If \(\log\sigma>\delta L/2\), consider the last \(\lfloor\sigma\rfloor\) indices, which lie in the summation window for large \(T\). Their sum has expectation at least \(\sigma e^{\alpha n_T/\sigma-o(L)}\). Independence and \(\operatorname{Var}(G)\le p^{-2}\) bound its relative variance by \(e^{o(L)}/\sigma\to0\). Chebyshev's inequality gives the same lower logarithmic bound. Since \(\delta\) is arbitrary,
\[
 \log\left(\sum_{k=m_T}^{n_T}G_{k,T}\right)
 =\log\sigma+\alpha n_T/\sigma+o_p(L). \tag{15}
\]
In particular the \(\log\sigma\) term cannot be dropped in the permitted inflation regime.

Fix \(0<\delta<1\) and define
\[
 n^- =\left\lfloor(1-\delta)\sigma L/\alpha_-\right\rfloor,
 \qquad n^+=\left\lceil(1+\delta)\sigma L/\alpha_+\right\rceil.
\]
Both exceed \(k_0\); the upper one is within the count window for (12) for large \(T\). Apply (15) to \(\sum_{k=k_0}^{n^- -1}G_k^-\). Its log-probability error is \(R_T+\tfrac12\log(k/\sigma)+O(1)=o(L)\), and all the other hypotheses were checked above. Thus this sum divided by \(T=\sigma e^L\) tends to zero in probability. Together with (14) and the lower-threshold coupling, this implies \(T_a(n^-)=o_p(T)\): if the dominating sum fits before the horizon, the successive truncated comparisons force every required pull to occur. Therefore
\[
 \Pr(N_{a,T}\ge n^-)\longrightarrow1. \tag{16}
\]

For the upper bracket put \(k_1=\max\{k_0,\lceil\sigma h_T\rceil\}\). By (1),
\(\mathbb EN_{a,t_0}=O(\sigma\log L)\). Since \(h_T\ge\sqrt L\), Markov's inequality gives \(\Pr(N_{a,t_0}\ge k_1)\to0\). Also \(k_1=o(\sigma L)\) and \(k_1/\sigma\to\infty\). On \(E_T\cap\Omega_T\cap\{N_{a,t_0}<k_1\}\), reaching \(n^+\) by \(T\) requires completing every waiting block from \(k_1\) through \(n^+-1\) after \(t_0\). The lower waiting-time comparisons then force
\[
 T\ge\sum_{k=k_1}^{n^+-1}G_k^+.
\]
Applying (15) with rate \(\alpha_+\) and no competitor-loss term shows that this last sum divided by \(T\) tends to infinity in probability. All excluded events have probability tending to zero, so
\[
 \Pr(N_{a,T}<n^+)\longrightarrow1. \tag{17}
\]
Retaining the floors and ceilings, (16)–(17) imply normalized brackets with endpoints \((1-\delta)/\alpha_-+O((\sigma L)^{-1})\) and \((1+\delta)/\alpha_++O((\sigma L)^{-1})\). Let \(\delta\downarrow0\) and then \(\eta\downarrow0\). This proves
\[
 \frac{N_{a,T}}{\sigma_T\log(T/\sigma_T)}\xrightarrow{p}\frac{2}{\Delta_a^2}.
\]
A finite union bound gives the statement for every suboptimal arm. If there are none, this part is vacuous. The optimal-arm limit was proved in Section 4. Finally \(T/r\to\infty\) and \(2\sigma_T\log(T/\sigma_T)/\Delta_a^2\to\infty\), so the displayed deterministic normalizers establish stability.
