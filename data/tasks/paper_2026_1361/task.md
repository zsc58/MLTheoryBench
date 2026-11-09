# Problem

## Setup

Let \(d,m\) be positive integers, \(\lambda>0\), and \(\eta\geq0\). Let \(\mathcal P_2(\mathbb R^d)\) be the Borel probability measures with finite second moment. For two such measures, let \(\Gamma(\mu,\nu)\) denote their couplings and define
\[
W_2^2(\mu,\nu)=\inf_{\gamma\in\Gamma(\mu,\nu)}\int|x-y|^2\,\gamma(dx,dy).
\]
All vector norms are Euclidean and matrix norms below are operator norms.

Let \(U\in C^2(\mathbb R^d)\). Assume that there are finite constants \(K_U\), \(\kappa>0\), \(a_U>0\), and \(b_U\in\mathbb R\) such that, for every \(x\),
\[
\kappa I\preceq\nabla^2U(x)\preceq K_UI,
\qquad U(x)\geq a_U|x|^2+b_U.
\]
Set \(Z_U=\int e^{-U(x)}dx\) and \(\pi(dx)=Z_U^{-1}e^{-U(x)}dx\).

Let \(H:(\mathbb R^d)^m\to\mathbb R\) be permutation invariant and \(C^2\). Assume finite nonnegative constants \(C_H,L_H\) and an exponent \(\varepsilon\in(0,2]\) such that, for every \(x_{1:m}\) and every \(j\),
\[
|H(x_{1:m})|\leq C_H\left(1+\sum_{j=1}^m|x_j|^{2-\varepsilon}\right),
\]
\[
|\nabla_jH(x_{1:m})|\leq C_H\left(1+\sum_{\ell=1}^m|x_\ell|\right),
\qquad \|\nabla^2H(x_{1:m})\|_{\mathrm{op}}\leq L_H.
\]
The Hessian here is the full \(md\)-dimensional Hessian. When \(\varepsilon=2\), interpret \(|x|^0\) as \(1\), including at zero.

Let \(q:\mathbb R^d\to\mathbb R\) be even and \(C^2\). Assume finite nonnegative constants \(C_q,L_q\) and \(q_{\min}\in\mathbb R\) such that
\[
|q(z)|\leq C_q(1+|z|^2),\qquad q(z)\geq q_{\min},\qquad
\|\nabla^2q(z)\|_{\mathrm{op}}\leq L_q
\]
for every \(z\). Assume
\[
\alpha:=\lambda\kappa-mL_H-\eta L_q>0.
\]

For \(\mu\in\mathcal P_2\), define
\[
\mathcal J(\mu)=\int H(x_1,\ldots,x_m)\,\mu^{\otimes m}(dx_{1:m}),
\]
\[
A(x;\mu)=\int H(x,x_2,\ldots,x_m)\,\mu^{\otimes(m-1)}(dx_{2:m}),
\]
\[
\mathcal R(\mu)=\frac12\iint q(x-y)\,\mu(dx)\mu(dy),
\qquad B(x;\mu)=\int q(x-y)\,\mu(dy).
\]
For \(m=1\), the empty-product integral means \(A(x;\mu)=H(x)\). Define
\[
\operatorname{KL}(\mu\|\pi)=\int\log\frac{d\mu}{d\pi}\,d\mu
\]
when \(\mu\ll\pi\), and set it to \(+\infty\) otherwise. Set
\[
\mathcal E(\mu)=-\mathcal J(\mu)+\eta\mathcal R(\mu)+\lambda\operatorname{KL}(\mu\|\pi).
\]
Fix the constant
\[
L_\mu:=mL_H\sqrt{m-1}+\eta L_q,
\qquad\delta:=\alpha-L_\mu,
\]
and assume \(\delta>0\). Gradients of \(A\) and \(B\) are taken in their spatial argument.

The notation \(\delta\mathcal E/\delta\mu\) denotes a linear first variation, determined up to an additive spatial constant: its integral against a zero-mass perturbation equals the directional derivative of \(\mathcal E\), whenever that derivative exists.

## Regular-Density Qualification

The gradient-flow identification and energy identity below concern regular decaying solutions. Here this means \(\mu_t=p_t\,dx\), with \(p_t>0\), \(p\) continuously differentiable in time and twice continuously differentiable in space for \(t>0\), and finite \(\operatorname{KL}(\mu_t\|\pi)\). Require, for every compact time interval \(I\subset(0,\infty)\),
\[
\int_{\mathbb R^d}\sup_{t\in I}\left[(1+|x|^2)(p_t+|\partial_tp_t|)+|\log p_t|\,|\partial_tp_t|+\frac{|\nabla p_t|^2}{p_t}\right]dx<\infty,
\]
and
\[
\lim_{R\to\infty}\sup_{t\in I}\int_{\partial B_R}(1+R^2+|\log p_t|)\left(|\nabla p_t|+(1+R)p_t\right)dS=0.
\]
Here \(B_R=\{x:|x|<R\}\), and \(dS\) is surface measure. These qualifications apply only to the regular-density assertions, not to the other conclusions or to arbitrary initial laws.

## Task

Prove that \(\mathcal E\) has a unique minimizer \(\mu^*\in\mathcal P_2(\mathbb R^d)\), and that it is the unique solution in this space of the nonlinear Gibbs equation
\[
\mu^*(dx)=\frac1Z\exp\!\left(\frac{mA(x;\mu^*)-\eta B(x;\mu^*)}{\lambda}\right)\pi(dx),\qquad 0<Z<\infty.
\]

With
\[
b(x,\mu)=m\nabla A(x;\mu)-\eta\nabla B(x;\mu)-\lambda\nabla U(x),
\]
show that for every \(\mu_0\in\mathcal P_2\), the McKean-Vlasov SDE
\[
dX_t=b(X_t,\mu_t)\,dt+\sqrt{2\lambda}\,dW_t,
\qquad\mu_t=\operatorname{Law}(X_t),
\]
has a unique global strong solution. The standard strong-solution interpretation is used: on a filtered probability space carrying a standard \(d\)-dimensional Brownian motion \(W\) and an \(\mathcal F_0\)-measurable \(X_0\) of law \(\mu_0\), independent of \(W\), existence holds and uniqueness is pathwise for the same \(X_0,W\).

Show that its law has finite second moments, is continuous in \(W_2\), and solves
\[
\partial_t\mu_t=\lambda\Delta\mu_t-\nabla\cdot\bigl(b(\cdot,\mu_t)\mu_t\bigr)
\]
weakly. Explicitly, for every \(\varphi\in C_c^\infty(\mathbb R^d)\) and \(t\geq0\), prove
\[
\int\varphi\,d\mu_t=\int\varphi\,d\mu_0+
\int_0^t\int\bigl(\nabla\varphi(x)\cdot b(x,\mu_s)+\lambda\Delta\varphi(x)\bigr)\,\mu_s(dx)\,ds.
\]

For regular decaying solutions in the sense specified above, identify this equation as the Wasserstein gradient-flow equation of \(\mathcal E\), in the continuity-equation sense with velocity \(-\nabla(\delta\mathcal E/\delta\mu)\), and prove, for almost every \(t>0\),
\[
\frac d{dt}\mathcal E(\mu_t)=-\int\left|\nabla\frac{\delta\mathcal E}{\delta\mu}(x)\right|^2\,\mu_t(dx)\leq0.
\]
Show separately that \(\mu^*\) is a stationary weak solution and that starting the SDE from \(\mu^*\) preserves its law.

Finally, prove that any two solution laws satisfy, for every \(t\geq0\),
\[
W_2(\mu_t,\widetilde\mu_t)\leq e^{-\delta t}W_2(\mu_0,\widetilde\mu_0),
\]
so every solution converges exponentially to \(\mu^*\).
