# Problem

## Setup

Fix positive integers \(m\) and \(d\). Let \(\Theta\subseteq\mathbb R^d\) be a measurable parameter space, let \(\mathcal O\) be an observation space, and let \(\ell:\Theta\times\mathcal O\to[0,\infty)\) be a measurable loss. Fix an ordered list of task distributions \(P^1,\ldots,P^m\), and define the expected loss on task \(k\) by

\[
L^k(\theta):=\mathbb E_{o\sim P^k}[\ell(\theta,o)].
\]

For each positive integer \(N\), run this task list sequentially, with every task having duration \(N\). The observation distribution is fixed within each task, and task switch points are known to the procedures. A procedure's prediction is evaluated on the next observation before that observation is used for learning.

Consider two procedures. The retained procedure \(R\) trains within task \(k\) using the fixed duration-weighted mixture of all tasks seen so far, which for these equal durations is \(k^{-1}\sum_{j=1}^kP^j\), and preserves its parameters across task boundaries. The reset procedure \(S\) trains only on \(P^k\) and resets its parameters at every task boundary to a fixed initialization distribution \(Q_{\mathrm{init}}\).

For each procedure, its update law within a task is time homogeneous. The task distributions, update rules, initial parameter laws, and reset distribution are fixed as \(N\) varies. The retained procedure's parameter law at a later task boundary may nevertheless depend on \(N\) through its previous training.

Let \(Q_{N,t}^k(A)\), for \(t=0,\ldots,N-1\), be the parameter law used by procedure \(A\) to predict the next observation at local step \(t\) of task \(k\) in this duration-\(N\) run. Define its average expected loss during that task by

\[
E_N^k(A):=\frac1N\sum_{t=0}^{N-1}\mathbb E_{\theta\sim Q_{N,t}^k(A)}[L^k(\theta)].
\]

These expectations include the randomness of the learning trajectory; evaluation uses the current task distribution \(P^k\), not the procedure's training mixture.

Assume both procedures are task-wise convergent in the following sense. For every \(A\in\{R,S\}\) and task \(k\), indefinitely repeating its fixed within-task dynamics gives a stationary parameter law \(Q_\infty^k(A)\). From every initialization law with finite second moment, the iterate laws \(Q_t\) have finite second moments and satisfy

\[
W_2(Q_t,Q_\infty^k(A))\longrightarrow0\qquad(t\to\infty),
\]

with the same limit regardless of initialization. Here, for probability laws \(\mu,\nu\) with finite second moments,

\[
W_2(\mu,\nu):=\left(\inf_{\gamma\in\Gamma(\mu,\nu)}\int\|x-y\|_2^2\,\gamma(dx,dy)\right)^{1/2},
\]

where \(\Gamma(\mu,\nu)\) is the set of joint probability laws with marginals \(\mu\) and \(\nu\). All initialization laws used by the procedures have finite second moments.

Let

\[
r^k(A):=\mathbb E_{\theta\sim Q_\infty^k(A)}[L^k(\theta)]
\]

be the stationary expected loss on task \(k\). Assume these stationary losses and every finite-horizon expected loss used above are finite. The stationary laws and losses are those of the fixed within-task dynamics and do not vary with \(N\).

Define the finite-horizon transient excess, transfer gap, stationary instability, and cumulative transient excesses by

\[
\varepsilon_N^k(A):=E_N^k(A)-r^k(A),
\qquad
g_N^k:=E_N^k(S)-E_N^k(R),
\]

\[
\iota^k:=r^k(R)-r^k(S),\qquad
\Delta_N^k(A):=N\varepsilon_N^k(A).
\]

For any task-indexed quantity \(x^k\), write \(\bar x=m^{-1}\sum_{k=1}^m x^k\). In particular, let

\[
D_N:=\bar\Delta_N(S)-\bar\Delta_N(R).
\]

Assume \(\bar\iota>0\) and, separately, for each \(A\in\{R,S\}\), \(\bar\Delta_N(A)=o(N)\) as \(N\to\infty\) through positive integers; that is, \(\bar\Delta_N(A)/N\to0\).

## Task

Prove the following integrated claim:

\[
\bar g_N=-\bar\iota+\bar\varepsilon_N(S)-\bar\varepsilon_N(R)
=-\bar\iota+\frac{D_N}{N}.
\]

Deduce that there exists a positive integer \(N_0\) such that \(\bar g_N<0\) for every integer \(N\ge N_0\). Finally, show that any positive integer breakeven duration \(N_{\mathrm{crit}}\) satisfying \(\bar g_{N_{\mathrm{crit}}}=0\) obeys

\[
N_{\mathrm{crit}}
=\frac{\bar\Delta_{N_{\mathrm{crit}}}(S)-\bar\Delta_{N_{\mathrm{crit}}}(R)}{\bar\iota}.
\]

Thus the displayed ratio is interpreted with its cumulative transient quantities evaluated at the breakeven scale.
