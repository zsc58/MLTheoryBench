# Problem

## Setup

Fix an origin \(r\) with a finite nonempty set of feasible destinations \(\mathcal J_r\), of size \(n_r\). Its exposure to destination \(j\) is
\[
X_{rj}=(x_r,w_j,d_{rj},h_{rj},v_j),
\]
where these components respectively encode origin context, destination opportunity, pairwise impedance, intervening exposure, and a destination-side local field. Condition throughout on the exposure row \(X_r=(X_{rj})_{j\in\mathcal J_r}\).

Let \((\mathcal U,\mathcal F,\mu)\) be a measure space. Let \(a_r:\mathcal U\to[0,\infty)\) and all filter functions below be measurable. For every destination \(j\), independently of the other destinations, baseline opportunities form a marked Poisson process on \([0,\infty)\times\mathcal U\) with intensity
\[
dt\,a_r(u)\,d\mu(u).
\]
A baseline opportunity with mark \(u\) becomes effective only if it passes four sequential filters having retention probabilities
\[
b(w_j,u),\qquad s(h_{rj},u),\qquad c(v_j),\qquad d(d_{rj}).
\]
Conditional on \(X_r\) and the complete collection of baseline point configurations, including all arrival times and marks at every destination, the filter decisions are independent across stages, baseline points, and destinations. Under this conditioning, the four decisions for a point at destination \(j\) with mark \(u\) are Bernoulli variables with the respective retention probabilities displayed above. Assume that
\[
0<d(d_{rj})c(v_j)
\int_{\mathcal U}a_r(u)s(h_{rj},u)b(w_j,u)\,d\mu(u)<\infty
\]
for every \(j\). For one trip, let \(J_r\) be the destination whose first effective opportunity arrives.

Let \(N_r\) be a nonnegative integer-valued number of trips generated at the origin, with
\[
\mathbb E[N_r\mid X_r]=\rho_r<\infty.
\]
Conditional on \(N_r\) and \(X_r\), the trips make independent selections, each using an independent copy of the mechanism above. Let \(Y_{rj}\) be the number selecting \(j\), and set
\[
\lambda_{rj}=\mathbb E[Y_{rj}\mid X_r].
\]
For \(\tau>0\), let \(I_{n_r}\) be the \(n_r\times n_r\) identity and \(\mathbf1\in\mathbb R^{n_r}\) the all-ones vector, and define
\[
H_r=I_{n_r}-\frac1{n_r}\mathbf1\mathbf1^\top.
\]

## Task

Prove the following integrated theorem. The effective-opportunity process for destination \(j\) has rate
\[
\alpha_{rj}
=d(d_{rj})c(v_j)
\int_{\mathcal U}a_r(u)s(h_{rj},u)b(w_j,u)\,d\mu(u),
\]
and the induced allocation and aggregate mean satisfy
\[
p_{rj}:=\Pr(J_r=j\mid X_r)
=\frac{\alpha_{rj}}{\sum_{k\in\mathcal J_r}\alpha_{rk}}
=\frac{\exp(f_{rj}/\tau)}{\sum_{k\in\mathcal J_r}\exp(f_{rk}/\tau)},
\qquad
f_{rj}:=\tau\log\alpha_{rj},
\qquad
\lambda_{rj}=\rho_rp_{rj}.
\]
Moreover, characterize identifiability exactly: two positive intensity rows induce the same allocation if and only if they differ by a common positive multiplier, equivalently two score rows induce the same allocation if and only if they differ by a common additive constant. Deduce that
\[
\phi_r:=H_rf_r
\]
is the unique zero-mean representative identified by destination-choice behavior, while the production scale \(\rho_r\) is a separate quantity controlling the row total of the mean flow.
