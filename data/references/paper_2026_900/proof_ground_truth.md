# Reference Proof

## Proof structure and obligations

1. Establish finiteness, regularity, the resolvent equation, and the monotonicity and endpoint properties needed for both boundaries.
2. Recover the boundary and coefficient from the continuation equation and matching conditions; check all coefficient and inverse endpoints.
3. Verify regularity at positive fuel, the gradient constraint, the stopping-region inequality, and a uniform growth bound.
4. Apply the full Ito formula, including control jumps, to establish the upper bound for every admissible control and equality for the reflected control.
5. Verify the classical stopping threshold directly and prove the pointwise vanishing-entropy limit.

All these obligations are closed below. Regularity at zero fuel is continuity, not differentiability.

## 1. Resolvent and boundary preliminaries

Write
\[
d=\sigma^2/2,\quad a=-\alpha_->0,\quad q=\lambda/\rho,
\quad Z_t=\exp((\mu-\sigma^2/2)t+\sigma W_t),
\quad m_\theta=\theta\mu+d\theta(\theta-1).
\]
The restored standing assumptions give \(\rho>\max\{0,\mu\}\), hence \(m_\theta<\rho\). Since \(\pi\ge0\),
\[
0\le H(x)\le c/\rho+c x^\theta/(\rho-m_\theta).
\]
In particular all control payoffs are absolutely integrable: the absolute running reward is bounded by \(\pi(X_t)+\rho\kappa+\lambda/e\).

Concavity and \(\pi(0)=0\) give \(0\le x\pi'(x)\le\pi(x)\). As \(x\pi'(x)\) is differentiable and increasing,
\[
-x\pi'(x)\le x^2\pi''(x)\le0.
\]
These inequalities dominate both spatial derivatives of \(\pi(xZ_t)\) on every compact positive-state interval by a constant times \(\pi(MZ_t)\), where \(M\) is the upper endpoint. Consequently differentiation under the discounted integral is legitimate twice. Thus \(H\in C^2((0,\infty))\) is concave and
\[
h(x):=xH'(x)=\mathbb E\int_0^\infty e^{-\rho t}(xZ_t)\pi'(xZ_t)\,dt.
\]
Strict increase of \(x\pi'(x)\), together with its nonnegativity, makes \(h\) positive and strictly increasing. Also \(0<h\le H\) and \(h'\ge0\).

For completeness, the resolvent equation need not be assumed as a black box. Apply the localized discounted Ito identity to \(\pi(X_t^x)\). The preceding derivative bounds imply \(|\mathcal L\pi|\le(|\mu|+d)\pi\); finite-horizon geometric-Brownian moments remove localization. The terminal expectation tends to zero as the horizon tends to infinity, by the growth bound and \(m_\theta<\rho\). It follows that
\[
\mathbb E\int_0^\infty e^{-\rho t}(\mathcal L-\rho)\pi(xZ_t)\,dt=-\pi(x).
\]
The justified derivative interchanges identify the left side with \((\mathcal L-\rho)H(x)\). Hence
\[
(\mathcal L-\rho)H+\pi=0.
\]
Dominated convergence, using \(\pi(xZ_t)\le\pi(Z_t)\) for \(x\le1\), gives \(H(0+)=0\); therefore \(h(0+)=0\) as well.

The profit is unbounded: for any fixed \(r>0\), \(r\pi'(r)>0\), and for \(x\ge r\),
\[
\pi(x)-\pi(r)\ge r\pi'(r)\log(x/r).
\]
Monotone convergence applied to the integral representation gives \(H(x)\to\infty\).

Define privately
\[
K(x)=H(x)+h(x)/a.
\]
Then \(K'=H'+h'/a>0\), \(K(0+)=0\), and \(K(x)\to\infty\). It has a continuous strictly increasing inverse on \([0,\infty)\), with inverse value zero at zero. The characteristic equation gives
\[
\mu+\rho/a=d(a+1).
\]
Combining this with the resolvent equation yields the useful sign identity
\[
\pi(x)-\rho K(x)
=-d\bigl(xh'(x)+a h(x)\bigr)
=-d a xK'(x)<0. \tag{1}
\]
The two characteristic roots have the stated ordering because the quadratic is negative at zero and at one and has positive leading coefficient.

## 2. Construction and endpoint definitions

The continuation equation is
\[
(\mathcal L-\rho)U+(\pi-\rho\kappa)y-\lambda y\log y=0.
\]
For fixed positive fuel its general solution is
\[
A_2(y)x^{-a}+A_1(y)x^{\alpha_+}
+H(x)y-\kappa y-qy\log y.
\]
Immediate depletion gives value at least zero, while the running-reward bound gives value at most \(H(x)+\lambda/(e\rho)\). Thus the increasing homogeneous power is incompatible with the value's growth, motivating \(A_1=0\). The ensuing candidate is verified independently below.

Impose \(F_y=F_{xy}=0\) at an active reflection boundary. These equations give
\[
K(x)=\kappa+q(1+\log g_\lambda(x)),
\qquad
A_2'(g_\lambda(x))=h(x)x^a/a.
\]
Solving the first equation gives precisely the stated exponential until it reaches one. Since \(K\) increases from zero to infinity, the cap is first reached at the finite point
\[
\widehat x_\lambda=K^{-1}(\kappa+q).
\]
The boundary extends continuously to \(y_\lambda=e^{-1-\kappa/q}\) at zero and is strictly increasing on \([0,\widehat x_\lambda]\). On its open increasing branch the correct derivative is
\[
g_\lambda'(x)=g_\lambda(x)K'(x)/q>0.
\]
The inverse on that closed branch is therefore well defined, including
\(b_\lambda(y_\lambda)=0\) and \(b_\lambda(1)=\widehat x_\lambda\).

For \(u\in(y_\lambda,1]\), put \(b=b_\lambda(u)\). The coefficient integrand simplifies to
\[
A_2'(u)=\frac{h(b)b^a}{a}\ge0. \tag{2}
\]
It tends to zero as \(u\downarrow y_\lambda\). Thus the displayed integral is finite and has \(A_2(y_\lambda)=A_2'(y_\lambda)=0\). Differentiating \(K(b_\lambda(u))=\kappa+q(1+\log u)\) and then (2) gives
\[
A_2''(u)=\frac{q}{u}b_\lambda(u)^a, \tag{3}
\]
which also tends to zero at \(y_\lambda\). This proves the coefficient endpoint assertions and the matching with the zero coefficient in the low-fuel region.

Let \(U\) be exactly the public three-region candidate, with \(U(x,0)=0\). Its stopping branch is \(F(x,g_\lambda(x))\), not \(F(x,g_\lambda^{-1}(x))\).

## 3. Matching, HJB inequalities, and growth

For \(y\ge y_\lambda\) in the retained-fuel region, let \(b=b_\lambda(y)\le x\). Direct differentiation gives
\[
F_{xy}(x,y)=\frac{h(x)-h(b)(b/x)^a}{x}\ge0,
\qquad
F_{yy}(x,y)=\frac qy\bigl((b/x)^a-1\bigr).
\]
At \(x=b\), \(F_y=F_{xy}=F_{yy}=0\). Integrating \(F_{xy}\ge0\) in \(x\) from \(b\) proves \(F_y\ge0\) throughout this region. At \(y=y_\lambda\), the same conclusion follows from \(F_y=H(x)\).

In the low-fuel region,
\[
U_y=H(x)-\kappa-q(1+\log y)>0
\]
for \(0<y<y_\lambda\), and the continuation equation holds by the resolvent equation. In the stopping region \(U_y=0\). Thus \(U\) is nondecreasing in fuel and, since it is continuous at zero with value zero, \(U\ge0\).

Equations (2)-(3) give second-order matching at \(y=y_\lambda\). On an uncapped active boundary, differentiating the stopping branch gives
\[
U_x=F_x(x,g_\lambda(x)),\qquad
U_{xx}=F_{xx}(x,g_\lambda(x)),
\]
because \(F_y=F_{xy}=0\) there. Together with \(F_{yy}=0\), this proves matching of all first and second derivatives across that boundary. The candidate is therefore locally \(C^2\) for \(x>0,0<y<1\), with the required one-sided regularity at \(y=1\). Near the cap point it can also be extended locally past \(y=1\) using the uncapped exponential and its inverse. No differentiability at \(y=0\) is asserted or used.

The HJB equality holds where \(y\le g_\lambda(x)\). For \(y>g_\lambda(x)\), the preceding spatial derivative identities give
\[
(\mathcal L-\rho)U+(\pi(x)-\rho\kappa)y-\lambda y\log y
=\int_{g_\lambda(x)}^y
[\pi(x)-\rho\kappa-\lambda(1+\log z)]\,dz.
\]
The integrand decreases in \(z\), and at its lower endpoint equals \(\pi(x)-\rho K(x)<0\) by (1). This proves the stopping-region inequality and hence both HJB inequalities everywhere at positive fuel, including the interfaces by continuity.

To establish a bound suitable for verification, set \(z=\min\{y,g_\lambda(x)\}\). When \(z\ge y_\lambda\), (2) gives
\[
0\le A_2(z)x^{-a}
=\int_{y_\lambda}^{z}\frac{h(b_\lambda(u))}{a}
\left(\frac{b_\lambda(u)}x\right)^a du
\le H(x)/a.
\]
Together with \(|z\log z|\le1/e\), this yields
\[
0\le U(x,y)\le (1+1/a)H(x)+\kappa+q/e
\le C(1+x^\theta). \tag{4}
\]
Here and below constants may depend on the fixed model parameters and on \(\lambda\), but not on \(x\) or \(y\). Also, throughout all regions,
\((\mathcal L-\rho)U=-r(x,z)\), where
\(r(x,v)=(\pi(x)-\rho\kappa)v-\lambda v\log v\).
Consequently the absolute drift is bounded by \(\pi(x)+\rho\kappa+\lambda/e\).

## 4. Verification, including jumps and zero fuel

The standard stochastic-calculus result used here is the Ito formula for a continuous diffusion and an adapted cadlag finite-variation coordinate. For a locally \(C^2\) function at positive fuel, the finite-variation terms are
\[
\int e^{-\rho t}U_y(X_t,Y_{t-})\,dY_t^c
+\sum_t e^{-\rho t}[U(X_t,Y_t)-U(X_t,Y_{t-})].
\]
The sum includes an initial jump from \(Y_{0-}=y\). The other terms are the drift \((\mathcal L-\rho)U\) and the local martingale with integrand \(e^{-\rho t}\sigma X_tU_x\). The regularity just proved verifies the formula's local hypotheses whenever fuel is bounded away from zero. Stopping \(X\) on compact subintervals of \((0,\infty)\) makes the stochastic integral a true martingale.

First suppose \(Y\ge\varepsilon>0\). Both finite-variation contributions are nonpositive: \(Y\) decreases and \(U_y\ge0\), while every downward jump decreases a function nondecreasing in fuel. The HJB inequality therefore gives, after localization,
\[
\mathbb E\left[e^{-\rho T}U(X_T,Y_T)
+\int_0^T e^{-\rho t}r(X_t,Y_t)dt\right]\le U(x,y). \tag{5}
\]
To justify removing the spatial stopping times, use (4), the drift bound, and finite moments of \(\sup_{t\le T}X_t\) for each fixed finite \(T\). These dominate the terminal and running terms. Nonpositive control terms can be discarded before this passage. Moreover,
\[
\mathbb E[e^{-\rho T}U(X_T,Y_T)]
\le C\bigl(e^{-\rho T}+x^\theta e^{-(\rho-m_\theta)T}\bigr)\longrightarrow0.
\]
Absolute integrability of the running reward then yields \(J^\lambda(x,y;\xi)\le U(x,y)\).

For an arbitrary control and \(0<\varepsilon<y\), use
\(\xi_t^\varepsilon=\min\{\xi_t,y-\varepsilon\}\). It is admissible and has remaining fuel \(Y_t^\varepsilon=\max\{Y_t,\varepsilon\}\). The preceding upper bound applies with the same initial state. Continuity of \(v\log v\) at zero and the common integrable running-reward bound give \(J^\lambda(\xi^\varepsilon)\to J^\lambda(\xi)\). This proves the upper bound for every admissible control. For \(y=0\), the only control and the value are zero.

Now take
\[
\xi_t^\lambda=\sup_{0\le s\le t}(y-g_\lambda(X_s))^+.
\]
Continuity and adaptedness of \(g_\lambda(X)\) imply admissibility. After its possible initial jump this control is continuous. Its fuel is
\[
Y_t=\min\{y,\inf_{0\le s\le t}g_\lambda(X_s)\},
\]
so it remains at least \(\min\{y,y_\lambda\}>0\) when \(y>0\), and satisfies \(Y_t\le g_\lambda(X_t)\). Thus the HJB equality holds along the state. The continuous control measure is supported on \(Y_t=g_\lambda(X_t)\), where \(U_y=0\). The initial jump, if present, goes from \(y\) to \(g_\lambda(x)\) through a constant-value segment and hence also contributes zero. Every inequality in (5) is therefore an equality for this policy. The same localization and terminal estimates prove
\[
J^\lambda(x,y;\xi^\lambda)=U(x,y).
\]
This establishes the entire value formula and optimal-control claim.

## 5. Classical threshold and the limit

Since \(K\) is a continuous increasing bijection from \([0,\infty)\) onto itself, there is exactly one positive \(b_*\) with \(K(b_*)=\kappa\). To identify it with the classical stopping threshold rather than merely an algebraic root, define
\[
v(x)=\begin{cases}
0,&x\le b_*,\\
H(x)-\kappa+\dfrac{h(b_*)}{a}(b_*/x)^a,&x>b_*.
\end{cases}
\]
The equation \(K(b_*)=\kappa\) gives value matching, and direct differentiation gives smooth fit. For \(x>b_*\),
\[
v'(x)=\frac{h(x)-h(b_*)(b_*/x)^a}{x}>0.
\]
Thus \(v\ge0\). It solves \((\mathcal L-\rho)v+\pi-\rho\kappa=0\) above \(b_*\). Below it, monotonicity of \(\pi\) and (1) give \(\pi(x)\le\pi(b_*)<\rho\kappa\), establishing the stopping inequality.

The standard one-dimensional Ito-Meyer formula applies: \(v\) is \(C^1\), piecewise \(C^2\), and has locally bounded second derivative; smooth fit removes an interface local-time term. Localize as above and stop additionally at any stopping time \(\tau\). Nonnegativity of the terminal value gives the upper bound on the expected stopped running payoff. Letting the deterministic horizon increase is justified by absolute integrability. For \(\tau_* =\inf\{t\ge0:X_t\le b_*\}\), equality holds before stopping and the terminal value is zero when stopping occurs. On \(\{\tau_*>T\}\) its expectation tends to zero by the same sublinear-growth estimate as (4). Thus \(\tau_*\) is optimal, proving the claimed classical interpretation without invoking an unspecified classical free-boundary theorem.

Finally, for \(y\in[y_\lambda,1]\),
\[
b_\lambda(y)=K^{-1}\!\left(\kappa+\frac\lambda\rho(1+\log y)\right).
\]
For fixed \(y>0\), \(y_\lambda\to0\), so this formula is defined for all sufficiently small \(\lambda\). Its argument tends to \(\kappa\); continuity of \(K^{-1}\) proves
\(b_\lambda(y)\to K^{-1}(\kappa)=b_*\).

The corrected comparison directions are: for \(y\ge e^{-1}\), the boundary is at least \(b_*\) and is nondecreasing as a function of \(\lambda\); for \(y\le e^{-1}\), it is at most \(b_*\) and is nonincreasing in \(\lambda\) on its domain. At equality it is constant. These corrections leave the pointwise limit unchanged.
