# Problem

## Setup

Let \(n,p,q,r,r_0\) be integers with \(n\geq1\), \(p\geq2\), \(q\geq1\), and \(1\leq r\leq r_0\leq\min(p,q)\). The rank \(r\) is known. Let \(X\in\mathbb R^{n\times p}\) be fixed, and observe
\[
Y=XC^*+E,\qquad C^*=U^*D^*V^{*\top},
\]
where \(U^*\in\mathbb R^{p\times r}\) and \(V^*\in\mathbb R^{q\times r}\) have orthonormal columns and \(D^*=\operatorname{diag}(d_1^*,\ldots,d_r^*)\) has ordered positive entries. The rows of \(E\) are independent \(N(0,\Sigma)\), where \(\Sigma\) is positive semidefinite and \(\|\Sigma\|_2\leq\alpha_{\max}\) for \(\alpha_{\max}>0\).

A fixed clean source matrix has ordered SVD
\[
C^{(0)}=U^{(0)}D^{(0)}V^{(0)\top},
\]
with rank \(r_0\) and positive singular values \(d_1^{(0)}\geq\cdots\geq d_{r_0}^{(0)}\). A supplied source matrix is
\[
\widetilde C^{(0)}=C^{(0)}+E^{(0)},\qquad
\varepsilon^{(0)}=\|\widetilde C^{(0)}-C^{(0)}\|_2.
\]
Its nonzero singular values are distinct. Both source matrices and their chosen completed singular bases are fixed in the probability assertion; no distributional assumption is made on the fixed perturbation \(E^{(0)}\).

Extend the ordered left and right singular bases of each source matrix to full orthonormal bases. For an integer \(0\leq k\leq p\), let \(U^{\mathrm{s}}(k)\) and \(U^{\mathrm{s}}_\perp(k)\) contain the first \(k\) and the remaining clean left source vectors, respectively. Define \(\widetilde U^{\mathrm{s}}(k),\widetilde U^{\mathrm{s}}_\perp(k)\) using the supplied source matrix. Define the four corresponding right-basis matrices for \(0\leq k\leq q\) analogously. Empty matrices have compatible dimensions, and their entrywise norms and support sizes are zero.

Assume
\[
\operatorname{col}(U^*)\subseteq\operatorname{col}(U^{(0)}),\qquad
\operatorname{col}(V^*)\subseteq\operatorname{col}(V^{(0)}).
\]
Define the clean-source containment cutoffs by
\[
r_u^*=\min\{k:\operatorname{col}(U^*)\subseteq\operatorname{col}(U^{\mathrm{s}}(k))\},\qquad
r_v^*=\min\{k:\operatorname{col}(V^*)\subseteq\operatorname{col}(V^{\mathrm{s}}(k))\}.
\]
Fix integers \(0\leq r_u\leq p\) and \(0\leq r_v\leq q\), and set
\[
S_u=\{(i,j):[U^{\mathrm{s}}_\perp(r_u)^TU^*]_{ij}\ne0\},\qquad s_u(r_u)=|S_u|,
\]
\[
S_v=\{(i,j):[V^{\mathrm{s}}_\perp(r_v)^TV^*]_{ij}\ne0\},\qquad s_v(r_v)=|S_v|.
\]

For a matrix \(M\), let \(\|M\|_1=\sum_{i,j}|M_{ij}|\) denote its entrywise \(\ell_1\) norm, let \(\|M\|_2\) denote its spectral norm, and let
\[
\|M\|_{1,2}=\left(\sum_j\left(\sum_i|M_{ij}|\right)^2\right)^{1/2}.
\]
The notation \(\|M\|_F\) denotes the Frobenius norm.

Let \(R_{2,n},R_{1,n}\geq0\) be deterministic radii. A measurable initializer \(\widehat C^{\mathrm{init}}\), based on the observed inputs \((X,Y,\widetilde C^{(0)})\), is assumed to satisfy almost surely
\[
\|\widehat C^{\mathrm{init}}-C^*\|_F\leq R_{2,n},\qquad
\|\widehat C^{\mathrm{init}}-C^*\|_{1,2}\leq R_{1,n}.
\]
It need not be independent of \(E\). Let \((\widehat U,\widehat D,\widehat V)\) be any measurable choice of a global minimizer of
\[
\frac1{2n}\|Y-XUDV^T\|_F^2+
\lambda_u\|\widetilde U^{\mathrm{s}}_\perp(r_u)^TUD\|_1+
\lambda_v\|\widetilde V^{\mathrm{s}}_\perp(r_v)^TVD\|_1
\]
over \(U\in\mathbb R^{p\times r}\), \(V\in\mathbb R^{q\times r}\), and diagonal \(D\in\mathbb R^{r\times r}\), subject to
\[
U^TU=V^TV=I_r,\qquad D\geq0,
\]
\[
\|UDV^T-\widehat C^{\mathrm{init}}\|_F\leq2R_{2,n},\qquad
\|UDV^T-\widehat C^{\mathrm{init}}\|_{1,2}\leq2R_{1,n}.
\]
Set \(\widehat C=\widehat U\widehat D\widehat V^T\).

Let \(\rho_1,\rho_2,\nu,d_{\min},d_{\min}^{(0)},K_R\) be fixed positive absolute constants, and let \(\tau\in(0,1)\) be a fixed absolute constant. These constants do not vary with the dimensions, sample size, noise scale, or coefficient matrices. Assume, for every \(\beta\in\mathbb R^p\),
\[
\frac1{2n}\|X\beta\|_2^2\geq\frac{\rho_2}{2}\|\beta\|_2^2-\rho_1\frac{\log p}{n}\|\beta\|_1^2,
\qquad \sup_{\|u\|_2\leq1}\|Xu\|_2^2\leq\nu n,
\]
and assume
\[
d_r^*\geq d_{\min},\qquad d_{r_0}^{(0)}\geq d_{\min}^{(0)},
\]
\[
(d_{j-1}^*)^2-(d_j^*)^2\geq\tau(d_{j-1}^*)^2\quad(2\leq j\leq r),
\]
\[
(d_{j-1}^{(0)})^2-(d_j^{(0)})^2\geq\tau(d_{j-1}^{(0)})^2\quad(2\leq j\leq r_0).
\]
Put
\[
\eta_r=1+\tau^{-1}\left(\sum_{j=1}^r(d_1^*/d_j^*)^2\right)^{1/2}.
\]

## Task

Prove that there exist absolute constants \(c,c_1,c_2>0\) for which the following assertion holds.

Fix \(\delta\in(0,1)\), and assume
\[
R_{2,n}\leq\frac{\tau}{18\sqrt5}\frac{d_r^*}{\sqrt r}(d_r^*/d_1^*)^{3/2},
\]
\[
R_{1,n}^2\leq K_R\alpha_{\max}\eta_r^2\{r(r_u+r_v+1)+s_u(r_u)+s_v(r_v)\}
\frac{\log(12r\max(p,q)/\delta)}{\log p},
\]
\[
\frac{9c^2\eta_r^2R_{2,n}^2}{2\alpha_{\max}d_{\min}^2}
\left[\operatorname{tr}(\Sigma)+c_1\max\left\{
\sqrt{\operatorname{tr}(\Sigma^2)\log(6p/\delta)/c_2},
\alpha_{\max}\log(6p/\delta)/c_2\right\}\right]
\leq\log(12pr/\delta).
\]
Choose
\[
\lambda_u=8\sqrt2\sqrt{\nu\alpha_{\max}\log(12pr/\delta)/n},\qquad
\lambda_v=2\sqrt2\sqrt{\nu\alpha_{\max}\log(6qr/\delta)/n}.
\]
Then, with probability at least \(1-\delta\),
\[
\|\widehat C-C^*\|_F\leq C\sqrt{\alpha_{\max}}\eta_r
\sqrt{\frac{\{r(r_u+r_v+1)+s_u(r_u)+s_v(r_v)\}\log(12r\max(p,q)/\delta)}{n}}
+C\alpha_{\max}^{1/4}(d_1^*)^{1/2}\varepsilon_{\rm src}
\left[\frac{\log(12r\max(p,q)/\delta)}{n}\right]^{1/4},
\]
where \((a)_+=\max(a,0)\) and
\[
\begin{aligned}
\varepsilon_{\rm src}={}&
\Bigl[r\{(r_u^*-r_u)_++(r_v^*-r_v)_+\}-s_u(r_u)-s_v(r_v)\Bigr]^{1/2}
(\varepsilon^{(0)})^{1/2}(2d_1^{(0)}+\varepsilon^{(0)})^{1/2}\\
&+\sqrt r\Bigl[(r_u^*)^{1/4}\sqrt{p-\max(r_u^*,r_u)}
+(r_v^*)^{1/4}\sqrt{q-\max(r_v^*,r_v)}\Bigr]^{1/2}
(\varepsilon^{(0)})^{1/4}(2d_1^{(0)}+\varepsilon^{(0)})^{1/4}.
\end{aligned}
\]
Here \(C>0\) may depend only on the fixed absolute constants \(\rho_1,\rho_2,\nu,d_{\min},d_{\min}^{(0)},\tau,K_R\) and the chosen absolute constants \(c,c_1,c_2\), and not on any other model quantities. The probability assertion is over \(E\) with the fixed inputs specified above.
