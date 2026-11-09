# Reference Proof

## Proof Structure and Obligations

The proof retains the source's subdifferential-to-conjugate-to-proximal argument. Its obligations are: (1) verify the compatibility and orientation of the convex-potential relation; (2) establish global well-posedness, conjugate differentiability, and recovery of the endpoint; (3) identify the conjugate gradient with the proximal map; and (4) verify that the displayed field is an everywhere-defined Borel representative of the conditional expectation. The last obligation is a version-selection statement, not an assertion about every conditional-expectation version.

## Complete Proof

### Step 1: Potential relation and source compatibility

The task supplies a proper lower-semicontinuous convex phi satisfying X_0 in partial phi(X_1) almost surely. This is the relation used below; a solver need not reprove the existence of phi.

For completeness of the source dependency closure, the standard-independent input recorded as theory_020 has the following relevant statement. A quadratic-cost optimal plan between two Borel probability measures with finite second moments has cyclically monotone support in the transport orientation. Every nonempty cyclically monotone set Gamma contained in R^d x R^d is contained in the graph of the subdifferential of a proper lower-semicontinuous convex function. Here cyclic monotonicity means that for every finite sequence (u_i,p_i) in Gamma, with u_{n+1}=u_1, one has sum_i <p_i,u_{i+1}-u_i> <= 0.

Both marginals in the task have finite second moments, so the quadratic cost is finite. Reversing the coordinates of pi preserves optimality because the quadratic cost is symmetric. Applying the stated result to the reversed support gives X_0 in partial phi(X_1), with exactly the orientation used in the task. Multiplying the cost by 1/2 does not change its minimizers. No density assumption on P_1 enters this standard-independent input. This closes the background existence assertion indexed by theory_002 and theory_020; the rest of the proof uses the given phi.

Fix any t in (0,1), and write alpha=alpha_t>0, beta=beta_t>0, lambda=alpha/beta, Y=Y_t, and psi=psi_t.

### Step 2: Global inverse, conjugate differentiability, and endpoint recovery

There exists at least one pair (u_bar,p_bar) with p_bar in partial phi(u_bar), because the given subdifferential relation holds on a set of pi-probability one. By the definition of a convex subgradient,

phi(u) >= phi(u_bar)+<p_bar,u-u_bar>

for every u. In particular, phi has an affine lower bound.

For each y in R^d, consider

G_y(u)=alpha phi(u)+(beta/2)||u||^2-<y,u>.

This function is proper, lower semicontinuous, and beta-strongly convex. Its affine lower bound plus the positive quadratic term makes it coercive and bounded below. A minimizing sequence is bounded, has a convergent subsequence, and attains its infimum by lower semicontinuity. Strong convexity gives uniqueness. Denote the minimizer by q(y).

The minimizer condition is equivalent to

y-beta q(y) in alpha partial phi(q(y)).

Here is a direct verification that also covers extended-valued phi. If q minimizes G_y, compare q with q+s(z-q), for 0<s<1 and phi(z)<infinity. Convexity of phi and minimality give

0 <= alpha(phi(z)-phi(q))+<beta q-y,z-q>+(beta s/2)||z-q||^2.

Let s decrease to zero. The resulting inequality is precisely (y-beta q)/alpha in partial phi(q). Points z outside the effective domain impose no further condition. Conversely, that subgradient inequality gives

G_y(z)-G_y(q) >= (beta/2)||z-q||^2,

so q is the unique minimizer. This also proves the required identity partial psi(u)=alpha partial phi(u)+beta u in this setting.

The subgradient inequalities for q(y) and q(z), added together, imply

beta||q(y)-q(z)||^2 <= <y-z,q(y)-q(z)>.

Thus q is globally 1/beta-Lipschitz, and in particular Borel measurable.

The conjugate psi*(y)=sup_u{<y,u>-psi(u)} is finite, with its supremum attained uniquely at q(y). Evaluating the supremum at q(y) and q(y+h) gives

0 <= psi*(y+h)-psi*(y)-<q(y),h>
   <= <q(y+h)-q(y),h>
   <= ||h||^2/beta.

Therefore psi* is differentiable everywhere and nabla psi*(y)=q(y). In combination with the minimizer condition, this proves the needed conjugate inversion:

y in partial psi(u) if and only if u=nabla psi*(y).

Now the given relation X_0 in partial phi(X_1) yields

Y=alpha X_0+beta X_1 in alpha partial phi(X_1)+beta X_1=partial psi(X_1)

almost surely. Consequently,

X_1=q(Y)=nabla psi*(Y)

almost surely. Since alpha>0, also

X_0=(Y-beta q(Y))/alpha

almost surely. These conclusions do not require phi to be finite everywhere or P_1 to have a density.

### Step 3: Exact proximal identity

For every lambda>0 and z in R^d, the objective

phi(u)+(2lambda)^{-1}||u-z||^2

is proper, lower semicontinuous, coercive by the affine lower bound, and strongly convex. Hence its proximal minimizer exists and is unique. The same minimizer argument as in Step 2 gives its optimality condition:

u=prox_{lambda phi}(z) if and only if z in u+lambda partial phi(u).

Take lambda=alpha/beta and z=y/beta. For u=prox_{lambda phi}(y/beta), multiplication of the optimality condition by beta gives

y in beta u+alpha partial phi(u)=partial psi(u).

The inversion proved in Step 2 therefore yields, for every y in R^d,

nabla psi_t*(y)=prox_{(alpha_t/beta_t) phi}(y/beta_t).

This is the exact identity, not an approximation.

### Step 4: Conditional expectation and the everywhere-defined version

Define, for every y in R^d,

g_t(y)=(dot alpha_t/alpha_t)y+(dot beta_t-beta_t dot alpha_t/alpha_t)q(y).

Since q is continuous, g_t is Borel measurable. Endpoint recovery gives

g_t(Y_t)=dot alpha_t X_0+dot beta_t X_1

almost surely. The variable on the right is integrable, indeed square-integrable, because both marginals have finite second moments and the schedule derivatives at the fixed time are finite. Therefore g_t(Y_t) is an integrable function of Y_t equal almost surely to the teaching variable, and

g_t(Y_t)=E_pi[dot alpha_t X_0+dot beta_t X_1 | Y_t]

almost surely.

Consequently, choosing v_t=g_t on all of R^d gives a Borel version of the conditional teaching field. Substitution of Step 3 and the identity

dot beta_t-beta_t dot alpha_t/alpha_t
=beta_t(dot beta_t/beta_t-dot alpha_t/alpha_t)

gives, for every y in R^d,

v_t(y)=(dot alpha_t/alpha_t)y+beta_t(dot beta_t/beta_t-dot alpha_t/alpha_t)prox_{(alpha_t/beta_t) phi}(y/beta_t).

The equality at every y follows from this choice of representative. Arbitrary versions can differ on sets of zero probability under the law of Y_t, and are not claimed to satisfy the formula there. No full-support assumption on the law of Y_t is used.

The time t was arbitrary in (0,1). Positivity of alpha_t and beta_t makes every quotient and proximal parameter well-defined; no endpoint formula is asserted. All four proof obligations are closed, including singular-target and lower-dimensional-domain cases.
