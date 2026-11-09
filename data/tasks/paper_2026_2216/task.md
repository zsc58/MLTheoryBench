# Problem

## Setup

Let S and A be finite nonempty sets of states and actions, respectively, and let \(0<\gamma<1\). At every state the available action set is A. Let \(P(\cdot\mid s,a)\) be transition probabilities on S and let \(R(s,a)\in\mathbb R\). Define the Bellman operator on real state-action functions by
\[
(\mathcal BQ)(s,a)=R(s,a)+\gamma\sum_{s'\in S}P(s'\mid s,a)\max_{a'\in A}Q(s',a').
\]
Let \(Q^*\) be its unique fixed point. For an arbitrary initial function \(Q_0\), define \(Q_{k+1}=\mathcal BQ_k\) for integers \(k\geq0\). Fix a deterministic tie-breaking rule and write \(\pi_Q(s)\) for the resulting greedy action. Let \(\Phi^*(s)\) be the set of all maximizers of \(Q^*(s,\cdot)\), and define
\[
X^*=\{Q:\pi_Q(s)\in\Phi^*(s)\text{ for every }s\},\qquad
X_1=\{Q^*+\alpha\mathbf1:\alpha\in\mathbb R\}.
\]
Here \(\mathbf1\) denotes the all-ones state-action vector. For \(p\in\{2,\infty\}\), write
\[
\operatorname{dist}_p(Q,X_1)=\inf_{Y\in X_1}\|Q-Y\|_p.
\]

Vectorize state-action functions in a fixed order and put \(m=|S||A|\). Let P also denote the matrix with entries \(P_{(s,a),s'}=P(s'\mid s,a)\). For a deterministic policy \(\pi:S\to A\), define
\[
(\Pi^\pi Q)(s)=Q(s,\pi(s)).
\]
Enumerate all deterministic policies as \(\{\pi_i\}_{i=1}^M\), and put
\[
A_i=\gamma P\Pi^{\pi_i},\qquad
\Pi_\perp=I-\frac1m\mathbf1\mathbf1^\top,\qquad
\bar A_i=\Pi_\perp A_i\Pi_\perp.
\]
Define their joint spectral radius by
\[
\bar\rho=\lim_{j\to\infty}
\left(\max_{i_1,\ldots,i_j\in\{1,\ldots,M\}}
\|\bar A_{i_j}\cdots\bar A_{i_1}\|_{2\to2}\right)^{1/j},
\]
where \(\|\cdot\|_{2\to2}\) is the Euclidean operator norm.

Assume that at least one state has a nonoptimal action. For each such state define
\[
\Delta_s=\max_{a\in A}Q^*(s,a)-\max_{a\in A\setminus\Phi^*(s)}Q^*(s,a),
\qquad \Delta=\min_{s:\Phi^*(s)\ne A}\Delta_s>0.
\]
For \(0<\delta<\Delta/2\), define
\[
T_\delta=\{Q:\operatorname{dist}_\infty(Q,X_1)\leq\delta\}.
\]

## Task

Prove that for every \(\varepsilon\in(0,1-\bar\rho)\) there is a constant \(c_\varepsilon>0\), allowed to depend on the fixed MDP and epsilon but not on \(Q_0\) or k, such that, with \(\beta_\varepsilon=\bar\rho+\varepsilon\), every initialization satisfies
\[
\operatorname{dist}_2(Q_k,X_1)
\leq c_\varepsilon\beta_\varepsilon^k\operatorname{dist}_2(Q_0,X_1)
\qquad(k\geq0).
\]

Moreover, prove that for every \(0<\delta<\Delta/2\),
\[
T_\delta\subseteq X^*,\qquad \mathcal B(T_\delta)\subseteq T_\delta,
\]
and for every initialization there is an integer \(K\geq0\) such that \(Q_k\in T_\delta\) for every \(k\geq K\). Consequently, show that
\[
\pi_{Q_k}(s)\in\Phi^*(s)\qquad\text{for every }s\in S\text{ and every }k\geq K.
\]
