# Reference Proof

## Proof Structure

1. Derive both information-coordinate averaging identities, including measurability and almost-everywhere admissibility.
2. Realize finite convex combinations by selector time-sharing.
3. Prove closed-convex-hull containment by separation.
4. Identify the frontier and prove extended-valued concavity.
5. Prove the two-predictor approximation by finite-dimensional support reduction.

## Standard Background Used

For random variables on standard Borel spaces, regular conditional distributions exist. Integration of a jointly measurable function against a probability kernel is measurable, and relative entropy between two probability kernels is a measurable nonnegative extended-real function of the parameter. Conditional mutual information is the integral of the relative entropy between the conditional joint law and the product of its conditional marginals. The chain rules are

I((B,W);Y)=I(B;Y)+I(W;Y|B),

I((B,W);Z|Y)=I(B;Z|Y)+I(W;Z|Y,B).

These are nonnegative extended-real identities and do not require finite entropies. These facts are the standard-independent material in theory_006, theory_016, and theory_018.

The standard-independent separation result in theory_017 says that if K is a nonempty closed convex subset of R^2 and x is outside K, there exist theta in R^2 and c in R such that theta dot y<=c for every y in K, but theta dot x>c.

## Complete Proof

### 1. Information averaging

The target space is nonempty because it carries the law of T. A constant predictor is measurable and has both information coordinates zero. Thus (0,0) belongs to D.

Fix an admissible revealed randomized output Vtilde=(R,W), where W=G(A,S,R), R is uniform on [0,1], and R is independent of (A,T,S). For each r, the section g_r(a,s)=G(a,s,r) is measurable. Write V_r=g_r(A,S), q(r)=I(V_r;T), and d(r)=I(V_r;S|T), initially allowing infinity.

To verify measurability, the laws of (G(A,S,r),T) and their marginals are probability kernels in r, obtained by integrating jointly measurable indicators against the fixed law of (A,T,S). Therefore q(r) is measurable by measurability of relative entropy for kernels. For d(r), take a regular conditional law K_t of (A,S) given T=t. Its pushforward under (a,s) -> (G(a,s,r),s) is a probability kernel in (r,t). The relative entropy between this conditional joint law and the product of its marginals is measurable in (r,t); integrating against P_T gives the measurable function d(r). All spaces involved are Polish or finite products of Polish spaces, so the stated standard-Borel results apply.

Independence identifies the conditional data law given R=r with the original data law, and the conditional law of (A,S) given (T,R)=(t,r) with K_t, almost everywhere. Applying the chain rules and conditional-information disintegration gives

I(Vtilde;T)=I(R;T)+I(W;T|R)=integral_0^1 q(r) dr,

I(Vtilde;S|T)=I(R;S|T)+I(W;S|T,R)=integral_0^1 d(r) dr.

Here I(R;T)=I(R;S|T)=0 by independence. Admissibility makes both integrals finite. Hence g_r is admissible for almost every r, and the vector s(r)=(d(r),q(r)) is integrable after assigning (0,0) on the null set where either coordinate is infinite. This modification changes neither integral. In particular, s(r) belongs to D almost everywhere and

(d(Vtilde),q(Vtilde))=integral_0^1 s(r) dr.

The public setup already supplies the uniform selector, so no representation theorem is needed to begin this proof. For correspondence with the source's arbitrary standard-Borel external noise N, its law is the pushforward of Lebesgue measure under a measurable h. Replacing f(a,s,N) by G(a,s,r)=f(a,s,h(r)) preserves both information coordinates: conditioning on N gives the averages over its law, and conditioning on R gives the same averages by pushforward. Revealing R rather than h(R) therefore does not change either coordinate. Conversely, uniform noise is itself an allowed external noise.

### 2. Finite convex combinations

Choose finitely many admissible deterministic predictors g_i with coordinates (d_i,q_i), and nonnegative weights alpha_i summing to one. Partition [0,1] into measurable sets E_i of Lebesgue measures alpha_i and define G(a,s,r)=g_i(a,s) for r in E_i. This map is jointly measurable. The averaging identities give

(d(Vtilde),q(Vtilde))=sum_i alpha_i(d_i,q_i).

Both coordinates are finite, so the constructed revealed predictor is admissible. This proves conv(D) is contained in Rset.

### 3. Closed-convex-hull containment

Let C=closure(conv(D)). It is nonempty, closed, and convex. If an attainable randomized point x were outside C, separation would give theta and c satisfying theta dot y<=c for every y in C and theta dot x>c. Its averaging representation from Step 1 has s(r) in D subset C almost everywhere. Moreover, theta dot s(r) is integrable because both coordinates of s are integrable. Consequently

theta dot x=integral_0^1 theta dot s(r) dr<=c,

a contradiction. Thus Rset is contained in C. Taking closures of both inclusions proves closure(Rset)=C, and the definitions immediately give phi_R(v)=phi_C(v) for every v>=0.

### 4. Concavity, including infinite values

Since (0,0) belongs to C, each feasible slice at a nonnegative budget is nonempty, and phi_C takes values in [0,infinity]. Fix budgets v_1,v_2>=0 and a weight t in (0,1). Whenever (d_i,q_i) belongs to C with d_i<=v_i, convexity gives

(t d_1+(1-t)d_2, t q_1+(1-t)q_2) in C.

Its first coordinate is at most t v_1+(1-t)v_2. Therefore

phi_C(t v_1+(1-t)v_2)>=t q_1+(1-t)q_2.

If both frontier values are finite, take witnesses with utilities approaching their respective suprema to obtain the concavity inequality. If either frontier value is infinite, choose feasible witnesses at that budget with arbitrarily large utility and use any feasible witness at the other budget. The displayed bound makes the frontier at the mixed budget infinite, which is the required extended-valued inequality. Weights zero and one give the identical endpoint statement. This proves concavity of phi_C and hence phi_R.

### 5. Two-predictor approximation

Fix v>=0 with F=phi_R(v)<infinity and epsilon>0. Because the feasible slice is nonempty and F is its supremum, choose (d_*,q_*) in C with d_*<=v and q_*>F-epsilon/3. By the definition of C, choose a finite convex combination

(bar d,bar q)=sum_{i=1}^m alpha_i(d_i,q_i),

where each (d_i,q_i) is realized by an admissible deterministic predictor, such that |bar d-d_*|<epsilon/3 and |bar q-q_*|<epsilon/3. Then bar d<v+epsilon and bar q>F-2epsilon/3.

Consider the finite-dimensional feasible set

P={beta in [0,1]^m: sum_i beta_i=1, sum_i beta_i d_i=bar d}.

It is nonempty because it contains alpha, and is compact. The continuous function sum_i beta_i q_i attains its maximum on P. Among its maximizers choose beta with the smallest number of positive coordinates.

Suppose this support has at least three elements. The vectors (1,d_i) on that support are linearly dependent in R^2. There is a nonzero vector h supported there with sum_i h_i=0 and sum_i h_i d_i=0. Since h is nonzero and its entries sum to zero, it has both positive and negative entries. For all sufficiently small positive t, both beta+t h and beta-t h are feasible. Optimality of beta therefore forces sum_i h_i q_i=0; otherwise one of these perturbations would improve the objective. Increase t in the positive direction to

t_*=min_{i:h_i<0} beta_i/(-h_i).

This is positive and finite. The vector beta+t_* h remains nonnegative, preserves normalization and average violation, and has the same optimal utility. At least one formerly positive coordinate becomes zero, while no new positive coordinate outside the original support appears. This contradicts the minimum-support choice of beta. Hence beta has at most two positive entries.

The corresponding predictors g_1,g_2 and their weights lambda,1-lambda satisfy

lambda d(V_{g_1})+(1-lambda)d(V_{g_2})=bar d<v+epsilon,

lambda q(V_{g_1})+(1-lambda)q(V_{g_2})>=bar q>F-epsilon.

If the support has one element, repeat that predictor and use lambda=1. Each predictor is admissible because the finite list was chosen from D. This proves the requested non-strict inequalities as well. The argument includes v=0 and F=0 and does not assume attainment of the frontier. The allowed budget slack accommodates approximation from the closed convex hull without asserting exact-budget achievability.

All five theorem-critical obligations are closed.
