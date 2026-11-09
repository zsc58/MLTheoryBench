# Problem

## Setup

Let D be an integer with D >= 1. Define the global domain X_1 = [0,1]^D and, for a side length L with 0 < L <= 1, the domain X_L = [0,L]^D. Fix c > 0 and set ell_1 = c sqrt(D) and ell_L = c L sqrt(D). Let kappa be a fixed profile such that, for ell in {ell_1, ell_L},

k_ell(x,x') = kappa(||x - x'||_2 / ell)

is a valid isotropic stationary kernel on the relevant domain. A zero-mean Gaussian process with this kernel is observed with independent Gaussian noise of variance sigma_epsilon^2 > 0. For an N-point design X = (x_1,...,x_N), let K_XX be its kernel Gram matrix.

Define the information gain of X by

IG(X) = (1/2) log det(I_N + sigma_epsilon^{-2} K_XX),

and define the maximum information gain over a domain A by

gamma_N(A,k) = sup_{X subset A, |X| = N} IG(X).

## Task

Prove that, for every integer N >= 1,

gamma_N(X_1,k_{ell_1}) = gamma_N(X_L,k_{ell_L}).
