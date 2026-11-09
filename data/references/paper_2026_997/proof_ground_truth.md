# Reference Proof

## Proof Structure

Work on compact subintervals of (0,1), using integral identities so that the interaction schedule need only be measurable. Take expectations in the state equation and in Itô's formula for the control. Differentiate the HJB equation spatially, compute the gradient of the finite quadratic effective potential, and show that the expected control is constant. Endpoint continuity in L1 then determines the affine mean, and self-consistency identifies the guidance.

## Complete Proof

Write
\[
m_t=\mathbb E[X_t],\qquad q_t=\mathbb E[u_t(X_t)]\quad(0<t<1).
\]
All these expectations are finite by the setup.

### 1. Integrated first-mean evolution

For 0<s<t<1, the SDE gives
\[
X_t-X_s=\int_s^t u_r(X_r)\,dr+W_t-W_s.
\]
The assumed integrability permits Fubini's theorem, and the Brownian increment has zero expectation. Therefore
\[
m_t-m_s=\int_s^t q_r\,dr.
\]
In particular, m is locally absolutely continuous on (0,1).

### 2. Stochastic-calculus input and its hypotheses

The standard Itô formula used here is the following: if a deterministic vector field g is twice continuously differentiable in space and locally absolutely continuous in time, with its time derivative locally integrable uniformly on compact spatial sets, then along dX_r=u_r(X_r)dr+dW_r,
\[
g_t(X_t)-g_s(X_s)
=\int_s^t\left[\partial_r g_r+D_xg_r\,u_r+\tfrac12\Delta g_r\right](X_r)\,dr
+\int_s^tD_xg_r(X_r)\,dW_r.
\]
The formula follows from the usual smooth Itô formula by time regularization and spatial localization. It uses time derivatives only almost everywhere. When the drift integrand is integrable and the stochastic integral is a true martingale, taking expectations gives the corresponding integral expectation identity.

Apply this result to g=u. The spatial regularity follows from the three spatial derivatives of J, and the time regularity follows from the stated absolute continuity of its gradient. The displayed integrability assumption in the task controls every drift term, since |(D_xu)u| is at most ||D_xu|| ||u|| and the Laplacian is bounded by a dimension-dependent multiple of ||D_x^2u||. The stochastic integral is a true martingale by assumption. Thus
\[
q_t-q_s=\int_s^t\mathbb E\!\left[\partial_r u_r(X_r)+(u_r(X_r)\!\cdot\nabla)u_r(X_r)+\tfrac12\Delta u_r(X_r)\right]dr.
\]

### 3. Spatial differentiation of the HJB

For almost every r, the HJB is
\[
\partial_rJ_r+\tfrac12\Delta J_r-\tfrac12\|\nabla J_r\|^2+U_r=0,
\qquad u_r=-\nabla J_r.
\]
The stated mixed-derivative regularity permits spatial differentiation. For each coordinate i,
\[
\partial_i\!\left(\tfrac12\|\nabla J_r\|^2\right)
=\sum_j(\partial_jJ_r)(\partial_{ij}J_r)
=\sum_j u_{r,j}\,\partial_j u_{r,i},
\]
where the last equality uses symmetry of the Hessian. Consequently,
\[
-\partial_r u_{r,i}-\tfrac12\Delta u_{r,i}
-\sum_j u_{r,j}\partial_j u_{r,i}+\partial_iU_r=0.
\]
Equivalently,
\[
\partial_r u_r+(u_r\!\cdot\nabla)u_r+\tfrac12\Delta u_r=\nabla U_r
\]
for almost every r. Substitution into the preceding expectation identity yields
\[
q_t-q_s=\int_s^t\mathbb E[\nabla U_r(X_r)]\,dr.
\]
The integrability of this expression follows from its equality to the already integrable drift expression; no separate regularity or derivative of beta is needed.

### 4. Quadratic interaction and self-consistency

For each interior r, finiteness of U_r(0) and 0<beta_r<infinity imply
\[
\int\|y\|^2p_r(y)\,dy<\infty.
\]
Hence the defining integral can be expanded as
\[
U_r(x)=\frac{\beta_r}{2}\left(\|x\|^2-2x\cdot m_r+\int\|y\|^2p_r(y)\,dy\right).
\]
Its spatial gradient is therefore
\[
\nabla U_r(x)=\beta_r(x-m_r).
\]
Taking expectation at X_r gives
\[
\mathbb E[\nabla U_r(X_r)]=\beta_r(\mathbb E[X_r]-m_r)=0.
\]
It follows that q_t=q_s for every pair of interior times. Let b denote this constant vector. The first-mean identity now gives m_t-m_s=(t-s)b, so there is a vector a such that
\[
m_t=a+tb\qquad(0<t<1).
\]
This establishes the mean-acceleration conclusion in integral form, without assuming pointwise second time derivatives.

### 5. Endpoint identification and guidance

The endpoint L1 conditions imply
\[
\|m_t-m_0\|\leq\mathbb E\|X_t-X_0\|\longrightarrow0
\quad(t\downarrow0),
\]
and similarly m_t tends to m_1 as t increases to 1. The endpoint laws give
\[
m_0=\bar x^{(in)},\qquad m_1=\bar x^{(tar)}.
\]
Taking endpoint limits in the affine interior formula yields a=\bar x^{(in)} and b=\bar x^{(tar)}-\bar x^{(in)}. Thus
\[
m_t=(1-t)\bar x^{(in)}+t\bar x^{(tar)}\qquad(0\leq t\leq1).
\]
Finally, the stated self-consistency condition gives nu_t=m_t at every time, proving the requested identity.

## Obligation Closure

The argument explicitly establishes mean evolution, the differentiated HJB relation, the expected quadratic-force cancellation, affineness, and the endpoint passage. Its only stochastic-calculus input is the standard Itô formula stated above, with its hypotheses checked. Existence of the regular self-consistent bridge is an assumption, not an unproved conclusion. No Green-function representation, Gaussian-mixture formula, or specialized external theorem is used. There are no unresolved theorem-critical obligations.
