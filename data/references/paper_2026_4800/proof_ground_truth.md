# Reference Proof

## Proof Structure

1. Use the chain rule in the diagonal parameterization to show that balanced layer squares remain equal, hence each effective coordinate is the Lth power of a common positive layer coordinate.
2. Reduce the layer gradient flow to an effective-weight flow with multiplier \(Lw_i^{2-2/L}\).
3. Prove the Rayleigh quotient gradient is orthogonal to \(w\).
4. Differentiate the sum of powers \(w_i^{2/L}\), use the orthogonality identity, and integrate.

## Complete Proof

Write \(L\) for the number of layers and let \(\partial_i\ell\) denote partial differentiation of the loss with respect to \(w_i\). Derivatives with respect to layer parameters are derivatives of the composite loss \(\ell(w(u))\). Since \(w_i=\prod_{k=1}^L u_i^{(k)}\), the chain rule gives
\[
\frac{\partial}{\partial u_i^{(k)}}\ell(w(u))
=\partial_i\ell(w(u))\prod_{m\ne k}u_i^{(m)}
=\partial_i\ell(w(u))\frac{w_i}{u_i^{(k)}}.
\]
The division is legitimate because the layer coordinates are positive. The layer gradient flow is therefore
\[
\dot u_i^{(k)}=-\partial_i\ell(w)\frac{w_i}{u_i^{(k)}}.
\]
Consequently,
\[
\frac12\frac{d}{dt}(u_i^{(k)})^2
=u_i^{(k)}\dot u_i^{(k)}
=-w_i\partial_i\ell(w),
\]
which is independent of \(k\). Thus the differences \((u_i^{(k)})^2-(u_i^{(m)})^2\) are constant in time. Balanced initialization makes these differences zero initially, so they remain zero. Positivity then gives
\[
u_i^{(1)}=\cdots=u_i^{(L)}=w_i^{1/L}.
\]

Differentiate the product defining \(w_i\) and substitute the layer equations:
\[
\dot w_i
=\sum_{k=1}^L\frac{w_i}{u_i^{(k)}}\dot u_i^{(k)}
=-\partial_i\ell(w)\sum_{k=1}^L\frac{w_i^2}{(u_i^{(k)})^2}
=-Lw_i^{2-2/L}\partial_i\ell(w).
\]

It remains to establish the orthogonality used below. Set \(N(w)=w^TS_ww\) and \(D(w)=w^TS_bw\), so \(\ell=N/D\) on the admissible domain. Symmetry gives \(\nabla N=2S_ww\) and \(\nabla D=2S_bw\). Since \(D\ne0\), the quotient rule yields
\[
\nabla\ell(w)=\frac{2}{D(w)}\bigl(S_ww-\ell(w)S_bw\bigr).
\]
Therefore
\[
w^T\nabla\ell(w)
=\frac{2}{D(w)}\bigl(N(w)-\ell(w)D(w)\bigr)=0,
\]
because \(\ell=N/D\). Equivalently, differentiate \(\ell(\alpha w)=\ell(w)\) at \(\alpha=1\); this identity is defined for nonzero \(\alpha\) when \(D(w)\ne0\).

For each coordinate, positivity permits the power rule, and the effective flow gives
\[
\frac{d}{dt}w_i^{2/L}
=\frac{2}{L}w_i^{2/L-1}\dot w_i
=-2w_i\partial_i\ell(w).
\]
Summing over coordinates,
\[
\frac{d}{dt}\sum_{i=1}^d w_i^{2/L}
=-2\sum_{i=1}^d w_i\partial_i\ell(w)
=-2w^T\nabla\ell(w)=0.
\]
The sum is therefore constant on every finite interval of the assumed global trajectory. By the definition in the task,
\[
\|w(t)\|_{2/L}^{2/L}=\|w(0)\|_{2/L}^{2/L}
\qquad\text{for every }t\ge0.
\]

## Valid Alternative Without Effective-Weight Dynamics

After proving preservation of balance and the orthogonality identity as above, fix any layer \(k\). Balance and positivity imply
\[
\sum_i w_i^{2/L}=\sum_i(u_i^{(k)})^2.
\]
The layer-square derivative already proved gives
\[
\frac{d}{dt}\sum_i(u_i^{(k)})^2
=-2\sum_i w_i\partial_i\ell(w)=0.
\]
This proves the same initial-value identity without deriving a separate equation for \(\dot w_i\).
