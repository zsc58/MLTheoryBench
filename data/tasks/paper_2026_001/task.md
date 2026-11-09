# Problem

## Setup

Let d,m,N be positive integers. Let (X_0,X_1) have coupling pi on R^d x R^d, with marginals rho_0 and rho_1. Let T be independent of (X_0,X_1) and uniform on [0,1], set X_T=(1-T)X_0+T X_1 and u=X_1-X_0. All expectations below use an independent test triple generated this way.

Fix a feature map phi:[0,1] x R^d -> R^m and N fixed training triples (T_i,X_{T_i},u_i), with T_i in [0,1] and X_{T_i},u_i in R^d. Assume phi(T,X_T) is measurable and

E||u||^2 < infinity,    E||phi(T,X_T)||^2 < infinity.

Let Phi be the N x m matrix whose i-th row is phi(T_i,X_{T_i})^T, and let U be the N x d matrix whose i-th row is u_i^T. For a coefficient matrix W in R^(m x d), define the linear velocity field v_W(t,x)=W^T phi(t,x).

For lambda>0, define

Sigma=Phi^T Phi/N,    Q_lambda=(Sigma+lambda I_m)^(-1),
W_lambda=Q_lambda Phi^T U/N,

where I_m is the m x m identity matrix, and let v_lambda=v_(W_lambda). Define the teacher predictions U_hat_lambda=Phi W_lambda and the pure-distilled fit

W_pd,lambda=Q_lambda Phi^T U_hat_lambda/N,

with field v_pd,lambda=v_(W_pd,lambda). For xi in R, set U^(xi)=(1-xi)U+xi U_hat_lambda, define

W_sd,lambda,xi=Q_lambda Phi^T U^(xi)/N,

and let v_sd,lambda,xi=v_(W_sd,lambda,xi).

Conditioned on the fixed training data, define the integrated velocity risk

R(lambda)=E||u-v_lambda(T,X_T)||^2,
R_pd(lambda)=E||u-v_pd,lambda(T,X_T)||^2,
C(lambda)=E<u-v_lambda(T,X_T),u-v_pd,lambda(T,X_T)>,
D(lambda)=E||v_lambda(T,X_T)-v_pd,lambda(T,X_T)||^2.

All norms and inner products on vectors are Euclidean. When lambda varies, the coupling pi, feature map phi, and training triples remain fixed. Assume R(lambda) is differentiable at the lambda under consideration whenever a derivative formula is invoked; R'(lambda) denotes this derivative.

## Task

Prove the following integrated theorem. For every lambda>0 and xi in R,

1. W_sd,lambda,xi=(1-xi)W_lambda+xi W_pd,lambda and v_sd,lambda,xi(t,x)=(1-xi)v_lambda(t,x)+xi v_pd,lambda(t,x) for all (t,x) in [0,1] x R^d.
2. The student risk satisfies
   R_sd(lambda,xi)=R(lambda)-2 xi (R(lambda)-C(lambda))+xi^2 D(lambda), where R_sd(lambda,xi)=E||u-v_sd,lambda,xi(T,X_T)||^2. If D(lambda)>0, the unique unconstrained minimizer over xi in R is
   xi_star(lambda)=(R(lambda)-C(lambda))/D(lambda),
   and the minimum risk is R(lambda)-(R(lambda)-C(lambda))^2/D(lambda).
3. If D(lambda)>0 and R is differentiable at lambda, then xi_star(lambda)=-lambda R'(lambda)/(2D(lambda)) and the minimum risk is R(lambda)-lambda^2 (R'(lambda))^2/(4D(lambda)). Consequently, whenever D(lambda)>0 and R'(lambda)!=0, the optimum strictly improves the teacher risk and sign(xi_star(lambda))=-sign(R'(lambda)).
