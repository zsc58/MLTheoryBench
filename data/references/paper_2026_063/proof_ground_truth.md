# Reference Proof

## Proof Structure

1. Use the chosen strictly convex stored-energy primitives and their Legendre duals to obtain the dual coordinate and inverse-Hessian identities.
2. Rewrite the network equation in charge variables, compute the potential gradient, and derive the gradient dynamics and output relation in the output coordinates.
3. Apply the chain rule along a differentiable trajectory to obtain the exact dissipation identity and inequality.

## Complete Proof

Let q=Cx. Since q_i=C_i x_i and y_i=g_i(x_i)=h_i(q_i), the defining relation E_i'(q_i)=h_i(q_i) gives
\[
\nabla_q E(q)=y,\qquad E(q)=\sum_i E_i(q_i).
\]
The chosen positive Hessian makes \(\nabla_q^2E(q)\) positive definite. For \(y_i\in J_i\), Legendre duality yields
\[
q=\nabla_yE^*(y),\qquad G(y):=\nabla_y^2E^*(y)\succ0,
\]
and differentiating inverse gradient maps gives
\[
G(y)=\bigl(\nabla_q^2E(q)\bigr)^{-1}.
\]
Differentiating q=\nabla_yE^*(y) along a trajectory therefore gives \(\dot q=G(y)\dot y\).

The network equation and q_i=C_i x_i imply
\[
\dot q=C\dot x=Ty-R^{-1}x+u.
\]
For
\[
\Phi(y,u)=-\tfrac12 y^TTy+\sum_i(R_iC_i)^{-1}E_i^*(y_i)-y^Tu,
\]
symmetry of T and \(\partial_{y_i}E_i^*(y_i)=q_i\) give
\[
\nabla_y\Phi=-Ty+\operatorname{diag}((R_iC_i)^{-1})q-u.
\]
Because \(\operatorname{diag}((R_iC_i)^{-1})q=R^{-1}x\), we have \(\nabla_y\Phi=-\dot q\). Combining this with \(\dot q=G(y)\dot y\) proves
\[
G(y)\dot y=-\nabla_y\Phi(y,u).
\]
Direct differentiation of the potential gives \(\nabla_u\Phi=-y\), while the primitive-energy relation already gives \(\nabla_qE=y\).

For a C^1 input and trajectory, the chain rule and the gradient equation yield
\[
\frac{d}{dt}\Phi(y(t),u(t))
=\nabla_y\Phi^T\dot y+\nabla_u\Phi^T\dot u
=-\dot y^TG(y)\dot y-y^T\dot u.
\]
Since G(y) is positive definite, the first term is nonpositive, and hence
\[
\frac{d}{dt}\Phi(y(t),u(t))\le -y(t)^T\dot u(t).
\]
This establishes every clause of the integrated target.
