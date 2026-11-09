# Problem

## Setup

Let a connected finite graph have N vertices and M edges. Fix an oriented incidence vector d_e in R^N for each edge. The conductance domain is Omega=(0,infinity)^M. For k in Omega, define

L(k)=sum_e k_e d_e d_e^T,

G(x;k)=x^T L(k)x/2.

Inputs and outputs are represented by fixed matrices P in R^(N x I) and Q in R^(N x O), with fixed prescribed vectors v in R^I and w in R^O. Inputs and outputs use disjoint state coordinates: no row index has both a nonzero row of P and a nonzero row of Q. Assume P has full column rank and ker L(k) intersect ker P^T={0} near the point considered below. Define

Lhat(k)=[[L(k),P],[P^T,0]].

The free state x_0(k) is the unique minimizer of G(x;k) subject to P^T x=v. Set

r(k)=Q^T x_0(k)-w,

S={k in Omega:r(k)=0},

and assume S is nonempty. In all energy derivatives partial_(k_e) G(x;k), the state argument x is held fixed.

For eta>0 sufficiently small, define the EP nudged state x_eta_EP as the minimizer of

G(x;k)-eta <Q r(k),x>

subject to P^T x=v. Define the CL nudged state x_eta_CL as the minimizer of G(x;k) subject to

P^T x=v,

Q^T x=(1+eta)Q^T x_0(k)-eta w.

For j equal to EP or CL, define its continuous-time field by

(F_j(k))_e=lim_(eta->0+) [partial_(k_e)G(x_eta_j;k)-partial_(k_e)G(x_0(k);k)]/eta,

and its dynamics by dot k=F_j(k).

For AL, let the fully constrained reference state and its multipliers be determined by

[[L,P,Q],[P^T,0,0],[Q^T,0,0]] (x^a,lambda,mu)^T=(0,v,w)^T.

Define x_eta_AL as the minimizer of G(x;k) subject to

P^T x=v,

Q^T x=w+eta mu(k).

Its field and loss are

(F_AL(k))_e=lim_(eta->0+) [partial_(k_e)G(x_eta_AL;k)-partial_(k_e)G(x^a(k);k)]/eta,

Phi_*(k)=||mu(k)||^2/2.

For every nudge, k and the residual or multiplier specifying that nudge are held fixed while the constrained state is determined. Assume all these states and limiting fields are smooth near the solution point below.

Fix k_* in S. Define the lifted incidence vectors and output matrix by

d_hat_e=[d_e;0_I],

Q_hat=[Q;0_(I x O)].

Let

E'={e:d_e^T x_0(k_*) is nonzero},

Lambda=diag((d_e^T x_0(k_*))^2)_(e in E'),

Dprime=[d_hat_e]_(e in E').

Assume the residual Jacobian Dr(k_*) has full row rank, equivalently Dprime^T Lhat(k_*)^(-1) Q_hat has full column rank. For the AL reference state define

E'_a={e:d_e^T x^a(k_*) is nonzero},

Dprime_a=[d_hat_e]_(e in E'_a),

and assume Dprime_a^T Lhat(k_*)^(-1) Q_hat has full column rank as well.

Write

D(k)=(Q_hat^T Lhat(k)^(-1) Q_hat)^(-1),

Phi_D(k)=r(k)^T D(k)r(k)/2

for the CL weighted loss near k_*.

## Task

Prove that there exist a neighborhood U of k_* contained in Omega and rho>0 such that, for each of EP, CL, and AL, every solution with ||k(0)-k_*||<rho exists for all t>=0, remains in U, and converges to a limit k_infinity in S.

Moreover, prove exponential residual decay uniformly for such initial points: for each method there are constants C>=1 and a>0, independent of the initial point within this radius, such that

||r(k(t))||<=C exp(-a t)||r(k(0))|| for every t>=0.

For CL, also prove that there is a_D>0 such that

Phi_D(k(t))<=exp(-a_D t)Phi_D(k(0)),

and for AL that there is a_*>0 such that

Phi_*(k(t))<=exp(-a_* t)Phi_*(k(0)).

The neighborhood, radius, prefactors, and rates may depend on the fixed graph, input and output data, and k_*, but not on the initial point within the stated radius.
