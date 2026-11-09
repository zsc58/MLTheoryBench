# Reference Proof

## Proof Structure

Differentiate the local invariance identity along continuous augmentation curves and extend the resulting annihilation property to their span. This identifies null directions of the pullback metric. Then identify the actual augmentation sensitivities, compose them by the chain rule, and use the normalized parameter-space Jacobian-Gram representation of Fisher information.

## Complete Proof

Fix the point \(z\), and write \(J_h=D h(z)\). Let \(\alpha\) be any differentiable parameter curve through \(0\), and set
\[
v_\alpha=\left.\frac{d}{dt}\right|_{t=0}A(z,\alpha(t)).
\]
For all sufficiently small \(t\), continuity of \(\alpha\) and exact local invariance give
\[
h(A(z,\alpha(t)))=h(z).
\]
Since \(A(z,0)=z\), differentiating at \(t=0\) and applying the chain rule yields
\[
J_h v_\alpha=0.
\]
Every element of \(V_{\mathrm{aug}}(z)\) is a finite linear combination of such generating velocities. The linearity of \(J_h\) therefore proves
\[
V_{\mathrm{aug}}(z)\subseteq\ker J_h.
\]
For every \(v\in V_{\mathrm{aug}}(z)\), it follows that
\[
G(z)v=J_h^\top J_hv=0,
\qquad
v^\top G(z)v=\|J_hv\|^2=0.
\]
Thus every nonzero augmentation direction is a null direction of the pullback metric, and \(G(z)\) is singular whenever the augmentation-tangent space is nonzero. If that space is zero, the inclusion and quadratic-form statement remain valid but do not assert global singularity.

For the information claim, let
\[
S_z=D_\xi A(z,0),\qquad
S_h=\left.D_\xi\bigl[h(A(z,\xi))\bigr]\right|_{\xi=0}.
\]
For every generating curve, the chain rule gives
\[
v_\alpha=S_z\alpha'(0).
\]
Conversely, for every \(a\in\mathbb R^m\), the curve \(\alpha(t)=ta\) lies in \(U\) for sufficiently small \(t\) and has augmentation velocity \(S_za\). Consequently,
\[
\operatorname{col}(S_z)=V_{\mathrm{aug}}(z),
\qquad
\operatorname{rank}(S_z)=\dim V_{\mathrm{aug}}(z).
\]
Applying the chain rule to the definition of \(S_h\) gives
\[
S_h=J_hS_z.
\]
The kernel inclusion already proved shows that every column of \(S_z\) is annihilated by \(J_h\), hence \(S_h=0\).

Under the stipulated normalized local Fisher-information approximation,
\[
I_z=S_z^\top S_z,\qquad I_h=S_h^\top S_h.
\]
For any real matrix \(S\) and any vector \(a\) in its domain,
\[
a^\top S^\top Sa=\|Sa\|^2.
\]
Thus \(\ker(S^\top S)=\ker(S)\): one inclusion follows immediately from \(Sa=0\), and the other follows from the displayed identity. Since \(S\) and \(S^\top S\) have the same domain, rank-nullity gives
\[
\operatorname{rank}(S^\top S)=\operatorname{rank}(S).
\]
Therefore
\[
\operatorname{rank}(I_h)=0,
\qquad
\operatorname{rank}(I_z)=\dim V_{\mathrm{aug}}(z).
\]
In particular,
\[
\operatorname{rank}(I_h)
\leq \operatorname{rank}(I_z)-\dim V_{\mathrm{aug}}(z),
\]
as required. The information claim assumes \(\dim V_{\mathrm{aug}}(z)>0\), so the backbone information has positive rank while the head information has rank zero.
