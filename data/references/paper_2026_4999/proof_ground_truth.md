# Reference Proof

## Proof Structure

1. Bound the logit perturbation caused by replacing the weight matrix.
2. Compute the softmax Jacobian and bound each row's `\ell_1` norm by `1/2`.
3. Apply the mean-value integral along the segment between the two logit vectors and combine the bounds uniformly over inputs and classes.

## Complete Proof

Fix `x` and write `h=h(x)`. Let `\Delta W=\widetilde W-W`. Since the two classifiers share the same bias,

`\widetilde z(x)-z(x)=\Delta W h`.

Therefore,

`\|\widetilde z(x)-z(x)\|_\infty\le \|\Delta W h\|_2\le \|\Delta W\|_2\|h\|_2\le R\|\widetilde W-W\|_2`.

For `u\in\mathbb R^C`, set `s(u)=\sum_{\ell=1}^C e^{u_\ell}`. Differentiating `\sigma_i(u)=e^{u_i}/s(u)` gives

`\partial_j\sigma_i(u)=\sigma_i(u)(\delta_{ij}-\sigma_j(u))`.

Thus `J_\sigma(u)=\operatorname{diag}(\sigma(u))-\sigma(u)\sigma(u)^\top`. Its `i`th row has absolute sum

`|\sigma_i(1-\sigma_i)|+\sum_{j\ne i}\sigma_i\sigma_j
 =2\sigma_i(1-\sigma_i)\le 1/2`,

because `0\le\sigma_i\le1` and `t(1-t)\le1/4` on `[0,1]`.

Let `a=z(x)`, `\tilde a=\widetilde z(x)`, and `d=\tilde a-a`. For each coordinate `i`, apply the mean-value integral along `a+td`:

`\sigma_i(\tilde a)-\sigma_i(a)=\int_0^1 \nabla\sigma_i(a+td)^\top d\,dt`.

The row-sum bound and the `\ell_1`-`\ell_\infty` dual inequality imply

`|\sigma_i(\tilde a)-\sigma_i(a)|\le\int_0^1 (1/2)\|d\|_\infty\,dt=(1/2)\|d\|_\infty`.

Taking the maximum over `i` and substituting the logit estimate yields

`\|\widetilde p(x)-p(x)\|_\infty\le (1/2)R\|\widetilde W-W\|_2`.

The bound is independent of `x`; hence it holds uniformly for all inputs. The coordinatewise class bound follows directly from the definition of the infinity norm.
