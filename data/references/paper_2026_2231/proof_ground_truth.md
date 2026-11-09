# Reference Proof

## Proof Structure

1. Check the divergence conventions and prove simultaneous pushforward invariance, including the integral and singular terms.
2. Use target invariance and family stability to show that the objective is constant on group orbits, so the minimizer set is stable; uniqueness then makes the minimizer invariant.
3. Verify that statistic compatibility makes the induced maps on statistic values well-defined, and apply invariance of the target and minimizer to place both statistic values in the fixed set.

## Complete Proof

### Divergence well-definedness and standard background

A finite convex function on an open interval has a finite supporting slope at every interior point. Apply this standard convexity result at 1: there is c in R such that
\[
f(t)\ge c(t-1),\qquad t>0.
\]
The hypothesis holds because f is finite-valued on (0,infinity). The inequality extends to zero by the specified right limit and implies f'(infinity)>=c. Put F(t)=f(t)-c(t-1), including its endpoint extension. Then F>=0 and F'(infinity)=f'(infinity)-c>=0.

For a sigma-finite common dominating measure lambda with densities a,b, choose nonnegative finite versions outside a lambda-null set, assigning zero on that null set. On {b>0},
\[
bf(a/b)\ge c(a-b).
\]
Its negative part is integrable because |c(a-b)|<=|c|(a+b) and both densities have integral one. The singular coefficient f'(infinity) is bounded below by the finite number c. Thus the divergence expression is defined without an infinity-minus-infinity ambiguity, using the stipulated zero-times-infinity convention. Moreover,
\[
\begin{aligned}
D_F(\alpha\|\beta)-D_f(\alpha\|\beta)
&=-c\left[\int_{\{b>0\}}(a-b)\,d\lambda+\alpha(\{b=0\})\right]\\
&=-c[1-1]=0.
\end{aligned}
\]
Here the displayed difference denotes the finite affine correction: equivalently, D_F equals D_f plus that correction, even when both divergences are infinite. Consequently D_f=D_F is nonnegative, with +infinity allowed.

For completeness, the value is independent of the sigma-finite dominating measure. Define the nonnegative perspective
\[
\Psi(s,t)=\begin{cases}
tF(s/t),&t>0,\\
F'(\infty)s,&t=0,
\end{cases}
\qquad s,t\ge0,
\]
with the zero-times-infinity convention. It satisfies Psi(0,0)=0 and Psi(rs,rt)=r Psi(s,t) for every finite r>0. The divergence D_F computed from lambda equals the integral of Psi(a,b) against lambda.

If eta is another sigma-finite common dominating measure, let theta=lambda+eta, which is sigma-finite. Write r=d lambda/d theta. The density identities give d alpha/d theta=ar and d beta/d theta=br theta-almost everywhere, with both products taken as zero where r=0. Hence homogeneity and the integration formula for a density yield
\[
\int\Psi(d\alpha/d\theta,d\beta/d\theta)\,d\theta
=\int r\Psi(a,b)\,d\theta
=\int\Psi(a,b)\,d\lambda.
\]
At r=0 both sides of the integrand identity are zero. Applying the same argument to eta proves independence. Common finite dominating measures exist, for example alpha+beta.

We also use the standard pushforward integration identity
\[
\int\Phi\,d(h_\#\lambda)=\int\Phi\circ h\,d\lambda
\]
for every nonnegative measurable Phi and measurable h. It follows from the definition of pushforward for indicators, then linearity for nonnegative simple functions and monotone convergence. No finiteness of the integral is required.

### Simultaneous pushforward invariance

Fix a measurable bijection h with measurable inverse and probability measures alpha,beta. Choose a sigma-finite common dominating measure lambda, write a=d alpha/d lambda and b=d beta/d lambda, and put lambda'=h_#lambda. Images under h of a countable finite-measure cover are measurable and form a finite-measure cover for lambda', so lambda' is sigma-finite. It dominates h_#alpha and h_#beta.

For every measurable A, pushforward integration gives
\[
\int_A(a\circ h^{-1})\,d\lambda'
=\int_{h^{-1}(A)}a\,d\lambda
=\alpha(h^{-1}(A)).
\]
Thus a'=a composed with h inverse is a density of h_#alpha with respect to lambda'; similarly b'=b composed with h inverse is a density of h_#beta. All these functions are measurable.

Using the nonnegative generator F and applying pushforward integration to the function equal to b'F(a'/b') on {b'>0} and zero elsewhere gives
\[
\int_{\{b'>0\}}b'F(a'/b')\,d\lambda'
=\int_{\{b>0\}}bF(a/b)\,d\lambda.
\]
Also h^{-1}({b'=0})={b=0}, so
\[
(h_\#\alpha)(\{b'=0\})=\alpha(\{b=0\}).
\]
The singular terms therefore agree, including when the coefficient is infinite and the mass is zero. Combining the two equalities and using D_f=D_F yields
\[
D_f(h_\#\alpha\|h_\#\beta)=D_f(\alpha\|\beta).
\]

### Invariance of the unique minimizer

Let
\[
L(\nu)=D_f(\mu\|\nu),\qquad \nu\in\mathcal V.
\]
For h in H and nu in V, family stability ensures h_#nu belongs to V. Target invariance and simultaneous pushforward invariance give
\[
L(h_\#\nu)=D_f(\mu\|h_\#\nu)
=D_f(h_\#\mu\|h_\#\nu)
=D_f(\mu\|\nu)=L(\nu).
\]
In particular, h_#nu^star attains the same minimum as nu^star. Uniqueness therefore implies
\[
h_\#\nu^\star=\nu^\star\qquad\text{for every }h\in H.
\]
This uses equality of extended objective values, not subtraction, and remains valid if the minimum is +infinity. Existence of the unique minimizer already implies that V is nonempty.

### Statistic values in the fixed set

Let Y_0=T(dom(T)). If T(pi)=T(pi') for pi,pi' in dom(T), compatibility gives T(h_#pi)=T(h_#pi'). Thus varrho_h is independent of the representative. Domain stability ensures that its values belong to Y_0.

Since mu is in dom(T) and h_#mu=mu,
\[
\varrho_h(T(\mu))=T(h_\#\mu)=T(\mu).
\]
Since nu^star is in V, it is also in dom(T); its established invariance gives
\[
\varrho_h(T(\nu^\star))=T(h_\#\nu^\star)=T(\nu^\star).
\]
These equalities hold for every h in H. By the definition of Gamma_T(H),
\[
T(\mu)\in\Gamma_T(H),\qquad T(\nu^\star)\in\Gamma_T(H).
\]

All theorem-critical obligations are closed. The supporting-slope and pushforward-integration results are standard independent background with their statements and applicable hypotheses given above; no application-specific theorem is used.
