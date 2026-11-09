# Problem

## Setup

Let X in R^d, response Y, parameter w in R^q, differentiable loss ell(w;X,Y), population risk L(w)=E ell(w;X,Y), and complete stochastic gradient g(w;X,Y)=nabla_w ell(w;X,Y). Assume differentiation and expectation commute, so nabla L(w)=E g(w;X,Y). Missingness is represented by a mask M in {0,1}^d, where 1 means missing. Let V be the always-observed part of X; coordinates that are always observed have zero missingness probability.

A single fixed, data-independent imputation rule is used independently for each observation and at every missingness scale. It may depend on the observed covariates and the missingness pattern, and it leaves observed entries unchanged. Its auxiliary randomness xi is conditionally independent of the original-mask and additional-thinning randomization given (X,Y). For a deterministic missing set A, let Gamma_A(w;X,Y,xi) denote the resulting gradient when exactly A is declared missing, and let Gamma_emptyset=g. Assume E||Gamma_A(w)||^2<infinity for every fixed w and A. For every subset A of potentially missing coordinates, also assume sup over admissible pi of E[(product over j in A of a_j(V))||Gamma_A(w)||]<infinity for each fixed w. No raw-gradient moment bound uniform over all w in R^q is imposed.

For potentially missing coordinates, pi_j>=0, the missingness mechanism is conditionally independent of the complete data given V, and, conditional on (X,Y,V), mask coordinates are independent with Pr(M_j=1 | X,Y,V)=Pr(M_j=1 | V)=pi_j a_j(V). Under hMCAR, a_j(V)=1. Under sMAR, a_j(V)=q_j(V), where q_j is a fixed nonnegative measurable function with E q_j(V)=1. In either case pi_j is the marginal missingness probability, and admissible probabilities satisfy 0<=pi_j a_j(V)<=1 almost surely. This formulation includes pi_j=0. The intensity functions, complete-data law, and imputation law are held fixed as pi tends to zero.

Write B(w,pi)=E[Gamma_{S(M)}(w)]-nabla L(w), where S(M)={j:M_j=1}.

Fix lambda>1 and restrict to pi satisfying lambda pi_j a_j(V)<=1 almost surely for every potentially missing j. Generate M^(pi) first. Conditional on the complete data and M^(pi), generate independent Bernoulli bits r_j, independently of xi, with retention probabilities (1-lambda pi_j a_j(V))/(1-pi_j a_j(V)); set r_j=1 on always-observed coordinates. Set M_j^(lambda pi)=1-(1-M_j^(pi))r_j. Impute once under M^(lambda pi) using the fixed rule and one auxiliary draw. Keep the resulting covariates for the higher-scale gradient ghat^(lambda pi)(w). To obtain the linked lower-scale gradient ghat^(pi)(w), restore entries hidden only by the additional thinning with the complete values that were observed before thinning, leaving originally missing entries at their higher-scale imputations. Define ghat_R(w)=(lambda ghat^(pi)(w)-ghat^(lambda pi)(w))/(lambda-1). Require E||ghat^(pi)(w)||<infinity for every fixed w and every admissible pi, so its population mean is an ordinary finite expectation.

Assume L is alpha-strongly convex and beta-smooth on R^q, with alpha>0, beta>0, and minimizer w*. For each one-pass SGD algorithm, let (F_k) be its history filtration and let w_k be F_k-measurable. Conditional on F_k, the iteration-k observation, mask, thinning, and auxiliary imputation variables have the population law specified above; the gradient is evaluated at w_k. For plain SGD, ghat_k is the directly imputed gradient Gamma_{S(M^(pi))}(w_k). For Richardson-SGD, ghat_k is the linked gradient ghat_R(w_k).

Assume there are constants C_plain, C_R, sigma^2, and C_0, independent of pi and k, such that for every iteration the plain conditional bias has norm at most C_plain||pi||_1, the Richardson conditional bias has norm at most C_R||pi||_1^2, and for either algorithm E[||ghat_k-E[ghat_k | F_k]||^2 | F_k]<=sigma^2 almost surely. Thus the bias bounds are required uniformly along the encountered trajectories, separately from the fixed-w population conclusions. Require E||w_0-w*||^2<=C_0 uniformly over admissible pi for each algorithm.

One-pass SGD uses w_{k+1}=w_k-eta_k ghat_k, eta_k=c/(k+gamma), with c>1/alpha and gamma>=6c beta^2/alpha. The constants alpha, beta, c, gamma, and lambda are fixed independently of pi and n. In particular eta_k<=alpha/(6 beta^2).

## Task

Prove that, for fixed admissible lambda and ||pi||_1 tending to zero, for every fixed w there are constants independent of pi such that ||B(w,pi)||=O(||pi||_1) and ||E ghat_R(w)-nabla L(w)||=O(||pi||_1^2). These constants may depend on w, the fixed data, intensity, and imputation laws, d, and lambda.

Moreover, under the stated trajectory-uniform bias, conditional variance, and initialization conditions, after one pass of n updates, plain imputed SGD satisfies E||w_n-w*||^2=O(||pi||_1^2)+O(1/n), while linked Richardson-SGD satisfies E||w_n-w*||^2=O(||pi||_1^4)+O(1/n). The same orders hold for expected excess population loss E[L(w_n)-L(w*)]. The constants in these optimization bounds are independent of pi and n.
