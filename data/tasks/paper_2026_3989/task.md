# Problem

## Setup

Let C be a convex subset of R^d, let psi:C->R be differentiable and strictly convex, and define the Bregman divergence
D_psi(x,y)=psi(x)-psi(y)-<grad psi(y),x-y>.
Assume all observations y_i lie in C. For a finite nonempty node u with observations {y_i:i in u}, define its barycenter (node representative) by
mu_u=|u|^{-1} sum_{i in u} y_i,
and define its impurity by
I_psi(u)=|u|^{-1} sum_{i in u}D_psi(y_i,mu_u).
Consider a binary split of a parent node t into disjoint nonempty children t_L and t_R, with t=t_L union t_R. Set p_L=|t_L|/|t| and p_R=|t_R|/|t|. The split gain is
Delta_psi(t)=I_psi(t)-p_L I_psi(t_L)-p_R I_psi(t_R).

## Task

Prove the following integrated theorem: every such binary split satisfies the exact decomposition
Delta_psi(t)=p_L D_psi(mu_{t_L},mu_t)+p_R D_psi(mu_{t_R},mu_t).
If, additionally, psi is lambda-strongly convex on C for some lambda>0, meaning that D_psi(x,y)>=lambda||x-y||^2/2 for all x,y in C, prove the quantitative bound
Delta_psi(t)>= (lambda/2) p_L p_R ||mu_{t_L}-mu_{t_R}||^2.
