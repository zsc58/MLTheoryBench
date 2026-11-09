# Reference Proof

## Proof Structure

For Wasserstein density, first approximate an arbitrary law by a finitely supported law, then replace each atom by a Gaussian with a fixed nonzero trace-class covariance scaled by a small factor. An explicit coupling makes the smoothing error vanish. For the MMD bound, use an empirical measure formed from K iid samples, control its RKHS embedding error in expectation, select one realization, and smooth its atoms; bounded continuity of the kernel makes the smoothing error vanish. The triangle inequality then gives the stated rate.

## Complete Proof

Fix p >= 1 and P in P_p(X). By the standard W_p-density of finitely supported probability measures on the Polish space X, for every eta > 0 there is an atomic law P_0 = sum_{j=1}^m a_j delta_{x_j} with W_p(P,P_0) < eta. Choose a self-adjoint positive nonzero trace-class operator C on X and let Z have law N(0,C). For epsilon > 0 define

P_epsilon = sum_{j=1}^m a_j N(x_j, epsilon^2 C).

Couple P_0 and P_epsilon by drawing J with probabilities a_j and setting Y = x_J and Y_epsilon = x_J + epsilon Z. Then

W_p(P_0,P_epsilon)^p <= E||Y-Y_epsilon||^p = epsilon^p E||Z||^p,

which is finite because a Gaussian with trace-class covariance has moments of every order. Hence W_p(P_0,P_epsilon) tends to zero as epsilon tends to zero. The triangle inequality gives W_p(P,P_epsilon) <= W_p(P,P_0)+W_p(P_0,P_epsilon), so Gaussian mixtures with nonzero trace-class covariances are W_p-dense in P_p(X).

Now let kappa be continuous positive definite with sup_x kappa(x,x) <= 1, let H_kappa be its RKHS, and write phi(x)=kappa(x,.) and mu_R = E_R phi(X). The diagonal bound implies ||phi(x)|| <= 1, so these embeddings are well defined. For iid X_1,...,X_K with law P, let P_K = K^{-1} sum_{i=1}^K delta_{X_i}. Independence and the Hilbert-space variance identity give

E ||mu_{P_K}-mu_P||^2 = (1/K) E||phi(X_1)-mu_P||^2 <= (1/K) E||phi(X_1)||^2 <= 1/K.

Therefore some realization x_1,...,x_K satisfies MMD_kappa(P,P_K) = ||mu_P-mu_{P_K}|| <= 1/sqrt(K). Fix such a realization. Using the same C as above, set

Q_{K,epsilon} = (1/K) sum_{i=1}^K N(x_i, epsilon^2 C).

As epsilon tends to zero, each Gaussian component converges weakly to delta_{x_i}. Since kappa is bounded and continuous, all kernel expectations in the three-term formula for MMD_kappa^2(P_K,Q_{K,epsilon}) converge to those for (P_K,P_K). Thus MMD_kappa(P_K,Q_{K,epsilon}) tends to zero. Choose epsilon small enough that this quantity is at most 1/sqrt(K). The triangle inequality for the RKHS norm then yields

MMD_kappa(P,Q_{K,epsilon}) <= MMD_kappa(P,P_K)+MMD_kappa(P_K,Q_{K,epsilon}) <= 2/sqrt(K).

Each Q_{K,epsilon} has exactly K Gaussian components and every covariance epsilon^2 C is nonzero, self-adjoint, positive, and trace class. This proves both claims.
