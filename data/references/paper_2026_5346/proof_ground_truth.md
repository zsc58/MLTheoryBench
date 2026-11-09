# Reference Proof

## Proof Structure

First, each threshold product is shown to be a nonnegative supermartingale until just before that threshold first becomes safe. Ville's inequality and the epoch-threshold allocation rule out every premature certificate simultaneously. Frontier monotonicity then transfers certification safety to next-round deployment.

Second, a conditional Hoeffding argument constructs an exponential supermartingale for drift-adjusted excess losses on predictably selected safe rounds. This process is constructed under the original probability law, before intersecting with any good event. Dyadic stitching over its random action clock gives the required time-uniform boundary. On the no-false-certificate event, this clock is the actual action count.

## Standard Independent Results Used

We use the following two standard results, with their hypotheses verified below.

1. **Ville's inequality.** If a nonnegative adapted supermartingale starts at one, then for every \(\varepsilon\in(0,1)\), the probability that it ever reaches \(1/\varepsilon\) is at most \(\varepsilon\).
2. **Conditional Hoeffding's lemma.** Under a conditional probability law, if a random variable \(W\) lies in an interval of length one, then
\[
\mathbb E\left[\exp\{\lambda(W-\mathbb E[W\mid\mathcal H])\}\mid\mathcal H\right]\le e^{\lambda^2/8}.
\]
In particular, for \(\lambda\ge0\), a nonpositive conditional mean implies \(\mathbb E[e^{\lambda W}\mid\mathcal H]\le e^{\lambda^2/8}\). The conditioning can include an action event of positive conditional probability.

These are the results indexed by theory_015 and theory_016. No specialized external or unproved paper-specific result is used as a black box.

## Complete Proof

### 1. Conditional safety and predictable stopping

For a fixed threshold, put
\[
p_t(q)=\mathbb E[A_t(q)\mid\mathcal F_{t-1}],\qquad
\mu_t(q)=\mathbb E[Z_t(q)\mid\mathcal F_{t-1}].
\]
When \(p_t(q)>0\), define
\[
r_t(q)=\frac{\mathbb E[A_t(q)(1-V_t)\mid\mathcal F_{t-1}]}{p_t(q)}.
\]
Then \(\mu_t(q)=p_t(q)(r_t(q)-\alpha)\). When \(p_t(q)=0\), boundedness gives \(\mu_t(q)=0\).

The safe thresholds form an initial segment. Indeed, suppose \(q\le q'\) and \(q'\) is safe. If \(p_t(q)=0\), then \(q\) is safe immediately. Otherwise nestedness gives \(p_t(q')>0\), and monotone conditional failure rates give
\[
r_t(q)\le r_t(q')\le\alpha.
\]
The abstention symbol is always safe. Thus \(q\le q_t^\star\) implies that \(q\) is safe, including zero-action-probability cases.

Choose versions of the conditional expectations throughout. Since the grid is finite, \(q_t^\star\) is \(\mathcal F_{t-1}\)-measurable. The controller's one-round delay makes \(q_t\) predictable as well. All almost-sure statements can be imposed simultaneously over the countably many rounds and the finite grid.

Fix an epoch \(I_j\) and threshold \(q\), and define
\[
\sigma_{j,q}=\inf\{t\in I_j:q\le q_t^\star\},
\]
with \(\inf\varnothing=\infty\). For \(s\in I_j\), the indicator \(\mathbf1\{s<\sigma_{j,q}\}\) is \(\mathcal F_{s-1}\)-measurable. Define the frozen product
\[
\widetilde E_{j,t}(q)=\prod_{s=\tau_j}^{t}
\left(1-\mathbf1\{s<\sigma_{j,q}\}\lambda_{j,s}(q)Z_s(q)\right).
\]
This is \(E_{j,t\wedge(\sigma_{j,q}-1)}(q)\), with the initial value convention from the task. It remains equal to one if the threshold is already safe at the start of the epoch.

On \(\{s<\sigma_{j,q}\}\), the threshold is unsafe, so \(\mu_s(q)>0\), and in particular \(\mu_s(q)\ge0\). Consequently the conditional mean of each factor of \(\widetilde E\) is at most one. Every factor is nonnegative because
\[
Z_s(q)\in\{-\alpha,0,1-\alpha\},\qquad
0\le\lambda_{j,s}(q)\le(1-\alpha)^{-1}.
\]
The factors are also at most \((1-\alpha)^{-1}\), so finite-time products are integrable. Therefore \(\widetilde E\) is an adapted nonnegative supermartingale starting at one. A finite epoch can be extended by freezing the process at its last value; before the epoch it can be set equal to one.

### 2. Simultaneous certification and deployment safety

Ville's inequality yields
\[
\mathbb P\left(\exists t\in I_j:\ t<\sigma_{j,q},\ E_{j,t}(q)\ge\delta_{j,q}^{-1}\right)\le\delta_{j,q}.
\]
The total allocation over all deployed epochs and thresholds is at most
\[
\sum_{j\ge1}\sum_{q\in\mathcal Q}\delta_{j,q}
=\sum_{j\ge1}\frac{6\delta}{\pi^2j^2}=\delta.
\]
Hence there is an event \(G\), with \(\mathbb P(G)\ge1-\delta\), on which no threshold is certified before first becoming safe in its epoch.

Consider a noninitial round \(t\in I_j\). If \(q_t\ne\bot\), then \(q_t\) was certified at \(t-1\) in the same epoch. On \(G\), its first safe time satisfies \(\sigma_{j,q_t}\le t-1\). Within-epoch frontier monotonicity gives \(q_t\le q_t^\star\). If \(q_t=\bot\), safety is immediate. Every epoch-initial round abstains by definition. Thus
\[
G\subseteq\{q_t\le q_t^\star\text{ for every }t\}.
\tag{1}
\]
This argument handles the adaptively selected maximum certified threshold, not just each fixed threshold separately. It does not require the unstopped threshold product to remain a supermartingale after the threshold becomes safe.

### 3. An unconditional safe-round exponential supermartingale

Define
\[
J_t=\mathbf1\{q_t\le q_t^\star\},\qquad
B_t=J_tA_t,\qquad
D_t=J_t\bigl(Z_t(q_t)-\nu_{j(t)}A_t\bigr),
\]
\[
W_T=\sum_{t\le T}D_t,\qquad K_T=\sum_{t\le T}B_t.
\]
The indicator \(J_t\) is predictable; \(A_t\) and \(B_t\) need not be predictable. The safe-round drift assumption and predictability of \(J_t\) give
\[
\mathbb E[D_t\mid\mathcal F_{t-1}]
=J_t\left(\mathbb E[Z_t(q_t)\mid\mathcal F_{t-1}]
-\nu_{j(t)}\mathbb E[A_t\mid\mathcal F_{t-1}]\right)\le0.
\tag{2}
\]

Let \(p_t=\mathbb P(B_t=1\mid\mathcal F_{t-1})\). On \(B_t=0\), both \(D_t\) and \(B_t\) vanish. On \(B_t=1\),
\[
D_t=(1-V_t)-\alpha-\nu_{j(t)}.
\]
When \(p_t>0\), equation (2) implies that this variable has nonpositive mean conditional on \(\mathcal F_{t-1}\) and \(B_t=1\). Under that conditional law it lies in
\[
[-\alpha-\nu_{j(t)},\ 1-\alpha-\nu_{j(t)}],
\]
an interval of length one. Conditional Hoeffding's lemma therefore gives, for every \(\lambda\ge0\),
\[
\mathbb E\left[e^{\lambda D_t-\lambda^2/8}\mid\mathcal F_{t-1},B_t=1\right]\le1.
\]
Combining the two action branches yields
\[
\mathbb E\left[e^{\lambda D_t-\lambda^2B_t/8}\mid\mathcal F_{t-1}\right]
=(1-p_t)+p_t\mathbb E\left[e^{\lambda D_t-\lambda^2/8}\mid\mathcal F_{t-1},B_t=1\right]\le1.
\tag{3}
\]
When \(p_t=0\), the left side is one, so no conditioning on a null action event is needed.

It follows that
\[
L_T(\lambda)=\exp\left\{\lambda W_T-\frac{\lambda^2}{8}K_T\right\},\qquad L_0(\lambda)=1,
\]
is a nonnegative supermartingale under the original probability law. Its finite-time integrability follows either inductively from (3), or from the upper bound \(D_t\le1-\alpha\). This construction applies to zero and positive drift budgets alike and does not condition on \(G\).

### 4. Stitching over every positive clock value

For each integer \(k\ge0\), let
\[
\eta_k=\frac{\delta}{(k+1)(k+2)},\qquad
h_k=\log(1/\eta_k),\qquad
\lambda_k=\sqrt{\frac{8h_k}{2^{k+1}}}.
\]
Since \(\sum_{k\ge0}\eta_k=\delta\), Ville's inequality and a union bound give an event \(H\), with \(\mathbb P(H)\ge1-\delta\), on which, for every \(k\) and every \(T\),
\[
W_T\le\frac{\lambda_k}{8}K_T+\frac{h_k}{\lambda_k}.
\tag{4}
\]
If \(2^k\le K_T<2^{k+1}\), then
\[
\frac{\lambda_k}{8}K_T+\frac{h_k}{\lambda_k}
\le\frac{\lambda_k}{8}2^{k+1}+\frac{h_k}{\lambda_k}
=\sqrt{2^kh_k}\le\sqrt{K_Th_k}.
\tag{5}
\]
These blocks cover every positive integer \(K_T\), including one. If \(K_T=0\), then every \(B_t\) up to \(T\) is zero and \(W_T=0\).

Define
\[
H_\delta(n)=\log(1/\delta)+\log\log(en+e).
\]
For \(n\ge1\), write \(b(n)=\log\log(en+e)=\log(1+\log(n+1))\), and set \(b_0=\log(1+\log2)>0\). If \(2^k\le n\), then
\[
k+2\le2(1+\log(n+1)),
\]
so
\[
h_k\le\log(1/\delta)+2\log(k+2)
\le\log(1/\delta)+2\log2+2b(n).
\]
Because \(b(n)\ge b_0\), there is an absolute constant
\[
C=\max\left\{1,\ 2+\frac{2\log2}{b_0}\right\}
\]
such that \(h_k\le C H_\delta(n)\). Equations (4)-(5) therefore imply, simultaneously for all \(T\) on \(H\),
\[
W_T\le\sqrt C\sqrt{(K_T\vee1)H_\delta(K_T)}+H_\delta(K_T).
\tag{6}
\]
For \(K_T=0\), this also follows from \(W_T=0\) and \(H_\delta(0)=\log(1/\delta)>0\). The nonnegative linear term in (6) merely weakens the square-root bound.

### 5. Intersecting events and normalizing

The union bound gives \(\mathbb P(G\cap H)\ge1-2\delta\); independence is not asserted or needed. On \(G\), equation (1) gives \(J_t=1\) for every \(t\), hence
\[
K_T=N_T,\qquad
W_T=\sum_{t\le T}A_t((1-V_t)-\alpha)-\sum_{t\le T}\nu_{j(t)}A_t.
\]
For \(N_T>0\), divide (6) by \(N_T\). With the universal choices \(c_1=\sqrt C\) and \(c_2=1\), this gives
\[
R_T^{\mathrm{act}}\le\alpha+\bar\nu_T
+c_1\sqrt{\frac{\log(1/\delta)+\log\log(eN_T+e)}{N_T\vee1}}
+c_2\frac{\log(1/\delta)+\log\log(eN_T+e)}{N_T\vee1}.
\]
For \(N_T=0\), the left side and \(\bar\nu_T\) are zero and the bound is immediate. All events used above are simultaneous over time. The constants are independent of the grid, epoch schedule, betting strategy, distribution, drift budgets, \(\alpha\), and \(\delta\).

## Source-Local Proof Repairs

The mathematical conclusion is unchanged. The following corrections are recorded explicitly rather than treated as clean source derivations.

- **theory_004, L000696:** The displayed raw conditional-mgf bound with the random \(A_t\) on its right side is not valid in general. The valid statement is the compensated-mgf inequality (3), obtained by conditioning on action and then averaging. The range-of-length-one assertion applies to the action-conditional variable.
- **theory_005, L000699-L000704 and L000707-L000712:** A supermartingale cannot be obtained merely by restricting attention to a future good event. Use the source's predictable safe-step mask under the original law for all drift budgets, including zero, and intersect with the certification event only after obtaining the concentration event.
- **theory_005, L000709:** The conditional drift calculation subtracts \(\nu_j\mathbb E[A_t\mid\mathcal F_{t-1}]\), not \(\nu_j\). The shifted increment has length-one range conditional on action; an inactive zero need not belong to that shifted interval.
- **theory_005, L000700 and L000710:** The source's strict-lower dyadic blocks omit action count one. The blocks in step 4 cover all positive integer clock values.

Each correction uses the same source-defined processes and elementary conditioning or endpoint accounting. Every theorem-critical obligation is closed above; no GT quality warning is required.
