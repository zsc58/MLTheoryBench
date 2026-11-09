# Problem

## Setup

Let \(d\geq 1\), let \(\mathcal C\) be a measurable condition space with a fixed sigma-finite reference measure \(\nu\), and let \((Z,C)\) have a source joint probability density \(P(z,c)\) with respect to \(dz\,\nu(dc)\), where \(z\in\mathbb R^d\). Write
\[
P(c)=\int P(z,c)\,dz,\qquad P(z\mid c)=\frac{P(z,c)}{P(c)}
\]
for conditions with \(0<P(c)<\infty\). Conditional distributions at exceptional conditions may be assigned arbitrarily.

Let \(R:\mathbb R^d\times\mathcal C\to\mathbb R\) be measurable and let \(\tau>0\). Assume that, for \(P(c)\nu(dc)\)-almost every \(c\),
\[
0<A(c):=\mathbb E_{P(z\mid c)}\!\left[\exp\left(R(z,c)/\tau\right)\right]<\infty.
\]
Define the target joint density by
\[
Q(z,c)=P(z,c)\,\frac{\exp(R(z,c)/\tau)}{A(c)}.
\]

Fix \(0<T<\infty\), let \(\mu(dt)=dt/T\) on \([0,T]\), and let \(\lambda:[0,T]\to(0,\infty)\) be a finite-valued measurable function.

For each \(t\in[0,T]\), let \(K_t(dx\mid z)\) be a probability kernel, jointly measurable in \((t,z)\). At time \(t\), under either the source or the target law, draw \(X\) conditionally on \((Z,C)\) using this same kernel, independently of \(C\) given \(Z\):
\[
P(dx\mid z,c,t)=Q(dx\mid z,c,t)=K_t(dx\mid z).
\]
Let \(P_t(dx\mid c)\) and \(Q_t(dx\mid c)\) denote the resulting conditional laws of \(X\). Assume that for \(\mu\)-almost every \(t\), the kernel has a jointly measurable Lebesgue density \(K_t(x\mid z)\). At these times, use the conditional densities
\[
P_t(x\mid c)=\int K_t(x\mid z)P(z\mid c)\,dz,\qquad
Q_t(x\mid c)=\int K_t(x\mid z)Q(z\mid c)\,dz.
\]
Define the source posterior, whenever its denominator is positive and finite, by
\[
P(z\mid x,c,t)=\frac{P(z\mid c)K_t(x\mid z)}{P_t(x\mid c)}.
\]
Write
\[
Q_t(dx,dc)=Q_t(dx\mid c)P(c)\nu(dc).
\]

Assume that, for \(\mu(dt)Q_t(dx,dc)\)-almost every \((t,x,c)\), the following three functions of \(x\) are finite, strictly positive, and differentiable at \(x\):
\[
P_t(x\mid c),\qquad Q_t(x\mid c),\qquad
\mathbb E_{P(z\mid x,c,t)}\!\left[\exp\left(R(z,c)/\tau\right)\right].
\]
Assume their \(x\)-gradients admit finite jointly measurable versions on this full-measure set. All gradients hold \(c\) and \(t\) fixed. Values of the scores and posterior quantities on the exceptional sets may be assigned arbitrarily.

Minimize over all jointly measurable fields \(u:\mathbb R^d\times\mathcal C\times[0,T]\to\mathbb R^d\). Define \(u^*\) as any minimizer of
\[
L(u)=\int\mu(dt)\,\lambda(t)\,\mathbb E_{Q_t(dx,dc)}
\left[\left\|u(x,c,t)-\nabla_x\log Q_t(x\mid c)\right\|^2\right],
\]
where the nonnegative integral is allowed to take the value \(+\infty\).

## Task

Prove that, for \(\mu(dt)Q_t(dx,dc)\)-almost every \((t,x,c)\),
\[
u^*(x,c,t)
=\nabla_x\log P_t(x\mid c)
+\nabla_x\log\mathbb E_{P(z\mid x,c,t)}\!\left[\exp\left(R(z,c)/\tau\right)\right].
\]
In other words, the target score equals the source conditional score plus the gradient of the log posterior expectation of the exponentiated reward, with equality understood up to the null sets inherent in the score-matching objective.
