# Problem

## Setup

Let S be finite and fix a deterministic policy. Its transition matrix P is row-stochastic and its one-step reward vector is r >= 0. Fix gamma in [0,1). The discounted value column v is the unique solution of v = gamma P v + r.

For a row-stochastic K, restart probability row vector u, and c in [0,1), define PageRank w as the unique probability row vector satisfying w = c w K + (1-c)u.

For each irreducible recurrent block P^(k), let mu^(k) be its positive stationary distribution, D_k=diag(mu^(k)), and (P^(k))* = D_k^{-1}(P^(k))^T D_k. Write <q>_mu = sum_s mu(s)q(s).

Permute states into irreducible transient diagonal blocks Q^(1),...,Q^(m) and irreducible recurrent stochastic diagonal blocks P^(1),...,P^(ell), with transitions between distinct blocks only to later blocks in a downstream order. Let P_{T_j,d} denote the transition block from transient class T_j to a downstream block d. For each transient block set lambda_j=rho(Q^(j)). When lambda_j>0, let nu_j be its positive probability row vector satisfying nu_j Q^(j)=lambda_j nu_j, set D_nu_j=diag(nu_j), and define the row-stochastic kernel B_j=lambda_j^{-1}D_nu_j^{-1}(Q^(j))^T D_nu_j.

## Task

Prove the following integrated theorem. For every recurrent block with a_k=<r^(k)>_{mu^(k)}>0, set u_k(s)=mu^(k)(s)r^(k)(s)/a_k. If w_k is PageRank for (P^(k))* with teleportation gamma and restart u_k, then

v^(k)(s) = a_k w_k(s) / ((1-gamma)mu^(k)(s)).

If r^(k) is identically zero, then v^(k)=0. Process transient classes in reverse downstream order. Define bvec^(j)=r^(j)+gamma sum_{d downstream} P_{T_j,d}v^(d). For each transient block with lambda_j>0 and bvec^(j) not identically zero, set b_j=<bvec^(j)>_{nu_j}, and let w_j be PageRank for B_j with teleportation gamma lambda_j and restart nu_j(s)bvec^(j)(s)/b_j. Prove

v^(j)(s) = b_j w_j(s) / ((1-gamma lambda_j)nu_j(s)).

If bvec^(j) is identically zero, then v^(j)=0. If lambda_j=0, prove that Q^(j) is a singleton zero block and v^(j)=bvec^(j). Together these classwise formulas and the downstream recursion yield the unique global discounted policy value v.
