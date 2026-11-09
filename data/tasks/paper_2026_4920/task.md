# Problem

## Setup

Let \(H,n\) be positive integers and \(\delta\in(0,1)\). Consider a finite-horizon Markov decision process with stages \(h=0,\ldots,H-1\), nonempty Borel state and action spaces \(\mathcal X\subseteq\mathbb R^{d_x}\) and \(\mathcal U\subseteq\mathbb R^{d_u}\), and fixed norms on the two ambient spaces. Policies are time-dependent measurable Markov probability kernels.

The dynamics have measurable noise representations
\[
X_0=f_{\mathrm{init}}(\xi_0),\qquad
X_{h+1}=f_h(X_h,A_h,\xi_{h+1}).
\]
The noises have prescribed laws \(\mu_0,\ldots,\mu_H\). In each rollout, the initial noise is sampled first, and each transition noise is sampled independently of the past and the current action. The initial noise map and, for every state-action pair, each noise-to-next-state map are almost surely injective under their respective noise laws.

For constants \(R,L_x,L_u\ge0\), the measurable rewards satisfy, for every stage and all arguments,
\[
|r_h(x,u)|\le R,
\qquad
|r_h(x,u)-r_h(x',u')|
\le L_x\|x-x'\|+L_u\|u-u'\|.
\]
Write
\[
J(\pi)=\mathbb E_{\pi}\!\left[\sum_{h=0}^{H-1}r_h(X_h,A_h)\right]
\]
for the return when \(\pi\) is deployed in these dynamics.

A shared-noise coupling of two rollout laws is a joint realization of their trajectories and prescribed noises in which the two copies of every noise agree almost surely. Fix an expert policy \(\pi^*\). Assume there is a continuous nondecreasing function \(\gamma:[0,\infty)\to[0,\infty)\), with \(\gamma(0)=0\), such that for every comparison Markov policy and every shared-noise coupling of its rollout with the expert rollout, almost surely
\[
\|X_{t+1}^*-X_{t+1}'\|
\le\gamma\!\left(\max_{0\le s\le t}\|A_s^*-A_s'\|\right),
\qquad t=0,\ldots,H-1.
\]
This is the global stability assumption used here.

For \(\varepsilon\ge0\), define
\[
c_\varepsilon(u,u')=\mathbf1\{\|u-u'\|>\varepsilon\},
\qquad
W_{c_\varepsilon}(P,Q)=\inf_{\lambda\in\Gamma(P,Q)}\int c_\varepsilon\,d\lambda,
\]
where \(\Gamma(P,Q)\) is the set of probability couplings of \(P,Q\). A policy \(\pi\) is \(\varepsilon\)-RTVC with nondecreasing modulus \(\kappa:[0,\infty)\to[0,\infty)\) if
\[
W_{c_\varepsilon}(\pi_h(\cdot\mid x),\pi_h(\cdot\mid x'))
\le\kappa(\|x-x'\|)
\]
for every stage and every \(x,x'\in\mathcal X\). No continuity of \(\kappa\) is required.

Fix \(\epsilon_q>0\), \(k>0\), and a measurable quantizer \(q:\mathcal U\to\mathcal V\), where \(\mathcal V=q(\mathcal U)\subseteq\mathcal U\) is a nonempty finite set of representative actions. Assume
\[
\|q(u)-u\|\le\epsilon_q\qquad\text{for every }u\in\mathcal U.
\]
Define the quantized expert by
\[
(q\#\pi^*)_h(v\mid x)=\pi_h^*(q^{-1}(\{v\})\mid x).
\]
Assume this quantized policy is deterministic at every state and stage. The raw expert policy itself need not be deterministic.

Let \(\Pi\) be a nonempty finite class of measurable Markov policies on \(\mathcal V\), fixed before observing the training data. Assume \(q\#\pi^*\in\Pi\), and assume every \(\pi\in\Pi\), viewed as a probability kernel on the representative actions in \(\mathcal U\), is \(k\epsilon_q\)-RTVC with the same modulus \(\kappa\).

Observe \(n\) independent raw expert rollouts, retaining their states and quantized actions:
\[
\bigl(X_0^i,\ldots,X_H^i,\ V_0^i,\ldots,V_{H-1}^i\bigr),
\qquad V_h^i=q(A_h^i).
\]
The quantizer is fixed before these samples are drawn. Let \(\widehat\pi\) be any measurable choice of maximizer
\[
\widehat\pi\in\operatorname*{argmax}_{\pi\in\Pi}
\sum_{i=1}^n\sum_{h=0}^{H-1}\log\pi_h(V_h^i\mid X_h^i),
\]
with \(\log0=-\infty\). At deployment, sample an action from \(\widehat\pi_h(\cdot\mid X_h)\) and execute that representative action directly in the original dynamics.

## Task

Prove that there is a constant \(C\), depending only on \(R,L_x,L_u\), such that with probability at least \(1-\delta\) over the training data,
\[
J(\pi^*)-J(\widehat\pi)
\le C\left[
\frac{H\log(|\Pi|/\delta)}{n}
+H^2\kappa\!\left(\gamma((k+1)\epsilon_q)\right)
+H\left\{\gamma((k+1)\epsilon_q)+(k+1)\epsilon_q\right\}
\right].
\]
