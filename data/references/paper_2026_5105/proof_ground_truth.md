# Reference Proof

## Contract and obligations

The design and supplied source matrices, including their completed bases, are fixed. Probability is over the target noise. The initializer may depend on the target observations, and its error bounds are standing almost-sure assumptions. We do not condition the Gaussian law on an initializer-success event. Source perturbation estimates below are deterministic.

We prove: (1) localization, full estimated rank, and compatible factor alignment; (2) factor perturbation bounds; (3) simultaneous score bounds despite the fitted right factor depending on the noise; (4) the correctly signed basic inequality and clean-support decomposition; (5) the noisy-source off-support bounds; and (6) the final quadratic estimate. No nonstandard external result is left as an unproved obligation.

Write |M|_1 and |M|_infty for entrywise norms. Put
\[
K=r(r_u+r_v+1)+s_u(r_u)+s_v(r_v),\qquad L=\log(12r\max(p,q)/\delta),
\]
\[
A^*=U^*D^*,\quad B^*=V^*D^*,\quad \widehat A=\widehat U\widehat D,\quad \widehat B=\widehat V\widehat D.
\]
Let \(\Delta=\widehat C-C^*\), \(\Delta_a=\widehat A-A^*\), \(\Delta_b=\widehat B-B^*\), \(\Delta_d=\widehat D-D^*\), and \(t=\|\Delta\|_F\). All support sets below are defined by the CLEAN source bases.

## 1. Standard perturbation facts and their application

We use the following independently standard perturbation statements. Ordered singular values satisfy Weyl's bound \(\max_j|d_j-\bar d_j|\leq\|C-\bar C\|_2\) and Hoffman--Wielandt's bound \(\sum_j(d_j-\bar d_j)^2\leq\|C-\bar C\|_F^2\). For symmetric matrices \(G,\widetilde G\), a simple ordered eigenvector of \(G\) with population eigengap \(g>0\) and the corresponding ordered eigenvector of \(\widetilde G\) satisfy
\[
\min_{s\in\{\pm1\}}\|s\widetilde w-w\|_2\leq 2\sqrt2\,\|\widetilde G-G\|_2/g.
\]
For their leading \(k\)-dimensional eigenvector matrices, with population boundary gap \(g>0\), there is an orthogonal \(O\) such that
\[
\|\widetilde W O-W\|_F\leq 2\sqrt{2k}\,\|\widetilde G-G\|_2/g.
\]
These are the population-gap eigenvector/subspace perturbation bounds used in the source. A full-dimensional subspace needs no perturbation bound: its orthogonal-complement contribution is zero.

The true matrix is feasible for the localized problem. The triangle inequality gives
\[
t\leq3R_{2,n},\qquad \|\Delta\|_{1,2}\leq3R_{1,n}.
\]
Simultaneously permuting factor columns leaves the objective and constraints unchanged, so sort the estimated singular values. With \(e=\|\Delta\|_2\), the radius assumption gives
\[
e\leq\frac{\tau}{6\sqrt5}\frac{d_r^*}{\sqrt r}(d_r^*/d_1^*)^{3/2}<d_r^*/4.
\]
Consequently \(\widehat d_j\geq3d_j^*/4>0\), \(\|\widehat D^{-1}\|_2\leq2/d_{\min}\), and \(\|D^*\widehat D^{-1}\|_2\leq2\).

For either target Gram matrix, the perturbation norm is at most \((2d_1^*+e)e\leq3d_1^*e\). The target relative gaps, including the gap to zero when needed, are at least \(\tau(d_j^*)^2\). Thus the separate sign-aligned left and right vector errors are each bounded by
\[
a_j=\frac{3\cdot2^{3/2}d_1^*e}{\tau(d_j^*)^2}.
\]
We verify that the two signs can be chosen together. If
\((\widehat u_j^Tu_j^*)(\widehat v_j^Tv_j^*)\leq0\), then
\[
u_j^{*T}(C^*-\widehat C)v_j^*\geq d_j^*-\sum_{k\ne j}\widehat d_k|\widehat u_k^Tu_j^*|\,|\widehat v_k^Tv_j^*|.
\]
Orthogonality bounds each off-diagonal inner product by its corresponding aligned vector error. Using \(\widehat d_1\leq5d_1^*/4\), the sum is at most
\[
\frac{90r(d_1^*)^3e^2}{\tau^2(d_j^*)^4}\leq d_j^*/2.
\]
The last inequality follows because the radius bound for \(j=r\) implies the same bound for every \(j\). This contradicts \(e<d_j^*/4\). Therefore the paired inner products have the same nonzero sign. Simultaneously flip each ESTIMATED vector pair so both inner products are positive, retaining the true vectors as fixed deterministic vectors. Such flips preserve the objective and localization.

Hoffman--Wielandt gives \(\|\Delta_d\|_F\leq t\). Also
\[
\widehat U\widehat D-U^*D^*=\widehat U(\widehat D-D^*)+(\widehat U-U^*)D^*,
\]
so
\[
\|\Delta_a\|_F\leq t+\left(\sum_j(d_j^*)^2a_j^2\right)^{1/2}
\leq\left[1+\frac{3\cdot2^{3/2}}{\tau}\left(\sum_j(d_1^*/d_j^*)^2\right)^{1/2}\right]t.
\]
The identical argument for the right Gram matrix gives the same bound for \(\Delta_b\). Hence, for a fixed universal \(c\), for example \(c=20\),
\[
\|\Delta_a\|_F,\|\Delta_b\|_F\leq c\eta_rt,\qquad \|\Delta_d\|_F\leq t.
\]
This supplies the factor result directly; the specialized supplementary citation is not needed.

## 2. Gaussian score events

Let \(Q_u,Q_v\) be the full noisy-source orthogonal bases, and let \(Z=X^TE/n\). We prove that with probability at least \(1-\delta\),
\[
|Q_u^TZ\widehat V|_\infty\leq\lambda_u/2,\qquad
|U^{*T}Z\widehat V|_\infty\leq\lambda_u/2,\qquad
|U^{*T}ZQ_v|_\infty\leq\lambda_v/2. \tag{A}
\]

For completeness, a centered Gaussian vector \(g\) with covariance \(\Sigma\) satisfies, for \(x>0\),
\[
\Pr\{\|g\|_2^2>\operatorname{tr}\Sigma+2\sqrt{\operatorname{tr}(\Sigma^2)x}+2\|\Sigma\|_2x\}\leq e^{-x}.
\]
Indeed diagonalization expresses the centered squared norm as \(\sum_j\mu_j(Z_j^2-1)\). Its log moment-generating function is at most
\(\theta^2\sum_j\mu_j^2/(1-2\theta\max_j\mu_j)\); exponential Markov optimization gives the displayed tail. If \(\Sigma=0\), the assertion is deterministic. Since \(2a+2b\leq4\max(a,b)\), the constants in the task can be chosen as \(c_1=4,c_2=1\). Other fixed valid universal choices give the same argument.

Denote the square bracket in the task's covariance condition by \(B_\Sigma\). Every fixed unit direction \(w\in\mathbb R^p\) satisfies
\[
E^TXw/n\sim N(0,\beta\Sigma/n),\qquad \beta=\|Xw\|_2^2/n\leq\nu.
\]
A union bound over the \(p\) columns of \(Q_u\) therefore gives, with failure probability at most \(\delta/6\),
\[
M_u^2:=\max_i\|E^TX(Q_u)_{:i}/n\|_2^2\leq\nu B_\Sigma/n.
\]
The same conclusion, with failure probability at most \(\delta/6\), holds for the maximum \(M_*\) over the \(r\) columns of \(U^*\), since \(r\leq p\).

Because \(\widehat V=(B^*+\Delta_b)\widehat D^{-1}\),
\[
|Q_u^TZ\widehat V|_\infty
\leq2|Q_u^TZV^*|_\infty+\frac{6c\eta_rR_{2,n}}{d_{\min}}M_u.
\]
Every entry of the fixed Gaussian matrix \(Q_u^TZV^*\) has variance at most \(\nu\alpha_{\max}/n\). The scalar Gaussian tail and the specified \(\lambda_u\) give
\[
\Pr\{2|Q_u^TZV^*|_\infty>\lambda_u/4\}
\leq2pr\exp\{-n\lambda_u^2/(128\nu\alpha_{\max})\}=\delta/6.
\]
On the vector-norm event the squared second term is at most
\[
\frac{36c^2\eta_r^2R_{2,n}^2\nu B_\Sigma}{d_{\min}^2n}\leq\lambda_u^2/16
\]
by the covariance condition. This proves the first event in (A) with failure at most \(\delta/3\). Replacing \(Q_u\) by \(U^*\) uses at most \(r^2\leq pr\) scalar scores and \(M_*\), and proves the second event with the same failure bound.

Finally the \(rq\) entries of \(U^{*T}ZQ_v\) are fixed Gaussian scores of variance at most \(\nu\alpha_{\max}/n\). Thus
\[
\Pr\{|U^{*T}ZQ_v|_\infty>\lambda_v/2\}
\leq2qr\exp\{-n\lambda_v^2/(8\nu\alpha_{\max})\}=\delta/3.
\]
A union bound proves (A). None of these arguments assumes that \(\widehat V\) is independent of \(E\).

## 3. Optimality and the deterministic quadratic inequality

Work on (A). Define
\[
P_u(A)=|\widetilde U_\perp^{\mathrm{s}T}A|_1,\qquad P_v(B)=|\widetilde V_\perp^{\mathrm{s}T}B|_1.
\]
Optimality against the feasible true factors gives the correctly signed inequality
\[
\frac{\|X\Delta\|_F^2}{2n}
\leq\langle Z,\Delta\rangle+\lambda_u[P_u(A^*)-P_u(\widehat A)]+\lambda_v[P_v(B^*)-P_v(\widehat B)]. \tag{B}
\]
The exact decomposition is
\[
\Delta=\Delta_a\widehat V^T-U^*\Delta_d\widehat V^T+U^*\Delta_b^T.
\]
Thus its score consists respectively of pairings of \(\Delta_a,\Delta_d,\Delta_b\) with \(Z\widehat V,-U^{*T}Z\widehat V,Z^TU^*\).

Set
\[
M_u^0=|[\widetilde U_\perp^{\mathrm{s}T}A^*]_{S_u^c}|_1,\qquad
M_v^0=|[\widetilde V_\perp^{\mathrm{s}T}B^*]_{S_v^c}|_1.
\]
To spell out decomposability on the left, write \(a=\widetilde U_\perp^{\mathrm{s}T}\Delta_a\), \(a^*=\widetilde U_\perp^{\mathrm{s}T}A^*\), and \(\widehat a=\widetilde U_\perp^{\mathrm{s}T}\widehat A\). Then
\[
|a^*|_1-|\widehat a|_1\leq|a_{S_u}|_1+|a^*_{S_u^c}|_1-|\widehat a_{S_u^c}|_1,
\quad |a_{S_u^c}|_1\leq|a^*_{S_u^c}|_1+|\widehat a_{S_u^c}|_1.
\]
Splitting the left score into the leading and complementary noisy coordinates and using (A), these inequalities give
\[
\langle Z\widehat V,\Delta_a\rangle+\lambda_u[P_u(A^*)-P_u(\widehat A)]
\leq\frac{3\lambda_u}{2}\sqrt{2(rr_u+s_u)}\,\|\Delta_a\|_F+\frac{3\lambda_u}{2}M_u^0.
\]
Here Cauchy--Schwarz uses \(rr_u\) leading entries and \(s_u\) clean-support entries, and orthogonal projections do not increase the Frobenius norm. The identical right-coordinate argument gives the expression with \(\lambda_v,rr_v+s_v,\Delta_b,M_v^0\). The diagonal term is at most \((\lambda_u/2)\sqrt r\|\Delta_d\|_F\).

Let \(\lambda=\max(\lambda_u,\lambda_v)\). Combining these bounds with (B) and the factor estimates yields
\[
\frac{\|X\Delta\|_F^2}{2n}\leq C_0\lambda\eta_r\sqrt K\,t+\frac{3\lambda}{2}(M_u^0+M_v^0).
\]
Columnwise restricted curvature and localization give
\[
\frac{\|X\Delta\|_F^2}{2n}\geq\frac{\rho_2}{2}t^2-9\rho_1R_{1,n}^2\frac{\log p}{n}.
\]
Consequently
\[
t^2\leq\frac{2C_0}{\rho_2}\lambda\eta_r\sqrt K\,t+
\frac{3\lambda}{\rho_2}(M_u^0+M_v^0)+\frac{18\rho_1}{\rho_2}R_{1,n}^2\frac{\log p}{n}. \tag{C}
\]

## 4. Explicit noisy-source off-support mass

Put \(H=\varepsilon^{(0)}(2d_1^{(0)}+\varepsilon^{(0)})\). The left and right source Gram perturbations have norm at most \(H\).

For the left side let \(k=r_u^*\), \(m=r(k-r_u)_+-s_u(r_u)\), and \(\ell=p-\max(k,r_u)\). These integers are nonnegative. If \(r_u\leq k\), partition the complementary source coordinates into indices \(r_u+1,\ldots,k\) and indices after \(k\). There are exactly \(m\) clean-zero entries in the first block. Each such noisy entry is bounded, after an immaterial source-vector sign choice, by
\[
2\sqrt2\,H/[\tau(d_k^{(0)})^2].
\]
Indeed its clean inner product is zero and its individual-vector population gap is at least \(\tau(d_k^{(0)})^2\). Thus the gap block contributes at most \(2\sqrt2 mH/[\tau(d_k^{(0)})^2]\).

For the tail, let \(W\) and \(\widetilde W\) contain the first \(k\) clean and noisy left vectors. Containment gives \(\|U^{*T}W\|_F=\sqrt r\). When \(k<p\), the boundary gap is at least \(\tau(d_k^{(0)})^2\), including the gap to zero if \(k=r_0\). The standard subspace bound gives an orthogonal \(O\) with
\[
\|\widetilde W O-W\|_F\leq2\sqrt{2k}H/[\tau(d_k^{(0)})^2].
\]
Let \(T\) consist of the noisy vectors after \(\max(k,r_u)\), so it has \(\ell\) columns. Orthogonality and Cauchy--Schwarz imply
\[
|T^TU^*|_1^2\leq r\ell\|T^TU^*\|_F^2
\leq r\ell\{r-\|U^{*T}\widetilde W\|_F^2\}
\leq2r^2\ell\|\widetilde W O-W\|_F.
\]
For the last inequality, factor the difference of squares and use
\(\sqrt r-\|U^{*T}\widetilde W\|_F\leq\sqrt r\|\widetilde W O-W\|_F\).
Therefore
\[
|[\widetilde U_\perp^{\mathrm{s}T}U^*]_{S_u^c}|_1
\leq\frac{2^{3/2}mH}{\tau(d_k^{(0)})^2}
+\frac{2^{5/4}rk^{1/4}\sqrt\ell\,H^{1/2}}{\sqrt\tau\,d_k^{(0)}}. \tag{D}
\]
If \(r_u>k\), the clean support is empty and the same tail argument proves (D) with \(m=0\). If \(\ell=0\), the tail is empty and its estimate is zero, without invoking a nonexistent full-dimensional boundary gap. The right-side proof replaces \((p,r_u,r_u^*,s_u,U)\) with \((q,r_v,r_v^*,s_v,V)\).

Multiplication by \(D^*\) preserves these coordinate masks and multiplies entrywise mass by at most \(d_1^*\). Since \(d_{r_u^*}^{(0)},d_{r_v^*}^{(0)}\geq d_{\min}^{(0)}\), summing (D) and its right counterpart yields
\[
M_u^0+M_v^0\leq C_1d_1^*\{MH+rT_0H^{1/2}\}\leq C_1d_1^*\varepsilon_{\rm src}^2,
\]
where
\[
M=r\{(r_u^*-r_u)_++(r_v^*-r_v)_+\}-s_u-s_v,
\]
\[
T_0=(r_u^*)^{1/4}\sqrt{p-\max(r_u^*,r_u)}+(r_v^*)^{1/4}\sqrt{q-\max(r_v^*,r_v)}.
\]
The last inequality follows from the task's expression \(\varepsilon_{\rm src}=\sqrt M H^{1/2}+\sqrt{rT_0}H^{1/4}\). In particular the mass scales as \(\varepsilon_{\rm src}^2\), not \(\varepsilon_{\rm src}\).

## 5. Conclusion and source-local corrections

For nonnegative \(t,b,a\), \(t^2\leq bt+a\) implies \(t\leq b+\sqrt a\). Apply this to (C), using \(\sqrt{x+y}\leq\sqrt x+\sqrt y\), the mass estimate, and
\[
\lambda\leq8\sqrt{2\nu\alpha_{\max}}\sqrt{L/n}.
\]
It follows that
\[
t\leq C\sqrt{\alpha_{\max}}\eta_r\sqrt{KL/n}
+C\alpha_{\max}^{1/4}\sqrt{d_1^*}\,\varepsilon_{\rm src}(L/n)^{1/4}
+C R_{1,n}\sqrt{\log p/n}.
\]
The assumed mixed-norm radius bound absorbs the last term into the first. The event (A) has probability at least \(1-\delta\), proving the claim.

All constants absorbed here depend only on the fixed absolute ambient constants. Zero source perturbation, zero covariance, zero localization radii, empty coordinate supports, and full truncations are covered by the same inequalities or their explicitly stated empty-block interpretations.

The source-local corrections recorded under theory_005 are used explicitly: the quadratic solution has a square root; the tail coefficient retains 1/sqrt(tau) until it is absorbed into a constant; and substituting an upper bound for lambda_max preserves an inequality rather than an equality. No final theorem clause is changed by these source repairs.
