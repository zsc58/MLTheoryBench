# Problem

## Setup

Let \((\mathcal F_t)_{t\ge0}\) be a filtration, let \(\alpha\in(0,1)\), \(\delta\in(0,1)\), and let
\[
\mathcal Q=\{q_1<\cdots<q_m\}
\]
be a finite ordered threshold grid. Time is partitioned into deterministic epochs \(I_j\), whose first times are denoted by \(\tau_j\).

At round \(t\), a score rule fixed using \(\mathcal F_{t-1}\) produces nested gates
\[
A_t(q)=\mathbf 1\{S_t(X_t,Y_t)\le q\},\qquad q\in\mathcal Q.
\]
The verifier outcome is \(V_t\in\{0,1\}\), where \(V_t=0\) denotes failure. Information generated at round \(t\) is incorporated only into \(\mathcal F_t\), and hence can affect the controller only from round \(t+1\) onward. Assume that, conditionally on \(\mathcal F_{t-1}\), the failure rate among gated samples is nondecreasing in \(q\) (whenever the relevant conditional action probability is positive).

Define
\[
Z_t(q)=A_t(q)((1-V_t)-\alpha)
\]
and let \(q_t^\star\) be the largest \(q\in\mathcal Q\) satisfying
\[
\mathbb E[Z_t(q)\mid\mathcal F_{t-1}]\le0.
\]
Adjoin an abstention symbol \(\bot<q_1\), set \(A_t(\bot)=0\), and take \(q_t^\star=\bot\) if no grid threshold satisfies the inequality.

For each epoch \(I_j\), threshold \(q\), and predictable sequence
\[
0\le \lambda_{j,t}(q)\le (1-\alpha)^{-1},
\]
define
\[
E_{j,t}(q)=\prod_{s=\tau_j}^{t}\bigl(1-\lambda_{j,s}(q)Z_s(q)\bigr),
\qquad E_{j,\tau_j-1}(q)=1,
\]
and
\[
\delta_{j,q}=\frac{6\delta}{\pi^2mj^2},
\qquad
\mathcal C_{j,t}=\{q\in\mathcal Q:E_{j,t}(q)\ge\delta_{j,q}^{-1}\}.
\]
Within an epoch, the next-round threshold is
\[
q_{t+1}=\max\mathcal C_{j,t},
\]
with \(q_{t+1}=\bot\) when the set is empty. At every deterministic epoch boundary, all products are reset and the first round of the new epoch abstains.

Assume the oracle frontier is nondecreasing within each epoch: if \(s\le t\) belong to \(I_j\), then \(q_s^\star\le q_t^\star\). Let \(\nu_j\ge0\) be deterministic declared drift budgets such that, on every round \(t\in I_j\), whenever \(q_t\le q_t^\star\),
\[
\mathbb E\!\left[A_t(q_t)((1-V_t)-\alpha)\mid\mathcal F_{t-1}\right]
\le \nu_j\,\mathbb E[A_t(q_t)\mid\mathcal F_{t-1}].
\]

Write
\[
A_t=A_t(q_t),\qquad
N_T=\sum_{t=1}^T A_t,
\]
\[
R_T^{\mathrm{act}}=
\frac{\sum_{t=1}^T A_t(1-V_t)}{N_T\vee1},
\qquad
\bar\nu_T=
\frac{\sum_{t=1}^T\nu_{j(t)}A_t}{N_T\vee1},
\]
where \(j(t)\) is the epoch containing \(t\).

## Task

Prove that there are universal constants \(c_1,c_2>0\) such that, with probability at least \(1-2\delta\), simultaneously for every integer \(T\ge1\),
\[
R_T^{\mathrm{act}}
\le \alpha+\bar\nu_T
+c_1\sqrt{\frac{\log(1/\delta)+\log\log(eN_T+e)}{N_T\vee1}}
+c_2\frac{\log(1/\delta)+\log\log(eN_T+e)}{N_T\vee1}.
\]
