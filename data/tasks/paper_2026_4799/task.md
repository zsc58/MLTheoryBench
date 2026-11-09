# Problem

## Setup

Let \(E=(S,A,P,\mu_0)\) be a finite, stationary, fully observed controlled Markov environment. Write \(P_{ss'}(a)=P(s'\mid s,a)\). Assume \(|A|\ge2\), that some transition probability differs between two actions, and that the environment is communicating: from any state, every other state can be reached with positive probability by some finite action sequence.

Fix an initial state \(s_0\in S\), an integer \(n\ge1\), and distinct marker actions \(L,R\in A\). All policy probabilities and values below refer to experiments started at \(S_0=s_0\). Policies are goal-conditioned and nonanticipating: their action distributions depend on the observed history and the supplied goal, with private randomization independent of future environment transitions. At time zero a policy chooses \(A_0\in\{L,R\}\); thereafter it may choose any action in \(A\).

For \(s,s'\in S\), \(a\in A\), and \(k\in\{0,\ldots,n\}\), define a goal \(G^{(n)}_{s,a,s',k}\) as follows. For the infinite trajectory, let
\[
T_1=\inf\{t\ge1:(S_t,A_t)=(s,a)\},\qquad
T_{i+1}=\inf\{t>T_i:(S_t,A_t)=(s,a)\},
\]
with \(\inf\varnothing=\infty\). Let \(X_i\) be one if \(T_i<\infty\) and \(S_{T_i+1}=s'\), and zero otherwise, and set \(N_n=\sum_{i=1}^nX_i\). The goal succeeds exactly when
\[
T_n<\infty
\quad\text{and}\quad
\bigl[(A_0=L\text{ and }N_n\le k)\text{ or }(A_0=R\text{ and }N_n>k)\bigr].
\]
Its utility is this success indicator. In particular, not obtaining all n attempts is failure; success probabilities are not conditioned on obtaining them.

For a fixed policy \(\pi\), let
\[
q_{s,a,s',k}=\Pr_\pi(A_0=L\mid S_0=s_0,G^{(n)}_{s,a,s',k}),\qquad
V_{s,a,s',k}=\Pr_\pi(G^{(n)}_{s,a,s',k}\mid S_0=s_0).
\]
Let \(V^*_{s,a,s',k}\) be the supremum of the success probability over admissible policies, optimizing both the initial marker and all subsequent actions. Define
\[
\delta_{s,a,s',k}=1-\frac{V_{s,a,s',k}}{V^*_{s,a,s',k}}.
\]
Assume that, for some \(\bar\delta\ge0\),
\[
\mathbb E_{(s,a,s',k)\sim\operatorname{Unif}(S\times A\times S\times\{0,\ldots,n\})}
\delta_{s,a,s',k}\le\bar\delta.
\]

For \(\gamma\in(0,1/2)\), set
\[
c(\gamma)=\frac{4\gamma}{1+2\gamma},\qquad
t_\gamma=\sqrt{\frac{1+2\gamma}{1-2\gamma}}.
\]
Define
\[
\widehat P_{ss'}(a)=\operatorname{clip}_{[0,1]}\!\left[\frac1n\left(\sum_{k=0}^{n}(1-q_{s,a,s',k})-\frac12\right)\right],
\]
where \(\operatorname{clip}_{[0,1]}(x)=\min\{1,\max\{0,x\}\}\).

Optionally suppose the environment has a causal interpretation with one-step interventional kernel
\[
P^{\rm do}_{ss'}(a)=\Pr(S_{t+1}=s'\mid S_t=s,\operatorname{do}(A_t=a))
\]
and a number \(\varepsilon_{\rm cMP}\ge0\) such that
\[
|P_{ss'}(a)-P^{\rm do}_{ss'}(a)|\le\varepsilon_{\rm cMP}
\qquad\text{for every }s,a,s'.
\]

## Task

Prove that, for every fixed \(\gamma\in(0,1/2)\),
\[
\mathbb E_{s,a,s'}\!\left|\widehat P_{ss'}(a)-P_{ss'}(a)\right|
\le 2t_\gamma\,\mathbb E_{s,a,s'}\!\sqrt{\frac{P_{ss'}(a)(1-P_{ss'}(a))}{n}}
+\frac{\bar\delta}{c(\gamma)}+O_\gamma(n^{-1})
\le \frac{t_\gamma}{\sqrt n}+\frac{\bar\delta}{c(\gamma)}+O_\gamma(n^{-1}),
\]
where expectations are uniform over \(S\times A\times S\). Here the remainder means an upper-bound term \(C_\gamma/n\), with a finite constant depending only on \(\gamma\), uniformly over the environment, policy, initial state, \(\bar\delta\), and \(n\).

Under the optional causal assumption, prove the same bounds relative to \(P^{\rm do}\), with an additional additive \(\varepsilon_{\rm cMP}\) and with the variance term still expressed using \(P\).

Also prove that exact knowledge of the entire one-step interventional kernel does not, in general, identify joint cross-action counterfactuals. Construct two explicit structural models in the stated environment class that have the same complete interventional kernel but different joint laws of \((S_{t+1}^{a},S_{t+1}^{a'})\) for some current state and distinct actions. Here \(S_{t+1}^{a}\) denotes the potential next state under action \(a\); the two potential outcomes in a joint counterfactual use the same exogenous realization within a structural model.
