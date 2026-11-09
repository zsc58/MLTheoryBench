# Reference Proof

## Contract and proof obligations

The prior is assumed to have a finite first moment, not a finite second moment. The class definition supplies the deterministic hard-truncation convergence and terminal recovery. These properties are used as hypotheses; proving Gaussian membership or general noncompact well-posedness is not an additional obligation of this conditional transfer theorem.

The obligations are: (1) compact drift estimates and invariance; (2) compact-flow and particle well-posedness and stability; (3) expected empirical Wasserstein convergence; (4) compact-uniform continuity of the posterior quotient and the particle limit at fixed radius; (5) the deterministic radius limit; (6) the terminal recovery limit; (7) the ordered expectation conclusion, measurability, and posterior interpretation; and (8) the probability conclusion. Each is closed below.

Initially, \(f_0\in\mathcal P_1\), since for independent \(X\sim P_0\) and \(Z\sim N(0,\tau I_d)\), \(\mathbb E|X+Z|\le\mathbb E|X|+\mathbb E|Z|<\infty\). Its density \(y\mapsto\int\gamma_\tau(y-x)\,dP_0(x)\) is strictly positive. Thus \(f_0(B_R)>0\) for every \(R>0\), so every normalized truncation in the statement is defined.

## 1. Compact drift estimates and invariance

Fix \(\beta,R,T>0\), temporarily allowing an arbitrary finite horizon \(T\). For \(\nu\) supported in \(B_R\), write
\[
D_\nu(y)=\int K_\beta(y,x)\,d\nu(x),\qquad A_\nu(y)=\int xK_\beta(y,x)\,d\nu(x).
\]
For \(y\in B_R\),
\[
D_\nu(y)\ge e^{-2\beta R^2}=:c_{\beta,R}>0,\qquad |A_\nu(y)|\le R.
\]
On \(B_R\times B_R\), the derivatives of \(K_\beta\) in either argument are bounded by \(2\beta R\). The derivative of \(xK_\beta(y,x)\) in \(x\) is bounded by \(1+2\beta R^2\), and its derivative in \(y\) is bounded by \(2\beta R^2\). Integrating against any coupling of \(\nu,\widetilde\nu\), and then taking the infimum over couplings, bounds numerator and denominator differences by
\[
C_{\beta,R}\bigl(|y-y'|+W_1(\nu,\widetilde\nu)\bigr).
\]
The quotient identity, the common lower bound \(c_{\beta,R}\), and \(b_{\beta,\nu}=A_\nu/D_\nu-\mathrm{id}\) therefore give a finite constant \(L=L_{\beta,R}>0\) such that
\[
|b_{\beta,\nu}(y)-b_{\beta,\widetilde\nu}(y')|
\le L\bigl(|y-y'|+W_1(\nu,\widetilde\nu)\bigr)
\]
for all \(y,y'\in B_R\) and \(\nu,\widetilde\nu\in\mathcal P(B_R)\). The same calculation on any larger bounded query set gives local spatial Lipschitz bounds there.

The weights defining \(F_{\beta,\nu}(y)\) are a probability distribution on \(B_R\). Hence \(F_{\beta,\nu}(y)\in B_R\) for every \(y\). For a prescribed continuous path \(q_t\in\mathcal P(B_R)\), any characteristic satisfies
\[
z_t=e^{-t}z_0+\int_0^t e^{-(t-s)}F_{\beta,q_s}(z_s)\,ds.
\]
Consequently \(|z_t|\le R\) whenever \(|z_0|\le R\). This proves invariance without assuming strict inward motion at a boundary point.

For the particle system, its vector field is smooth on \((\mathbb R^d)^N\) and has positive denominators. Let \(H(t)=\max_i|X_i(t)|^2\). At any index attaining this maximum, the current barycenter has norm at most \(\sqrt{H(t)}\), so
\[
2X_i(t)\cdot\bigl(F_{\beta,\mu_t^{N,R}}(X_i(t))-X_i(t)\bigr)\le0.
\]
The upper right derivative of the finite maximum \(H\) is therefore nonpositive. Thus all particles remain in \(B_R\). Local ODE existence and uniqueness extend over every finite horizon because the solution stays in a compact set.

## 2. Compact nonlinear flows and stability

For a prescribed \(q\in C([0,T];\mathcal P(B_R))\), the drift is continuous in time, locally Lipschitz in space, and its characteristics starting in \(B_R\) stay there. The usual ODE existence and uniqueness theorem therefore gives a characteristic map \(\Phi_t^q:B_R\to B_R\).

For an initial law \(\lambda\in\mathcal P(B_R)\), define
\[
(\Gamma q)_t=(\Phi_t^q)_\#\lambda.
\]
The space \(\mathcal P(B_R)\) is complete in \(W_1\): on a compact metric space weak convergence and \(W_1\)-convergence agree, and probability measures form a compact space. Hence continuous paths in this space are complete under the uniform metric and under its equivalent exponentially weighted versions. These are the compact Wasserstein facts used here.

Subtracting characteristics with the same initial point and applying Gronwall gives
\[
|\Phi_t^q(x)-\Phi_t^r(x)|\le L\int_0^t e^{L(t-s)}W_1(q_s,r_s)\,ds.
\]
For \(d_\alpha(q,r)=\sup_{t\le T}e^{-\alpha t}W_1(q_t,r_t)\), it follows that
\[
d_\alpha(\Gamma q,\Gamma r)\le\frac{L}{\alpha-L}d_\alpha(q,r).
\]
Choose \(\alpha>2L\). The contraction theorem on the complete path space gives a unique fixed point \(\mu_t\). Its characteristics have speed at most \(2R\), so the resulting curve is \(W_1\)-continuous, has finite action, and satisfies the stated weak equation by the chain rule.

For completeness, this also specifies the compact-support weak flow unambiguously. If \(\nu_t\) is another continuous weak solution supported in \(B_R\), prescribe its own field \(b_{\beta,\nu_t}\). For a smooth terminal spatial test, transport it backward along this field and multiply by a spatial cutoff equal to one on a neighborhood of \(B_R\). The transported test satisfies the backward transport equation on \(B_R\). Time-dependent testing follows from the stated weak formulation by approximation with finite sums of products of time and space test functions. Integrating that identity gives
\[
\int\psi\,d\nu_t=\int\psi(\Phi_{0,t}^{\nu}(x))\,d\nu_0(x).
\]
All tests and derivatives are bounded on the relevant compact cylinder, so the approximation is legitimate. Thus \(\nu_t=(\Phi_{0,t}^{\nu})_\#\nu_0\), and \(\nu\) is a fixed point of the same map. It is therefore the characteristic solution already constructed.

If \(\mu_t,\widetilde\mu_t\) are compact flows, transport any coupling of their initial laws along their respective characteristics. Its mean distance \(h(t)\) satisfies
\[
h(t)\le h(0)+2L\int_0^t h(s)\,ds,
\]
because \(W_1(\mu_s,\widetilde\mu_s)\le h(s)\). Gronwall and the infimum over initial couplings give
\[
W_1(\mu_t,\widetilde\mu_t)\le e^{2Lt}W_1(\mu_0,\widetilde\mu_0).
\]
Here the elementary Gronwall statement is that a nonnegative continuous function bounded by \(a+L\int_0^t h\) is bounded by \(ae^{Lt}\). This verifies the required compact-flow well-posedness and stability with constants allowed to depend on the fixed parameters.

## 3. Empirical convergence and propagation of chaos

Let \(\mu_t^R=\mu_t^{\beta,[R]}\), with \(\mu_0^R=f_0^{[R]}\), and couple the particles to
\[
\bar X_i(t)=\Phi_t(X_i(0)),\qquad \bar\mu_t^N=N^{-1}\sum_i\delta_{\bar X_i(t)},
\]
where \(\Phi_t\) is the deterministic nonlinear characteristic flow of \(\mu^R\). For each fixed time, the \(\bar X_i(t)\) are iid with law \(\mu_t^R\). Define
\[
a_N(t)=\mathbb E\frac1N\sum_i|X_i(t)-\bar X_i(t)|,
\qquad e_N(t)=\mathbb E W_1(\bar\mu_t^N,\mu_t^R).
\]
The indexwise coupling and the drift estimate imply
\[
\mathbb E W_1(\mu_t^{N,R},\mu_t^R)\le a_N(t)+e_N(t),
\]
\[
a_N(t)\le2L\int_0^t a_N(s)\,ds+L\int_0^t e_N(s)\,ds.
\]
Since the last integral is nondecreasing in \(t\), Gronwall gives
\[
a_N(t)\le Le^{2Lt}\int_0^t e_N(s)\,ds.
\]

The needed compact empirical Wasserstein convergence can be proved directly. Partition \(B_R\) into finitely many Borel cells \(C_1,\ldots,C_J\) of diameter at most \(h>0\), and choose a representative in each nonempty cell. Moving a law and its empirical measure to these representatives costs at most \(h\) each. If \(p_j\) is a cell probability and \(\widehat p_j\) its empirical frequency, unmatched discrete mass can be transported at distance at most \(2R\). Therefore
\[
\mathbb E W_1(\lambda_N,\lambda)
\le2h+R\sum_{j=1}^J\mathbb E|\widehat p_j-p_j|
\le2h+R\sum_{j=1}^J\sqrt{p_j(1-p_j)/N}.
\]
First let \(N\to\infty\), then \(h\downarrow0\). This proves expected empirical \(W_1\) convergence for every law supported in \(B_R\), without any unverified rate theorem.

Applying this at each fixed \(s\) gives \(e_N(s)\to0\). Also \(0\le e_N(s)\le2R\). The characteristic curves are continuous, so these functions are measurable. Dominated convergence on the finite time interval gives \(\int_0^t e_N(s)\,ds\to0\). Consequently
\[
\mathbb E W_1(\mu_t^{N,R},\mu_t^R)\longrightarrow0
\]
for every fixed \(t\le T\). The usual fixed-particle marginal conclusion also follows: exchangeability and the same coupling bound the \(k\)-particle Wasserstein discrepancy, with sum distance as cost, by \(k a_N(t)\to0\).

An equally valid shorter route to the empirical conclusion applies the pathwise stability estimate from Step 2 directly to the empirical and deterministic initial laws, followed by the compact empirical estimate just proved.

## 4. Posterior continuity and the fixed-radius particle limit

This step applies to arbitrary measures in \(\mathcal P_1\), not just compactly supported measures. Write
\[
k_y(x)=e^{-|y-x|^2/(2\tau)},\quad Z_\nu(y)=\int k_y(x)\,d\nu(x),\quad U_\nu(y)=\int xk_y(x)\,d\nu(x).
\]
For \(|y|\le M\), both \(k_y\) and \(xk_y(x)\) are bounded in \(x\), uniformly in \(y\). Indeed, with \(r=|x-y|\),
\[
|x|k_y(x)\le(M+r)e^{-r^2/(2\tau)}.
\]
Their Lipschitz constants in \(x\) are also uniformly bounded. The relevant derivatives are
\[
\nabla_x k_y(x)=\frac{y-x}{\tau}k_y(x),\qquad
D_x(xk_y(x))=I_d k_y(x)+\frac{x(y-x)^\top}{\tau}k_y(x),
\]
and their norms are bounded by Gaussian-decaying polynomials in \(r\), with constants depending only on \(M,\tau\). Hence, by integrating differences against couplings,
\[
\sup_{|y|\le M}\bigl(|Z_\nu(y)-Z_{\widetilde\nu}(y)|+|U_\nu(y)-U_{\widetilde\nu}(y)|\bigr)
\le C_{M,\tau}W_1(\nu,\widetilde\nu).
\]
The integrals are continuous in \(y\), by bounded convergence on bounded query sets. For any probability measure \(\nu\), \(Z_\nu(y)>0\) everywhere, so
\[
z_{\nu,M}:=\min_{|y|\le M}Z_\nu(y)>0.
\]
If \(W_1(\nu_n,\nu)\to0\), then eventually \(Z_{\nu_n}\ge z_{\nu,M}/2\) on \(B_M\). The quotient identity therefore gives
\[
\sup_{|y|\le M}|m_{\nu_n}^\tau(y)-m_\nu^\tau(y)|\longrightarrow0.
\]
This uses neither a uniform second moment nor a uniform transport-action bound, and it asserts no denominator bound uniform over all probability measures.

When both measures are supported in \(B_R\), the common bound
\[
Z_\nu(y),Z_{\widetilde\nu}(y)\ge e^{-(M+R)^2/(2\tau)}
\]
makes the quotient estimate uniform over that support class:
\[
\sup_{|y|\le M}|m_\nu^\tau(y)-m_{\widetilde\nu}^\tau(y)|
\le C_{M,\tau,R}W_1(\nu,\widetilde\nu).
\]
Now set \(T=T_\beta\). Steps 1–3 and this bound yield, at fixed \(\beta,R\),
\[
\lim_{N\to\infty}\mathbb E\sup_{|y|\le M}
|m_{\mu_{T_\beta}^{N,R}}^\tau(y)-m_{\mu_{T_\beta}^{\beta,[R]}}^\tau(y)|=0.
\]

## 5. Removing the deterministic truncation

For fixed \(\beta\), the class definition supplies
\[
\sup_{0\le t\le T_\beta}W_1(\mu_t^{\beta,[R]},\mu_t^\beta)\to0.
\]
In particular this holds at the terminal time. Applying the general posterior-continuity result from Step 4, with the fixed limiting probability measure \(\mu_{T_\beta}^\beta\), gives
\[
B_{R,\beta}:=\sup_{|y|\le M}
|m_{\mu_{T_\beta}^{\beta,[R]}}^\tau(y)-m_{\mu_{T_\beta}^\beta}^\tau(y)|\longrightarrow0.
\]
The limiting flow here is precisely the associated admissible flow in the definition. No independent noncompact uniqueness theorem is required. If two flows were associated with the same compact truncation flows, their uniform-in-time \(W_1\) distance would be bounded by the sum of their distances to those truncations and hence would be zero.

## 6. Terminal recovery

The other defining property of \(\mathcal A_\tau\) is
\[
W_1(\mu_{T_\beta}^\beta,P_0)\to0\qquad(\beta\to\infty).
\]
Applying Step 4 again, this time with the fixed limit \(P_0\), gives
\[
C_\beta:=\sup_{|y|\le M}|m_{\mu_{T_\beta}^\beta}^\tau(y)-m_{P_0}^\tau(y)|\longrightarrow0.
\]
The observation variance remains \(\tau\) throughout; the bandwidth parameter affects only the flow and its terminal time.

## 7. Ordered expectation limit and posterior interpretation

Let
\[
A_{N,R,\beta}:=\mathbb E\sup_{|y|\le M}
|m_{\mu_{T_\beta}^{N,R}}^\tau(y)-m_{\mu_{T_\beta}^{\beta,[R]}}^\tau(y)|,
\]
and let \(Z_{N,R,\beta}\) be the supremum error against \(m_{P_0}^\tau\) appearing in the task. The triangle inequality gives
\[
\mathbb E Z_{N,R,\beta}\le A_{N,R,\beta}+B_{R,\beta}+C_\beta.
\]
First take \(\limsup_{N\to\infty}\) at fixed \(\beta,R\), using Step 4. Then take \(\limsup_{R\to\infty}\), using Step 5. The result is
\[
0\le\limsup_{R\to\infty}\limsup_{N\to\infty}\mathbb E Z_{N,R,\beta}\le C_\beta.
\]
Step 6 and the squeeze theorem give the stated outer limit as \(\beta\to\infty\). No estimate uniform in \(R\) or \(\beta\), and no joint scaling of these parameters, is used.

These random variables are measurable and integrable. The finite-particle ODE depends continuously on its initial points. The posterior quotient is continuous in both query and finite particle positions. Its supremum over \(B_M\) can be taken over a fixed countable dense subset; for \(M=0\), it is simply evaluation at zero. Moreover the empirical posterior mean lies in \(B_R\), while Step 4 shows that \(m_{P_0}^\tau\) is bounded on \(B_M\). Thus
\[
0\le Z_{N,R,\beta}\le R+\sup_{|y|\le M}|m_{P_0}^\tau(y)|<\infty.
\]

For independent \(X\sim P_0\) and \(Z\sim N(0,\tau I_d)\), the joint law of \((X,Y=X+Z)\) is \(P_0(dx)\gamma_\tau(y-x)\,dy\). Its \(Y\)-density is everywhere positive. Normalizing this joint law at \(y\) gives the posterior probability measure proportional to \(\gamma_\tau(y-x)P_0(dx)\). Its first moment is exactly \(m_{P_0}^\tau(y)\). The finite first moment of \(P_0\) justifies the conditional-expectation identity, and the continuity proved in Step 4 selects its continuous version for every \(y\).

## 8. Probability limit

For each \(\varepsilon>0\), Markov's inequality for the nonnegative integrable error gives
\[
\mathbb P(Z_{N,R,\beta}>\varepsilon)\le\varepsilon^{-1}\mathbb E Z_{N,R,\beta}.
\]
Taking the same ordered limits proves the probability assertion.

All eight obligations are closed. The argument includes zero query radius, every positive truncation radius, every positive integer sample size, and singular clean priors whenever they satisfy the stated class definition.
