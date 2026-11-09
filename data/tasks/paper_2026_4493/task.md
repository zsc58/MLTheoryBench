# Problem

## Setup

Let d be a positive integer, let I=[t0,t1] be a nonempty compact interval, and let g:I->R^d be C^2, with every coordinate g_i(t) nonzero. Fix tau_1,tau_2>0 and let m,v solve, coordinatewise,

tau_1 m'(t)=-m(t)+g(t),    tau_2 v'(t)=-v(t)+g(t)^2,

with arbitrary initial values m(t0),v(t0) in R^d. Define the normalized update R_i(t)=m_i(t)/sqrt(v_i(t)) whenever v_i(t)>0, and let

P={t in I: v_i(t)>0 for every i}.

For each coordinate define the logarithmic scale drift delta_i(t)=g_i'(t)/g_i(t). In the discrete parametrization, beta_j=exp(-Delta t/tau_j) for a common Delta t>0.

For this problem, a first-order scale-drift decomposition means the explicit non-tautological decomposition required in the Task, with its remainder fixed by that formula. The coefficient a_i is, by definition, the coefficient of the displayed term linear in delta_i in that prescribed decomposition; it may not be changed by absorbing such a term into the remainder. On a nonempty interval contained in P, the flow is first-order gradient-scale invariant exactly when these canonical coefficients a_i are all identically zero there.

## Task

Prove the following integrated claim. On every nonempty subinterval contained in P, each coordinate admits a canonical decomposition

R_i(t)=sign(g_i(t)) [1+(tau_2-tau_1) delta_i(t)] + E_i(t),

where E_i is given by an explicit non-tautological formula in terms of the stated ODE data, initial moments, tau_1,tau_2, g, and its derivatives, and where on every nonempty compact subinterval of P its magnitude has a quantitative finite bound depending only on those data and lower bounds that keep the normalization defined (the bound may not use R_i or E_i itself). Conclude that, on every nonempty interval contained in P, the flow is first-order gradient-scale invariant if and only if tau_1=tau_2, equivalently beta_1=beta_2.
