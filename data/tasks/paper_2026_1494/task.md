# Problem

## Setup

Let \((M,\langle\cdot,\cdot\rangle)\) be a connected, complete smooth Riemannian manifold, with tangent norm \(\|\cdot\|_x\), distance \(d_M\), exponential map \(\operatorname{Exp}_x\), and injectivity radius \(\operatorname{inj}(M)\). For a specified minimizing geodesic from \(x\) to \(y\), write \(\Gamma_x^y\) for parallel transport along that geodesic. Minimizing geodesics need not be unique.

Let \(A\subset M\) be a nonempty compact geodesically convex set of diameter \(D\): every minimizing geodesic joining two points of \(A\) lies in \(A\). Fix an initial point \(x_1\in A\) and a global minimizer \(x^*\in A\) of a differentiable function \(f:M\to\mathbb R\). Assume every iterate appearing below, including \(x_{T+1}\) when \(T\) updates are used, lies in \(A\); for the stochastic iteration this holds almost surely.

A differentiable function is called geodesically convex on \(A\) when its restriction to every minimizing geodesic in \(A\) is convex. Equivalently, its values satisfy the convex interpolation inequality along all such geodesics. In particular, if \(v\in T_xM\) is the initial velocity of a minimizing geodesic \(s\mapsto\operatorname{Exp}_x(sv)\) from \(x\) to \(y\) in \(A\), then
\[
f(y)-f(x)\ge\langle\operatorname{grad}f(x),v\rangle_x.
\]

Let \(G>0\), \(r>0\), and \(L_f,L_\Phi\ge0\) be finite constants. Assume that for every \(x,y\in M\) and every minimizing geodesic joining them,
\[
\|\Gamma_x^y\operatorname{grad}f(x)-\operatorname{grad}f(y)\|_y
\le L_f d_M(x,y),
\qquad
\|\operatorname{grad}f(x)\|_x\le G.
\]

At each iteration \(t\), let \(\widehat R_t:TM\to M\) be a first-order retraction, with restrictions \(\widehat R_{t,x}:T_xM\to M\) satisfying
\[
\widehat R_{t,x}(0)=x,
\qquad D\widehat R_{t,x}(0)=\mathrm{Id}.
\]
For each \(t,x\), assume there is \(0<\rho_{t,x}<\operatorname{inj}(M)\) such that
\[
\widehat R_{t,x}(\{u:\|u\|_x\le r\})
\subseteq\{y:d_M(x,y)\le\rho_{t,x}\}.
\]
Consequently \(\Phi_{t,x}=\operatorname{Exp}_x^{-1}\circ\widehat R_{t,x}\) is defined there using the inverse exponential map on that normal neighborhood. Assume it is twice continuously differentiable for \(\|u\|_x<r\), and satisfies the radial regularity condition
\[
\sup_{s\in[0,1]}
\|D^2\Phi_{t,x}(su)[u,u]\|_x
\le L_\Phi\|u\|_x^2
\qquad(\|u\|_x<r).
\]

The deterministic iteration is
\[
x_{t+1}=\widehat R_{t,x_t}(-\eta\operatorname{grad}f(x_t)).
\]
For the stochastic iteration, let \(\xi_1,\xi_2,\ldots\) be iid oracle samples. Iterates and the retraction chosen at iteration \(t\) depend measurably only on information available before \(\xi_t\) is drawn; this fresh sample is independent of that information. For each fixed \(x\), the measurable oracle output \(\operatorname{grad}f(x,\xi)\in T_xM\) satisfies
\[
\mathbb E[\operatorname{grad}f(x,\xi)]=\operatorname{grad}f(x),
\qquad
\|\operatorname{grad}f(x,\xi)\|_x\le G\quad\text{a.s.},
\]
\[
\mathbb E\|\operatorname{grad}f(x,\xi)-\operatorname{grad}f(x)\|_x^2
\le\sigma^2,
\]
where \(0\le\sigma^2<\infty\) is a fixed bound. Write \(\zeta_t=\operatorname{grad}f(x_t,\xi_t)\). The update is
\[
x_{t+1}=\widehat R_{t,x_t}(-\eta\zeta_t).
\]
The oracle conditions need only hold at the points that can be queried by this stochastic iteration.

The step size is constant within each run and satisfies, respectively,
\[
0<\eta<\min\!\left\{
\frac1{L_\Phi G/2+L_f+L_fL_\Phi^2},\frac2G,\frac rG
\right\}
\]
for the deterministic iteration, and
\[
0<\eta<\min\!\left\{
\frac1{L_\Phi G+2L_f+2L_fL_\Phi^2},\frac2G,\frac rG
\right\}
\]
for the stochastic iteration. A reciprocal with zero denominator is interpreted as \(+\infty\).

## Task

Prove the following integrated convergence theorem for positive integer horizons \(T\). For the deterministic iteration with a fixed admissible step size, in the smooth nonconvex case,
\[
\frac1T\sum_{t=1}^T\|\operatorname{grad}f(x_t)\|_{x_t}^2=O(T^{-1}),
\]
and, if \(f\) is geodesically convex on \(A\),
\[
f(x_T)-f(x^*)=O((\eta T)^{-1}).
\]
For the stochastic iteration, under the oracle assumptions above,
\[
\frac1T\sum_{t=1}^T\mathbb E\|\operatorname{grad}f(x_t)\|_{x_t}^2
=O\!\left(\frac1{\eta T}+\eta\sigma^2\right)
\]
in the nonconvex case, while in the geodesically convex case
\[
\mathbb E[f(x_T)-f(x^*)]
=O\!\left(\frac1{\eta T}+\eta^2T\sigma^2\right).
\]
Consequently, admissible constant-within-run choices \(\eta\asymp T^{-1/2}\) and \(\eta\asymp T^{-2/3}\), with fixed sufficiently small proportionality constants, yield respectively stochastic rates \(O(T^{-1/2})\) and \(O(T^{-1/3})\).

Constants may depend on the geometric, smoothness, boundedness, diameter, variance, and initial-objective parameters, but not on \(T\). Deterministic constants may also depend on the fixed admissible deterministic step size. The two stochastic bounds are to hold with constants uniform over admissible stochastic step sizes, so that the stated horizon-dependent choices are justified. In the specialized rates, constants may also depend on the fixed proportionality constants. All problem parameters other than the chosen stochastic step size remain fixed as the horizon varies.
