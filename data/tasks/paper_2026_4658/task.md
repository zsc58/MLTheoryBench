# Problem

## Setup

Let d be a positive integer. Let P_0=N(0,I_d) and let P_1 be any probability measure on R^d with finite second moment. Let pi be a coupling of (P_0,P_1) minimizing the quadratic cost E_pi[||X_0-X_1||^2], and let (X_0,X_1) have joint law pi.

Choose C^1 schedules alpha_t,beta_t on [0,1] with alpha_0=1, beta_0=0, alpha_1=0, beta_1=1, alpha_t>0 and beta_t>0 for t in (0,1), alpha nonincreasing, and beta nondecreasing. Define Y_t=alpha_t X_0+beta_t X_1. For a fixed t, a version of the conditional teaching field means a Borel map v_t:R^d->R^d satisfying

v_t(Y_t)=E_pi[dot alpha_t X_0+dot beta_t X_1 | Y_t]

pi-almost surely.

Let phi:R^d->(-infinity,+infinity] be a proper lower-semicontinuous convex function whose subdifferential graph contains the support of pi in the sense that X_0 is in partial phi(X_1) pi-almost surely. For t in (0,1), define

psi_t(u)=alpha_t phi(u)+(beta_t/2)||u||^2,

and for lambda>0 define prox_{lambda phi}(z) as the unique minimizer of phi(u)+(2lambda)^{-1}||u-z||^2.

## Task

Prove that for every t in (0,1), the convex conjugate psi_t* is differentiable on R^d and, for every y in R^d,

nabla psi_t*(y)=prox_{(alpha_t/beta_t) phi}(y/beta_t).

Moreover, prove that for every such t the conditional teaching field admits a Borel version defined at every y in R^d by

v_t(y)=(dot alpha_t/alpha_t)y+beta_t( dot beta_t/beta_t-dot alpha_t/alpha_t ) prox_{(alpha_t/beta_t) phi}(y/beta_t).

The statement must remain valid without assuming that P_1 has a density.
