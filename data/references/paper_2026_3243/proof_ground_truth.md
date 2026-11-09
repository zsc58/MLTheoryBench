# Reference Proof

## Proof Structure

1. Establish the latent-to-process conditional pushforward identity.
2. Derive the density and score of the noised latent conditional.
3. Construct the reversed forward diffusion, identify its drift, and use uniqueness in law to establish the reverse marginals.
4. Justify the endpoint law by continuity, then push it through the generator.

## Complete Proof

The pushforward assumption gives \(Z=\int_{\mathbb R^d}\Lambda(\xi)r(\xi)\,d\xi\). For every measurable \(A\subseteq E\),
\[
\mathbb P(T(\xi_0)\in A)=\frac1Z\int \mathbf 1_A(T(\xi))\Lambda(\xi)r(\xi)\,d\xi
=\frac1Z\int_A L(f)p(f)\,df.
\]
Thus \(T_\#(\rho_0\,d\xi)=\pi(f\mid C)\,df\).

Consider the forward SDE \(dX_t=-\beta(t)X_t\,dt/2+\sqrt{\beta(t)}\,dW_t\), with its initial state independent of \(W\). Its explicit solution is
\[
X_t=\alpha(t)X_0+\alpha(t)\int_0^t\frac{\sqrt{\beta(v)}}{\alpha(v)}\,dW_v.
\]
The integral term is independent of \(X_0\) and has covariance \((1-\alpha(t)^2)I_d=\sigma(t)^2I_d\). Hence, with \(X_0\sim\rho_0\), this SDE has the one-time laws \(\rho_t\) specified by the bridge in the task. The bridge need not use the same noise variable jointly at every time to specify those laws.

First take \(X_0\sim r\). Stationarity of the Gaussian SDE gives \(X_t\sim r\). For \(t>0\), joint Gaussian conditioning gives \(X_0\mid X_t=u\sim N(\alpha(t)u,\sigma(t)^2I_d)\). Tilting its initial law by \(\Lambda/Z\) therefore gives
\[
\rho_t(u)=\frac{r(u)}Z\,\mathbb E[\Lambda(X_0)\mid X_t=u]
=\frac{r(u)\psi(t,u)}Z.
\]
Here \(0<\sigma(t)^2<1\). The conditional Gaussian density divided by \(r\), together with its spatial derivatives, is bounded locally uniformly in \((t,u)\) on interior time intervals. Since \(\Lambda\in L^1(r)\) and \(Z>0\), \(\psi\) is finite, positive, and spatially smooth there. Consequently
\[
\nabla_u\log\rho_t(u)=\nabla_u\log\psi(t,u)+\nabla_u\log r(u)=g(t,u)-u.
\]
The same Gaussian-kernel bounds and local integrability of \(\beta\) make \(t\mapsto\rho_t(u)\) locally absolutely continuous, with locally bounded spatial derivatives on compact subsets of \((0,1)\times\mathbb R^d\).

Put \(b_t(u)=-\beta(t)u/2\) and \(L_t^*v=-\nabla\!\cdot(b_tv)+\beta(t)\Delta v/2\). The forward marginals satisfy \(\partial_t\rho_t=L_t^*\rho_t\) in the weak sense. Set \(q_s=\rho_{\tau_s}\) and
\[
\widetilde b_s(u)=-b_{\tau_s}(u)+\beta(\tau_s)\nabla_u\log\rho_{\tau_s}(u)
=\beta(\tau_s)g(\tau_s,u)-\tfrac12\beta(\tau_s)u.
\]
This is the drift in the task. Direct substitution also shows that the proposed densities satisfy its reverse Fokker--Planck equation:
\[
\partial_s q_s=\nabla\!\cdot(b_{\tau_s}q_s)-\tfrac12\beta(\tau_s)\Delta q_s
=-\nabla\!\cdot(\widetilde b_s q_s)+\tfrac12\beta(\tau_s)\Delta q_s.
\]
This calculation alone does not establish that the marginals of an arbitrary solution are density-valued; that applicability point is addressed next.

Take the actual forward process with \(X_0\sim\rho_0\), and on the fixed interior interval define its continuous reversal \(Y_s=X_{t_1-s}\). It has marginals \(q_s\). For \(v<t\), the forward transition density is
\[
P_{v,t}(z,u)=\mathcal N\!\left(u;\frac{\alpha(t)}{\alpha(v)}z,
\left[1-\frac{\alpha(t)^2}{\alpha(v)^2}\right]I_d\right).
\]
Bayes’ rule gives the reverse transition kernel, for \(h>0\) with \(s+h\le t_1-t_0\), as
\[
\mathbb P(Y_{s+h}\in dz\mid Y_s=u)
=\frac{\rho_{\tau_s-h}(z)P_{\tau_s-h,\tau_s}(z,u)}{\rho_{\tau_s}(u)}\,dz.
\]
For a smooth compactly supported test function \(\varphi\), expand this kernel at almost every \(s\), using \(\partial_t\rho_t=L_t^*\rho_t\). The resulting reverse generator is
\[
\mathcal A_s^{\leftarrow}\varphi(u)
=\frac{L_{\tau_s}^*(\rho_{\tau_s}\varphi)(u)-\varphi(u)L_{\tau_s}^*\rho_{\tau_s}(u)}{\rho_{\tau_s}(u)}
=\widetilde b_s(u)\cdot\nabla\varphi(u)+\tfrac12\beta(\tau_s)\Delta\varphi(u).
\]
The expansion is valid on compact spatial sets by the established Gaussian smoothing and local absolute continuity in time. Localization of the corresponding martingale problem gives \(Y_s=Y_0+\int_0^s\widetilde b_v(Y_v)\,dv+M_s\), with \(\langle M\rangle_s=\int_0^s\beta(\tau_v)I_d\,dv\). The drift integral is locally finite: \(g(t,u)-u/2\) is bounded on compact interior time--space sets, \(\beta\) is integrable there, and a continuous path is bounded on this interval. Since \(\beta>0\), the continuous-martingale characterization applied to \(\int_0^s\beta(\tau_v)^{-1/2}\,dM_v\) supplies a reverse-time Brownian motion. Thus \(Y\) is a weak solution of precisely the SDE in the task, initialized with \(Y_0\sim\rho_{t_1}\).

The assumed uniqueness in law identifies \(\bar\xi\) with \(Y\) on \([0,t_1-t_0]\). In particular, \(\bar\xi_s\sim\rho_{t_1-s}\), so its marginals are now known to have densities. The density-valued Fokker--Planck uniqueness assumption is consistent with, but is not needed in place of, this identification.

As \(t\downarrow0\), local integrability of \(\beta\) implies \(\alpha(t)\to1\) and \(\sigma(t)\to0\). The bridge coupling therefore gives \(\xi_t\to\xi_0\) almost surely, so \(\rho_t\Rightarrow\rho_0\). If the reverse solution has continuous paths through \(s=t_1\), then \(\bar\xi_s\to\bar\xi_{t_1}\) almost surely as \(s\uparrow t_1\). Its already established interior marginals and uniqueness of weak limits imply \(\bar\xi_{t_1}\sim\rho_0\). Applying the first pushforward identity to this terminal law gives \(T(\bar\xi_{t_1})\sim\pi(\cdot\mid C)\). No value of \(g(0,\cdot)\) is needed.
