# Reference Proof

## Proof Structure and Obligations

Fix an admissible setup, a noise level \(\tau>0\), and \(K\ge1\). The fitted denoiser is a fixed measurable function. The obligations are: justify finite-horizon moment integrability and the conditional expectations; bound discretization; transfer denoiser error through the oracle conditional mean; bound the change from the conditional forward law to a standard Gaussian; bound Monte Carlo variance; and combine these bounds with their stated constants. Each obligation is discharged below. No Gaussian assumption on the true SDE increments, stationarity assumption, second-moment assumption on \(Y_0\), or guarantee about training error is used.

## 1. Moment Integrability and Increment Estimates

Write \(H=T+\Delta\). The assumption \(m_\mu(0)<\infty\), together with global Lipschitzness, implies the integrability claimed in the source; it is not necessary to add it as a new assumption.

Indeed, set \(c=\|\mu(Y_0)\|\), \(q(t)=\|B_t-B_0\|\), \(u(t)=\|\mu(Y_t)\|\), and \(v(t)=\int_0^t u(s)\,ds\). The SDE and Lipschitzness imply, pathwise,
\[
u(t)\le c+L v(t)+L\sigma q(t).
\]
Here \(v\) is absolutely continuous, so multiplication of \(v'(t)-Lv(t)\le c+L\sigma q(t)\) by \(e^{-Lt}\) and integration gives
\[
u(t)\le e^{Lt}c+L\sigma q(t)
 +L^2\sigma\int_0^t e^{L(t-s)}q(s)\,ds.
\]
Since \(\mathbb E q(s)^2=Ds\), the right side has an \(L^2\) norm bounded, uniformly for \(0\le t\le H\), by
\[
e^{LH}\sqrt{m_\mu(0)}+L\sigma\sqrt{DH}
 +L^2\sigma H e^{LH}\sqrt{DH}<\infty.
\]
Thus
\[
M:=\int_0^{T+\Delta}m_\mu(s)\,ds<\infty.
\]
This derivation only uses an integrating factor and the second moments of Brownian motion.

For \(0\le t\le T\) and \(0\le h\le\Delta\), the SDE, the squared-sum inequality, Cauchy--Schwarz, and Brownian variance give
\[
R(t,h):=\mathbb E\|Y_{t+h}-Y_t\|^2
\le 2h\int_t^{t+h}m_\mu(s)\,ds+2\sigma^2Dh.
\]
For fixed \(h\), Tonelli's theorem yields the sliding-interval bound
\[
\int_0^T\int_t^{t+h}m_\mu(s)\,ds\,dt
=\int_0^{T+h}m_\mu(s)\,|[s-h,s]\cap[0,T]|\,ds
\le hM.
\]
Consequently, with
\[
A_\Delta:=\frac{\Delta^2}{T}M+\sigma^2D\Delta,
\]
we have
\[
\frac1T\int_0^T\mathbb E\|Z_t\|^2\,dt\le 2A_\Delta.
\]
Forward-noise independence also gives
\[
\frac1T\int_0^T\mathbb E\|X_{\tau,t}\|^2\,dt
\le 2\alpha_\tau^2A_\Delta+\sigma_\tau^2D.
\]
The denoiser condition implies
\[
\frac1T\int_0^T\mathbb E\|D_{\theta^*}(\tau,X_{\tau,t},Y_t)\|^2\,dt
\le 2\varepsilon_{\rm score}(\tau)+4A_\Delta.
\]
In particular, the conditional \(L^2\) operations below are justified for Lebesgue-almost every \(t\), which is sufficient for the time-averaged assertion. No pointwise-in-time denoiser accuracy assumption is needed.

## 2. Intermediate Quantities and Decomposition

Abbreviate \(f_y(x)=\widehat\mu(\tau,x,y)\) and \(\ell=L_{\rm est}(\tau)\). The schedule conditions imply that the coefficients are finite and \(b_\Delta(\tau)>0\); therefore \(f_y\) is \(\ell\)-Lipschitz uniformly in \(y\).

For each relevant \(t\), choose conditional-expectation versions and define
\[
\mu_{\Delta,t}(y)=\Delta^{-1}\mathbb E[Z_t\mid Y_t=y],
\qquad
\widetilde\mu_t(\tau,y)=\mathbb E[f_y(X_{\tau,t})\mid Y_t=y],
\]
\[
\widetilde\mu_N(\tau,y)=\mathbb E_{G\sim N(0,I_D)}f_y(G).
\]
The time subscript merely records the conditioning law and avoids requiring a simultaneous choice of conditional versions. It does not change the source's intermediate quantities. For each fixed \(y\), the Gaussian expectation exists in \(L^2\), because
\(\|f_y(G)\|\le\|f_y(0)\|+\ell\|G\|\).

Brownian increments have conditional mean zero given the filtration at time \(t\). Adaptedness and conditional Fubini therefore give
\[
\mu_{\Delta,t}(Y_t)=\frac1\Delta\int_0^\Delta
\mathbb E[\mu(Y_{t+h})\mid Y_t]\,dh.
\]
Decompose
\[
\mu(Y_t)-\bar\mu_K(\tau,Y_t)=E_1(t)+E_2(t)+E_3(t)+E_4(t),
\]
where
\[
E_1=\mu(Y_t)-\mu_{\Delta,t}(Y_t),\quad
E_2=\mu_{\Delta,t}(Y_t)-\widetilde\mu_t(\tau,Y_t),
\]
\[
E_3=\widetilde\mu_t(\tau,Y_t)-\widetilde\mu_N(\tau,Y_t),\quad
E_4=\widetilde\mu_N(\tau,Y_t)-\bar\mu_K(\tau,Y_t).
\]
All conditional identities are needed only almost everywhere for the corresponding conditioning law.

## 3. Discretization Contribution

Jensen's inequality for the time average and conditional expectation, followed by Lipschitzness, gives
\[
\mathbb E\|E_1(t)\|^2\le\frac{L^2}{\Delta}\int_0^\Delta R(t,h)\,dh.
\]
Using the increment and sliding-interval estimates,
\[
\frac1T\int_0^T\mathbb E\|E_1(t)\|^2\,dt
\le\frac{L^2}{\Delta T}\int_0^\Delta
\bigl(2h^2M+2\sigma^2DhT\bigr)\,dh
\]
\[
=\frac{2L^2\Delta^2}{3T}M+L^2\sigma^2D\Delta
\le L^2A_\Delta.
\]
This explicitly verifies the coefficient used in the claimed discretization bound.

## 4. Denoiser Contribution

For the fixed conditioning time, let
\[
D_t^{\rm orc}(\tau,x,y)=\mathbb E[Z_t\mid X_{\tau,t}=x,Y_t=y].
\]
Direct substitution of the coefficients gives
\[
a(\tau)\alpha_\tau+b_\Delta(\tau)=\Delta^{-1}.
\]
Because \(\epsilon\) is centered and independent of \((Y_t,Z_t)\),
\(\mathbb E[X_{\tau,t}\mid Y_t]=\alpha_\tau\mathbb E[Z_t\mid Y_t]\).
The tower property therefore proves
\[
\mathbb E\bigl[a(\tau)X_{\tau,t}
+b_\Delta(\tau)D_t^{\rm orc}(\tau,X_{\tau,t},Y_t)\mid Y_t\bigr]
=\mu_{\Delta,t}(Y_t).
\]
This is an exact conditional-mean identity for the true increments, not an assertion that their law is the Euler--Maruyama Gaussian approximation.

Subtracting the learned estimator and applying conditional Jensen gives
\[
\mathbb E\|E_2(t)\|^2
\le b_\Delta(\tau)^2
\mathbb E\|D_t^{\rm orc}(\tau,X_{\tau,t},Y_t)
-D_{\theta^*}(\tau,X_{\tau,t},Y_t)\|^2.
\]
The conditional residual \(Z_t-D_t^{\rm orc}\) has mean zero given \((X_{\tau,t},Y_t)\). Expanding the square and conditioning therefore yields the orthogonal decomposition
\[
\mathbb E\|Z_t-D_{\theta^*}\|^2
=\mathbb E\|Z_t-D_t^{\rm orc}\|^2
 +\mathbb E\|D_t^{\rm orc}-D_{\theta^*}\|^2,
\]
where the denoisers are evaluated at \((\tau,X_{\tau,t},Y_t)\). Thus
\[
\frac1T\int_0^T\mathbb E\|E_2(t)\|^2\,dt
\le b_\Delta(\tau)^2\varepsilon_{\rm score}(\tau).
\]

## 5. Gaussian-Initialization Contribution

For probability laws \(P,Q\) with finite second moments, define
\(W_2(P,Q)^2=\inf\mathbb E\|U-V\|^2\), where the infimum is over couplings with marginals \(P,Q\). For any such coupling and any vector-valued \(\ell\)-Lipschitz map \(f\), Jensen's inequality gives
\[
\|\mathbb E f(U)-\mathbb E f(V)\|^2
\le\mathbb E\|f(U)-f(V)\|^2
\le\ell^2\mathbb E\|U-V\|^2.
\]
Taking the infimum proves the vector expectation bound used here. This directly verifies the required consequence of the standard transport result indexed by theory_012, without any unexpanded transport-theorem dependency. Equivalently, scalar Kantorovich--Rubinstein duality applied to unit-vector projections, followed by \(W_1\le W_2\), gives the same result.

Conditionally on \(Y_t=y\), couple \(X_{\tau,t}=\alpha_\tau Z_t+\sigma_\tau\epsilon\) with a standard Gaussian \(G=\epsilon\). The conditional second moments are finite for almost every \(y\). Forward-noise independence makes the cross term vanish, so
\[
\mathbb E[\|X_{\tau,t}-G\|^2\mid Y_t=y]
=\alpha_\tau^2\mathbb E[\|Z_t\|^2\mid Y_t=y]
 +(1-\sigma_\tau)^2D.
\]
Applying the expectation bound, then averaging over the state and time, yields
\[
\frac1T\int_0^T\mathbb E\|E_3(t)\|^2\,dt
\le\ell^2\left[2\alpha_\tau^2A_\Delta+(1-\sigma_\tau)^2D\right].
\]
The same coupling and \(\|f_y(G)\|^2\le2\|f_y(X_{\tau,t})\|^2+2\ell^2\|G-X_{\tau,t}\|^2\) also verify time-averaged square integrability of the Gaussian evaluations and their mean.

## 6. Monte Carlo Contribution

The actual Gaussian sampling vector is independent of \(Y\), and the denoiser is fixed. Hence, conditionally on \(Y_t=y\), the \(K\) evaluations are iid with mean \(\widetilde\mu_N(\tau,y)\). Independence and centering cancel the off-diagonal terms in the squared norm, giving
\[
\mathbb E_G\|\widetilde\mu_N(\tau,y)-\bar\mu_K(\tau,y)\|^2
=\frac1K\mathbb E_G\|f_y(G)-\mathbb E_G f_y(G)\|^2.
\]
The standard Gaussian Poincare inequality, indexed by theory_013, states that a scalar Lipschitz function \(h\) satisfies
\(\operatorname{Var}(h(G))\le\mathbb E\|\nabla h(G)\|^2\le\operatorname{Lip}(h)^2\), with its almost-everywhere gradient. Each coordinate of \(f_y\) is \(\ell\)-Lipschitz and square integrable under the Gaussian law, so summing its coordinate variances gives a bound of \(D\ell^2\).

There is also an elementary verification of precisely this consequence: for independent standard Gaussians \(G,G'\),
\[
\mathbb E\|f_y(G)-\mathbb E f_y(G)\|^2
=\tfrac12\mathbb E\|f_y(G)-f_y(G')\|^2
\le\tfrac12\ell^2\mathbb E\|G-G'\|^2
=D\ell^2.
\]
Thus this numerical variance bound has no unresolved external proof obligation. It follows that
\[
\frac1T\int_0^T\mathbb E\|E_4(t)\|^2\,dt\le\frac{D\ell^2}{K}.
\]
No independence between evaluations at different times is required.

## 7. Combination

Apply \(\|u_1+u_2+u_3+u_4\|^2\le4\sum_{i=1}^4\|u_i\|^2\), and combine the four estimates:
\[
\frac1T\int_0^T\mathbb E\|\mu(Y_t)-\bar\mu_K(\tau,Y_t)\|^2\,dt
\le4\left\{L^2A_\Delta+b_\Delta(\tau)^2\varepsilon_{\rm score}(\tau)
+L_{\rm est}(\tau)^2\left[2\alpha_\tau^2A_\Delta+(1-\sigma_\tau)^2D\right]
+\frac{D L_{\rm est}(\tau)^2}{K}\right\}.
\]
Substitution of the definition of \(A_\Delta\) is exactly the requested inequality, with the original quantifiers, time domain, and constants. All obligations are closed.
