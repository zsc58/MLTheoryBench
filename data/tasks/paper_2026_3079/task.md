# Problem

## Setup

Let d be a positive integer, let Omega be a compact subset of R^d, and let F=C(Omega;R) have the uniform norm. Fix 1<=p<=infinity and C_W,C_B>0, and define

\[
W=\{w\in\mathbb R^d:\|w\|_p\le C_W\},\qquad I=[-C_B,C_B],\qquad
B_1=\{x\mapsto w^\top x+b:w\in W,\ b\in I\}.
\]

Choose one of the following activations. Write t_+=max{0,t}, and let Psi be the standard normal cumulative distribution function.

- ReLU: sigma(t)=t_+; or a rectified power sigma(t)=(t_+)^m with fixed m>1.
- Leaky ReLU: sigma(t)=t for t>=0 and sigma(t)=alpha t for t<0, with fixed 0<alpha<1.
- Identity: sigma(t)=t; or absolute value: sigma(t)=|t|.
- GELU: sigma(t)=t Psi(t); SiLU: sigma(t)=t/(1+exp(-t)); or Mish: sigma(t)=t tanh(log(1+exp(t))).
- ELU: sigma(t)=t for t>=0 and sigma(t)=alpha(exp(t)-1) for t<0, with fixed 0<alpha<=1.
- SELU: sigma(t)=kappa t for t>=0 and sigma(t)=kappa alpha(exp(t)-1) for t<0, with fixed positive activation parameters alpha and kappa.
- CELU: sigma(t)=t for t>=0 and sigma(t)=alpha(exp(t/alpha)-1) for t<0, with fixed alpha>0.
- Centered softplus: sigma(t)=log(1+exp(t))-log 2; or bent identity: sigma(t)=t+(sqrt(1+t^2)-1)/2.
- Softsign: sigma(t)=t/(1+|t|); tanh: sigma(t)=tanh(t); centered logistic sigmoid: sigma(t)=1/(1+exp(-t))-1/2; or arctan: sigma(t)=arctan(t).
- Hard tanh: sigma(t)=max{-1,min{1,t}}; or centered hard sigmoid: sigma(t)=max{-1/2,min{1/2,t/6}}.

For s>0, define sigma_s(t)=sigma(st)/s, except for the rectified power of degree m, for which sigma_s(t)=sigma(st)/s^m. Define sigma_0 and sigma_infinity to be the limits as s decreases to zero and increases to infinity, respectively, with convergence uniform on every compact interval of R. These limits exist for the listed activations. Give S=[0,infinity) union {infinity} its one-point compactification topology.

For l>=2, recursively define

\[
B_l=\overline{\operatorname{absconv}}\{\sigma_s\circ g:g\in B_{l-1},\ s>0\},
\]

where closure is in F and absconv consists of finite sums whose sum of absolute coefficients is at most one. Define

\[
\|f\|_{V_l}=\inf\{c>0:f\in cB_l\},\qquad
V_l=\{f\in F:\|f\|_{V_l}<\infty\},
\]

with the infimum of the empty set equal to infinity. Give each B_l its subspace topology from F.

A finite depth-L network with allowed normalized activations means a function of the form

\[
h_{1,k}(x)=\sigma_{s_{1,k}}(w_k^\top x+b_k),\qquad
h_{l,k}(x)=\sigma_{s_{l,k}}\left(\sum_{j=1}^{K_{l-1}}W^{(l)}_{k,j}h_{l-1,j}(x)\right)
\quad(2\le l\le L-1),
\]

\[
f(x)=\sum_{k=1}^{K_{L-1}}a_k h_{L-1,k}(x),
\]

where w_k in W, b_k in I, all coefficients are real, all scales s_{l,k} belong to S, and all widths are finite. An empty expansion represents zero. The hidden levels are indexed from the affine-adjacent innermost level l=1 to the outermost level l=L-1.

Fix integers L>=2 and N>=1, data (x_i,y_i) in Omega times R, a finite-valued loss ell:R times R -> [0,infinity) such that ell(y,.) is lower semicontinuous for every y, and lambda>0. Set

\[
J(f)=\sum_{i=1}^N\ell(y_i,f(x_i))+\lambda\|f\|_{V_L},\qquad f\in V_L.
\]

## Targets

Prove the following integrated theorem.

1. The functions in V_L are exactly the functions admitting the pointwise representation

\[
f(x)=\int_{S\times B_{L-1}}\sigma_s(g(x))\,d\mu(s,g),\qquad x\in\Omega,
\]

for a finite signed Radon measure mu on S times B_{L-1}. Moreover,

\[
\|f\|_{V_L}=\inf\{\|\mu\|_{\mathrm{TV}}:\mu\text{ represents }f\},
\]

where total variation is the mass of the variation measure. For homogeneous activations, the scale coordinate can be removed from both the representation and this infimum.

2. J has a minimizer that is a finite depth-L network with allowed normalized activations and widths

\[
K_l\le N^{L-l},\qquad l=1,\ldots,L-1.
\]

For a nonlinear activation, suppose that the interpolation set {f in V_L:f(x_i)=y_i for every i} is nonempty, with duplicate inputs assigned equal labels. Prove that minimizing ||f||_{V_L} over this set also has a finite depth-L network minimizer with the same width bounds. Nonhomogeneous endpoint activations are allowed in both conclusions.
