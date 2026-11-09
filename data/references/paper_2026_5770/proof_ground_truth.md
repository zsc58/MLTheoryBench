# Reference Proof

## Obligations and conventions

The proof must establish: (i) the finite-feature interpretations of the sequential limits; (ii) shallow independence for both activation classes, including several distinct monomial marks at one location; (iii) propagation of joint jet nondegeneracy, including zeroth-order marks; (iv) covariance positivity for the stated general operators; and (v) a positive-semidefinite tangent remainder. All five obligations are derived below.

Write \(a_{i,\alpha}=a_{i,\alpha}(x_i)\), and write \(a_{i,0}=A_i1\). Coefficients are evaluated at their locations and are not differentiated. The trainable parameters are the unscaled entries of every weight matrix and bias vector; \(\gamma\) is fixed.

The standard probabilistic inputs used here are the finite-dimensional CLT for i.i.d. centered vectors with finite second moments and the LLN for i.i.d. integrable vectors. Gaussian vectors have finite moments of every order. A Gaussian vector with positive-definite covariance has an everywhere positive density, so a continuous function of it that vanishes almost surely vanishes everywhere. The algebraic inputs are the product rule
\[
\partial^\alpha(fg)=\sum_{\xi\leq\alpha}\binom\alpha\xi\partial^\xi f\,\partial^{\alpha-\xi}g
\]
and the multivariate chain rule in partition form, described explicitly next.

## 1. Finite jets and the limiting kernels

At each location include the value coordinate \(t_i\) and every positive-order jet coordinate \(z_{i,\beta}\), \(1\leq|\beta|\leq m\). For a multi-index \(\alpha\ne0\), label its \(|\alpha|\) differentiations individually, and let \(\Pi_\alpha\) be the partitions of these labels. Each block has a multi-index \(\beta(B)\) recording its coordinate multiplicities. Define
\[
F_{i,0}(t,z)=\sigma(t_i),\qquad
F_{i,\alpha}(t,z)=\sum_{\pi\in\Pi_\alpha}\sigma^{(|\pi|)}(t_i)\prod_{B\in\pi}z_{i,\beta(B)}.
\]
Thus the feature for \(A_i\) is \(\Phi_i=\sum_\alpha a_{i,\alpha}F_{i,\alpha}\). This is exactly the multivariate chain rule applied to \(A_i\sigma(h(x_i))\). Every feature has polynomial magnitude growth in the finite jet vector. Consequently its products are integrable for every Gaussian jet law. The analogous formulas for \(\partial^\xi\sigma'(h(x_i))\) use activation derivatives only through order \(m+1\), so their products are integrable as well.

At depth one the jets are linear functions of independent Gaussian weights and biases. For general marks their covariance is
\[
\Sigma_1(i,j)=\sum_{k=1}^d(a_{i,0}x_{i,k}+a_{i,e_k})(a_{j,0}x_{j,k}+a_{j,e_k})+\gamma^2a_{i,0}a_{j,0},
\]
where absent coefficients are zero. The same direct gradient calculation gives \(\Theta^{(1)}_{\mu\nu}(i,j)=\delta_{\mu\nu}\Sigma_1(i,j)\).

For the output induction, hold the next width \(n_\ell\) fixed while taking all preceding widths sequentially. Joint convergence is applied to the finite collection containing all needed marks and all \(n_\ell\) hidden coordinates. The limiting hidden-coordinate jet vectors are independent copies \(Z_r\) of a centered Gaussian vector with covariance \(\Sigma_\ell\). The next output vector becomes
\[
\frac1{\sqrt{n_\ell}}\sum_{r=1}^{n_\ell}W^{(\ell+1)}_{\mu r}\Phi(Z_r)+\gamma b^{(\ell+1)}_\mu a_0.
\]
The summands are i.i.d., centered, and have finite second moments. The multivariate CLT, followed by addition of the independent Gaussian bias, gives
\[
\Sigma_{\ell+1}(i,j)=\mathbb E[\Phi_i(Z)\Phi_j(Z)]+\gamma^2a_{i,0}a_{j,0}. \tag{1}
\]
Applying the same CLT jointly to finitely many output coordinates gives zero cross-covariances between different outputs, because the corresponding outer weights have zero covariance. The joint limit is Gaussian, so these output jet vectors are independent. This proves the induction on the stated sequential limit, without interchanging width limits or differentiating an unspecified sample-path limit.

Here the feature maps through order \(m\) are continuous for both permitted activation classes. For the tangent calculation their highest derivatives may be discontinuous at zero for RePU. Every preactivation value has variance at least \(\gamma^2>0\), including conditionally at finite width because of its independent bias. Thus these exceptional values have probability zero. The transformations used in the limiting argument are continuous almost surely. Parameter derivatives at the fixed marked locations also exist almost surely. No derivative convention on the exceptional event affects a kernel entry.

For completeness, split the tangent kernel into the current-layer and earlier-layer parameter blocks. The current-layer block is the empirical version of (1), and its sequential limit is \(\delta_{\mu\nu}\Sigma_{\ell+1}\). Put
\[
D_{i,\xi}(Z)=\partial^\xi\sigma'(h(x_i)),
\]
interpreted by the same partition formula on the Gaussian jet \(Z\). For fixed \(n_\ell\), the earlier-layer block expands exactly as
\[
\frac1{n_\ell}\sum_{r,s}W^{(\ell+1)}_{\mu r}W^{(\ell+1)}_{\nu s}
\sum_{\alpha,\beta}\sum_{\xi\leq\alpha,\zeta\leq\beta}
a_{i,\alpha}a_{j,\beta}\binom\alpha\xi\binom\beta\zeta
D_{i,\xi}(Z_r)D_{j,\zeta}(Z_s)
\Theta^{(\ell)}_{rs}(x_i^{\partial^{\alpha-\xi}},x_j^{\partial^{\beta-\zeta}}).
\]
In this display the jets before taking the inner limits are the finite-width jets. The lower-layer tangent induction converges jointly on this finite list to its deterministic diagonal output-coordinate limit. Joint convergence with the jets follows because convergence in probability to a constant can be combined with convergence in distribution of a finite random vector. Thus, only after the preceding limits, the terms with \(r\ne s\) vanish. Different hidden coordinates do share lower-layer parameters at finite width; parameter disjointness is not used.

The remaining average is over independent copies of the hidden Gaussian jets and outer weights. Its terms are integrable by the moment bounds already checked. The LLN therefore gives the scalar recursion
\[
\Theta_{\ell+1}(i,j)=\Sigma_{\ell+1}(i,j)+
\sum_{\alpha,\beta}\sum_{\xi\leq\alpha,\zeta\leq\beta}
a_{i,\alpha}a_{j,\beta}\binom\alpha\xi\binom\beta\zeta
\mathbb E[D_{i,\xi}(Z)D_{j,\zeta}(Z)]
\Theta_\ell(x_i^{\partial^{\alpha-\xi}},x_j^{\partial^{\beta-\zeta}}). \tag{2}
\]
The output-coordinate factor is \(\delta_{\mu\nu}\). This also verifies the deterministic probability limit on every fixed pair. These derivations apply to arbitrary finite lists of admissible marks, not merely the distinct-location lists in the final claim.

## 2. Shallow Gram reduction

Let \(U\sim N(0,I_d)\) and \(V\sim N(0,1)\) be independent and set
\[
\phi_i(U,V)=A_i\sigma(U^\top x_i+\gamma V).
\]
Then
\[
\Sigma_2=\mathbb E[\phi\phi^\top]+\gamma^2a_0a_0^\top. \tag{3}
\]
Direct differentiation of the four parameter blocks also gives
\[
\Theta_2=\Sigma_2+\sum_{k=1}^d\mathbb E[\psi_k\psi_k^\top]+\mathbb E[\eta\eta^\top], \tag{4}
\]
where
\[
\psi_{i,k}=\left.A_i\big[z_k\sigma'(U^\top z+\gamma V)\big]\right|_{z=x_i},\qquad
\eta_i=\gamma A_i\sigma'(U^\top x_i+\gamma V).
\]
The second-layer weight squares have expectation one, which accounts for their absence in (4). All terms are integrable by the growth condition through \(m+1\).

A zero covariance quadratic form forces the corresponding feature sum to vanish almost surely. The features in (3) are continuous, including for \(q\ge m+1\), and \((U,\gamma V)\) has full support. Consequently the identity holds for every \((u,b)\in\mathbb R^d\times\mathbb R\).

We prove the stronger statement that, for distinct locations and any finite real coefficient array,
\[
\sum_i\sum_{|\alpha|\le m}b_{i,\alpha}u^\alpha\sigma^{(|\alpha|)}(b+u^\top x_i)\equiv0
\quad\Longrightarrow\quad b_{i,\alpha}=0\text{ for all }i,\alpha. \tag{5}
\]
This covers both the original operator features and several monomial marks at the same location.

## 3. Smooth non-polynomial activations

A standard expression at a location is a nonempty sum
\[
P_i(b,u)=\sum_\alpha p_{i,\alpha}\sigma^{(|\alpha|+s_i)}(b+u^\top x_i)u^\alpha,
\]
with distinct monomials, nonzero coefficients, and nonnegative displayed derivative orders. The offset \(s_i\) is fixed within the expression. The expressions in (5), after discarding empty groups, have offset zero.

For one location, put \(t=b+u^\top x_i\). Since \((b,u)\mapsto(t,u)\) is invertible, an identity \(P_i=0\) gives a polynomial identity in \(u\) for every fixed \(t\). Comparing coefficients yields \(p_{i,\alpha}\sigma^{(|\alpha|+s_i)}(t)=0\) for every \(t\). Any surviving coefficient therefore forces a derivative of \(\sigma\) to vanish identically, making \(\sigma\) a polynomial, a contradiction.

For the induction on the number of locations, replace \(b\) by \(t-u^\top x_N\), leaving \(u\) unchanged. The last expression becomes polynomial in \(u\), with coefficients depending only on \(t\). Choose \(j\) such that \((x_1-x_N)_j\ne0\), and differentiate with respect to \(u_j\) more times than the largest \(u_j\)-degree in the last expression. That expression is annihilated.

Every derivative of another expression is orderly: a chain-rule term increases the activation derivative order by one, whereas a monomial derivative decreases its degree by one, so both increase the offset by one. If the transformed location has nonzero \(j\)-coordinate, a monomial of maximal \(u_j\)-degree contributes a nonzero chain-rule term of that same degree. No monomial-derivative term can cancel it. Thus the differentiated first expression remains nonempty. If a transformed location has zero \(j\)-coordinate, ordinary monomial differentiation either gives an orderly nonempty expression or annihilates it. After discarding annihilated groups, one obtains a nonempty identity on fewer distinct locations. Induction reaches the impossible one-location case. This proves (5) for smooth non-polynomial \(\sigma\).

## 4. Biased RePU activations

Let \(\sigma(t)=t_+^q\), with integer \(q\ge m+1\). Suppose (5) holds with a nonempty coefficient group at location \(i\), and let
\[
r=\max\{|\alpha|:b_{i,\alpha}\ne0\},\qquad
H_i(u)=\sum_{|\alpha|=r}b_{i,\alpha}u^\alpha.
\]
The polynomial \(H_i\) is nonzero. Choose \(u\) such that \(H_i(u)\ne0\) and \(u^\top(x_j-x_i)\ne0\) for every other location \(j\). Such a choice exists: the latter exclusions are finitely many proper hyperplanes, and a nonzero polynomial cannot vanish on a nonempty open set.

For this fixed \(u\), consider the identity as a function of \(b\) near \(b_0=-u^\top x_i\). Every other location's contribution is smooth near \(b_0\). At location \(i\), a term of order \(s\) is
\[
b_{i,\alpha}u^\alpha\frac{q!}{(q-s)!}(b-b_0)_+^{q-s},\qquad s=|\alpha|.
\]
The jump between the one-sided derivatives of order \(q-r\) of the entire identity is therefore exactly \(q!H_i(u)\): lower-order operator terms have zero jump at this derivative order. This contradicts the zero identity. Thus no nonempty coefficient group exists, proving (5).

Geometrically this is the source's extended-hyperplane argument, with hyperplane \(b+u^\top x_i=0\). Its free \(u\)-parametrization is essential. No claim that a general polynomial vanishing on a hyperplane vanishes in the ambient space is used. Since these functions are piecewise polynomial, their one-sided derivatives give the jumps directly, without requiring an additional differentiation theorem.

By (3)-(5), both shallow kernels are positive definite for the stated general marks. More strongly, for any finite collection of distinct locations and distinct monomial marks at each location, the Gaussian vector of shallow marked outputs has positive-definite covariance. Denote this property by LI.

## 5. Propagation of LI, including value marks

Assume LI at depth \(\ell\ge2\). Enlarge a proposed finite monomial-mark collection to contain the value mark and every derivative mark through order \(m\) at its locations. Its depth-\(\ell\) Gaussian jet vector \((t,z)\) has positive-definite covariance and full support.

If a next-layer monomial covariance form vanished, (1) would imply
\[
\sum_i\sum_{|\alpha|\le m}b_{i,\alpha}F_{i,\alpha}(t,z)=0 \tag{6}
\]
almost surely, with missing marks given coefficient zero. The feature functions are continuous for both permitted activation classes, so (6) holds for all \((t,z)\).

Fix \(t\) and regard (6) as a polynomial in the positive-order jet coordinates \(z\). For every \(\alpha\ne0\), the coefficient of the linear monomial \(z_{i,\alpha}\) is exactly
\[
b_{i,\alpha}\sigma'(t_i).
\]
Indeed, it comes from the one-block partition for \(\alpha\); partitions with at least two blocks have polynomial degree at least two, and a one-block partition for any different multi-index gives a different jet coordinate. Since \(\sigma'\) is not identically zero for either permitted activation, every positive-order coefficient \(b_{i,\alpha}\) vanishes.

The remaining identity is
\[
\sum_i b_{i,0}\sigma(t_i)=0\qquad\text{for all }(t_1,\ldots,t_N).
\]
Choose \(s,t\) with \(\sigma(s)\ne\sigma(t)\), and subtract two evaluations differing only in coordinate \(i\). This gives \(b_{i,0}(\sigma(s)-\sigma(t))=0\), hence \(b_{i,0}=0\).

This step does not set other locations to zero and discard their value features. Such a substitution would leave constants proportional to \(\sigma(0)\), which need not vanish. It also does not assume independence of the jet coordinates: joint full support suffices.

Thus every next-layer covariance form has trivial null space. LI propagates from depth two to every depth.

## 6. General operator covariance positivity

At a fixed depth, expand each marked output as
\[
A_i h(x_i)=\sum_{|\alpha|\le m}a_{i,\alpha}\partial^\alpha h(x_i).
\]
For a vector \(c\ne0\), choose \(i\) with \(c_i\ne0\). At least one \(a_{i,\alpha}\ne0\), so the expanded jet coefficient array \(b_{i,\alpha}=c_i a_{i,\alpha}\) is nonzero. Different locations occupy distinct coordinates in this array. LI therefore gives strictly positive variance of this linear combination. Hence \(c^\top\Sigma_L(X)c>0\) for every \(L\ge2\).

## 7. Tangent remainder and conclusion

We explicitly close the positivity step in (2), including the independence needed when multiplying expectations. Inductively represent the preceding tangent kernel as a finite sum
\[
\Theta_\ell(x^A,y^B)=\sum_{r\in J_\ell}\mathbb E[H_r(x^A)H_r(y^B)]. \tag{7}
\]
At depth one take the deterministic features
\[
H_k(x^A)=a_0(x)x_k+a_{e_k}(x)\quad(1\le k\le d),\qquad H_0(x^A)=\gamma a_0(x).
\]
For the induction step, take the Gaussian jet vector \(Z\) used in the differentiated activation factor independently of all random variables realizing the features in (7). Define
\[
G_r(x_i^{A_i})=\sum_\alpha a_{i,\alpha}\sum_{\xi\le\alpha}\binom\alpha\xi D_{i,\xi}(Z)H_r(x_i^{\partial^{\alpha-\xi}}).
\]
Expansion, independence, and (7) show that the remainder in (2) equals
\[
R_{\ell+1}(i,j)=\sum_{r\in J_\ell}\mathbb E[G_r(x_i^{A_i})G_r(x_j^{A_j})]. \tag{8}
\]
All these expectations are finite: the differentiated activation features have finite second moments, the preceding features have finite second moments by induction, and the two families are independent. The covariance term (1) supplies two additional features, \(\Phi_i(Z)\) and \(\gamma a_{i,0}\), so (7) also holds at the next depth with finitely many features.

Consequently
\[
c^\top R_L(X)c=\sum_r\mathbb E\left[\left(\sum_i c_iG_r(x_i^{A_i})\right)^2\right]\ge0.
\]
Combining (8) with the covariance result gives
\[
\Theta_L(X)=\Sigma_L(X)+R_L(X)\succ0\qquad(L\ge2).
\]
The argument includes \(m=0\), the boundary RePU degree \(q=m+1\), zero input locations, and arbitrary nonzero evaluated coefficient rows. An empty marked collection has no nonzero coefficient vector and satisfies the quadratic-form formulation vacuously. All five proof obligations listed at the start are closed.
