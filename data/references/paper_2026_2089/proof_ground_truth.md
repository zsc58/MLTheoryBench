# Reference Proof

## Proof Structure

1. Verify finiteness and identify the specified conditional version.
2. Split the value function into regional contributions and use linearity of the finite Shapley sum.
3. Compute the full affine regional value by coordinate independence and derive its marginal contribution.
4. Explain the contribution of other regions for a feature outside both relevant sets.
5. Verify a nonzero total attribution in a valid closed-rectangle example.

## Complete Proof

Write \(H_{i,k}={\bf1}\{x_i\in I_{i,k}\}\), and define
\[
q_{i,k}=\Pr(X_i\in I_{i,k}),\qquad
 t_{i,k}=\mathbb E[X_i{\bf1}\{X_i\in I_{i,k}\}].
\]
All \(q_{i,k}\) are positive, and \(|t_{i,k}|\leq\mathbb E|X_i|<\infty\). Empty products below equal one and empty sums equal zero.

### Finiteness and conditional versions

For any fixed \(x\) and coalition \(S\), each regional integrand at \((x_S,X_{-S})\) is bounded in absolute value by
\[
|b_k|+\sum_{i\in S}|a_{i,k}||x_i|+
\sum_{i\notin S}|a_{i,k}||X_i|.
\]
This bound is integrable. There are finitely many regions, so every value and marginal contribution is finite. The interval indicators and affine functions are measurable.

For an integrable regional function \(h_k(z)=g_k(z){\bf1}_{A_k}(z)\), independence implies that \(x_S\mapsto\mathbb E[h_k(x_S,X_{-S})]\) is a version of \(\mathbb E[h_k(X)\mid X_S]\). Indeed, multiplying by any bounded measurable function of \(X_S\) and integrating gives the defining conditional-expectation identity by product integration. The problem specifies this version also at null conditioning events. Consequently,
\[
V_k(S;x)=\mathbb E[g_k(x_S,X_{-S}){\bf1}_{A_k}(x_S,X_{-S})].
\]
The same argument applies to \(f\).

### Regional decomposition

The defining finite sum for \(f\) gives
\[
v(S;x)=\sum_{k=1}^m V_k(S;x).
\]
Therefore, interchanging two finite sums,
\[
\phi_{x_l}=\sum_{k=1}^m\phi^k_{x_l},\qquad
\phi^k_{x_l}=\sum_{S\subseteq D\setminus\{l\}}
\frac{V_k(S\cup\{l\};x)-V_k(S;x)}{p\binom{p-1}{|S|}}.
\]
This proves the asserted regional decomposition directly from the definition.

### Independence-based regional formula

Set
\[
\eta_{j,k}^S(x)=\begin{cases}H_{j,k},&j\in S,\\q_{j,k},&j\notin S,\end{cases}
\qquad
\mu_{i,k}^S(x)=\begin{cases}x_iH_{i,k},&i\in S,\\t_{i,k},&i\notin S.\end{cases}
\]
Expand the affine function, and factor each expectation over distinct independent coordinates. This gives
\[
V_k(S;x)=b_k\prod_j\eta_{j,k}^S(x)
+\sum_i a_{i,k}\mu_{i,k}^S(x)\prod_{j\ne i}\eta_{j,k}^S(x).
\]
In particular, the intercept is retained. An equivalent form, using the positive probabilities, is
\[
V_k(S;x)=
\left(\prod_{i\in S}H_{i,k}\right)
\left(\prod_{j\notin S}q_{j,k}\right)
\left[b_k+\sum_{i\in S}a_{i,k}x_i+
\sum_{j\notin S}a_{j,k}\frac{t_{j,k}}{q_{j,k}}\right].
\]
These formulas hold for the empty and full coalitions as well, including when an observed coordinate falls outside a particular region.

For completeness, let \(l\notin S\) and put
\[
P_{k,S,l}=\prod_{i\in S\cup\{l\}}H_{i,k}
\prod_{j\in D\setminus(S\cup\{l\})}q_{j,k}.
\]
Multiplying the formula for \(V_k(S;x)\) by \(H_{l,k}/q_{l,k}\) changes its prefactor to \(P_{k,S,l}\). In the bracket, passing to \(S\cup\{l\}\) replaces only \(a_{l,k}t_{l,k}/q_{l,k}\) by \(a_{l,k}x_l\). Thus
\[
V_k(S\cup\{l\};x)=\frac{H_{l,k}}{q_{l,k}}V_k(S;x)
+a_{l,k}\left(x_l-\frac{t_{l,k}}{q_{l,k}}\right)P_{k,S,l},
\]
and hence
\[
V_k(S\cup\{l\};x)-V_k(S;x)
=\left(\frac{H_{l,k}}{q_{l,k}}-1\right)V_k(S;x)
+a_{l,k}\left(x_l-\frac{t_{l,k}}{q_{l,k}}\right)P_{k,S,l}.
\]
The second probability product excludes \(l\). Weighted summation gives the corresponding explicit regional Shapley formula. This factorized marginal identity is useful for checking the source, but the public task also admits a proof using the explicit regional-value formula and direct subtraction.

### Cross-region mechanism

If \(l\notin G\), then \(I_{l,k}=\mathbb R\) for every \(k\), so \(H_{l,k}=q_{l,k}=1\) and \(t_{l,k}=\mathbb E[X_l]\). The regional marginal becomes
\[
a_{l,k}(x_l-\mathbb E[X_l])
\prod_{i\in S}H_{i,k}
\prod_{j\in D\setminus(S\cup\{l\})}q_{j,k}.
\]
If also \(l\notin J_{k^*}\), this expression is zero for the active region \(k^*\). It need not be zero for another region with \(a_{l,k}\ne0\). The condition \(l\notin G\) excludes region-boundary dependence, not affine dependence in other regions. Nonzero regional terms alone would not rule out cancellation, so we verify the total in a concrete example.

### A valid nonzero witness

Take \(p=2\). Let \(X_1\) have the equal mixture of the uniform distributions on \([-1,-1/4]\) and \([1/4,1]\), and let independent \(X_2\sim\mathrm{Unif}[0,1]\). Define
\[
A_1=(-\infty,-1/4]\times\mathbb R,\qquad
A_2=[1/4,\infty)\times\mathbb R,
\qquad \mathcal X=A_1\cup A_2.
\]
These are disjoint closed hyperrectangles under the allowed infinite-endpoint convention, and they partition \(\mathcal X\), not all of \(\mathbb R^2\). The input lies in \(\mathcal X\) almost surely. The coordinate-region probabilities are \(q_{1,1}=q_{1,2}=1/2\) and \(q_{2,1}=q_{2,2}=1\), and both coordinates have finite first moments.

Set \(g_1=0\), \(g_2(z)=z_2\), and let \(f\) be the displayed regional sum, also outside \(\mathcal X\). At \(x=(-1/2,3/4)\in A_1\), we have \(J_1=\varnothing\) and \(G=\{1\}\). Independence gives
\[
v(\varnothing;x)=\tfrac12\mathbb E[X_2]=\tfrac14,
\qquad v(\{2\};x)=\tfrac12\cdot\tfrac34=\tfrac38,
\]
whereas fixing the first coordinate to \(-1/2\) yields
\[
v(\{1\};x)=v(\{1,2\};x)=0.
\]
For two features both Shapley weights are \(1/2\), and therefore
\[
\phi_{x_2}=\tfrac12(\tfrac38-\tfrac14)+\tfrac12(0-0)=\tfrac1{16}\ne0.
\]
Thus feature \(2\) lies outside both \(J_1\) and \(G\) and nevertheless has nonzero total attribution.

## Private Source Audit Notes

The source's main-text regional formula uses the correct probability product. The appendix restatement and final marginal displays incorrectly retain an additional \(q_{l,k}\); the preceding appendix identity and the direct derivation above uniquely fix the error. The source also sets all regional intercepts to zero without establishing the affine extension. The proof above retains them throughout. These local source repairs do not change the target or its hypotheses. All theorem-critical obligations are explicitly closed; no specialized external result is assumed.
