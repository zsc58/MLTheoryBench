# Problem

## Setup

Consider a network with state \(x\in\mathbb R^n\), input \(u(t)\in\mathbb R^n\), diagonal matrices \(C=\operatorname{diag}(C_i)\) and \(R=\operatorname{diag}(R_i)\) with \(C_i,R_i>0\), and a symmetric matrix \(T\). Its dynamics and componentwise activation are
\[
C\dot x=Ty-R^{-1}x+u,\qquad y_i=g_i(x_i).
\]
Each \(g_i\) is a bounded, strictly increasing activation. Put \(q=Cx\), let \(J_i=g_i(\mathbb R)\), and define \(h_i(q_i)=g_i(q_i/C_i)\). Choose twice-differentiable strictly convex stored-energy primitives \(E_i\) satisfying \(E_i'(q_i)=h_i(q_i)\) and \(E_i''(q_i)>0\). Set \(E(q)=\sum_iE_i(q_i)\). For \(y_i\in J_i\), define the separable Legendre dual
\[
E^*(y)=\sum_iE_i^*(y_i),\qquad E_i^*(y_i)=\sup_{r\in\mathbb R}\{r y_i-E_i(r)\}.
\]
Finally define
\[
\Phi(y,u)=-\tfrac12 y^TTy+\sum_i(R_iC_i)^{-1}E_i^*(y_i)-y^Tu.
\]
Assume \(u\) and the corresponding trajectory are \(C^1\), with \(y(t)\in\prod_iJ_i\).

## Task

Prove that, in the output coordinates \(y\), every such trajectory satisfies
\[
G(y)\dot y=-\nabla_y\Phi(y,u),
\qquad G(y):=\nabla_y^2E^*(y)=\bigl(\nabla_q^2E(q)\bigr)^{-1}\succ0,
\]
along with the output identities \(\nabla_qE(q)=y\) and \(\nabla_u\Phi(y,u)=-y\). Moreover, prove the dissipation identity and inequality
\[
\frac{d}{dt}\Phi(y(t),u(t))
=-\dot y(t)^TG(y(t))\dot y(t)-y(t)^T\dot u(t)
\le -y(t)^T\dot u(t).
\]
