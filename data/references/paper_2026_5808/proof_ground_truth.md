# Reference Proof

## Obligations and source coverage

The obligations are: (i) construct and verify a weighted one-step contraction, including its augmented-coordinate estimate and reference-point integrability; (ii) obtain an invariant law and uniqueness among all Borel invariant probability laws; (iii) establish the driving-chain Poisson estimates and identify the covariance; (iv) justify stationary moments, tightness, and Lindeberg control; (v) derive the limiting stationary generator, including all Poisson correction terms; and (vi) establish existence, uniqueness, and stationary-generator characterization for the possibly degenerate limiting diffusion.

The derivations below recover these obligations from the supplied Appendix A and Appendix B. The contractive-drift framework cited as background is not used as a black-box contraction theorem. The only specialized independent result used at the final identification step is the stationary martingale-problem criterion, stated with its relevant hypotheses below.

Throughout, constants denoted by C or c may change, but do not depend on the sufficiently small stepsize. Estimates stated uniformly in x and xi have constants independent of these variables. Innovations used in a transition are independent of the current state.

## 1. Jacobian estimates and the weight

Write A(x,xi)=D_x G(x,xi), and A_s=(A+A^T)/2. Co-coercivity and Cauchy--Schwarz give

\[
\|G(x,\xi)-G(y,\xi)\|\le L_G\|x-y\|.
\]

Taking directional difference quotients gives

\[
\|Av\|^2\le L_G\langle v,A_sv\rangle,
\qquad 0\preceq A_s\preceq L_GI.
\]

The conditional mean-perturbation inequality implies

\[
\mathbb E A_s(x,\Phi(\xi,U))\succeq(1-\theta)\nabla^2H(x).
\]

Differentiation under expectation is justified by the uniform Lipschitz bound on G. Thus, with L_h=L_G/(1-theta) and L_x=L_G+L_h,

\[
0\preceq\nabla^2H\preceq L_hI,
\qquad \|D_xg(x,\xi)\|\le L_x.
\]

Consequently h and g are globally Lipschitz in x, the latter uniformly in xi. Since h(0)=0, Jensen's inequality applied to h(x)=integral_0^1 Hess H(tx)x dt gives

\[
\|h(x)\|^2\le\int_0^1\|\nabla^2H(tx)x\|^2dt
\le L_h\langle x,h(x)\rangle.
\]

For alpha L_G<=1,

\[
\|(I-\alpha A)v\|^2
\le\|v\|^2-\alpha\langle v,A_sv\rangle.
\]

Therefore the update is samplewise nonexpansive in x. For unit e, writing xi^+=Phi(xi,U), f(x)=x-alpha G(x,xi^+), and D=||(I-alpha A(x,xi^+))e||, we have

\[
0\le D\le1,
\qquad
\mathbb ED\le1-\frac{\alpha(1-\theta)}2
\langle e,\nabla^2H(x)e\rangle.
\tag{1}
\]

Define T=1 when beta=2. When beta<2, put q=2-beta in (0,1] and

\[
T(x)=\exp\{\kappa(\|x\|^q-(3R_H/4)^q)_+\}.
\]

For m=2, put omega=0 and delta_alpha=0. For m>2, put

\[
s=\min\{m-2,1\},\qquad
\omega(x)=\left(1-(2\|x\|/R_H)^s\right)_+,
\]
\[
\delta_\alpha=
\begin{cases}
\kappa_0\alpha,&2<m\le3,\\
\kappa_0\alpha^{m-2},&m>3.
\end{cases}
\]

Set V_alpha(x,xi)=V_alpha(x)=T(x)+delta_alpha omega(x). This weight is continuous, at least one, and delta_alpha<=kappa_0 alpha for alpha<=1. The choices of kappa and then kappa_0 are sufficiently small fixed constants.

### Tail and positive-increment estimates

For beta<2, exponential integrability gives uniform exponential moments of ||g(x,xi^+)|| on every fixed bounded x-region. If ||x||<=R_H/2, T(f(x))>1 requires ||g(x,xi^+)||>=c/alpha, after reducing alpha. Since q<=1, the exponential defining T(f(x)) is bounded by exp(C kappa(1+alpha||g||)). Exponential-tail integration yields

\[
\mathbb E[T(f(x))-1]\le Ce^{-c/\alpha},
\qquad \|x\|\le R_H/2.
\tag{2}
\]

For beta=2 the left side is zero. On ||x||<=R_H, split at ||g||<=alpha^{-1/2}. On this event T is C kappa-Lipschitz on a fixed enlargement of the ball, giving expected positive increment at most C kappa alpha. On its complement exponential integrability gives a bound C kappa exp(-c alpha^{-1/2}). The omega increment is at most delta_alpha. Hence

\[
\mathbb E[(V_\alpha(f(x))-V_\alpha(x))_+]
\le C(\kappa+\kappa_0)\alpha V_\alpha(x),
\quad \|x\|\le R_H,
\tag{3}
\]

with kappa=0 in the quadratic-tail case; there the omega bound alone proves (3).

For beta<2 and r=||x||>=R_H, set N=||g(x,xi^+)||/(1+r^{beta-1}), and choose eta in (0,1/2). On N<=alpha^{-eta}, the step has norm at most C alpha^{1-eta}r^{beta-1}, and the segment remains outside radius 3R_H/4. Taylor expansion of ||x||^q gives

\[
\|f(x)\|^q-r^q
\le-q\alpha r^{-\beta}\langle x,h(x)+\bar g(x,\xi)\rangle
-q\alpha r^{-\beta}\langle x,g(x,\xi^+)-\bar g(x,\xi)\rangle
+C\alpha^{2-2\eta}.
\]

The first term is at most -q c_diss alpha. The second is alpha times a centered variable having a uniform exponential moment. To justify its exponential estimate, if Z is centered and E exp(lambda|Z|)<=M, Taylor's inequality gives E exp(tZ)<=1+C t^2<=exp(C t^2) for sufficiently small |t|. Thus the expected weight on this event is at most

\[
T(x)\exp\{-c\alpha+C\alpha^{2-2\eta}\}.
\]

Concavity of r^q also gives the global upper comparison

\[
T(f(x))\le T(x)\exp\{C\kappa\alpha(1+N)\}.
\]

It remains valid if f(x) crosses the cutoff, since then T(f(x))<=T(x). On N>alpha^{-eta}, exponential integrability bounds the expectation by C T(x)exp(-c alpha^{-eta}). Consequently

\[
\mathbb ET(f(x))\le(1-c\alpha)T(x),\qquad r\ge R_H.
\tag{4}
\]

The same global comparison and e^t-1<=te^t imply that the positive increment of T has expectation at most C alpha T(x). Including the bounded correction and (3) gives, in both tail regimes,

\[
\mathbb E[(V_\alpha(f(x))-V_\alpha(x))_+]
\le C_+\alpha V_\alpha(x),
\qquad
\mathbb EV_\alpha(f(x))\le(1+C_V\alpha)V_\alpha(x).
\tag{5}
\]

Since 0<=L_Phi<=1, this also proves the joint estimate, without assuming independence between L_Phi and the update,

\[
\mathbb E[L_\Phi(U)V_\alpha(f(x))]
\le(\rho_\Xi+C_+\alpha)V_\alpha(x).
\tag{6}
\]

### Core directional contraction

For m>2, nondegeneracy implies, for sufficiently small alpha,

\[
\inf_\xi\mathbb E\min\{(\alpha\|g(0,\xi^+)\|)^s,1\}
\ge p_g\varepsilon_g^s\alpha^s.
\tag{7}
\]

For r=||x||<=R_H/2, write

\[
f(x)=-\alpha g(0,\xi^+)+v,
\qquad \|v\|\le Cr.
\]

This follows from the local bound on h and the uniform x-Lipschitz bound on g. The s-Hölder continuity of omega gives

\[
\mathbb E\omega(f(x))-\omega(x)
\le-c\mathbb E\min\{(\alpha\|g(0,\xi^+)\|)^s,1\}+Cr^s.
\]

Combining this with (1), (2), and D<=1 yields

\[
\mathbb E[D V_\alpha(f(x))]-V_\alpha(x)
\le-a\alpha r^{m-2}-c\delta_\alpha\alpha^s
+C\delta_\alpha r^s+Ce^{-c/\alpha}.
\tag{8}
\]

If 2<m<=3, s=m-2 and delta_alpha=kappa_0 alpha; choosing kappa_0 small absorbs the positive r^s term and leaves a decrease c alpha^{m-1}. If m>3, s=1. Young's inequality, with exponent (m-2)/(m-3), gives

\[
C\kappa_0\alpha^{m-3}r
\le(a/2)r^{m-2}
+C_*\kappa_0^{(m-2)/(m-3)}\alpha^{m-2}.
\]

After multiplication by alpha, the last term is absorbed by c kappa_0 alpha^{m-1} for sufficiently small kappa_0. The exponential remainder is negligible. Since V_alpha is uniformly bounded in this core, (8) gives a multiplicative contraction by 1-c alpha^{m-1}.

For m=2, omega=0 and local curvature in (1), together with (2), directly gives contraction by 1-c alpha. No nondegeneracy assumption is used in this case.

### Bridge and far regions

On R_H/2<=||x||<=R_H, (1) gives ED<=1-c alpha. Combining it with (3), and choosing kappa and kappa_0 small, gives

\[
\mathbb E[D V_\alpha(f(x))]\le(1-c\alpha)V_\alpha(x).
\]

For ||x||>=R_H and beta=2, V_alpha(x)=1 and the tail Hessian bound gives ED<=1-c alpha; the possible correction at f(x) is at most delta_alpha and is absorbed by choosing kappa_0 small. For beta<2, omega(x)=0, and (4) gives

\[
\mathbb E[D V_\alpha(f(x))]
\le(1-c\alpha)T(x)+\delta_\alpha.
\]

Again choose kappa_0 sufficiently small. Because alpha>=alpha^{m-1}, these estimates and the core estimate prove, uniformly in x, xi, and unit e,

\[
\mathbb E[D V_\alpha(f(x))]
\le(1-c_0\alpha^{m-1})V_\alpha(x).
\tag{9}
\]

## 2. Augmented contraction and the invariant law

Let gamma(t)=(x(t),xi(t)) be an absolutely continuous joining curve. For fixed u, the composed curve F_u(gamma(t)) is absolutely continuous: the driving map is Lipschitz, G is uniformly Lipschitz in x, and g(x,Phi(xi,u)) is uniformly Lipschitz in xi. Its base-norm metric derivative satisfies almost everywhere

\[
\operatorname{md}_\alpha(F_u\circ\gamma)
\le\|(I-\alpha A(x,\Phi(\xi,u)))\dot x\|
+(L_\Phi(u)+\alpha^2L_{g,\Phi})\alpha^{-1}\|\dot\xi\|.
\]

For the x derivative, freeze the driving argument at the current path point. The remaining change in the x-coordinate is bounded by alpha L_{g,Phi}||dot xi||; this explains the alpha^2 term after factoring out alpha^{-1}.

Multiply by V_alpha of the image point, integrate, and take expectation. Equations (5), (6), and (9) apply to the fixed path directions. Reduce alpha_0 so that

\[
\rho_\Xi+C_+\alpha+\alpha^2L_{g,\Phi}(1+C_V\alpha)
\le1-c_0\alpha^{m-1}.
\]

This is possible because rho_Xi<1. Taking the infimum over joining curves gives

\[
\mathbb E d_{V_\alpha,\alpha}(F_U(z),F_U(z'))
\le(1-c_0\alpha^{m-1})d_{V_\alpha,\alpha}(z,z').
\tag{10}
\]

For z_*=(0,xi_*), move first in the xi-coordinate at x=0 and then along the radial x-segment to -alpha g(0,Phi(xi_*,U)). The first path cost has finite mean by reference-point integrability. For beta=2 the weight is bounded, so the second cost is bounded by (1+delta_alpha)alpha||g(0,Phi(xi_*,U))||. For beta<2 it is bounded by

\[
C\alpha\|g(0,\Phi(\xi_*,U))\|
\{1+\exp(C\kappa\alpha^{2-\beta}\|g(0,\Phi(\xi_*,U))\|^{2-\beta})\}.
\]

This is integrable for sufficiently small alpha by the exponential assumption, since 2-beta<=1. Thus E d(F_U(z_*),z_*)<infinity.

The induced metric dominates the augmented base metric. On bounded convex subsets, straight segments and boundedness of the continuous weight give the converse local comparison. Hence it has the usual topology, is separable, and is complete: an induced-metric Cauchy sequence has a base-metric limit in the closed state space and converges in the induced metric by local comparison.

For any coupling of two initial laws, use independent fresh innovations synchronously for its two coordinates. Equation (10) proves Wasserstein contraction, including when the two laws individually lack first moments but their mutual cost is finite. Reference-point integrability shows that P_alpha maps P_1 into itself. Starting from delta_{z_*}, successive laws have distances bounded by a geometric sequence, hence converge in the complete Wasserstein space to a law pi_alpha. Contraction proves pi_alpha P_alpha=pi_alpha and the asserted n-step bound.

For uniqueness beyond P_1, first note that every fixed-state law delta_z P_alpha^n converges to pi_alpha in this Wasserstein distance. Thus P_alpha^n phi(z) converges to pi_alpha(phi) for every bounded induced-metric Lipschitz phi. If another Borel probability is invariant, integrate this pointwise convergence against it and use bounded convergence. Bounded Lipschitz functions determine probability laws, so it equals pi_alpha.

## 3. Driving-chain Poisson estimates and covariance

The driving chain is contractive in ordinary W_1 with factor rho_Xi, and the reference-point condition makes its kernel Q preserve P_1. The same fixed-point and bounded-test-function argument proves existence and uniqueness of pi_Xi among all Borel invariant laws. The xi-marginal of pi_alpha is invariant for Q, so it equals pi_Xi.

Write g_x(zeta)=g(x,zeta). Coupling a chain started at xi to a stationary chain and applying the composed-noise Lipschitz condition at the final transition yields, for k>=1,

\[
\|Q^kg_x(\xi)\|
\le L_{g,\Phi}\rho_\Xi^{k-1}
\left(\|\xi-\xi_*\|+\mathbb E_{\pi_\Xi}\|\eta-\xi_*\|\right).
\tag{11}
\]

One may replace rho_Xi by any fixed number in (rho_Xi,1) in geometric bounds, covering rho_Xi=0 without endpoint conventions. Stationary centering is used in (11). The series

\[
\chi_x=\sum_{k\ge1}Q^kg_x
\]

therefore converges absolutely, satisfies chi_x-Qchi_x=Qg_x, and is centered under pi_Xi. With R(xi)=1+||xi-xi_*||,

\[
\|\chi_x(\xi)\|\le CR(\xi),\qquad R\in L^2(\pi_\Xi).
\tag{12}
\]

Termwise application of Q is justified by summing the geometric bounds and one-step first-moment integrability. The uniform x-Lipschitz estimate gives ||Q^k(g_x-g_y)||<=L_x||x-y||. Applying (11) separately to g_x and g_y gives an alternative bound C rho_Xi^{k-1}R(xi). Using min(a,b)<=a^p b^{1-p} and summing gives, for each p in (0,1),

\[
\|\chi_x(\xi)-\chi_y(\xi)\|
\le C_p\|x-y\|^pR(\xi)^{1-p}.
\tag{13}
\]

Define

\[
D_x(\xi,U)=g_x(\xi^+)+\chi_x(\xi^+)-\chi_x(\xi).
\]

The Poisson equation gives conditional mean zero and

\[
g_x(\xi^+)=D_x(\xi,U)+\chi_x(\xi)-\chi_x(\xi^+).
\tag{14}
\]

At x=0 all terms are square-integrable under the stationary transition law. By (11) and Cauchy--Schwarz,

\[
\|\Gamma_k\|\le C\rho_\Xi^{k-1},\qquad k\ge1.
\]

Thus the defining Green--Kubo series is absolutely convergent. For stationary noise f_n=g(0,xi_n), (14) gives

\[
\sum_{n=1}^N f_n=\sum_{n=0}^{N-1}D_0(\xi_n,U_{n+1})
+\chi_0(\xi_0)-\chi_0(\xi_N).
\]

The martingale sum has covariance N E[D_0D_0^T]. The boundary term has bounded second moment; its covariance divided by N vanishes, and its cross covariance with the martingale sum divided by N is O(N^{-1/2}). Expanding the covariance of the stationary noise sum using the absolutely summable lag covariances proves

\[
\Sigma=\mathbb E[D_0D_0^T]\succeq0.
\tag{15}
\]

For later use, a bounded Lipschitz centered scalar f has a solution u=sum_{k>=0}Q^k f to u-Qu=f. Indeed, synchronous coupling gives

\[
|Q^kf(\xi)|\le\min\{2\|f\|_\infty,C\rho_\Xi^k(1+\|\xi-\xi_*\|)\}.
\]

Summation proves absolute convergence, a Lipschitz bound, and growth at most C(1+log(1+||xi-xi_*||)). Thus u is in L^2(pi_Xi), even using only the first moment of pi_Xi.

## 4. Stationary moments, tightness, and Lindeberg control

Put a(x)=<x,h(x)>. Integration of the local Hessian inequality gives

\[
a(x)\ge\frac{c_{in}}{m-1}\|x\|^m,\qquad \|x\|\le R_H.
\tag{16}
\]

Radial convexity makes a(x) bounded away from zero outside any fixed sufficiently small ball. The tail assumptions give

\[
\|x\|^\beta\le C(1+a(x))\quad(\beta<2),
\qquad
\|x\|^2\le C(1+a(x))\quad(\beta=2).
\tag{17}
\]

For beta=2, integrate the tail Hessian on the radial segment from x/2 to x for ||x||>=2R_H. This also gives a(x)>=c||x||^2-C.

At stationarity write (X,xi)~pi_alpha, xi^+=Phi(xi,U), G_alpha=G(X,xi^+), and X^+=X-alpha G_alpha. The stationary xi^+ marginal and the uniform x-Lipschitz bound yield, for beta=2,

\[
\mathbb E\|g(X,\xi^+)\|^2\le C+C\mathbb E a(X).
\]

For beta<2 the conditional exponential bound gives E[||g(X,xi^+)||^2|X,xi]<=C(1+||X||^{beta-1})^2; since 2beta-2<=beta, (17) gives the same result. Together with ||h||^2<=L_h a,

\[
\mathbb E\|G_\alpha\|^2\le C(1+\mathbb E a(X))
\tag{18}
\]

whenever the expectations are justified.

### Justifying second moments

For beta<2, the induced first moment already implies every polynomial moment of X. In fact, projecting a joining path onto its radial coordinate gives the lower bound

\[
d_{V_\alpha,\alpha}((x,\xi),(0,\xi_*))
\ge\int_0^{\|x\|}T(r)\,dr,
\]

which grows faster than any fixed power. This justifies (18) and the square identity below.

For beta=2, start from X_0=0 and xi_0~pi_Xi. Finite second moments hold at each finite time by induction. Define

\[
J_\alpha(x,\xi)=\|x\|^2-2\alpha\langle x,\chi_0(\xi)\rangle.
\]

For any joint law with xi marginal pi_Xi, (12) and Young's inequality give

\[
\tfrac12\mathbb E\|X\|^2-C\alpha^2
\le\mathbb EJ_\alpha(X,\xi)
\le\tfrac32\mathbb E\|X\|^2+C\alpha^2.
\tag{19}
\]

Writing G_n=G(X_n,xi_{n+1}), expand one step and use (14) at x=0. The terms linear in g(0,xi_{n+1}) cancel, leaving

\[
\mathbb E\Delta J_\alpha
=-2\alpha\mathbb E\langle X_n,G(X_n,\xi_{n+1})-G(0,\xi_{n+1})\rangle
+\alpha^2\mathbb E\|G_n\|^2
+2\alpha^2\mathbb E\langle G_n,\chi_0(\xi_{n+1})\rangle.
\]

The first term is at most -2alpha(1-theta)E a(X_n). The other terms have absolute upper bound C alpha^2(1+E||X_n||^2), using stationary second moments of g(0,xi) and chi_0. Coercivity and (19), followed by decreasing alpha, give

\[
\mathbb EJ_\alpha(X_{n+1},\xi_{n+1})
\le(1-c\alpha)\mathbb EJ_\alpha(X_n,\xi_n)+C\alpha.
\]

Iteration bounds E||X_n||^2 uniformly in n. The initial law belongs to P_1 of the induced metric, so its finite-time laws converge to pi_alpha. Lower semicontinuity gives E_{pi_alpha}||X||^2<infinity. This justifies (18) and all following identities.

### The O(alpha) stationary energy

Stationarity and (14) at zero give

\[
\mathbb E\langle X,g(0,\xi^+)\rangle
=\mathbb E\langle X,\chi_0(\xi)-\chi_0(\xi^+)\rangle
=-\alpha\mathbb E\langle G_\alpha,\chi_0(\xi^+)\rangle.
\]

Its absolute value is at most C alpha(1+E a(X)) by (12), (18), and Cauchy--Schwarz. The mean-perturbation inequality at y=0 therefore gives

\[
\mathbb E\langle X,G_\alpha\rangle
\ge(1-\theta)\mathbb E a(X)-C\alpha(1+\mathbb E a(X)).
\]

The justified stationary square identity is

\[
0=-2\alpha\mathbb E\langle X,G_\alpha\rangle
+\alpha^2\mathbb E\|G_\alpha\|^2.
\]

Using (18) and absorbing the small multiple of E a(X) proves

\[
\mathbb E a(X)\le C\alpha,
\qquad \mathbb E\|G_\alpha\|^2\le C.
\tag{20}
\]

Let r_0=min(1,R_H/2). Equation (16) controls ||X||^m on ||X||<=r_0, while a is bounded below on ||X||>=r_0. Hence

\[
\mathbb E[\|X\|^m\mathbf1_{\{\|X\|\le1\}}]\le C\alpha,
\qquad \mathbb P(\|X\|\ge1)\le C\alpha.
\tag{21}
\]

For Y=alpha^{-1/m}X and fixed R>=1, eventually R alpha^{1/m}<=1, and

\[
\mathbb P(\|Y\|>R)\le CR^{-m}+C\alpha.
\]

Thus the stationary rescaled laws are tight as alpha tends to zero.

### Increment estimates

Set epsilon=alpha^{1-1/m}. Then Delta Y=-epsilon G_alpha. For beta=2,

\[
\|G_\alpha\|\le C\|X\|+\|g(0,\xi^+)\|.
\]

The latter variable has a fixed square-integrable distribution. For the X part of E[||G_alpha||^2 1_{epsilon||G_alpha||>eta}], the relevant threshold tends to infinity. There ||X||^2<=C a(X), and (20) makes the contribution vanish.

For beta<2 put w=1+||X||^{beta-1}. The normalized factor in ||G_alpha||<=Cw(1+||g||/w) has a uniform conditional exponential moment. On w<=epsilon^{-1/2}, exponential-tail integration bounds the large-increment contribution by C E w^2 exp(-c epsilon^{-1/2}), which vanishes by (17), (20). On w>epsilon^{-1/2}, it is at most C E[w^2 1_{w>epsilon^{-1/2}}]. For sufficiently small alpha this event is in the tail, where w^2<=C a(X), so this also vanishes. If beta=1, w=2 and the complementary event is eventually empty. Therefore

\[
\mathbb E[\|G_\alpha\|^2\mathbf1_{\{\epsilon\|G_\alpha\|>\eta\}}]\longrightarrow0
\quad\text{for every }\eta>0.
\tag{22}
\]

On every fixed compact Y-region, ||g(alpha^{1/m}Y,xi^+)||^2 is uniformly integrable: for beta=2 it is dominated by C_R(1+||g(0,xi^+)||^2), and for beta<2 the conditional exponential bound applies. Finally,

\[
\mathbb E\|h(X)\|^2\le C\alpha,
\quad \sup_\alpha\mathbb E\|g(X,\xi^+)\|^2<\infty,
\quad \mathbb E[\|h(X)\|\|g(X,\xi^+)\|]\to0.
\tag{23}
\]

## 5. Decorrelation and the limiting generator

For bounded Lipschitz psi and bounded Lipschitz centered f on Xi, use the scalar solution u-Qu=f from Section 3. Stationarity gives

\[
\mathbb E[\psi(Y)f(\xi)]
=\mathbb E[(\psi(Y^+)-\psi(Y))u(\xi^+)].
\]

Equations (20) and Delta Y=-epsilon G_alpha imply

\[
|\mathbb E[\psi(Y)f(\xi)]|\le C_{\psi,f}\epsilon.
\tag{24}
\]

Bounded Lipschitz functions are dense in L^1(pi_Xi). Since the xi marginal is fixed, approximation in L^1 extends (24) to the following product limit along any subsequence Y_alpha=>mu:

\[
\mathbb E[\psi(Y_\alpha)\Psi(\xi_\alpha)]
\longrightarrow\mu(\psi)\pi_\Xi(\Psi),
\qquad \Psi\in L^1(\pi_\Xi).
\tag{25}
\]

Define the covariance integrand correctly by

\[
M_x(\zeta)=g_x(\zeta)g_x(\zeta)^T
+g_x(\zeta)\chi_x(\zeta)^T
+\chi_x(\zeta)g_x(\zeta)^T.
\tag{26}
\]

The two cross terms are essential. Equations (12), (13), and the x-Lipschitz bound on g imply, for ||x||<=1,

\[
\|M_x(\zeta)-M_0(\zeta)\|
\le C_p(\|x\|+\|x\|^p)F(\zeta),
\]

where F=1+||g_0||+R+||g_0||R is pi_Xi-integrable. Thus QM_0 is integrable and, for any compact K,

\[
\mathbb E[\|QM_{\alpha^{1/m}Y}(\xi)-QM_0(\xi)\|
\mathbf1_{\{Y\in K\}}]\to0.
\tag{27}
\]

Here one bounds the left side by C_K(alpha^{1/m}+alpha^{p/m}) pi_Xi(QF), and uses invariance of pi_Xi.

Fix phi in C_c^3. Set

\[
h_\alpha(y)=\alpha^{-(m-1)/m}h(\alpha^{1/m}y),
\qquad \Delta Y=-\epsilon^2h_\alpha(Y)-\epsilon g_X(\xi^+).
\]

The local expansion and homogeneity give h_alpha->h_0 locally uniformly. Consider

\[
\varphi_\alpha(y,\xi)
=\varphi(y)-\epsilon\langle\nabla\varphi(y),\chi_{\alpha^{1/m}y}(\xi)\rangle.
\tag{28}
\]

This is integrable by (12); outside the support of grad phi its correction is zero. Thus no global growth of h_alpha is used in that correction. Stationarity permits applying (28).

Taylor expansion of the uncorrected part, divided by epsilon^2, gives

\[
-\langle h_\alpha(Y),\nabla\varphi(Y)\rangle
-\epsilon^{-1}\langle\nabla\varphi(Y),g_X(\xi^+)\rangle
+\tfrac12\operatorname{tr}(g_Xg_X^T(\xi^+)\nabla^2\varphi(Y))
+r_\alpha,
\]

where E|r_alpha|->0. Terms involving h(X) in the quadratic expansion vanish by (23). For the other Taylor remainder, uniform continuity of Hess phi bounds its expectation by a quantity tending to zero using (20), (22), first restricting ||Delta Y||<=eta and then sending eta to zero.

Split the correction increment into a change in xi at fixed Y and a change in Y at fixed xi^+. The first, after division by epsilon^2, has expectation

\[
\epsilon^{-1}\mathbb E\langle\nabla\varphi(Y),Qg_X(\xi)\rangle.
\]

It cancels the expectation of the singular noise term exactly.

For the remaining increment, let E_alpha={||Delta Y||<=1/2}. Equation (22) gives P(E_alpha^c)=o(epsilon^2). The bound (12) and Cauchy--Schwarz show that its contribution after division by epsilon is o(1). On E_alpha, if either correction is nonzero, both Y and Y^+ lie in a fixed compact enlargement of supp(grad phi). Decompose

\[
\langle\nabla\varphi(Y^+)-\nabla\varphi(Y),\chi_X(\xi^+)\rangle
+\langle\nabla\varphi(Y^+),\chi_{X^+}(\xi^+)-\chi_X(\xi^+)\rangle.
\]

Taylor expansion of the first term, including its negative epsilon^{-1} prefactor, produces

\[
\mathbb E\operatorname{tr}(g_X(\xi^+)\chi_X(\xi^+)^T\nabla^2\varphi(Y))+o(1).
\]

The h contribution tends to zero by compact boundedness of h_alpha and (12). If omega_phi is a bounded modulus of continuity of Hess phi, the remaining error is bounded by

\[
C\mathbb E[\omega_\varphi(\epsilon\|G_\alpha\|)\|G_\alpha\|R(\xi^+)].
\]

On epsilon||G_alpha||<=eta use (20) and Cauchy--Schwarz; on the complement use (22) and R in L^2. This proves the error vanishes. Removing the E_alpha restriction in the leading term is justified by the same argument and (23).

For the second term choose p in (1-1/m,1). Equation (13), X^+-X=-alpha G_alpha, and weighted AM--GM give

\[
\epsilon^{-1}\mathbb E[\|\chi_{X^+}(\xi^+)-\chi_X(\xi^+)\|
\|\nabla\varphi(Y^+)\|]
\le C_p\alpha^{p-(1-1/m)}
\mathbb E[\|G_\alpha\|^pR(\xi^+)^{1-p}]
\longrightarrow0.
\]

The expectation is uniformly bounded by the first moments implied by (12), (20). Therefore the stationary expansion is

\[
0=-\mathbb E\langle h_\alpha(Y),\nabla\varphi(Y)\rangle
+\tfrac12\mathbb E\operatorname{tr}(QM_{\alpha^{1/m}Y}(\xi)\nabla^2\varphi(Y))+o(1).
\tag{29}
\]

To identify its averaged matrix, let f=g_0 and chi=chi_0, with (xi,xi^+) stationary. The Poisson equation gives E[f(xi^+)+chi(xi^+)|xi]=chi(xi). Expansion of D_0=f(xi^+)+chi(xi^+)-chi(xi), followed by stationarity, cancels the chi-square terms and yields

\[
\mathbb E[D_0D_0^T]=\int M_0\,d\pi_\Xi=\Sigma.
\tag{30}
\]

Along a weakly convergent subsequence, the drift term in (29) converges by compact support and local uniform convergence. Apply (27) and then (25) entrywise to the bounded Lipschitz entries of Hess phi. Equations (29), (30) give

\[
\int\left[-\langle h_0(y),\nabla\varphi(y)\rangle
+\tfrac12\operatorname{tr}(\Sigma\nabla^2\varphi(y))\right]\mu(dy)=0.
\tag{31}
\]

## 6. The limiting diffusion and full convergence

Scaling (16) gives

\[
\langle y,h_0(y)\rangle\ge\frac{c_{in}}{m-1}\|y\|^m.
\tag{32}
\]

For e=y-z, integrate the local Hessian inequality along the segment joining t z to t y and divide by t^m. Let t decrease to zero and use the local gradient expansion. This yields

\[
\langle e,h_0(y)-h_0(z)\rangle
\ge c_{in}\|e\|^2\int_0^1\|z+se\|^{m-2}ds
\ge c_m\|e\|^m.
\tag{33}
\]

For the last bound, project z onto e. After normalizing ||e||=1, the scalar integral is minimized when its interval is centered at zero, and equals 2 integral_0^{1/2} s^{m-2} ds>0. This includes m=2. No convergence of Hessians is assumed.

The drift -h_0 is locally Lipschitz, so the SDE with constant covariance has a pathwise unique solution up to explosion. Its generator L satisfies, for W=1+||y||^2,

\[
LW=-2\langle y,h_0(y)\rangle+\operatorname{tr}\Sigma
\le C-c\|y\|^m.
\tag{34}
\]

Stopped Itô estimates give P_y(tau_R<=t)<=(W(y)+Ct)/(1+R^2), proving nonexplosion. The same estimates and Fatou's lemma give tightness of the time-averaged laws, since their averaged m-th moments are bounded by C+W(y)/(cT). Local Lipschitz continuity, localization, and nonexplosion give a Feller semigroup. A weak limit of time-averaged laws is invariant: for each bounded continuous test and fixed s, the difference between its integral under the average and the average advanced by s is bounded by 2s||test||_infinity/T, and the Feller property permits passage to the weak limit.

Every invariant law has finite m-th moment. Choose smooth nondecreasing concave truncations theta_n with 0<=theta_n'<=1, theta_n'=1 up to n, theta_n'=0 beyond 2n, and theta_n' increasing pointwise to one. The function theta_n(W) is constant outside a compact set, so its generator is bounded and invariance gives integral L theta_n(W)=0. Concavity and (34) yield

\[
c\int\theta_n'(W)\|y\|^m\,d\mu\le C.
\]

Monotone convergence proves the moment assertion. If two invariant laws are coupled using the same Brownian motion, their difference satisfies

\[
\frac d{dt}\|\Delta_t\|^2\le-2c_m\|\Delta_t\|^m.
\]

For m=2 this gives exponential decay of E||Delta_t||^2. For m>2 the scalar differential inequality gives the bound ||Delta_t||^2<=[c_m(m-2)t]^{-2/(m-2)} for t>0, independently of the finite initial difference. Thus E||Delta_t||^2 tends to zero. The marginals remain invariant, so their W_2 distance is zero. This proves uniqueness, without requiring Sigma to be positive definite.

Finally use the standard stationary martingale-problem criterion in the following form: for a diffusion operator on C_c^infinity with locally Lipschitz drift and constant positive semidefinite covariance, whose martingale problem is well posed and conservative, a probability rho annihilating the generator on C_c^infinity is invariant. Here local Lipschitz continuity has been checked, (15) gives the finite positive semidefinite covariance, and (34) establishes conservativity; pathwise uniqueness and nonexplosion give the well-posed martingale problem. Each generator test is bounded because its derivatives have compact support, so its rho-integrability is automatic. Equation (31) holds in particular on C_c^infinity, and the criterion identifies every subsequential limit with the unique invariant law just proved.

Tightness and uniqueness of every possible subsequential limit now imply convergence of the entire family Y_alpha as alpha decreases to zero. Together with Section 2, this proves both requested conclusions.
