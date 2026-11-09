# Problem

## Setup

Let \(D\ge 1\), and write each coordinate of
\(x\in(\mathbb C\setminus\{0\})^D\) as
\[
x_j=r_j e^{i\theta_j},\qquad r_j>0,
\quad \theta_j\in[-\pi,\pi).
\]
Consider the energy
\[
\mathcal E(x)=-\frac12x^HQx-\operatorname{Re}(h^Hx)
-\frac12\log|x|^TA\log|x|-\eta^T\log|x|,
\]
where \(Q\in\mathbb C^{D\times D}\) is Hermitian, \(h\in\mathbb C^D\), \(A\in\mathbb R^{D\times D}\) is symmetric with zero diagonal, and \(\eta\in\mathbb R^D\). Assume
\[
Q_{jj}=-2\beta_j,
\qquad \beta_j>0.
\]
The vector \(\log|x|\) is defined componentwise. Holding all other coordinates fixed, the conditional kernel for one complex coordinate is \(e^{-\mathcal E(x)}\) with respect to planar Lebesgue measure.

Fix \(d\) and a value of \(x_{-d}\). Define
\[
\alpha_d=1+\frac12\left(A_{-d,d}^{T}\log|x_{-d}|+\eta_d\right)>0,
\qquad
g_d=Q_{-d,d}^{H}x_{-d}+h_d=a_de^{i\phi_d},
\]
where \(a_d=|g_d|\); if \(a_d=0\), choose \(\phi_d\) arbitrarily.

Write \(\Gamma\) for the gamma function, \({}_1F_1\) for the confluent hypergeometric function of the first kind, and \(I_0\) for the modified Bessel function of the first kind of order zero.

For \(\gamma>0\), \(m\in\mathbb C\), and \(s^2>0\), define
\[
q_{\gamma,m,s^2}(z)=
\frac{|z|^{2\gamma-2}\exp(-|z-m|^2/s^2)}
{\pi(s^2)^\gamma\Gamma(\gamma)
L_{\gamma-1}(-|m|^2/s^2)},
\qquad z\in\mathbb C\setminus\{0\},
\]
where \(L_\rho(t)={}_1F_1(-\rho;1;t)\). Also define
\[
\operatorname{VM}(\theta;\phi,\kappa)
=\frac{e^{\kappa\cos(\theta-\phi)}}{2\pi I_0(\kappa)},
\qquad \kappa\ge0.
\]

## Task

Prove the following integrated characterization. With
\[
m_d=\frac{g_d}{2\beta_d},
\qquad s_d^2=\frac1{\beta_d},
\qquad \nu_d=|m_d|,
\]
the conditional density of \(x_d\) given \(x_{-d}\), with respect to planar Lebesgue measure, is
\[
x_d\mid x_{-d}\sim q_{\alpha_d,m_d,s_d^2}.
\]
Moreover, conditional on \(R_d=|x_d|=r\), its phase satisfies
\[
\theta_d\mid(R_d=r,x_{-d})
\sim \operatorname{VM}(\phi_d,a_dr),
\]
and its magnitude has density
\[
p_{R_d\mid x_{-d}}(r)=
\frac{2r^{2\alpha_d-1}
\exp(-(r^2+\nu_d^2)/s_d^2)
I_0(2\nu_dr/s_d^2)}
{(s_d^2)^{\alpha_d}\Gamma(\alpha_d)
L_{\alpha_d-1}(-\nu_d^2/s_d^2)},
\qquad r>0.
\]
