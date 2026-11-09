# Problem

## Model and occupation laws

Let \(T>0\), let \(A\subset\mathbb R\) be compact, let \(\sigma>0\), and let \(m_0\) be a probability measure on \(\mathbb R\) such that \(\int |x|^{\bar p}m_0(dx)<\infty\) for some \(\bar p>2\). Write \(\mathcal P_2(E)\) for probability measures on a metric space \(E\) with finite second moment.

The drift \(b:[0,T]\times\mathbb R\times A\to\mathbb R\) is bounded and measurable, continuous in \((x,a)\) for each fixed \(t\), and Lipschitz in \(x\) uniformly in \((t,a)\). In particular, it does not depend on a population law.

For \(i\in\{0,1\}\), the running and terminal costs are
\[
f_i(t,x,m,a)=\overline f_i\left(t,x,\int_{\mathbb R\times A}\widehat f_i(t,y)m(dy,du),a\right),
\qquad
g_i(x,\nu)=\overline g_i\left(x,\int_{\mathbb R}\widehat g_i(y)\nu(dy)\right),
\]
where \(m\in\mathcal P_2(\mathbb R\times A)\) and \(\nu\in\mathcal P_2(\mathbb R)\). The functions \(\overline f_i\) are measurable and continuous in \((x,z,a)\) for each fixed \(t\), and \(\overline g_i\) are continuous. There is a finite constant \(c\), uniform over the displayed variables and over \(i\), such that
\[
|\overline f_i(t,x,z,a)|\le c(1+|x|^2+|a|^2+|z|^2),\qquad
|\overline g_i(x,z)|\le c(1+|x|^2+|z|^2),
\]
\[
|\overline f_i(t,x,z,a)-\overline f_i(t,x,z',a)|
\le c(1+|x|+|a|+|z|+|z'|)|z-z'|,
\]
\[
|\overline g_i(x,z)-\overline g_i(x,z')|
\le c(1+|x|+|z|+|z'|)|z-z'|.
\]
Each \(\widehat f_i\) belongs to \(C^{1,2}([0,T]\times\mathbb R)\) with bounded first time derivative and bounded first and second spatial derivatives. Each \(\widehat g_i\) is continuous with at most linear growth. Set \(f=f_1\) and \(g=g_1\); the index zero denotes the moderator's costs.

Let \(V_2\) be the space of measurable flows \(m_t\in\mathcal P_2(\mathbb R\times A)\) satisfying
\[
\int_0^T\int |x|^2m_t(dx,da)dt<\infty,
\]
where flows agreeing \(dt\)-almost everywhere are identified. Its topology is convergence of \(\int_0^T\int v(t,x,a)m_t(dx,da)dt\) for every continuous \(v\) satisfying \(|v(t,x,a)|\le C_v(1+|x|^2)\). On terminal laws in \(\mathcal P_2(\mathbb R)\), use convergence against every continuous function of at most quadratic growth.

An occupation pair is \(\boldsymbol m=(m,\overline m)\in V_2\times\mathcal P_2(\mathbb R)\). Let \(\mathcal R\) consist of those pairs satisfying
\[
\int u(T,x)\overline m(dx)-\int u(0,x)m_0(dx)
=\int_0^T\int\left(\partial_tu(t,x)+b(t,x,a)\partial_xu(t,x)+\frac{\sigma^2}{2}\partial_{xx}u(t,x)\right)m_t(dx,da)dt
\]
for every \(u\in C_b^{1,2}([0,T]\times\mathbb R)\), meaning that \(u\) and its displayed derivatives are bounded and continuous. Equip \(\mathcal R\) with the preceding product topology.

A randomized consistent occupation law is a Borel probability measure on \(\mathcal R\). Write \(\mathcal M=\mathcal P(\mathcal R)\), equipped with weak convergence against bounded continuous functions on \(\mathcal R\). An admissible deviation is a fixed pair \(\boldsymbol k=(k,\overline k)\in\mathcal R\); it is chosen independently of the realized occupation pair drawn from \(\rho\).

For \(\rho\in\mathcal M\), define
\[
\Gamma(\rho)=\int_{\mathcal R}\left[\int_0^T\int f(t,x,m_t,a)m_t(dx,da)dt+\int g(x,\overline m)\overline m(dx)\right]\rho(d\boldsymbol m),
\]
\[
\Gamma^{\rm dev}(\rho,\boldsymbol k)=\int_{\mathcal R}\left[\int_0^T\int f(t,x,m_t,a)k_t(dx,da)dt+\int g(x,\overline m)\overline k(dx)\right]\rho(d\boldsymbol m),
\]
\[
\Gamma_0(\rho)=\int_{\mathcal R}\left[\int_0^T\int f_0(t,x,m_t,a)m_t(dx,da)dt+\int g_0(x,\overline m)\overline m(dx)\right]\rho(d\boldsymbol m).
\]
Let
\[
\operatorname{ER}(\rho)=\sup_{\boldsymbol k\in\mathcal R}\bigl(\Gamma(\rho)-\Gamma^{\rm dev}(\rho,\boldsymbol k)\bigr),\qquad
\mathcal E=\{\rho\in\mathcal M:\operatorname{ER}(\rho)\le0\},\qquad
V_{\rm LP}=\inf_{\rho\in\mathcal E}\Gamma_0(\rho).
\]
Assume that there is \(\rho_{\rm s}\in\mathcal M\) with \(\operatorname{ER}(\rho_{\rm s})<0\), and that for every \(\rho\in\mathcal M\) the supremum defining \(\operatorname{ER}(\rho)\) has a unique maximizing deviation.

## Regularizer and iteration

Fix a continuous convex function \(h:\mathcal M\to\mathbb R\) with a bounded jointly continuous flat derivative \(h_\rho:\mathcal M\times\mathcal R\to\mathbb R\). Here this means that for every \(\rho,\rho'\in\mathcal M\),
\[
h(\rho')-h(\rho)=\int_0^1\int_{\mathcal R}h_\rho\bigl(\rho+s(\rho'-\rho),\boldsymbol m\bigr)(\rho'-\rho)(d\boldsymbol m)ds.
\]
Define
\[
D_h(\rho',\rho)=h(\rho')-h(\rho)-\int_{\mathcal R}h_\rho(\rho,\boldsymbol m)(\rho'-\rho)(d\boldsymbol m),
\qquad
L(\rho,\lambda)=\Gamma_0(\rho)+\lambda\operatorname{ER}(\rho),\quad\lambda\ge0.
\]
Fix \(\rho^0\in\mathcal M\) and \(\lambda^0>0\). For each integer \(N\ge1\), run the following iteration afresh from this same initial pair, using the same \(h\), and put \(\eta_N=N^{-1/2}\). Suppressing the dependence of the iterates on the horizon \(N\), set
\[
\rho^{n+1}\in\operatorname*{argmin}_{\rho\in\mathcal M}\left\{L(\rho,\lambda^n)+\frac12D_h(\rho,\rho^n)\right\},
\qquad
\lambda^{n+1}=\left[\lambda^n+\eta_N\operatorname{ER}(\rho^{n+1})\right]_+,
\quad n=0,\ldots,N-1,
\]
where \([z]_+=\max\{z,0\}\). Define
\[
\bar\rho_N=\frac1N\sum_{n=0}^{N-1}\rho^{n+1},\qquad
\bar\lambda_N=\frac1N\sum_{n=0}^{N-1}\lambda^n.
\]

## Task

Prove that the iteration is well-defined and that there are finite constants \(C_{\rm gap},C_{\rm reg},C_{\rm obj}\), depending only on the structural bounds, the fixed regularizer, the initial iterates, and the strict-feasibility margin \(-\operatorname{ER}(\rho_{\rm s})\), but not on \(N\) or \(\Lambda\), such that for every integer \(N\ge1\) and every \(0\le\Lambda<\infty\),
\[
\sup_{\rho\in\mathcal M,\,0\le\lambda\le\Lambda}\left[L(\bar\rho_N,\lambda)-L(\rho,\bar\lambda_N)\right]
\le\frac{C_{\rm gap}(1+\Lambda^2)}{\sqrt N},
\]
\[
\operatorname{ER}(\bar\rho_N)\le\frac{C_{\rm reg}}{\sqrt N},\qquad
\Gamma_0(\bar\rho_N)\le V_{\rm LP}+\frac{C_{\rm obj}}{\sqrt N}.
\]
The claims must hold for every choice of minimizers in the primal updates.

Moreover, prove that there are integers \(N_j\to\infty\) for which \((\bar\rho_{N_j},\bar\lambda_{N_j})\) converges in the product of the weak topology on \(\mathcal M\) and the ordinary topology on \([0,\infty)\), and that every such subsequential limit \((\rho^\infty,\lambda^\infty)\) is a saddle point:
\[
L(\rho^\infty,\lambda)\le L(\rho^\infty,\lambda^\infty)\le L(\rho,\lambda^\infty)
\quad\text{for every }\rho\in\mathcal M,\ \lambda\ge0,
\]
with \(\rho^\infty\in\mathcal E\) and \(\Gamma_0(\rho^\infty)=V_{\rm LP}\).
