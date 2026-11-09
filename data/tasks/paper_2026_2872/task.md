# Problem

## Setup

Let T,d be positive integers, and let p_max,C_theta>0 be fixed structural constants. Contexts belong to a set C contained in the Euclidean unit ball in R^d. An unknown fixed parameter theta satisfies ||theta||_2<=C_theta, and the utility is u(c)=c^T theta>=0 for every c in C. A supplied nondegenerate compact interval U=[u_min,u_max] contains all these utilities.

The complete context sequence (c_t)_{t=1}^T is generated exogenously and is independent of both the demand-noise sequence and all seller randomization. It need not be iid or satisfy a covariance condition. At round t the seller observes c_t, chooses p_t in [0,p_max], and observes only y_t=1{u(c_t)+xi_t>=p_t}. The noises xi_t are iid, independent of the contexts, and have mean zero. Their unknown tail is g(x)=Pr(xi_t>=x). For every admissible context c, assume u(c)+xi_t lies in [0,p_max] almost surely.

A policy is nonanticipating: its price is a measurable function of the current context, past observed contexts, prices and binary outcomes, supplied structural information, and independent internal randomization. It is not given theta, g, future contexts, or unobserved valuations and noises.

Set V=p_max+max{|u_min|,|u_max|}. Fix beta>=2 and L_g>0, and write s=floor(beta). Assume g restricted to [-V,V] is s times continuously differentiable, with

max_{1<=k<=s} ||g^{(k)}||_infinity <= L_g,

and, for every x,x' in [-V,V],

|g(x')-sum_{k=0}^s g^{(k)}(x)(x'-x)^k/k!| <= L_g |x'-x|^beta.

For u in U and p in [0,p_max], define r(u,p)=p g(p-u). For every u in U this revenue has a unique maximizer p*(u) in (0,p_max). Assume fixed constants 0<sigma_r<=L_r satisfy, for all such u,p,

(sigma_r/2)|p-p*(u)|^2 <= r(u,p*(u))-r(u,p) <= (L_r/2)|p-p*(u)|^2.

Define the random regret of a policy by

R_T=sum_{t=1}^T [r(u(c_t),p*(u(c_t)))-r(u(c_t),p_t)].

The expectation includes demand noise, seller randomization, and any random contexts. The notation ~O suppresses logarithmic factors and constants associated with fixed structural parameters and fixed numerical structural tuning, including beta, but not polynomial dependence on d or T. Structural tuning is permitted as a supplied numerical input; it is not a revelation of theta or the tail function. The upper guarantee below is instance-wise when that tuning is instance-wise, and uniform when common structural tuning bounds are supplied for a class.

The policy constructed for the upper bound may interleave its pricing rounds with exploration rounds using a fresh price P_t uniform on [0,p_max], independent of the past and the demand noises. On those rounds it may use z_t=p_max y_t in a ridge estimate. Its exploration indicators must be determined by observed contexts and previous exploration indicators, without pricing feedback. Its scalar pilots use only contexts and exploration-side observations and randomization. Conditional on the whole resulting pilot stream and its length, the demand noises on the remaining pricing rounds must retain their iid law and the pricing-side randomization must remain fresh. These requirements concern the constructed policy only; they do not restrict the policies in the lower bound.

## Normalized Class

Let P_norm denote the class of instances with d=1, p_max=C_theta=theta=1, u(c)=c, and C contained in [0,1], satisfying the preceding model and structural assumptions on their supplied utility interval. The context space is not required to equal [0,1]. Require additionally that, for every u in that interval,

[p*(u)-1/16,p*(u)+1/16] is contained in (0,1),

and -partial_{pp}r(u,p)>=sigma_r/2 whenever |p-p*(u)|<=1/16.

The structural constants have common finite upper bounds and, where applicable, positive lower bounds independent of T. For the lower theorem these common bounds may be chosen once, depending on beta, and then held fixed. The class includes exogenous iid context laws as well as other exogenous context sequences allowed by the setup. The supplied interval and structural information are available to the policy in both the upper and lower experiments.

## Task

Prove the following integrated theorem. There is a structurally tuned coarse-to-fine pricing policy that partitions the utility interval into bins, localizes a price in each bin using coarse grid prices, refines using a trust-region polynomial price in each bin, and uses adaptive scalar-pilot exploration for the linear utility model, with the following guarantee: for fixed valid numerical structural tuning there are constants A,B>0 independent of d,T and the realized context sequence such that, for all T>=max{A,Bd},

E R_T=~O(T^{(2beta-1)/(4beta-3)}+sqrt(dT)).

The policy and constants can be chosen uniformly on P_norm with its common structural bounds.

Moreover, there are a choice of the common structural bounds defining P_norm, a constant c_beta>0, and a threshold T_beta such that, for every T>=T_beta and every nonanticipating pricing policy pi,

sup_{I in P_norm} E_pi^I R_T >= c_beta T^{(2beta-1)/(4beta-3)}.

The instance inside this supremum may depend on pi and T. Thus the horizon exponent is minimax sharp for fixed dimension, up to logarithmic factors.
