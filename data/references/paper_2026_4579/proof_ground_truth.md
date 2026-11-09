# Reference Proof

## Proof obligations

1. Establish the policy-independent root at theta-star and identify the assumed positive-axis greedy root correctly.
2. Derive the local affine greedy fields and their nonsingular Hurwitz Jacobians.
3. Establish quantitative C^1 convergence for the actual normalized tamed-Gibbs policy and its stationary mean field, including sensitivity of the invariant distribution.
4. Obtain a nearby second root with a constant independent of epsilon and kappa.
5. Transfer Hurwitzness and local asymptotic stability to both roots, and handle epsilon-greedy exploration.

The inherited exploration-chain assumptions are part of the source contract. This local proof does not use the global drift, boundedness, or existence conclusions of theory_005, or the nonstandard external result theory_012.

## 1. Exact roots and conditional Bellman identities

Write theta-star=(1,0) and theta-diamond=(0,beta-diamond). Let P(x'|x,u) be the controlled transition probabilities. Define the conditional residual

r_theta(x,u) = -Q^theta(x,u) + c(x,u) + gamma sum_{x'} P(x'|x,u) min_v Q^theta(x',v).

For any fixed stationary policy pi, the mean field is the stationary expectation of psi(X,U) r_theta(X,U). The Bellman equation gives r_{theta-star}(x,u)=0 for every state-action pair. Thus theta-star is a root for every stationary training policy, including a policy selected as a function of theta. The sampled residual need not vanish for each realized next state; it is its conditional expectation that vanishes.

For beta>0, minimization commutes with multiplication by beta. The Bellman equation for Q-diamond consequently gives

r_{(0,beta)}(x,u)=c(x,u)-beta c-diamond(x,u),

and hence

f-bar_pi(0,beta)=E_pi[psi(X,U)(c(X,U)-beta c-diamond(X,U))].

At beta=beta-diamond, the second greedy root is precisely the root assumed in the task. No assertion for negative beta is needed.

## 2. Greedy neighborhoods and a direct TD stability calculation

Choose disjoint closed balls B_star and B_diamond around the two parameters, contained in open neighborhoods on which all minimizing actions are unique. This is possible because there are finitely many state-action pairs, the Q-functions depend continuously on theta, and the two parameters are distinct. On each ball the greedy policy is a fixed deterministic policy g. The ball can be chosen so that every non-greedy action has a strictly positive action gap throughout a slightly larger compact neighborhood.

Under this fixed greedy policy, the stationary law does not depend on theta. Since the minimizing next action is also g, the mean field is affine, with matrix

A_g=E_g[psi(Z)(gamma psi(Z')-psi(Z))^T],

where Z,Z' are consecutive stationary state-action pairs under g. At the associated root theta_g this gives f-bar_0(theta)=A_g(theta-theta_g).

Here is the relevant on-policy TD fact, with its proof. Let R_g=E_g[psi(Z)psi(Z)^T]. For a real vector v put Y=v^T psi(Z) and Y'=v^T psi(Z'). Stationarity gives E[(Y')^2]=E[Y^2]. Cauchy-Schwarz therefore yields

v^T A_g v = -E[Y^2]+gamma E[YY'] <= -(1-gamma)E[Y^2] = -(1-gamma)v^T R_g v.

The assumed full rank of R_g makes it positive definite. Thus the symmetric part of A_g is negative definite. For any complex eigenvector, the real part of its quadratic form is determined by this symmetric part, so every eigenvalue has strictly negative real part. In particular A_g is Hurwitz and invertible. This verifies directly the standard TD fact indexed by theory_013, without depending on an unreproduced external proof.

Applying the calculation to both greedy policies gives matrices A_star and A_diamond and a common constant m>0 such that

v^T A_g v <= -m ||v||^2

for both matrices and every real v.

## 3. Quantitative policy and stationary-law perturbations

All estimates in this section are uniform on the two selected compact neighborhoods. Constants may depend on the fixed MDP, costs, features, discount, exploration pmf, beta-diamond, and the neighborhoods, but not on epsilon or kappa.

For a fixed greedy policy g on one neighborhood, define the normalized non-greedy gaps

d_{x,u}(theta) = [Q^theta(x,u)-Q^theta(x,g(x))]/sqrt(1+||theta||^2),  u != g(x).

Their values have a positive lower bound a>0 and their first derivatives are bounded. If there are no non-greedy actions, the policy perturbation is identically zero and the following estimates hold trivially.

Divide the softmax numerator and denominator by the greedy-action exponential. Every non-greedy weight is then exp(-kappa d_{x,u}(theta)). Its size is at most exp(-a kappa), and the norm of its theta derivative is at most C kappa exp(-a kappa). Differentiating the finite normalized sums gives the same bounds for non-greedy probabilities; the greedy probability is one minus their sum. Mixing with the fixed pmf nu gives, for kappa>=1,

||pi_{kappa,epsilon}-g||_{C^1} <= C[epsilon+kappa exp(-a kappa)] <= C'[epsilon+1/kappa].

The last inequality follows because kappa^2 exp(-a kappa) is bounded for kappa>=1. This calculation includes the derivative of the taming factor through d_{x,u}.

For epsilon-greedy exploration, the policy on this neighborhood is exactly (1-epsilon)g+epsilon nu. It is constant as a function of theta there, and its C^1 distance from g is at most C epsilon.

We next justify the passage to invariant distributions, including at a greedy policy with zero action probabilities. On the finite state-action space, let T_pi be the row-stochastic transition matrix

T_pi((x,u),(x',u'))=P(x'|x,u) pi(u'|x').

Let n be its dimension and let 1 denote the n-vector of ones. If T has a unique invariant probability vector d, then

M(T)=I-T^T+11^T

is invertible and d=M(T)^{-1}1. Indeed, a finite Markov chain with a unique invariant probability has one closed recurrent class, so the kernel of I-T^T is the span of d. If M(T)v=0, multiplication by 1^T gives n 1^T v=0; consequently (I-T^T)v=0 and v must be a multiple of d with zero sum, hence v=0. Conversely, the displayed inverse solves the normalized stationary equations.

At either greedy transition matrix this inverse exists. Matrix inversion is smooth on a neighborhood of an invertible matrix; its derivatives are bounded after reducing the neighborhood. Also T_pi is linear in pi. The policy estimates therefore imply

||d_{kappa,epsilon}-d_g||_{C^1} <= C[epsilon+1/kappa],

and the analogous O(epsilon) estimate for epsilon-greedy. This argument requires neither positive stationary mass on every pair nor aperiodicity of the greedy chain. It also establishes local uniqueness of the invariant law for sufficiently small epsilon-greedy perturbations.

On a fixed greedy neighborhood, the conditional residual r_theta is affine in theta. The mean field is the finite sum

f-bar_{kappa,epsilon}(theta)=sum_z d_{kappa,epsilon}(theta,z) psi(z) r_theta(z).

The residual and its first derivatives are uniformly bounded there. Multiplication and differentiation of this sum now give

||f-bar_{kappa,epsilon}-f-bar_0||_{C^1} <= C eta,

where eta=epsilon+1/kappa for finite kappa, and eta=epsilon for epsilon-greedy. This estimate includes the derivative of the invariant law; it does not treat the training distribution as fixed when differentiating an exploratory field.

## 4. Quantitative persistence of the second root

Work on B_diamond, write A=A_diamond, and put

e(theta)=f-bar_{kappa,epsilon}(theta)-A(theta-theta-diamond).

The preceding estimate gives sup ||e|| <= C eta and sup ||De|| <= C eta. Define

H(theta)=theta-A^{-1}f-bar_{kappa,epsilon}(theta)=theta-diamond-A^{-1}e(theta).

For sufficiently small eta, sup ||DH|| <= ||A^{-1}|| C eta <= 1/2. Moreover,

||H(theta-diamond)-theta-diamond|| <= ||A^{-1}|| C eta.

Set L=||A^{-1}||C and consider the closed ball of radius 2L eta centered at theta-diamond. For small enough eta it lies inside B_diamond. On this ball,

||H(theta)-theta-diamond|| <= (1/2)||theta-theta-diamond||+L eta <= 2L eta.

Thus H maps the ball into itself and is a contraction. Its fixed point theta-t is a root of the exploratory field and satisfies

||theta-t-theta-diamond|| <= 2L eta.

This is a quantitative form of the local implicit-function argument and proves the required estimate with b_0=2L, enlarged if necessary to be positive. The constant is independent of epsilon and kappa.

Choose delta>0 small enough for all neighborhood, contraction, and later stability estimates. Choose epsilon_gamma in (0,min(1,delta/2)), and choose each finite kappa_{epsilon,gamma} large enough that all preceding large-kappa estimates hold and epsilon+1/kappa<delta for every kappa>=kappa_{epsilon,gamma}. For example, a sufficiently large common threshold works after further reducing epsilon_gamma. This has the required quantifier order. The same choices apply to epsilon-greedy with eta=epsilon. By making delta smaller, the second-root ball remains disjoint from theta-star.

## 5. Hurwitzness and local stability

Theta-star remains an exact root by Section 1. On either chosen neighborhood,

||D f-bar_{kappa,epsilon}(theta)-A_g|| <= C eta.

Reduce delta further so C eta<m/2. The symmetric part of every such Jacobian is then bounded above by -(m/2)I. In particular the Jacobians at theta-star and theta-t are Hurwitz.

For completeness, this also gives local asymptotic stability directly. Let theta_e be either root and take a small convex ball about theta_e contained in its greedy neighborhood. For h with theta_e+h in this ball, the fundamental theorem of calculus yields

h^T f-bar_{kappa,epsilon}(theta_e+h) = integral_0^1 h^T D f-bar_{kappa,epsilon}(theta_e+s h) h ds <= -(m/2)||h||^2.

Along the mean-flow ODE, the derivative of ||h||^2 is consequently at most -m||h||^2. A sufficiently small initial ball is forward invariant and solutions converge exponentially to theta_e. Hence both equilibria are locally asymptotically stable.

Every argument in Sections 4 and 5 applies to epsilon-greedy using its O(epsilon) C^1 bound. This proves the entire conclusion with kappa=infinity and 1/kappa=0. All five proof obligations are closed.
