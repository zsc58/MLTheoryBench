# Problem

## Setup

Let \(S\) and \(A\) be finite nonempty state and action sets. Fix \(\gamma\in(0,1)\) and an initial distribution \(\mu\) with \(\mu(s)>0\) for every state. Let \(\mathcal U\) be a nonempty compact set of models \(u=(c,P)\), where \(c:S\times A\to[0,1]\) and \(P(\cdot\mid s,a)\) is a probability distribution on \(S\). Let
\[
\Pi=\{\pi\in\mathbb R^{S\times A}:\pi(a\mid s)\ge0,\ \sum_a\pi(a\mid s)=1\text{ for every }s\}
\]
be the set of stationary randomized policies. Use the Euclidean inner product and norm on policy arrays, and let \(\operatorname{Proj}_\Pi\) denote Euclidean projection onto \(\Pi\).

For \(u=(c,P)\) and \(\pi\in\Pi\), define
\[
V_u^\pi(s)=c_\pi(s)+\gamma\sum_{s'}P_\pi(s'\mid s)V_u^\pi(s'),\qquad
Q_u^\pi(s,a)=c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V_u^\pi(s'),
\]
with \(c_\pi(s)=\sum_a\pi(a\mid s)c(s,a)\) and \(P_\pi(s'\mid s)=\sum_a\pi(a\mid s)P(s'\mid s,a)\). Set
\[
J_u(\pi)=\sum_s\mu(s)V_u^\pi(s),\qquad J_{\mathcal U}(\pi)=\max_{u\in\mathcal U}J_u(\pi).
\]
Let \(\pi^*\in\arg\min_{\pi\in\Pi}J_{\mathcal U}(\pi)\), let \(\mathcal U^\pi=\arg\max_{u\in\mathcal U}J_u(\pi)\), and write \(P^\pi=\{P:u=(c,P)\in\mathcal U^\pi\}\) and \(Q^\pi=\{Q_u^\pi:u\in\mathcal U^\pi\}\).

For subdifferentiation, extend the objectives to real policy arrays in a sufficiently small open neighborhood of \(\Pi\) using the same Bellman formulas, and let \(\partial J_{\mathcal U}(\pi)\) denote the Clarke subdifferential of this extension, without adding a policy-constraint indicator. Define
\[
G(\pi)=\min_{g\in\partial J_{\mathcal U}(\pi)}\max_{\rho\in\Pi}\sum_{s,a}(\pi(a\mid s)-\rho(a\mid s))g(s,a).
\]
The objective is called subgradient-dominant with constant \(D>0\) if
\[
J_{\mathcal U}(\pi)-J_{\mathcal U}(\pi^*)\le D G(\pi)\qquad\text{for every }\pi\in\Pi.
\]
For \(\varepsilon>0\), a policy is \(\varepsilon\)-optimal if its robust objective gap is at most \(\varepsilon\).

## Task

Prove the following theorem. Assume either that \(P^\pi\) is a singleton for every \(\pi\in\Pi\), or that \(Q^\pi\) is a singleton for every \(\pi\in\Pi\). Then \(J_{\mathcal U}\) is subgradient-dominant with
\[
D=\frac{1}{(1-\gamma)\min_s\mu(s)}.
\]
Moreover, let
\[
\ell=\frac{2\gamma|A|}{(1-\gamma)^3},\qquad
D'=2D\sqrt{|S|}+\frac{\sqrt{|A|}}{2\ell(1-\gamma)^2},
\]
and, for any integer \(T\ge1\), run projected subgradient descent
\[
\pi_{t+1}=\operatorname{Proj}_{\Pi}(\pi_t-\eta g_t),\qquad
g_t\in\partial J_{\mathcal U}(\pi_t),\qquad \eta=\frac{1}{\sqrt T},\qquad t=0,\ldots,T-1,
\]
from any \(\pi_0\in\Pi\), with any choice of the indicated subgradients. Then
\[
\min_{0\le t<T}\bigl[J_{\mathcal U}(\pi_t)-J_{\mathcal U}(\pi^*)\bigr]
\le C T^{-1/4},
\quad
C=D'\left(\frac4{1-\gamma}+\frac{4\gamma |A|^2}{(1-\gamma)^7}\right)^{1/2}.
\]
In particular, for fixed model parameters, an \(\varepsilon\)-optimal policy among the generated iterates is obtained within \(O(\varepsilon^{-4})\) updates.
