# Reference Proof

## Proof Structure

1. Rewrite the leave-one-out estimator as a symmetric order-two U-statistic and establish unbiasedness.
2. Compute its centered first projection and identify the first-order component with the centered oracle estimator.
3. Derive degeneracy and orthogonality directly, count the surviving variance terms, and bound the second-order remainder.
4. Compute the oracle MSE and compare all deterministic prompt-only baselines using conditional uncorrelation.

## Complete Proof

Fix \(x,\theta\). All expectations and covariances below are under the fixed-prompt law. Write \(U_i=(Y_i,Z_i)\), \(S_i=S(Y_i)\), and \(V=\mathbb E Z\). The observations are iid, \(\mathbb E S=0\), and \(g=\mathbb E[SZ]\). Bounded rewards and the finite score second moment ensure that every random vector used below is square-integrable. In particular, \(|V|\le M\).

### 1. Symmetrization and unbiasedness

For every integer \(G\ge2\),
\[
\widehat g_{\rm loo}
=\frac1{G(G-1)}\sum_{i\ne j}S_i(Z_i-Z_j)
=\frac1{2G(G-1)}\sum_{i\ne j}(S_i-S_j)(Z_i-Z_j).
\]
With
\[
h(U_i,U_j)=\tfrac12(S_i-S_j)(Z_i-Z_j),
\]
this is
\[
\widehat g_{\rm loo}
=\frac1{G(G-1)}\sum_{i\ne j}h(U_i,U_j)
=\binom G2^{-1}\sum_{i<j}h(U_i,U_j).
\]
The kernel is symmetric. Independence and \(\mathbb E S=0\) give
\[
\mathbb E h(U_1,U_2)
=\tfrac12\bigl(\mathbb E[S_1Z_1]+\mathbb E[S_2Z_2]
-\mathbb E[S_1Z_2]-\mathbb E[S_2Z_1]\bigr)=g.
\]
Thus the estimator is unbiased.

### 2. The correctly centered projection

Let \(U'\) be an independent copy and define
\[
q(u)=\mathbb E[h(u,U')],\qquad h_1(u)=q(u)-g.
\]
For \(u=(y,z)\), direct expansion gives
\[
q(y,z)=\tfrac12\bigl(S(y)z-S(y)V-z\mathbb E S+\mathbb E[SZ]\bigr)
=\tfrac12\bigl(S(y)(z-V)+g\bigr).
\]
Consequently,
\[
2h_1(Y,Z)=S(Y)(Z-V)-g,\qquad \mathbb E h_1(U)=0.
\]
Define
\[
h_2(u,v)=h(u,v)-g-h_1(u)-h_1(v).
\]
Conditioning on the first argument gives
\[
\mathbb E[h_2(U_1,U_2)\mid U_1]
=q(U_1)-g-h_1(U_1)-\mathbb E h_1(U_2)=0.
\]
Symmetry gives the same identity conditional on the second argument. Thus \(h_2\) is degenerate.

Each observation occurs in \(G-1\) unordered pairs, so the kernel identity yields
\[
\widehat g_{\rm loo}-g
=\frac2G\sum_{i=1}^G h_1(U_i)+R_G,
\qquad
R_G=\binom G2^{-1}\sum_{i<j}h_2(U_i,U_j).
\]
In particular,
\[
\frac2G\sum_i h_1(U_i)
=\frac1G\sum_i\bigl(S_i(Z_i-V)-g\bigr)
=\widehat g_{\rm or}-g.
\]

### 3. Orthogonality and the remainder bound

All the required orthogonality relations follow from independence and the conditional mean-zero identities just proved. Distinct first-order terms are independent and centered. For a first-order term and a second-order pair, disjoint indices give independence; if they share an index, conditioning on that observation makes the second-order factor have conditional mean zero. Two distinct unordered second-order pairs are independent when disjoint. If they share one observation, their remaining observations are conditionally independent given the shared observation, and both factors have conditional mean zero. In each case the expected inner product is zero.

It follows that
\[
\mathbb E\|\widehat g_{\rm loo}-g\|^2
=\frac4G\mathbb E\|h_1(U)\|^2+\mathbb E\|R_G\|^2
=\frac{\operatorname{tr}\Sigma_{\rm or}}G+\mathbb E\|R_G\|^2.
\]
There are \(\binom G2\) identical diagonal pair contributions and no nonzero off-diagonal contributions, giving
\[
\mathbb E\|R_G\|^2
=\binom G2^{-1}\mathbb E\|h_2(U_1,U_2)\|^2
=\frac2{G(G-1)}\mathbb E\|h_2(U_1,U_2)\|^2.
\]
The same conditional-centering argument makes the four components in
\[
h(U_1,U_2)=g+h_1(U_1)+h_1(U_2)+h_2(U_1,U_2)
\]
orthogonal in square-integrable vector space. Therefore
\[
\mathbb E\|h(U_1,U_2)\|^2
=\|g\|^2+2\mathbb E\|h_1(U)\|^2+\mathbb E\|h_2(U_1,U_2)\|^2,
\]
and in particular \(\mathbb E\|h_2\|^2\le\mathbb E\|h\|^2\). Since \(|Z_1-Z_2|\le2M\),
\[
\mathbb E\|h(U_1,U_2)\|^2
\le M^2\mathbb E\|S_1-S_2\|^2
=2M^2\mathbb E\|S\|^2,
\]
where the last equality uses independence and \(\mathbb E S=0\). Hence, for every \(G\ge2\),
\[
0\le\mathbb E\|R_G\|^2
\le\frac{4M^2\mathbb E\|S\|^2}{G(G-1)}
\le\frac{8M^2\mathbb E\|S\|^2}{G^2}.
\]
This proves
\[
\mathbb E\|\widehat g_{\rm loo}-g\|^2
=\frac{\operatorname{tr}\Sigma_{\rm or}}G
+O\!\left(\frac{\mathbb E\|S\|^2}{G^2}\right)
\]
with a constant depending only on \(M\).

### 4. Oracle equivalence and baseline comparison

The oracle summands \(A_i=S_i(Z_i-V)\) are iid with mean \(g\) and covariance \(\Sigma_{\rm or}\). Thus
\[
\operatorname{MSE}(\widehat g_{\rm or}\mid x)
=\frac{\operatorname{tr}\Sigma_{\rm or}}G,
\qquad
\lim_{G\to\infty}G\operatorname{MSE}(\widehat g_{\rm loo}\mid x)
=\operatorname{tr}\Sigma_{\rm or}.
\]
These statements remain valid when \(\Sigma_{\rm or}=0\); no ratio of MSEs is asserted.

Now fix a deterministic real baseline \(b=b(x)\), and put \(D=V-b\). The summand \(T_b=S(Z-b)=A+DS\) has mean \(g\), so \(\widehat g_b\) is unbiased and
\[
G\operatorname{MSE}(\widehat g_b\mid x)
=\mathbb E\|T_b-g\|^2.
\]
Expanding,
\[
\mathbb E\|T_b-g\|^2
=\mathbb E\|A-g\|^2
+2D\mathbb E\langle A-g,S\rangle
+D^2\mathbb E\|S\|^2.
\]
Here
\[
\mathbb E\langle A-g,S\rangle
=\mathbb E[\|S\|^2(Z-V)]-\langle g,\mathbb E S\rangle
=0,
\]
because the score has mean zero and conditional uncorrelation gives
\(\mathbb E[\|S\|^2Z\mid x]=V\mathbb E[\|S\|^2\mid x]\). It follows that
\[
\operatorname{MSE}(\widehat g_b\mid x)
=\frac1G\left(\operatorname{tr}\Sigma_{\rm or}
+\mathbb E[\|S(Y)\|^2(V-b(x))^2\mid x]\right).
\]
The second term in parentheses is nonnegative. Therefore the leave-one-out estimator has a leading MSE coefficient no larger than that of every such baseline estimator. For \(b=0\), the coefficient comparison is strict when
\(\mathbb E[\|S(Y)\|^2V^2\mid x]>0\). The remainder bound also implies actual strict MSE improvement for all sufficiently large \(G\) in that case, but not necessarily for every finite \(G\).

No step divides by the score second moment, reward variance, value, or oracle covariance. Thus zero and degenerate cases require no additional assumptions, and the finite-sample calculations include \(G=2\).

## Source-Repair and Obligation Notes

The source's raw first projection and the centered first projection used here are different: \(q=[S(Z-V)+g]/2\), whereas \(h_1=q-g\). The mean subtraction is essential even though subtracting a constant leaves covariance unchanged. The source's baseline second-moment expansion must also retain cross-observation means, or equivalently start directly from the variance of a single summand as above. All theorem-critical obligations have been derived explicitly; none is discharged solely by citing a specialized method or an external paper. The source's separate minibatch strictness sentence is not used in this fixed-prompt theorem.
