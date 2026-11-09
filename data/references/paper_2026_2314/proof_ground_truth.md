# Reference Proof

## Proof Structure

1. Express every simplex directional derivative through the influence function and identify its arm-wise expectation coordinates.
2. Prove these coordinates are the centered simplex gradient, using the mixture-centering identity and uniqueness modulo the all-ones vector.
3. Condition on the sampled arm to compute the expectation of the one-sample score vector.
4. Use the softmax Jacobian and the chain rule to identify that expectation with the logit-space gradient.

## Complete Proof

Fix an interior weight vector $w\in\Delta_K^\circ$ and a tangent vector $v\in\mathbb R^K$ with $\sum_i v_i=0$. For sufficiently small $\varepsilon$, $w+\varepsilon v$ remains in the simplex, and
\[
Q_{w+\varepsilon v}=\sum_i(w_i+\varepsilon v_i)Q_i
=Q_w+\varepsilon\sum_i v_iQ_i.
\]
By influence-function differentiability,
\[
D F(w)[v]
=\int \phi_w\,d\Big(\sum_i v_iQ_i\Big)
=\sum_i v_i\int\phi_w\,dQ_i.
\]
Define $g_i(w):=\mathbb E_{Q_i}[\phi_w(Y)]$. Thus $D F(w)[v]=\sum_i v_i g_i(w)$ for every tangent $v$, so $g(w)$ is a simplex-gradient representative. Moreover,
\[
\sum_iw_i g_i(w)
=\int\phi_w\,dQ_w
=0,
\]
so $g(w)$ is centered.

If two vectors represent all tangent directional derivatives, their difference has zero inner product with every vector $e_i-e_j$; hence all its coordinates are equal. Therefore simplex gradients are unique modulo multiples of the all-ones vector, and the centering condition selects the representative $g(w)$ above.

Now let $h\in\mathbb R^K$, set $w=\sigma(h)$, sample $A\sim\operatorname{Categorical}(w)$, and conditionally sample $Y\mid A=i\sim Q_i$. Define
\[
Z_k=(\mathbf 1\{A=k\}-w_k)\phi_w(Y),\qquad k=1,\ldots,K.
\]
For each coordinate, conditioning on $A$ gives
\[
\mathbb E[Z_k]
= w_k\mathbb E_{Q_k}[\phi_w(Y)]
-w_k\sum_iw_i\mathbb E_{Q_i}[\phi_w(Y)]
= w_kg_k(w),
\]
where the second term vanishes by centering. Hence
\[
\mathbb E[Z]=\operatorname{diag}(w)g(w).
\]
Since $\langle w,g(w)\rangle=0$, this equals
\[
(\operatorname{diag}(w)-ww^\top)g(w)=J(h)g(w).
\]
The softmax Jacobian is $J(h)=\operatorname{diag}(w)-ww^\top$, and the chain rule yields
\[
\nabla_h(F\circ\sigma)(h)=J(h)g(w).
\]
Therefore $\mathbb E[Z]=\nabla_h(F\circ\sigma)(h)$, proving both the centered simplex-gradient formula and unbiasedness of the single-draw bandit estimator.
