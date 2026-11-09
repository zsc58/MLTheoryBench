# Problem

## Setup

All vectors are real row vectors. For positive integers `n,p,d,m`, let an input sequence be a matrix `X in R^{n x p}` with token rows `x_1,...,x_n`. A single-head content-aware attention block has fixed projection matrices

` W_Q,W_K in R^{p x d}, W_V in R^{p x 3}. `

At a fixed position `j in {1,...,n}`, its attention weights, values, and output are

` alpha_i(X)=exp((x_j W_Q)(x_i W_K)^T) / sum_{ell=1}^n exp((x_j W_Q)(x_ell W_K)^T), `

` u_i(X)=x_i W_V, Y(X)=sum_{i=1}^n alpha_i(X)u_i(X). `

The matrix `W_V` may include a composed value and output projection.

A multiplicatively gated version has

` Y'(X)=Y(X) odot sigma(x_g(X)W_theta), `

where `x_g` is a differentiable function of the input sequence, defined on an open neighborhood of the input family and taking values in `R^m`, and `W_theta in R^{m x 3}` is a fixed matrix of rank three. Here `odot` is coordinatewise multiplication and `sigma(t)=1/(1+e^{-t})` acts coordinatewise. The same input sequence and attention projections are used for `Y` and `Y'`.

For a fixed-covariance Gaussian location family `N(mu,Sigma)`, with positive-definite covariance `Sigma`, the Fisher information in the location parameter is `Sigma^{-1}`. Thus a smooth immersion `mu(phi)` induces the metric `J_mu(phi)^T Sigma^{-1} J_mu(phi)`, where `J_mu` is its Jacobian. In this problem take `Sigma=I_3` and equip each Gaussian representation manifold `{N(mu(phi),I_3): phi in U}` with this metric.

## Task

Prove that there exist dimensions `n,p,d,m`, a fixed output position `j`, attention projections, a gate feature map `x_g`, a gate matrix `W_theta` as specified above, a nonempty connected open set `U in R^2`, and a smooth input family `X:U -> R^{n x p}` such that the following hold throughout `U`:

- The ungated map `phi -> Y(X(phi))` is an affine immersion whose Gaussian representation manifold has Gaussian curvature `0`.
- The gated map is

  ` Y'(X(phi))=s(phi_1,phi_2)=(cos(phi_1) cos(phi_2), cos(phi_1) sin(phi_2), sin(phi_1)), `

  parametrizes a smooth open patch of the unit sphere, and has a Gaussian representation manifold of Gaussian curvature `1` everywhere.

Conclude that multiplicative gating yields a strictly positively curved representation manifold although the corresponding ungated realization is intrinsically flat.
