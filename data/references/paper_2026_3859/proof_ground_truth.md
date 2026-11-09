# Reference Proof

## Proof obligations

The proof must establish: the affine product-form characterization; applicability of characteristic-kernel injectivity to signed mass-one measures; the uniform concentration bound with its numerical constant; isolated population low-loss regions; and preservation of their connectedness for the specifically defined empirical criterion. Uniform function approximation by itself is not a sufficient convexity argument. The finite-degree structure of the two criteria must be used or replaced by another valid argument derived from the stated setup.

## Step 001 — Affine and product-form geometry

For \(r\in A\), put \(\beta=\Theta^Tr\). Row stochasticity gives
\[
\mathbf1_m^T\beta=r^T\Theta\mathbf1_m=r^T\mathbf1_L=1,
\qquad
r^TU=\sum_i\beta_iq_i.
\]
If this signed density is product-form, the no-cancellation assumption forces \(\beta_j=0\) for all \(j\notin R_{12}\). If \(R_{12}\) is empty, this contradicts the sum constraint, so there is no product-form affine combination.

Suppose instead that \(R_{12}\) is nonempty. For a product-form affine combination supported on this set,
\[
\sum_{i\in R_{12}}\beta_i a_i\otimes b_i
=
\left(\sum_{i\in R_{12}}\beta_i a_i\right)
\otimes
\left(\sum_{j\in R_{12}}\beta_j b_j\right).
\]
The family \(\{a_i\otimes b_j:i,j\in R_{12}\}\) is linearly independent: applying the independence of the \(a_i\) to almost-everywhere sections of a vanishing linear combination, and then the independence of the \(b_j\), makes every coefficient zero. Comparing coefficients in the display therefore gives
\[
\beta_i\beta_j=0\quad(i\ne j),\qquad \beta_i^2=\beta_i.
\]
Together with \(\sum_i\beta_i=1\), these identities imply \(\beta=e_i\) for exactly one \(i\in R_{12}\). Conversely, \(\beta=e_i\) gives the product density \(q_i\).

Because \(L=m\), full column rank makes \(\Theta^T\) invertible. Hence the unique solution of \(\Theta^Tr=e_i\) is
\[
r_i=(\Theta^T)^{-1}e_i=\Theta(\Theta^T\Theta)^{-1}e_i.
\]
Moreover,
\[
\mathbf1_L^Tr_i=(\Theta\mathbf1_m)^Tr_i
=\mathbf1_m^T\Theta^Tr_i=1.
\]
All these vectors lie strictly inside the radius constraint by the specified choice of \(\bar r\), and different indices give different vectors. Uniqueness here uses the square assumption, not merely full column rank of a rectangular matrix.

## Step 002 — Signed embeddings and population zeros

Every affine combination considered has finite total variation and total mass one. Its marginal measures have finite total variation and mass one, and their product has the same properties. Boundedness of the feature map and the specified strong measurability ensure that the embeddings used in the proof exist. Finite empirical combinations also have well-defined embeddings.

Characteristic-kernel injectivity extends to the signed measures used here by a direct argument. If finite signed measures \(Q,Q'\) have the same total mass and \(\mu(Q)=\mu(Q')\), write the Jordan decomposition of \(\eta=Q-Q'\) as \(\eta=\eta^+-\eta^-\). The two positive parts have equal mass \(a\). If \(a=0\), then \(\eta=0\). If \(a>0\), equality of embeddings implies equality of the embeddings of the probability measures \(\eta^+/a\) and \(\eta^-/a\). Characteristicness makes those probability measures equal, and consequently \(\eta=0\). Their embeddings exist because their total variations are dominated by the finite variation measures already under consideration.

Apply this to \(Q=r^TU\) and \(Q'=\Pi(r^TU)\). They both have mass one. Thus \(d(r)=0\) if and only if \(r^TU\) is product-form. Step 001 proves
\[
\{r\in\Delta_{\bar r}:d(r)=0\}=\{r_i:i\in R_{12}\}.
\]

## Step 003 — Uniform concentration

Write \(Z_{lj}=(X_{lj},Y_{lj})\) and \(\psi(x,y)=k((x,y),\cdot)\), so \(\|\psi(x,y)\|_{\mathcal H}\leq K\). Define
\[
M_l=\mathbb E\psi(X_l,Y_l),\qquad
\widehat M_l=\frac1{n_l}\sum_j\psi(X_{lj},Y_{lj}),
\]
\[
V_{lh}=\mathbb E\psi(X_l,\widetilde Y_h),\qquad
\widehat V_{lh}=\frac1{n_ln_h}\sum_{j=1}^{n_l}\sum_{t=1}^{n_h}\psi(X_{lj},Y_{ht}),
\]
where the expectation defining \(V_{lh}\) uses independent random variables with the respective first and second marginal laws. In particular, \(V_{ll}\) uses independent marginal draws, whereas \(\widehat V_{ll}\) includes its diagonal terms.

Linearity of integration and the definition of the product of the empirical marginals give
\[
F(r)=\sum_lr_lM_l-\sum_{l,h}r_lr_hV_{lh},\qquad
\widehat F(r)=\sum_lr_l\widehat M_l-\sum_{l,h}r_lr_h\widehat V_{lh},
\]
with \(\operatorname{MMD}(r^TU)=\|F(r)\|\) and \(\widehat{\operatorname{MMD}}(\widehat U_r)=\|\widehat F(r)\|\). Hence
\[
\left|\|F(r)\|-\|\widehat F(r)\|\right|
\leq\sum_l|r_l|\|\widehat M_l-M_l\|
+\sum_{l,h}|r_lr_h|\|\widehat V_{lh}-V_{lh}\|.
\]

We use the following standard independent concentration results, in the forms needed here. For independent inputs and a measurable real function \(G\), if replacing input \(j\) changes \(G\) by at most \(b_j\), then
\[
\Pr\{G-\mathbb EG>t\}\leq
\exp\left(-\frac{2t^2}{\sum_jb_j^2}\right),\qquad t>0.
\]
For a square-integrable Hilbert-valued function \(W\) of independent inputs, with \(W^{(j)}\) obtained by replacing the \(j\)-th input by an independent copy,
\[
\mathbb E\|W-\mathbb EW\|^2
\leq\frac12\sum_j\mathbb E\|W-W^{(j)}\|^2.
\]
These are respectively the bounded-difference and Hilbert-space Efron–Stein inequalities. All their hypotheses hold below: the inputs are the independent observed pairs, the functions are measurable, and their Hilbert norms are bounded. Coordinates within a pair are not treated as independent inputs.

If \(K=0\), every feature vector is zero and the concentration conclusion is immediate. Assume \(K>0\) for the calculations below. For the ordinary embedding, independence gives
\[
\mathbb E\|\widehat M_l-M_l\|^2\leq K^2/n_l.
\]
Replacing one observed pair changes its norm error by at most \(2K/n_l\). Therefore, for every \(a>0\), except on an event of probability at most \(e^{-a}\),
\[
\|\widehat M_l-M_l\|
\leq\frac{K}{\sqrt{n_l}}+K\sqrt{\frac{2a}{n_l}}
\leq\frac{2K(1+\sqrt a)}{\sqrt{n_l}}.
\]

For \(l\ne h\), independence between the two samples gives \(\mathbb E\widehat V_{lh}=V_{lh}\). Replacement bounds are \(2K/n_l\) for an input from sample \(l\) and \(2K/n_h\) for an input from sample \(h\). Efron–Stein consequently yields
\[
\mathbb E\|\widehat V_{lh}-V_{lh}\|
\leq\sqrt2K\sqrt{n_l^{-1}+n_h^{-1}}.
\]
Applying bounded differences to the norm error adds at most
\(\sqrt{2a}K\sqrt{n_l^{-1}+n_h^{-1}}\), with failure probability at most \(e^{-a}\). In particular,
\[
\|\widehat V_{lh}-V_{lh}\|
\leq2K(1+\sqrt a)(n_l^{-1/2}+n_h^{-1/2})
\]
on that event.

For \(l=h\), distinguishing equal and unequal observation indices gives the exact expectation
\[
\mathbb E\widehat V_{ll}=
\left(1-\frac1{n_l}\right)V_{ll}+\frac1{n_l}M_l.
\]
Its bias relative to \(V_{ll}\) has norm at most \(2K/n_l\). Replacing one whole pair affects at most \(2n_l-1\) summands in the all-pairs average, so its Hilbert norm changes by at most \(4K/n_l\). Efron–Stein bounds the centered mean norm by \(2\sqrt2K/\sqrt{n_l}\), and bounded differences adds at most \(2\sqrt2K\sqrt{a/n_l}\). Thus, with failure probability at most \(e^{-a}\),
\[
\|\widehat V_{ll}-V_{ll}\|
\leq\frac{2K}{n_l}+
\frac{2\sqrt2K(1+\sqrt a)}{\sqrt{n_l}}
\leq\frac{8K(1+\sqrt a)}{\sqrt{n_l}}.
\]
This also covers \(n_l=1\). Both product-embedding cases therefore satisfy the common bound
\[
\|\widehat V_{lh}-V_{lh}\|
\leq4K(1+\sqrt a)(n_l^{-1/2}+n_h^{-1/2}).
\]

Set \(a=\log(2L^2/\delta)>0\). There are \(L+L^2\leq2L^2\) embedding bounds, so a union bound makes all of them simultaneous with probability at least \(1-\delta\). On this single event, for every \(r\in\Delta_{\bar r}\), the reverse-triangle estimate is at most
\[
K(1+\sqrt a)\left(2+8\|r\|_1\right)
\sum_l|r_l|n_l^{-1/2}.
\]
Each \(r_i\) has coordinate sum one, so \(\bar r>\max_i\|r_i\|_1\geq1\). Using
\(\sum_l|r_l|n_l^{-1/2}\leq\bar r N_{1/2}\), the last display is bounded by
\[
K(1+\sqrt a)(2\bar r+8\bar r^2)N_{1/2}
\leq10\bar r^2K(1+\sqrt a)N_{1/2}.
\]
Taking the supremum proves the requested probability bound. The supremum is measurable: the criterion is continuous in \(r\) on a compact finite-dimensional domain, so the same supremum can be taken over a fixed countable dense subset.

## Step 004 — Population geometry

The representations of \(F\) and \(\widehat F\) show that they are Hilbert-valued polynomials of degree at most two. Expanding their squared norms gives real polynomials \(d\) and \(\widehat d\) of degree at most four, restricted to \(A\). In particular their tangent Hessians are continuous. This is a consequence of the criterion definitions, not an additional task assumption.

First consider \(R_{12}=\varnothing\). The compact domain \(\Delta_{\bar r}\) is nonempty, and Step 002 gives no zeros. Therefore
\[
\zeta=\min_{\Delta_{\bar r}}d>0.
\]
Population sublevel sets below \(\zeta\) are empty. If \(\varepsilon_0=\zeta/8\), \(c_0=\zeta/2\), and the stated perturbation conditions hold, then everywhere on the domain
\[
\widehat d\geq\zeta-\varepsilon\geq7\zeta/8>c_0\geq c.
\]
The empirical sublevel set is also empty, which is exactly the claimed zero-component conclusion.

Next, if \(L=1\) and \(R_{12}\ne\varnothing\), then \(\Theta=(1)\), \(R_{12}=\{1\}\), \(r_1=1\), and \(\Delta_{\bar r}=\{1\}\). Under the perturbation condition, \(\widehat d(1)\leq\varepsilon\leq c\). Thus the empirical set is this singleton. Any fixed positive \(\varepsilon_0,c_0\), for example both equal to one, suffice. The zero-dimensional tangent-space condition causes no difficulty.

It remains to consider \(L\geq2\) and \(R_{12}\ne\varnothing\). The strict radius condition puts every target in the relative interior of \(\Delta_{\bar r}\). By Hessian continuity and positive definiteness, choose open Euclidean balls \(B_i\) in \(A\), centered at \(r_i\), whose closures are pairwise disjoint and lie in that relative interior, such that
\[
\nabla_T^2d(r)\succeq\lambda_i I_T\quad(r\in\overline B_i)
\]
for constants \(\lambda_i>0\). The tangent gradient vanishes at \(r_i\), because \(d\geq0\) and \(d(r_i)=0\). Integration along a segment gives
\[
d(r)\geq\frac{\lambda_i}{2}\|r-r_i\|_2^2\quad(r\in B_i).
\]
Choose the balls small enough that their union does not cover \(\Delta_{\bar r}\). Its compact complement contains no population zero, and hence
\[
\zeta=\min_{r\in\Delta_{\bar r}\setminus\bigcup_iB_i}d(r)>0.
\]
For \(0\leq c<\zeta\), every population sublevel point lies in one of the balls. Its intersection with each ball is nonempty because it contains \(r_i\), and convex because \(d\) is strongly convex there. The balls have disjoint closures, so these intersections are precisely the separate connected components. This proves the population low-level geometry used in the transfer argument.

## Step 005 — Empirical stability

We now justify the derivative control that is indispensable to the transfer. Identify \(A\) with \(\mathbb R^{L-1}\) by fixed orthonormal affine coordinates. The restrictions to \(A\) of real polynomials of degree at most four form a finite-dimensional vector space. The compact domain \(\Delta_{\bar r}\) contains a nonempty open subset of \(A\), so a polynomial restriction vanishing on the domain is identically zero: this follows by applying the univariate polynomial identity property successively in affine coordinates.

For completeness, express such a polynomial \(p\) by its monomial coefficient vector \(u\). On the coefficient unit sphere, the continuous function \(u\mapsto\|p\|_{\infty,\Delta_{\bar r}}\) is positive and has a positive minimum \(b\). Therefore
\[
\|u\|_2\leq b^{-1}\|p\|_{\infty,\Delta_{\bar r}}.
\]
Every second derivative is a fixed finite linear combination of the coefficients with polynomial factors bounded on this compact domain. Consequently there is a finite constant \(C\geq1\), depending only on the domain and the fixed affine coordinates, such that
\[
\sup_{r\in\Delta_{\bar r}}\|\nabla_T^2p(r)\|_{\mathrm{op}}
\leq C\|p\|_{\infty,\Delta_{\bar r}}.
\]
This controls tangent derivatives of polynomial restrictions; no claim about normal derivatives from an affine-domain norm is needed.

Apply the bound to \(p=\widehat d-d\), whose degree is at most four by Step 004. With \(\lambda=\min_i\lambda_i>0\), choose
\[
c_0=\zeta/2,\qquad
\varepsilon_0=\min\{\zeta/8,\lambda/(2C)\}.
\]
All these constants are determined by the population function and fixed domain, independently of sample sizes and sample realizations. Whenever the required uniform approximation holds, on each \(B_i\)
\[
\nabla_T^2\widehat d\succeq
(\lambda_i-C\varepsilon)I_T
\succeq(\lambda_i/2)I_T.
\]
Thus the empirical function is strongly convex on each ball.

For every point outside the balls,
\[
\widehat d(r)\geq d(r)-\varepsilon
\geq\zeta-\varepsilon
\geq7\zeta/8>c_0\geq c.
\]
On the other hand, for every target,
\[
\widehat d(r_i)\leq\varepsilon\leq c,
\]
where \(2\varepsilon\leq c\) and nonnegativity of the parameters have been used. Non-strict containment is sufficient, including when \(\varepsilon=c=0\).

Define
\[
A_i=\{r\in\Delta_{\bar r}:\widehat d(r)\leq c\}\cap B_i.
\]
The empirical sublevel set is the union of these sets. Each \(A_i\) contains \(r_i\) and is convex, being a sublevel set of a convex function on the convex ball \(B_i\). Thus each is connected. The disjoint ball closures separate the sets, so they are exactly the connected components of the empirical sublevel set. Each contains its own target and no other target. This proves the theorem.

## Closure assessment

All obligations are closed. The only external concentration inputs are the explicitly stated standard bounded-difference and Hilbert-space Efron–Stein inequalities, with their hypotheses verified above. Signed-measure injectivity and finite-dimensional derivative control are explicitly derived. No paper-specific result is left as an unproved dependency.
