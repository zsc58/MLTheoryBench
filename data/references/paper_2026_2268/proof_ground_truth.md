# Reference Proof

## Proof Structure and Obligations

We prove the Hausdorff support/value estimates, establish selector-aware translation cancellation and fixed-set objective sensitivity, derive both asymmetric support/value bounds, and control the optimizer term. For the refinement we derive quadratic growth and directional stability directly from the intersection-of-balls definition, then prove cross-set stability. Finally we give an explicit admissible family establishing the diameter-scale obstruction. All obligations are closed below without invoking a specialized external theorem.

## 1. Support and optimal-value estimates

For a nonempty compact set write
\[
F_S(h,c)=\xi_S(c-2h)-z_S^*(c),\qquad
\ell_S^{\mathrm{SPO+}}(h,c)=F_S(h,c)+2h^\top w_S^*(c).
\]
Let \(\delta=d_H(A,B)\). For every \(x\in A\), compactness supplies \(y\in B\) with \(\|x-y\|\le\delta\). Thus
\[
u^\top x\le\xi_B(u)+\|u\|\delta.
\]
Maximizing over \(x\) and interchanging the sets proves
\[
|\xi_A(u)-\xi_B(u)|\le\|u\|\delta.
\]
Since \(z_S^*(c)=-\xi_S(-c)\), also
\[
|z_A^*(c)-z_B^*(c)|\le\|c\|\delta.
\]
These estimates include zero directions and singleton sets.

## 2. Translation and fixed-set objective sensitivity

For a vector \(v\), use an auxiliary translated copy \(S+v\) with the transported selector \(w_v^*(c)=w_S^*(c)+v\). This is an optimizer on that copy. The support and value shifts are
\[
\xi_{S+v}(u)=\xi_S(u)+u^\top v,\qquad
z_{S+v}^*(c)=z_S^*(c)+c^\top v.
\]
Consequently the change in the full loss is
\[
(c-2h)^\top v+2h^\top v-c^\top v=0.
\]
This argument imposes no translation-equivariance assumption on independently specified original oracles. If the translated copy coincides geometrically with another set, its transported selector is still used for that auxiliary loss.

For objective sensitivity, the representation
\[
F_S(h,c)=\max_{w,y\in S}\{c^\top(w-y)-2h^\top w\}
\]
shows that
\[
F_S(h,c_1)-F_S(h,c_2)
\le\max_{w,y\in S}(c_1-c_2)^\top(w-y)
\le D(S)\|c_1-c_2\|.
\]
Interchanging the costs gives the absolute-value version.

## 3. The two asymmetric support/value bounds

Fix \(v\), put \(A=S_{\rm ref}\), \(B=S_{\rm cl}+v\), and let \(\delta_v=d_H(A,B)\). The client loss on \(B\), using its transported selector, equals its original loss. Set \(D_{\rm ref}=D(S_{\rm ref})\) and \(D_{\rm cl}=D(S_{\rm cl})=D(B)\).

Add and subtract \(F_A(h,c_{\rm cl})\). Sections 1–2 give
\[
|F_A(h,c_{\rm ref})-F_B(h,c_{\rm cl})|
\le D_{\rm ref}c_d+\delta_v(\|c_{\rm cl}-2h\|+\|c_{\rm cl}\|).
\]
Instead adding and subtracting \(F_B(h,c_{\rm ref})\) gives
\[
|F_A(h,c_{\rm ref})-F_B(h,c_{\rm cl})|
\le D_{\rm cl}c_d+\delta_v(\|c_{\rm ref}-2h\|+\|c_{\rm ref}\|).
\]
Denote the minimum of these right-hand sides by \(T_{\delta_v}(h)\).

These are estimates on the translated comparison. They do not assert a shape-distance bound for the original, unshifted support/value contribution by itself.

## 4. General optimizer bound and the shape-distance limit

For any \(a\in A\), \(b\in B\), choose \(\widetilde b\in B\) with \(\|a-\widetilde b\|\le\delta_v\). Then
\[
\|a-b\|\le\delta_v+D(B).
\]
The symmetric argument gives \(\|a-b\|\le\delta_v+D(A)\), so
\[
\|a-b\|\le\delta_v+D_{\min}.
\]
Apply this to \(a=w_{S_{\rm ref}}^*(c_{\rm ref})\) and \(b=w_{S_{\rm cl}}^*(c_{\rm cl})+v\). Decomposing the translated full loss and using Cauchy–Schwarz yields
\[
|\ell_{S_{\rm ref}}^{\mathrm{SPO+}}(h,c_{\rm ref})-
\ell_{S_{\rm cl}}^{\mathrm{SPO+}}(h,c_{\rm cl})|
\le T_{\delta_v}(h)+2\|h\|(\delta_v+D_{\min}).
\]
The shape distance is finite and nonnegative. By the definition of its infimum, choose \(v_n\) such that \(\delta_{v_n}\to\delta_N\). The right-hand side is continuous in \(\delta_v\), including the minimum of its two affine expressions. Passing to the limit proves \(H(h)\). No attainment of the translation infimum is required.

## 5. Curvature growth, uniqueness, and directional stability

Let \(S\) be nonempty, compact, and an intersection of closed Euclidean balls of radius \(\rho>0\). Fix a unit vector \(p\), choose a support maximizer \(y\in S\), and take \(x\in S\). Put \(L=\|x-y\|\). For any center \(a\) of a ball in the intersection and \(0<t<1\), the squared-norm identity gives
\[
\|(1-t)y+tx-a\|^2
=(1-t)\|y-a\|^2+t\|x-a\|^2-t(1-t)L^2
\le\rho^2-t(1-t)L^2.
\]
Here \(L\le2\rho\), so the square root below is defined. Define
\[
m_t=(1-t)y+tx,\qquad
r_t=\rho-\sqrt{\rho^2-t(1-t)L^2}.
\]
Every point within distance \(r_t\) of \(m_t\) belongs to every defining ball, by the triangle inequality. Hence \(m_t+r_tp\in S\). Support optimality of \(y\) implies
\[
p^\top(y-x)\ge\frac{r_t}{t}
=\frac{(1-t)L^2}{\rho+\sqrt{\rho^2-t(1-t)L^2}}.
\]
Letting \(t\downarrow0\) proves
\[
\xi_S(p)-p^\top x\ge\frac{\|x-y\|^2}{2\rho}.
\]
If \(x\) is another support maximizer, this forces \(x=y\). Thus the support point \(x_S(p)\) is unique, and the displayed inequality is the required quadratic growth. The argument includes singleton sets.

For unit \(p,q\), write \(y_p=x_S(p)\), \(y_q=x_S(q)\). Apply growth first in direction \(p\) to \(y_q\), and then in direction \(q\) to \(y_p\). Adding gives
\[
(p-q)^\top(y_p-y_q)\ge\frac{\|y_p-y_q\|^2}{\rho}.
\]
Cauchy–Schwarz, with the zero-distance case treated directly, gives
\[
\|x_S(p)-x_S(q)\|\le\rho\|p-q\|.
\]
For nonzero \(c\), minimization uses the negative normalized direction:
\[
w_S^*(c)=x_S\!\left(-\frac{c}{\|c\|}\right).
\]
Therefore
\[
\|w_S^*(c_1)-w_S^*(c_2)\|
\le\rho\left\|\frac{c_1}{\|c_1\|}-\frac{c_2}{\|c_2\|}\right\|.
\]

## 6. Cross-set support stability and the refined optimizer bound

Let \(A,B\) have radii \(\rho_A,\rho_B\), and let \(\delta=d_H(A,B)\). Fix unit \(p\), and put \(x_A=x_A(p)\), \(x_B=x_B(p)\). Choose \(y\in B\) with \(\|y-x_A\|\le\delta\). Section 1 implies
\[
\xi_B(p)-p^\top y
\le |\xi_B(p)-\xi_A(p)|+p^\top(x_A-y)
\le2\delta.
\]
Quadratic growth on \(B\) gives \(\|y-x_B\|\le2\sqrt{\rho_B\delta}\), and hence
\[
\|x_A-x_B\|\le\delta+2\sqrt{\rho_B\delta}.
\]
Interchanging the sets yields
\[
\|x_A(p)-x_B(p)\|\le\delta+2\sqrt{\rho_{\min}\delta}.
\]

Return to \(A=S_{\rm ref}\), \(B=S_{\rm cl}+v\), with \(\delta=\delta_v\). Translation preserves the intersection-of-balls property and its radius. Write
\[
\theta=\left\|\frac{c_{\rm ref}}{\|c_{\rm ref}\|}-\frac{c_{\rm cl}}{\|c_{\rm cl}\|}\right\|.
\]
A triangle inequality through the optimizer on \(A\) at cost \(c_{\rm cl}\) gives
\[
\|w_A^*(c_{\rm ref})-w_B^*(c_{\rm cl})\|
\le\rho_{\rm ref}\theta+\delta_v+2\sqrt{\rho_{\min}\delta_v}.
\]
A triangle inequality through the optimizer on \(B\) at cost \(c_{\rm ref}\) instead gives the same expression with \(\rho_{\rm cl}\theta\). Taking the minimum yields
\[
\|w_A^*(c_{\rm ref})-w_B^*(c_{\rm cl})\|
\le\rho_{\min}\theta+\delta_v+2\sqrt{\rho_{\min}\delta_v}.
\]
All normalized directions are defined by the positive lower cost bound.

## 7. Strongly convex loss bound

Use the translated full-loss comparison from Sections 3–4. Replace its general optimizer estimate by Section 6 and retain the same support/value bound \(T_{\delta_v}(h)\). This gives
\[
|\ell_{S_{\rm ref}}^{\mathrm{SPO+}}(h,c_{\rm ref})-
\ell_{S_{\rm cl}}^{\mathrm{SPO+}}(h,c_{\rm cl})|
\le T_{\delta_v}(h)+2\|h\|\left(\rho_{\min}\theta+\delta_v+2\sqrt{\rho_{\min}\delta_v}\right).
\]
Let \(\delta_v\to\delta_N\) along the same type of approximating sequence. Continuity of the square root at zero as well as elsewhere gives exactly \(H_{\rm SC}(h)\). The proof covers \(h=0\), \(\tau=0\), identical shapes, zero diameters, and equal costs.

## 8. Explicit diameter-scale obstruction

Choose fixed parameters \(d=2\), \(C_{\min}=1\), \(C_{\max}=3\), and \(\tau=1\). Let
\[
S=\operatorname{conv}\{(1,0),(0,1),(1,1)\},\qquad
h=\frac{1}{\sqrt2}(1,-1).
\]
Then \(D(S)=\sqrt2\), \(\|h\|=1\), and using \(S\) for both sets gives \(\delta_N=0\). For \(0<\epsilon\le1\), set
\[
c_1(\epsilon)=(1,1+\epsilon),\qquad
c_2(\epsilon)=(1+\epsilon,1).
\]
Their norms lie between \(1\) and \(3\), and their distance is \(\sqrt2\epsilon\). The unique minimizers are \((1,0)\) and \((0,1)\), respectively, and both minimum values equal \(1\). Thus the difference of decision terms is
\[
2h^\top\big((1,0)-(0,1)\big)=2\sqrt2.
\]
The objective-sensitivity estimate from Section 2 gives
\[
|F_S(h,c_1(\epsilon))-F_S(h,c_2(\epsilon))|\le2\epsilon.
\]
The reverse triangle inequality therefore yields
\[
|\ell_S^{\mathrm{SPO+}}(h,c_1(\epsilon))-
\ell_S^{\mathrm{SPO+}}(h,c_2(\epsilon))|
\ge2\sqrt2-2\epsilon.
\]
Taking \(\epsilon=1/n\) produces fixed admissible parameters, a fixed common set and prediction, and objective shifts tending to zero, while the liminf of the loss discrepancy divided by \(\|h\|D(S)\) is at least \(2\). This proves the stated existential necessity claim.

## Source-local corrections used

The translation must precede decomposition; shape distance does not separately bound the original unshifted components. Auxiliary translated selectors are transported rather than independently reselected. A minimizing cost uses the negative support direction. The lower-bound example is written with the prediction as the first loss argument. These local corrections preserve both final upper bounds and the lower-bound conclusion.
