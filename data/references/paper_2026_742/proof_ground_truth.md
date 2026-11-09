# Reference Proof

## Proof Structure

First verify that the adaptive parameter is well defined and measurable. For the actual online rule, compare the next-round loss with the current empirical average using a uniformly deleted occurrence and exchangeability at a deterministic time. This yields the regret decomposition. Optimize its accuracy-sensitivity sum by the minimizing selector, use Jensen twice and a direct random-prefix optimum estimate, and control its parameter-change sum by stability and a supergradient telescope.

## Complete Proof

Fix the horizon and the full multiset M. All permutation expectations below are for this fixed multiset. Put g(u)=phi*(u), e(u)=epsilon_min(u), epsilon_t=e(OPT_t+lambda), and epsilon_empty=e(lambda).

### 1. Well-defined selector and its properties

Because phi is proper, choose epsilon_0 in (0,1] with phi(epsilon_0)<infinity. For each u>0, the extended-valued function epsilon->u epsilon+phi(epsilon) is lower-semicontinuous on the compact interval [0,1], has a finite feasible value, and is infinite at zero. Thus its minimum is finite and attained at a point in (0,1]. In particular,

`g(u)=u e(u)+phi(e(u))`.

The function g is nonnegative and nondecreasing, since every affine objective has a positive slope. It is concave: for 0<=a<=1, taking the infimum of the affine objectives gives

`g(a u+(1-a)v) >= a g(u)+(1-a)g(v)`.

The selector is non-increasing. Indeed, if 0<u<v, optimality at the two arguments gives

`u e(u)+phi(e(u)) <= u e(v)+phi(e(v))`,

`v e(v)+phi(e(v)) <= v e(u)+phi(e(u))`.

Adding yields `(v-u)(e(u)-e(v))>=0`. Therefore every fixed tie-broken selector is a Borel function of u. Together with the stated measurability of OPT and of the offline kernel, this makes the adaptive laws measurable.

Using e(u) as a feasible choice at v also gives, for all u,v>0,

`g(v) <= g(u)+e(u)(v-u)`.

This is the supergradient inequality that will be used below. These comparisons also imply `0<=g(v)-g(u)<=v-u` when v>=u, so all applications of Jensen below concern finite, integrable quantities on bounded argument intervals.

### 2. Bounded-loss TV control

For probability laws P,Q and any measurable h with 0<=h<=1, the layer-cake formula gives

`integral h dP-integral h dQ = integral_0^1 [P(h>s)-Q(h>s)] ds`.

Consequently,

`|integral h dP-integral h dQ| <= TV(P,Q)`.

No optimal coupling or product-measure theorem is needed.

### 3. Fresh-loss comparison for the online learner

For every finite multiset Y, including the empty multiset, write

`B(Y)=A_{epsilon_Y}(Y)`,

`f(Y,z)=integral ell(theta,z) B(Y)(dtheta)`.

For t<T the learner's next prediction has conditional law B(X_t), so its expected next-round loss is `E f(X_t,x_{t+1})`.

Independently choose an index I uniformly from {1,...,t}, put x=x_I, and U=X_t minus {x}. Occurrences are distinguished when sampling I, even when their values coincide. Conditional on the reduced multiset U, the deleted occurrence x and the next occurrence x_{t+1} are exchangeable: swapping their two positions is a measure-preserving bijection of the uniform permutations and leaves U unchanged. Since B(U) depends only on U,

`E f(U,x)=E f(U,x_{t+1})`.

It follows, by adding and subtracting the reduced-input loss, that

`E[f(X_t,x_{t+1})-(1/t)sum_{x in X_t} f(X_t,x)]`

`= E (1/t)sum_{x in X_t} [f(X_t,x_{t+1})-f(X_t minus {x},x_{t+1})`

`+ f(X_t minus {x},x)-f(X_t,x)]`.

Apply bounded-loss TV control to both differences. For each deletion, the triangle inequality gives

`TV(B(X_t),B(X_t minus {x}))`

`<= TV(A_{epsilon_t}(X_t),A_{epsilon_t}(X_t minus {x}))`

`+ TV(A_{epsilon_t}(X_t minus {x}),A_{epsilon_{X_t minus {x}}}(X_t minus {x}))`.

Define

`P_t=(2/t)sum_{x in X_t} TV(A_{epsilon_t}(X_t minus {x}),A_{epsilon_{X_t minus {x}}}(X_t minus {x}))`.

Conditional on X_t, epsilon_t is fixed, so the offline sensitivity assumption applies at this value. Twice its averaged deletion bound is phi(epsilon_t)/t. The approximation assumption gives

`(1/t)sum_{x in X_t} f(X_t,x) <= (1+epsilon_t)OPT_t/t+c/T`.

Combining these facts proves, for every 1<=t<T,

`E ell(theta_{t+1},x_{t+1}) <= E[(1+epsilon_t)OPT_t/t+phi(epsilon_t)/t+P_t]+c/T`.

### 4. Prefix-optimum estimate and regret decomposition

Choose a minimizer theta_star of the full-multiset loss. For every realized prefix,

`OPT_t <= sum_{x in X_t} ell(theta_star,x)`.

Each occurrence of M belongs to X_t with probability t/T. Thus

`E OPT_t <= (t/T)OPT_T`,

and summing after division by t gives

`E sum_{t=1}^T OPT_t/t <= OPT_T`.

The initial loss is at most one. Sum the fresh-loss comparison over t=1,...,T-1 and extend its nonnegative right-hand summands through T. Subtract OPT_T and apply the preceding prefix estimate. Since the accumulated approximation error is at most c, this yields

`R_T <= E sum_{t=1}^T [epsilon_t OPT_t+phi(epsilon_t)]/t + E sum_{t=1}^T P_t+c+1`.

This derivation concerns the prediction-before-observation learner, not a rule that chooses its current accuracy after seeing its current loss instance. It also holds for T=1, when the fresh-loss sum is empty.

### 5. Adaptive accuracy-sensitivity bound

Optimality gives

`epsilon_t OPT_t+phi(epsilon_t)=g(OPT_t+lambda)-lambda epsilon_t <= g(OPT_t+lambda)`.

Jensen's inequality for the concave function g with weights 1/(t H_T) therefore gives, for each realized permutation,

`sum_{t=1}^T [epsilon_t OPT_t+phi(epsilon_t)]/t`

`<= H_T g((sum_{t=1}^T OPT_t/t)/H_T+lambda)`.

Apply Jensen again to the random argument, then apply the prefix estimate and monotonicity of g:

`E sum_{t=1}^T [epsilon_t OPT_t+phi(epsilon_t)]/t`

`<= H_T g((E sum_{t=1}^T OPT_t/t)/H_T+lambda)`

`<= H_T g(OPT_T/H_T+lambda)`.

### 6. Parameter-change bound and telescope

Since TV is at most one, P_1<=2. For t>=2, the parameter-change assumption gives

`P_t <= (C_pc epsilon_t/t)sum_{x in X_t} [OPT_t-OPT(X_t minus {x})]`.

Conditional on X_t, its last occurrence is uniformly distributed among its t occurrences. Therefore

`E[OPT_{t-1}|X_t]=(1/t)sum_{x in X_t} OPT(X_t minus {x})`.

Because epsilon_t depends only on X_t, taking expectations yields

`E P_t <= C_pc E[epsilon_t(OPT_t-OPT_{t-1})]`.

Nonnegative losses imply OPT_t>=OPT_{t-1}. Since C_pc>=0, we may extend the weighted-increment sum to include t=1, obtaining

`E sum_{t=1}^T P_t <= 2+C_pc E sum_{t=1}^T epsilon_t(OPT_t-OPT_{t-1})`.

Put a_t=OPT_t+lambda and a_0=lambda. All these arguments are positive, including when some or all prefix optima vanish. The supergradient inequality at a_t, evaluated at a_{t-1}, gives

`epsilon_t(OPT_t-OPT_{t-1}) <= g(a_t)-g(a_{t-1})`.

Consequently, for every permutation,

`sum_{t=1}^T epsilon_t(OPT_t-OPT_{t-1}) <= g(OPT_T+lambda)-g(lambda)`.

The endpoint OPT_T is deterministic. Thus

`E sum_{t=1}^T P_t <= 2+C_pc[g(OPT_T+lambda)-g(lambda)]`.

### 7. Conclusion and constants

Substitute the two bounds into the regret decomposition:

`R_T <= H_T phi*(OPT_T/H_T+lambda)`

`+ C_pc[phi*(OPT_T+lambda)-phi*(lambda)]+c+3`.

The constant c+3 is independent of T and the presented multiset. In particular, the asserted O(1) does not conceal any dependence on possibly horizon-dependent phi or C_pc. The proof includes T=1, repeated instances, and OPT_T=0. All theorem-critical obligations have been derived explicitly.
