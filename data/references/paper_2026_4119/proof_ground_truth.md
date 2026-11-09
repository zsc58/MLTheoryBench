# Reference Proof

## Contract and proof obligations

The iteration is the source iteration: the primal divergence has coefficient \(1/2\), the dual step size is \(\eta=N^{-1/2}\), and the dual average uses \(\lambda^0,\ldots,\lambda^{N-1}\). Each horizon is a separate run from the same initial pair and potential. The drift is independent of the population law. Consequently deviations are fixed occupation pairs, and randomized consistent occupation laws have domain \(\mathcal M=\mathcal P(\mathcal R)\).

The obligations are: (a) compactness and the continuity/affinity properties of the occupation model; (b) continuity, convexity, and the required derivative of regret; (c) strong duality and saddle attainment; (d) existence of the updates and the correctly indexed telescoping estimate; (e) separate rates, bounded averaged multipliers, and identification of every subsequential limit. All are addressed below. No specialized occupation-representation or Nash-existence theorem is assumed to close an obligation.

## 1. Occupation-space properties

Write \(p=\bar p>2\). First derive uniform moment bounds for \(\boldsymbol m=(m,\overline m)\in\mathcal R\). Let \(V(x)=(1+x^2)^{p/2}\). Boundedness of the drift gives
\[
b(t,x,a)V'(x)+\tfrac{\sigma^2}{2}V''(x)\le C V(x).
\]
Use the bounded smooth functions \(V_R=\chi_R\circ V\), where \(\chi_R(s)=R(1-e^{-s/R})\). Their first two derivatives are bounded for fixed \(R\). Concavity, nonnegativity, and \(s\chi_R'(s)\le\chi_R(s)\) imply \(\mathcal L V_R\le C V_R\), with \(C\) independent of \(R\). Testing the weak identity with \(u(t,x)=\varphi(t)V_R(x)\) shows that \(t\mapsto\int V_R(x)m_t(dx,da)\) has an absolutely continuous representative with initial value \(\int V_R\,dm_0\), derivative \(\int\mathcal L V_R\,dm_t\), and terminal value \(\int V_R\,d\overline m\). Gronwall followed by monotone convergence yields
\[
\operatorname*{ess\,sup}_{t\in[0,T]}\int |x|^p m_t(dx,da)+\int |x|^p\overline m(dx)\le C_p.
\]
The constants depend only on the model bounds, horizon, and initial moment. Thus the occupation measures with time marginal \(dt\), and their terminal laws, are tight and have uniformly integrable second moments.

We use the standard probability compactness fact that tightness together with uniform integrability of second moments gives relative compactness for weak convergence tested against continuous functions of at most quadratic growth. It follows by extracting a weakly convergent subsequence and truncating the test functions; the uniform tail bound makes the truncation error tend to zero. Here time and action are compact, and the displayed \(p\)-moment estimate supplies the required tails. Limits retain time marginal \(dt\) and disintegrate into measurable probability flows.

We also need a stable-convergence observation. On a compact state-action set, a measurable-in-time, continuous-in-state-action test function with a uniform bound can be approximated in \(L^1(dt;C(K))\) by finite sums \(c_j(t)q_j(x,a)\). Approximate the scalar measurable coefficients \(c_j\) in \(L^1(dt)\) by continuous functions. Since every occupation measure has the same time marginal, these approximation errors are uniform over the measures. Therefore quadratic weak convergence implies convergence against such Caratheodory tests. A continuous cutoff and the uniform moment tails extend the assertion to tests bounded by \(C(1+|x|^2)\). Apply this to the bounded generator integrand in each martingale identity. The identity passes to the limit, so \(\mathcal R\) is closed, hence compact. Convexity follows from linearity of the identity. Its topology is metrizable: identify \(m\) with \(T^{-1}dt\,m_t\) and use the usual second-moment weak metric, together with the corresponding terminal metric.

For completeness, this domain agrees with the original consistent-law definition. Testing the integrated residual against all bounded continuous functions of the occupation pair makes the residual zero almost surely. Intersect these full-measure sets over a countable determining family of smooth martingale tests. Such a family is obtained by smooth approximation on increasing compact sets; boundedness of the coefficients permits passage from this family to all bounded smooth tests. Every consistent law is therefore supported on \(\mathcal R\). Conversely, integrating the pointwise occupation identity against any law on \(\mathcal R\) gives the consistent-law identity. Thus \(\mathcal M=\mathcal P(\mathcal R)\), compact and metrizable in its weak topology and convex in the vector space of finite signed measures. Strict feasibility ensures nonemptiness; a separate Nash-existence theorem is unnecessary.

Define privately, for \(\boldsymbol m,\boldsymbol k\in\mathcal R\),
\[
F[\boldsymbol m](\boldsymbol k)=\int_0^T\!\int f(t,x,m_t,a)k_t(dx,da)dt+\int g(x,\overline m)\overline k(dx),
\]
and let \(F_0(\boldsymbol m)\) be the analogous moderator integrand evaluated at \(\boldsymbol m\).

Here is the required continuity argument. For a running-cost statistic \(\widehat f_i\), put \(H_i^m(t)=\int\widehat f_i(t,x)m_t(dx,da)\). Its at-most-linear growth and the moment bounds give a uniform bound. The weak identity, extended to this statistic by smooth cutoffs, gives uniformly bounded time variation, since its derivatives and the drift are bounded. If \(\boldsymbol m_j\to\boldsymbol m\), compactness of bounded-variation functions in \(L^1([0,T])\) gives convergent subsequences of \(H_i^{m_j}\). Testing against continuous time functions identifies every such limit with \(H_i^m\); hence the whole sequence converges in \(L^1\).

For \(\boldsymbol m_j\to\boldsymbol m\) and \(\boldsymbol k_j\to\boldsymbol k\), split the running-cost difference into a fixed-integrand term integrated against \(k_j-k\), and a term involving \(H_i^{m_j}-H_i^m\). The stable-convergence observation makes the first term vanish. The weighted local Lipschitz assumption bounds the second by
\[
C\int_0^T |H_i^{m_j}(t)-H_i^m(t)|dt,
\]
using the uniform moments and bounded scalar aggregates. It also vanishes. For terminal costs the statistic converges by quadratic weak convergence and its linear growth; the same splitting and Lipschitz bound apply. Thus \(F\) is jointly continuous and \(F_0\) is continuous. Compactness makes them bounded. The public cost formulas consequently define continuous affine functions of \(\rho\), and the deviation cost is jointly continuous in \((\rho,\boldsymbol k)\).

## 2. Regret and its derivative

Set
\[
q(\boldsymbol m,\boldsymbol k)=F[\boldsymbol m](\boldsymbol m)-F[\boldsymbol m](\boldsymbol k),\qquad J(\rho,\boldsymbol k)=\int q(\boldsymbol m,\boldsymbol k)\rho(d\boldsymbol m).
\]
The kernel is bounded and jointly continuous. Uniform continuity on the compact product shows that \(J\) is jointly continuous, including in its weak probability-law variable. It is affine in \(\rho\). Therefore \(r(\rho):=\operatorname{ER}(\rho)=\max_{\boldsymbol k\in\mathcal R}J(\rho,\boldsymbol k)\) is convex. Compactness and joint continuity show that this maximum is attained and varies continuously; in particular \(G:=\max_{\rho\in\mathcal M}|r(\rho)|<\infty\). Also \(r(\rho)\le0\) is exactly the family of inequalities \(\Gamma(\rho)\le\Gamma^{\rm dev}(\rho,\boldsymbol k)\) for all fixed deviations.

Uniqueness gives continuous dependence of \(\boldsymbol k^*(\rho)\). Indeed, for any converging sequence of laws, each convergent subsequence of their maximizers has, by joint continuity, a maximizing limit for the limiting law. Uniqueness identifies that limit, and compactness then gives convergence of the whole sequence.

For \(\rho_t=\rho+t(\rho'-\rho)\), \(t>0\), optimality at the two endpoints gives
\[
\int q(\boldsymbol m,\boldsymbol k^*(\rho))(\rho'-\rho)(d\boldsymbol m)
\le\frac{r(\rho_t)-r(\rho)}t
\le\int q(\boldsymbol m,\boldsymbol k^*(\rho_t))(\rho'-\rho)(d\boldsymbol m).
\]
The bounds have a common limit. Applying the same argument at points of the segment gives a continuous segment derivative. The fundamental theorem of calculus yields the flat derivative
\[
\frac{\delta r}{\delta\rho}(\rho,\boldsymbol m)=q(\boldsymbol m,\boldsymbol k^*(\rho)).
\]
It is bounded and jointly continuous. Thus \(L(\cdot,\lambda)\) is convex, continuous, and flat differentiable for every \(\lambda\ge0\). Affinity of the underlying cost integrals, rather than flat differentiability alone, is what establishes convexity of regret.

## 3. Strong duality and saddle attainment

Write \(f_0=\Gamma_0\), \(V=V_{\rm LP}\), and \(\delta=-r(\rho_{\rm s})>0\). The feasible set is nonempty and closed in compact \(\mathcal M\), so a constrained optimizer \(\rho^*\) exists. For fixed \(\rho\),
\[
\sup_{\lambda\ge0}L(\rho,\lambda)=
\begin{cases}f_0(\rho),&r(\rho)\le0,\\+\infty,&r(\rho)>0.\end{cases}
\]
We use the standard minimax theorem in the following form: if the minimizing domain is compact convex in a Hausdorff topological vector space, the maximizing domain is convex, and the real-valued function is continuous and convex in the first variable and continuous and concave in the second, then its infimum-supremum equals its supremum-infimum. The second domain need not be compact. Here the ambient space is the finite signed measures with topology \(\sigma(\mathcal M_s(\mathcal R),C(\mathcal R))\), the minimizing domain is \(\mathcal M\), and the maximizing domain is \([0,\infty)\). The preceding section verifies all function hypotheses. Consequently
\[
V=\min_{\rho\in\mathcal M}\sup_{\lambda\ge0}L(\rho,\lambda)
=\sup_{\lambda\ge0}\min_{\rho\in\mathcal M}L(\rho,\lambda).
\]
The dual objective \(d(\lambda)=\min_\rho L(\rho,\lambda)\) is upper semicontinuous, being an infimum of continuous affine functions, and
\[
d(\lambda)\le f_0(\rho_{\rm s})-\delta\lambda\longrightarrow-\infty.
\]
It therefore attains its maximum at some \(\lambda^*\ge0\). Pair this dual optimizer with the constrained primal optimizer \(\rho^*\). For every \(\rho,\lambda\),
\[
L(\rho^*,\lambda)\le V=d(\lambda^*)\le L(\rho,\lambda^*).
\]
Taking \((\rho,\lambda)=(\rho^*,\lambda^*)\) shows equality at the pair and proves the saddle inequalities. In particular \(\lambda^*r(\rho^*)=0\). Conversely, any saddle pair is feasible, since otherwise its multiplier supremum is infinite; comparison with multiplier zero gives complementary slackness, and comparison with feasible primal points proves optimality.

Let \(\Omega_0=\max_{\mathcal M}f_0-\min_{\mathcal M}f_0\). The strict-feasibility comparison gives the useful bound
\[
0\le\lambda^*\le\frac{f_0(\rho_{\rm s})-V}{\delta}\le\frac{\Omega_0}{\delta}.
\]
Selecting an arbitrary minimizer of \(L(\cdot,\lambda^*)\) would not justify these conclusions; the constrained primal optimizer is essential to this argument.

## 4. Updates and the telescoping estimate

The potential and its derivative are continuous on their compact domains. Hence \(D_h\) is jointly continuous and finite. Convexity gives \(D_h\ge0\), and
\[
B_h:=\max_{\rho\in\mathcal M}D_h(\rho,\rho^0)<\infty.
\]
The primal minimum is attained by compactness; the dual projection is uniquely defined. Strict convexity of \(h\) is not needed, and all estimates hold for every choice of primal minimizers.

We recall and derive the primal inequality. If \(x\) minimizes \(F(x)+\tau D_h(x,y)\) on a convex set, its directional derivative toward any comparator \(z\) is nonnegative. Combining this with convexity of \(F\) gives
\[
F(x)-F(z)\le\tau\langle h'(x)-h'(y),z-x\rangle
=\tau\big(D_h(z,y)-D_h(z,x)-D_h(x,y)\big).
\]
The pairing here is integration of the flat derivative against a difference of laws; the equality follows by expanding the three divergences. With \(\tau=1/2\), \(x=\rho^{n+1}\), \(y=\rho^n\), and \(F=L(\cdot,\lambda^n)\), this yields
\[
L(\rho^{n+1},\lambda^n)-L(\rho,\lambda^n)
\le\tfrac12\big(D_h(\rho,\rho^n)-D_h(\rho,\rho^{n+1})-D_h(\rho^{n+1},\rho^n)\big).
\]
Fix \(\eta=N^{-1/2}\), set \(r_{n+1}=r(\rho^{n+1})\) and \(\Delta\lambda_n=\lambda^{n+1}-\lambda^n\). The first-order condition for minimizing \(-\lambda r_{n+1}+(\lambda-\lambda^n)^2/(2\eta)\) on the nonnegative half-line gives
\[
(\lambda-\lambda^{n+1})r_{n+1}
\le\frac{(\lambda^n-\lambda)^2-(\lambda^{n+1}-\lambda)^2-|\Delta\lambda_n|^2}{2\eta}.
\]
This sign is important. The gap at the old dual iterate decomposes exactly as
\[
\begin{aligned}
L(\rho^{n+1},\lambda)-L(\rho,\lambda^n)
={}&L(\rho^{n+1},\lambda^n)-L(\rho,\lambda^n)\\
&+(\lambda-\lambda^{n+1})r_{n+1}+\Delta\lambda_n r_{n+1}.
\end{aligned}
\]
Young's inequality bounds the last term by \(|\Delta\lambda_n|^2/(2\eta)+\eta r_{n+1}^2/2\). It cancels the negative squared increment. Dropping the nonpositive Bregman increment leaves
\[
L(\rho^{n+1},\lambda)-L(\rho,\lambda^n)
\le P_n(\rho,\lambda)-P_{n+1}(\rho,\lambda)+\frac{\eta G^2}{2},
\]
where
\[
P_n(\rho,\lambda)=\frac12D_h(\rho,\rho^n)+\frac{(\lambda^n-\lambda)^2}{2\eta}\ge0.
\]
Summation, division by \(N\), convexity in the primal variable, and affinity in the multiplier give
\[
L(\bar\rho_N,\lambda)-L(\rho,\bar\lambda_N)
\le\frac{D_h(\rho,\rho^0)}{2N}
+\frac{(\lambda-\lambda^0)^2+G^2}{2\sqrt N}.
\tag{*}
\]
For \(0\le\lambda\le\Lambda\), use \((\lambda-\lambda^0)^2\le2\Lambda^2+2(\lambda^0)^2\) and \(N^{-1}\le N^{-1/2}\). Thus the requested gap bound holds, for example, with
\[
C_{\rm gap}=1+\tfrac12\big(B_h+2(\lambda^0)^2+G^2\big).
\]
It is independent of both \(N\) and \(\Lambda\).

## 5. Separate rates and bounded averaged multipliers

Use \((\rho,\lambda)=(\rho^*,0)\) in (*). Since \(r(\rho^*)\le0\) and \(\bar\lambda_N\ge0\),
\[
f_0(\bar\rho_N)-V\le\frac{C_{ rm obj}}{\sqrt N},\qquad
C_{ rm obj}=\tfrac12\big(B_h+(\lambda^0)^2+G^2\big).
\]
In this display, the constant is denoted \(C_{\rm obj}\).

For clarity, the separate regret estimate requires a different comparator. The saddle inequality gives
\[
f_0(\bar\rho_N)-V+\lambda^*r(\bar\rho_N)\ge0.
\]
Use \((\rho,\lambda)=(\rho^*,\lambda^*+1)\) in (*). Its left-hand side is at least
\[
f_0(\bar\rho_N)-V+(\lambda^*+1)r(\bar\rho_N)\ge r(\bar\rho_N).
\]
Therefore
\[
r(\bar\rho_N)\le\frac{C_{\rm reg}}{\sqrt N},\qquad
C_{\rm reg}=\tfrac12\left(B_h+\left(1+\frac{\Omega_0}{\delta}+\lambda^0\right)^2+G^2\right).
\]
These inequalities do not presume that either the objective gap or regret is nonnegative.

Finally take \((\rho,\lambda)=(\rho_{\rm s},0)\) in (*). Since \(r(\rho_{\rm s})=-\delta\),
\[
\delta\bar\lambda_N\le f_0(\rho_{\rm s})-f_0(\bar\rho_N)+\frac{C_{\rm obj}}{\sqrt N}
\le\Omega_0+C_{\rm obj}.
\]
This uniformly bounds the averaged multipliers. All constants depend only on structural bounds, the fixed potential and initial iterates, and the strict-feasibility margin.

## 6. Every subsequential limit

Compact metrizability of \(\mathcal M\) and the preceding multiplier bound give a convergent subsequence with indices tending to infinity. Let \((\rho^\infty,\lambda^\infty)\) be any such limit. For arbitrary fixed \(\rho\in\mathcal M\) and finite \(\lambda\ge0\), continuity allows passage to the limit in (*), giving
\[
L(\rho^\infty,\lambda)-L(\rho,\lambda^\infty)\le0.
\]
The same convergent subsequence works for every comparator; no uniformity over an unbounded multiplier set or additional diagonal extraction is needed. Set \(\rho=\rho^\infty\) and then \(\lambda=\lambda^\infty\) to obtain the two saddle inequalities. Section 3 then gives feasibility, complementary slackness, and \(\Gamma_0(\rho^\infty)=V_{\rm LP}\).

## Source-local corrections

The envelope proof's reference to (6.2) at line 736 means (6.14). The three-point calculation's reference to (6.2) at line 790 means (6.20). In line 819 the divergence is \(D_\psi(\overline\rho,\rho^{(0)})\), not its reverse. These are local reference/orientation corrections; the proof above derives the relevant statements explicitly.
