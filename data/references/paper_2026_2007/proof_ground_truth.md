# Reference Proof

## Proof Structure

Use the normalized ICAR prior on the constrained subspace and integrate the flat-prior fixed effects. Interpret the resulting quadratic form through its compression to the constrained subspace, and complete the square to identify and normalize the posterior. Derive the ELBO-KL identity and choose the posterior itself from the Gaussian family.

## Complete Proof

Fix Y and positive tau_y,tau_u. All densities and integrals in u are with respect to the induced Euclidean Lebesgue measure on E. Write m=n-1, P=P_X^perp, and R_E=R|_E. The symmetric graph Laplacian has nullspace spanned by 1, so R_E is a positive definite self-adjoint operator on E. Determinants of operators on E below are computed in any orthonormal basis of E.

### 1. Prior normalization and integration of beta

Gaussian integration on E gives the normalized prior

pi_tau_u(u)=(tau_u/(2 pi))^(m/2) det(R_E)^(1/2) exp[-tau_u u^T R u/2].

To integrate the observation density, let z=Y-u and beta_hat=(X^T X)^(-1)X^T z. Orthogonal decomposition gives

||z-X beta||^2=z^T P z+(beta-beta_hat)^T X^T X(beta-beta_hat).

Since X has full column rank, X^T X is positive definite. Consequently,

integral_{R^p} f(Y|beta,u,tau_y) d beta
=(tau_y/(2 pi))^((n-p)/2) det(X^T X)^(-1/2) exp[-tau_y(Y-u)^T P(Y-u)/2].

It follows that

g(Y,u|tau_y,tau_u)=C exp{-1/2[tau_y(Y-u)^T P(Y-u)+tau_u u^T R u]},

where the finite positive constant, independent of u, is

C=(tau_y/(2 pi))^((n-p)/2) det(X^T X)^(-1/2) (tau_u/(2 pi))^(m/2) det(R_E)^(1/2).

This is the integrated likelihood-prior function; no normalization over Y is asserted.

### 2. The quadratic form on E

Let A=tau_y P+tau_u R and define A_E:E to E by A_E v=Pi_E A v. For v,w in E,

<v,A_E w>=<v,A w>=<A v,w>=<A_E v,w>.

Thus A_E is self-adjoint. Moreover, <v,A_E v>=v^T A v>0 for nonzero v in E by the assumed positivity. Hence A_E is invertible and A_E^(-1) is positive definite on E. This argument does not require A to preserve E.

Set b_E=Pi_E(tau_y P Y). For u in E, <b_E,u>=tau_y<PY,u>, and therefore

tau_y(Y-u)^T P(Y-u)+tau_u u^T R u
=tau_y Y^T P Y-2<b_E,u>+<u,A_E u>.

### 3. Square completion and posterior normalization

Define mu_*=A_E^(-1)b_E and Sigma_*=A_E^(-1). Then mu_* belongs to E, and

<u,A_E u>-2<b_E,u>
=<u-mu_*,A_E(u-mu_*)>-<b_E,A_E^(-1)b_E>.

The integral Z=integral_E g(Y,u|tau_y,tau_u) du is thus

Z=C exp[-tau_y Y^T P Y/2+<b_E,A_E^(-1)b_E>/2] (2 pi)^(m/2) det(A_E)^(-1/2).

Every factor is finite and positive. In particular L=log Z is a finite real number. Dividing g by Z yields the density of N_E(mu_*,Sigma_*), proving the posterior assertion. This posterior belongs to Q.

### 4. ELBO-KL identity and nonnegativity

Let h(u)=g(Y,u|tau_y,tau_u)/Z denote the posterior density. For any q in Q, both q and h are strictly positive Gaussian densities on E. Their log densities, and log g for fixed Y and precisions, are quadratic functions plus constants. Gaussian second moments are finite, so the expectations defining the ELBO and KL(q||h) are finite.

Using log h=log g-log Z gives directly

KL(q||h)=E_q[log q-log h]
=E_q[log q]-E_q[log g]+L
=L-ELBO(q,tau_y,tau_u).

For completeness, the elementary inequality -log t>=1-t for t>0 gives

KL(q||h)=E_q[-log(h/q)]>=E_q[1-h/q]=1-integral_E h(u) du=0.

Hence ELBO(q,tau_y,tau_u)<=L for every q in Q.

### 5. Attainment

Choose q=h=N_E(mu_*,Sigma_*), which is an admissible member of Q. Its KL divergence from h is zero, so its ELBO equals L. Therefore

sup_{q in Q} ELBO(q,tau_y,tau_u)=L(tau_y,tau_u;Y).

The maximizing family contains the exact posterior, so the optimized variational approximation has zero posterior approximation error. The argument applies to every Y and every fixed positive pair of precisions satisfying the setup; it makes no claim about convergence of an optimization algorithm over the precisions.
