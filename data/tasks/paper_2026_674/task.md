# Problem

## Setup

Let Theta be a nonempty closed convex subset of a finite-dimensional Euclidean parameter space, and let Xi be a nonempty compact convex subset of a finite-dimensional Euclidean data space. Write D_xi=sup_{x,y in Xi}||x-y||. All norms and projections are Euclidean. For probability laws P,Q on Xi, let W_1(P,Q) be the infimum of E||X-Y|| over joint laws of (X,Y) with marginals P,Q.

Fix a distribution-sensitivity bound s>=0. For every theta in Theta, let P_hat(theta) be a probability law on Xi satisfying

W_1(P_hat(theta),P_hat(theta')) <= s||theta-theta'||

for all theta,theta' in Theta.

Let l:Theta x Xi -> R be continuously differentiable. Assume that l(.,zeta) is m-strongly convex for every zeta in Xi, where m>0. Let L_{theta theta}, L_{theta zeta}, and L_{zeta theta} be finite nonnegative constants such that, for all theta,theta' in Theta and zeta,zeta' in Xi,

||nabla_theta l(theta,zeta)-nabla_theta l(theta',zeta)|| <= L_{theta theta}||theta-theta'||,

||nabla_theta l(theta,zeta)-nabla_theta l(theta,zeta')|| <= L_{theta zeta}||zeta-zeta'||,

||nabla_zeta l(theta,zeta)-nabla_zeta l(theta',zeta)|| <= L_{zeta theta}||theta-theta'||.

Let lambda:Theta -> R be differentiable. For finite positive constants lambda_min, lambda_max, L_lambda, and H_lambda, assume

0<lambda_min<=lambda(theta)<=lambda_max,

||nabla lambda(theta)||<=L_lambda,

||nabla lambda(theta)-nabla lambda(theta')||<=H_lambda||theta-theta'||.

Set gamma=m-H_lambda D_xi^2>0. Define

phi(theta,xi,zeta)=l(theta,zeta)-lambda(theta)||xi-zeta||^2,

f(theta,xi)=sup_{zeta in Xi}phi(theta,xi,zeta).

Assume that phi(theta,xi,.) is mu-strongly concave on Xi for every theta in Theta and xi in Xi, where mu>0. Denote its unique maximizer by zeta^*(theta,xi).

A robust performative stable point for this Lagrangian surrogate is a point theta_s in Theta minimizing the frozen-law objective

theta -> E_{xi~P_hat(theta_s)}f(theta,xi).

Fix an inner approximation tolerance delta>=0, independently of s. Let z:Theta x Xi -> Xi be measurable and satisfy

||z(theta,xi)-zeta^*(theta,xi)||<=delta

for every theta,xi. Define the exact expected approximate-inner gradient

G(theta)=E_{xi~P_hat(theta)}[nabla_theta phi(theta,xi,z(theta,xi))],

where nabla_theta phi differentiates only the first argument of phi. For theta_0 in Theta and eta>0, consider the iteration

theta_{t+1}=Proj_Theta(theta_t-eta G(theta_t)),  t=0,1,2,... .

## Task

Prove the following statements.

If Theta consists of one point, that point is the unique robust performative stable point and theta_t=theta_s=theta_0 for every t>=0 and every eta>0.

Otherwise, define

L^phi_{theta theta}=L_{theta theta}+H_lambda D_xi^2,
L^phi_{theta xi}=2L_lambda D_xi,
L^phi_{theta zeta}=L_{theta zeta}+2L_lambda D_xi,
L^phi_{zeta theta}=L_{zeta theta}+2L_lambda D_xi,
L^phi_{zeta xi}=2lambda_max,

L^f_{theta theta}=L^phi_{theta theta}+L^phi_{theta zeta}L^phi_{zeta theta}/mu,
L^f_{theta xi}=L^phi_{theta xi}+L^phi_{theta zeta}L^phi_{zeta xi}/mu,

beta=L^f_{theta theta}+s L^f_{theta xi}.

If gamma>s L^f_{theta xi}, then beta>0. For any step size

0<eta<2(gamma-s L^f_{theta xi})/beta^2,

the quantity

kappa_gd=sqrt(1+2eta(s L^f_{theta xi}-gamma)+eta^2 beta^2)

is real and belongs to [0,1), there exists a unique robust performative stable point theta_s, and for every theta_0 in Theta and every integer t>=0,

||theta_t-theta_s|| <= kappa_gd^t||theta_0-theta_s||
 + (eta L^phi_{theta zeta}delta/(1-kappa_gd))(1-kappa_gd^t).

In particular,

limsup_{t->infinity}||theta_t-theta_s|| <= eta L^phi_{theta zeta}delta/(1-kappa_gd).

Thus the iterates approach this neighborhood with the displayed geometric error bound. When delta=0, they converge linearly to theta_s, without requiring s=0.
