# Reference Proof

## Proof Structure

Derive coordinate descent from projected coordinate smoothness and the defining Wasserstein differential. Average under the prescribed probabilities, then telescope for stationarity. Use the optimal-coupling convexity inequality and the sublevel radius for the convex rate. Derive PL from strong geodesic convexity, and combine PL with the same expected descent for geometric convergence.

## Complete Proof

Write ||h||_mu^2=integral |h(x)|^2 dmu(x), g_k=g_{mu_k}, and Delta(mu)=E[mu]-E_*. The minimum value E_* is finite because E is real-valued and has a minimizer. Let F_k=sigma(I_0,...,I_{k-1}); mu_0 is fixed and mu_k is F_k-measurable. At any fixed finite time there are only finitely many coordinate histories, so all energies and squared gradient norms appearing in the expectations are finite-valued random variables on a finite set. No measurable selection of minimizers is needed.

### 1. Coordinate descent from the projected assumption

Fix mu, a coordinate i, and T in L^2(mu;R^d). Put a=U_iT, F_t(x)=x+ta(x), and rho_t=(F_t)#mu for 0<=t<=1. The second moments are finite because integral |F_t(x)|^2 dmu(x)<=2 integral |x|^2 dmu(x)+2||a||_mu^2. The coupling (F_s,F_t)#mu gives W_2(rho_s,rho_t)<=|s-t| ||a||_mu.

For completeness, this path has a compatible velocity even if F_t is non-injective. If X has law mu, define v_t(z)=E[a(X)|F_t(X)=z]. Conditional Jensen gives ||v_t||_{rho_t}<=||a||_mu. For a smooth compactly supported test function phi, differentiation under the integral gives

d/dt integral phi d rho_t = integral grad phi(F_t(x)) dot a(x) dmu(x) = integral grad phi(z) dot v_t(z) d rho_t(z).

Thus the continuity equation holds, and the defining Wasserstein differential gives, for h(t)=E[rho_t],

h'(t)=integral g_{rho_t}(F_t(x)) dot a(x) dmu(x).

This is the ordinary velocity-field chain rule in the assumed differentiability convention, not an assumption that F_t is an optimal transport map. Since a=U_i a, the projected coordinate-smoothness inequality applied at mu with displacement tT gives

|h'(t)-<g_mu,a>_mu|
= |<U_i(g_{rho_t} composed with F_t-g_mu),a>_mu|
<= t L_i ||a||_mu^2.

The derivative is bounded on this interval; the scalar differential rule therefore permits integration (equivalently, the mean-value theorem gives Lipschitz continuity of h, followed by the fundamental theorem for absolutely continuous scalar functions). Consequently,

E[(Id+U_iT)#mu] <= E[mu]+<g_mu,U_iT>_mu+(L_i/2)||U_iT||_mu^2.

Only the projected gradient difference was bounded. No full-gradient Lipschitz bound, tangency of U_iT, or invertibility of the pushforward map is used.

Apply this with T=-g_mu/L_i. If mu^{(i)}=(Id-U_i g_mu/L_i)#mu, then

E[mu^{(i)}] <= E[mu]-||U_i g_mu||_mu^2/(2L_i).

Every update is therefore well-defined in P_2 and non-increasing in energy.

### 2. Expected descent and the nonconvex rate

Conditioning on F_k and using P(I_k=i|F_k)=L_i/L_sum gives

E[E[mu_{k+1}]|F_k]
<= E[mu_k]-sum_i (L_i/L_sum)||U_i g_k||_{mu_k}^2/(2L_i)
= E[mu_k]-||g_k||_{mu_k}^2/(2L_sum).

The last equality follows from sum_i |U_i z|^2=|z|^2, integrated against mu_k. The first relation is an inequality, not generally an equality.

Taking expectations and summing from k=0 to K-1 yields

sum_{k=0}^{K-1} E||g_k||_{mu_k}^2 <= 2L_sum(E[mu_0]-E[E[mu_K]]) <= 2L_sum(E[mu_0]-E_*).

For each coordinate history, the minimum of the K nonnegative squared norms is at most their arithmetic average. Hence

E[min_{0<=k<K}||g_k||_{mu_k}^2] <= 2L_sum(E[mu_0]-E_*)/K.

This preserves the source order of expectation and minimum. Every realized update also satisfies E[mu_{k+1}]<=E[mu_k], so E[mu_K]<=E[mu_0] almost surely.

### 3. Geodesically convex rate

Assume geodesic convexity and the stated sublevel condition with 0<R_0<infinity. Let S be the nonempty minimizer set. Monotonicity puts every iterate in the initialization sublevel set.

Fix any mu in that sublevel set and any nu in S. An optimal coupling pi of mu and nu exists. Indeed, a sequence of couplings with costs approaching the infimum is tight because its marginals are fixed; a weakly convergent subsequence has the same marginals, and lower semicontinuity of the nonnegative squared-distance cost gives an optimal limit.

Geodesic convexity and Cauchy-Schwarz give

Delta(mu) <= -integral <g_mu(x),y-x> d pi(x,y) <= ||g_mu||_mu W_2(mu,nu).

Take the infimum over nu in S to obtain

Delta(mu) <= R_0 ||g_mu||_mu.

This argument neither asserts that the nearest minimizer exists nor selects one measurably.

Set Delta_k=Delta(mu_k) and C=2L_sum R_0^2>0. Expected descent gives

E[Delta_{k+1}|F_k] <= Delta_k-Delta_k^2/C.

With b_k=E[Delta_k], Jensen gives

0<=b_{k+1}<=b_k-b_k^2/C.

If any b_j=0, then Delta_j=0 almost surely, and pathwise monotonicity together with E>=E_* implies b_k=0 for every k>=j. Otherwise, for consecutive positive terms, b_{k+1}<=b_k and

1/b_{k+1}-1/b_k = (b_k-b_{k+1})/(b_k b_{k+1}) >= (b_k-b_{k+1})/b_k^2 >= 1/C.

If no zero term occurs through time K, summation gives 1/b_K>=1/b_0+K/C>=K/C. In either case,

E[E[mu_K]-E_*]=b_K<=2L_sum R_0^2/K.

### 4. Strong geodesic convexity implies PL

Suppose m>0 and E is m-geodesically convex. Fix mu and a minimizer nu, and let pi be an optimal coupling of mu and nu. The first-order inequality implies

Delta(mu) <= integral [-<g_mu(x),y-x>-(m/2)|y-x|^2] d pi(x,y).

For vectors a,b,

-a dot b-(m/2)|b|^2 = |a|^2/(2m)-(m/2)|b+a/m|^2 <= |a|^2/(2m).

Apply this pointwise and use the first marginal of pi to get

Delta(mu)<=||g_mu||_mu^2/(2m).

This proves the required PL inequality directly. It is Young's inequality/completing the square, not Jensen's inequality.

### 5. PL contraction, including degenerate cases

Under the m-PL condition, expected descent yields

0<=E[Delta_{k+1}|F_k] <= Delta_k-||g_k||_{mu_k}^2/(2L_sum) <= q Delta_k,

where q=1-m/L_sum.

If Delta_0=0, monotonicity and E>=E_* imply Delta_k=0 for all k, so the claimed bound holds for every m>0, even when q<0.

If Delta_0>0, the preceding inequality at k=0 forces q>=0. Since m>0, also q<1. Taking expectations gives b_{k+1}<=q b_k, and induction gives

E[E[mu_K]-E_*]<=q^K(E[mu_0]-E_*).

This includes q=0, when the first expected gap and all later gaps vanish. No additional restriction on m is imposed. By the preceding section, the same rate holds whenever E is m-geodesically strongly convex.

## Audit Closure

The proof explicitly establishes update well-definedness, the coordinate descent inequality under the projected assumption, anisotropic conditional averaging, the expected-minimum rate, monotonicity, the convex gap comparison and reciprocal recurrence, strong convexity implying PL, and PL contraction with zero-gap and endpoint cases. No specialized external theorem or unresolved paper-specific dependency is used.
