# Problem

## Setup

Let \(\mathcal M=(\mathcal S,\mathcal A,P,\gamma)\) be a reward-free discounted Markov decision process with \(\gamma\in(0,1)\). The state and action spaces are measurable, and \(P(\cdot\mid s,a)\) is a measurable probability kernel. For a policy \(\rho\), which may depend on the observed history, define
\[
m_\beta^\rho(X\mid s,a)=(1-\beta)\sum_{t=0}^{\infty}\beta^t\Pr(S_{t+1}\in X\mid S_0=s,A_0=a,\rho),
\]
for measurable \(X\subseteq\mathcal S\) and \(\beta\in[0,1)\). Here the probability denotes the trajectory law started at the prescribed pair \((s,a)\) and following \(\rho\) thereafter.

Fix a positive integer \(n\), stationary Markov policies \(\pi_{z_1},\ldots,\pi_{z_n}\), each a measurable probability kernel from states to actions, and switching probabilities \(\alpha_1,\ldots,\alpha_{n-1}\in[0,1]\), with \(\alpha_n:=0\). Let \(\nu\) be the following switching policy, initialized in phase 1. Starting from the prescribed \((S_0,A_0)=(s,a)\), at each transition first draw \(S_{t+1}\sim P(\cdot\mid S_t,A_t)\). If the current phase is \(k<n\), use a fresh Bernoulli draw with parameter \(\alpha_k\) to decide whether to advance permanently to phase \(k+1\) or remain in phase \(k\), and draw \(A_{t+1}\) from the policy of the resulting phase at \(S_{t+1}\). Phase \(n\) is absorbing, and its actions are drawn from \(\pi_{z_n}\).

Set
\[
\beta_k:=\gamma(1-\alpha_k)\quad(k=1,\ldots,n),\qquad \beta_n=\gamma,
\]
and
\[
w_k:=\frac{1-\gamma}{1-\beta_k}\prod_{i<k}\frac{\gamma-\beta_i}{1-\beta_i},
\]
where an empty product equals 1. Define \(\bar m_\beta^\pi(\cdot\mid s):=\int\pi(da\mid s)m_\beta^\pi(\cdot\mid s,a)\), and let \(C_{1:k}(\cdot\mid s,a)\) be the sequential kernel obtained by sampling first from \(m_{\beta_1}^{\pi_{z_1}}(\cdot\mid s,a)\), then successively from \(\bar m_{\beta_j}^{\pi_{z_j}}(\cdot\mid\cdot)\) for \(j=2,\ldots,k\).

## Task

Prove that, for every initial state-action pair \((s,a)\),
\[
m_\gamma^\nu(\cdot\mid s,a)=\sum_{k=1}^{n}w_k\,C_{1:k}(\cdot\mid s,a).
\]
