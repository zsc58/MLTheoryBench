# Problem

## Setup

Let \(G=(S,E)\) be a finite directed graph. There are distinct states \(s_0\) and \(s_f\): the initial state \(s_0\) has no incoming edges, and the sink \(s_f\) has no outgoing edges. Every state is reachable from \(s_0\), and every state can reach \(s_f\). Let
\[
X=\{x\in S:(x,s_f)\in E\}
\]
be the terminal states. Each \(x\in X\) has a positive real reward \(R(x)\), and write \(Z=\sum_{x\in X}R(x)\).

A trajectory is a finite directed walk
\[
\tau=(s_0\to s_1\to\cdots\to s_{n_\tau}=x\to s_f),\qquad x\in X,
\]
where repeated states are permitted and \(n_\tau\ge0\) counts the edges before the final transition to \(s_f\). In particular, if \(s_0\in X\), the trajectory \(s_0\to s_f\) has \(n_\tau=0\). The graph may contain directed cycles. For each state \(s\), let \(\operatorname{cl}(s)\) be the length of a shortest directed path from \(s_0\) to \(s\); in particular, \(\operatorname{cl}(x)\) is the shortest possible value of \(n_\tau\) among trajectories terminating at \(x\).

A backward policy \(P_B(\cdot\mid s')\), for each \(s'\ne s_0\), is a probability distribution on \(\{s:(s,s')\in E\}\). It defines a reversed walk starting at \(s_f\) and stopping when it reaches \(s_0\); no transition is required at \(s_0\). For a terminating walk, its length \(n_\tau\) is its number of reversed transitions minus one, consistently with the trajectory convention above. Set this length to \(+\infty\) on nontermination, and assume its unconditioned expectation satisfies \(\mathbb E_B[n_\tau]<\infty\). Write \(\mathbb P_B(\tau)\) for the probability of a finite trajectory, given by multiplying the backward transition probabilities along its reversed walk.

The policy is reward-matching when
\[
P_B(x\mid s_f)=R(x)/Z\quad\text{for every }x\in X.
\]

## Task

Prove the following theorem: among all reward-matching backward policies with finite expected trajectory length, a policy minimizes \(\mathbb E_B[n_\tau]\) if and only if every trajectory \(\tau\) with positive probability is shortest for its terminal state, i.e. \(n_\tau=\operatorname{cl}(x)\) whenever \(\mathbb P_B(\tau)>0\). Equivalently, the minimizing trajectory distribution is supported entirely on shortest paths from \(s_0\) to terminal states.
