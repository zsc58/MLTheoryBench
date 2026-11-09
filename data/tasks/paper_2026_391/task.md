# Problem

## Setup

Let P be a fixed probability law, and let (X_i,Y_i), i=1,...,n, be iid observations from P, where n is a positive integer. Let h be a fixed prediction rule and let R_i=M(h(X_i),Y_i), where M is a fixed measurable real-valued metric. Fix a measurable subgroup G before observing the sample. Write R=M(h(X),Y), I_i=1{(X_i,Y_i) in G}, and pi_G=P((X,Y) in G). Assume

0 < pi_min <= pi_G <= 1

for a constant pi_min. The reference value theta_P is a known finite real number, and e0 is a fixed real threshold specified before observing the sample. Define

epsilon* = E_P[R | (X,Y) in G] - theta_P.

Assume E_P[R^2 | (X,Y) in G] < infinity, |epsilon*| <= B_epsilon for a finite constant B_epsilon, and that the conditional variance of R given G is bounded above and away from zero. For each candidate e in R, define

U_i(e) = (R_i - theta_P - e) I_i.

Writing sigma_G^2=Var_P(U_i(epsilon*)), the variance condition can equivalently be expressed, with suitable constants, as

0 < sigma_min^2 <= sigma_G^2 <= sigma_max^2 < infinity.

The law, prediction rule, metric, group, reference value, threshold, and constants are fixed as n tends to infinity. The assertions below are pointwise in P.

Define the empirical likelihood

L_n(e) = sup { product_{i=1}^n p_i : p_i >= 0, sum_{i=1}^n p_i = 1, sum_{i=1}^n p_i U_i(e) = 0 }.

If the constraint is infeasible, set L_n(e)=0. Let N_G=sum_{i=1}^n I_i and define

hat_e = (sum_{i=1}^n I_i R_i)/N_G - theta_P when N_G>0,

and hat_e=0 when N_G=0. Define

ell_n(e) = -2 log[L_n(e)/L_n(hat_e)]

and

T_n(e0) = -2 log [ sup_{e in R, e<=e0} L_n(e) / sup_{e in R} L_n(e) ].

Use the convention -2 log(0)=+infinity.

Let W be a random variable with distribution 0.5 delta_0 + 0.5 chi-square_1, where delta_0 is a point mass at zero and chi-square_1 is the chi-square distribution with one degree of freedom. For alpha in (0,1/2), let c_alpha be its positive upper alpha quantile, defined by P(W>c_alpha)=alpha.

## Task

Prove the following integrated theorem for testing the null hypothesis epsilon*<=e0 with T_n(e0).

1. If epsilon*=e0, then T_n(e0) converges in distribution to W, and P(T_n(e0)>c_alpha) converges to alpha.
2. For every fixed law P satisfying the setup with epsilon*<e0, P(T_n(e0)>c_alpha) converges to zero.

Consequently, for every fixed law P satisfying the setup and epsilon*<=e0,

limsup_{n->infinity} P(T_n(e0)>c_alpha) <= alpha,

with equality at the boundary epsilon*=e0. Thus the boundary is least favorable in this pointwise asymptotic sense.
