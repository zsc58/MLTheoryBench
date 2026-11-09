# Problem

## Setup

For each channel i in {1,...,d}, let s_{i,k}=(tau_{i,k|k})^2 denote its estimated scale at time k, initialized at a fixed, deterministic finite value s_{i,0}. Let E_{i,k} be the realized nonnegative variational error entering the scale update. In a steady regime, the prior degrees of freedom nu_i^- is a positive constant and the forgetting factor is

rho_i=nu_i^-/(nu_i^-+1),

so 0<rho_i<1. The one-step update is

s_{i,k}=[nu_i^- s_{i,k-1}+E_{i,k}]/(nu_i^-+1)
       =rho_i s_{i,k-1}+(1-rho_i)E_{i,k}.

Assume that, for each i, (E_{i,k})_{k>=1} is weakly stationary with

E[E_{i,k}]=sigma_i^2,    Var(E_{i,k})=eta_i^4<infinity.

For the variance assertion below, additionally assume temporal independence of the errors and independence from the initialization.

## Task

Prove that, for every channel i:

1. The scale estimate is asymptotically unbiased: lim_{k->infinity} E[s_{i,k}]=sigma_i^2.
2. Under the additional temporal-independence assumption,
   lim_{k->infinity} Var(s_{i,k})=((1-rho_i)/(1+rho_i))eta_i^4=eta_i^4/(2nu_i^-+1).
3. The EWMA tracking time constant, defined by the e-folding decay of weights rho_i^r across r sampling intervals, is T_i=-1/log rho_i.
