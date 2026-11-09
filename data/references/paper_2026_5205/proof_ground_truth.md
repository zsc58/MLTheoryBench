# Reference Proof

## Proof Structure and Obligations

The proof must establish: the geometric properties of the stated hat width; a continuous hard map chosen independently of the learner; exact unrestricted reconstruction; a fixed-query lower bound preserving the exact nonzero-parameter budget; globally admissible adaptive query maps; and a uniform reconstruction error and size bound valid for every eta > 0. All six obligations are closed below.

The mechanism is to encode the location r and the coefficient vector s in fixed hats, while placing the hard value G_m(s) at r. An unrestricted fixed-query learner can compute that value. A bounded-size fixed-query predictor is forced to approximate the hard map, whereas an adaptive learner reads its value by querying r.

## Standard-Independent Background

We use precisely the following two background results recorded in the supplied source.

1. For every fixed finite input dimension k and every fixed finite nonzero-parameter budget W, the class of binary classifiers obtained by thresholding scalar-output ReLU networks of size at most W at 1/2 has finite VC dimension. This is the finite-VC result used in source.html L000095-L000098 and indexed by theory_014. The architecture and parameter convention are those in the task; there is no bound on parameter magnitudes.
2. For every epsilon in (0,1), there is a ReLU network `Mult_epsilon:[0,1]^2 -> [0,1]` such that

   `sup_{a,b in [0,1]} |Mult_epsilon(a,b)-ab| <= epsilon`,

   with `O(log(1/epsilon))` nonzero parameters as epsilon decreases to zero. On `0 < epsilon <= 1/2`, its size can be bounded by `C(1+log(1/epsilon))` for an absolute constant C. This is the multiplication result stated in source.html L000307-L000312 and indexed by theory_007.

The first result is applied below with k=N-2 >= 1 and W=m. The second is applied only with epsilon in (0,1/2] and with both inputs in [0,1]. No paper-specific theorem is left as an unproved proof obligation.

## Geometry of the Fixed Family

Fix N >= 3, eta > 0, and the delta already specified in the task. We do not replace it by a smaller value. Since

`2 delta < 1/(3N) < 1/(2(N-1))`,

the closed supports of hats at distinct fixed centers q_i are disjoint. Also

`2 delta < 1/(3N) <= 1/9 < 1/6`,

so every fixed-hat support is disjoint from the support of every hat centered at r in [2/3,1]. These assertions remain valid when supports are truncated at the endpoints of [0,1].

Each hat takes values in [0,1], and at most one hat in a task's defining sum is nonzero at a given x. Consequently every task takes values in [0,1]. We also have

`2N delta < 1/3`.

These properties follow from the source restriction on delta; disjointness alone is not substituted for that restriction.

## Existence of the Hard Map

Let k=N-2 >= 1 and fix an integer m. Suppose, for contradiction, that every continuous map from [0,1]^k to [0,1] has a ReLU approximation of size at most m with uniform error strictly below 1/2.

Take an arbitrary finite set of distinct points z_1,...,z_K in the cube, with K >= 2, and an arbitrary labeling b_1,...,b_K in {0,1}. Choose rho > 0 smaller than half the minimum pairwise infinity-norm distance between these points. Define

`B_i(s)=max(0,1-||s-z_i||_infinity/rho)`

and

`g_b(s)=sum_{i:b_i=1} B_i(s)`.

The supports of these bumps are disjoint. Thus g_b is continuous, takes values in [0,1], and satisfies g_b(z_i)=b_i. An approximating network with error strictly below 1/2 has output below 1/2 at every point labeled 0 and above 1/2 at every point labeled 1. Thresholding therefore realizes the labeling.

Because a positive-dimensional cube contains arbitrarily large finite sets, this would give infinite VC dimension, contradicting the stated finite-VC result. Hence there is a continuous map `G_m:[0,1]^k -> [0,1]` such that every ReLU network R of size at most m satisfies

`sup_s |R(s)-G_m(s)| >= 1/2`.

Choose this G_m once for the whole task family, before considering any learner or its query points. Define F_{N,m}=F(G_m).

## Exact Unrestricted Reconstruction

Use the N fixed query points q_1,...,q_N. By the support separation,

`f_{s,r}(q_1)=r`,

`f_{s,r}(q_i)=s_i` for `2 <= i <= N-1`,

and `f_{s,r}(q_N)=0`.

An unrestricted predictor therefore recovers r and s, evaluates the known map G_m(s), and outputs

`r H_{q_1}(x) + sum_{i=2}^{N-1} s_i H_{q_i}(x) + G_m(s) H_r(x)`.

This is exactly f_{s,r}(x). Define the predictor arbitrarily, for example as zero, on other transcripts on which the displayed recovery is not applicable; unrestricted predictors need not be continuous. This makes it a map on the full required domain.

An unrestricted adaptive learner uses the same first query, constant subsequent query maps, and the same final predictor. Its output is identical. Both regimes therefore attain zero error, and their optimal errors are zero because errors are nonnegative. This directly establishes the needed unrestricted monotonicity rather than leaving it as an unproved dependency.

## Fixed-Query ReLU Lower Bound

Let a fixed-query ReLU learner have query points t_1,...,t_N and a final predictor P of size at most m. The union of the closed intervals `[t_j-delta,t_j+delta]` has length at most `2N delta < 1/3`. It cannot cover [2/3,1]. Choose r in that interval outside the union. This r may depend on the learner's fixed query points, but it is then held fixed while s varies over the entire coefficient cube.

For every j, H_r(t_j)=0. Thus

`y_j(s)=f_{s,r}(t_j)=r H_{q_1}(t_j)+sum_{i=2}^{N-1} s_i H_{q_i}(t_j)`.

The disjoint fixed supports give more than mere affineness: each y_j is either a constant or a constant multiple of one coordinate s_i, with no additional constant term in the latter case. Therefore every coordinate of

`z(s)=((t_j,y_j(s)))_{j=1}^N` followed by the test coordinate r

is either constant or a constant multiple of a single coordinate of s.

We now verify the exact parameter count. Take a network representation of P with at most m nonzero matrix and bias entries. Substitute z(s) directly into its first affine layer, including the fixed test coordinate. In any row of that layer, each old edge from a varying input contributes to at most one new coefficient. Contributions to the same coefficient can be combined, so the number of new nonzero variable coefficients is at most the number of old nonzero edges from varying inputs. All old constant-input contributions combine with the old bias into one new bias. If that new bias is nonzero, either the old bias was nonzero or there was at least one old nonzero edge from a constant input. The new bias can therefore be charged to an old parameter not used to count the varying-input edges. Row by row, the number of nonzero parameters does not increase.

Every later layer is unchanged. The same argument applies to a network with no hidden layer, when its first affine layer is also its output layer. Consequently

`R(s)=P(((t_j,y_j(s)))_{j=1}^N,r)`

is a ReLU network of size at most m. This conclusion uses the special coordinate structure just proved; arbitrary affine precomposition would not, by itself, justify preservation of the nonzero-parameter budget.

At x=r, all fixed hats vanish and H_r(r)=1, so

`f_{s,r}(r)=G_m(s)`.

It follows that the learner's worst-case uniform error is at least

`sup_s |R(s)-G_m(s)| >= 1/2`.

This proves the lower bound for every admissible fixed-query ReLU learner, with no change to its weight budget.

## Adaptive ReLU Construction

Let `sigma(u)=max(0,u)` and define the clipping map

`c(u)=sigma(u)-sigma(u-1)`.

It is a ReLU network, maps all real inputs into [0,1], and equals u on [0,1].

The adaptive learner first queries q_1=0. For n=2,...,N-1 it uses the constant query map Q_n=q_n. For its last query it uses

`Q_N(((t_j,y_j)))=c(y_1)`.

These are ReLU maps into [0,1] on their full transcript domains. Their sizes are bounded by a constant independent of delta, m, and G_m. On an actual task transcript, y_1=r and y_i=s_i for 2 <= i <= N-1, so the final query is exactly r. Its response is y_N=G_m(s). The total number of queries is exactly N.

The hats have the exact joint-input ReLU representation

`H_a(x)=sigma(1-(sigma(x-a)+sigma(a-x))/delta)`.

This representation applies both to a fixed center and to a center provided as an input. It uses a fixed number of nonzero parameters. Its coefficients may depend on delta, but its parameter count does not.

Choose

`epsilon=min{1/2,eta/N}`.

Then `0 < epsilon <= 1/2` and `N epsilon <= eta`. For an arbitrary transcript set `u_i=c(y_i)` for i=1,...,N. Define the final predictor to be c applied to

`Mult_epsilon(u_1,H_{q_1}(x)) + sum_{i=2}^{N-1} Mult_epsilon(u_i,H_{q_i}(x)) + Mult_epsilon(u_N,H_{u_1}(x))`.

Every multiplier input lies in [0,1], even on transcripts not generated by the family. The formula defines a single ReLU network acting jointly on the transcript and x: clipping, hat formation, parallel multiplication networks, summation, and final clipping can all be composed as finite affine/ReLU networks.

On a valid transcript, u_1=r, u_i=s_i for 2 <= i <= N-1, and u_N=G_m(s). There are exactly N products. Each has approximation error at most epsilon, uniformly over s, r, and x. Before final clipping, the total error is at most N epsilon. Since the true task value lies in [0,1], final clipping cannot increase the error. Therefore

`sup_{f in F_{N,m}} sup_{x in [0,1]} |P(C_N(f),x)-f(x)| <= N epsilon <= eta`.

For completeness, the size bound is uniform in delta. The clipping and hat networks have sizes bounded in terms of N alone. Use N parallel copies of the same multiplication network, with identical depths; the necessary routing and summation are implemented by sparse affine maps. The resulting predictor has at most `C_N(1+log(1/epsilon))` nonzero parameters for some finite constant C_N depending only on N. The factors 1/delta change parameter values, not the number of parameters. No evaluation or representation of G_m occurs inside these networks.

Choose an integer m_0(N,eta) at least 1 and at least the size of this predictor and every query network. For every m >= m_0, select the hard map for that m as above. The adaptive construction respects the same query and weight budgets as those used in the lower bound, for every allowed delta.

## Conclusion

Both unrestricted regimes attain zero error. Every fixed-query ReLU learner has error at least 1/2, and the constructed adaptive ReLU learner has error at most eta. When eta < 1/2 the latter bound is strictly smaller. A fixed-query learner can also be simulated by constant adaptive query maps; on the scalar domain these maps require at most one nonzero bias each, so they fit the sufficiently large common budget. Thus the asserted strict adaptive advantage and unrestricted equality both follow.

All theorem-critical obligations are explicitly established or obtained from the two stated standard-independent results with their hypotheses verified. There is no unresolved private proof obligation.
