# Problem

## Setup

Let m,p be positive integers, let x belong to an arbitrary input space X, let w belong to R^p, and let f_w(x) in R^m be differentiable with respect to w. An online stream may update w after each observation, but the claim below is pointwise for any fixed x,w,y.

The likelihood for an observation y in R^m is the product of independent Student-t components with degrees of freedom nu>0, scale s>0, and location f_w(x):

p_w(y|x) = product_{i=1}^m c_{nu,s} [1 + (y_i-f_{w,i}(x))^2/(nu s^2)]^{-(nu+1)/2},

where c_{nu,s} is the normalizing constant. Let J_w(x) be the m-by-p Jacobian of f_w(x) with respect to w, and let z(y,x,w)=nabla_f log p_w(y|x) be the output score. Define the Fisher covariance in parameter space by

F_w(x)=Cov_{Y~p_w(.|x)}(J_w(x)^T z(Y,x,w) | x).

For a regularization constant tau>0, define the Tikhonov-regularized natural-gradient score

tilde g(y,x,w)=(F_w(x)+tau I_p)^(-1) J_w(x)^T z(y,x,w).

## Task

Prove that, uniformly for every x in X, w in R^p, and y in R^m,

||tilde g(y,x,w)||_2 <= (1/4) sqrt(((nu+1)(nu+3)m)/(tau nu)).
