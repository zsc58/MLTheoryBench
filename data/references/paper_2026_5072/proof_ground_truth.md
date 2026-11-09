# Reference Proof

## Proof Structure

We construct a two-token attention block with token width six. Its fixed value projection gives an affine immersion, while a fixed projection of the same input tokens supplies a sigmoid gate that converts the output into the required spherical parametrization. We then verify the two Fisher pullback metrics and their intrinsic curvatures.

## Complete Proof

Fix `epsilon` with `0 < epsilon < pi/4` and let `U=(0,epsilon)^2`. This is a nonempty connected open subset of `R^2`. For `phi=(phi_1,phi_2) in U`, define

` s(phi)=(cos(phi_1) cos(phi_2), cos(phi_1) sin(phi_2), sin(phi_1)) `

and

` y(phi)=(2+phi_1,2+phi_2,2). `

All coordinates of `s` are strictly between zero and one on `U`, and every coordinate of `y` is at least two. Consequently,

` r_k(phi)=s_k(phi)/y_k(phi) `

lies in `(0,1)` for each `k=1,2,3`. Define

` z_k(phi)=log(r_k(phi)/(1-r_k(phi))). `

The functions `r_k` and `z_k` are smooth and finite at every point of `U`, and `sigma(z_k)=r_k`.

Use two identical tokens, each with feature vector

` h(phi)=(1,phi_1,phi_2,z_1(phi),z_2(phi),z_3(phi)) in R^6. `

Let `X(phi)` be the `2 x 6` matrix with both rows equal to `h(phi)`. This is a smooth two-dimensional input family; its coordinates containing `phi_1` and `phi_2` also show directly that its Jacobian has rank two.

Choose query/key width one and set the fixed `6 x 1` matrices `W_Q` and `W_K` equal to zero. Fix output position `j=1`. Both attention scores are zero, and hence both softmax weights are `1/2`.

Choose the fixed `6 x 3` value projection whose columns are

` (2,1,0,0,0,0)^T, (2,0,1,0,0,0)^T, (2,0,0,0,0,0)^T. `

Each token value is `y(phi)`, so

` Y(phi)=(1/2)y(phi)+(1/2)y(phi)=y(phi). `

This projection can also be viewed as a value projection followed by the identity output projection.

Take gate-feature width `m=3`. On every input sequence, define `x_g(X)` to select coordinates four through six of its first token. This is a fixed linear, hence differentiable, function of the same input sequence. Along the constructed family it equals `z(phi)`. Choose the fixed gate matrix `W_theta=I_3`, which has rank three. Thus

` Y'(phi)=Y(phi) odot sigma(x_g(X(phi))W_theta)=y(phi) odot r(phi)=s(phi). `

All projections and the gate matrix are independent of `phi`; only the input sequence varies. The construction is therefore a legitimate member of the specified content-aware architecture.

For a Gaussian location family `N(mu,I_3)`, the Fisher information in the mean is `I_3`, so the induced representation metric is `J_mu^T J_mu`. The ungated map is `y(phi)=a+B phi`, with `a=(2,2,2)` and the columns of `B` equal to the first two standard basis vectors of `R^3`. Hence `B` has rank two and

` g_ung=B^T B=I_2. `

The map is an affine embedding onto an open subset of the plane with third coordinate two. Every derivative of its metric coefficients vanishes. The Christoffel formula therefore gives zero connection coefficients, and the curvature tensor, formed from their derivatives and products, also vanishes. In particular, `K_ung=0` throughout `U`.

For the gated map, direct differentiation gives

` s_1=(-sin(phi_1)cos(phi_2),-sin(phi_1)sin(phi_2),cos(phi_1)), `

` s_2=(-cos(phi_1)sin(phi_2),cos(phi_1)cos(phi_2),0). `

Their inner products satisfy

` <s_1,s_1>=1, <s_1,s_2>=0, <s_2,s_2>=cos^2(phi_1). `

Since `cos(phi_1)>0` on `U`, the gated map has rank-two Jacobian everywhere and its Fisher metric is

` g_gat=diag(1,cos^2(phi_1)). `

Moreover, `||s(phi)||=1`. On its image the parameters can be recovered smoothly as

` phi_1=arcsin(s_3), phi_2=arctan(s_2/s_1). `

Here `s_1>0` and the angle ranges lie in `(0,epsilon)`, so these inverse formulas use single smooth branches. The image is the open sphere patch defined by those angle ranges. Thus the gated Gaussian representation manifold is isometric to an open subset of the unit sphere with its induced Euclidean metric.

The standard sphere-curvature fact states that the unit sphere with its induced Euclidean metric has Gaussian curvature one; restriction to an open patch and isometric identification preserve that curvature. Its hypotheses have just been verified, so `K_gat=1` everywhere on `U`.

The same input family and attention projections therefore give an intrinsically flat affine ungated representation and an exactly spherical, strictly positively curved gated representation. All theorem-critical obligations are closed.
