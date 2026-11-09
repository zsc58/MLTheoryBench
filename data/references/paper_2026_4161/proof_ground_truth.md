# Reference Proof

## Proof Structure and Obligations

1. Verify that the normalized variance tilt defines a probability density, and obtain its positive-time density by conditioning under the independent base experiment.
2. Derive the Gaussian posterior mean, covariance, and Jacobian identities pointwise.
3. Compute the conditional batch variance using conditional independence.
4. Differentiate the posterior-mean variance and covariance-trace terms, including the column-wise divergence calculation.
5. Apply the Brownian reverse-time result to the tilted forward process, checking its initialization, dimension, positive-time regularity, and continuous terminal limit.

All five obligations are closed below. No paper-specific result is used without its derivation.

## Complete Proof

Write f(boldsymbol{u})=Var_n^A(boldsymbol{u}) and Z_A=E[f(boldsymbol{X}_0)] under the independent base initial law p_0^{otimes n}. By assumption, 0<Z_A<infinity, so pi_0^A=Z_A^{-1}f p_0^{otimes n} is a probability density.

For an integer m>=1, let K_t^(m)(v)=(4 pi t)^(-m/2) exp(-||v||^2/(4t)) denote the heat kernel. Gaussian convolution of a probability density is positive and smooth at every positive time. Its spatial derivatives and its time derivative can be computed under the integral locally on t>0: derivatives of the Gaussian kernel are polynomials times a Gaussian and are bounded uniformly in the integration variable when the evaluation point and positive time range over compact sets. This also proves the heat equation. These observations apply both to p_t and to q_t^A, the latter in dimension nd.

### 1. Normalized tilt and its pointwise conditional representation

For every t>0 and x in R^d, define the posterior density

rho_t(u|x)=p_0(u)K_t^(d)(x-u)/p_t(x).

This is a probability density for every x, not merely almost every x. All of its polynomial moments are finite: a polynomial in u multiplied by K_t^(d)(x-u) is bounded as a function of u, and p_0 is integrable. The corresponding posterior moments can also be differentiated locally under the integral by the same Gaussian domination argument. No unconditional full-dimensional second moment of p_0 is needed.

Under the base independent batch experiment, the posterior density of boldsymbol{X}_0 given boldsymbol{X}_t=boldsymbol{x} is product_i rho_t(u^(i)|x^(i)). Define

H_t(boldsymbol{x})=integral f(boldsymbol{u}) product_i rho_t(u^(i)|x^(i)) d boldsymbol{u}.

This integral is finite for every batch because f is quadratic. Direct substitution into the forward convolution of pi_0^A gives

q_t^A(boldsymbol{x})=Z_A^{-1}H_t(boldsymbol{x}) product_i p_t(x^(i)).

Both q_t^A and the product density are strictly positive at positive times, so H_t>0. Consequently,

nabla_boldsymbol{x} log q_t^A=(s_t(x^(1)),...,s_t(x^(n)))+nabla_boldsymbol{x} log H_t.

This proves the terminal-reweighting identity with its normalization and pointwise interpretation explicitly checked.

### 2. Gaussian posterior identities

Let m_t(x)=integral u rho_t(u|x) du. Differentiating the Gaussian convolution gives

s_t(x)=integral -(x-u)/(2t) rho_t(u|x) du=(m_t(x)-x)/(2t).

Thus m_t(x)=x+2t s_t(x)=mu_t(x).

For a coordinate b, logarithmic differentiation of the posterior density gives, wherever its numerator is nonzero,

partial_b rho_t(u|x)=rho_t(u|x)(u_b-m_t(x)_b)/(2t).

The same equality holds directly by quotient differentiation everywhere. Therefore, writing Sigma_t(x) for the covariance under rho_t(.|x),

partial_b m_t(x)_a=integral u_a(u_b-m_t(x)_b)rho_t(u|x)du/(2t)=Sigma_t(x)_(ab)/(2t).

Differentiating m_t=x+2t s_t now yields

J_t=I_d+2t nabla s_t,

Sigma_t=2t J_t=2t I_d+4t^2 nabla s_t.

All these equalities hold for every x and t>0 by the pointwise posterior construction and Gaussian domination.

### 3. Conditional batch variance

Fix t>0 and boldsymbol{x}. Write mu_i=mu_t(x^(i)), Sigma_i=Sigma_t(x^(i)), and bar mu=n^{-1}sum_i mu_i. Under the product posterior, set Z_i=AX_0^(i). The Z_i are independent with means A mu_i and covariances A Sigma_i A^T.

The empirical variance identity gives

f(boldsymbol{X}_0)=n^{-1}sum_i ||Z_i||^2-||n^{-1}sum_i Z_i||^2.

The conditional second moments are

E[||Z_i||^2|boldsymbol{X}_t=boldsymbol{x}]=||A mu_i||^2+Tr(A Sigma_i A^T)

and

E[||n^{-1}sum_i Z_i||^2|boldsymbol{X}_t=boldsymbol{x}]=||A bar mu||^2+n^{-2}sum_i Tr(A Sigma_i A^T).

Subtracting gives

H_t=Var_n^A(mu_1,...,mu_n)+(n-1)n^{-2}sum_i Tr(A Sigma_i A^T).

Substituting the covariance formula and Tr(AA^T)=Tr(B) yields exactly the public formula for h_t^A. Thus H_t=h_t^A everywhere. In particular, this formula is finite and positive; its positivity is also consistent with the public assumption.

### 4. Differentiating the two terms

Since B=A^T A is symmetric,

Var_n^A(mu_1,...,mu_n)=n^{-1}sum_j mu_j^T B mu_j-bar mu^T B bar mu.

Only mu_i varies directly with x^(i), and its Jacobian is J_t(x^(i)); the Jacobian of bar mu with respect to x^(i) is J_t(x^(i))/n. Hence

nabla_{x^(i)} Var_n^A(mu_1,...,mu_n)=(2/n)J_t(x^(i))^T B(mu_i-bar mu).

For the covariance-trace contribution, only the ith summand depends on x^(i). Let ell=log p_t. With the Jacobian convention (nabla s_t)_(ab)=partial_b(s_t)_a, mixed derivatives give (nabla s_t)_(ab)=partial_b partial_a ell. For each coordinate c,

partial_c Tr(B nabla s_t)=sum_{a,b} B_(ab) partial_c partial_a partial_b ell,

while

[div(B nabla s_t)]_c=sum_{a,b} B_(ab) partial_a partial_c partial_b ell.

The two expressions agree by commutation of the mixed derivatives. Therefore,

nabla_x Tr(A Sigma_t(x) A^T)=4t^2 div(B nabla s_t(x)).

Combining the two differentiated terms proves

nabla_{x^(i)}h_t^A=(2/n)J_t(x^(i))^T B(mu_i-bar mu)+(n-1)n^{-2}4t^2 div(B nabla s_t(x^(i)))=g_t^{A,i}.

Since h_t^A>0, its logarithmic gradient is the concatenation of these vectors divided by h_t^A. Substitution into the identity in Step 1 proves the claimed score formula at every positive time and every batch.

### 5. Exact reverse-time diffusion and terminal law

The relevant standard reverse-time result is the following Brownian specialization. If U_t=U_0+sqrt(2)W_t in R^m, where U_0 has probability density rho_0 and is independent of standard Brownian motion W, then for finite T>0 the continuous reversed process Y_r=U_{T-r} satisfies

dY_r=2 nabla log rho_{T-r}(Y_r)dr+sqrt(2)dWbar_r,  0<=r<T,

with Y_0 distributed according to rho_T. Its continuous endpoint has density rho_0. Here rho_t=rho_0*K_t^(m), and Wbar is Brownian motion in the reverse-time filtration. The needed smoothness and positivity hold at every positive forward time. No score at time zero is required.

For completeness, the reverse-kernel calculation verifies this specialization. If t=T-r and 0<u<t, Bayes' rule gives the reversed transition density from y at reverse time r to z at time r+u as

K_u^(m)(y-z)rho_{t-u}(z)/rho_t(y).

For a smooth compactly supported test function phi, the corresponding conditional expectation is

[K_u^(m)*(phi rho_{t-u})](y)/rho_t(y).

Differentiating at u=0, and using partial_t rho_t=Delta rho_t, gives the reverse generator

[Delta(phi rho_t)-phi Delta rho_t]/rho_t=Delta phi+2 nabla log rho_t dot nabla phi.

On each interval r<=T-delta with delta>0, this calculation and the Markov transition identity give the associated local martingale problem. Applying it to localized coordinate and coordinate-product functions shows that

M_r=Y_r-Y_0-integral_0^r 2 nabla log rho_{T-v}(Y_v)dv

is a continuous local martingale with quadratic covariation 2r I_m. The standard Brownian characterization of continuous local martingales therefore makes M/sqrt(2) a Brownian motion, giving the displayed SDE. Localization is legitimate because the coefficients are smooth on positive-time compact sets and the reversed forward paths are continuous. Those paths also give the continuous limit Y_T=U_0. This verifies the terminal law directly.

Apply this result with m=nd and rho_0=pi_0^A. The normalizer assumption verifies that rho_0 is a probability density; the tilted forward process uses independent Brownian coordinate noises independent of its joint initial state. Its positive-time density is q_t^A, already shown positive and smooth. Its score is the formula proved in Step 4. Thus the reverse process starts from q_T^A, has precisely the stated drift and diffusion coefficient, and extends continuously to an endpoint with density pi_0^A.

## Boundary and Scope Checks

The condition 0<Z_A<infinity excludes A=0 and every zero or nonnormalizable tilt. No full-rank assumption on A is used. No unconditional second moments outside the feature directions are required. Every pointwise posterior calculation is valid at t>0, and the terminal claim uses continuity of the reversed paths rather than evaluation of a score at t=0. Initialization is the exact joint density q_T^A, not a product Gaussian approximation. No discretization, approximate score, or guidance scaling is part of this theorem.
