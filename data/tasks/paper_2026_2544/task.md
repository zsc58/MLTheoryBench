# Problem

## Setup

Let \(d\ge1\). A convex body is a compact convex set \(K\subset\mathbb R^d\) with nonempty interior and \(0\in\operatorname{int}K\); let \(\mathcal K\) denote this class. For \(K\in\mathcal K\), define its gauge and support functions by
\[
 g_K(u)=\inf\{\lambda\ge0:u\in\lambda K\},\qquad h_K(u)=\sup_{y\in K}y\cdot u.
\]
Let \(d_H\) be Hausdorff distance. For an integer \(m\ge1\), \(W\in\mathbb R^{d\times m}\), and \(\beta>0\), write
\[
 \operatorname{LSE}(z)=\log\sum_{i=1}^m e^{z_i}\quad(z\in\mathbb R^m),
\]
and define
\[
 p_\theta(0)=0,\qquad p_\theta(x)=\beta\|x\|\,\operatorname{LSE}\!\left(W^\top x/\|x\|\right)\quad(x\ne0),
\]
where \(\theta=(\beta,W,m)\). Define the gauge-generated set
\[
 \Omega_\theta^g=\{y:p_\theta(y)\le1\},
\]
and, when \(p_\theta\) is positive on the unit sphere, define the support-gradient image
\[
 \Omega_\theta^s=\{0\}\cup\{\|x\|\nabla p_\theta(x):0<\|x\|\le1\}.
\]

## Task

Prove that every \(p_\theta\) is sublinear and \(C^\infty\) on \(\mathbb R^d\setminus\{0\}\). Moreover, for every \(K\in\mathcal K\) and every \(\varepsilon>0\), there are parameters \(\theta_g\) and \(\theta_s\) (with the corresponding functions positive on the sphere) such that \(\Omega_{\theta_g}^g,\Omega_{\theta_s}^s\in\mathcal K\) and
\[
 d_H(K,\Omega_{\theta_g}^g)<\varepsilon,\qquad d_H(K,\Omega_{\theta_s}^s)<\varepsilon.
\]
