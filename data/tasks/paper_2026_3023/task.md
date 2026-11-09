# Problem

## Setup

Let `S` and `A` be finite nonempty state and action sets. For each state `s`, let `A_s` be a nonempty subset of `A` consisting of the actions available at that state. Fix a discount rate `r>0`, an initial probability distribution `rho` on `S`, an entropy temperature `tau>0`, and a radius `epsilon>=0`.

Let `Theta` be a nonempty parameter set. For each `theta in Theta`, each `s in S`, and each `a in A_s`, let `lambda_theta^a(s,s')` (`s' != s`) be finite nonnegative transition rates, with diagonal entries chosen so each generator row sums to zero, and let `R_theta(s,a)` be a finite strictly positive instantaneous reward.

A stationary randomized policy `pi` assigns a probability distribution on `A_s` at each state `s`. Let `mu` be a reference policy assigning a strictly positive probability to every action in `A_s`. Under `(theta,pi)`, the controlled CTMC starts from `rho` and has rates

`lambda_theta^pi(s,s') = sum_{a in A_s}pi(a|s)lambda_theta^a(s,s')`.

The policy and initial distribution remain unchanged when the model parameter is perturbed. Write `E_theta^pi` for expectation under this CTMC law.

Define the normalized discounted state occupancy

`bar d_{rho,theta}^pi(s) = r E_theta^pi[int_0^infty exp(-rt) 1{S_t=s} dt]`.

For each nominal parameter `theta` under consideration, assume common jump support with every perturbed parameter `tilde theta in Theta`: for every `s' != s` and `a in A_s`, `lambda_theta^a(s,s')` and `lambda_tilde theta^a(s,s')` are either both positive or both zero.

Define

`ell(lambda_theta^a,lambda_tilde theta^a)(s) = sum_{s' != s} [lambda_theta^a(s,s') log(lambda_theta^a(s,s')/lambda_tilde theta^a(s,s')) - (lambda_theta^a(s,s')-lambda_tilde theta^a(s,s'))]`,

where a summand with two zero rates is zero. Set

`c_theta,tilde theta(s,a) = ell(lambda_theta^a,lambda_tilde theta^a)(s) - r log(R_tilde theta(s,a)/R_theta(s,a))`.

For fixed `(theta,pi)`, let `C_{tau,epsilon}^pi(theta)` be the set of `tilde theta in Theta` satisfying

`sum_s bar d_{rho,theta}^pi(s) tau log[sum_{a in A_s} mu(a|s) exp(c_theta,tilde theta(s,a)/tau)] <= epsilon`.

The robust performance of this policy is

`inf_{tilde theta in C_{tau,epsilon}^pi(theta)} E_tilde theta^pi[int_0^infty exp(-rt) sum_{a in A_{S_t}} pi(a|S_t) R_tilde theta(S_t,a) dt]`.

Define

`KL(pi(.|s)||mu(.|s)) = sum_{a in A_s} pi(a|s) log(pi(a|s)/mu(a|s))`,

with the convention `0 log(0/x)=0` for `x>0`.

## Task

Prove that, for every nominal model `theta` satisfying the common-support assumption and every stationary randomized policy `pi`,

`inf_{tilde theta in C_{tau,epsilon}^pi(theta)} E_tilde theta^pi[int_0^infty exp(-rt) sum_{a in A_{S_t}} pi(a|S_t) R_tilde theta(S_t,a) dt]`

is at least

`exp( E_theta^pi[int_0^infty exp(-rt) (sum_{a in A_{S_t}} pi(a|S_t) r log R_theta(S_t,a) - tau KL(pi(.|S_t)||mu(.|S_t))) dt] - epsilon/r - log r )`.
