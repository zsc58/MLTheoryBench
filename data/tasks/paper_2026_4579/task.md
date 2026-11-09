# Problem

## Setup

Consider a finite discounted Markov decision process with nonempty finite state and action sets \(\mathcal X\) and \(\mathcal U\), transition probabilities \(P(x'\mid x,u)\), discount factor \(\gamma\in(0,1)\), and bounded one-step cost \(c\). Let \(Q^\star\) be its optimal action-value function. Let \(c^\diamond\) be a second bounded cost on the same MDP, with the same discount factor, and let \(Q^\diamond\) be its optimal action-value function.

Use the realizable class
\[
Q^\theta(x,u)=\theta^\top\psi(x,u),\qquad
\psi(x,u)=(Q^\star(x,u),Q^\diamond(x,u))\in\mathbb R^2,
\qquad \theta\in\mathbb R^2.
\]
Thus \(\theta^\star=(1,0)\) represents \(Q^\star\). Let \(\phi^\theta(x)\) minimize \(Q^\theta(x,\cdot)\), with a fixed tie-breaking rule.

Fix a probability mass function \(\nu\) on \(\mathcal U\). For \(\kappa>0\) and \(0\le\epsilon\le1\), define
\[
\kappa_\theta=\frac{\kappa}{\sqrt{1+\|\theta\|^2}},\qquad
\pi_{\kappa,\epsilon}^\theta(u\mid x)
=(1-\epsilon)
\frac{\exp(-\kappa_\theta Q^\theta(x,u))}
{\sum_{v\in\mathcal U}\exp(-\kappa_\theta Q^\theta(x,v))}
+\epsilon\nu(u).
\]
Assume that, for every \(\theta\in\mathbb R^2\), the deterministic policy \(\phi^\theta\) and each of these randomized policies induce unique invariant state-action distributions.

For a stationary policy \(\pi\) with invariant state-action distribution \(d_\pi\), define
\[
\bar f_\pi(\theta)=\mathbb E_\pi\!\left[
\psi(X,U)\left(-Q^\theta(X,U)+c(X,U)
+\gamma\min_{v\in\mathcal U}Q^\theta(X',v)\right)
\right],
\qquad
R_\pi=\mathbb E_\pi[\psi(X,U)\psi(X,U)^\top],
\]
where \((X,U)\sim d_\pi\) and, conditionally on \((X,U)\), the next state \(X'\) has law \(P(\cdot\mid X,U)\). A zero of the mean field is a projected Bellman equation solution. Write
\[
\bar f_0(\theta)=\bar f_{\phi^\theta}(\theta),\qquad
\bar f_{\kappa,\epsilon}(\theta)=\bar f_{\pi_{\kappa,\epsilon}^\theta}(\theta).
\]

Assume that the state-action chain under the policy \(\pi_\nu(u\mid x)=\nu(u)\) has exactly one closed recurrent class, that this class is aperiodic, and that \(R_{\pi_\nu}\) is positive definite.

Suppose there is \(\beta^\diamond>0\) such that, with \(\theta^\diamond=(0,\beta^\diamond)\),
\[
\bar f_0(\theta^\diamond)=0.
\]
Assume that the greedy action is unique at every state for both \(\theta^\star\) and \(\theta^\diamond\), and that \(R_{\phi^{\theta^\star}}\) and \(R_{\phi^{\theta^\diamond}}\) are full rank.

On neighborhoods where the greedy action is unique, define epsilon-greedy exploration by
\[
\pi_{\infty,\epsilon}^\theta(u\mid x)
=(1-\epsilon)\mathbf 1\{u=\phi^\theta(x)\}+\epsilon\nu(u).
\]
Use \(\bar f_{\infty,\epsilon}\) for its stationary mean field wherever the invariant distribution is unique. All norms on parameter vectors below are Euclidean.

## Task

Prove that there exist \(\epsilon_\gamma\in(0,1)\), \(b_0>0\), and finite thresholds \(\kappa_{\epsilon,\gamma}>0\) such that, for every \(0<\epsilon<\epsilon_\gamma\) and every \(\kappa\ge\kappa_{\epsilon,\gamma}\), the mean field \(\bar f_{\kappa,\epsilon}\) has a zero \(\theta^t\) satisfying
\[
\|\theta^t-\theta^\diamond\|\le b_0\left(\epsilon+\frac1\kappa\right),
\]
and both \(\theta^\star\) and \(\theta^t\) are locally asymptotically stable equilibria of
\[
\dot\theta=\bar f_{\kappa,\epsilon}(\theta),
\]
with Hurwitz Jacobians, meaning that every eigenvalue has strictly negative real part.

The constants may depend on the fixed MDP, costs, discount factor, exploration pmf, and \(\beta^\diamond\), but \(b_0\) and \(\epsilon_\gamma\) must be independent of \(\epsilon\) and \(\kappa\).

Prove the same conclusion for epsilon-greedy exploration, interpreted as \(\kappa=\infty\) and \(1/\kappa=0\), including local well-definedness of its stationary mean field near the two equilibria.
