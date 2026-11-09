# Reference Proof

## Proof obligations

We establish: (1) well-defined measurable state and adjoint trajectories with uniform bounds; (2) the state first variation for feasible convex perturbations; (3) differentiation of the population loss and adjoint cancellation; (4) the finite needle expansion; (5) simultaneous Hamiltonian minimization outside one null set; and (6) stationarity on interior times, without assuming a uniform distance from the boundary.

The continuous integral estimate used below is the following form of Gronwall's inequality: if q is nonnegative and continuous and q(t) <= A + integral_0^t [b q(s)+f(s)] ds, where A,b >= 0 and f is nonnegative and integrable, then q(t) <= A exp(bt) + integral_0^t exp(b(t-s))f(s) ds. In particular, sup q <= exp(bT)(A+||f||_1). Terminal-value estimates follow by reversing time. This is the standard-independent dependency theory_028. Every application below has bounded coefficients and integrable forcing on the finite interval.

## 1. State, loss, and adjoint bounds

The field evaluated at a measurable deterministic control is measurable in time and uniformly Lipschitz in the state on the compact region under consideration. The integral equation therefore has a unique absolutely continuous solution on the prescribed horizon; locally this follows by contraction on intervals whose length times the Lipschitz constant is less than one, and iteration extends the solution along the assumed confined trajectories. Comparing two initial conditions by the integral estimate proves continuous dependence on the initial input. Thus the state is measurable in the input. The same integral-equation argument applies backward to the linear adjoint, whose terminal condition is measurable because the labels are measurable.

Let B_X, B_u, and B_G bound the operator norms of D_XF, D_uF, and DG on their stated compact domains, and put zeta_+=sup_t zeta(t). The rowwise softmax residual has Euclidean norm at most 2. Consequently
\[
\|\nabla_Z\ell(Y,Z)\|_F\le 2/\sqrt L,
\qquad
\|P_T\|_F\le 2B_G/\sqrt L.
\]
The adjoint integral equation gives
\[
\|P_t\|_F\le \|P_T\|_F+\zeta_+B_X\int_t^T\|P_s\|_F\,ds,
\]
so
\[
\sup_{t,x}\|P_t(x)\|_F\le B_P:=\frac{2B_G}{\sqrt L}e^{\zeta_+B_XT}.
\]
All bounds are uniform over inputs in the support of the input law. Compactness and the C1 neighborhood interpretation give uniform first-order Taylor remainders for F and G on the compact domains. The same holds for the terminal function x -> ell(Y,G(x)), uniformly in one-hot label matrices Y, of which there are finitely many. No regularity of the label map beyond measurability is needed: the label remains fixed when a control is perturbed.

## 2. Feasible convex first variation

Fix v in the admissible class satisfying the stated interpolation condition. Write w=v-u*, u^alpha=u*+alpha w, and Delta^alpha=S^{u^alpha}-S*. Compactness of Theta makes w bounded. The state integral equations, state Lipschitzness, and the parameter derivative bound along the feasible parameter segments give
\[
\|\Delta_t^\alpha\|_F\le \zeta_+L_F\int_0^t\|\Delta_s^\alpha\|_F\,ds
+\alpha\zeta_+B_u\int_0^t\|w_s\|\,ds.
\]
Thus sup_{t,x}||Delta_t^alpha||_F=O(alpha). Define
\[
A_t=\zeta(t)D_XF(S_t^*;u_t^*),
\qquad b_t=\zeta(t)D_uF(S_t^*;u_t^*)[w_t].
\]
Uniform C1 Taylor expansion in the state and parameter gives
\[
\dot\Delta_t^\alpha=A_t\Delta_t^\alpha+\alpha b_t+r_t^\alpha,
\qquad
\sup_x\int_0^T\|r_t^\alpha(x)\|_F\,dt=o(\alpha).
\]
The expansions are legitimate even when the compact state set is not convex: sufficiently short segments between nearby points lie in the neighborhoods on which the C1 extensions are defined.

Let Z solve
\[
\dot Z_t=\zeta(t)\bigl[D_XF(S_t^*;u_t^*)Z_t+D_uF(S_t^*;u_t^*)[v_t-u_t^*]\bigr],
\qquad Z_0=0.
\]
Apply the integral estimate to Delta^alpha/alpha-Z. The preceding remainder bound proves uniform convergence to zero over time and initial inputs. This establishes the one-sided directional state derivative, not merely its formal equation.

## 3. Population differentiation and cancellation

For each input, apply the terminal Taylor expansion with its fixed label. The uniform state estimate and uniform terminal remainder give
\[
\left.\frac{d}{d\alpha}J(u^\alpha)\right|_{0+}
=\mathbb E\langle P_T,Z_T\rangle_F.
\]
Equivalently, dominated convergence applies because the difference quotients are uniformly bounded and converge pointwise. The terminal covector is exactly
\[
P_T=DG(S_T^*)^\top\frac1L\bigl(\operatorname{softmax}(G(S_T^*))-Y(X_0)\bigr).
\]
The product rule for absolutely continuous functions and the adjoint equation imply
\[
\frac{d}{dt}\langle P_t,Z_t\rangle_F
=\zeta(t)\langle P_t,D_uF(S_t^*;u_t^*)[v_t-u_t^*]\rangle_F.
\]
Integrating, using Z_0=0, and taking expectation yields
\[
\left.\frac{d}{d\alpha}J(u^\alpha)\right|_{0+}
=\int_0^T\mathbb E\bigl[\zeta(t)\langle P_t,D_uF(S_t^*;u_t^*)[v_t-u_t^*]\rangle_F\bigr]dt.
\]
The integrand is bounded on the product of the finite time interval and the probability space, which justifies Fubini's interchange. Feasibility and convergence in the local-minimality topology imply J(u^alpha)>=J(u*) for sufficiently small positive alpha. The derivative is therefore nonnegative.

## 4. Finite needle expansion

Assume now that the admissible class is all measurable Theta-valued controls and that u* is a strong L1 local minimizer. Fix a in Theta and an interval I of length h, and let u^{I,a} equal a on I and u* elsewhere. Set Delta=S^{u^{I,a}}-S*. If B_F bounds F, then
\[
\|\Delta_t\|_F\le \zeta_+L_F\int_0^t\|\Delta_s\|_F\,ds
+2\zeta_+B_F|I\cap[0,t]|.
\]
Hence sup_{t,x}||Delta_t||_F<=C h, uniformly in a and I. Define
\[
f_t^a=\zeta(t)\bigl[F(S_t^*;a)-F(S_t^*;u_t^*)\bigr].
\]
Decompose the displacement equation as
\[
\dot\Delta_t=A_t\Delta_t+\mathbf1_I(t)f_t^a+r_t.
\]
Here r_t is the sum of the baseline state Taylor remainder and, on I, the correction
\[
\zeta(t)\bigl[F(S_t^*+\Delta_t;a)-F(S_t^*;a)
-F(S_t^*+\Delta_t;u_t^*)+F(S_t^*;u_t^*)\bigr].
\]
Let omega be a uniform modulus for the baseline first-order Taylor remainder, with omega(r)->0 as r->0. The first term is bounded by zeta_+ omega(C h) C h. State Lipschitzness bounds the correction on I by 2 zeta_+ L_F C h. Consequently
\[
\sup_x\int_0^T\|r_t(x)\|_Fdt
\le \zeta_+TC h\,\omega(C h)+2\zeta_+L_FC h^2=o(h).
\]
The terminal Taylor expansion gives
\[
J(u^{I,a})-J(u^*)=\mathbb E\langle P_T,\Delta_T\rangle_F+o(h).
\]
Pair the displacement equation with P. Cancellation of A_t and the uniform bound B_P show
\[
\mathbb E\langle P_T,\Delta_T\rangle_F
=\int_I\mathbb E\langle P_t,f_t^a\rangle_Fdt+o(h).
\]
Thus
\[
J(u^{I,a})-J(u^*)
=\int_I\bigl[\overline H(t,a)-\overline H(t,u_t^*)\bigr]dt+o(h).
\]
The bounds prove the remainder uniformly in a in Theta and in the location of I. This uses the finite difference F(S_t^*;a)-F(S_t^*;u_t^*), not its parameter linearization.

## 5. Localization and a common exceptional set

The L1 distance between the needle control and u* is at most diam(Theta)h. Strong L1 local minimality therefore makes the preceding cost difference nonnegative for sufficiently small h.

For fixed a, the function g_a(t)=overline H(t,a)-overline H(t,u_t^*) is measurable and bounded, hence belongs to L1([0,T]). The Lebesgue differentiation theorem states that for an L1 function the averages over [t,t+h] converge to its value for almost every t in [0,T). Applying it after division of the needle expansion by h gives g_a(t)>=0 almost everywhere.

Choose a countable dense subset D of the compact subset Theta of Euclidean space. Discard the union of the exceptional null sets for a in D, together with any null set needed to choose a Theta-valued representative of u*. For every remaining t, the inequality holds for every a in D. At that fixed t, a -> overline H(t,a) is continuous: F is continuous in a and its product with P is uniformly bounded, so dominated convergence applies. Approximation by D proves the inequality for every a in Theta at every such t. This establishes the simultaneous quantifier order in the task.

## 6. Interior stationarity

Put
\[
g(t)=\zeta(t)\mathbb E\bigl[D_uF(S_t^*;u_t^*)^\top P_t\bigr].
\]
This is a bounded measurable vector-valued function. For each positive integer n, let
\[
E_n=\{t:\operatorname{dist}(u_t^*,\mathbb R^m\setminus\Theta)\ge 1/n\}.
\]
Take any bounded measurable eta vanishing outside E_n. Choose delta>0 with delta||eta||_infinity<1/n. Then v_+=u*+delta eta and v_-=u*-delta eta are admissible, and their one-sided convex interpolations with u* are admissible and converge in L1. Applying the first conclusion to both comparisons gives
\[
\int_{E_n}\langle g(t),\eta_t\rangle\,dt=0.
\]
For each coordinate, test eta equal to the corresponding unit vector times the indicator of an arbitrary measurable subset of E_n. An integrable scalar function whose integral vanishes over every measurable subset is zero almost everywhere: otherwise one of its positive or negative level sets would have a nonzero integral. Thus g=0 almost everywhere on E_n. Taking the countable union proves this on all interior times, since every interior point has positive distance from the complement of Theta. On the subset where zeta(t)>0, division by zeta yields
\[
\mathbb E\bigl[D_uF(S_t^*;u_t^*)^\top P_t\bigr]=0.
\]
Alternatively, differentiability and the established pointwise Hamiltonian minimum give the same interior stationarity directly.

The source's unrestricted signed-support assertion is repaired here by the E_n exhaustion. No uniform interior margin is assumed. If Theta has empty interior, the stationarity statement is vacuous; where zeta=0 no division is made; and for a single output class the softmax residual and adjoint vanish. All proof obligations are closed.
