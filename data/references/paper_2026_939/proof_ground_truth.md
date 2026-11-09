# Reference Proof

## Proof Structure

Differentiate the unpenalized empirical objective using the assumed conjugate derivative and the linearity of the moment functional. Use coordinate optimality to construct a single penalty subgradient vector satisfying stationarity, treating zero coefficients and zero regularization explicitly. Then obtain the three balancing conclusions.

## Complete Proof

Write

F(beta)=n^{-1} sum_i [G*(x_i,t_beta(x_i))-m(w_i,t_beta)],

so that L_lambda=F+lambda Omega_q. All derivatives below are evaluated at the finite-valued minimizer beta_hat. The assumed differentiability of the conjugates, the finiteness of the sample, and the chain rule give

partial_{beta_j} G*(x_i,t_beta(x_i)) = a_hat(x_i) psi_j(x_i).

Indeed, the scalar derivative of G*(x_i,.) at t_beta_hat(x_i) is a_hat(x_i), and partial_{beta_j}t_beta(x_i)=psi_j(x_i).

By linearity on the span of the basis,

m(w_i,t_beta)=sum_k beta_k m(w_i,psi_k).

Consequently,

partial_{beta_j}F(beta_hat)
= n^{-1} sum_i [a_hat(x_i)psi_j(x_i)-m(w_i,psi_j)]
= Delta_j.

For a convex function H on R^p, the subgradient condition s in partial H(beta_hat) means that

H(beta) >= H(beta_hat)+s^T(beta-beta_hat)

for every beta. We now construct such a vector for H=Omega_q and verify the stationarity equation.

First suppose q>1. The function h_q(u)=|u|^q/q is differentiable on R, with derivative sign(u)|u|^(q-1) at u not equal to zero and derivative zero at u=0. The value at zero follows directly because |h_q(h)-h_q(0)|/|h|=|h|^(q-1)/q tends to zero. Define

s_j=sign(beta_hat_j)|beta_hat_j|^(q-1),

with s_j=0 when beta_hat_j=0. The function h_q is convex, so its derivative gives a supporting-line inequality. Summing those scalar inequalities proves s in partial Omega_q(beta_hat). Since L_lambda is differentiable at beta_hat, minimizing it along each coordinate gives

0=partial_{beta_j}L_lambda(beta_hat)=Delta_j+lambda s_j.

This argument includes lambda=0.

Next suppose q=1. For each nonzero beta_hat_j, the coordinate penalty is differentiable near beta_hat_j. Coordinate optimality therefore gives

Delta_j+lambda sign(beta_hat_j)=0.

Set s_j=sign(beta_hat_j) at these coordinates. For a coordinate with beta_hat_j=0, consider beta_hat+h e_j. Differentiability of F gives

L_lambda(beta_hat+h e_j)-L_lambda(beta_hat)
= h Delta_j+lambda |h|+o(|h|).

This difference is nonnegative for both signs of h. Taking h down to zero and h up to zero respectively yields

Delta_j+lambda>=0,    Delta_j-lambda<=0.

Thus |Delta_j|<=lambda. If lambda>0, set s_j=-Delta_j/lambda at each zero coordinate; then s_j is in [-1,1] and Delta_j+lambda s_j=0. If lambda=0, the same inequalities give Delta_j=0 at zero coordinates, and the equations at nonzero coordinates also give Delta_j=0. In this case set s_j=0 at zero coordinates.

For every coordinate, the constructed s_j is sign(beta_hat_j) when beta_hat_j is nonzero and belongs to [-1,1] when beta_hat_j is zero. These choices satisfy

|u| >= |beta_hat_j|+s_j(u-beta_hat_j)

for every real u. Summing over coordinates proves s in partial Omega_1(beta_hat). By construction, Delta_j+lambda s_j=0 for every j.

We have therefore established the asserted existence of a single vector s in partial Omega_q(beta_hat) satisfying all coordinate equations. If q=1, |s_j|<=1 implies |Delta_j|<=lambda. If q>1, the displayed formula for s_j implies |Delta_j|=lambda|beta_hat_j|^(q-1), including beta_hat_j=0. Finally, when lambda=0, the stationarity equation gives Delta_j=0 for every coordinate. In particular, this proves the stated unregularized conclusion under its feasibility and minimizer assumptions. Feasibility alone is not used to assert that an empirical minimizer exists; its existence is separately assumed.
