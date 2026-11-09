# Reference Proof

## Theorem-critical obligations

The proof closes the following obligations, corresponding to the provenance step identifiers:

1. **step_001:** Recover the observation transformation, verify the domains and integrability needed for the true experiment, and prove equality of the endpoint constants.
2. **step_002:** Derive the tail-integral and scale-transform estimates uniformly on compact parameter intervals above the endpoint constant.
3. **step_003:** Derive the DP value asymptotic, identify the optimal known-parameter value, and prove the prophet asymptotic with explicit integrable envelopes.
4. **step_004:** Establish the estimator confidence event in its valid parameter range.
5. **step_005:** Prove the conditional policy comparison and parameter monotonicity, and justify averaging over all exploration outcomes.
6. **step_006:** Verify that the compact-uniform result applies to the moving conservative parameter.
7. **step_007:** Control the exploration and estimation perturbations and obtain both claimed ratios.

All constants below may depend on the fixed function phi and its support endpoint. Constants indexed by a compact parameter interval may additionally depend on that interval, but not on its varying parameter or on the horizon. No uniformity over different underlying families is asserted.

## step_001: Definition closure, integrability, and endpoint constants

A strictly increasing bijection between the intervals in the task is continuous, as is its inverse. For every lambda>0 and y>=0,
\[
\mathbb P_\lambda\{\phi(X_1)\le y\}
=F_\lambda(\psi(y))=1-e^{-\lambda y}.
\]
Thus Y=phi(X_1) has the exponential distribution with rate lambda, and X_1=psi(Y). In particular, the exploration sum is finite and strictly positive almost surely. The estimator can be completed arbitrarily on its null exceptional set, for example by accepting the final reward there.

On the smooth tail, set
\[
f=\psi'/\psi,\qquad g=\psi''/\psi'.
\]
These quantities are defined and f>0. Direct differentiation gives
\[
f'=f(g-f).
\]
If c>0, then f' converges to c(c'-c). A nonzero limit would make f eventually change at a rate bounded away from zero, contradicting its finite limit. Therefore c'=c. If c=0 and c'>0, then eventually f<=c'/4 and g>=c'/2, so
\[
(\log f)'=g-f\ge c'/4.
\]
This forces f to grow exponentially, contradicting f->0. Consequently c'=c also at the endpoint c=0.

For any eta>c, choose b>0 with c+b<eta. The bound f(y)<=c+b on a sufficiently late tail gives psi(y)<=A exp((c+b)y) there. Since psi is bounded on bounded intervals,
\[
\mu(\eta):=\mathbb E_\eta X_1
=\eta\int_0^\infty e^{-\eta y}\psi(y)\,dy<\infty.
\]
Also mu(eta)>x0, because psi(Y)>x0 almost surely. In particular, the true mean is positive and finite. For each finite n, the prophet benchmark is positive and finite since the maximum is bounded by the sum.

For finite a>=x0, writing the positive part as an integral of indicators and exchanging nonnegative integrals gives
\[
\mathbb E_\eta[(X_1-a)^+]
=\int_a^\infty\mathbb P_\eta(X_1>t)\,dt=r_\eta(a).
\]
It also gives mu(eta)=x0+r_eta(x0), with extended-real values permitted. If mu(eta)=infinity, every finite-a tail integral is infinite. The task's recursion then has V_i(eta;h)=infinity for every i<=h, because r_eta(infinity)=0. The corresponding policy rejects until its prescribed final acceptance. No finite-mean assumption is made for such estimated parameters.

The functions mu(eta) and r_eta(a) are measurable extended-real functions: their integral representations have nonnegative measurable integrands, and the prescribed value at a=infinity is measurable. Consequently the recursively defined thresholds are measurable functions of the exploration data. The policy is adapted and always stops by n. Its true payoff is nonnegative and bounded by the realized prophet maximum, hence integrable.

## step_002: Uniform tail and scale estimates

Fix K=[a,b] contained in (c,infinity), so a>c. Choose kappa>0 with c+kappa<a. Since g(y)->c, for all sufficiently large y and every s>=0,
\[
\frac{\psi'(y+s)}{\psi'(y)}\le e^{(c+\kappa)s},
\]
and this ratio tends to e^{cs} for every fixed s. These statements follow by applying the derivative bounds to log psi'; bounded derivatives on each sufficiently late compact interval justify the corresponding integral identities.

Changing variables only on the smooth tail yields
\[
r_\eta(\psi(y))=\psi'(y)e^{-\eta y}I_\eta(y),\qquad
I_\eta(y)=\int_0^\infty e^{-\eta s}\frac{\psi'(y+s)}{\psi'(y)}\,ds.
\]
Moreover,
\[
\sup_{\eta\in K}\left|I_\eta(y)-\frac1{\eta-c}\right|
\le\int_0^\infty e^{-as}
\left|\frac{\psi'(y+s)}{\psi'(y)}-e^{cs}\right|\,ds\longrightarrow0.
\]
Here dominated convergence applies with the integrable majorant
\[
e^{-(a-c-\kappa)s}+e^{-(a-c)s}.
\]
Since 1/(eta-c) is bounded above and bounded away from zero on K,
\[
r_\eta(\psi(y))=\frac{\psi'(y)e^{-\eta y}}{\eta-c}(1+o(1))
\]
uniformly in eta in K.

The tail-integral formula shows that mu(eta) decreases in eta. Thus
\[
x_0<\mu(b)\le\mu(\eta)\le\mu(a)<\infty.
\]
For x>=mu(eta), define
\[
H_\eta(x)=1+\int_{\mu(\eta)}^x\frac{dt}{r_\eta(t)},
\qquad Q_\eta(y)=H_\eta(\psi(y)).
\]
Choose y0 on the smooth tail with psi(y0)>=mu(a). The initial quantities Q_eta(y0) are uniformly bounded: on the integration interval,
\[
r_\eta(t)\ge r_b(\psi(y_0))>0.
\]
For large y, the tail estimate gives
\[
Q_\eta'(y)=(\eta-c)e^{\eta y}(1+o(1))
\]
uniformly in eta. For any alpha in (0,1), take y0 larger if necessary so that the derivative is between (1-alpha)(eta-c)e^{eta y} and (1+alpha)(eta-c)e^{eta y}, for every eta in K and y>=y0. Integrating these inequalities, dividing by ((eta-c)/eta)e^{eta y}, and using a>0, the uniform initial bound, and the positive lower bound on (eta-c)/eta gives
\[
H_\eta(\psi(y))=\frac{\eta-c}{\eta}e^{\eta y}(1+o(1))
\]
uniformly in eta. Equivalently,
\[
H_\eta(x)=\frac{\eta-c}{\eta}e^{\eta\phi(x)}(1+o(1)),\qquad x\to\infty,
\]
uniformly on K.

## step_003: DP and prophet asymptotics

First, for a finite-mean parameter eta, backward induction in the finite-horizon stopping problem gives
\[
V_h(\eta;h)=\mu(\eta),\qquad
V_i(\eta;h)=\mathbb E_\eta[\max\{X_1,V_{i+1}(\eta;h)\}].
\]
At a nonterminal stage, accepting the current reward is optimal exactly when it is at least the constant optimal continuation value. At the final stage acceptance is optimal because rewards are nonnegative. The positive-part identity therefore gives precisely the task's recursion for i<h. This both establishes optimality and avoids evaluating r_eta below x0.

Take h=N and eta in K. Write W_i=H_eta(V_i(eta;N)); then W_N=1. If v=V_{i+1}, monotonicity of r_eta gives
\[
1\le W_i-W_{i+1}
=\int_v^{v+r_\eta(v)}\frac{dt}{r_\eta(t)}
\le\frac{r_\eta(v)}{r_\eta(v+r_\eta(v))}.
\]
Also,
\[
r_\eta(v)-r_\eta(v+r_\eta(v))
\le r_\eta(v)e^{-\eta\phi(v)}.
\]
Since v>=mu(eta)>x0, this implies
\[
W_i-W_{i+1}\le\frac1{1-e^{-\eta\phi(v)}}.
\]
To make the resulting error uniform, put
\[
G_\eta(v)=H_\eta(v)\frac{e^{-\eta\phi(v)}}{1-e^{-\eta\phi(v)}}.
\]
The uniform scale estimate shows that G_eta(v) is uniformly bounded for sufficiently large v. On any remaining bounded range mu(eta)<=v<=A, the bounds
\[
H_\eta(v)\le1+\frac{A-\mu(b)}{r_b(A)},\qquad
1-e^{-\eta\phi(v)}\ge1-e^{-a\phi(\mu(b))}>0
\]
give a uniform bound there as well. Hence a finite B, independent of eta and N, satisfies
\[
1\le W_i-W_{i+1}\le1+\frac{B}{W_{i+1}}.
\]
The lower bound yields W_j>=N-j+1. Summation now gives
\[
N\le W_1\le N+B\sum_{k=1}^{N-1}\frac1k
=N+O(\log N)
\]
uniformly in eta.

The values V_1(eta;N) escape to infinity uniformly on K: otherwise W_1 would remain bounded along a sequence with bounded V_1 by the preceding bounded-range estimate for H, contradicting W_1>=N. Therefore the uniform scale estimate is applicable at V_1. Taking logarithms gives
\[
\phi(V_1(\eta;N))=
\frac{\log N}{\eta}+d(\eta)+o(1),\qquad
 d(\eta)=\frac1\eta\log\frac{\eta}{\eta-c},
\]
uniformly on K.

For every fixed D>0,
\[
\sup_{|u|\le D}\left|
\log\frac{\psi(y+u)}{\psi(y)}-cu\right|
\le D\sup_{t\ge y-D}|f(t)-c|\longrightarrow0.
\]
The function d is bounded on K, and inf_eta(log N)/eta=(log N)/b tends to infinity. Applying the bounded-shift estimate, including the uniform o(1) shift, proves
\[
V_1(\eta;N)=C(\eta)\psi\!\left(\frac{\log N}{\eta}\right)(1+o(1)),\qquad
C(\eta)=\left(\frac{\eta}{\eta-c}\right)^{c/\eta},
\]
uniformly on K. In particular, at eta=theta and N=n this is the expected payoff of tau*.

For the prophet, put Y_i=phi(X_i), Y_(n)=max_i Y_i, and y_n=(log n)/theta. The transformed maximum has distribution (1-e^{-theta y})^n for y>=0, and hence density n theta e^{-theta y}(1-e^{-theta y})^{n-1}. Since max_i X_i=psi(Y_(n)), changing variables z=theta y-log n gives
\[
\frac{\mathrm{OPT}_n(\theta)}{\psi(y_n)}
=\int_{-\log n}^\infty e^{-z}
\left(1-\frac{e^{-z}}n\right)^{n-1}
\frac{\psi(y_n+z/\theta)}{\psi(y_n)}\,dz.
\]
Extend the integrand by zero below -log n. For each fixed z it converges to
\[
e^{-z-e^{-z}}e^{(c/\theta)z}.
\]
For z<0, the psi ratio is at most one, and, for n>=2 on the integration domain, the remaining factor is bounded by
\[
e^{-z}\exp(-e^{-z}/2),
\]
which is integrable on the negative half-line. For z>=0 choose kappa>0 with c+kappa<theta. For all sufficiently large n, the logarithmic derivative bound gives
\[
\frac{\psi(y_n+z/\theta)}{\psi(y_n)}
\le e^{((c+\kappa)/\theta)z}.
\]
Thus the integrand is bounded by exp(-(1-(c+kappa)/theta)z), integrable on the positive half-line. Dominated convergence is therefore justified, including c=0. Substituting u=e^{-z} in the limiting integral yields
\[
\frac{\mathrm{OPT}_n(\theta)}{\psi(y_n)}
\longrightarrow\int_0^\infty u^{-c/\theta}e^{-u}\,du
=\Gamma(1-c/\theta).
\]
The gamma argument is positive because c<theta. Dividing the known-parameter DP asymptotic by this prophet asymptotic proves the first required limit.

## step_004: Confidence event

Let S=sum_{i=1}^m phi(X_i) and T=theta S. Then T is a sum of m independent rate-one exponential variables. Direct integration gives E[e^{tT}]=(1-t)^{-m} for t<1. Applying exponential Markov bounds with t=epsilon/(1+epsilon) for the upper tail and t=-epsilon/(1-epsilon) for the lower tail gives, for 0<epsilon<1,
\[
\mathbb P(T\ge m(1+\epsilon))
\le e^{-m(\epsilon-\log(1+\epsilon))},
\]
\[
\mathbb P(T\le m(1-\epsilon))
\le e^{-m(-\epsilon-\log(1-\epsilon))}.
\]
The two exponents in parentheses are at least epsilon^2/4: integrate t/(1+t)>=t/2 on [0,epsilon] for the first, and t/(1-t)>=t for the second. Thus
\[
\mathbb P(|T/m-1|>\epsilon)\le2e^{-m\epsilon^2/4}.
\]
The exploration assumptions imply m->infinity, so 0<epsilon_m<1 for all sufficiently large n. Since theta/theta_hat_m=T/m, the event
\[
\mathcal G_m=\{|\theta/\widehat\theta_m-1|\le\varepsilon_m\}
\]
has probability at least 1-delta for these n. On this event,
\[
\theta\le\eta\le\theta_+:=\theta\frac{1+\varepsilon_m}{1-\varepsilon_m}.
\]
No finite-horizon confidence claim with epsilon_m<1 is used before that inequality holds.

## step_005: Conditional comparison and averaging

Fix a deterministic eta>=theta and a post-exploration horizon N. These surrogate values are finite since eta>=theta>c. For the thresholds t_i=V_{i+1}(eta;N), let L_i denote their expected payoff from stage i under the true law, with final acceptance. Then L_N=mu(theta)>=mu(eta)=V_N(eta;N).

If L_{i+1}>=t_i, independence of future observations gives
\[
L_i=\mathbb E_\theta[X_1\mathbf1\{X_1\ge t_i\}]
+\mathbb P_\theta(X_1<t_i)L_{i+1}.
\]
Using the positive-part identity,
\[
L_i=t_i+\mathbb P_\theta(X_1<t_i)(L_{i+1}-t_i)+r_\theta(t_i)
\ge t_i+r_\eta(t_i)=V_i(\eta;N).
\]
Here r_theta>=r_eta because eta>=theta. Backward induction proves L_1>=V_1(eta;N).

For finite-mean parameters, the map
\[
T_\eta(v)=v+r_\eta(v)=\mathbb E_\eta\max\{X_1,v\},\qquad v\ge x_0,
\]
is increasing in v and decreasing in eta. Its first property follows directly from the maximum, and its second from the tail integral. Together with monotonicity of mu, backward induction proves that V_i(eta;N) decreases in eta.

Condition now on the actual exploration data. Future observations remain independent with law F_theta. For almost every exploration history in G_m, the preceding deterministic comparisons give
\[
\mathbb E_\theta[X_\tau\mid X_1,\ldots,X_m]
\ge V_1(\eta;N)\ge V_1(\theta_+;N).
\]
On the complement, the policy is still defined and its payoff is nonnegative, even if the surrogate mean is infinite. Consequently
\[
\mathbb E_\theta X_\tau
\ge\mathbb P_\theta(\mathcal G_m)V_1(\theta_+;N)
\ge(1-\delta)V_1(\theta_+;N).
\]

## step_006: Application of compact uniformity

The uniform result needed here was derived, not assumed, in steps 002 and 003. Its constants are uniform on each fixed K contained in (c,infinity); this includes the tail envelope, initial scale-transform bound, increment bound, escape of V_1, and inversion error.

Because epsilon_m->0, theta_+->theta. Choose d0 in (0,theta-c) and K=[theta-d0,theta+d0]. Then K is contained in (c,infinity) and theta_+ belongs to K eventually. Also N=n-m tends to infinity. Therefore
\[
V_1(\theta_+;N)=C(\theta_+)\psi\!\left(\frac{\log N}{\theta_+}\right)(1+o(1)).
\]
The compact interval is only an analytical device: neither it nor theta_+ is supplied to the learning policy.

## step_007: Perturbation and final limit

Since delta is fixed in (0,1), the prescribed lower growth rate of m implies
\[
\varepsilon_m\log n\longrightarrow0.
\]
The difference in the arguments of psi has the exact form
\[
u_n:=\frac{\log N}{\theta_+}-\frac{\log n}{\theta}
=\frac{\log(1-m/n)}{\theta_+}
-\frac{2\varepsilon_m\log n}{\theta(1+\varepsilon_m)}\longrightarrow0.
\]
The first term vanishes because m/n->0 and theta_+->theta>0. Since f=psi'/psi is bounded on a sufficiently late tail,
\[
\log\frac{\psi(y_n+u_n)}{\psi(y_n)}
=\int_{y_n}^{y_n+u_n}f(t)\,dt\longrightarrow0.
\]
Hence the psi ratio tends to one. The function C is continuous on (c,infinity), including the case c=0 where it is identically one. It follows that
\[
V_1(\theta_+;N)=C(\theta)\psi(y_n)(1+o(1)).
\]
Combining this with the unconditional lower bound and the already proved prophet asymptotic gives
\[
\liminf_{n\to\infty}\mathrm{CR}_n(\tau;\theta)
\ge(1-\delta)\frac{C(\theta)}{\Gamma(1-c/\theta)}.
\]
Together with the known-parameter limit in step 003, this proves both targets. All arguments allow x0=0 or x0>0 and c=0 or 0<c<theta. There is no unresolved theorem-critical dependency.
