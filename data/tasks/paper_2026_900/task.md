# Problem

## Setup

Let \(\sigma>0\), \(\mu\in\mathbb R\), \(\rho>\max\{0,\mu\}\), \(\kappa>0\), and \(\lambda>0\). On a complete probability space let \(W\) be a one-dimensional Brownian motion, and let \(\mathbb F^W\) be its natural filtration with the usual augmentation. Let
\[
dX_t^x=\mu X_t^x\,dt+\sigma X_t^x\,dW_t,\qquad X_0^x=x>0.
\]
Let \(\pi:[0,\infty)\to\mathbb R\) be continuous, twice continuously differentiable on \((0,\infty)\), nondecreasing and concave, with \(\pi(0)=0\). Assume that \(x\pi'(x)\) is strictly increasing on \((0,\infty)\) and that
\[
|\pi(x)|\le c(1+x^\theta)
\]
for some \(c>0\) and \(\theta\in(0,1)\). Define
\[
H(x)=\mathbb E\!\left[\int_0^\infty e^{-\rho t}\pi(X_t^x)\,dt\right],
\qquad
\mathcal Lf=\tfrac12\sigma^2x^2f''+\mu xf'.
\]

For initial fuel \(y\in[0,1]\), an admissible control is an \(\mathbb F^W\)-adapted, nondecreasing, cadlag process \(\xi\) with \(0\le\xi_t\le y\) and \(\xi_{0-}=0\). Put \(Y_t=y-\xi_t\) and
\[
J^\lambda(x,y;\xi)=\mathbb E\!\left[\int_0^\infty e^{-\rho t}\Big((\pi(X_t^x)-\rho\kappa)Y_t-\lambda Y_t\log Y_t\Big)\,dt\right],
\qquad
V^\lambda(x,y)=\sup_\xi J^\lambda(x,y;\xi),
\]
where \(0\log0:=0\).

The classical stopping problem is
\[
V^0(x)=\sup_\tau\mathbb E\!\left[\int_0^\tau e^{-\rho t}(\pi(X_t^x)-\rho\kappa)\,dt\right],
\]
where \(\tau\) ranges over \(\mathbb F^W\)-stopping times with values in \([0,\infty]\). A lower hitting threshold for this problem means a number \(b>0\) such that \(\inf\{t\ge0:X_t^x\le b\}\) is optimal for every \(x>0\), with \(\inf\varnothing=\infty\).

Let \(\alpha_-<0<1<\alpha_+\) be the roots of
\[
\tfrac12\sigma^2\alpha(\alpha-1)+\mu\alpha-\rho=0.
\]

## Task

For \(x>0\), define
\[
g_\lambda(x)=\left[\exp\!\left(\frac{-xH'(x)/\alpha_-+H(x)-\kappa-\lambda/\rho}{\lambda/\rho}\right)\right]\wedge1,
\qquad
y_\lambda=e^{-1-\kappa\rho/\lambda},
\]
and set \(g_\lambda(0)=y_\lambda\). Let
\[
\widehat x_\lambda=\inf\{x\ge0:g_\lambda(x)=1\}.
\]
Prove that this cap point is finite and that \(g_\lambda\) is continuous and strictly increasing on \([0,\widehat x_\lambda]\). Let \(b_\lambda:[y_\lambda,1]\to[0,\widehat x_\lambda]\) be the inverse of this restriction; in particular, \(b_\lambda(y_\lambda)=0\) and \(b_\lambda(1)=\widehat x_\lambda\).

For \(y\in[y_\lambda,1]\), define
\[
A_2(y)=\int_{y_\lambda}^{y}\frac{\kappa+(\lambda/\rho)\log u+\lambda/\rho-H(b_\lambda(u))}{b_\lambda(u)^{\alpha_-}}\,du,
\]
where the integral at its lower endpoint is interpreted as an improper integral and \(A_2(y_\lambda)=0\). Define, for \(x>0\) and \(y\in[y_\lambda,1]\),
\[
F(x,y)=A_2(y)x^{\alpha_-}+H(x)y-\kappa y-\frac\lambda\rho y\log y.
\]
Prove that these quantities are well defined and that, for every \(x>0\) and \(y\in[0,1]\),
\[
V^\lambda(x,y)=
\begin{cases}
H(x)y-\kappa y-(\lambda/\rho)y\log y,&0\le y<y_\lambda,\\
F(x,y),&y_\lambda\le y\le g_\lambda(x),\\
F(x,g_\lambda(x)),&y>g_\lambda(x),
\end{cases}
\]
with optimal control
\[
\xi_t^\lambda=\sup_{0\le s\le t}\big(y-g_\lambda(X_s^x)\big)^+,\qquad t\ge0,
\qquad \xi_{0-}^\lambda=0.
\]

Moreover, prove that the unique positive solution \(b_*\) of
\[
\frac{b_*H'(b_*)}{-\alpha_-}+H(b_*)=\kappa
\]
is a lower hitting threshold for the classical stopping problem, and that for every fixed \(y\in(0,1]\),
\[
b_\lambda(y)\longrightarrow b_*\qquad(\lambda\downarrow0).
\]
This limit uses \(b_\lambda(y)\) for sufficiently small \(\lambda>0\), when \(y\in[y_\lambda,1]\).
