# Reference Proof

## Proof Structure

1. Establish the graph relations and environmentwise additional-variable separation.
2. Construct a particular measurable stable-blanket conditional kernel valid under every fixed environment; do not upgrade an arbitrary observational version.
3. Prove that Condition II supplies Condition I.
4. Identify the selected environment's full conditional mean, compare risks conditionally, transfer the stable-blanket risk, and take suprema.

## Complete Proof

Write V={1,...,d}, W=D^c, H=C\D, and B=S. Parent sets are full graph-parent sets, but B contains covariate indices only. All unmarked graph sets refer to G.

### 1. Graphical preliminaries

D is closed under descendants. No parent of Y belongs to D, by acyclicity. Every child in H is outside D, and so is every covariate parent of such a child: otherwise descendant closure would put the child in D. Thus PA_G(Y) is contained in B and B is contained in W. A child in H cannot have E as a parent, since it would then belong to C_int and D.

Both B and W d-separate Y from E in G. Indeed, let A be either B or W and consider a simple path from Y to E. A first edge Y<-i is blocked at the conditioned parent i, a noncollider. If the first edge is Y->i with i in D, the path must meet a collider because E is a source. The first collider reached from Y and all its descendants lie in D; none lies in A, so it blocks the path. Otherwise the first child i belongs to H and is conditioned on. It blocks the path if it is a noncollider. If it is a collider, the next node is another parent k of i. This k is neither E nor Y, lies in B and A, and is a conditioned noncollider, so it blocks the path.

These separations imply ordinary conditional independence in the augmented law. They do not assert that an arbitrary observational conditional-law version works in every fixed environment. Section 2 supplies the required common version separately.

We also have Y d-separated from W\B given B in each fixed-environment graph. For a path from Y to j in W\B, a first edge from a parent is blocked at that conditioned noncollider. A first edge into a child i in D must encounter a collider; otherwise the path is directed to j and puts j in the descendant-closed set D. Its first collider and all descendants lie in D and therefore have no conditioned descendant in B. A first edge into i in H is blocked at i unless i is a collider. In that case its next node is another covariate parent k in B, a conditioned noncollider. It cannot be the endpoint j, since j is outside B. Fixing and deleting E cannot introduce a path, and E cannot be that alternate parent of a child in H.

Thus, by the fixed-environment global Markov property,

Y independent of X_(W\B) given X_B under every P_e.

### 2. A common conditional kernel for every environment

We first give the measurable probability-kernel fact used in the construction. If M_t is a probability kernel on the product of the real response space and a standard Borel observation space, there exists a jointly measurable kernel L(t,z,dy) such that, for each fixed t, L(t,Z,dy) is a conditional distribution of Y given Z under M_t. The exceptional observation set may depend on t; the same measurable formula nevertheless works for each t separately.

Here is a construction rather than an invocation of an unexplained uniform-version theorem. Choose increasing finite measurable partitions of the observation space whose union generates its sigma-field. Such partitions exist on a standard Borel space by enumerating a countable generating family. For a partition atom A_n(z) and rational r, form

M_t((−infinity,r] x A_n(z)) / M_t(R x A_n(z)),

with an arbitrary value when the denominator is zero. These ratios are measurable in (t,z). For each fixed t, they are conditional expectations of the indicators {Y<=r} with respect to the partition sigma-fields. The bounded martingale convergence theorem therefore makes them converge to the conditional expectations given Z, almost surely under the observation marginal of M_t. Intersect the convergence sets over rational r and impose the countable monotonicity and limiting conditions for a probability distribution. Take the right-continuous extension from rational arguments. On the remaining measurable exceptional set use delta_0. This gives a measurable probability kernel L. For each fixed t it has the conditional-distribution integral identities for rational half-lines, and hence for all Borel response sets by the monotone-class theorem. This proves the stated parameterized fact without any dominating observation measure. Its hypotheses apply to the finite products of the covariate spaces and the real response in this task.

Now discard D from the SCM. Since D is closed under descendants, no node of W or Y has a parent in D. Thus the induced SCM on W and Y is autonomous. Its children of Y are exactly H. Neither Y nor a node of H has an assignment depending directly on E. Their structural kernels are consequently fixed across environments. Moreover, every parent of a node of H other than Y belongs to B.

Let U=B\H. Split the independent exogenous noises into the noise at Y, the noises at H, and all remaining noises, denoted jointly by Z. Fix any e; it need not have positive probability under the observational law of E. In the reduced SCM every node outside Y and H can be computed as a measurable function of e, Z, and earlier outputs at H. This follows recursively along a topological ordering: such a node cannot have Y as a direct parent, because all direct children of Y in the reduced model are in H.

Expose the B coordinates in topological order, inserting the generation of Y at its own position. Before Y, all exposed B coordinates belong to U and are functions of e and Z. All parents A=PA_G(Y) have been exposed. Conditional on this history, Y has its fixed structural kernel K_Y(x_A,dy). The noise at Y is independent of Z, so Y and Z are conditionally independent given this history. Initialize the posterior at K_Y(x_A,dy).

Proceed through the remaining B coordinates. Maintain two assertions under the fixed P_e: the posterior of Y is a measurable function of the exposed B history, independent of e, and Y is conditionally independent of Z given that history.

If the next coordinate is in U, it is a measurable function of e, Z, and previously exposed H outputs. Given the previous history, it is therefore generated from Z alone. Conditional independence implies that exposing this coordinate does not change the posterior of Y and preserves conditional independence of Y and Z given the enlarged history.

If the next coordinate is h in H, all its parents other than Y have already been exposed in B. Its assignment and its independent noise give a fixed observation kernel Q_h(history,y,dx_h), independent of e and Z. Given the previous history, the joint conditional law of (Y,X_h) is

Pi(history,dy) Q_h(history,y,dx_h),

where Pi is the current posterior. Apply the parameterized kernel construction above, with the previous history as parameter, to choose the updated posterior Pi_new(history,x_h,dy). It is one measurable formula valid for each fixed history parameter. Since the observation uses only Y, the fixed history, and a fresh independent noise, the previous conditional independence of Y and Z implies that Y and Z remain conditionally independent after this observation. The disintegration identity holds for every parameter, so it remains valid after integration against the history law in any fixed environment. No observational distribution over environments is used to choose the update.

Induction finishes the construction. The final posterior depends measurably on x_B only, not e. Denote it by K_B(x_B,dy). For every fixed e it is a conditional-law version of Y given X_B under P_e. Thus B is invariant in the task's precise every-environment sense.

Define the mean of K_B where its absolute first moment is finite and set it to zero elsewhere. Integrability of Y under each P_e makes the exceptional set null under each environment's X_B marginal. This gives the required real-valued measurable f_S and

E_e[Y|X_B]=f_S(X)

almost surely for every e. Any other common conditional-law version yields the same conditional mean almost surely under each environment and hence the same risks.

Combine this construction with Section 1's environmentwise conditional independence. The standard identity for integrable Y is: if Y is conditionally independent of Z' given U', then E[Y|U',Z']=E[Y|U'] almost surely. Its integrability hypothesis is explicit here. It yields

E_e[Y|X_W]=E_e[Y|X_B]=f_S(X)

in every environment. In fact K_B(x_B,dy), viewed as a function of x_W, is also a common conditional-law kernel given X_W. This establishes the complement's common version without an unsupported upgrade from augmented-law conditional independence.

### 3. Condition II implies Condition I

Fix e and its companion e' under Condition II. Replace assignments at C_int by the stipulated independent noises, leaving every other assignment and noise law unchanged. Let G' delete incoming edges into C_int, with E subsequently fixed.

No node of B, or ancestor of such a node, has a replaced assignment, because B is outside the descendant-closed set D. Couple the unchanged exogenous noises in e and e' and evaluate assignments recursively. X_B is identical under this coupling, proving equality of its marginals.

Consider a path in G' from Y to an original forbidden covariate, conditioning on X_W. If it starts Y<-i, the parent i lies in W and is a conditioned noncollider. If it starts Y->i with i in D, the graph condition places that original child in C_int, so the edge was deleted. Otherwise the first child i belongs to H and is conditioned on. If it is a noncollider it blocks the path. If it is a collider, its next node k is another original covariate parent of i, belongs to B and W, and is a conditioned noncollider. The child i was not replaced, so its parent set is unchanged. Every path is blocked.

Markovness of the modified SCM gives Y independent of X_D given X_W under P_e'. Thus e' satisfies both parts of Condition I. The independence stipulated for replacement noises does not assert independence of their outputs from descendants generated later.

### 4. Conditional risk comparison

It suffices to use Condition I. Fix a measurable f and an environment e, and choose its companion e'. Condition I's conditional independence, integrability, and Section 2 give

E_e'[Y|X]=E_e'[Y|X_W]=f_S(X)

almost surely.

If R_e'(f)=+infinity, then R_e'(f)>=R_e'(f_S) immediately because the latter is finite. Otherwise condition on X. Its conditional response law has finite absolute first moment almost surely. Nonnegativity and the stipulated finite risks ensure that the conditional expected losses at f(X) and at E_e'[Y|X] are both finite almost surely. Strict consistency on its finite-expectation domain therefore gives

E_e'[ell(Y,f(X))|X] >= E_e'[ell(Y,E_e'[Y|X])|X]

almost surely. Integrating and identifying the conditional mean yields

R_e'(f) >= R_e'(f_S).

Only the minimizing inequality is needed; no uniqueness of a worst-case minimizer is claimed.

### 5. Risk transfer and suprema

Condition I gives identical X_S marginals under e and e'. The constructed K_B is a conditional-law version under both environments, including any environments having observational probability zero. Therefore their joint laws of (Y,X_S) are identical. Since ell(Y,f_S(X)) is a measurable function of this pair,

R_e'(f_S)=R_e(f_S).

Consequently,

sup_(a in E) R_a(f) >= R_e'(f) >= R_e(f_S).

Take the supremum over arbitrary e on the right. This proves the required inequality. The extended-order argument also applies if a supremum is infinite and needs neither attainment nor measurable selection of companion environments. Since f_S is a measurable predictor, it is a minimizer over the stated class.

When C_int or D is empty, the forbidden-path cases disappear. When H is empty, the common-kernel construction has no posterior observation updates. When S is empty, its kernel is the fixed unconditional law of Y and its mean is constant. Constant interventions are included. No faithfulness, density, positivity, atomic environment law, or finite environment set was used.

## Obligation Closure

The graphical separations are proved by explicit path cases. A particular common conditional-law version is constructed from the unchanged structural mechanisms, with the parameterized measurable disintegration step derived by finite partitions and bounded martingale convergence. The recursion is verified under each fixed environment separately and does not modify an arbitrary observational version. Marginal preservation, modified-graph independence, conditional-mean removal, finite-domain loss comparison, joint-law transfer, and supremum passage are explicit. No theorem-critical obligation remains unresolved.
