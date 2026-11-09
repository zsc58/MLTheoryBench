# Problem

## Setup

Let \(\mathcal S\) and \(\mathcal A\) be nonempty finite state and action sets with cardinalities \(S\) and \(A\), and let \(H,K\) be positive integers. For each stage \(h=1,\ldots,H\), the reward \(r_h(s,a)\) is known and belongs to \([0,1]\), while the transition kernel \(P_h(\cdot\mid s,a)\) is unknown. Rewards and transition kernels are fixed and shared across episodes.

A context \(c\) specifies an initial-state distribution \(\mu_c\) and a nonempty admissible action set \(\mathcal A_h(s;c)\subseteq\mathcal A\) at every stage-state pair. The context space \(\mathcal C\) consists of such descriptors, with the topology inherited from the probability simplex for \(\mu_c\) and the discrete topology for the finitely many action-set coordinates. Let \(\rho\) be a Borel probability distribution on \(\mathcal C\), and let \(\operatorname{supp}(\rho)\) denote its support in this space.

An admissible policy in context \(c\) is a sequence of state-to-action-distribution maps \(\pi_h\) supported on \(\mathcal A_h(s;c)\). Define \(V_{H+1}^{\pi,c}=V_{H+1}^{*,c}=0\). For \(h\le H\), \(V_h^{\pi,c}(s)\) is the expected sum of rewards from stages \(h\) through \(H\) when the process is started at state \(s\) at stage \(h\) and follows \(\pi\). For an admissible action,

\[
Q_h^{\pi,c}(s,a)=r_h(s,a)+P_h(\cdot\mid s,a)V_{h+1}^{\pi,c}.
\]

Let \(V_h^{*,c}\) and \(Q_h^{*,c}\) be the maxima of these quantities over admissible policies, and write \(V_h^{\pi,c}(\mu)=\sum_s\mu(s)V_h^{\pi,c}(s)\), with the same convention for optimal values. For a probability distribution \(q\) and vector \(v\), write \(qv=\sum_s q(s)v(s)\) and \(\operatorname{Var}(q,v)=q[v^2]-(qv)^2\).

At the beginning of episode \(k\), a context \(c_k\) is drawn from \(\rho\), independently of previous episodes and of the randomness used for initial states and transitions, and its entire descriptor is revealed to the learner. The initial state is then drawn from \(\mu_{c_k}\). Conditional on the current history, state, and action, the next state has law \(P_h(\cdot\mid s,a)\).

For a confidence parameter \(\delta\in(0,1)\), the learner runs the following planner. Set \(L=\log(SAHK/\delta)\). For each triple \((h,s,a)\), initialize a global visit count, an accumulating transition histogram, and a cached sample size to zero; initialize its cached kernel to any fixed probability distribution on \(\mathcal S\). Whenever its global visit count becomes \(1,2,4,8,\ldots\), replace its cached sample size by the number of samples in the just-completed batch, replace its cached kernel by that batch's empirical distribution, and reset the accumulating histogram. Only samples observed by the learner are used.

Write \(N_h^k(s,a)\) and \(\widehat P_h^k(\cdot\mid s,a)\) for these cached quantities before episode \(k\). After observing \(c_k\), set \(\widetilde V_{H+1}^k=0\) and compute backward for \(h=H,\ldots,1\):

\[
b_h^k(s,a)=\frac{460}{9}\sqrt{\frac{\operatorname{Var}(\widehat P_h^k(\cdot\mid s,a),\widetilde V_{h+1}^k)L}{\max\{N_h^k(s,a),1\}}}+\frac{544}{9}\frac{HL}{\max\{N_h^k(s,a),1\}},
\]

\[
\widetilde Q_h^k(s,a)=\min\{r_h(s,a)+\widehat P_h^k(\cdot\mid s,a)\widetilde V_{h+1}^k+b_h^k(s,a),H\},
\qquad
\widetilde V_h^k(s)=\max_{a\in\mathcal A_h(s;c_k)}\widetilde Q_h^k(s,a).
\]

The episode policy \(\pi_k\) chooses an admissible maximizing action at every stage-state pair, with a fixed deterministic rule for ties. This policy and its planned values are held fixed throughout the episode; newly observed transitions update the batch statistics for subsequent episodes.

The cumulative regret is

\[
R_K=\sum_{k=1}^K\bigl(V_1^{*,c_k}(\mu_{c_k})-V_1^{\pi_k,c_k}(\mu_{c_k})\bigr).
\]

For an admissible action define its contextual gap by

\[
\gamma_h^c(s,a)=V_h^{*,c}(s)-Q_h^{*,c}(s,a),
\]

and set it to \(+\infty\) when the action is inadmissible. Let

\[
\mathcal C_{h,s,a}^+=\{c\in\operatorname{supp}(\rho):0<\gamma_h^c(s,a)<+\infty\},
\qquad
Z_{\mathrm{pos}}=\{(h,s,a):\rho(\mathcal C_{h,s,a}^+)>0\}.
\]

For \(p\in[0,1)\) and \((h,s,a)\in Z_{\mathrm{pos}}\), define

\[
\gamma_h^p(s,a)=\sup\{x\in\mathbb R:\Pr(\gamma_h^c(s,a)<x\mid c\in\mathcal C_{h,s,a}^+)\le p\}.
\]

For triples outside \(Z_{\mathrm{pos}}\), set \(\gamma_h^p(s,a)=+\infty\). If \(Z_{\mathrm{pos}}\ne\varnothing\), define

\[
\gamma_{\min}^p=\min_{(h,s,a)\in Z_{\mathrm{pos}}}\gamma_h^p(s,a);
\]

otherwise set \(\gamma_{\min}^p=0\). Define

\[
Z_{\mathrm{trim}}^p=\{(h,s,a):\text{some }c\in\operatorname{supp}(\rho)\text{ satisfies }0\le\gamma_h^c(s,a)<\gamma_h^p(s,a)\}.
\]

For every context and admissible triple, let

\[
\operatorname{Var}_h^{*,c}(s,a)=\operatorname{Var}(P_h(\cdot\mid s,a),V_{h+1}^{*,c}).
\]

In the following definition, a trajectory under \((\pi,c)\) starts with \(s_1\sim\mu_c\). Define

\[
\Sigma_\star=\sup_{\substack{c\in\mathcal C,\ \pi\text{ admissible},\ h\in\{1,\ldots,H\},\ s\in\mathcal S\\\Pr^{\pi,c}(s_h=s)>0}}
\mathbb E^{\pi,c}\!\left[\sum_{t=1}^H\operatorname{Var}_t^{*,c}(s_t,a_t)\ \middle|\ s_h=s\right],
\qquad W=\min\{H^2,\Sigma_\star\}.
\]

Finally set \(\Lambda=200\log(SAHK/\delta)\) and \(\ell(x)=\log(e\max\{1,x\})\).

## Task

Prove that there is a universal constant \(C\) such that, for every \(\delta\in(0,1)\), with probability at least \(1-\delta\),

\[
R_K\le C\inf_{\substack{0\le p<1\\\gamma_{\min}^p>0}}\Lambda\left[
\sum_{(h,s,a)\in Z_{\mathrm{pos}}}\frac{W}{\gamma_h^p(s,a)}
+\frac{|Z_{\mathrm{trim}}^p|W\ell(H)}{\gamma_{\min}^p}
+(pK+1)SAH\gamma_{\min}^p
+S^2AH^4\ell\!\left(\frac{SAH\Lambda}{\gamma_{\min}^p}\right)
+SAH^2\right].
\]

The trimming level \(p\) may depend on the fixed MDP and \(\rho\), but not on sampled contexts, initial states, transitions, rewards, or the learner's trajectory. If no \(p\) satisfies \(\gamma_{\min}^p>0\), including when \(Z_{\mathrm{pos}}\) is empty, interpret the infimum as \(+\infty\).
