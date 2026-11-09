# Problem

## Setup

Let \(\mathcal X\) be a Riemannian manifold on which a compact Lie group \(\mathsf G\) acts smoothly, freely, properly, and isometrically. Let \(\mathcal B=\mathcal X/\mathsf G\), equipped with the quotient Riemannian metric, and let \(q:\mathcal X\to\mathcal B\) be the quotient map. For \(x\in\mathcal X\), set
\[
\mathcal V_x=\ker q_{*x},\qquad
\mathcal H_x=\mathcal V_x^\perp,
\]
and let \(\mathsf H_x:T_x\mathcal X\to\mathcal H_x\) be orthogonal projection. The horizontal lift of a vector field \(u\) on \(\mathcal B\) is the horizontal vector field \(\widetilde u\) satisfying \(q_{*x}\widetilde u(x)=u(q(x))\).

Let \(\nabla^{\mathcal X}\) denote the Levi-Civita connection. For a local orthonormal vertical frame \((V_a)_a\), define the quotient vector field \(\kappa\) by
\[
 \kappa(q(x))=q_{*x}\!\left(\sum_a\nabla^{\mathcal X}_{V_a}V_a\right).
\]
The expression is independent of the chosen local vertical orthonormal frame and the representative \(x\) of the orbit. Let \(\widetilde\kappa\) denote its horizontal lift.

For a continuous semimartingale \(Z\) in \(\mathcal X\), horizontal motion means
\[
 \int_0^t\Theta_{Z_r}\circ dZ_r=0
\]
for every smooth one-form \(\Theta\) annihilating \(\mathcal H\) and every \(t\), with the integral understood in the Stratonovich sense. A horizontal lift of a continuous semimartingale \(U\) in \(\mathcal B\), from a specified initial point above \(U_0\), is a horizontal continuous semimartingale \(Z\) with \(q(Z_t)=U_t\).

Use intrinsic diffusion notation for the stochastic equations. If a diffusion noise has unit-scale generator \(A\), the notation \(dZ_t=a_t(Z_t)\,dt+s_t\,dB_t\) means that its generator is \(a_t+s_t^2A\), acting at the current state \(Z_t\). Riemannian Wiener noise has generator \(\tfrac12\Delta\), where \(\Delta\) is the Laplace-Beltrami operator. Horizontally lifted Wiener noise is the noise defined by horizontally lifting unit-speed quotient Wiener process, with the same scaling convention.

All stochastic processes are adapted to a common filtration, all random initial points are measurable at time zero, and any local real Brownian drivers are Brownian motions for that filtration. Let \(b_t\) be a deterministic smooth \(\mathsf G\)-equivariant time-dependent vector field. Let \(s:[0,1]\to\mathbb R\) be deterministic and measurable, with \(\int_0^1s_t^2\,dt<\infty\). Let \(X_t\) solve
\[
 dX_t=b_t(X_t)\,dt+s_t\,dW_t,
\]
where \(W_t\) denotes Riemannian Wiener noise on \(\mathcal X\). Assume \(X_0\) has \(\mathsf G\)-invariant law \(\nu\), and write \(\mu=\mathcal L(X_1)\). Assume that the processes appearing in the stochastic equations are well defined without explosion throughout \([0,1]\).

## Task

Prove the following integrated claim.

The projected process \(Y_t=q(X_t)\) is a diffusion on \(\mathcal B\) satisfying
\[
 dY_t=\left((q_*b_t)(Y_t)-\frac{s_t^2}{2}\kappa(Y_t)\right)dt+s_t\,d\Omega_t,
 \qquad \mathcal L(Y_0)=q_\#\nu,
\]
where \(\Omega_t\) denotes Riemannian Wiener noise on \(\mathcal B\), and \((q_*b_t)(q(x)):=q_{*x}b_t(x)\).

For any time-zero measurable \(\widetilde X_0\) with law \(\nu\) and \(q(\widetilde X_0)=Y_0\) almost surely, let \(\widetilde X_t\) be the horizontal lift of \(Y_t\) from \(\widetilde X_0\). Prove that it satisfies
\[
 d\widetilde X_t=
 \left(\mathsf H_{\widetilde X_t}b_t(\widetilde X_t)
 -\frac{s_t^2}{2}\widetilde\kappa(\widetilde X_t)\right)dt
 +s_t\,d\widetilde W_t,
\]
where \(\widetilde W_t\) denotes horizontally lifted quotient Wiener noise. In particular, \(\widetilde X_t\) has horizontal motion, \(q(\widetilde X_t)=Y_t\) almost surely for all \(t\in[0,1]\), and
\[
 \mathcal L(\widetilde X_1)=\mu.
\]

For the deterministic comparison, instead take \(s_t\equiv0\) and initialize the original and horizontally lifted equations at an arbitrary common fixed point \(x_0\in\mathcal X\) for which both trajectories exist throughout \([0,1]\). No invariant-initial-law requirement is imposed on this fixed-point comparison. Prove
\[
 \int_0^1\!\|\mathsf H_{\widetilde X_t}b_t(\widetilde X_t)\|^2\,dt
 \leq
 \int_0^1\!\|b_t(X_t)\|^2\,dt.
\]
