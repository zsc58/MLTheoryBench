# Reference Proof

## Proof Structure

Establish measurability and strictly positive finite normalization. Use power-mean monotonicity to bound the normalizer by one for orders at most one. For orders in `[0,1]`, combine Jensen's inequality, including the geometric-mean identity at order zero, with this normalizer bound. For negative orders, use the source's separated Gaussian densities and an explicit lower bound on their normalizer. For orders above one, use strict power-mean monotonicity at a consensus point. The same Gaussian family also handles both extended orders.

## Standard Results Used

For positive finite inputs `a_1,...,a_k` and orders `r<s`, the power-mean inequality states `M_r(a_1,...,a_k)<=M_s(a_1,...,a_k)`, with equality if and only if all inputs are equal. The minimum and maximum conventions give the extended-order comparisons as well. For positive finite `u_1,...,u_k`, concavity of the logarithm gives `log(k^{-1}sum_i u_i)>=k^{-1}sum_i log u_i`. All applications below have positive finite inputs.

## Complete Proof

### Well-Definedness and Normalizer Bounds

Each `p_i` is a measurable function with values in `(0,infinity)`. Every prescribed generalized mean is therefore measurable and strictly positive, including the geometric mean and the finite minimum and maximum. Since `integral_X p_1 dx=1`, the reference measure of `X` is not zero. A strictly positive measurable function on such a space has a strictly positive integral: if its integral were zero, each measurable set where its value is at least `1/n` would have measure zero, and their countable union is `X`.

By power-mean monotonicity,
`M_{k,r}(x)<=M_{k,+infinity}(x)=max_i p_i(x)<=sum_i p_i(x)`.
Integrating gives `0<Z_{k,r}<=k<infinity` for every finite or extended order. Thus the normalized aggregate is a measurable positive density, and all logarithms used below are finite at every point. If `r<=1`, then
`M_{k,r}(x)<=M_{k,1}(x)=k^{-1}sum_i p_i(x)`,
so `Z_{k,r}<=1`.

### Guarantee for Orders in `[0,1]`

Fix any positive integer `k`, any permitted collection of densities, and any `x in X`. If `0<r<=1`, apply the logarithmic Jensen inequality to `u_i=p_i(x)^r`:
`log(k^{-1}sum_i p_i(x)^r)>=k^{-1}sum_i log(p_i(x)^r)`.
Dividing by the positive number `r` yields
`log M_{k,r}(x)>=k^{-1}sum_i log p_i(x)`.
Since `0<Z_{k,r}<=1`,
`log p^circ_{k,r}(x)=log M_{k,r}(x)-log Z_{k,r}>=k^{-1}sum_i log p_i(x)`.

For `r=0`, the definition gives
`log M_{k,0}(x)=k^{-1}sum_i log p_i(x)`,
and the same conclusion follows from `0<Z_{k,0}<=1`. This includes `k=1` and the endpoints `r=0,1` without additional restrictions.

### Gaussian Pair and a Normalizer Lower Bound

On `R` with Lebesgue measure, define the standard normal density
`phi(x)=(2*pi)^(-1/2)exp(-x^2/2)`.
For `m>0`, let
`p_1(x)=phi(x+m)` and `p_2(x)=phi(x-m)`.
These are measurable, strictly positive, finite probability densities and are distinct. For every order, the generalized mean is at least their minimum. For `m>=1` and `|x|<=1/m`,
`min(p_1(x),p_2(x))=phi(0)exp(-(m+|x|)^2/2)>=phi(0)exp(-(m+1/m)^2/2)`.
Integrating over this interval gives
`Z_{2,r}>=(2/m)phi(0)exp(-(m+1/m)^2/2)`.
Consequently,
`-log Z_{2,r}<=m^2/2+log m+1+1/(2*m^2)-log(2*phi(0))`.

### Counterexamples for Every Finite `r<0`

Fix a finite `r<0`. At `x=m`,
`p_1(m)=phi(0)exp(-2*m^2)` and `p_2(m)=phi(0)`.
The unnormalized excess over the average log-density equals
`D_m=log M_{2,r}(m)-(1/2)(log p_1(m)+log p_2(m))`
`=m^2+(1/r)log((1+exp(-2*r*m^2))/2)`
`=-m^2-(log 2)/r+(1/r)log(1+exp(2*r*m^2))`.
Because `r<0`, the last term is nonpositive. The normalized excess therefore satisfies
`D_m-log Z_{2,r}<=-m^2/2+log m+1+1/(2*m^2)-log(2*phi(0))-(log 2)/r`.
For the fixed order `r`, this tends to minus infinity as `m` tends to infinity. Choose `m>=1` sufficiently large to make it negative. This proves the required normalized violation. The choice of `m` is allowed to depend on `r`; no uniform separation over all negative orders is required.

### Counterexample for `r=-infinity`

Use the same Gaussian pair. At `x=m`, the minimum is `p_1(m)`, so
`log M_{2,-infinity}(m)-(1/2)(log p_1(m)+log p_2(m))=-m^2`.
The previously proved lower bound on the normalizer gives
`log p^circ_{2,-infinity}(m)-(1/2)(log p_1(m)+log p_2(m))`
`<=-m^2/2+log m+1+1/(2*m^2)-log(2*phi(0))`.
This is negative for sufficiently large `m`, proving the minimum-order violation. No upper tail bound on the normalizer is used.

### Counterexamples for Every `r>1`, Including `r=+infinity`

Fix any `m>0` and use the same Gaussian pair. At `x=0`,
`p_1(0)=p_2(0)=phi(m)`,
so `M_{2,r}(0)=phi(m)` for every order. The densities differ at every `x!=0`, a set of positive Lebesgue measure. For every finite `r>1`, strict power-mean monotonicity gives `M_{2,r}(x)>M_{2,1}(x)` on that set. For `r=+infinity`, the maximum is likewise strictly greater than the arithmetic mean there. The differences are measurable, nonnegative, integrable, and strictly positive on a set of positive measure; their integrals are strictly positive. Since `Z_{2,1}=1`, it follows that `Z_{2,r}>1`.

Thus
`log p^circ_{2,r}(0)=log phi(m)-log Z_{2,r}<log phi(m)`
`=(1/2)(log p_1(0)+log p_2(0))`.
This proves the required violations for every finite order above one and for the maximum order.

## Audit Notes

The source's finite-negative-order calculation must be supplemented by the displayed lower bound on its normalizer; an unnormalized deficit alone does not imply a normalized violation. The former private minimum-order proof incorrectly inferred an upper density-ratio bound from an upper normalizer bound. Both obligations are closed above with an elementary estimate using the unchanged Gaussian construction. No theorem-critical proof obligation remains unresolved.
