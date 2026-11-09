# Reference Proof

## Proof Structure and Obligations

We prove: (1) harmonicity of the lift; (2) the Gaussian eigenvalue on harmonic homogeneous polynomials; (3) the Taylor/symmetry ReLU representation, including zero inner products; (4) projection and identification of the sharpened coefficients; (5) the Hermite/Fischer identity and Gaussian radial moments; (6) the sub-Gaussian neuron-norm estimates with the exact constants; and (7) finite-width existence by an explicit Hilbert-space sampling calculation. Each obligation is derived below.

The proof uses only the nondegenerate Gaussian specialization of the source's spectral calculation. It does not assume invertibility for every spherical probability. Likewise, the final sampling law need not dominate parameters whose neurons vanish in L2(D); no global dominating-measure optimization assertion is needed.

## 1. Harmonic Lift

Write p=sum_{k=0}^m p_k and extend p_k by zero for k>m. Define
\[
P(x,y)=\sum_{j\geq0}\frac{(-1)^j y^{2j}}{(2j)!}\Delta^j p(x),\qquad
P_k(x,y)=\sum_{0\leq j\leq k/2}\frac{(-1)^j y^{2j}}{(2j)!}\Delta^j p_k(x).
\]
These sums are finite. Every term in P_k has total degree k, and P_k(x,0)=p_k(x). Differentiating twice in y and shifting the index cancels the terms obtained by applying Delta_x. The remaining terminal Laplacian vanishes by degree. Thus
\[
(\Delta_x+\partial_y^2)P_k=0,
\qquad P=\sum_{k=0}^mP_k,
\qquad P(x,0)=p(x).
\]

## 2. Gaussian Harmonic Eigenvalue

Let q=d+1 and Z~N(0,tau^2 I_q). First, for any polynomial r and a in R^q, finite Taylor expansion and independent Gaussian even moments give
\[
\mathbb E r(a+Z)
=\sum_{\beta\in\mathbb N_0^q}
\frac{(\tau^2/2)^{|\beta|}}{\beta!}\partial^{2\beta}r(a)
=\sum_{j\geq0}\frac{(\tau^2/2)^j}{j!}\Delta^j r(a).
\]
Consequently, if h is harmonic, E h(a+Z)=h(a).

Completing the square in the Gaussian density gives, for real t,
\[
\mathbb E\big[h(Z)e^{t\langle z,Z\rangle}\big]
=e^{\tau^2t^2\|z\|^2/2}\mathbb E h(Z+\tau^2tz).
\]
If h is also homogeneous of degree k, the right side is
\[
e^{\tau^2t^2\|z\|^2/2}\tau^{2k}t^k h(z).
\]
Taking the coefficient of t^k, or differentiating k times at zero, is justified by Gaussian integrability of polynomial times exponential functions. It yields
\[
\mathbb E\big[h(Z)\langle z,Z\rangle^k\big]
=\tau^{2k}k!h(z).
\]
By homogeneity, therefore,
\[
\mathbb E h(\langle z,Z\rangle Z)=\tau^{2k}k!h(z). \tag{1}
\]
This proves the needed eigenvalue rather than merely citing a paper-specific spectral result.

For completeness, the radial density of Z gives
\[
\mathbb E\|Z\|^{2k}
=\tau^{2k}2^k\frac{\Gamma(k+q/2)}{\Gamma(q/2)}.
\]
Factoring Z into independent radius and uniform direction in (1) recovers the corresponding angular eigenvalue
\[
\frac{\Gamma(q/2)k!}{2^k\Gamma(k+q/2)}.
\]
Thus the direct calculation agrees with the source's angular-times-radial diagonalization, including q=2.

Set
\[
g(z)=\sum_{k=0}^m\frac{P_k(z)}{k!\tau^{2k}}.
\]
Equation (1) implies E g(<z,Z>Z)=P(z), and g(0)=P(0)=p_0.

## 3. Taylor and Symmetry

Fix z and put t=<z,Z>. The function
\[
F_z(Z)=g(\langle z,Z\rangle Z)-g(0)
\]
is unchanged when Z is replaced by -Z and is zero whenever <z,Z>=0. Hence
\[
\mathbb E F_z(Z)=2\mathbb E\big[F_z(Z)\mathbf1_{\{\langle z,Z\rangle>0\}}\big].
\]
Subtracting g(0) before this split avoids losing a contribution on the zero hyperplane and handles z=0 as well.

For g_v(t)=g(tv) and t>0, Taylor's integral remainder gives
\[
g_v(t)-g_v(0)=t g_v'(0)+\int_0^t(t-s)g_v''(s)\,ds.
\]
Substituting into the preceding symmetry identity gives
\[
P(z)=P(0)+\mathbb E\left[
2g_Z'(0)\operatorname{ReLU}(\langle z,Z\rangle)
+2\int_0^\infty g_Z''(s)\operatorname{ReLU}(\langle z,Z\rangle-s)\,ds
\right]. \tag{2}
\]
Homogeneity gives exactly
\[
g_{(v,w)}'(0)=\frac{P_1(v,w)}{\tau^2},\qquad
g_{(v,w)}''(s)=\sum_{k=2}^m\frac{s^{k-2}P_k(v,w)}{(k-2)!\tau^{2k}}. \tag{3}
\]
All exchanges here are absolutely integrable. Indeed, for k>=2,
\[
\int_0^\infty s^{k-2}(t-s)_+\,ds
=\frac{(t_+)^k}{k(k-1)},
\]
and |P_k(Z)|<=C_k||Z||^k. For fixed z, the absolute integrated kth term is therefore bounded by a constant times ||Z||^{2k}, which has finite Gaussian expectation. The linear term has the same elementary integrability property.

## 4. Projection and Sharpening

Put z=(x,0) and write Z=(V,W), where V~N(0,tau^2 I_d) and W~N(0,tau^2) are independent. The neuron depends only on V. Gaussian even moments give
\[
\mathbb E W^{2j}=\tau^{2j}\frac{(2j)!}{2^j j!},
\]
so
\[
\mathbb E_WP_k(v,W)
=\sum_j\frac{(-\tau^2/2)^j}{j!}\Delta^j p_k(v)
=p_k^\sharp(v). \tag{4}
\]
The absolute-integrability argument above also justifies this projection. Substituting (3) and (4) into (2) gives, for every x,
\[
\begin{aligned}
p(x)=p_0
&+\mathbb E_V\left[
\frac{2p_1^\sharp(V)}{\tau^2}\operatorname{ReLU}(\langle x,V\rangle)\right.\\
&\left.\qquad+\int_0^\infty
2\sum_{k=2}^m\frac{s^{k-2}p_k^\sharp(V)}{(k-2)!\tau^{2k}}
\operatorname{ReLU}(\langle x,V\rangle-s)\,ds\right].
\end{aligned}
\]
In particular, p_1^sharp=p_1. The formula includes constant and zero polynomials under the stated zero-component convention.

## 5. Hermite/Fischer Identity and Radial Moments

Define polynomial coefficients H_{tau,alpha}(v) by
\[
e^{\langle t,v\rangle-\tau^2\|t\|^2/2}
=\sum_{\alpha\in\mathbb N_0^d}H_{\tau,\alpha}(v)\frac{t^\alpha}{\alpha!}.
\]
Expanding the exponential, or comparing coefficients after applying the finite polynomial heat operator, shows
\[
H_{\tau,\alpha}(v)=e^{-\tau^2\Delta/2}v^\alpha.
\]
For V~N(0,tau^2 I_d), the expectation of the product of generating functions with parameters t and r is
\[
\mathbb E\left[e^{\langle t,V\rangle-\tau^2\|t\|^2/2}
 e^{\langle r,V\rangle-\tau^2\|r\|^2/2}\right]
=e^{\tau^2\langle t,r\rangle}.
\]
Comparing coefficients gives
\[
\mathbb E H_{\tau,\alpha}(V)H_{\tau,\beta}(V)
=\mathbf1_{\{\alpha=\beta\}}\alpha!\tau^{2|\alpha|}.
\]
Therefore, for homogeneous p_k,
\[
\mathbb E[p_k^\sharp(V)^2]=\tau^{2k}\|p_k\|_F^2. \tag{5}
\]
Also, substituting r^2/(2tau^2) in the Gaussian radial integral gives
\[
\mathbb E\|V\|^{2k}
=\tau^{2k}2^k\frac{\Gamma(k+d/2)}{\Gamma(d/2)}. \tag{6}
\]

## 6. Integrated Neuron Norm

The tail assumption for both signs of each coordinate implies finite moments of every coordinate of X, hence E||X||^r<infinity for every positive integer r. Thus all polynomials under consideration belong to L2(D).

For v!=0 let a=sigma_X||v||. For s>=0, tail integration gives
\[
\begin{aligned}
\mathbb E(\langle X,v\rangle-s)_+^2
&=\int_0^\infty\Pr(\langle X,v\rangle>s+\sqrt t)\,dt\\
&\leq\int_0^\infty e^{-(s+\sqrt t)^2/(2a^2)}\,dt\\
&\leq e^{-s^2/(2a^2)}\int_0^\infty e^{-t/(2a^2)}\,dt
=2a^2e^{-s^2/(2a^2)}.
\end{aligned}
\]
Consequently,
\[
\|\operatorname{ReLU}(\langle\cdot,v\rangle-s)\|_{L^2(D)}
\leq\sqrt2\,\sigma_X\|v\|e^{-s^2/(4\sigma_X^2\|v\|^2)}. \tag{7}
\]
For v=0 the neuron is identically zero; this case is handled separately and involves no division by zero. For k>=2, substituting s^2/(4a^2) in the integral of (7) yields
\[
\int_0^\infty s^{k-2}
\|\operatorname{ReLU}(\langle\cdot,v\rangle-s)\|_{L^2(D)}\,ds
\leq2^{k-3/2}(\sigma_X\|v\|)^k\Gamma((k-1)/2). \tag{8}
\]
This also holds at v=0.

Let nu be N(0,tau^2 I_d) times delta_0+Lebesgue measure on [0,infinity). Define
\[
u(v,0)=\frac{2p_1^\sharp(v)}{\tau^2},\qquad
u(v,s)=2\sum_{k=2}^m\frac{s^{k-2}p_k^\sharp(v)}{(k-2)!\tau^{2k}}
\quad(s>0),
\]
where the symbol u in these formulas denotes the scalar coefficient, not the measure nu. Equivalently, write this coefficient as c(v,s) with the displayed values, and put
\[
\phi(x;v,s)=c(v,s)\operatorname{ReLU}(\langle x,v\rangle-s),\qquad
A=\int\|\phi(\cdot;v,s)\|_{L^2(D)}\,\nu(dv,ds).
\]
The s=0 contribution satisfies
\[
\begin{aligned}
A_1
&\leq\frac{2\sqrt2\sigma_X}{\tau^2}
\mathbb E[|p_1(V)|\|V\|]\\
&\leq\frac{2\sqrt2\sigma_X}{\tau^2}
(\tau^2\|p_1\|_F^2)^{1/2}(\tau^2d)^{1/2}
=K_{d,1}\|p_1\|_F.
\end{aligned}
\]
For k>=2, the triangle inequality, (8), Cauchy--Schwarz, (5), and (6) give the kth upper-bound contribution
\[
\begin{aligned}
A_k
&\leq\frac{2^{k-1/2}\sigma_X^k\Gamma((k-1)/2)}{(k-2)!\tau^{2k}}
\mathbb E[|p_k^\sharp(V)|\|V\|^k]\\
&\leq\frac{2^{k-1/2}\sigma_X^k\Gamma((k-1)/2)}{(k-2)!\tau^{2k}}
(\tau^{2k}\|p_k\|_F^2)^{1/2}
\left(\tau^{2k}2^k\frac{\Gamma(k+d/2)}{\Gamma(d/2)}\right)^{1/2}\\
&=K_{d,k}\|p_k\|_F.
\end{aligned}
\]
Thus
\[
A\leq B:=\sum_{k=1}^m K_{d,k}\|p_k\|_F<\infty. \tag{9}
\]
The coefficient c is measurable. The unweighted neuron is continuous as an L2(D)-valued function of (v,s), since ReLU is Lipschitz and E||X||^2<infinity. Thus the integrals above define measurable, integrable L2-valued functions. Equation (9), Fubini, and the pointwise representation imply
\[
\int\phi(\cdot;v,s)\,\nu(dv,ds)=p-p_0
\quad\text{in }L^2(D).
\]
In particular, ||p-p_0||_2<=A<=B, so the asserted square root is real.

## 7. Finite-Width Existence

If A=0, then p-p_0=0 in L2(D); choose the constant network p_n=p_0 with n zero output weights.

Otherwise define
\[
\pi(dv,ds)=\frac{\|\phi(\cdot;v,s)\|_2}{A}\nu(dv,ds).
\]
On its full-measure support define
\[
\psi(\cdot;v,s)=\frac{A\phi(\cdot;v,s)}{\|\phi(\cdot;v,s)\|_2}.
\]
Parameters with zero L2 neuron norm contribute zero to the original Hilbert-space integral. Therefore
\[
\mathbb E_\pi\psi=p-p_0=:f,\qquad
\|\psi\|_2=A\quad\pi\text{-almost surely}.
\]
Take n independent copies psi_i. Expanding the squared Hilbert-space norm, independence and zero mean of psi_i-f eliminate all cross terms, giving
\[
\mathbb E\left\|\frac1n\sum_{i=1}^n\psi_i-f\right\|_2^2
=\frac1n\mathbb E\|\psi-f\|_2^2
=\frac{A^2-\|f\|_2^2}{n}.
\]
Some realization has squared error no greater than this expectation. Each psi_i is a scalar multiple of one ReLU neuron with s_i>=0. Adding p_0 and absorbing 1/n into the output coefficients therefore produces an admissible n-neuron network. By (9),
\[
\|p_n-p\|_2
\leq\frac1{\sqrt n}\sqrt{A^2-\|p-p_0\|_2^2}
\leq\frac1{\sqrt n}\sqrt{B^2-\|p-p_0\|_2^2}
\leq\frac B{\sqrt n}.
\]
This proves both conclusions, including constant polynomials, d=1, n=1, and degenerate input distributions. All theorem-critical obligations are closed.
