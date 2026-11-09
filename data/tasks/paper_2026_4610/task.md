# Problem

## Setup

Let `M>1` and `C>=1` be integers. For each member `m=1,...,M`, let `x^(m)` lie in the probability simplex `Delta^(C-1)`. Define the componentwise ensemble mean and stabilized spread by

`mu_c = (1/M) sum_m x_c^(m)`,

`sigma_c = sqrt((1/(M-1)) sum_m (x_c^(m)-mu_c)^2) + epsilon`,

where `epsilon>0`. Thus `mu_c>=0` and `sigma_c>0`. Let each classwise scale satisfy `kappa_c>0`, and define the gate

`G_c = 1 - exp(-mu_c/(kappa_c sigma_c))`.

For the sensitivity and asymptotic statements, consider the scalar function

`F(u,v,w) = 1 - exp(-u/(w v))`,

on `[0,infinity) x (0,infinity) x (0,infinity)`, so that `G_c=F(mu_c,sigma_c,kappa_c)`. Partial derivatives refer to the independent arguments of `F`, with the other two arguments held fixed, and are evaluated at the ensemble statistics when describing `G_c`. At `u=0`, interpret the derivative with respect to `u` as the right-hand derivative.

## Task

Prove that `F` is monotone increasing in its first argument and monotone nonincreasing in its second and third arguments, and determine when these monotonicities are strict. Derive the three partial derivatives and their exact values at `u=0`, thereby giving the classwise sensitivities and their boundary behavior when `mu_c=0`.

Show also that, for every fixed pair `v>0` and `w>0`, as `u/(w v)` tends to infinity, `F(u,v,w)` tends to `1` and all three partial derivatives tend to zero. This last assertion is an asymptotic statement about `F` on its stated scalar domain, not an assertion that ensemble probability means can tend to infinity.
