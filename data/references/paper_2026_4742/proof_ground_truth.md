# Reference Proof

## Proof Structure

Treat the escort field and hence `g_alpha` as fixed data. Rewrite the distance objective as a strictly convex quadratic, project its unconstrained target onto the zero-mean subspace, then solve the lower-bounded problem by a single normalization multiplier and a pointwise clipped quadratic. Verify integrability and square integrability in the countably infinite case. The clamped branch gives exact sparsity.

## Complete Proof

Write `g=g_alpha`, `E=E_{pi_k}`, and `u*=g/mu`. Since the reference measure is a probability measure and `g in H`, Cauchy-Schwarz gives `E[|g|]<=||g||<infinity`. The same observation applies to every element of `H`. Since every action has strictly positive reference mass, equality almost everywhere is equality at every action.

Since `mu>0`,

`(mu/2)||v-u*||^2 = (mu/2)||v||^2 - <g,v> + (1/(2mu))||g||^2`.

The final term is independent of `v`, so minimizing the distance is equivalent to maximizing `J(v)=<g,v>-(mu/2)||v||^2`.

The Hilbert projection theorem states that every vector in a Hilbert space has a unique nearest point in a nonempty closed linear subspace, characterized by an orthogonal residual. Here `H` is a Hilbert space, `1 in H`, and `||1||^2=E[1]=1`. The functional `f -> <f,1>` is continuous, so `H0={1}^perp` is a closed subspace containing zero. For any `f in H`, the vector `f-E[f]1` lies in `H0` and its residual is a multiple of `1`, hence orthogonal to `H0`. Consequently `P_H0(f)=f-E[f]1`, and

`v_perp=P_H0(u*)=(g-E[g]1)/mu`

is the unique minimizer over `H0`.

For the bounded problem define, for each real `lambda`,

`h_lambda(y)=max(-1,(g(y)-lambda)/mu)`,

`F(lambda)=E[h_lambda]`.

The pointwise bound

`|h_lambda| <= 1+(|g|+|lambda|)/mu`

shows that `h_lambda in H`, since the right-hand side is square integrable. In particular, `F(lambda)` is finite. The scalar clipping map is nondecreasing and 1-Lipschitz, so

`|F(lambda)-F(kappa)| <= |lambda-kappa|/mu`,

and `F` is continuous and nonincreasing.

Also `F(lambda)>=(E[g]-lambda)/mu`, which implies `F(lambda) -> +infinity` as `lambda -> -infinity`. For `lambda>=0`, the functions `h_lambda` converge pointwise to `-1` as `lambda -> +infinity` and satisfy

`|h_lambda| <= 1+|g|/mu`.

The displayed dominating function is integrable. Dominated convergence therefore gives `F(lambda) -> -1` as `lambda -> +infinity`. Continuity and the intermediate value theorem yield a real root `lambda*`.

For uniqueness, suppose `lambda_1<lambda_2` are both roots. Let `S={y:h_lambda_2(y)>-1}`. This set has positive reference probability: otherwise `F(lambda_2)=-1`, contradicting its being zero. On `S`, both clipped functions use their affine branches, so

`h_lambda_1-h_lambda_2=(lambda_2-lambda_1)/mu`.

Outside `S`, their difference is nonnegative. Thus

`F(lambda_1)-F(lambda_2) >= ((lambda_2-lambda_1)/mu) pi_k(S) > 0`,

contradicting that both values are zero. The root is unique.

Set `v_b=h_lambda*`. The square-integrability bound above, its pointwise lower bound, and the root equation establish `v_b in K`.

For each action `y`, the strictly convex scalar function

`phi_y(t)=(mu/2)t^2-g(y)t+lambda* t`, for `t>=-1`,

has unconstrained minimum at `(g(y)-lambda*)/mu`, and hence its minimum on the half-line is attained at `t=v_b(y)`. For any `w in K`, integrate the pointwise inequalities to obtain

`(mu/2)||v_b||^2-<g,v_b>+lambda*E[v_b] <= (mu/2)||w||^2-<g,w>+lambda*E[w]`.

All terms are finite: the quadratic terms are integrable because `v_b,w in H`, the products with `g` are integrable by Cauchy-Schwarz, and the linear terms are integrable because `H` is contained in `L^1(pi_k)`. Both mean terms vanish. Therefore `J(v_b)>=J(w)`, proving global optimality for the original distance objective. The set `K` is convex, and the squared-distance objective is strictly convex because `mu>0`, so its minimizer is unique.

Finally, `v_b>=-1` implies that `pi_new(y)=pi_k(y)(1+v_b(y))` is nonnegative, and

`sum_y pi_new(y)=1+E[v_b]=1`.

Thus the update is a probability distribution. If `g(y)<lambda*-mu`, then the affine branch is below `-1`, so `v_b(y)=-1` and `pi_new(y)=0`. Threshold equality also produces zero mass, although the stated conclusion only requires the strict inequality.
