# Problem

## Setup

Let \(L\geq1\) and \(n_0,n_1,\ldots,n_L\) be positive integers, and put \(n_{L+1}=1\). Let \(f_\theta:\mathbb R^{n_0}\to\mathbb R\) be a feed-forward ReLU network with finite real parameters
\[
\theta=\{W^{(l)},b^{(l)}\}_{l=1}^{L+1},\qquad
W^{(l)}\in\mathbb R^{n_l\times n_{l-1}},\quad b^{(l)}\in\mathbb R^{n_l}.
\]
Its forward evaluation is
\[
z^{(l)}=W^{(l)}\hat x^{(l-1)}+b^{(l)}\quad(1\leq l\leq L+1),\qquad
\hat x^{(l)}=\max\{0,z^{(l)}\}\quad(1\leq l\leq L),
\]
with \(\hat x^{(0)}=x\) and scalar affine output \(f_\theta(x)=z^{(L+1)}\). All vector maxima are componentwise.

Fix finite vectors \(x^{lb}\leq x^{ub}\), the box \(\mathcal X=\{x:x^{lb}\leq x\leq x^{ub}\}\), a finite nonempty index set \(B\), and fixed inputs \(x_i\in\mathcal X\) for \(i\in B\). These objects do not vary with \(\theta\).

For a vector or matrix, define \([v]^+=\max\{v,0\}\) and \([v]^-=\min\{v,0\}\) componentwise. For every hidden neuron, interval bound propagation is
\[
L_j^{(l)}=[W_j^{(l)}]^+\ell^{(l-1)}+[W_j^{(l)}]^-u^{(l-1)}+b_j^{(l)},\qquad
U_j^{(l)}=[W_j^{(l)}]^+u^{(l-1)}+[W_j^{(l)}]^-\ell^{(l-1)}+b_j^{(l)},
\]
with
\[
\ell_j^{(l)}=\max\{L_j^{(l)},0\},\qquad
u_j^{(l)}=\max\{U_j^{(l)},0\},\qquad
\ell^{(0)}=x^{lb},\quad u^{(0)}=x^{ub}.
\]
In this display, the upper postactivation bound is denoted by \(u_j^{(l)}\); thus the second formula reads \(u_j^{(l)}=\max\{U_j^{(l)},0\}\).

For sample \(x_i\), define the continuous relaxation using real variables \(z^{(l)},\hat x^{(l)},a^{(l)}\), the affine equalities
\[
\hat x^{(0)}=x_i,\qquad
z^{(l)}=W^{(l)}\hat x^{(l-1)}+b^{(l)}\quad(1\leq l\leq L+1),
\]
and, for each hidden neuron, the inequalities
\[
\hat x_j^{(l)}\geq z_j^{(l)},\quad
\hat x_j^{(l)}\geq0,\quad
\hat x_j^{(l)}\leq z_j^{(l)}-L_j^{(l)}(1-a_j^{(l)}),\quad
\hat x_j^{(l)}\leq U_j^{(l)}a_j^{(l)},\quad
0\leq a_j^{(l)}\leq1.
\]
Exact hidden-layer ReLU equalities are not imposed in this relaxation. Let \(V_i(\theta)\) be its minimum of \(z^{(L+1)}\), define \(\delta_i=f_\theta(x_i)-V_i(\theta)\), and set
\[
R_{LP}=\frac1{|B|}\sum_{i\in B}\delta_i,\qquad
R_{BW}=\frac1{N_h}\sum_{l=1}^L\sum_{j=1}^{n_l}(U_j^{(l)}-L_j^{(l)}),\qquad
N_h=\sum_{l=1}^L n_l.
\]

When taking partial derivatives with respect to bound entries or differentiating with the bounds fixed, regard the entries appearing in the LP as independent arguments, while the forward network output remains independent of those arguments. Evaluate these partial derivatives at the current IBP bounds. Let \(D_{\rm fix}\) denote differentiation with respect to \(\theta\) in this independent-argument representation, holding all bound entries fixed. Assume each LP optimum has a unique nondegenerate optimal basis and parameter-independent variable bounds, and that this optimal basis is locally constant in the joint independent-argument parameterization by \(\theta,L,U\).

Use ordinary gradients at points where the fixed-input forward outputs and IBP bounds are differentiable. At a kink, a displayed identity is interpreted by taking every term along the same sequence of differentiability points approaching the parameter value within a common smooth branch, with the resulting finite limits. Convex combinations are allowed only by combining complete matched identities with the same weights in every term; independently selected component subgradients are not asserted to satisfy the identities. Fix a real scalar \(\alpha\), independent of \(\theta\).

## Task

Prove the following integrated theorem. The exact total derivative decomposes as
\[
\nabla_\theta R_{LP}=D_{\rm fix}R_{LP}+\frac1{|B|}\sum_{i\in B}\sum_{l=1}^L\sum_{j=1}^{n_l}\left(\frac{\partial\delta_i}{\partial L_j^{(l)}}\nabla_\theta L_j^{(l)}+\frac{\partial\delta_i}{\partial U_j^{(l)}}\nabla_\theta U_j^{(l)}\right).
\]
Moreover, if
\[
\nabla^{\rm sur}_\theta(R_{LP}+\alpha R_{BW}):=D_{\rm fix}R_{LP}+\alpha\nabla_\theta R_{BW},
\]
then
\[
\nabla^{\rm sur}_\theta(R_{LP}+\alpha R_{BW})
=D_{\rm fix}R_{LP}+\frac{\alpha}{N_h}\sum_{l=1}^L\sum_{j=1}^{n_l}(\nabla_\theta U_j^{(l)}-\nabla_\theta L_j^{(l)}).
\]
Thus the surrogate replaces the batch-averaged exact LP-gap sensitivity coefficients of the indirect bound channel by uniform weights \(-\alpha/N_h\) and \(+\alpha/N_h\), respectively. This is a statement about the defined surrogate, not the ordinary total gradient of the combined numerical regularizer; no quantitative approximation-error bound is asserted.
