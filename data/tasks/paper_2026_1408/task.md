# Problem

## Setup

Let Theta, X, and Xi be measurable spaces. Fix dominating measures on Theta and X; all densities and their integrals below are with respect to these measures. Let p(theta) be a probability density and p(x|theta,xi) a jointly measurable likelihood density. Write

P_xi(theta,x)=p(theta)p(x|theta,xi).

A conditional joint density q(theta,x|xi) is a jointly measurable probability kernel: for each xi it is a probability density on Theta times X. Throughout, q ranges over all such kernels, with no additional restriction on their joint densities. Write q(x|xi)=integral q(theta,x|xi)dtheta. For a fixed xi, nu ranges over all probability densities on X.

Use the relative-entropy convention KL(R||S)=integral R log(R/S), with zero-density terms interpreted in the usual extended-real sense and KL equal to infinity when absolute continuity fails. Assume the displayed integrals are measurable in their unintegrated variables. Expectations of nonnegative divergences are interpreted as extended-real integrals. The normalizing integrals defining p_alpha and the joint law below are assumed finite and strictly positive. Conditional-density formulas are asserted only almost everywhere under the corresponding outcome marginal; values on null outcomes may be chosen arbitrarily.

Fix rho>0. Define

U(xi,q)=integral q(theta,x|xi) log[q(theta,x|xi)/(p(theta)q(x|xi))]dtheta dx.

For a probability policy pi on Xi, define

Q_rho(pi)={q: E_{xi~pi} KL(q(theta,x|xi)||P_xi(theta,x))<=rho}.

For every policy under consideration, assume effective-domain strict feasibility: there exists a measurable conditional joint density q0 such that

E_{xi~pi} U(xi,q0)<infinity,

E_{xi~pi} KL(q0(theta,x|xi)||P_xi(theta,x))<rho.

For 0<alpha<1, define

D_alpha(R||S)=1/(alpha-1) log integral R(z)^alpha S(z)^(1-alpha)dz,

with value infinity when the integral is zero, and

I_alpha^S(theta;x|xi)=inf_nu D_alpha(P_xi(theta,x)||p(theta)nu(x|xi)).

## Task

Prove that, for every policy pi under consideration,

inf_{q in Q_rho(pi)} E_{xi~pi} U(xi,q)
= sup_{0<alpha<1} {E_{xi~pi} I_alpha^S(theta;x|xi)-alpha/(1-alpha) rho}.

Consequently, the robust design value is obtained by taking sup_pi of both sides over the same policies.

Moreover, for each xi and 0<alpha<1, define

p_alpha(x|xi)
= [integral p(theta)p(x|theta,xi)^alpha dtheta]^(1/alpha)
  / integral [integral p(vartheta)p(x|vartheta,xi)^alpha dvartheta]^(1/alpha)dx.

Show that the pointwise minimization over all joint probability densities q,

inf_q {U(xi,q)+alpha/(1-alpha) KL(q(theta,x|xi)||P_xi(theta,x))},

has a minimizing law q_alpha^* given by

q_alpha^*(theta,x|xi)
proportional to [p(theta)p_alpha(x|xi)]^(1-alpha)[P_xi(theta,x)]^alpha,

and that its posterior satisfies

q_alpha^*(theta|x,xi)
= p(theta)p(x|theta,xi)^alpha
  / integral p(vartheta)p(x|vartheta,xi)^alpha dvartheta.

If the dual supremum for a fixed policy is attained at alpha in (0,1), show that the corresponding kernel q_alpha^* is a constrained worst-case law in Q_rho(pi).
