# Reference Proof

## Proof Structure

Fix an observation point. The observable embedded conditionals admit both the true and candidate factorizations. Full embedded rank forces an invertible change of basis between the latent components. The stochastic constraints and sufficient-scattering geometry give a determinant bound for that change of basis; hence the Gram-determinant minimizer is unique up to a permutation. Injectivity of the embedding gives equality of measures. Continuity, component separation, and connectedness make the pointwise permutation global, and an anchored subset removes it.

## Complete Proof

If $\mathcal O$ is empty, choose $\Sigma=I_k$. The first conclusion is vacuous and there is no nonempty anchor subset. Hence assume $\mathcal O$ is nonempty.

Fix $o\in\mathcal O$ and write
\[
T=T^*(o)=[\Phi(t_1^o)\ \cdots\ \Phi(t_k^o)],\qquad P=[\Phi(p_1^o)\ \cdots\ \Phi(p_m^o)].
\]
Linearity and the mixture identity give $P=T\Pi^*$, where $\Pi^*=\Pi^*(o)$. A feasible candidate gives $P=\bar T\Pi$, where $\bar T=[\Phi(\bar t_1^o)\ \cdots\ \Phi(\bar t_k^o)]$.

The true Gram matrix is positive semidefinite, and its positive determinant makes it positive definite. Thus $T$ is injective and has rank $k$. Put $K=\operatorname{cone}(\Pi^*)$. Since $k\ge2$, the inequality defining $C_k$ is strict at $\mathbf1$: $k>\sqrt{k(k-1)}$. Consequently $C_k$ has nonempty interior in $\mathbb R^k$. Its inclusion in $K$ implies that the columns of $\Pi^*$ span $\mathbb R^k$. Therefore $\operatorname{rank}\Pi^*=k$, $\operatorname{rank}P=k$, and $\operatorname{range}P=\operatorname{range}T$.

Since $P=\bar T\Pi$, its range is contained in the span of the $k$ columns of $\bar T$. That span must have dimension $k$ and equal the range of $T$. Hence there is an invertible matrix $S$ such that $\bar T=TS$. Substitution and injectivity of $T$ give $S\Pi=\Pi^*$, or $\Pi=S^{-1}\Pi^*$.

Linearity and injectivity of $\Phi$ also imply, as equalities of finite signed measures,
\[
\bar t_a^o=\sum_{b=1}^k S_{ba}t_b^o.
\]
Taking total mass gives $1=\sum_b S_{ba}$ for each $a$. Thus $\mathbf1^TS=\mathbf1^T$. For $A=S^{-1}$, multiplication on the right by $A$ gives $\mathbf1^TA=\mathbf1^T$, equivalently $A^T\mathbf1=\mathbf1$.

Let $r_i^T$ be row $i$ of $A$. Since $A\Pi^*=\Pi\ge0$, each $r_i$ belongs to $K^*$, and therefore has nonnegative inner product with every vector of $C_k$.

Here is the cone norm inequality directly from the displayed definition. Write $u=\mathbf1/\sqrt{k}$ and decompose $r_i=s u+w$ with $w\perp u$. Since $u\in C_k$, we have $s\ge0$. If $w\ne0$, the vector
\[
x=u-\frac{w}{\sqrt{k-1}\|w\|_2}
\]
belongs to $C_k$: its coordinate sum is $\sqrt{k}$ and its norm is $\sqrt{k/(k-1)}$. Hence
\[
0\le r_i^Tx=s-\frac{\|w\|_2}{\sqrt{k-1}}.
\]
For $w=0$ the same resulting inequality $\|w\|_2\le\sqrt{k-1}s$ is immediate. Thus
\[
\|r_i\|_2^2=s^2+\|w\|_2^2\le k s^2=(\mathbf1^Tr_i)^2,
\]
so $\|r_i\|_2\le\mathbf1^Tr_i$ and $r_i\in C_k^*$.

Hadamard's inequality bounds the absolute determinant by the product of row norms. Applying it and then AM--GM to the positive row sums yields
\[
|\det A|\le\prod_i\|r_i\|_2
\le\prod_i(\mathbf1^Tr_i)
\le\left(\frac{\sum_i\mathbf1^Tr_i}{k}\right)^k=1.
\]
The row sums are positive because $A$ is invertible and $\mathbf1^Tr_i\ge\|r_i\|_2>0$. Their total is $\mathbf1^TA\mathbf1=k$.

If $|\det A|=1$, equality holds throughout. Equality in AM--GM makes every row sum one, and equality in the product of the positive norm bounds gives $\|r_i\|_2=\mathbf1^Tr_i$ for every $i$. Such a row is on $\operatorname{bd}(C_k^*)$. Indeed, it is nonzero, belongs to this closed cone, and subtracting $\varepsilon\mathbf1$ gives
\[
\mathbf1^T(r_i-\varepsilon\mathbf1)-\|r_i-\varepsilon\mathbf1\|_2
\le-\varepsilon(k-\sqrt{k})<0,
\]
so points outside the cone approach it. The scattering boundary condition now implies $r_i=\lambda_i e_{j_i}$ with $\lambda_i\ge0$. Its row sum is one, so $\lambda_i=1$. Invertibility makes the indices $j_i$ distinct. Hence $A$ is a permutation matrix. Conversely, every permutation matrix satisfies these constraints and has determinant of absolute value one. We have proved $|\det S|\ge1$, with equality exactly when $S$ is a permutation matrix.

The Gram matrices satisfy
\[
G_\Phi(\bar t_1^o,\ldots,\bar t_k^o)=S^T G_\Phi(t_1^o,\ldots,t_k^o)S,
\]
and therefore
\[
\det G_\Phi(\bar t_1^o,\ldots,\bar t_k^o)
=(\det S)^2\det G_\Phi(t_1^o,\ldots,t_k^o).
\]
The true factorization is feasible. Every feasible candidate has objective at least the positive true value, while a minimizer has objective at most that value. Thus a minimizer has $|\det S|=1$, so $S$ is a permutation matrix, denoted $\Sigma(o)$. Injectivity of $\Phi$ and $\Pi=S^{-1}\Pi^*$ give
\[
\bar t_a^o=t_{\Sigma(o)(a)}^o,\qquad
\Pi(o)=\Sigma(o)^T\Pi^*(o).
\]
Pairwise distinctness makes this permutation unique at each observation.

To align the permutations, fix $o_0\in\mathcal O$, put $\Sigma_0=\Sigma(o_0)$, and write $\phi_a(o)=\Phi(\bar t_a^o)$ and $\phi_a^*(o)=\Phi(t_a^o)$. Since $k\ge2$ and the true components are distinct, injectivity gives
\[
\delta=\min_{i\ne j}\|\phi_i^*(o_0)-\phi_j^*(o_0)\|_{\mathcal H}>0.
\]
By continuity and finiteness of the component families, there is a neighborhood $U$ of $o_0$ in which every true and recovered component moves by less than $\delta/4$ from its value at $o_0$. For $o\in U$ and $b\ne\Sigma_0(a)$, the triangle inequality gives
\[
\|\phi_a(o)-\phi_b^*(o)\|_{\mathcal H}
\ge\|\phi_{\Sigma_0(a)}^*(o_0)-\phi_b^*(o_0)\|_{\mathcal H}
-\|\phi_a(o)-\phi_a(o_0)\|_{\mathcal H}
-\|\phi_b^*(o)-\phi_b^*(o_0)\|_{\mathcal H}
>\delta/2.
\]
But pointwise identification says $\phi_a(o)=\phi_{\Sigma(o)(a)}^*(o)$. Consequently $\Sigma(o)(a)=\Sigma_0(a)$ for every $a$, so $\Sigma(o)=\Sigma_0$ on $U$.

Thus the permutation map is locally constant. Each of its fibers is open, and its complement, being a union of other fibers, is open as well. A nonempty connected space cannot have two nonempty disjoint open fibers, so the map is constant. Denote its value by $\Sigma$.

Finally, choose any $o\in\mathcal S$ if a nonempty anchor is present. Agreement with the true labeling gives $t_{\Sigma(a)}^o=t_a^o$ for every $a$. Pairwise distinctness forces $\Sigma(a)=a$ for every $a$. Hence $\Sigma=I_k$, and the transition and policy equalities hold exactly everywhere.
