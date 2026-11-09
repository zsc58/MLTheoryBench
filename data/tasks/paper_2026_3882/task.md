# Problem

## Setup

Fix integers \(M\geq2\) and \(N\geq3\), and fix \(\alpha_{\mathrm{task}},\alpha_{\mathrm{leader}}\in(0,1)\) with
\[
\alpha_{\mathrm{leader}}\geq\frac{2}{N+1}.
\]
The \(M\) models are fixed in advance and indexed by \(j=1,\ldots,M\).

A task configuration \(t\) specifies real true scores \(\mu_j(t)\) and a conditional law \(Q_t\) for an evaluation record \(D\). The record contains the observable evaluation data and any randomness used by the tests. Let \(\mathcal P\) be a distribution on task configurations. Sample \((t_1,D_1),\ldots,(t_N,D_N)\) independently from the same joint law obtained by drawing \(t\sim\mathcal P\) and then \(D\sim Q_t\). Let \(t^*\sim\mathcal P\) be independent of these observed records. The leaderboard interval is constructed using only the \(N\) observed records.

For each task, define the lower and upper ranks, allowing ties, by
\[
l_j(t)=1+\#\{k\ne j:\mu_j(t)>\mu_k(t)\},\qquad
u_j(t)=M-\#\{k\ne j:\mu_j(t)<\mu_k(t)\},
\]
where the upper-rank symbol in the remainder of the problem is \(u_j(t):=\nu_j(t)\). Define the rank set
\[
r_j(t)=\{l_j(t),l_j(t)+1,\ldots,u_j(t)\}.
\]

For every ordered pair \(j\ne k\), a fixed measurable testing rule produces \(p_{jk}(D)\in[0,1]\) for
\[
H_{jk,0}(t):\mu_j(t)\geq\mu_k(t)
\quad\text{against}\quad
H_{jk,1}(t):\mu_j(t)<\mu_k(t).
\]
The same rules are used on every task and use only that task's evaluation record. For every task configuration \(t\), every ordered pair whose null is true, and every \(s\in[0,1]\), assume
\[
Q_t\{D:p_{jk}(D)\leq s\}\leq s.
\]
The score functions and sampling laws are measurable.

For each fixed model \(j\), apply Holm's step-down rule separately to the families \(\{p_{kj}(D):k\ne j\}\) and \(\{p_{jk}(D):k\ne j\}\), each at level \(\beta=\alpha_{\mathrm{task}}/2\). Specifically, for a family of \(K=M-1\) hypotheses, order its p-values as \(q_{(1)}\leq\cdots\leq q_{(K)}\), reject the corresponding hypotheses sequentially while
\[
q_{(i)}\leq\frac{\beta}{K-i+1},
\]
and stop at the first failure, retaining that hypothesis and all subsequent ones.

Let \(W_j(t)\) contain the models \(k\ne j\) whose null \(H_{kj,0}(t)\) is rejected in the first family, and let \(B_j(t)\) contain those whose null \(H_{jk,0}(t)\) is rejected in the second family. Write
\[
L_j(t)=1+|W_j(t)|,\qquad U_j(t)=M-|B_j(t)|,
\]
with dependence on the task's evaluation record understood.

For each model, sort the observed endpoints in ascending order:
\[
L_{j,(1)}\leq\cdots\leq L_{j,(N)},\qquad
U_{j,(1)}\leq\cdots\leq U_{j,(N)}.
\]
Set
\[
k_l=\left\lfloor(N+1)\frac{\alpha_{\mathrm{leader}}}{2}\right\rfloor,
\qquad
k_u=\left\lceil(N+1)\left(1-\frac{\alpha_{\mathrm{leader}}}{2}\right)\right\rceil,
\]
and define the leaderboard interval by
\[
[L_j,U_j]=[L_{j,(k_l)},U_{j,(k_u)}].
\]

## Task

Prove that, for every fixed model \(j\),
\[
\mathbb P\bigl(r_j(t^*)\subseteq[L_j,U_j]\bigr)
\geq1-(\alpha_{\mathrm{task}}+\alpha_{\mathrm{leader}}),
\]
where the probability is over the observed task-data records and the independent unseen task.
