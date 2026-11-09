# Reference Proof

## Proof Structure

1. Identify the fixed-design likelihood objects and the actual adaptive experiment law. Verify the posterior policy-factor cancellation and sequential marginal interpretation privately, using a reference measure when policies are general probability kernels; the public problem already defines the objective by its likelihood ratio.
2. Pull the adaptive objective back to the fixed base law and differentiate to obtain both marginal score contractions.
3. Differentiate the independently defined static objective and cancel only the expected fixed-y marginal design score using the pushforward law and marginal normalization.
4. Define the population score-substituted gradient, subtract it from the exact gradient, and transfer score error through the rollout Jacobian.
5. Bound the existing Jacobian at every fixed policy parameter directly from Lipschitz difference quotients, preserving the every-parameter conclusion.

## Complete Proof

Write y=y_{1:T}, xi=xi_{1:T}, and define
\[
\ell_\theta(y,\xi)=\prod_{t=1}^T p(y_t\mid\theta,\xi_t,h_{t-1}),\qquad
m(y,\xi)=\int p(\theta)\ell_\theta(y,\xi)\,d\theta.
\]
These are the likelihood objects denoted by p(y|theta,xi) and p(y|xi) in the task. For each fixed design sequence, the observation kernels successively integrate to one, so ell_theta and m are normalized densities in y. They need not be the ordinary conditional densities given the selected design sequence under an adaptive policy.

### Experiment-Law and Posterior Interpretation

The public task specifies policy probability kernels. These may be singular or deterministic, and need not possess scalar Lebesgue densities. The following calculation therefore uses a reference trajectory measure rather than an assumed policy-density product.

Fix phi. Choose a strictly positive probability density r on R^{d_y}, for example the standard Gaussian density, and write
\[
b(y)=\prod_{t=1}^T r(y_t).
\]
Define a reference trajectory probability measure R_phi by sequentially drawing xi_t from the same policy kernel pi_phi(.|h_{t-1}) and then drawing y_t from r(y_t)dy_t. More explicitly, integration against R_phi is the chronological iterated integral with factors
\[
\pi_\phi(d\xi_1\mid h_0)r(y_1)dy_1\cdots
\pi_\phi(d\xi_T\mid h_{T-1})r(y_T)dy_T.
\]
Each factor is a probability kernel, so this defines a probability measure. It does not depend on theta, because the policy kernels have no additional access to theta.

Let P_{phi,theta} denote the actual conditional experiment law given theta. For any nonnegative measurable trajectory function f, substitution in the chronological iterated integral gives
\[
\begin{aligned}
\int f(y,\xi)\frac{\ell_\theta(y,\xi)}{b(y)}\,R_\phi(dy,d\xi)
&=\int\cdots\int f(y,\xi)
\prod_{t=1}^T\left[
\pi_\phi(d\xi_t\mid h_{t-1})
p(y_t\mid\theta,\xi_t,h_{t-1})dy_t
\right]\\
&=\int f(y,\xi)\,P_{\phi,\theta}(dy,d\xi).
\end{aligned}
\]
Here the product notation denotes chronological kernel integration, not multiplication of scalar policy densities. The positive reference observation factors cancel pointwise, and nonnegative integration justifies the calculation. Consequently P_{phi,theta} has density ell_theta/b relative to R_phi. Its prior marginal P_phi has density m/b relative to R_phi, by nonnegative integration over theta.

On the set where 0<m(y,xi)<infinity, define
\[
K(\theta\mid y,\xi)=\frac{p(\theta)\ell_\theta(y,\xi)}{m(y,\xi)}.
\]
This integrates to one in theta. The exceptional set has P_phi measure zero: m/b is a probability density relative to R_phi, b is everywhere positive and finite, and the set m=0 carries zero P_phi mass. Define K arbitrarily as a probability density on that exceptional set.

To verify the posterior interpretation explicitly, for every nonnegative measurable F(theta,y,xi),
\[
\begin{aligned}
\int\!\int F(\theta,y,\xi)K(\theta\mid y,\xi)\,d\theta\,P_\phi(dy,d\xi)
&=\int\!\int F(\theta,y,\xi)
\frac{p(\theta)\ell_\theta(y,\xi)}{b(y)}\,d\theta\,R_\phi(dy,d\xi)\\
&=\int p(\theta)\left[\int F(\theta,y,\xi)\,P_{\phi,\theta}(dy,d\xi)\right]d\theta.
\end{aligned}
\]
Thus K is a conditional density of theta given the trajectory under the actual joint experiment law. The likelihood formula for the posterior contains no explicit policy factor, even though the trajectory law and the reference measure depend on phi. This argument covers arbitrary measurable policy probability kernels, including singular and deterministic ones.

The posterior log-density ratio to the prior is therefore log ell_theta minus log m, almost surely under the joint experiment law. Averaging it gives the objective defined in the public task; no additional prior-entropy constant is needed for that definition. When entropy quantities are separately finite, this also equals the expected prior-to-posterior entropy reduction.

For completeness, the sequential marginal factorization follows without an external theorem. Let M_t be the prior integral of the first t observation factors and M_0=1. Applying the same reference-measure calculation to a prefix history gives the posterior proportional to the prior times those t-1 factors, normalized by M_{t-1}. Selecting xi_t through a kernel independent of theta conditional on that history does not change this posterior: its conditional joint law with theta is the product of the posterior law and the policy kernel. Consequently the next predictive observation factor is M_t/M_{t-1}. Multiplying these ratios gives M_T=m(y,xi), on histories where the factors are defined. These interpretive calculations are not additional public proof requirements because the objective and likelihood objects are already defined there.

### Adaptive Gradient

Let rho(dtheta,du)=p(theta)dtheta q(du), and abbreviate the rollout by z_phi=(y_phi,xi_phi). Its conditional pushforward given theta is the stated experiment law, hence
\[
I_T(\phi)=\mathbb E_\rho\left[
\log\ell_\theta(y_\phi,\xi_\phi)-\log m(y_\phi,\xi_\phi)
\right].
\]
The base law rho is independent of phi. The stated differentiability, integrability, and differentiation-under-expectation assumptions therefore give
\[
\nabla_\phi I_T(\phi)=\mathbb E_\rho\left[
D_\phi\log\ell_\theta(y_\phi,\xi_\phi)
-D_\phi\log m(y_\phi,\xi_\phi)
\right].
\]
There is no direct phi dependence in either likelihood object at fixed theta, y, and xi. The chain rule yields
\[
D_\phi\log m(y_\phi,\xi_\phi)
=J_y^\top s_y(y_\phi,\xi_\phi)+J_\xi^\top s_\xi(y_\phi,\xi_\phi).
\]
Substitution proves the adaptive identity. The conditional term remains a total derivative and includes both observation and design paths.

### Static Gradient

For fixed designs xi chosen independently of theta and observations, let delta have the fixed law q_stat and let y_xi=g_stat(delta,theta,xi). Its conditional law given theta is ell_theta(y,xi)dy. The static objective is thus
\[
I_T(\xi)=\mathbb E_{p(\theta)q_{\rm stat}}\left[
\log\ell_\theta(y_\xi,\xi)-\log m(y_\xi,\xi)
\right].
\]
Differentiating this fixed-base-law expectation and applying the chain rule gives
\[
\nabla_\xi I_T(\xi)=\mathbb E\left[
D_\xi\log\ell_\theta(y_\xi,\xi)
-(J_y^{\rm stat})^\top s_y(y_\xi,\xi)-s_\xi(y_\xi,\xi)
\right].
\]
The pushforward law and integrability, not invertibility of g_stat, imply
\[
\begin{aligned}
\mathbb E[s_\xi(y_\xi,\xi)]
&=\iint p(\theta)\ell_\theta(y,\xi)\,\nabla_\xi\log m(y,\xi)\,dy\,d\theta\\
&=\int m(y,\xi)\nabla_\xi\log m(y,\xi)\,dy\\
&=\int\nabla_\xi m(y,\xi)\,dy\\
&=\nabla_\xi\int m(y,\xi)\,dy=0.
\end{aligned}
\]
The last interchange is precisely the static marginal-integral regularity assumed in the task. Densities and derivatives are interpreted on the fixed observation space, with no omitted support-boundary contributions. Hence
\[
\nabla_\xi I_T(\xi)=\mathbb E\left[
D_\xi\log p(y_\xi\mid\theta,\xi)
-(J_y^{\rm stat})^\top s_y(y_\xi,\xi)
\right].
\]
Only the fixed-y marginal design score has canceled; no observation-path contribution in the conditional total derivative is discarded.

### Score-Error Transfer at Every Policy Parameter

Set
\[
J_z=\begin{pmatrix}J_y\\J_\xi\end{pmatrix},\qquad s=(s_y,s_\xi).
\]
The population score-substituted estimator is
\[
\widehat G_\psi(\phi)=\mathbb E_\rho\left[
D_\phi\log\ell_\theta(y_\phi,\xi_\phi)-J_z^\top s_\psi(z_\phi)
\right].
\]
Fix an arbitrary phi in the open parameter domain. For rho-almost every realization, J_z exists at this phi by the task's differentiability assumption. For any direction v and sufficiently small nonzero h, the Lipschitz assumption gives
\[
\left\|\frac{z_{\phi+hv}-z_\phi}{h}\right\|_2\le L\|v\|_2.
\]
Taking h to zero gives ||J_z v||_2 <= L||v||_2, and therefore ||J_z||_op <= L at this fixed phi, almost surely in the base randomness. This argument uses differentiability already assumed by the task. Rademacher's theorem alone would only give an almost-everywhere-in-phi assertion and is not needed here.

Subtracting the approximate gradient from the exact one gives
\[
\nabla_\phi I_T(\phi)-\widehat G_\psi(\phi)
=\mathbb E_\rho\left[J_z^\top\bigl(s_\psi(z_\phi)-s(z_\phi)\bigr)\right].
\]
The error term is integrable because its norm is bounded by L times the assumed integrable score error. Thus Jensen's inequality and operator-norm submultiplicativity imply
\[
\begin{aligned}
\left\|\nabla_\phi I_T(\phi)-\widehat G_\psi(\phi)\right\|_2
&\le\mathbb E_\rho\left[\|J_z\|_{\rm op}\,\|s_\psi(z_\phi)-s(z_\phi)\|_2\right]\\
&\le L\,\mathbb E_\rho\left[\|s_\psi(z_\phi)-s(z_\phi)\|_2\right]\\
&\le L(\eta/L)=\eta.
\end{aligned}
\]
Since phi was arbitrary and the same L and eta apply throughout the domain, this is the required uniform every-phi bound. Constant rollouts cause no exception: their Jacobian is zero, and the stated bound still holds with any permitted positive L.

## Obligation Closure

- The likelihood and marginal definitions and experiment-law expectation are explicitly verified above.
- The posterior interpretation is verified by a reference trajectory probability measure and a test-function calculation, without assuming policy densities.
- The prefix posterior and sequential marginal interpretation are established with the same kernel argument.
- Conditional pushforward laws justify both fixed-base representations.
- The adaptive identity follows from the assumed interchange and an explicit chain rule.
- The static cancellation follows from the pushforward law, prior marginalization, and the explicitly permitted normalized-integral differentiation; no inverse map is assumed.
- The every-parameter Jacobian bound is proved by difference quotients, rather than by changing the scope of Rademacher's almost-everywhere conclusion.
- The population estimator's error bound and integrability are explicitly derived with the original uniform constants.

No theorem-critical proof obligation remains unresolved.
