# Reference Proof

## Proof Structure

The proof controls the logarithmic displacement of each retraction step, derives deterministic and conditional expected descent, and telescopes these inequalities for the nonconvex conclusions. For the convex conclusions it derives a weighted objective-potential increment, completes a square in a tangent space, and sums the resulting diameter and noise bounds. No geometric displacement telescoping identity is needed.

## Complete Proof

Write \(g_t=\operatorname{grad}f(x_t)\), \(f_*=f(x^*)\), and \(\Delta_1=f(x_1)-f_*\ge0\). Define
\[
K=\frac{L_\Phi G}{2}+L_f+L_fL_\Phi^2.
\]
The stochastic step-size denominator is \(2K\). When \(K=0\), all expressions below remain valid with the corresponding products equal to zero.

### Retraction Displacement

For any update input \(u\) with \(\|u\|_x<r\), first-order retraction properties imply \(\Phi_{t,x}(0)=0\) and \(D\Phi_{t,x}(0)=I\). Taylor's integral formula along the line segment \(su\) gives
\[
\Phi_{t,x}(u)-u
=\int_0^1(1-s)D^2\Phi_{t,x}(su)[u,u]\,ds.
\]
The stated radial regularity therefore implies
\[
\|\Phi_{t,x}(u)-u\|_x\le\frac{L_\Phi}{2}\|u\|_x^2.
\]
Only this radial derivative bound is used.

### Smoothness Along a Minimizing Geodesic

If \(x,y\in A\) and \(w\in T_xM\) is the initial velocity of a minimizing geodesic \(\gamma(s)=\operatorname{Exp}_x(sw)\) from \(x\) to \(y\), then \(\|w\|_x=d_M(x,y)\). Every subsegment is minimizing. Parallel transport is an isometry and transports \(w\) to \(\dot\gamma(s)\). Thus the smoothness assumption gives
\[
\left|\langle\operatorname{grad}f(\gamma(s)),\dot\gamma(s)\rangle
-\langle\operatorname{grad}f(x),w\rangle_x\right|
\le L_f s\|w\|_x^2.
\]
Integrating the derivative of \(f\circ\gamma\) yields
\[
f(y)-f(x)\le\langle\operatorname{grad}f(x),w\rangle_x
+\frac{L_f}{2}\|w\|_x^2.
\]
The retraction logarithm is a minimizing displacement because its endpoint is in the specified normal neighborhood.

### Deterministic Descent and Nonconvex Rate

Set \(d_t=-\operatorname{Exp}_{x_t}^{-1}(x_{t+1})\) and \(e_t=d_t-\eta g_t\). The input lies in the regularity ball since \(\eta G<r\), and
\[
\|e_t\|\le\frac{L_\Phi}{2}\eta^2\|g_t\|^2.
\]
All tangent norms and inner products in a one-step calculation are at \(x_t\). Smoothness, the absolute Cauchy--Schwarz bound on the error inner product, and \(\|a+b\|^2\le2\|a\|^2+2\|b\|^2\) imply
\[
\begin{aligned}
f(x_{t+1})-f(x_t)
&\le-\eta\|g_t\|^2-\langle g_t,e_t\rangle
+\frac{L_f}{2}\|\eta g_t+e_t\|^2\\
&\le-\left(\eta-\frac{L_\Phi G}{2}\eta^2-L_f\eta^2\right)\|g_t\|^2
+\frac{L_fL_\Phi^2}{4}\eta^4\|g_t\|^4.
\end{aligned}
\]
Since \(\eta G<2\), \(\eta^4\|g_t\|^4\le4\eta^2\|g_t\|^2\). Consequently,
\[
f(x_{t+1})-f(x_t)\le-c_d\|g_t\|^2,
\qquad c_d=\eta-K\eta^2>0.
\]
Summing for \(t=1,\ldots,T\), using the existence of the update to \(x_{T+1}\) and \(f(x_{T+1})\ge f_*\), gives
\[
\frac1T\sum_{t=1}^T\|g_t\|^2
\le\frac{\Delta_1}{c_dT}=O(T^{-1})
\]
for fixed admissible deterministic \(\eta\).

### Deterministic Convex Rate

For each \(t\), choose an initial velocity \(v_t\) of a minimizing geodesic from \(x_t\) to \(x^*\). Uniqueness is unnecessary. The diameter and convexity assumptions give
\[
\|v_t\|\le D,
\qquad \Delta_t=f(x_t)-f_*\le-\langle g_t,v_t\rangle.
\]
Define \(E_t=t^2\Delta_t\) and \(a_t=(t+1)^2-t^2=2t+1\). The exact potential identity is
\[
E_{t+1}-E_t=(t+1)^2[f(x_{t+1})-f(x_t)]+a_t\Delta_t.
\]
Therefore
\[
E_{t+1}-E_t
\le-c_d(t+1)^2\|g_t\|^2-a_t\langle g_t,v_t\rangle.
\]
Completing the square gives
\[
\begin{aligned}
-c_d(t+1)^2\|g_t\|^2-a_t\langle g_t,v_t\rangle
&=-c_d(t+1)^2\left\|g_t+\frac{a_t v_t}{2c_d(t+1)^2}\right\|^2
+\frac{a_t^2\|v_t\|^2}{4c_d(t+1)^2}\\
&\le\frac{D^2}{c_d},
\end{aligned}
\]
since \(a_t/(t+1)<2\). Summing for \(t=1,\ldots,T-1\), with an empty sum for \(T=1\), yields
\[
f(x_T)-f_*
\le\frac{\Delta_1}{T^2}+\frac{D^2(T-1)}{c_dT^2}
\le\frac{\Delta_1}{T^2}+\frac{D^2}{c_dT}.
\]
Since \(c_d=\eta(1-K\eta)\), this is \(O((\eta T)^{-1})\) for fixed admissible deterministic \(\eta\). The implicit constant may depend on that fixed step size, as allowed by the replacement statement. No uniformity as \(K\eta\uparrow1\) is claimed.

### Stochastic Conditional Descent

Let \(\mathcal F_t\) contain the information available before sample \(\xi_t\), and write \(\mathbb E_t=\mathbb E[\cdot\mid\mathcal F_t]\). The fresh iid sampling and measurable dependence on previous samples imply
\[
\mathbb E_t\zeta_t=g_t,
\qquad \mathbb E_t\|\zeta_t-g_t\|^2\le\sigma^2.
\]
Define \(d_t=-\operatorname{Exp}_{x_t}^{-1}(x_{t+1})\) and \(e_t=d_t-\eta\zeta_t\). The same Taylor estimate holds almost surely:
\[
\|e_t\|\le\frac{L_\Phi}{2}\eta^2\|\zeta_t\|^2.
\]
Taking conditional expectation in the smoothness inequality gives
\[
\begin{aligned}
\mathbb E_t[f(x_{t+1})-f(x_t)]
&\le-\eta\|g_t\|^2
+\left(\frac{L_\Phi G}{2}+L_f\right)\eta^2\mathbb E_t\|\zeta_t\|^2
+\frac{L_fL_\Phi^2}{4}\eta^4\mathbb E_t\|\zeta_t\|^4.
\end{aligned}
\]
Here the retraction-error inner product is bounded in absolute value using \(\|g_t\|\le G\). The almost-sure bound \(\|\zeta_t\|\le G\) and \(\eta G<2\) imply
\[
\eta^4\mathbb E_t\|\zeta_t\|^4
\le4\eta^2\mathbb E_t\|\zeta_t\|^2.
\]
Thus the second-moment coefficient after absorption is \(K\), not \(2K\):
\[
\mathbb E_t[f(x_{t+1})-f(x_t)]
\le-\eta\|g_t\|^2+K\eta^2\mathbb E_t\|\zeta_t\|^2.
\]
Conditional unbiasedness cancels the cross term in the second-moment expansion, giving
\[
\mathbb E_t\|\zeta_t\|^2
=\|g_t\|^2+\mathbb E_t\|\zeta_t-g_t\|^2
\le\|g_t\|^2+\sigma^2.
\]
It follows that
\[
\mathbb E_t[f(x_{t+1})-f(x_t)]
\le-c_s\|g_t\|^2+K\eta^2\sigma^2,
\qquad c_s=\eta-K\eta^2.
\]
The stochastic restriction \(\eta<1/(2K)\), interpreted as no restriction from this reciprocal when \(K=0\), gives \(c_s\ge\eta/2\). In particular, the constants below are uniform over admissible stochastic step sizes.

### Stochastic Nonconvex Rate

Sum the conditional inequality and apply the tower property. Since \(f(x_{T+1})\ge f_*\),
\[
\frac1T\sum_{t=1}^T\mathbb E\|g_t\|^2
\le\frac{\Delta_1}{c_sT}+\frac{K\eta^2\sigma^2}{c_s}
\le\frac{2\Delta_1}{\eta T}+2K\eta\sigma^2.
\]
This proves the stated nonconvex bound.

### Stochastic Convex Rate

The minimizing-geodesic first-order inequality implies the scalar bound \(\Delta_t\le D\|g_t\|\) on every sample path. Combining this with conditional descent, and completing the scalar square, gives
\[
\begin{aligned}
(t+1)^2\mathbb E_t\Delta_{t+1}-t^2\Delta_t
&\le-c_s(t+1)^2\|g_t\|^2+a_tD\|g_t\|
+(t+1)^2K\eta^2\sigma^2\\
&\le\frac{a_t^2D^2}{4c_s(t+1)^2}
+(t+1)^2K\eta^2\sigma^2\\
&\le\frac{D^2}{c_s}+(t+1)^2K\eta^2\sigma^2.
\end{aligned}
\]
This is also the bound obtained by the tangent-space completion of the square in the deterministic argument. The scalar formulation avoids needing a measurable choice of minimizing geodesic when such geodesics are not unique.

Take expectations and sum for \(t=1,\ldots,T-1\). Because \(\sum_{t=1}^{T-1}(t+1)^2\le T^3\),
\[
\mathbb E[f(x_T)-f_*]
\le\frac{\Delta_1}{T^2}+\frac{D^2(T-1)}{c_sT^2}
+K\eta^2\sigma^2T
\le\frac{\Delta_1}{T^2}+\frac{2D^2}{\eta T}
+K\eta^2\sigma^2T.
\]
Since \(\eta<2/G\) and \(T\ge1\), the initial term satisfies
\[
\frac{\Delta_1}{T^2}\le\frac{2\Delta_1/G}{\eta T}.
\]
This proves \(O((\eta T)^{-1}+\eta^2T\sigma^2)\) with constants independent of the admissible stochastic step size and the horizon.

### Step-Size Specializations and Boundary Cases

Choose a fixed positive \(c\) strictly smaller than the stochastic upper step-size bound. In a run with horizon \(T\ge1\), use the constant step size \(\eta_T=cT^{-1/2}\) for the nonconvex conclusion, or \(\eta_T=cT^{-2/3}\) for the convex conclusion. These choices are admissible for every horizon. Substitution gives respectively
\[
O(c^{-1}T^{-1/2}+c\sigma^2T^{-1/2})=O(T^{-1/2})
\]
and
\[
O(c^{-1}T^{-1/3}+c^2\sigma^2T^{-1/3})=O(T^{-1/3}).
\]
The proportionality constant is fixed independently of \(T\). The preceding inequalities also cover \(\sigma=0\), \(D=0\), \(\Delta_1=0\), and \(T=1\). Positive \(G\) is an upper-bound parameter, so an identically zero gradient causes no division-by-zero issue. If \(K=0\), then \(c_d=c_s=\eta\), and the reciprocal convention in the task makes the same argument applicable. Every theorem-critical obligation has been explicitly derived; no specialized external result is required.
