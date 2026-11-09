# Problem

## Setup

Fix integers \(d\ge1\) and \(n\ge\max\{2,d\}\). Let \(\mathcal X\) be a nonempty closed subset of \(\{x\in\mathbb R^d:\|x\|_2\le1\}\), and let \(\theta_\star\in\mathbb R^d\) be a fixed unknown parameter satisfying \(\|\theta_\star\|_2\le1\).

Let \(\lambda\ge80\), \(\delta\in(0,1/4)\), and let \(m\) be a positive integer satisfying \(m\ge2000d\log(n/\delta)\). Initially draw independent vectors \(\zeta^j\sim N(0,I_d)\), \(1\le j\le m\), and set \(\mathcal H_0=\sigma(\zeta^1,\ldots,\zeta^m)\).

The interaction proceeds sequentially. At round \(t\), draw \(J_t\) uniformly from \(\{1,\ldots,m\}\), independently of \(\mathcal H_{t-1}\). Choose an action \(X_t\in\mathcal X\), measurable with respect to \(\mathcal H_{t-1}\vee\sigma(J_t)\), satisfying
\[
X_t\in\arg\max_{x\in\mathcal X}\langle x,\theta_{t-1}^{J_t}\rangle.
\]
Use any measurable tie-breaking rule based only on the available history, the current index, and the known inputs, not on \(\theta_\star\).

Put \(\mathcal G_t=\mathcal H_{t-1}\vee\sigma(J_t,X_t)\). Observe
\[
Y_t=\langle X_t,\theta_\star\rangle+\eta_t,
\qquad
\mathbb E[e^{s\eta_t}\mid\mathcal G_t]\le e^{s^2/2}
\quad\text{for every }s\in\mathbb R.
\]
After observing \(Y_t\), draw \((\xi_t^1,\ldots,\xi_t^m)\sim N(0,I_m)\), independently of \(\mathcal G_t\vee\sigma(Y_t)\). Define
\[
\mathcal H_t=\mathcal G_t\vee\sigma(Y_t,\xi_t^1,\ldots,\xi_t^m).
\]

For \(t\ge0\), with empty sums interpreted as zero, define
\[
V_t=\lambda I_d+\sum_{s=1}^tX_sX_s^\top,
\qquad
\widehat\theta_t=V_t^{-1}\sum_{s=1}^tX_sY_s,
\]
\[
S_t^j=\sqrt\lambda\,\zeta^j+\sum_{s=1}^tX_s\xi_s^j,
\qquad
\beta_t^\delta=\sqrt\lambda+\sqrt{2\log(1/\delta)+\log\frac{\det V_t}{\lambda^d}},
\]
and
\[
\theta_t^j=\widehat\theta_t+40\beta_t^\delta V_t^{-1}S_t^j.
\]
Define the regret
\[
R_n=\max_{x_\star\in\mathcal X}\sum_{t=1}^n\langle x_\star-X_t,\theta_\star\rangle.
\]

## Task

Prove that there is a universal constant \(C\) such that, with probability at least \(1-4\delta\),
\[
R_n\le C\,\beta_{n-1}^\delta\sqrt{d\log(n/\delta)}\left[\sqrt{dn\log\!\left(1+\frac{n}{d\lambda}\right)}+\sqrt{\left(\frac n\lambda+1\right)\log\!\left(\frac{\sqrt{n/\lambda+1}}{\delta}\right)}\right].
\]
In particular, for \(\lambda=80\) and \(m=\Theta(d\log(n/\delta))\) satisfying the stated lower bound, this is \(\widetilde O(d^{3/2}\sqrt n)\), where the notation suppresses logarithmic factors in \(n\) and \(1/\delta\).
