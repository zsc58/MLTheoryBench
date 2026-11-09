# Problem

## Setup

Consider a population observation \(y_i=(y_{1i},y_{2i})^T\) and covariates \(x_i\). The covariates are predetermined: they use information available before the outcomes' measurement window or time-invariant attributes, not contemporaneous outcomes, residuals, or post-outcome information. Any data-dependent preprocessing is fitted using training data only. Expectations below are under the population law of \((y_i,x_i)\).

Assume
\[
y_{1i}=\gamma_{10}y_{2i}+f_{10}(x_i)+\varepsilon_{1i},\qquad
y_{2i}=\gamma_{20}y_{1i}+f_{20}(x_i)+\varepsilon_{2i},
\]
where the functions are measurable and finite almost surely, and
\[
E(\varepsilon_i\mid x_i)=0,\qquad
\operatorname{Var}(\varepsilon_i\mid x_i)
=\operatorname{diag}(g_{10}(x_i),g_{20}(x_i)).
\]
For \(k=1,2\), assume \(0<g_{k0}(x_i)<\infty\) almost surely and \(E|\log g_{k0}(x_i)|<\infty\). Conditional moments are taken under the conditional distribution given \(x_i\) and are finite almost surely where used; no unconditional second moment of \(y_i\) is assumed.

Let
\[
\Gamma(\gamma)=\begin{pmatrix}1&-\gamma_1\\-\gamma_2&1\end{pmatrix},\qquad
d(\gamma)=1-\gamma_1\gamma_2,
\]
and \(\gamma_0=(\gamma_{10},\gamma_{20})\). Let \(\mathcal S\) be a compact candidate region containing \(\gamma_0\), with \(|\gamma_k|\leq\bar\gamma<1\) for every \(\gamma\in\mathcal S\) and \(k=1,2\). For local statements, let \(G\) be an open neighborhood of \(\gamma_0\) in \(\mathbb R^2\) on which \(|d(\gamma)|\geq c>0\). The local criterion is defined on \(G\), including when \(\gamma_0\) lies on the boundary of \(\mathcal S\).

Define \(\rho_0(x)=g_{10}(x)/g_{20}(x)\). Assume that there are constants \(0<c_\rho<C_\rho<\infty\) such that
\[
c_\rho\leq\rho_0(x_i)\leq C_\rho\quad\text{almost surely},
\]
and that \(\rho_0(x_i)\) is not almost surely constant.

For finite-dimensional neural nuisance coordinates \(\eta=(\nu_1,\nu_2,\alpha_1,\alpha_2)\), the represented means \(f_k(x;\nu_k)\) are measurable and finite almost surely, and the represented variances \(g_k(x;\alpha_k)\) are measurable, positive, and finite almost surely. All four functions use the same input \(x\). Define
\[
e_{1i}(\gamma,\eta)=y_{1i}-\gamma_1y_{2i}-f_1(x_i;\nu_1),\qquad
e_{2i}(\gamma,\eta)=y_{2i}-\gamma_2y_{1i}-f_2(x_i;\nu_2),
\]
and the unpenalized population criterion
\[
Q(\gamma,\eta)=E\left[\log|d(\gamma)|-\log(2\pi)-\frac12\sum_{k=1}^2\left\{\log g_k(x_i;\alpha_k)+\frac{e_{ki}(\gamma,\eta)^2}{g_k(x_i;\alpha_k)}\right\}\right].
\]
For each \(\gamma\in\mathcal S\cup G\), define
\[
m^*_{\gamma}(x)=E[\Gamma(\gamma)y_i\mid x_i=x],\qquad
r_{\gamma i}=\Gamma(\gamma)y_i-m^*_{\gamma}(x_i),\qquad
v^*_{\gamma,k}(x)=\operatorname{Var}(r_{\gamma,ki}\mid x_i=x).
\]
The unrestricted profile allows arbitrary measurable conditional mean functions and positive conditional variance functions. Fix its additive normalization by setting
\[
Q^*(\gamma)=\log|d(\gamma)|-\log(2\pi)-1
-\frac12E[\log v^*_{\gamma,1}(x_i)+\log v^*_{\gamma,2}(x_i)].
\]

## Local nuisance coordinates

Two nuisance parameters are equivalent if their two mean functions and two variance functions agree almost surely under the distribution of \(x_i\). Let \(\mathcal E_0\) be the equivalence class representing exactly \(f_{10},f_{20},g_{10},g_{20}\), and fix \(\eta_0\in\mathcal E_0\).

Assume \(\mathcal E_0\) is a \(C^2\) embedded manifold locally at \(\eta_0\). Let \(\mathcal K_{\eta_0}\) be its tangent space and define
\[
T_{\eta_0}=\mathcal K_{\eta_0}^{\perp},
\]
using the Euclidean inner product on nuisance coordinates. Norms below are Euclidean. For all sufficiently small \(a\in T_{\eta_0}\), \(\eta_0+a\) is an admissible nuisance parameter. Assume the real-valued function
\[
(\gamma,a)\longmapsto Q(\gamma,\eta_0+a)
\]
is twice continuously differentiable in a neighborhood of \((\gamma_0,0)\) in \(\mathbb R^2\times T_{\eta_0}\).

Assume there is a twice continuously differentiable map \(a^*\), defined for all \(h\) in a neighborhood of zero, with \(a^*(h)\in T_{\eta_0}\) and \(a^*(0)=0\), whose approximation to the unrestricted profiles has the following population-criterion meaning:
\[
Q(\gamma_0+h,\eta_0+a^*(h))-Q^*(\gamma_0+h)=o(\|h\|^2),\qquad h\to0.
\]

Assume the full-coordinate Hessian at the truth exists, and set
\[
J=-\nabla^2Q(\gamma_0,\eta_0)
=\begin{pmatrix}J_{\gamma\gamma}&J_{\gamma\eta}\\J_{\eta\gamma}&J_{\eta\eta}\end{pmatrix}.
\]
Assume \(J_{\eta\eta}\) is symmetric positive semidefinite, with
\[
\ker J_{\eta\eta}=\mathcal K_{\eta_0},\qquad
\mathcal K_{\eta_0}\subseteq\ker J_{\gamma\eta},
\]
and its restriction to \(T_{\eta_0}\) is positive definite. Write \(J_{\eta\eta}^{+}\) for its Moore-Penrose inverse.

For positive \(\delta\) small enough that the slice ball lies in this coordinate neighborhood, define
\[
Q_{\delta,\eta_0}(\gamma)=
\sup_{a\in T_{\eta_0},\ \|a\|<\delta}Q(\gamma,\eta_0+a).
\]

## Task

Prove that \(\gamma_0\) is the unique maximizer of \(Q^*\) over \(\mathcal S\). Moreover, prove that there exists \(\delta_0>0\) such that, for each fixed \(0<\delta<\delta_0\), as \(h\to0\),
\[
Q_{\delta,\eta_0}(\gamma_0+h)-Q_{\delta,\eta_0}(\gamma_0)
=-\tfrac12h^TI_\gamma^*h+o(\|h\|^2),
\qquad
I_\gamma^*=d_0^{-2}\begin{pmatrix}E\rho_0^{-1}&1\\1&E\rho_0\end{pmatrix},
\]
where \(d_0=d(\gamma_0)\).

Conclude that \(I_\gamma^*\) is positive definite, \(\gamma_0\) is a strict local maximizer of the neural profile, and the interaction vector is locally identified on the quotient slice: nearby population maximizers on this slice cannot have a different interaction coordinate. No uniqueness of neural weights is asserted. Also show
\[
J_{\gamma\gamma}-J_{\gamma\eta}J_{\eta\eta}^{+}J_{\eta\gamma}=I_\gamma^*.
\]
