# Reference Proof

## Proof Obligations

1. Verify well-definedness of the losses, the inner minimizer, and the expectations in the conclusion.
2. Differentiate the centered variance and identify its gradient in the common Hilbert space.
3. Compute the inner functional Hessian and solve the adjoint equation.
4. Justify the mixed parameter derivative using exactly the stated interchange assumptions.
5. Derive the task-specific adjoint sensitivity identity from differentiated inner stationarity, rather than citing the external functional framework.
6. Compute the direct derivative and assemble the claimed total gradient, including the case alpha = 0.

## Complete Proof

Write \(Q=P_{A,\mathrm{in}}=P_{A,\mathrm{out}}\), and use \(\langle\cdot,\cdot\rangle_H\) for the inner product on \(H=L^2(Q)\). All population laws and \(\alpha\) are fixed when differentiating in \(\omega\).

### 1. Well-definedness and the inner minimizer

The stated second moments and Cauchy–Schwarz imply that both losses are finite for every \(h\in H\), that \(\mu(h)\) is finite, and that every product appearing in the claimed gradient is integrable. In particular,
\[
\mathbb E_{P_{\mathrm{in}}}[|h(A)|\,\|\nabla_\omega f_\omega(X)\|]
\leq \|h\|_H\big(\mathbb E_{P_{\mathrm{in}}}\|\nabla_\omega f_\omega(X)\|^2\big)^{1/2}.
\]
The analogous estimate applies to \(f_\omega(X)-Y\) under \(P_{\mathrm{out}}\).

For completeness, fix \(\omega\) and put \(J(h)=L_{\mathrm{in}}(\omega,h)\). Its infimum \(m\) is finite and nonnegative because \(J(0)<\infty\). A direct quadratic expansion gives
\[
J\!\left(\frac{h+k}{2}\right)
=\frac{J(h)+J(k)}2-\frac14\|h-k\|_H^2.
\]
Thus a minimizing sequence \((h_n)\) satisfies
\[
\|h_n-h_m\|_H^2\leq2J(h_n)+2J(h_m)-4m,
\]
and is Cauchy. Completeness of \(H\) and continuity of \(J\) give a minimizer. Applying the same identity to two minimizers shows that they agree in \(H\), hence almost everywhere. This verifies the minimizer used in the setup.

### 2. Centered variance derivative

Define
\[
V(h)=\mathbb E_Q[(h-\mu(h))^2].
\]
For \(\delta\in H\), linearity of the mean gives the exact expansion
\[
V(h+\delta)=V(h)+2\mathbb E_Q[(h-\mu(h))(\delta-\mathbb E_Q\delta)]
+\mathbb E_Q[(\delta-\mathbb E_Q\delta)^2].
\]
Since \(\mathbb E_Q[h-\mu(h)]=0\), the linear term is \(2\mathbb E_Q[(h-\mu(h))\delta]\). The remainder is at most \(\|\delta\|_H^2\). Consequently this is a Fréchet derivative, and
\[
D_hL_{\mathrm{out}}(\omega,h)[\varphi]
=2\alpha\langle h-\mu(h),\varphi\rangle_H,
\qquad
\partial_hL_{\mathrm{out}}(\omega,h)=2\alpha(h-\mu(h)).
\]
Equality of the two A-marginals is what permits this representation in the same Hilbert space as the inner problem.

### 3. Inner Hessian and adjoint

Another exact quadratic expansion yields
\[
D_hL_{\mathrm{in}}(\omega,h)[\varphi]
=-2\mathbb E_{P_{\mathrm{in}}}[(f_\omega(X)-h(A))\varphi(A)],
\]
\[
D^2_{hh}L_{\mathrm{in}}(\omega,h)[\psi,\varphi]
=2\langle\psi,\varphi\rangle_H.
\]
Thus the Hessian operator is \(2I\). At the inner minimizer, the adjoint equation becomes
\[
2a^*_\omega=-2\alpha(h^*_\omega-\mu_\omega).
\]
Its solution is
\[
a^*_\omega=-\alpha(h^*_\omega-\mu_\omega)\quad\text{in }H,
\]
which is the required almost-everywhere formula. The right-hand side belongs to \(H\), and the operator \(2I\) is invertible.

### 4. Parameter derivatives and differentiated stationarity

Fix \(\omega\in U\), write \(g_\omega(X)=\nabla_\omega f_\omega(X)\), and let \(v\in\mathbb R^d\). The stipulated interchange for the prediction-error term gives
\[
D_\omega L_{\mathrm{out}}(\omega,h)[v]
=2\mathbb E_{P_{\mathrm{out}}}[(f_\omega(X)-Y)g_\omega(X)^\top v]
\]
when \(h\) is held fixed.

We next justify differentiation of the inner first variation without assuming any additional interchange. For a fixed \(\varphi\in H\),
\[
2\mathbb E_{P_{\mathrm{in}}}[f_\omega(X)\varphi(A)]
=L_{\mathrm{in}}(\omega,0)+\|\varphi\|_H^2-L_{\mathrm{in}}(\omega,\varphi).
\]
Both parameter-dependent terms on the right satisfy the public interchange assumption. Differentiating them and cancelling gives
\[
D_\omega\mathbb E_{P_{\mathrm{in}}}[f_\omega(X)\varphi(A)][v]
=\mathbb E_{P_{\mathrm{in}}}[(g_\omega(X)^\top v)\varphi(A)].
\]
It follows that the mixed derivative contracted with any fixed \(a\in H\) is
\[
\partial^2_{\omega h}L_{\mathrm{in}}(\omega,h)[a]
=-2\mathbb E_{P_{\mathrm{in}}}[a(A)g_\omega(X)].
\]

First-order optimality of the unconstrained inner minimizer gives, for every \(\varphi\in H\),
\[
\mathbb E_{P_{\mathrm{in}}}[f_\omega(X)\varphi(A)]
=\langle h^*_\omega,\varphi\rangle_H.
\]
Set \(w_v=Dh^*_\omega[v]\in H\), which exists by the explicit inner-solution regularity assumption. Differentiating this scalar stationarity identity using the preceding calculation yields
\[
\langle w_v,\varphi\rangle_H
=\mathbb E_{P_{\mathrm{in}}}[(g_\omega(X)^\top v)\varphi(A)]
\quad\text{for every }\varphi\in H.
\]
This is the required linearized inner optimality equation. It also shows that the mixed derivative is consistent with differentiation of the H-valued inner gradient: stationarity implies \(\partial_hL_{\mathrm{in}}(\omega,h)=2(h-h^*_\omega)\).

### 5. Derivation of the adjoint identity and assembly

The variance expansion in Section 2, together with Fréchet differentiability of \(h^*_\omega\), gives
\[
DF(\omega)[v]
=2\mathbb E_{P_{\mathrm{out}}}[(f_\omega(X)-Y)g_\omega(X)^\top v]
+2\alpha\langle h^*_\omega-\mu_\omega,w_v\rangle_H.
\]
By the solved adjoint equation, the last term is \(-2\langle a^*_\omega,w_v\rangle_H\). In the linearized stationarity equation, choose the test function \(\varphi=a^*_\omega\) at the fixed evaluation parameter. This gives
\[
-2\langle a^*_\omega,w_v\rangle_H
=-2\mathbb E_{P_{\mathrm{in}}}[a^*_\omega(A)g_\omega(X)^\top v]
=v^\top\partial^2_{\omega h}L_{\mathrm{in}}(\omega,h^*_\omega)[a^*_\omega].
\]
The test function is held fixed during differentiation; no derivative of the adjoint is taken. We have therefore derived, in this setting,
\[
\nabla_\omega F(\omega)
=\partial_\omega L_{\mathrm{out}}(\omega,h^*_\omega)
+\partial^2_{\omega h}L_{\mathrm{in}}(\omega,h^*_\omega)[a^*_\omega],
\]
without relying on the cited external functional-adjoint theorem.

Finally substitute \(a^*_\omega=-\alpha(h^*_\omega-\mu_\omega)\). Since the resulting directional identity holds for every \(v\in\mathbb R^d\),
\[
\nabla_\omega F(\omega)
=2\mathbb E_{P_{\mathrm{out}}}[(f_\omega(X)-Y)\nabla_\omega f_\omega(X)]
+2\alpha\mathbb E_{P_{\mathrm{in}}}[(h^*_\omega(A)-\mu_\omega)\nabla_\omega f_\omega(X)].
\]
No step divides by \(\alpha\) or by a variance. Hence the proof includes \(\alpha=0\), a constant inner solution, and degenerate sensitive-attribute distributions. All listed proof obligations are closed.
