# Problem

## Setup

Let \(d\geq1\) be an integer. Let \(Z\sim\mathcal N(0,I_d)\) and \(X\sim\mathcal N(0,I_d)\) be independent. Let \(\alpha,\beta\in C^1([0,1])\) satisfy
\[
\alpha_0=\beta_1=1,\qquad \alpha_1=\beta_0=0,
\]
with \(\alpha_t,\beta_t>0\), \(\dot\alpha_t<0\), and \(\dot\beta_t>0\) for \(0<t<1\). Derivatives at endpoints are one-sided.

Define, for \(t\in[0,1]\),
\[
I_t=\alpha_t Z+\beta_t X,
\]
\[
\eta_Z(t,x)=\mathbb E[Z\mid I_t=x],\qquad
\eta_X(t,x)=\mathbb E[X\mid I_t=x],
\]
and the deterministic interpolant velocity
\[
b^0(t,x)=\dot\alpha_t\eta_Z(t,x)+\dot\beta_t\eta_X(t,x).
\]
All conditional expectations in this problem use their spatially continuous versions. Assume also that \(t\mapsto b^0(t,x)\) belongs to \(C^1([0,1])\) for each \(x\in\mathbb R^d\).

For comparison, define the linear interpolant and its deterministic velocity by
\[
\bar I_u=(1-u)Z+uX,\qquad
\bar b(u,y)=\mathbb E[X-Z\mid\bar I_u=y],
\qquad (u,y)\in[0,1]\times\mathbb R^d.
\]
Set
\[
d_t=(1-t)^2+t^2,\qquad
\alpha_t^{\rm L}=\frac{1-t}{\sqrt{d_t}},\qquad
\beta_t^{\rm L}=\frac{t}{\sqrt{d_t}}.
\]
Write \(I_t^{\rm L}=\alpha_t^{\rm L}Z+\beta_t^{\rm L}X\), and define its deterministic velocity, including the endpoints, by
\[
b^{\rm L}(t,x)=\dot\alpha_t^{\rm L}\mathbb E[Z\mid I_t^{\rm L}=x]
+\dot\beta_t^{\rm L}\mathbb E[X\mid I_t^{\rm L}=x].
\]

## Task

Prove the following integrated theorem.

1. For the Gaussian data above, \(b^0(t,x)=0\) for every \(t\in(0,1)\) and \(x\in\mathbb R^d\) if and only if
\[
\alpha_t^2+\beta_t^2=1\qquad\text{for every }t\in(0,1).
\]

2. For the schedule \((\alpha^{\rm L},\beta^{\rm L})\), the associated deterministic velocity satisfies
\[
b^{\rm L}(t,x)=\frac{1-2t}{d_t}\,x+d_t^{-1/2}\,\bar b\!\left(t,\sqrt{d_t}\,x\right),
\qquad 0<t<1,\quad x\in\mathbb R^d,
\]
and its initial endpoint satisfies
\[
b^{\rm L}(0,z)=z+\bar b(0,z)=\mathbb E[X]
\qquad\text{for every }z\in\mathbb R^d.
\]
