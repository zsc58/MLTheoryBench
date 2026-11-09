# Problem

## Setup

Fix positive integer input and output dimensions and a depth-D linear network with D>=2 and fixed positive integer hidden widths. Let x in R^{d_x} and y in R^{d_y} satisfy
\[
y=Vx+\varepsilon,
\]
where \(\mathbb E x=\mathbb E\varepsilon=0\), \(x\) and \(\varepsilon\) are independent, and their finite positive-definite covariance matrices are
\[
\Sigma_x=\mathbb E[xx^\top],\qquad
\Sigma_\varepsilon=\mathbb E[\varepsilon\varepsilon^\top].
\]
The network and per-example loss are
\[
f_\theta(x)=W_D\cdots W_1x,\qquad
\ell(x,y,\theta)=\tfrac12\|y-f_\theta(x)\|^2.
\]
All entries of all weight matrices are trainable, and parameter space has its usual Euclidean inner product, equivalently the sum of the layer Frobenius inner products. Every hidden width is at least
\[
r=\operatorname{rank}(\Sigma_\varepsilon^{1/2}V\Sigma_x^{1/2}).
\]
Let \(L(\theta)=\mathbb E\ell(x,y,\theta)\). Define the expected Hessian and its sharpness by
\[
H(\theta)=\mathbb E[\nabla_\theta^2\ell(x,y,\theta)],\qquad
T(\theta)=\operatorname{Tr}H(\theta).
\]

Fix an integer batch size \(m\ge1\). Each batch \(B=(z_1,\ldots,z_m)\), with \(z_i=(x_i,y_i)\), consists of m iid draws from the data distribution. Set
\[
S(\theta)=\mathbb E_B\left\|\frac1m\sum_{i=1}^m\nabla_\theta\ell(z_i,\theta)\right\|^2,
\qquad
F_\eta(\theta)=L(\theta)+\frac\eta4 S(\theta),\quad \eta>0.
\]
The nonnegative expectation defining S is interpreted in \([0,+\infty]\); global minimization of \(F_\eta\) uses this extended-real convention.

Call \(\bar\theta\) an entropic-SGD selected point if there exist \(\eta_n\downarrow0\) and global minimizers \(\theta_n\in\arg\min_\theta F_{\eta_n}(\theta)\) such that \(\theta_n\to\bar\theta\) in parameter space. Claims about selected points concern such limits, not arbitrary finite-learning-rate minimizers or arbitrary SGD trajectories.

Write thin SVDs
\[
\Sigma_\varepsilon^{1/2}V\Sigma_x^{1/2}=L\,\mathsf S\,R^\top,
\qquad
V\Sigma_x^{1/2}=\widehat L\,\widehat{\mathsf S}\,\widehat R^\top,
\]
and denote
\[
G=\operatorname{Tr}\mathsf S,\qquad
C=\operatorname{Tr}\Sigma_x,\qquad
E=\operatorname{Tr}\Sigma_\varepsilon.
\]
For rank zero, the thin SVDs have no columns and their singular-value traces are zero.

## Task

Prove that every entropic-SGD selected point is a global minimizer of the population loss L, that the expected Hessians at any two selected points are orthogonally similar, and that their sharpness is
\[
T_{\mathrm{sel}}=(D-1)G^{(D-2)/D}(EC)^{1/D}\operatorname{Tr}(\Sigma_\varepsilon^{-1}L\mathsf S L^\top)
+d_y\frac{G^{2(D-1)/D}C^{1/D}}{E^{(D-1)/D}}.
\]
When G=0, the displayed expression is defined to be zero, including when D=2. Thus the complete expected-Hessian spectrum is independent of the selected point within the fixed architecture.

Moreover, prove that among all global minimizers of the population loss L, the minimum achievable sharpness is
\[
T_{\min}=D\bigl(\operatorname{Tr}\widehat{\mathsf S}\bigr)^{2(D-1)/D}\bigl(d_y\operatorname{Tr}\Sigma_x\bigr)^{1/D}.
\]
Exhibit SVD-aligned factors with suitable layer scalings that attain this minimum; when V=0, include an attaining factorization as well.
