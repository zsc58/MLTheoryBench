# Problem

## Setup

There exist universal constants C,c>0 with the following property.

Let d,n,m be positive integers with m>n. Fix a distribution on R^d and a measurable feature map phi:R^d->R^m satisfying ||phi(x)||_2<=b for some finite b>0. Let

Sigma=E[phi(x)phi(x)^T],
mu=lambda_min(Sigma)>0.

Fix a nonzero vector theta_star in R^m and parameters nu>0, lambda>0, eta>0, 0<delta<1, epsilon>0, and gamma>0. All these objects and parameters are fixed independently of the random draws below. Assume

m>=C max{log(6/delta), ||theta_star||_2^2/nu^2, gamma/(mu nu^2)},

m-n>=C max{log(6/delta), ||theta_star||_2^2/nu^2, gamma/(mu nu^2)},

n>=C b^4||theta_star||_2^4 epsilon^-2 log(6/delta),

eta<1/lambda,
eta<=1/(lambda+b^2).

Draw x_1,...,x_n independently from the fixed distribution, set y_i=<theta_star,phi(x_i)>, and independently draw theta^(0)~N(0,nu^2 I_m). Let Phi be the n by m matrix with rows phi(x_i)^T, and let

A=Phi^T Phi/n,
B_Phi=||Phi||_F^2/n.

Define

Lhat(theta)=1/(2n) sum_i(<theta,phi(x_i)>-y_i)^2,

L(theta)=E[(<theta,phi(x)>-<theta_star,phi(x)>)^2],

where the expectation in L is over a fresh draw from the fixed distribution. Set

F_lambda(theta)=Lhat(theta)+(lambda/2)||theta||_2^2,

theta^(t+1)=theta^(t)-eta grad F_lambda(theta^(t)), for t=0,1,2,... .

On any sample for which A has a positive eigenvalue, write alpha=lambda_min^+(A) for its smallest positive eigenvalue.

## Task

Prove that, with probability at least 1-delta over the sampled data and initialization, theta^(0) is nonzero and the following implication holds: if A has a positive eigenvalue and

0<eta<1/(lambda+lambda_max(A)),

lambda<=c min{epsilon/||theta_star||_2^2, sqrt(B_Phi epsilon)/||theta_star||_2},

then all three conclusions below hold simultaneously. The probability is taken under the original independent sampling experiment, without conditioning on these sample-dependent hypotheses.

Let q=1-eta(alpha+lambda). Then:

1. For every nonnegative integer t>=T_train:=1/2 log_q(epsilon/(6B_Phi||theta^(0)||_2^2)), Lhat(theta^(t))<=epsilon.
2. For every nonnegative integer t<=T_delay:=log_{1-eta lambda}(sqrt(2/((m-n)nu^2))(sqrt(gamma/mu)+||theta_star||_2)), L(theta^(t))>=gamma.
3. Gradient descent converges to the unique minimizer theta_lambda of F_lambda. Moreover, L(theta_lambda)<=2Lhat(theta_lambda)+epsilon, and L(theta^(t))<=3epsilon for all sufficiently large nonnegative integers t.
