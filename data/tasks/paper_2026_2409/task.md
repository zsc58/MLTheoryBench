# Problem

## Setup

Let \(T>0\) and \(d,m\) be positive integers. Let \(x^*:[0,T]\to\mathbb R^d\) be a continuous, piecewise continuously differentiable solution of a regime-switching ODE with one change point \(\tau\in(0,T)\):
\[
\dot x^*(t)=f(t,x^*(t);\theta^-),\quad t<\tau,
\qquad
\dot x^*(t)=f(t,x^*(t);\theta^+),\quad t>\tau,
\]
where \(\theta^-,\theta^+\in\Theta\subseteq\mathbb R^m\) and \(\theta^-\ne\theta^+\). The equations are understood almost everywhere, and all integrals below use Lebesgue measure. Write \(|A|\) for the measure of a measurable set \(A\), and define \((u)_+=\max\{u,0\}\).

Assume
\[
f(t,x;\theta)=G(t,x)\theta+b(t,x),
\]
where \(G:[0,T]\times\mathbb R^d\to\mathbb R^{d\times m}\) and \(b:[0,T]\times\mathbb R^d\to\mathbb R^d\). For every subinterval \(J\subseteq[0,T]\) of positive length, define the finite matrix
\[
M(J)=\int_JG(t,x^*(t))^\top G(t,x^*(t))\,dt,
\]
and assume \(\lambda_{\min}(M(J))\ge\alpha|J|\) for a fixed \(\alpha>0\). For an interval window \(I\subseteq[0,T]\) of positive length, let \(I^-=I\cap[0,\tau)\) and \(I^+=I\cap(\tau,T]\), and define
\[
R_I(\theta)=\int_I\|\dot x^*(t)-f(t,x^*(t);\theta)\|_2^2\,dt,
\qquad
\underline R_I=\inf_{\theta\in\Theta}R_I(\theta).
\]

Let \(E_+\subseteq(\tau,T]\) be measurable and have positive measure. Fix a finite real exponent \(1\le p_y<\infty\), a differentiable approximate trajectory \(\widehat x:[0,T]\to\mathbb R^d\), and \(\widetilde\theta\in\Theta\). Assume that there is a finite \(L\ge0\) such that, for almost every \(t\in E_+\) and all \(x,z\in\mathbb R^d\),
\[
\|f(t,x;\widetilde\theta)-f(t,z;\widetilde\theta)\|_2\le L\|x-z\|_2.
\]
Assume also that
\[
\|f(\cdot,x^*(\cdot);\theta^+)-f(\cdot,x^*(\cdot);\widetilde\theta)\|_{L^{p_y}(E_+)}
\ge\gamma_+\|\theta^+-\widetilde\theta\|_2
\]
for a finite \(\gamma_+>0\). Here vector-valued \(L^{p_y}\) norms use the Euclidean norm inside the integral. Set
\[
\varepsilon_+=\|\dot{\widehat x}-\dot x^*\|_{L^{p_y}(E_+)}
+L\|\widehat x-x^*\|_{L^{p_y}(E_+)}.
\]
The integrands defining the matrices and residuals are measurable, and the displayed \(L^{p_y}(E_+)\) norms are finite.

Let \(N_{r,+}\) be a positive integer, let \(t_1,\ldots,t_{N_{r,+}}\in E_+\) be collocation points at which the approximate residual is defined, and let \(w_1,\ldots,w_{N_{r,+}}\) be finite positive quadrature weights. Define the weighted discrete residual norm
\[
\mathcal R_{N,+}=\left(\sum_{j=1}^{N_{r,+}}w_j\|\dot{\widehat x}(t_j)-f(t_j,\widehat x(t_j);\widetilde\theta)\|_2^{p_y}\right)^{1/p_y}.
\]
For this trajectory, parameter, set, and quadrature rule, assume the powered quadrature-error bound
\[
\left|\mathcal R_{N,+}^{p_y}-\|\dot{\widehat x}-f(\cdot,\widehat x;\widetilde\theta)\|_{L^{p_y}(E_+)}^{p_y}\right|
\le C_{q,+}N_{r,+}^{-\alpha_q}
\]
with finite \(C_{q,+}\ge0\) and \(\alpha_q>0\). The quadrature exponent \(\alpha_q\) is distinct from the information-matrix constant \(\alpha\).

## Task

Prove the following integrated claim.

1. If \(I\) does not contain \(\tau\), then \(\underline R_I=0\). If \(\tau\in I\) and \(|I^-|,|I^+|>0\), then
\[
\underline R_I\ge
\alpha\frac{|I^-||I^+|}{|I^-|+|I^+|}\|\theta^- -\theta^+\|_2^2
\ge
\frac{\alpha}{2}\min\{|I^-|,|I^+|\}\|\theta^- -\theta^+\|_2^2.
\]

2. The approximate/discrete residual obeys
\[
\mathcal R_{N,+}\ge
\left[
\bigl(\gamma_+\|\theta^+-\widetilde\theta\|_2-\varepsilon_+\bigr)_+^{p_y}
-C_{q,+}N_{r,+}^{-\alpha_q}
\right]_+^{1/p_y}.
\]
In particular, when the hypotheses above hold with \(\widetilde\theta=\theta^-\), this choice makes the lower bound explicitly depend on the regime jump \(\|\theta^+-\theta^-\|_2\).
