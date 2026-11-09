# Reference Proof

## Proof Structure and Obligations

The proof must establish: finite strongly convex population objectives and unique minimizers; the transport comparison needed to obtain the minimizer-map contraction; well-defined stable comparators; the contraction-plus-drift recursion; its finite-horizon summation; and conversion to the stated deployed-risk regret with the specified expectation scope.

The source's mechanism is preserved: strong convexity and the common exogenous component yield a contraction factor \((1-\rho_t)\epsilon\beta/\mu\), followed by moving-comparator tracking and a Lipschitz regret conversion. To justify this mechanism for the public domain of exogenous distributions, the proof uses finite loss contrasts rather than silently assuming that every expected gradient exists. In particular, it does not impose a first-moment condition on \(Q_t\).

## Complete Proof

### 1. Population objectives and constrained minimizers

For fixed \(t\), write
\[
F_u(x)=\bar R_t(x,u),\qquad
G_t(u)=\arg\min_{x\in\mathcal X}F_u(x).
\]
The public integrability assumption makes every \(F_u(x)\) finite. Pointwise strong convexity implies, for \(a,b\in\mathcal X\) and \(0<\lambda<1\),
\[
F_u((1-\lambda)a+\lambda b)
\leq(1-\lambda)F_u(a)+\lambda F_u(b)
-\frac{\mu}{2}\lambda(1-\lambda)\|a-b\|^2.
\]
Indeed, apply the pointwise first-order strong-convexity inequalities at \((1-\lambda)a+\lambda b\) with endpoints \(a\) and \(b\), weight them by \(1-\lambda\) and \(\lambda\), and add; the gradient terms cancel before taking expectations. Thus no interchange of differentiation and expectation is required.

Attainment is assumed, and this strict convexity makes the minimizer unique. Moreover, if \(a\) minimizes \(F_u\), then
\[
F_u(a)\leq F_u((1-\lambda)a+\lambda b)
\]
combined with the preceding inequality gives
\[
F_u(b)-F_u(a)\geq\frac{\mu}{2}(1-\lambda)\|a-b\|^2.
\]
Letting \(\lambda\downarrow0\),
\[
F_u(b)-F_u(a)\geq\frac{\mu}{2}\|a-b\|^2.
\tag{1}
\]
This argument applies to boundary minimizers and lower-dimensional convex domains.

### 2. The transport comparison, including its hypotheses

The only Wasserstein expectation bound needed here is the following standard independent fact: if \(\nu,\eta\in\mathcal P_1(\mathcal Z)\) and \(h:\mathcal Z\to\mathbb R\) is \(K\)-Lipschitz, then
\[
\left|\int h\,d\nu-\int h\,d\eta\right|\leq K W_1(\nu,\eta).
\tag{2}
\]
Both integrals are finite because \(|h(z)|\leq |h(z_0)|+K d_{\mathcal Z}(z,z_0)\). For any coupling \(\pi\) of \(\nu\) and \(\eta\), the difference is the integral of \(h(z)-h(z')\); its absolute value is bounded by \(K\int d_{\mathcal Z}(z,z')\,d\pi\). Taking the infimum over couplings proves (2), so no specialized external theorem is left unproved.

Fix \(a,b\in\mathcal X\) and define the scalar contrast
\[
h(z)=\ell(z,b)-\ell(z,a).
\]
Continuous differentiability along the segment from \(a\) to \(b\) gives
\[
h(z)-h(z')
=\int_0^1\left\langle
\nabla_x\ell(z,a+r(b-a))-\nabla_x\ell(z',a+r(b-a)),\ b-a
\right\rangle\,dr.
\]
Consequently,
\[
|h(z)-h(z')|\leq\beta\|b-a\|d_{\mathcal Z}(z,z').
\tag{3}
\]
Thus \(h\) is integrable under every \(\mathsf M(u)\), and (2) applies to these endogenous laws. It is also integrable under every \(\mathsf P_t(u)\) by the loss-integrability assumption. If \(\rho_t>0\), this implies its integrability under \(Q_t\). If \(\rho_t=0\), no integral under \(Q_t\) is needed.

### 3. Contraction of the population minimizer map

Fix \(u,v\in\mathcal X\), set \(a=G_t(u)\), \(b=G_t(v)\), and use the contrast from the preceding section. Applying (1) to both minimizers yields
\[
\mu\|a-b\|^2
\leq F_u(b)-F_u(a)+F_v(a)-F_v(b)
=\int h\,d\mathsf P_t(u)-\int h\,d\mathsf P_t(v).
\]
The exogenous contribution cancels, so
\[
\int h\,d\mathsf P_t(u)-\int h\,d\mathsf P_t(v)
=(1-\rho_t)\left(\int h\,d\mathsf M(u)-\int h\,d\mathsf M(v)\right).
\]
For \(\rho_t=0\), this identity simply involves the endogenous laws; it does not interpret an undefined exogenous integral multiplied by zero. For \(\rho_t=1\), both full distributions are \(Q_t\), so the difference is zero.

Using (2), (3), and sensitivity,
\[
\mu\|a-b\|^2
\leq(1-\rho_t)\beta\|a-b\|W_1(\mathsf M(u),\mathsf M(v))
\leq(1-\rho_t)\epsilon\beta\|a-b\|\|u-v\|.
\]
If \(a=b\), the desired estimate is immediate. Otherwise divide by \(\mu\|a-b\|\). In either case,
\[
\|G_t(u)-G_t(v)\|\leq\gamma_t\|u-v\|,
\qquad
\gamma_t=\frac{(1-\rho_t)\epsilon\beta}{\mu}\leq\gamma<1.
\tag{4}
\]
This establishes the full contraction constant without requiring \(Q_t\in\mathcal P_1(\mathcal Z)\), expected-gradient integrability, or parameter-gradient Lipschitzness.

For completeness, stable comparators exist and are unique under these hypotheses. If \(\gamma_t=0\), \(G_t\) is constant and its value is a fixed point. If \(0<\gamma_t<1\), start at any \(q_0\in\mathcal X\) and set \(q_{n+1}=G_t(q_n)\). By (4),
\[
\|q_{n+1}-q_n\|\leq\gamma_t^n\|q_1-q_0\|.
\]
The geometric tail bound makes \((q_n)\) Cauchy. The compact set \(\mathcal X\) is closed in Euclidean space, so its limit \(s\) lies in \(\mathcal X\); continuity of \(G_t\), supplied by (4), gives \(s=G_t(s)\). Any two fixed points satisfy \(\|s-s'\|\leq\gamma_t\|s-s'\|\), hence coincide. Thus the public comparator is this fixed point, and
\[
x_{t+1}=G_t(x_t),\qquad s_t=G_t(s_t).
\]
All iterates and comparators are deterministic for the fixed environment and fixed initialization.

### 4. Tracking the moving comparator

Let \(e_t=\|x_t-s_t\|\). For \(1\leq t<T\), (4) and the triangle inequality imply
\[
\begin{aligned}
e_{t+1}
&=\|G_t(x_t)-s_{t+1}\|\\
&\leq\|G_t(x_t)-G_t(s_t)\|+\|s_t-s_{t+1}\|\\
&\leq\gamma e_t+\delta_t.
\end{aligned}
\tag{5}
\]

### 5. Summation with the terminal term retained

Summing (5) over \(t=1,\ldots,T-1\) gives
\[
\sum_{t=2}^{T}e_t\leq\gamma\sum_{t=1}^{T-1}e_t+\sum_{t=1}^{T-1}\delta_t.
\]
Therefore
\[
(1-\gamma)\sum_{t=1}^{T}e_t
\leq e_1-\gamma e_T+\sum_{t=1}^{T-1}\delta_t
\leq e_1+\sum_{t=1}^{T-1}\delta_t.
\]
Since \(1-\gamma>0\),
\[
\sum_{t=1}^{T}e_t
\leq\frac{e_1+\sum_{t=1}^{T-1}\delta_t}{1-\gamma}.
\tag{6}
\]
The same calculation holds for \(T=1\) using empty sums.

### 6. Conversion to regret

The assumed uniform Lipschitz bound gives
\[
R_t(x_t)-R_t(s_t)\leq L\|x_t-s_t\|=Le_t.
\]
The expectation in the public regret is redundant because the exact minimizers are unique and the initialization and environment are fixed. Summing and applying (6) proves
\[
\operatorname{Reg}^{\mathrm{stab}}_T
\leq\frac{L}{1-\gamma}
\left(\|x_1-s_1\|+\sum_{t=1}^{T-1}\delta_t\right).
\]
No division by \(L\), \(\beta\), \(\epsilon\), or \(1-\rho_t\) occurs. Thus \(L=0\), \(\beta=0\), \(\epsilon=0\), and purely exogenous rounds are covered. A singleton parameter domain gives zero tracking error and zero regret. No nonnegativity of stability regret is needed.

## Dependency Audit

The source supplies the objective-comparison and contraction mechanism in theory_005, the tracking and risk-conversion argument in theory_006, and the telescoping identity in theory_022. The relevant independent transport inequality associated with theory_020 is stated and derived above with its hypotheses checked. The pointwise regularity and risk definitions come from theory_004 and theory_002. The auxiliary sufficient condition in theory_009 is not invoked: the public task directly assumes the required Lipschitz property of \(R_t\), as does the source target. Its extra loss-Lipschitz assumptions are therefore not silently imported. Every theorem-critical obligation listed at the start is closed; there is no remaining private reference-proof gap.
