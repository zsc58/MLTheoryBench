# Reference Proof

## Proof Structure

The proof obligations are: differentiate the components and derive the elasticity identities; establish exact proportional rescaling and its quadratic remainder; differentiate margins and softmax probabilities; establish exact logarithmic component additivity; and justify each local expansion with its correct domain and remainder. All coefficients and exponents remain fixed.

## Complete Proof

Write `z_{c,k}(x) = alpha_{c,k} product_l x_l^{beta_{c,k,l}}`. Every component is smooth on the positive input orthant, including when its coefficient is zero or negative. The power rule gives
`partial z_{c,k}/partial x_j = beta_{c,k,j} z_{c,k}/x_j`.
Differentiating with respect to the coordinate `log x_j`, with other coordinates fixed, therefore gives
`G_{c,j}(x) = x_j partial z_c/partial x_j = sum_k beta_{c,k,j} z_{c,k}(x)`
throughout that orthant. Whenever `z_c(x)>0`, continuity makes the score positive on a neighborhood of x, so its logarithm is smooth there. The chain rule yields
`E_{c,j}(x) = G_{c,j}(x)/z_c(x) = sum_k (z_{c,k}(x)/z_c(x)) beta_{c,k,j}`.
Multiplying by `z_c(x)` gives `G_{c,j}(x)=z_c(x)E_{c,j}(x)` on precisely this domain. No component-sign assumption is used in these identities.

For a proportional change, set `x'_j=q x_j`, with `q>0`, and leave all other coordinates fixed. Each component is multiplied by `q^{beta_{c,k,j}}`. Summation gives the exact identity
`z_c(x') = sum_k q^{beta_{c,k,j}} z_{c,k}(x)`.
For each fixed real exponent beta, the function `epsilon -> (1+epsilon)^beta` is twice continuously differentiable near zero, with bounded second derivative on a sufficiently small closed interval. Taylor's theorem gives
`(1+epsilon)^beta = 1 + beta epsilon + O(epsilon^2)`.
There are finitely many terms, and x and the parameters are fixed. Multiplying these expansions by the component values and summing therefore gives
`z_c(x') = z_c(x) + epsilon sum_k beta_{c,k,j} z_{c,k}(x) + O(epsilon^2) = z_c(x) + epsilon G_{c,j}(x) + O(epsilon^2)`.
For sufficiently small epsilon, `1+epsilon>0`, as required.

For `M_{c,c'}=z_c-z_{c'}`, linearity of differentiation yields
`partial M_{c,c'}/partial log x_j = G_{c,j}-G_{c',j}`
throughout the positive input orthant. If both scores are positive, substituting the already proved elasticity relation gives
`G_{c,j}-G_{c',j}=z_c E_{c,j}-z_{c'} E_{c',j}`.
No positive-score assumption is needed for the first equality.

Let `S(x)=sum_r exp(z_r(x))`. This is smooth and strictly positive for every positive input, regardless of the signs of the scores. Since
`partial S/partial log x_j = sum_r exp(z_r) G_{r,j}`,
the quotient rule gives
`partial p_c/partial log x_j = exp(z_c)G_{c,j}/S - exp(z_c)(sum_r exp(z_r)G_{r,j})/S^2 = p_c [G_{c,j}-sum_r p_r G_{r,j}]`.
Every G in this formula is defined even when its score is nonpositive.

If `z_{c,k}(x)>0`, the product of the positive coordinate powers shows that `alpha_{c,k}>0`. Consequently this component is positive at every positive baseline b. Taking logarithms at x and b and subtracting gives
`log z_{c,k}(x)-log z_{c,k}(b) = sum_j beta_{c,k,j}(log x_j-log b_j) = sum_j beta_{c,k,j} log(x_j/b_j)`.
When `K=1`, the component is the entire class score, so the same identity holds for that score whenever it is positive. Components with zero or negative coefficients are not included in this logarithmic assertion.

For completeness, the standard Taylor result used for the remaining expansions is the following: if a real-valued function F is C2 on a neighborhood of zero in a finite-dimensional Euclidean space, then
`F(delta)=F(0)+sum_j partial_j F(0) delta_j+O(||delta||^2)`.
Indeed, choose a closed ball about zero contained in that neighborhood. The continuous Hessian has bounded operator norm there, say B. Applying the one-dimensional Taylor formula with integral remainder to `t -> F(t delta)` bounds the remainder by `B ||delta||^2/2` for delta in the ball. This establishes the stated order without any uniformity over changing functions or baselines.

Fix `b in R_{>0}^m` and write `x_j=b_j exp(delta_j)`. The functions `delta -> z_c(x)` and `delta -> p_c(x)` are smooth near zero for every such b. Their derivatives at zero are respectively `G_{c,j}(b)` and
`p_c(b)[G_{c,j}(b)-sum_r p_r(b)G_{r,j}(b)]`.
The Taylor result just stated therefore gives
`z_c(x)=z_c(b)+sum_j G_{c,j}(b) delta_j+O(||delta||^2)`
and
`p_c(x)=p_c(b)+sum_j p_c(b)[G_{c,j}(b)-sum_r p_r(b)G_{r,j}(b)] delta_j+O(||delta||^2)`.
These two expansions impose no score-sign conditions.

If additionally `z_c(b)>0`, continuity gives a neighborhood of delta=0 on which `z_c(x)>0`. Thus `delta -> log z_c(x)` is smooth on that neighborhood, and its derivative at zero is `E_{c,j}(b)`. Applying the same Taylor result gives
`log z_c(x)=log z_c(b)+sum_j E_{c,j}(b) delta_j+O(||delta||^2)`.
All remainder constants are local constants for fixed dimensions, parameters, indices, and expansion point. This proves every asserted identity and expansion on its stated domain.
