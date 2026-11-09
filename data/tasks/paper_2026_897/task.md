# Problem

## Setup

Let d>=1, let (E,mathcal E) be a measurable space, and let X_1,X_2,... be i.i.d. E-valued observations. Let phi:E x R^d->R be measurable in its first argument and finite and convex in its second argument. Assume E|phi(X_1,theta)|<infinity for every theta, and write
\[
Phi(theta)=E[phi(X_1,theta)].
\]
Let g:E x R^d->R^d be a jointly measurable subgradient selection: on one event of probability one, g(X_1,theta) is a subgradient of phi(X_1,cdot) at theta for every theta. Let G(theta)=E[g(X_1,theta)] be a well-defined measurable subgradient of Phi.

The stochastic-gradient recursion is
\[
theta_0\in R^d\ \text{fixed},\qquad
theta_k=theta_{k-1}-\frac{delta}{k}g(X_k,theta_{k-1}),\quad k\ge1.
\]
Set F_0 to be the trivial sigma-algebra and F_k=sigma(X_1,...,X_k). Write g(X_k,theta_{k-1})=G(theta_{k-1})+epsilon_k, with E[epsilon_k\mid F_{k-1}]=0.

Assume:

1. Phi has a unique minimizer theta*.
2. Phi is twice continuously differentiable on a neighborhood of theta*, and A:=nabla^2 Phi(theta*) is positive definite; let lambda_1 be its smallest eigenvalue.
3. There is L<infinity such that ||G(theta)||<=L||theta-theta*|| for all theta, and sup_theta E||g(X_1,theta)-G(theta)||^2<infinity.
4. For some open neighborhood U of theta*, the random variable sup_{theta in U}||g(X_1,theta)-G(theta)||^2 is measurable and has finite expectation.
5. delta>1/lambda_1.

Define
\[
Gamma=E[g(X_1,theta*)g(X_1,theta*)^T],\qquad H=delta A-I_d,
\]
and let Q=delta^2 Gamma. For every integer n>=1 and k>=0, set
\[
\widetilde Y_k^n=\frac{k(theta_k-theta*)}{\sqrt n}.
\]
Let Y^n be the continuous piecewise-linear interpolation with Y^n(k/n)=\widetilde Y_k^n, including \widetilde Y_0^n=0, restricted to positive times.

Let B be a standard d-dimensional Brownian motion and define
\[
Y_t=\int_0^t \exp\!\big(\log(s/t)H\big)Q^{1/2}\,dB_s,\qquad t>0,
\]
where Q^{1/2} is the symmetric positive-semidefinite square root and the matrix power is defined by functional calculus.

## Task

Prove that Y^n converges in distribution to Y in C^0((0,infinity),R^d) equipped with the topology of uniform convergence on compact time intervals. Equivalently, prove convergence jointly and compatibly on all compact intervals [eta,T], 0<eta<T<infinity, to the unique law of a continuous adapted solution of
\[
dY_t=-t^{-1}HY_t\,dt+Q^{1/2}dB_t,\qquad Y_t\longrightarrow0\ \text{in probability as }t\downarrow0.
\]
Here the SDE is understood on each compact interval bounded away from zero, and the driving process is Brownian relative to the solution's filtration.
