# Problem

## Setup

Consider an infinite-horizon discounted Markov decision process with initial-state distribution \(\mu\), discount \(\gamma\in(0,1)\), and one-step cost \(c\) satisfying \(|c(s,a)|\leq c_{\max}\).  For a deterministic policy \(\pi\), write
\[
J^\pi(\mu)=\mathbb E\left[\sum_{t\geq0}\gamma^t c(S_t,A_t)\right].
\]

Let \(\mathcal P\) be a nonempty application-specified class of deterministic policies, and suppose that \(\pi^*\in\mathcal P\) minimizes \(J^\pi(\mu)\) over \(\mathcal P\).  Let \(\Delta(\mathcal P)\) be the full simplex of probability distributions over \(\mathcal P\), and set \(q^*=\delta_{\pi^*}\).

For an integer \(k\geq1\) and \(q\in\Delta(\mathcal P)\), define \(J^{q,k}(\mu)\) as the expected discounted cost of the policy that, at times \(0,k,2k,\ldots\), draws a deterministic policy from \(q\) and executes it for the following \(k\) steps.  Write \(f(q)=J^{q,k}(\mu)\).

Fix a norm \(\|\cdot\|\).  Assume \(f\) is differentiable and \(\beta\)-smooth with respect to this norm, with \(\beta>0\).  Let \(\Phi\) be a differentiable mirror map that is \(\lambda\)-strongly convex with respect to the same norm, with \(\lambda>0\), and define
\[
D_\Phi(x,y)=\Phi(x)-\Phi(y)-\langle\nabla\Phi(y),x-y\rangle.
\]
Starting from \(q_0\in\Delta(\mathcal P)\), set \(\eta=\lambda/\beta\). Assume that every minimization in the following recursion attains its minimum, and choose, for \(t\geq0\),
\[
q_{t+1}\in\arg\min_{q\in\Delta(\mathcal P)}
\left\{\langle\nabla f(q_t),q\rangle+\eta^{-1}D_\Phi(q,q_t)\right\}.
\]

## Task

Prove that, for every integer \(T\geq1\), the last iterate satisfies
\[
\mathbb E_{\pi\sim q_T}\bigl[J^\pi(\mu)\bigr]-J^{\pi^*}(\mu)
\leq
\frac{8\gamma^k c_{\max}}{1-\gamma}
+\frac{\beta}{\lambda T}D_\Phi(q^*,q_0).
\]
