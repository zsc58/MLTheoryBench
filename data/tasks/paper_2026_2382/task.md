# Problem

## Setup

Let W_1,...,W_n be iid draws from a law P, with W_i=(X_i,Y_i,Z_i). Let H=L2(P_X) and G=L2(P_Z). Let T:H -> G be bounded with adjoint T*, and assume

  E[h(X)g(Z)] = <Th,g>_G = <h,T*g>_H

for every h in H and g in G. Let m(W;h) and tilde m(W;g) be known measurable linear maps with continuous Riesz representers a_P in H and r_P in G:

  E[m(W;h)] = <a_P,h>_H,
  E[tilde m(W;g)] = <r_P,g>_G.

Decompose

  r_P = r_P,parallel + r_P,perp,
  a_P = a_P,parallel + a_P,perp,

where r_P,parallel is the projection onto closure(ran T), r_P,perp is in ker(T*), a_P,parallel is the projection onto closure(ran T*), and a_P,perp is in ker(T). Assume

  r_P,parallel in ran T,
  a_P,parallel in ran T*.

Define

  H_P = argmin_h ||Th-r_P||_G^2,
  G_P = argmin_g ||T*g-a_P||_H^2,

and define h_P^dagger and g_P^dagger to be the minimum-H-norm and minimum-G-norm elements of H_P and G_P. Set

  Psi(P) = <Th_P^dagger,g_P^dagger>_G = E[h_P^dagger(X)g_P^
 dagger(Z)].

If r_P,perp is nonzero, assume a_P,parallel is in ran(T*T), and define alpha_P^(h,dagger) as the minimum-norm minimizer of ||T alpha-g_P^dagger||_G^2. If r_P,perp is zero, omit alpha^h and set all associated errors to zero. If a_P,perp is nonzero, assume r_P,parallel is in ran(TT*), and define alpha_P^(g,dagger) as the minimum-norm minimizer of ||T* alpha-h_P^dagger||_H^2. If a_P,perp is zero, omit alpha^g and set all associated errors to zero.

Assume the projected source conditions

  r_P,parallel in ran((TT*)^((beta_h+1)/2)),
  a_P,parallel in ran((T*T)^((beta_g+1)/2)),
  beta_h,beta_g >= 0.

## Nuisance learners and assumptions

For each fold, let H_n,G_n,G_n^r,H_n^a and their adjoint-symmetric classes be measurable classes containing zero and the population and regularized targets used in the corresponding optimization problems. Define the regularized targets, for positive lambda, by

  h_P,lambda = argmin_h {||Th-r_P||_G^2+lambda||h||_H^2},
  g_P,lambda = argmin_g {||T*g-a_P||_H^2+lambda||g||_G^2},

and, on active sides,

  alpha_P,lambda^h = argmin_alpha {||T alpha-g_P^dagger||_G^2+lambda||alpha||_H^2},
  alpha_P,lambda^g = argmin_alpha {||T* alpha-h_P^dagger||_H^2+lambda||alpha||_G^2}.

Assume the relevant population and regularized targets belong to their stated classes. Assume the inclusions, whenever the corresponding coordinate is active,

  T(h_P^dagger-H_n) subset G_n,
  T(alpha_P^(h,dagger)-H_n) subset G_n,
  T*(g_P^dagger-G_n) subset H_n,
  T*(alpha_P^(g,dagger)-G_n) subset H_n.

Assume mean-square continuity

  E[tilde m(W;g)^2] <= C||g||_G^2,
  E[m(W;h)^2] <= C||h||_H^2,

and uniform boundedness of the function and criterion components in the six displayed learner optimizations, including their population and regularized targets. For each of the six optimizations, assume the centered empirical criterion difference between every admissible candidate f and its explicitly corresponding population or regularized comparison target f_0 is, on an event of probability at least 1-zeta, bounded by

  C delta_{j,n}||f-f_0||+C delta_{j,n}^2,

uniformly over the relevant candidate class, where j ranges over h, g, alpha^h, alpha^g, r_perp, and a_perp, and

  delta_{j,n} >= c sqrt((log log n + |log zeta|)/n).

All displayed population, regularized, and foldwise empirical argmin and argmax problems are assumed to attain their stated optima, and a measurable optimizer is selected for each one, with a fixed measurable rule for ties. Thus every nuisance estimate and the resulting estimator is defined. This is a well-definedness convention for the optimization notation.

For active alpha^h, assume lambda_alpha^h,n decreases to zero and

  (delta_alpha^h,n^2+||hat g-g_P^dagger||_G^2)/lambda_alpha^h,n ->p 0.

Assume the symmetric condition for active alpha^g. The direct strong-error and product-rate conditions below are imposed separately and are not inferred from the radius lower bounds alone.

Define the primary learner by

  hat h = argmin_{h in H_n} max_{g in G_n}
    P_n[2{tilde m(W;g)-h(X)g(Z)}-g(Z)^2+lambda_h h(X)^2],

and define the adjoint-symmetric learner by

  hat g = argmin_{g in G_n} max_{h in H_n}
    P_n[2{m(W;h)-g(Z)h(X)}-h(X)^2+lambda_g g(Z)^2].

For active alpha^h, using a first-stage hat g trained independently of the sample in this criterion, define

  hat alpha^h = argmin_{alpha in H_n} max_{g in G_n}
    P_n[2{hat g(Z)g(Z)-alpha(X)g(Z)}-g(Z)^2
         +lambda_alpha^h alpha(X)^2].

Define hat alpha^g symmetrically, using an independent first-stage hat h. Define the residual learners by the exact squared-loss regressions

  hat r_perp = argmax_{q in G_n^r} P_n[2{tilde m(W;q)-hat h(X)q(Z)}-q(Z)^2],

and, symmetrically,

  hat a_perp = argmax_{q in H_n^a} P_n[2{m(W;q)-hat g(Z)q(X)}-q(X)^2].

For every cross-fitting fold k, require the conditional residual realizability conditions

  r_P-T hat h_{-k} belongs to G_{n,k}^r,
  a_P-T* hat g_{-k} belongs to H_{n,k}^a

almost surely given the corresponding training data. All first stages used inside a learner are trained on data independent of the empirical average defining that learner. Partition the iid observations into a fixed finite number of folds I_1,...,I_K, with n_k=|I_k| and sum_k n_k=n. Nuisances evaluated on fold I_k are trained without observations in I_k.

## Errors and rate conditions

Define

  e_h^s=||hat h-h_P^dagger||_H,
  e_h^w=||T(hat h-h_P^dagger)||_G,
  e_g^s=||hat g-g_P^dagger||_G,
  e_g^w=||T*(hat g-g_P^dagger)||_H,

  e_alpha^h,s=||hat alpha^h-alpha_P^(h,dagger)||_H,
  e_alpha^h,w=||T(hat alpha^h-alpha_P^(h,dagger))||_G,

with symmetric definitions for e_alpha^g,s and e_alpha^g,w, and

  e_rperp^s=||hat r_perp-r_P,perp||_G,
  e_aperp^s=||hat a_perp-a_P,perp||_H.

For inactive coordinates, the associated errors are zero. For each fixed fold, the corresponding foldwise versions of these errors are used below; all displayed convergence, product-rate, and sup-norm conditions apply to the finite collection of foldwise nuisance versions. Assume all active strong errors are o_p(1),

  sqrt(n) min{e_g^w e_h^s, e_g^s e_h^w}=o_p(1),

and

  sqrt(n)[(e_alpha^h,w+e_g^s)e_rperp^s
           +(e_alpha^g,w+e_h^s)e_aperp^s]=o_p(1).

Assume the high-probability sup-norm condition

  max{||hat h||_infty^2, ||h_P^dagger||_infty^2,
      ||g_P^dagger||_infty^2,
      ||alpha_P^(h,dagger)||_infty^2,
      ||alpha_P^(g,dagger)||_infty^2,
      ||hat r_perp||_infty^2,
      ||hat a_perp||_infty^2} <= C

with probability tending to one, omitting inactive alpha targets and inactive residual estimates. Finally assume 0<sigma_P^2<infinity, where sigma_P^2 is defined below.

## Task

Let

  chi(W;eta) = m(W;h)+tilde m(W;g)-h(X)g(Z)
    +r_perp(Z){alpha^h(X)-g(Z)}
    +a_perp(X){alpha^g(Z)-h(X)}.

For eta_P=(h_P^dagger,g_P^dagger,alpha_P^(h,dagger),alpha_P^(g,dagger),r_P,perp,a_P,perp), with inactive coordinates omitted, define the weighted cross-fitted estimator

  hat Psi = sum_k (n_k/n) P_{n,k}[chi(W;eta_hat,-k)].

Prove that

  sqrt(n)(hat Psi-Psi(P))
  = n^(-1/2) sum_i [chi(W_i;eta_P)-Psi(P)] + o_p(1)
  => N(0,sigma_P^2),

where

  sigma_P^2 = Var_P(chi(W;eta_P)).

Define the cross-fitted estimated-score standard deviation by

  hat sigma^2 = n^(-1) sum_i [chi(W_i;eta_hat,-k(i))-hat Psi]^2.

Prove that hat sigma converges in probability to sigma_P.
