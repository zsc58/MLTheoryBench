# Problem

## Setup

Let R be a nonnegative integer. Let X be a Polish space with Borel sigma-algebra and reference measure mu, and let Z be a measurable space. For each r=0,...,R, let nu_r be a sigma-finite reference measure on Z and let Q_{s_r}(dz | x) be a Markov kernel from X to Z with a jointly measurable density q_{s_r}(z | x) with respect to nu_r. The noise levels satisfy

0 < s_0 <= s_1 <= ... <= s_R.

Fix an observation y, a measurable prior density p(x) with integral p(x) mu(dx)=1, and a measurable nonnegative likelihood ell(x)=p(y | x). Use the convention t^0=1 for every t>=0. Fix

0 = lambda_R <= lambda_{R-1} <= ... <= lambda_1 <= lambda_0 = 1,

and assume, for every r,

0 < Z_r = integral p(x) ell(x)^(lambda_r) mu(dx) < infinity.

Define

pi_r(dx) = Z_r^(-1) p(x) ell(x)^(lambda_r) mu(dx),

and

eta_r(dz) = integral pi_r(dx) Q_{s_r}(dz | x).

For each r define

m_r(z) = integral p(u) ell(u)^(lambda_r) q_{s_r}(z | u) mu(du).

Fix one point x_star in X. For 0 < m_r(z) < infinity, define the exact reconstruction kernel by

K_r(dx | z) = m_r(z)^(-1) p(x) ell(x)^(lambda_r) q_{s_r}(z | x) mu(dx).

For m_r(z)=0 or m_r(z)=infinity, set K_r(dx | z)=delta_{x_star}(dx). This arbitrary convention is immaterial because eta_r assigns zero mass to the exceptional set. For r>=1, set P_{r-1}=Q_{s_{r-1}}.

For each r=R,...,1, define the proposal probability measure M_r on (z_r,x,z_{r-1}) by

M_r(dz_r,dx,dz_{r-1}) = eta_r(dz_r) K_r(dx | z_r) P_{r-1}(dz_{r-1} | x).

Define the normalized extended stage target GammaBar_{r-1} by its density with respect to nu_r(dz_r) mu(dx) nu_{r-1}(dz_{r-1}):

dGammaBar_{r-1}/d(nu_r x mu x nu_{r-1})
 = Z_{r-1}^(-1) p(x) ell(x)^(lambda_{r-1})
   q_{s_r}(z_r | x) q_{s_{r-1}}(z_{r-1} | x).

The exact stagewise incremental factor is the Radon-Nikodym derivative

W_r = dGammaBar_{r-1}/dM_r

on the support of M_r. Use the measurable version W_r=(Z_r/Z_{r-1})G_r(x) wherever the factor is evaluated, where

G_r(x)=ell(x)^(lambda_{r-1}-lambda_r).

This version agrees with the Radon-Nikodym derivative M_r-almost everywhere. Assume that each G_r is bounded and measurable and that pi_r(G_r)>0.

Initialize N particles iid from eta_R with weights 1/N. At each stage r=R,R-1,...,1, reconstruct each particle independently using K_r, apply W_r (equivalently, its common positive stagewise rescaling G_r when weights are normalized), and let D_{r,N} be the resulting total unnormalized weight. If D_{r,N}>0, normalize the weights by D_{r,N}; if D_{r,N}=0, retain the normalized weights entering that stage as the fallback. Then optionally resample with a scheme satisfying the following consistency property, and propagate with P_{r-1}:

if a weighted particle system converges in probability, for every bounded measurable test function, to a probability measure rho, then the equally weighted system output by the resampling scheme also converges in probability for every bounded measurable test function to rho.

If resampling is omitted, retain the current normalized weights; if it is performed, reset all post-resampling weights to 1/N. All conditional particle draws at each mutation step are independent given the input particles. The exact factor is applied in the reconstruct-weight-resample-propagate order; the proof must verify that this order is equivalent to the proposal-based Radon-Nikodym definition above.

At the end, reconstruct independently with K_0. If the final clean particles are x_0^(1),...,x_0^(N) and their final normalized weights are w_0^(1),...,w_0^(N), define

widehat pi_{0,N} = sum_i w_0^(i) delta_{x_0^(i)}.

## Task

Prove that, as N tends to infinity, for every bounded measurable h,

sum_i w_0^(i) h(x_0^(i)) -> integral h(x) pi_0(dx)

in probability. Since bounded continuous functions are bounded measurable, conclude that widehat pi_{0,N} converges weakly in probability to pi_0. Finally identify pi_0(dx)=p(x | y) mu(dx). Do not claim that weak convergence is logically equivalent to convergence for every bounded measurable test function; the latter is the stronger assertion requested here.

## Definition of the consistency property

All conditional particle draws at each mutation step are independent given the input particles. The resampling condition above is the only property of the resampling mechanism needed by the theorem; it is satisfied by the standard consistency-preserving SMC schemes covered by the source theorem. The zero-total-weight fallback is a finite-sample definition only; under the stated assumptions its probability tends to zero at every fixed stage and it does not alter the limiting target.
