# Reference Proof

Fix the base parameter \(\theta\). The local candidates remain fixed throughout differentiation.

## Preliminary obligations: law continuity and the law Itô formula

Write \(B_\eta=b_\eta\) and \(S_\eta=\sigma_\eta\) for the induced coefficients. The stated Lipschitz and growth bounds give, on every compact parameter set \(K\),
\[
\sup_{\eta\in K}\mathbb E\sup_{t\le s\le T}|X_s^{t,\xi,\eta}|^2\le C_K(1+\mathbb E|\xi|^2).
\]
Indeed, apply the deterministic integral Cauchy–Schwarz inequality and the square-integrable martingale maximal inequality to the SDE, use the linear-growth bound and \(M_2(\mu_s)^2=\mathbb E|X_s|^2\), and apply Gronwall. Constants may depend on the horizon and the compact parameter set, but not on its varying parameter.

To establish parameter continuity without a specialized external theorem, let \(\eta_j\to\eta\), and couple solutions with the same initial variable and Brownian motion. Splitting each coefficient difference into its state/law difference and its parameter difference at the fixed base solution, the Lipschitz bounds, the same maximal inequality, and Gronwall yield
\[
\mathbb E\sup_{t\le s\le T}|X_s^{\eta_j}-X_s^\eta|^2
\le C\int_t^T\mathbb E\big[|B_{\eta_j}(s,X_s^\eta,\mu_s^\eta)-B_\eta(s,X_s^\eta,\mu_s^\eta)|^2
+|S_{\eta_j}(s,X_s^\eta,\mu_s^\eta)-S_\eta(s,X_s^\eta,\mu_s^\eta)|^2\big]ds.
\]
The right side tends to zero by continuity and dominated convergence. Its integrand is bounded by \(C(1+|X_s^\eta|^2+M_2(\mu_s^\eta)^2)\), which is integrable. Thus the laws converge uniformly in time in \(\mathcal W_2\). The SDE increment estimate also gives
\[
\mathcal W_2(\mu_u^{t,\mu,\eta},\mu_v^{t,\mu,\eta})^2\le C_K|u-v|.
\]
Consequently \((s,\eta)\mapsto\mu_s^{t,\mu,\eta}\) is jointly continuous. No assertion about the hypotheses of the specialized continuous-dependence citation is needed.

The standard independent law Itô formula used below states that, for a square-integrable Itô process \(dX_s=B_sds+S_sdW_s\), its unconditional law \(\mu_s\), and a function \(w\) in the specified \(C^{1,2}\) class,
\[
w(v,\mu_v)-w(u,\mu_u)=\int_u^v\left(\partial_sw(s,\mu_s)+\mathbb E[B_s\cdot\partial_\mu w(s,\mu_s)(X_s)+\tfrac12S_sS_s^\top:\partial_x\partial_\mu w(s,\mu_s)(X_s)]\right)ds.
\]
For the present coefficients, its integrability hypotheses follow from the preceding moment estimate and the derivative bounds on compact sets of laws in the definition of \(C^{1,2}\). For example, the drift pairing is bounded by Cauchy–Schwarz, and the diffusion pairing by the essential bound on \(\partial_x\partial_\mu w\) times \(\mathbb E|S_s|^2\). The law path is compact. Multiplication by the deterministic discount therefore gives
\[
e^{-\beta v}w(v,\mu_v^{t,\mu,\eta})-e^{-\beta u}w(u,\mu_u^{t,\mu,\eta})
=\int_u^v e^{-\beta s}\mathcal L^\eta[w](s,\mu_s^{t,\mu,\eta})ds.
\]
The generators occurring here are continuous: continuity on supports, the compact-law-set derivative bounds, and the coefficient growth bounds justify truncation and passage to limits in their defining integrals. Compactness in \(\mathcal W_2\) provides uniform integrability of squared state norms. For the drift term its tail is controlled by Cauchy–Schwarz; for the diffusion term it is controlled by the uniform essential derivative bound.

## Step 1: Lift the martingale identity

Fix \((t,\mu)\), \(\eta\in O_{t,\mu}(\theta)\), and \(\xi\sim\mu\). Take expectations in the assumed true-martingale identity at \(s\) and \(t\). The explicitly assumed absolute time integrability permits Fubini. The push-forward definition gives the joint law of the state and its feedback action. Hence
\[
e^{-\beta s}\widehat V(s,\mu_s^{t,\mu,\eta})-e^{-\beta t}\widehat V(t,\mu)
+\int_t^s e^{-\beta u}\big[\bar r(u,\mu_u^{t,\mu,\eta},\eta)-\widehat q(u,\mu_u^{t,\mu,\eta},\eta)\big]du=0.
\]
The terminal condition and normalization give \(\widehat V(T,\nu)=\bar g(\nu)\) and \(\widehat q(u,\nu,\theta)=0\) for every \((u,\nu)\).

## Step 2: Identify the value and advantage

Set \(\eta=\theta\) and \(s=T\) in the preceding identity. Rearranging yields exactly the defining discounted reward representation of \(V^\theta(t,\mu)\). Thus
\[
\widehat V(t,\mu)=V^\theta(t,\mu),\qquad 0\le t\le T.
\]
This also proves the required classical uniqueness statement directly rather than merely naming Feynman–Kac uniqueness.

For \(t<T\), apply the discounted law Itô formula to \(\widehat V\) along the \(\eta\)-flow and subtract the lifted identity. The result is
\[
\int_t^s e^{-\beta u}\big[\mathcal A^\eta[\widehat V](u,\mu_u^{t,\mu,\eta})-\widehat q(u,\mu_u^{t,\mu,\eta},\eta)\big]du=0.
\]
Divide by \(s-t\) and let \(s\downarrow t\). Continuity gives
\[
\widehat q(t,\mu,\eta)=\mathcal A^\eta[V^\theta](t,\mu),\qquad t<T,\quad\eta\in O_{t,\mu}(\theta).
\]
In particular \(\mathcal A^\theta[V^\theta](t,\mu)=0\) for \(t<T\); continuity at fixed \(\mu\) extends this base-parameter equality to \(t=T\). There is no analogous off-policy terminal extension because the neighborhoods may shrink with \((t,\mu)\).

## Step 3: Derive parameter sensitivity

For any nearby parameter \(\eta\), the reward representation of \(V^\eta\), the terminal equality \(V^\theta(T,\nu)=\bar g(\nu)\), and the law Itô formula applied to the fixed function \(V^\theta\) imply
\[
V^\eta(t,\mu)-V^\theta(t,\mu)
=\int_t^T e^{-\beta(s-t)}\mathcal A^\eta[V^\theta](s,\mu_s^{t,\mu,\eta})ds.
\]
Since \(\mathcal A^\theta[V^\theta](s,\nu)=0\), the integrand can equivalently be replaced by \(\mathcal A^\eta[V^\theta]-\mathcal A^\theta[V^\theta]\), evaluated at the same perturbed law. This identity follows for all nearby \(\eta\) from the model and does not require a common neighborhood for the martingale hypotheses.

Put
\[
F(s,\nu,\zeta)=\partial_\zeta\big(\mathcal A^\zeta[V^\theta](s,\nu)\big).
\]
Here \(V^\theta\) is held fixed. For an arbitrary vector increment \(h\) with \(\theta+h\in\Theta\), the fundamental theorem of calculus yields
\[
V^{\theta+h}(t,\mu)-V^\theta(t,\mu)
=h\cdot\int_t^T e^{-\beta(s-t)}\int_0^1F(s,\mu_s^{t,\mu,\theta+h},\theta+vh)dv\,ds.
\]
Choose a closed parameter ball contained in \(\Theta\). Joint flow continuity makes the image of its product with \([t,T]\) compact in \(\mathcal P_2\). Joint continuity of \(F\) gives a bound and uniform continuity on the resulting compact set. The integral multiplying \(h\) therefore converges, as \(h\to0\), to
\[
\int_t^T e^{-\beta(s-t)}F(s,\mu_s^{t,\mu,\theta},\theta)ds.
\]
The remainder is \(o(|h|)\), proving differentiability, not only directional differentiability.

For each fixed \(s<T\) and \(\nu\), the local advantage identification holds on an open neighborhood of \(\theta\). Differentiation at fixed \((s,\nu)\) consequently gives
\[
F(s,\nu,\theta)=\partial_\eta\widehat q(s,\nu,\eta)\big|_{\eta=\theta}.
\]
Taking \(t=0\) and \(\mu=\mu_0\), which is fixed independently of the parameter, gives
\[
\nabla_\theta J(\varphi_\theta)=\int_0^T e^{-\beta s}\partial_\eta\widehat q(s,\mu_s^\theta,\eta)\big|_{\eta=\theta}ds.
\]
Changing or omitting the integrand at the single terminal time has no effect. No uniform lower bound on the radii of \(O_{s,\nu}(\theta)\) was used.

## Step 4: Insert the stipulated action/joint-law chain rule

For \(a_s=\varphi_\theta(s,X_s^\theta,\mu_s^\theta)\) and an independent copy \((\widetilde X_s^\theta,\widetilde a_s)\), the chain-rule assumption gives
\[
\partial_\eta\widehat q(s,\mu_s^\theta,\eta)\big|_{\eta=\theta}
=\mathbb E\!\left[\partial_\theta\varphi_\theta(s,X_s^\theta,\mu_s^\theta)^\top
\left(\partial_a\widehat q_D(s,X_s^\theta,a_s,\Gamma_s^\theta)
+\widetilde{\mathbb E}[\partial_\nu^a\widehat q_D(s,\widetilde X_s^\theta,\widetilde a_s,\Gamma_s^\theta)(X_s^\theta,a_s)]\right)\right].
\]
The stated absolute integrability of the individual-action and independent-copy terms permits Fubini in time and probability. Substitution proves the target formula. The candidates are not differentiated through their choice at the base parameter, and the state-law argument is held fixed in the chain rule.

## Audit closure

The critical obligations are: well-defined flows and moments; joint time/parameter law continuity; applicable law Itô formula; martingale lifting with Fubini; value and local advantage identification; full parameter differentiability; and the action/joint-law substitution with Fubini. Each is derived above or is an explicitly stated standard independent formula with its hypotheses checked. The optional construction of local candidates is not needed. There is no unresolved private proof obligation.
