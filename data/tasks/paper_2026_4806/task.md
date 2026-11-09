# Problem

## Setup

Let \(H,K\ge1\) be integers, and let \(X,Y,A\), and \(Z_{\rm eff}\) be finite nonempty sets. Consider a finite-horizon episodic Markov decision process with state space \(S=X\times Y\), horizon \(H\), a time-homogeneous transition kernel, and a known reward function \(r:S\times A\to[0,1]\).

The transition kernel factors as
\[
P(x',y'\mid s,a)=P_X(x'\mid s,a,y')P_Y(y'\mid s,a),
\]
where \(P_Y\) is known. There is a known map \(\phi_Z:S\times A\times Y\to Z_{\rm eff}\) and unknown probability distributions \(P_{\rm eff}(\cdot\mid z)\) on \(X\) such that
\[
P_X(\cdot\mid s,a,y)=P_{\rm eff}(\cdot\mid\phi_Z(s,a,y)).
\]
For each \(z\), a known integer \(B(z)\in[1,|X|]\) bounds the support size of \(P_{\rm eff}(\cdot\mid z)\). The support itself need not be known. The conditional laws are the only unknown parts of the reward and transition model.

Episodes start from a fixed initial-state distribution. The initial state is observed, and at each stage the learner observes the current state, chooses an action, receives its reward, and observes the sampled next state, including the final next state. Conditional on the current state and action, each next state is sampled from the specified kernel. No future observations are available when an action is chosen.

For a stage-dependent Markov policy \(\pi=(\pi_h)_{h=1}^H\), define
\[
V_h^\pi(s)=\mathbb E\left[\sum_{j=h}^H r(s_j,\pi_j(s_j))\mid s_h=s\right],\qquad V_h^*(s)=\max_\pi V_h^\pi(s).
\]
For the policies \(\pi^k\) used by the learner and the observed initial states \(s_1^k\), define cumulative regret by
\[
R_K=\sum_{k=1}^K\left(V_1^*(s_1^k)-V_1^{\pi^k}(s_1^k)\right).
\]

## Algorithm

Fix \(\delta\in(0,1)\). For every observed transition in episode \(i\), assign \(x_{h+1}^i\) to the context
\[
z_h^i=\phi_Z(s_h^i,a_h^i,y_{h+1}^i).
\]
Before episode \(k\), let
\[
N_k(z)=\sum_{i<k}\sum_{h=1}^H\mathbf1\{z_h^i=z\}.
\]
When \(N_k(z)>0\), let \(\widehat P_k(\cdot\mid z)\) be the empirical distribution of the assigned observations. When \(N_k(z)=0\), choose any fixed distribution on \(X\); it will not be used in the formula below. Counts and estimates are held fixed throughout the episode.

Set
\[
\ell(z)=\min\left\{\log\frac{128H^2|Y||Z_{\rm eff}|K}{\delta},\ B(z)\log\frac{128HB(z)|Z_{\rm eff}|K}{\delta}\right\}.
\]
For a probability distribution \(p\) on \(X\) and a function \(f:X\to\mathbb R\), write
\[
pf=\sum_xp(x)f(x),\qquad \operatorname{Var}_p(f)=\sum_xp(x)(f(x)-pf)^2.
\]
Given positive universal constants \(c_1,c_2\), compute \(V_{H+1}^k\equiv0\) and, backward for \(h=H,\ldots,1\), define the following quantities for every \(s,a,y\). Put \(z=\phi_Z(s,a,y)\), \(p=\widehat P_k(\cdot\mid z)\), and \(f(x)=V_{h+1}^k(x,y)\). Let
\[
q_h^k(s,a,y)=
\begin{cases}
H,&N_k(z)\le1,\\
\displaystyle\min\left\{H,\ r(s,a)+pf+c_1\sqrt{\frac{\operatorname{Var}_p(f)\ell(z)}{N_k(z)}}+c_2\frac{H\ell(z)}{N_k(z)}\right\},&N_k(z)\ge2.
\end{cases}
\]
Then set
\[
Q_h^k(s,a)=\sum_{y\in Y}P_Y(y\mid s,a)q_h^k(s,a,y),\qquad
V_h^k(s)=\max_{a\in A}Q_h^k(s,a),\qquad
\pi_h^k(s)\in\arg\max_{a\in A}Q_h^k(s,a),
\]
using a fixed tie-breaking rule. Construct this policy from the preceding episodes and execute it for episode \(k\), updating the data afterward. Terms with \(P_Y(y\mid s,a)=0\) contribute zero to the displayed sum.

## Task

Prove that there are positive universal constants \(c_1,c_2\) such that, for every MDP satisfying this setup, every \(H,K\ge1\), and every \(\delta\in(0,1)\), the algorithm satisfies, with probability at least \(1-\delta\),
\[
R_K\le\widetilde O\!\left(
H\sqrt{K\sum_{z\in Z_{\rm eff}}\min\{B(z),\log(e|Y|)\}}
+H\sum_{z\in Z_{\rm eff}}B(z)
\right).
\]
The hidden multiplicative constants are universal, and the hidden factors are logarithmic in the displayed problem dimensions and \(1/\delta\). The comparison policy is optimal for the true MDP.
