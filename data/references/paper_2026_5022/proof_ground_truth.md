# Reference Proof

## Proof Structure

1. Differentiate the negative Frobenius-inner-product loss with the realized activations and targets held fixed, and accumulate the updates over the specified prior chunks.
2. Establish integrability of the query-logit terms, expand their finite sum, and use the unrelated-position assumption to retain only the matching key position.
3. For the LM-aligned target, apply the alignment and embedding norm assumptions for the correct token and near-orthogonality for every incorrect token.
4. For reconstruction targeting, use the distinctness of the key and next-token embeddings and near-orthogonality to obtain the epsilon-scale correct-logit bound.

## Complete Proof

Fix either target choice. Every differentiation below holds the realized activations and targets fixed. For a chunk with index set $I$, write its matrices as $Z_I$ and $V_I$. The loss can be written entrywise as
\[
L(Z_IW^T,V_I)
=-\sum_{t\in I}\sum_{a=1}^d\sum_{b=1}^r v_{t,a}W_{ab}z_{t,b}.
\]
Consequently,
\[
\frac{\partial L}{\partial W_{ab}}
=-\sum_{t\in I}v_{t,a}z_{t,b},
\qquad
\nabla_W L(Z_IW^T,V_I)=-V_I^TZ_I.
\]
Thus the update following evaluation of chunk $i$ is
\[
W^{(i+1)}=W^{(i)}+\lambda V_{[i]}^TZ_{[i]}.
\]
The loss is the stated unnormalized Frobenius inner product, so there is no division by the chunk size.

The sets $I_0,\ldots,I_{m-1}$ partition $\{1,\ldots,n-1\}$, and every one of their updates is completed before the query is evaluated. Telescoping the updates therefore gives
\[
\Delta W
=\lambda\sum_{i=0}^{m-1}V_{[i]}^TZ_{[i]}
=\lambda\sum_{t=1}^{n-1}v_tz_t^T.
\]
For any fixed vocabulary item $w$,
\[
\Delta\ell_n[w]
=e_w^T\Delta Wz_n
=\lambda\sum_{t=1}^{n-1}(e_w^Tv_t)(z_t^Tz_n).
\]
The coefficient $e_w^Tv_t$ is a finite deterministic real number. The hypothesis $\mathbb E[|z_t^Tz_n|]<\infty$ therefore makes each summand integrable. There are only finitely many prior positions, so the logit change is integrable and linearity of expectation applies:
\[
\mathbb E[\Delta\ell_n[w]]
=\lambda\sum_{t=1}^{n-1}e_w^T\mathbb E[(v_tz_t^T)z_n].
\]
For every $t\ne t^*$ the vector expectation in this sum is zero by the assumption for the target choice under consideration. Hence
\[
\mathbb E[\Delta\ell_n[w]]
=\lambda\mathbb E[(e_w^Tv_{t^*})(z_{t^*}^Tz_n)].
\]
The matching target is also deterministic. Factoring out its coefficient and using the alignment assumption gives
\[
\mathbb E[\Delta\ell_n[w]]
=\lambda(e_w^Tv_{t^*})c_{\rm align}.
\]
This reduction uses no independence assumption and does not require the alignment inner product to be nonnegative in every realization.

### LM-aligned targeting

Here $v_{t^*}=e_{x_{t^*+1}}=e_{v^*}$. For the correct item,
\[
\mathbb E[\Delta\ell_n[v^*]]
=\lambda\|e_{v^*}\|^2c_{\rm align}
\ge\lambda c_{\rm norm}^2c_{\rm align},
\]
where multiplication preserves the inequality because $\lambda>0$ and $c_{\rm align}>0$.

For every $w\ne v^*$,
\[
|\mathbb E[\Delta\ell_n[w]]|
=\lambda|e_w^Te_{v^*}|c_{\rm align}
\le\lambda\epsilon c_{\rm align}.
\]
This proves both bounds for the LM-aligned run.

### Reconstruction targeting

Here $v_{t^*}=e_{x_{t^*}}=e_{k^*}$. Repeating the expectation reduction with the reconstruction targets and their unrelated-position assumption gives
\[
\mathbb E[\Delta\ell_n[v^*]]
=\lambda(e_{v^*}^Te_{k^*})c_{\rm align}.
\]
Since $k^*\ne v^*$, near-orthogonality applies to these two embeddings, yielding
\[
|\mathbb E[\Delta\ell_n[v^*]]|
=\lambda|e_{v^*}^Te_{k^*}|c_{\rm align}
\le\lambda\epsilon c_{\rm align}.
\]
All claimed bounds follow.

## Source and Closure Notes

The expectation convention is the one stated at L000378–L000381: representations are random, while token targets are determined. The key/value distinctness used for reconstruction is explicitly supplied at L000402. The exact-size partition condition merely makes the domain of the frozen all-prior-chunks procedure explicit.

The explicit scalar integrability condition does not impose a new second-moment or independence assumption. The source's matching scalar expectation is finite. At each other position, the source assumes a finite vector expectation of $v_t(z_t^Tz_n)$; because $v_t$ is fixed and nonzero, finiteness of its nonzero coordinate already entails integrability of $z_t^Tz_n$.

The source omits the learning-rate factor in the intermediate expectations at both L000395 and L000400. The common preceding expression at L000385 and the following bounds at L000396 and L000403 uniquely require that factor. It is retained throughout this proof, as it was in the previous reference proof. The distinction between a single chunk update and the accumulated prior-context change is also retained.

The four theorem-critical obligations listed above are fully discharged. No specialized external result, learned-convolution property, context-parallel implementation claim, or empirical update-clipping rule is used.
