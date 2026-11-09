# Reference Proof

## Obligations and Background

The obligations are: finiteness and existence; positivity and Gibbs characterization; uniqueness of the minimizer and of every Gibbs solution in the stated domain; global strong well-posedness and the weak PDE; regular-density gradient-flow identification and dissipation; stationarity and invariance; and contraction from an optimal initial coupling. All are closed below. Quadratic growth is retained as a useful private consequence, not an additional public requirement.

Optimal quadratic-cost couplings exist for any two laws in \(\mathcal P_2\): a minimizing sequence of couplings is tight because its marginals are fixed; a weak limit retains those marginals; and the nonnegative continuous squared cost is lower semicontinuous under that limit. The product coupling has finite cost, so an optimal coupling has finite cost.

We explicitly use the following audited standard-independent optimal-map theorem, included in the transport background indexed by theory_031: if \(\mu,\nu\in\mathcal P_2(\mathbb R^d)\) and \(\mu\) is absolutely continuous with respect to Lebesgue measure, the quadratic-cost Brenier theorem supplies a \(\mu\)-almost-everywhere unique optimal map \(T\), with
\[
T_\#\mu=\nu,\qquad (\mathrm{id},T)_\#\mu\in\Gamma(\mu,\nu),\qquad
\int|T(x)-x|^2\,d\mu=W_2^2(\mu,\nu).
\]
No absolute continuity of the target is required. We use the map only after checking these hypotheses.

We use two audited standard entropy results. First, for a probability reference \(\pi\) and measurable \(g\) with \(\int e^g\,d\pi<\infty\),
\[
\int g\,d\mu\leq\operatorname{KL}(\mu\|\pi)+\log\int e^g\,d\pi.
\]
For bounded \(g\) this follows by expanding the nonnegative KL divergence relative to \(e^g\pi/\int e^g d\pi\); truncation gives the nonnegative unbounded cases used here. This is the relevant independent entropy variational result indexed by theory_030.

Second, relative entropy with respect to \(\pi\propto e^{-U}\), where \(\nabla^2U\succeq\kappa I\), is \(\kappa\)-displacement convex. We also use its standard transport-support inequality: if \(\mu=p\,dx\in\mathcal P_2\) has positive \(C^1\) density, finite relative entropy, and \(\nabla\log(p/\pi)\in L^2(\mu)\), then for \(\nu\in\mathcal P_2\) and the optimal map \(T\) supplied above,
\[
\operatorname{KL}(\nu\|\pi)\geq\operatorname{KL}(\mu\|\pi)+\int\langle\nabla\log(p/\pi),T-x\rangle\,d\mu+\frac\kappa2W_2^2(\mu,\nu).
\]
It suffices to use this when the target entropy is finite; otherwise the lower bound is automatic. These are the independent entropy transport results indexed by theory_031. We do not invoke existence of an EVI flow or identify arbitrary weak laws with an EVI flow.

## Finiteness, Coercivity, and Existence

Write \(s=2-\varepsilon\in[0,2)\). The growth assumptions and finite second moments make \(\mathcal J,A,\mathcal R,B\) finite, including the empty-product case \(m=1\). Quadratic confinement normalizes \(\pi\) and gives finite moments of every order. Thus \(\mathcal E(\pi)<\infty\).

For every \(a>0\), \(\int e^{a|x|^s}\,d\pi<\infty\). For \(s>0\), this follows by absorbing \(a|x|^s\) into a strictly smaller quadratic term than the confining lower bound; for \(s=0\) the integrand is constant. The entropy inequality gives
\[
|\mathcal J(\mu)|\leq C_a+\frac{mC_H}{a}\operatorname{KL}(\mu\|\pi).
\]
Since \(\mathcal R\geq q_{\min}/2\), choose \(a>mC_H/\lambda\), obtaining
\[
\mathcal E(\mu)\geq-C_a+\eta q_{\min}/2+(\lambda-mC_H/a)\operatorname{KL}(\mu\|\pi).
\]
For \(0<c<a_U\), another application to \(c|x|^2\) gives
\[
M_2(\mu)\leq c^{-1}\operatorname{KL}(\mu\|\pi)+c^{-1}\log\int e^{c|x|^2}\,d\pi.
\]
Consequently finite-energy sublevels have bounded entropy and second moments, uniformly along a minimizing sequence.

Take a weakly convergent subsequence by tightness. The lower semicontinuity of the second moment puts its limit in \(\mathcal P_2\). Relative entropy is weakly lower semicontinuous, as also follows from its variational supremum over bounded continuous functions. The continuous pair integrand \(q(x-y)/2\) is bounded below, so product weak convergence and Portmanteau give lower semicontinuity of \(\mathcal R\).

For \(0<s<2\), the estimate \(|x|^s\mathbf1_{|x|>R}\leq R^{s-2}|x|^2\) gives uniform integrability of the subquadratic coordinate powers. For products, the other-coordinate tail terms are bounded using independence, bounded \(s\)-moments, and the second-moment tail probability bound. Hence \(1+\sum_j|x_j|^s\) is uniformly integrable under the product laws. Truncation and product weak convergence give continuity of \(\mathcal J\). When \(s=0\), \(H\) is bounded and ordinary weak convergence suffices. Therefore the weak limit attains the infimum. Denote a minimizer by \(\mu^*\).

## Positivity and the Gibbs Equation

Finite energy implies finite KL and \(\mu^*\ll\pi\). If its relative density vanishes on a Borel set \(D\) with \(\pi(D)>0\), set \(\nu_D=\pi(\cdot\mid D)\) and \(\mu_h=(1-h)\mu^*+h\nu_D\). This conditional law has finite second moment. The utility and interaction changes have finite one-sided derivatives by their product expansions. The entropy equals
\[
(1-h)\operatorname{KL}(\mu^*\|\pi)+(1-h)\log(1-h)+h\log\bigl(h/\pi(D)\bigr),
\]
whose derivative at zero is minus infinity. This contradicts minimality. Thus the relative density is positive \(\pi\)-almost everywhere.

Permutation symmetry and evenness give, respectively,
\[
\frac{\delta\mathcal J}{\delta\mu}=mA,\qquad
\frac{\delta\mathcal R}{\delta\mu}=B.
\]
The first follows by expanding the product in a signed perturbation and identifying its \(m\) identical linear terms. The second follows by expanding the pair product and using evenness to identify the two half-weighted linear terms. For relative entropy the variation is \(\log(d\mu/d\pi)+1\).

At \(\mu^*\), test with \((1+h\varphi)\mu^*\) for bounded \(\varphi\) of zero \(\mu^*\)-mean. The derivative vanishes, so
\[
-mA(x;\mu^*)+\eta B(x;\mu^*)+\lambda\log\frac{d\mu^*}{d\pi}(x)=C.
\]
These variations are justified by finite entropy, integrable growth, and bounded multiplicative perturbations. Finite KL also makes the logarithmic density ratio integrable: its negative part is integrable because \(u\log u\) is bounded below. Exponentiating gives the Gibbs equation. Its normalizer is finite and positive because the resulting density integrates to one.

## Convexity and Uniqueness

Let \((X,Y)\) have an optimal coupling and write \(D=Y-X\), \(X_t=X+tD\). Using \(m\) independent copies, the full Hessian bound gives
\[
\frac{d^2}{dt^2}[-\mathcal J(\mu_t)]\geq-mL_H\mathbb E|D|^2.
\]
For an independent copy \((X',Y',D')\),
\[
\frac{d^2}{dt^2}\mathcal R(\mu_t)
\geq-\frac{L_q}{2}\mathbb E|D-D'|^2
=-L_q\bigl(\mathbb E|D|^2-|\mathbb ED|^2\bigr)
\geq-L_q\mathbb E|D|^2.
\]
The audited entropy displacement-convexity result therefore makes \(\mathcal E\) \(\alpha\)-displacement convex. This proves uniqueness of the minimizer. Applying the convexity inequality along a geodesic from a minimizer, using minimality, dividing by its interpolation parameter, and letting that parameter decrease to zero gives
\[
\mathcal E(\nu)-\mathcal E(\mu^*)\geq\frac\alpha2W_2^2(\nu,\mu^*).
\]

It remains to show that every Gibbs solution is a minimizer; mixture criticality alone would not suffice. Suppose \(\mu\in\mathcal P_2\) solves the Gibbs equation. Its logarithmic relative density has at most quadratic growth because \(A\) has subquadratic growth and \(B\) has quadratic growth. Hence its relative entropy is finite. Differentiation under the defining integrals makes \(A,B\) \(C^2\), and the Gibbs law has a positive \(C^2\) Lebesgue density \(p\). Moreover,
\[
\nabla\log(p/\pi)=(m\nabla A-\eta\nabla B)/\lambda
\]
has at most linear growth and belongs to \(L^2(\mu)\).

For any finite-energy \(\nu\), both \(\mu\) and \(\nu\) belong to \(\mathcal P_2\), and \(\mu=p\,dx\) is Lebesgue absolutely continuous. Thus the audited Brenier theorem supplies an optimal map \(T\) from \(\mu\) to \(\nu\), with \(\int|T-x|^2\,d\mu=W_2^2(\mu,\nu)\). Set \(D=T-\mathrm{id}\). Taylor's inequality, integrated over independent product copies, gives
\[
-\mathcal J(\nu)\geq-\mathcal J(\mu)-m\int\langle\nabla A,D\rangle\,d\mu-\frac{mL_H}{2}\int|D|^2\,d\mu.
\]
The analogous pair Taylor inequality, using evenness and \(\mathbb E|D-D'|^2\leq2\mathbb E|D|^2\), gives
\[
\mathcal R(\nu)\geq\mathcal R(\mu)+\int\langle\nabla B,D\rangle\,d\mu-\frac{L_q}{2}\int|D|^2\,d\mu.
\]
All linear terms are integrable by linear gradient growth and Cauchy-Schwarz. Adding the audited entropy transport-support inequality gives
\[
\mathcal E(\nu)\geq\mathcal E(\mu)+\int\langle-m\nabla A+\eta\nabla B+\lambda\nabla\log(p/\pi),D\rangle\,d\mu+\frac\alpha2W_2^2(\mu,\nu).
\]
The linear term vanishes by the Gibbs formula. Infinite-energy targets cause no difficulty. Thus \(\mu\) is a minimizer and equals \(\mu^*\).

## Drift Bounds and Global Well-Posedness

Differentiation under the integrals is justified by the derivative growth bounds and finite moments. The Hessian bounds imply
\[
|b(x,\mu)-b(y,\mu)|\leq L_x|x-y|,
\qquad L_x=mL_H+\eta L_q+\lambda K_U.
\]
Couple \(m-1\) independent pairs with the optimal law coupling. Jensen's inequality and the full Hessian bound yield
\[
|\nabla A(x;\mu)-\nabla A(x;\nu)|\leq L_H\sqrt{m-1}\,W_2(\mu,\nu).
\]
The same one-pair argument gives the bound \(L_qW_2\) for \(\nabla B\). Therefore the task's fixed \(L_\mu\) is a valid uniform law-Lipschitz constant. For \(m=1\), the conditional utility does not depend on the law and its contribution is zero. Also,
\[
|b(x,\mu)|\leq |b(0,\delta_0)|+L_x|x|+L_\mu M_2(\mu)^{1/2}.
\]
Uniform convexity of \(U\) and the state gradient bounds give
\[
\langle x-y,b(x,\mu)-b(y,\mu)\rangle\leq-\alpha|x-y|^2.
\]

Here is the law fixed-point construction rather than an unclosed specialized citation. For a prescribed continuous law curve \(\sigma\) on \([0,T]\), solve the frozen equation with drift \(b(x,\sigma_t)\). Its integral equation is an ordinary Picard equation with the continuous additive Brownian forcing. Global state Lipschitzness gives pathwise existence and uniqueness; linear growth gives a finite second-moment supremum. Map \(\sigma\) to its solution law curve.

For two prescribed curves with the same initial variable and Brownian motion, the pathwise integral inequality gives
\[
\sup_{t\leq T}\mathbb E|X_t^\sigma-X_t^\tau|^2
\leq L_\mu^2T^2e^{2L_xT}\sup_{t\leq T}W_2^2(\sigma_t,\tau_t).
\]
For small \(T\) this is a contraction on the complete space of continuous \(\mathcal P_2\)-curves with the prescribed initial law. If \(L_\mu=0\), the map is constant. Iterating these fixed-length intervals constructs the global adapted strong solution. The growth estimate, the Brownian maximal second-moment bound, and Gronwall give
\[
\mathbb E\sup_{t\leq T}|X_t|^2\leq C_T(1+M_2(\mu_0)),
\]
preventing finite-time explosion. The same difference estimate gives pathwise uniqueness for a fixed initial variable and noise. The fixed-point construction also gives uniqueness of the law curve for a prescribed initial distribution: the frozen solution law depends only on that distribution and the independent Brownian motion, and the law map has a unique fixed point on successive short intervals. Mean-square continuity implies continuity of the law in \(W_2\). Itô's formula for compactly supported smooth tests gives exactly the weak PDE in the task.

## Regular Gradient-Flow Structure and Dissipation

For a regular density \(p\), the first variation is, up to a constant,
\[
f=-mA+\eta B+\lambda\bigl(\log(p/\pi)+1\bigr).
\]
Consequently
\[
\nabla f=-b+\lambda\nabla\log p,
\qquad
\partial_tp=\nabla\cdot(p\nabla f).
\]
This is the requested smooth-density Wasserstein gradient-flow identification, not an EVI identification for arbitrary weak laws.

On each compact time interval the public domination conditions justify differentiation of the utility, pair interaction, and entropy integrals. They also control \(\int|f\partial_tp|\) and \(\int p|\nabla f|^2\): uniformly on that interval, \(|f|\leq C(1+|x|^2+|\log p|)\) and \(|b|\leq C(1+|x|)\). The public boundary condition controls the absolute boundary term in integration by parts because \(p\nabla f=-bp+\lambda\nabla p\). Thus
\[
\frac d{dt}\mathcal E(\mu_t)=\int f\partial_tp_t\,dx
=-\int p_t|\nabla f|^2\,dx\leq0
\]
for almost every positive time. No assertion is made that the energy identity is already justified for every arbitrary weak initial law.

## Stationarity and Invariance

The positive \(C^2\) Gibbs density \(p^*\) satisfies
\[
b(x,\mu^*)=\lambda\nabla\log p^*(x).
\]
Compactly supported integration by parts therefore gives
\[
\int\bigl(b(x,\mu^*)\cdot\nabla\varphi+\lambda\Delta\varphi\bigr)p^*(x)\,dx=0.
\]
This proves stationary weak PDE status without requiring \(p^*\) to belong to the public regular time-dependent class. We now prove the additional forward-equation uniqueness bridge needed for SDE invariance.

### Frozen Forward-Equation Uniqueness

Let \(c:\mathbb R^d\to\mathbb R^d\) be globally Lipschitz, with Lipschitz constant \(L\) and thus linear growth. Fix a finite \(T\). Consider probability curves \(\rho\in C([0,T];\mathcal P_2)\), where continuity is in \(W_2\), satisfying
\[
\int\psi\,d\rho_t-\int\psi\,d\rho_0
=\int_0^t\int(c\cdot\nabla\psi+\lambda\Delta\psi)\,d\rho_s\,ds
\]
for every \(\psi\in C_c^\infty\). We prove that such a curve is uniquely determined by \(\rho_0\). This precise class contains both the frozen SDE law and the constant curve needed below.

Choose a nonnegative smooth unit-mass mollifier supported in the unit ball, and set \(c_n=c*\zeta_{1/n}\). Then
\[
\|c_n-c\|_\infty\leq L/n,\qquad \operatorname{Lip}(c_n)\leq L.
\]
The functions \(c_n\) are smooth with linear growth and bounded derivatives of every positive order, with higher-derivative bounds allowed to depend on \(n\).

For \(\varphi\in C_c^\infty\), solve the additive-noise SDE with drift \(c_n\), initial point \(x\), and write its transition semigroup as \(P_t^n\). This solution is obtained by the same Brownian-forcing Picard construction already used above. Define
\[
u_n(s,x)=P_{T-s}^n\varphi(x),\qquad 0\leq s\leq T.
\]
Here the symbol \(u_n\) denotes a function, not a probability law. The following properties follow directly from the smooth stochastic flow and Itô's formula:
\[
\partial_su_n+c_n\cdot\nabla u_n+\lambda\Delta u_n=0,
\qquad u_n(T,x)=\varphi(x),
\]
\[
\|u_n\|_\infty\leq\|\varphi\|_\infty,
\qquad
\|\nabla u_n\|_\infty\leq e^{LT}\|\nabla\varphi\|_\infty.
\]
We give the construction details to avoid assuming an unstated backward PDE theorem. For the smooth flow \(Y_t^{n,x}\), its first spatial derivative \(J_t\) solves
\[
\dot J_t=Dc_n(Y_t^{n,x})J_t,\qquad J_0=I,
\]
so \(\|J_t\|\leq e^{Lt}\). Its second spatial derivative in directions \(h,k\) solves the linear equation with forcing
\[
D^2c_n(Y_t^{n,x})[J_th,J_tk].
\]
Bounded \(D^2c_n\) and the bound on \(J_t\) therefore give a deterministic finite bound on this second derivative for \(t\leq T\), depending on \(n,T\). Differentiating the expectation defining \(P_t^n\varphi\) is justified by these bounds. It gives continuous bounded first and second spatial derivatives and the displayed gradient estimate.

With \(\mathcal L_n=c_n\cdot\nabla+\lambda\Delta\), Itô's formula gives
\[
P_t^n\varphi=\varphi+\int_0^tP_r^n\mathcal L_n\varphi\,dr.
\]
The function \(\mathcal L_n\varphi\) is bounded and continuous, so this gives the continuous time derivative \(\partial_tP_t^n\varphi=P_t^n\mathcal L_n\varphi\). The semigroup property and Itô's formula applied to the bounded \(C^2\) function \(P_t^n\varphi\) identify the same derivative with \(\mathcal L_nP_t^n\varphi\). Localization and the linear-growth moment bound justify this application; its spatial derivatives are bounded and its generator has at most linear growth. Consequently \(u_n\) is a \(C^{1,2}\) solution of the asserted backward equation, with bounded spatial derivatives on this finite horizon. Its time derivative is bounded as well, by the preceding formula.

For a forward curve \(\rho\), its compact-test weak identity extends to compactly spatially supported \(C^{1,2}\) time-dependent tests. Indeed, finite sums of time functions times smooth spatial tests give the integrated identity by the product rule; approximation on compact time-space sets in the time derivative and the spatial derivatives through order two gives the claimed extension. Linear growth of \(c\) causes no difficulty on those compact sets.

Choose smooth cutoffs \(\chi_R\) equal to one on \(B_R\), zero outside \(B_{2R}\), with \(|\nabla\chi_R|\leq C/R\) and \(|\Delta\chi_R|\leq C/R^2\). Apply the time-dependent identity to \(\chi_Ru_n\). The backward equation leaves the main term
\[
\chi_R(c-c_n)\cdot\nabla u_n
\]
and cutoff terms
\[
u_n c\cdot\nabla\chi_R+2\lambda\nabla\chi_R\cdot\nabla u_n+\lambda u_n\Delta\chi_R.
\]
In this display, the first and last factors are the function \(u_n\). Since \(\rho\) is \(W_2\)-continuous on a compact interval,
\[
M=\sup_{s\leq T}M_2(\rho_s)<\infty.
\]
On \(R\leq|x|\leq2R\), linear growth of \(c\) and the bounds on \(u_n,\nabla u_n\) bound the absolute cutoff terms by
\[
C_{T,\varphi,c,\lambda}\bigl((1+|x|)/R+1/R+1/R^2\bigr)\mathbf1_{|x|\geq R}.
\]
For \(R\geq1\), their integral over \(\rho_s\) is at most a constant times \(M/R^2\), uniformly in \(s\). They therefore vanish after time integration as \(R\to\infty\). Boundedness of \(u_n\) handles the endpoint limits, and the uniform bound on \(c-c_n\) handles the main-term limit. We obtain
\[
\int\varphi\,d\rho_T-\int u_n(0,x)\,\rho_0(dx)
=\int_0^T\int(c-c_n)\cdot\nabla u_n\,d\rho_s\,ds.
\]
The absolute value of the right side is at most
\[
\frac{TL}{n}e^{LT}\|\nabla\varphi\|_\infty.
\]
For two such curves \(\rho,\widetilde\rho\) with the same initial law, subtract their identities. The initial terms agree, so
\[
\left|\int\varphi\,d\rho_T-\int\varphi\,d\widetilde\rho_T\right|
\leq\frac{2TL}{n}e^{LT}\|\nabla\varphi\|_\infty.
\]
Letting \(n\to\infty\) proves equality for all compactly supported smooth tests. Such tests determine Borel probability measures, so \(\rho_T=\widetilde\rho_T\). Apply the same argument on every shorter horizon to obtain equality of the curves. This proves the required frozen forward-equation uniqueness; it does not claim uniqueness for an unspecified larger weak-solution class.

### Application to the Gibbs Law

Take \(c(x)=b(x,\mu^*)\). The drift bounds prove that \(c\) is globally Lipschitz with linear growth. The frozen SDE started from \(\mu^*\) has a \(W_2\)-continuous finite-second-moment law curve and solves its linear forward equation by Itô's formula. The constant curve \(\rho_t=\mu^*\) belongs to the same class and solves that equation by the stationary calculation. The uniqueness argument just proved identifies these curves. Thus the frozen SDE has law \(\mu^*\) at every time. It consequently also solves the nonlinear SDE, since its law-dependent drift is exactly \(b(\cdot,\mu^*)\). Nonlinear uniqueness from the fixed-point construction proves that starting the McKean-Vlasov SDE from \(\mu^*\) preserves its law.

## Contraction and Convergence

Choose an optimal initial coupling independent of the Brownian motion, and run both unique strong solutions with the same Brownian motion. For \(\Delta_t=X_t-\widetilde X_t\), cancellation of the additive noise, state dissipativity, and the law-Lipschitz bound give
\[
\frac d{dt}\mathbb E|\Delta_t|^2
\leq-2\alpha\mathbb E|\Delta_t|^2
+2L_\mu W_2(\mu_t,\widetilde\mu_t)\mathbb E|\Delta_t|.
\]
The current pair is a coupling, so its last product is at most \(\mathbb E|\Delta_t|^2\). The inequalities hold almost everywhere in time; finite-horizon moment bounds justify them. Gronwall yields
\[
W_2^2(\mu_t,\widetilde\mu_t)
\leq\mathbb E|\Delta_t|^2
\leq e^{-2\delta t}W_2^2(\mu_0,\widetilde\mu_0).
\]
Taking square roots proves the target estimate for all \(t\geq0\). With the second solution started from the invariant law \(\mu^*\), it also proves exponential convergence to that unique Gibbs minimizer. Every argument includes \(\eta=0\), \(m=1\), and zero interaction Hessian constants whenever the stated strict conditions hold.
