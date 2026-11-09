# Problem

## Setup

Let d be a positive integer, let mu be in R^d, and let Sigma be a symmetric positive-definite d x d matrix. Let p_0 be the Gaussian law N(mu,Sigma) on R^d. Its score is s_0(x) = -Sigma^{-1}(x-mu).

Consider the Ornstein-Uhlenbeck diffusion

dX_t = -X_t dt + sqrt(2) dW_t,

where W_t is a standard d-dimensional Brownian motion and X_0, independent of W, is distributed according to p_0. For t > 0, conditional on X_0=x, X_t has density

q_t(y|x) = N(y; exp(-t)x, (1-exp(-2t)) I),

and write a = exp(-t), v = 1-exp(-2t). Fix y in R^d, t > 0, and an integer N >= 1. Draw independent references X_1,...,X_N from p_0, set w_i = q_t(y|X_i), and normalize

tilde w_i = w_i / (sum_{j=1}^N w_j).

Define two estimators from this same reference bank:

hat s_A = -v^{-1} sum_{i=1}^N tilde w_i (y-a X_i),

hat s_B = exp(t) sum_{i=1}^N tilde w_i s_0(X_i).

All expectations below are over the reference bank with y and t fixed. Let

e_A = hat s_A - E[hat s_A],   e_B = hat s_B - E[hat s_B],

sigma_A^2 = E||e_A||^2,   sigma_B^2 = E||e_B||^2,   rho = E<e_A,e_B>.

## Task

Prove the following integrated theorem. First, the two centered errors are nonpositively aligned: rho <= 0 (and rho < 0 unless sum_{i=1}^N tilde w_i X_i is almost surely constant). Second, whenever D = sigma_A^2 + sigma_B^2 - 2 rho > 0, the function

J(lambda) = E||lambda e_A + (1-lambda)e_B||^2

has the unique minimizer over real lambda

lambda* = (sigma_B^2-rho)/(sigma_A^2+sigma_B^2-2rho),

with minimum value

J(lambda*) = (sigma_A^2 sigma_B^2-rho^2)/(sigma_A^2+sigma_B^2-2rho).

If rho < 0, prove additionally that 0 < lambda* < 1.
