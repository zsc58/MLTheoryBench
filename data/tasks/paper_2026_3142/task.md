# Problem

## Setup

Let T be a positive integer. Observations and designs take values in finite-dimensional continuous spaces, with y_t in R^{d_y} and xi_t in R^{d_xi}; densities in observations are with respect to Lebesgue measure. Let phi range over an open domain Phi in R^{d_phi}. Let theta have prior density p(theta), independent of phi.

In a sequential experiment, write h_{t-1}=(y_{1:t-1},xi_{1:t-1}), with h_0 the empty history. Given theta and the available history, an adaptive policy samples xi_t from pi_phi(.|h_{t-1}), and the observation has density p(y_t|theta,xi_t,h_{t-1}). The policy kernel has no additional access to theta, and the observation kernel has no direct dependence on phi beyond realized designs and history.

Use the following likelihood notation, with the designs treated as fixed arguments:
\[
p(y_{1:T}\mid\theta,\xi_{1:T})
:=\prod_{t=1}^T p(y_t\mid\theta,\xi_t,h_{t-1}),\qquad
p(y_{1:T}\mid\xi_{1:T})
:=\int p(\theta)p(y_{1:T}\mid\theta,\xi_{1:T})\,d\theta.
\]
Under adaptive selection, this notation does not mean the ordinary conditional observation density given the entire selected design sequence under the policy. For brevity, write y=y_{1:T} and xi=xi_{1:T}.

Define
\[
I_T(\phi)=\mathbb E\left[\log p(y\mid\theta,\xi)-\log p(y\mid\xi)\right],
\]
where the expectation is over theta from its prior and the sequential experiment just specified.

Assume measurable reparameterization maps with exogenous noise u=(delta,epsilon) having a fixed law q, independent of theta and phi:
\[
y=g^1_{1:T}(u,\theta,\phi),\qquad
\xi=g^2_{1:T}(u,\theta,\phi).
\]
For each theta and phi, the conditional law of these maps under q is the law of the specified sequential experiment given theta. Set z_phi=(y,xi), J_y=partial y/partial phi, and J_xi=partial xi/partial phi. Let D_phi denote total differentiation along this rollout, holding theta and u fixed. At each phi, the rollout maps are differentiable in phi for p(theta)q-almost every realization.

In the deterministic static-design regime, xi is fixed in advance independently of theta and observations. Assume a measurable rollout y=g_stat(delta,theta,xi), where delta has a fixed law q_stat independent of theta and xi, and its conditional law given theta is p(y|theta,xi)dy. Define
\[
I_T(\xi)=\mathbb E_{p(\theta)q_{\rm stat}}\left[\log p(y\mid\theta,\xi)-\log p(y\mid\xi)\right].
\]
Write J_y^{stat}=partial y/partial xi and let D_xi denote total differentiation along this static rollout with theta and delta fixed. Static gradients are evaluated at designs having an open neighborhood on which the densities and static rollout are defined; the static rollout is differentiable in xi almost surely at each such design.

Assume that the log likelihoods are finite and differentiable at the arguments used below, all displayed random quantities are measurable, and all expectations and derivative terms in the task are integrable. Differentiation of the two objective expectations may be interchanged with their respective fixed base laws p(theta)q and p(theta)q_stat. In the static regime, each coordinate derivative in xi may also be interchanged with the observation integral of the normalized marginal density p(y|xi); densities are interpreted on the fixed observation space, and this interchange has no omitted moving-support boundary contribution.

Define
\[
s_y(y,\xi)=\nabla_y\log p(y\mid\xi),\qquad
s_\xi(y,\xi)=\nabla_\xi\log p(y\mid\xi),\qquad
s=(s_y,s_\xi),
\]
where these are partial derivatives with the other argument fixed. Let s_psi=(s_{psi,y},s_{psi,xi}) be a fixed measurable approximating field with the same dimensions.

Fix eta>0 and L>0. Assume that for every latent/noise realization in the support of p(theta)q and every phi,phi' in Phi,
\[
\|z_\phi-z_{\phi'}\|_2\le L\|\phi-\phi'\|_2,
\]
and that for every phi in Phi,
\[
\mathbb E_{p(\theta)q}\left[\|s_\psi(z_\phi)-s(z_\phi)\|_2\right]\le\eta/L.
\]
All vector norms are Euclidean, and Jacobians act on column parameter vectors.

## Task

Prove that for every phi in Phi,
\[
\nabla_\phi I_T(\phi)=\mathbb E_{p(\theta)q}\left[
D_\phi\log p(y\mid\theta,\xi)-J_y^\top s_y(y,\xi)-J_\xi^\top s_\xi(y,\xi)
\right].
\]
In the deterministic static-design regime, prove
\[
\nabla_\xi I_T(\xi)=\mathbb E_{p(\theta)q_{\rm stat}}\left[
D_\xi\log p(y\mid\theta,\xi)-(J_y^{\rm stat})^\top s_y(y,\xi)
\right].
\]
Finally, let widehat G_psi(phi) be the population expectation obtained by replacing (s_y,s_xi) in the adaptive formula with (s_{psi,y},s_{psi,xi}), while retaining the exact conditional log-likelihood term. It is not a finite-sample Monte Carlo realization. Prove uniformly for every phi in Phi that
\[
\left\|\nabla_\phi I_T(\phi)-\widehat G_\psi(\phi)\right\|_2\le\eta.
\]
