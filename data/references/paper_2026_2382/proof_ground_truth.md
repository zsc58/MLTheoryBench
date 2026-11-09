# Reference Proof

Let H = L2(P_X) and G = L2(P_Z). Let W_1,...,W_n be iid draws from P. All expectations below are under P unless an empirical measure or a fold is explicitly specified.

## 1. Population targets and alpha targets

The bridge identity and the two Riesz identities imply

  E[m(W;h)] = <a_P,h>,
  E[tilde m(W;g)] = <r_P,g>,
  <Th,g> = <h,T*g>.

Write

  r_P = r_parallel + r_perp,  r_perp in ker(T*),
  a_P = a_parallel + a_perp,  a_perp in ker(T).

The projected-range assumptions imply that the least-squares sets are nonempty because

  ||Th-r_P||^2 = ||Th-r_parallel||^2 + ||r_perp||^2,

and the analogous identity holds for T* and a_P. The normal equations show that

  H_P = h + ker(T)
  and
  G_P = g + ker(T*)

for every h in H_P and g in G_P. Thus Th is common to H_P and T*g is common to G_P. The minimum-norm representatives satisfy

  Th_P^dagger = r_parallel,
  T*g_P^dagger = a_parallel,
  h_P^dagger in ker(T) perp,
  g_P^dagger in ker(T*) perp.

Consequently Psi(P) = <Th_P^dagger,g_P^dagger> is well defined and agrees with E[h_P^dagger(X)g_P^dagger(Z)].

If r_perp is nonzero, the residual-aware source condition gives a_parallel in ran(T*T). Equivalently, g_P^dagger is in ran(T). The minimization defining alpha_P^(h,dagger) therefore has a solution. For any minimizer alpha, the normal equation gives

  T*(T alpha-g_P^dagger) = 0.

Both T alpha and g_P^dagger belong to ran(T), so their difference belongs to ran(T) intersect ker(T*) = {0}. Hence

  T alpha_P^(h,dagger) = g_P^dagger.

The symmetric argument gives

  T* alpha_P^(g,dagger) = h_P^dagger

whenever a_perp is nonzero. Minimum-norm alpha representatives fix the population nuisance parametrization; the displayed projected identities hold for every minimizer. Inactive alpha coordinates and their errors are omitted.

The explicit attainment and measurable-selection convention in the task makes all empirical and regularized nuisance quantities used below well defined. No rate conclusion is drawn merely from that convention.

## 2. Exact bias identity

For a generic admissible tuple eta = (h,g,alpha^h,alpha^g,r_perp,a_perp), linearity gives

  E[chi(W;eta)]
  = <a_P,h> + <r_P,g> - <Th,g>
    + <r_perp,T alpha^h-g>
    + <a_perp,T* alpha^g-h>.

Substitute

  a_P = T*g_P^dagger + a_P,perp,
  r_P = Th_P^dagger + r_P,perp,
  Psi(P) = <Th_P^dagger,g_P^dagger>.

Using the bridge identity and expanding yields

  E[chi(W;eta)]-Psi(P)
  = -<T(h-h_P^dagger),g-g_P^dagger>
    + <r_perp,T alpha^h-g> + <r_P,perp,g>
    + <a_perp,T* alpha^g-h> + <a_P,perp,h>.

The correctly typed orthogonality relations are

  <r_P,perp,T alpha^h> = 0,
  <a_P,perp,T* alpha^g> = 0,

because r_P,perp is in ker(T*) and a_P,perp is in ker(T). Therefore

  E[chi(W;eta)]-Psi(P)
  = -<T(h-h_P^dagger),g-g_P^dagger>
    + <T alpha^h-g,r_perp-r_P,perp>
    + <T* alpha^g-h,a_perp-a_P,perp>.             (1)

The same formula holds with inactive coordinates deleted.

## 3. Nuisance guarantees and their logical scope

The task assumes attainment and measurable selection for every displayed optimization. The localized empirical-process conditions, source conditions, and class inclusions describe the intended learner construction. However, for arbitrary measurable classes they do not by themselves supply the additional translation, closure, restricted-population-curvature, or comparison-target geometry needed to derive the full unrestricted Tikhonov rate formulas. Accordingly, this proof does not assert those rate formulas as consequences of the displayed generic inequalities.

The theorem instead uses the direct assumptions stated in the task: all active strong nuisance errors converge to zero, the two primary weak/strong product conditions hold, and the two residual-debiasing product conditions hold. These are independent assumptions and are not inferred from a critical-radius lower bound. The explicit alpha regularization conditions and the conditional residual-class realizability conditions ensure that the corresponding auxiliary learner constructions are specified, but no unsupported rate implication is needed for the final inference result.

For completeness, conditional on the training data in fold k, put

  q_{0,k} = r_P - T hat h_{-k}.

The conditional realizability assumption places q_{0,k} in the residual class. The population excess squared-loss criterion for the residual learner is exactly

  ||q-q_{0,k}||_G^2.

Thus, whenever the stated localized comparison inequality is applied to this foldwise problem, empirical optimality compares the selected optimizer with q_{0,k}; the resulting auxiliary residual bound is not needed below because the direct residual strong-error condition is assumed explicitly. The adjoint statement is symmetric.

## 4. Correct cross-fitted expansion

Let the fixed folds be I_1,...,I_K, with n_k = |I_k| and sum_k n_k=n. Set w_k=n_k/n and P_{n,k}f=n_k^{-1} sum_{i in I_k} f(W_i). For i in I_k, let eta_hat,-k denote the nuisance tuple trained without I_k, including the independent first stages required for the alpha and residual learners. Define

  chi_k(w)=chi(w;eta_hat,-k),
  chi_P(w)=chi(w;eta_P),
  phi_P(w)=chi_P(w)-Psi(P).

The estimator is

  hat Psi = sum_k w_k P_{n,k} chi_k.

Therefore

  sqrt(n)(hat Psi-Psi(P))
  = sqrt(n) sum_k w_k(P_{n,k}-P)chi_P
    + sqrt(n) sum_k w_k(P_{n,k}-P)(chi_k-chi_P)
    + sqrt(n) sum_k w_k(P chi_k-Psi(P)).       (2)

The first term is exactly

  n^(-1/2) sum_{i=1}^n phi_P(W_i).

Conditional on the training data for fold k, the observations in I_k are iid from P. Mean-square continuity, the high-probability sup-norm bounds, and the strong errors give

  E[(chi_k(W)-chi_P(W))^2 | training data]
  <= C[(e_h^s)^2+(e_g^s)^2+(e_alpha^h,s)^2+(e_alpha^g,s)^2
        +(e_rperp^s)^2+(e_aperp^s)^2].

The task applies these error conditions to the finite collection of foldwise nuisance estimates. Because K is fixed, the right side is o_p(1). Conditional Chebyshev applied fold by fold gives

  sqrt(n) sum_k w_k(P_{n,k}-P)(chi_k-chi_P)=o_p(1).       (3)

For the population remainder, apply (1) fold by fold. Cauchy-Schwarz and the identities for the population alpha targets give

  |P chi_k-Psi(P)|
  <= min{e_g^w e_h^s,e_g^s e_h^w}
     +(e_alpha^h,w+e_g^s)e_rperp^s
     +(e_alpha^g,w+e_h^s)e_aperp^s.

The assumed product-rate conditions imply

  sqrt(n) sum_k w_k(P chi_k-Psi(P))=o_p(1).       (4)

Combining (2), (3), and (4) proves

  sqrt(n)(hat Psi-Psi(P))
  = n^(-1/2) sum_{i=1}^n [chi(W_i;eta_P)-Psi(P)] + o_p(1).

## 5. Limit distribution

The variables phi_P(W_i) are iid, have mean zero, and have finite variance sigma_P^2. Since 0<sigma_P^2<infinity, the ordinary Lindeberg-Feller central limit theorem gives

  n^(-1/2) sum_i phi_P(W_i) => N(0,sigma_P^2).

The claimed asymptotic normality follows from the expansion and Slutsky's theorem.

## 6. Variance consistency

For i in I_k define the estimated score chi_hat,i=chi(W_i;eta_hat,-k), and set

  hat sigma^2=n^(-1)sum_i(chi_hat,i-hat Psi)^2.

The conditional second-moment bound and the finite-fold strong consistency assumptions imply

  n^(-1)sum_i(chi_hat,i-chi_P(W_i))^2=o_p(1).

This follows by conditional Markov inequality on each fold and a finite-fold union bound. The reverse triangle inequality for the empirical L2 norm then gives

  |hat sigma-[n^(-1)sum_i(chi_P(W_i)-n^(-1)sum_j chi_P(W_j))^2]^(1/2)|=o_p(1).

Since chi_P is square integrable, the iid law of large numbers gives convergence of the expression under the square root to Var_P(chi_P(W))=sigma_P^2. Because sigma_P>0, hat sigma converges in probability to sigma_P.
