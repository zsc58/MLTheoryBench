# Problem

## Setup

### Uniform-bound setting

Let n be a positive integer, and let Z, Z_1, ..., Z_n be independent samples from a distribution D. Fix a compact set T contained in R^d with 0 in T, and a measurable loss ell satisfying ell(0;z)=0 and 0 <= ell(theta;z) <= B for every theta in T and sample z, where B > 0 is finite. Define R(theta) = E[ell(theta;Z)] and Rhat_n(theta) = n^(-1) sum_i ell(theta;Z_i).

Let {p_theta: theta in Theta} be a smooth statistical model with Theta contained in R^d and a common dominating measure. Its Fisher information is

G(theta) = E_{X~p_theta}[ grad_theta log p_theta(X) grad_theta log p_theta(X)^T ].

Assume G(theta) is finite and positive definite for every theta in Theta. Fix a base point theta_0 in Theta and write G0 = G(theta_0) and ||v||_{G0} = sqrt(v^T G0 v). Assume that, for some finite L > 0,

|ell(theta_1;z)-ell(theta_2;z)| <= L ||theta_1-theta_2||_{G0}

for all theta_1, theta_2 in T and all z.

For S contained in R^d, define the Gaussian width w(S) = E_g sup_{v in S} <g,v>, where g is standard Gaussian in R^d, and the Fisher width

w_G0(S) = E_g sup_{v in S} <g, G0^(1/2) v>.

### Exponential-family setting

In a separate sampling setting, consider a regular exponential family

p_theta(z) = h(z) exp(theta^T phi(z) - A(theta))

with parameter domain Theta contained in R^d. Its Fisher information, defined as above, is assumed finite and positive definite for every theta in Theta. Fix theta_0 in Theta and write G0 = G(theta_0) = Cov_{p_theta0}(phi(Y)). Use the same definition of w_G0 for this model and base point.

Let Y, Y_1, ..., Y_n be independent samples from p_theta0. Assume E_{p_theta0} ||phi(Y)||_2^2 is finite, and choose a fixed r > 0 with theta_0 + r B_2^d contained in Theta, where B_2^d is the closed Euclidean unit ball. For u in r B_2^d define

tilde ell(u;y) = -log p_{theta_0+u}(y) + log p_{theta_0}(y).

Interpret this difference on the common support of the family and extend it by zero on its common null complement. Define

tilde R(u) = E_{Y~p_theta0}[tilde ell(u;Y)],

Rhat_tilde_n(u) = n^(-1) sum_i tilde ell(u;Y_i).

## Task

Prove the following integrated theorem, with each assertion using its respective sampling setting.

1. **Uniform upper bound.** For every delta in (0,1), with probability at least 1-delta,

sup_{theta in T} |R(theta)-Rhat_n(theta)| <= C L w_G0(T-T)/sqrt(n) + B sqrt(log(1/delta)/(2n)),

where C is universal.

2. **Asymptotic sharpness.** In the exponential-family setting, with the model, dimension, base point, and radius fixed,

lim_{n to infinity} sqrt(n) E[sup_{u in r B_2^d} |tilde R(u)-Rhat_tilde_n(u)|] = w_G0(r B_2^d).

Consequently, for every epsilon in (0,1),

E[sup_{u in r B_2^d} |tilde R(u)-Rhat_tilde_n(u)|] >= (1-epsilon) w_G0(r B_2^d)/sqrt(n)

for all sufficiently large n. The threshold may depend on epsilon and the fixed exponential-family setting.
