# Reference Proof

## Proof Structure

Establish the well-defined quotient geometry, compute the generator on functions constant along the group orbits, and construct the horizontal lift using compatible initial data and horizontal Stratonovich directions. Establish invariance of both total-space laws and prove that invariant probability laws are determined by their quotient pushforwards. Finally compare the deterministic speeds by orthogonal decomposition.

## Audited Standard Background

The following standard independent results are used with their indicated hypotheses.

1. A smooth, free, proper, isometric Lie-group action makes the quotient a smooth Riemannian manifold and its projection a Riemannian submersion. These are exactly the geometric assumptions of the task.
2. For a Riemannian submersion, every quotient vector field has a unique smooth horizontal lift. If \(E_i\) is the horizontal lift of \(e_i\), then
\[
 \mathsf H\nabla^{\mathcal X}_{E_i}E_i
 =\widetilde{\nabla^{\mathcal B}_{e_i}e_i}.
\]
The task supplies the smooth orthogonal horizontal distribution, so these identities apply.
3. A local Stratonovich equation with drift \(A_0\) and real Brownian diffusion fields \(A_i\) has generator \(A_0+\tfrac12\sum_iA_i^2\). The corresponding test-function identities are local martingale identities; stopping in relatively compact charts justifies their use without global boundedness assumptions. Smooth spatial SDE coefficients have local existence and uniqueness up to explosion. This remains applicable to the time dependence here: in coordinates the drift and its local spatial Lipschitz bounds are bounded by a constant times \(1+s_t^2\), while diffusion coefficients and their local spatial Lipschitz bounds are bounded by a constant times \(|s_t|\). The required time integrals are finite. Localization and nonexplosion give uniqueness in law on the stated interval. No strict ellipticity is required.
4. For a smooth principal-bundle connection, an adapted continuous quotient semimartingale and a time-zero measurable initial point in its initial fiber have a unique horizontal semimartingale lift, up to its lifetime. The task supplies exactly this initial-fiber compatibility and assumes the relevant lifetimes contain \([0,1]\).

These are the standard geometric and stochastic facts recorded in theory_002, theory_009, theory_010, and theory_012. No paper-specific external theorem is used to close a remaining obligation.

## Complete Proof

### 1. Geometric well-definedness and the projected generator

The group action preserves the vertical spaces because \(q\circ L_g=q\), and preserves their orthogonal complements because it is isometric. Thus the horizontal projection is equivariant. The uniqueness of the Levi-Civita connection also implies its naturality under these isometries.

Set
\[
 K(x)=\mathsf H_x\sum_a\nabla^{\mathcal X}_{V_a}V_a.
\]
To check independence of the vertical orthonormal frame, write another such frame as \(V'_a=\sum_bO_{ab}V_b\), with \(O\) orthogonal. Expanding the connection trace gives
\[
 \sum_a\nabla_{V'_a}V'_a
 =\sum_b\nabla_{V_b}V_b
   +\sum_{a,b,c}O_{ab}V_b(O_{ac})V_c.
\]
The last term is vertical, so its horizontal projection vanishes. Hence \(K\) is a well-defined smooth horizontal vector field. Transporting the frame by a group isometry shows
\[
 K(gx)=(L_g)_{*x}K(x).
\]
Consequently \(q_*K\) is independent of the representative of an orbit; it is precisely \(\kappa\), and \(K=\widetilde\kappa\). Equivariance of \(b_t\) similarly gives a well-defined quotient vector field \(q_*b_t\), whose horizontal lift is \(\mathsf H b_t\).

Let \(u\in C^\infty(\mathcal B)\) and \(\bar u=u\circ q\). Work locally, with a quotient orthonormal frame \((e_i)_{i=1}^{m}\), where \(m=\dim\mathcal B\), and its horizontal lifts \((E_i)_{i=1}^{m}\). Complete these by a local orthonormal vertical frame \((V_a)\). Choosing the horizontal fields as lifts of quotient fields ensures that they are projectable.

The frame formula for the Laplacian gives
\[
 \Delta^{\mathcal X}\bar u
 =\sum_i\left(E_i^2\bar u-(\nabla^{\mathcal X}_{E_i}E_i)\bar u\right)
  +\sum_a\left(V_a^2\bar u-(\nabla^{\mathcal X}_{V_a}V_a)\bar u\right).
\]
Here \(V_a\bar u=0\), while \(E_i\bar u=(e_i u)\circ q\). The submersion connection identity identifies the horizontal connection terms with the quotient connection terms. The remaining vertical connection trace contributes \(-\kappa u\). Therefore
\[
 \Delta^{\mathcal X}(u\circ q)
 =\left(\Delta^{\mathcal B}u-\kappa u\right)\circ q.
\]
The original intrinsic equation has generator
\[
 L_t=b_t+\frac{s_t^2}{2}\Delta^{\mathcal X},
\]
so
\[
 L_t(u\circ q)
 =\left[(q_*b_t)u+\frac{s_t^2}{2}\left(\Delta^{\mathcal B}u-\kappa u\right)\right]\circ q.
\]
Applying the localized martingale identities shows that \(Y=q(X)\) has generator
\[
 \bar L_t=q_*b_t-\frac{s_t^2}{2}\kappa
              +\frac{s_t^2}{2}\Delta^{\mathcal B}.
\]
Local uniqueness identifies the associated quotient diffusion, and the intrinsic noise convention gives the claimed quotient equation. Its initial law is \(q_\#\nu\).

### 2. Horizontal lift and its precise noise convention

Write
\[
 a_t=q_*b_t-\frac{s_t^2}{2}\kappa,
 \qquad
 C_i=\widetilde{\nabla^{\mathcal B}_{e_i}e_i}
     =\mathsf H\nabla^{\mathcal X}_{E_i}E_i.
\]
Locally, the quotient diffusion can be represented as
\[
 dY_t=\left(a_t-\frac{s_t^2}{2}\sum_{i=1}^{m}\nabla^{\mathcal B}_{e_i}e_i\right)(Y_t)\,dt
       +\sum_{i=1}^{m}e_i(Y_t)\circ dM_t^i,
\]
where \(M_t^i=\int_0^t s_r\,d\beta_r^i\) for local real Brownian drivers, and
\[
 d[M^i,M^j]_t=\delta_{ij}s_t^2\,dt.
\]
Using \(M^i\) as the integrators avoids requiring differentiability or finite variation of the deterministic function \(s\).

Horizontally lifting this equation from the specified compatible \(\widetilde X_0\) yields
\[
 d\widetilde X_t=
 \left(\mathsf H b_t-\frac{s_t^2}{2}\widetilde\kappa
       -\frac{s_t^2}{2}\sum_{i=1}^{m}C_i\right)(\widetilde X_t)\,dt
 +\sum_{i=1}^{m}E_i(\widetilde X_t)\circ dM_t^i.
\]
Every displayed Stratonovich direction, including the connection correction in the drift, is horizontal. Therefore every smooth one-form \(\Theta\) annihilating \(\mathcal H\) has
\[
 \int_0^t\Theta_{\widetilde X_r}\circ d\widetilde X_r=0.
\]
Pushing the equation through \(q\), using the Stratonovich chain rule and \(q(\widetilde X_0)=Y_0\), recovers the equation for the given \(Y\). Equivalently, this construction is the unique horizontal semimartingale lift. Thus its projection equals \(Y\) pathwise, not merely in distribution. Local constructions agree on overlaps by uniqueness and extend over the stated lifetime.

The unit-speed horizontal lift of quotient Wiener process has local generator
\[
 A^{\mathrm h}=\frac12\sum_{i=1}^{m}\left(E_i^2-C_i\right).
\]
This expression follows by horizontally lifting the local Wiener equation with drift \(-\tfrac12\sum_i\nabla^{\mathcal B}_{e_i}e_i\). Consequently the lifted diffusion has generator
\[
 \widetilde L_t
 =\mathsf H b_t-\frac{s_t^2}{2}\widetilde\kappa+s_t^2A^{\mathrm h}.
\]
By the specified intrinsic convention this is exactly
\[
 d\widetilde X_t=
 \left(\mathsf H_{\widetilde X_t}b_t(\widetilde X_t)
       -\frac{s_t^2}{2}\widetilde\kappa(\widetilde X_t)\right)dt
       +s_t\,d\widetilde W_t.
\]
Only the \(m\) horizontal diffusion directions occur. Including the remaining vertical frame directions would contradict both this generator and horizontality; this is the local source-indexing repair recorded for theory_004.

### 3. Invariance and equality of endpoint laws

For each fixed \(g\in\mathsf G\), isometry implies that the Laplace-Beltrami operator commutes with the action. Together with equivariance of \(b_t\), this makes the original diffusion operator equivariant. Hence \(gX\) solves the same intrinsic equation with initial law \((L_g)_\#\nu=\nu\). Uniqueness in law gives
\[
 (L_g)_\#\mathcal L(X_t)=\mathcal L(X_t).
\]

The lifted equation is equivariant as well. The horizontal projection and \(\widetilde\kappa\) are equivariant by step 1. Each \(E_i\) is the unique horizontal lift of a quotient vector field and therefore is equivariant, as is each \(C_i\). Thus \(A^{\mathrm h}\) and \(\widetilde L_t\) commute with the action. Since \(\widetilde X_0\) has invariant law, uniqueness in law gives
\[
 (L_g)_\#\mathcal L(\widetilde X_t)=\mathcal L(\widetilde X_t).
\]
This argument uses equivariance of the lifted coefficients, not the invalid general implication that horizontality alone guarantees equivariance. Compatible initialization is at time zero and the drivers are Brownian for the same filtration; no dependence on future noise is permitted or used.

For completeness, prove directly that an invariant probability law is determined by its quotient pushforward. A compact Lie group admits a normalized bi-invariant probability measure \(\lambda\): choose an inner product on its Lie algebra, extend it by left translations, and normalize the resulting finite Riemannian volume density. This density is left invariant. A right translate of it is another left-invariant smooth density, hence a constant multiple because a left-invariant density is determined at the identity. Its total mass is still one, so the multiple is one. This also covers disconnected compact groups, and in dimension zero gives normalized counting measure.

For \(\varphi\in C_b(\mathcal X)\), define
\[
 A\varphi(x)=\int_{\mathsf G}\varphi(gx)\,\lambda(dg).
\]
Compactness and continuity show that \(A\varphi\) is continuous and bounded. Right invariance of \(\lambda\) makes \(A\varphi\) constant on each orbit, so it descends to a bounded continuous function \(\psi\) on \(\mathcal B\), with \(A\varphi=\psi\circ q\). If \(\rho\) is an invariant probability law, Fubini's theorem gives
\[
 \int_{\mathcal X}\varphi\,d\rho
 =\int_{\mathcal X}A\varphi\,d\rho
 =\int_{\mathcal B}\psi\,d(q_\#\rho).
\]
Thus invariant probability laws with equal quotient pushforwards agree on all bounded continuous test functions and therefore agree as Borel probability measures on the manifold. No density or choice of almost-everywhere orbit disintegrations is required.

Both total-space laws just proved invariant have quotient law \(\mathcal L(Y_t)\). Applying this result at \(t=1\) gives
\[
 \mathcal L(\widetilde X_1)=\mathcal L(X_1)=\mu.
\]

### 4. Deterministic comparison

For this part take \(s\equiv0\) and a fixed common initial point \(x_0\), without an invariant-law requirement. The two equations are
\[
 \dot X_t=b_t(X_t),\qquad
 \dot{\widetilde X}_t=\mathsf H_{\widetilde X_t}b_t(\widetilde X_t).
\]
Their projections solve the same smooth quotient ODE with the same initial point. ODE uniqueness gives \(q(X_t)=q(\widetilde X_t)\). Thus for each \(t\) there is \(g_t\in\mathsf G\) with \(X_t=g_t\widetilde X_t\). No differentiability of the choice \(g_t\) is needed. Equivariance and isometry imply
\[
 \|b_t(X_t)\|=\|b_t(\widetilde X_t)\|.
\]
Orthogonality at \(\widetilde X_t\) gives
\[
 \|b_t(\widetilde X_t)\|^2
 =\|\mathsf H b_t(\widetilde X_t)\|^2
  +\|(I-\mathsf H)b_t(\widetilde X_t)\|^2
 \geq\|\mathsf H b_t(\widetilde X_t)\|^2.
\]
Integration proves the requested inequality. Smoothness and existence throughout the closed interval ensure finiteness of these deterministic energies along each trajectory.

## Boundary Cases and Obligation Closure

No argument divides by \(s_t\), so vanishing diffusion coefficients, including the entirely deterministic case, are covered. Zero-dimensional vertical or horizontal spaces are handled by empty sums. Finite, disconnected, and trivial compact groups are permitted. The curvature is the unnormalized vertical trace, with no division by orbit dimension. All stochastic assertions are on the stipulated nonexplosive interval. Every theorem-critical obligation above is derived or reduced to the explicitly stated standard independent background; no unresolved private ground-truth obligation remains.
