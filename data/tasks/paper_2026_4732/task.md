# Problem

## Setup

Let `X=(x_1,\ldots,x_n)` be a fixed finite training list in `\mathbb R^d`, let `Y\in\mathbb R^n` be fixed labels, and let `Z=(z_1,\ldots,z_m)` be any fixed finite test list in `\mathbb R^d`. Fix an integer `L\geq1`, a Lipschitz function `\phi:\mathbb R\to\mathbb R`, and finite nonnegative constants `\sigma_w,\sigma_b`.

For widths `r_0=d`, `r_L=1`, and hidden widths `r_1,\ldots,r_{L-1}`, define a fully connected scalar-output network by
\[
v^0(x)=x,\qquad
 a^\ell(x)=\sigma_b b^\ell+
 \frac{\sigma_w}{\sqrt{r_{\ell-1}}}W^\ell v^{\ell-1}(x)
 \quad(1\leq\ell\leq L),
\]
\[
v^\ell(x)=\phi(a^\ell(x))\quad(1\leq\ell<L),
\qquad u_r(x;\vartheta)=a^L_1(x),
\]
where `\phi` is applied componentwise, `W^\ell\in\mathbb R^{r_\ell\times r_{\ell-1}}`, and `b^\ell\in\mathbb R^{r_\ell}`. Thus the final layer has no output activation or additional fixed offset. The parameter vector `\vartheta` consists of all weights and biases, all of which are trained. All coordinates of `\vartheta_0` and of a same-dimensional vector `\psi_0` are mutually independent standard-normal random variables.

Form `\psi_0^*` by retaining the coordinates of `\psi_0` belonging to layers before `L` and setting all final-layer weight and bias coordinates to zero. Define
\[
\widetilde g_r(x;\vartheta_0,\psi_0)
 =\nabla_\vartheta u_r(x;\vartheta_0)^{\mathsf T}\psi_0^*.
\]
Hold this entire random target function fixed during training and evolve the predictor by full-batch gradient flow:
\[
\mathcal L_r(\vartheta_t)
 =\tfrac12\|u_r(X;\vartheta_t)-\widetilde g_r(X;\vartheta_0,\psi_0)\|_2^2,
\qquad
\dot\vartheta_t=-\nabla_\vartheta\mathcal L_r(\vartheta_t).
\]
The labels `Y` are used only for the GP conditioning comparison, not as the training target in this loss. Assume the parameter gradients and this flow are well defined, with the chain rule valid almost everywhere along the flow.

The infinite-width training regime is assumed to have a stationary deterministic neural tangent kernel. Explicitly, define
\[
K_{r,t}(a,b)=\nabla_\vartheta u_r(a;\vartheta_t)^{\mathsf T}
                    \nabla_\vartheta u_r(b;\vartheta_t).
\]
For finite deterministic input lists `A,B`, let `K_{r,t}(A,B)` be the matrix of these evaluations. Assume there is a deterministic kernel `\Theta` such that, for every such pair of lists and every finite `T`,
\[
\sup_{0\leq t\leq T}
 \|K_{r,t}(A,B)-\Theta_{AB}\|_{\mathrm{op}}
 \xrightarrow{p}0
\]
as all hidden widths tend to infinity, where `\Theta_{AB}=(\Theta(a,b))_{a\in A,b\in B}`. Assume `\Theta_{XX}` is invertible and the limiting flow converges as time tends to infinity. Width is taken to infinity before time. When `L=1`, there is no hidden-width limit.

Define the finite-time error vector
\[
\varepsilon_{r,t}(Z)
 =u_r(Z;\vartheta_t)-\widetilde g_r(Z;\vartheta_0,\psi_0).
\]
A zero-mean GP with prior kernel `\Theta`, conditioned on the noiseless observations `(X,Y)`, has posterior mean `\Theta_{ZX}\Theta_{XX}^{-1}Y` and posterior covariance
\[
\Theta_{ZZ}-\Theta_{ZX}\Theta_{XX}^{-1}\Theta_{XZ}.
\]

## Task

Prove the iterated finite-dimensional convergence
\[
\lim_{t\to\infty}\ \lim_{r_1,\ldots,r_{L-1}\to\infty}
 \operatorname{Law}(\varepsilon_{r,t}(Z))
 =\mathcal N\!\left(
 0,\ \Theta_{ZZ}-\Theta_{ZX}\Theta_{XX}^{-1}\Theta_{XZ}
 \right),
\]
where the limits of laws are weak limits and the Gaussian law may be degenerate.

Equivalently, writing `\varepsilon_\infty(Z)` for this width-first, then time limiting error, prove that its law is the GP posterior predictive law conditioned on `(X,Y)` after subtracting that law's deterministic posterior mean.
