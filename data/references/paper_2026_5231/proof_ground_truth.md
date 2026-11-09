# Reference Proof

## Proof Structure

The obligations are: identify the fixed-drift laws; verify the weight's definition, smoothness, and absolute integrability; derive its transform without an invalid interchange; prove conditional and mixture unbiasedness and uniqueness; obtain both population bias orders; control empirical transforms at both scales; verify the estimators remain in their domains; and justify plugging a same-sample boundary estimate into the singular weight family. All are closed below.

## 1. Fixed-drift laws and estimator domains

We use the following standard Brownian first-exit facts, explicitly stated in the source and indexed by theory_021. For standard Brownian motion starting at zero, symmetric absorbing boundaries at \(\pm\beta\), and zero drift, the exit time has a strictly positive density on \((0,\infty)\):
\[
 f_{0,\beta}(t)=\sqrt{\frac2\pi}\,t^{-3/2}
 \sum_{k\ge0}(-1)^k(2k+1)\beta
 e^{-(2k+1)^2\beta^2/(2t)}.
\]
For deterministic drift \(d\) and boundary \(a\), the joint density of choice and exit time is
\[
 p_{d,a}(y,t)=\frac12 f_{0,a}(t)e^{ady-d^2t/2},
 \qquad y\in\{-1,1\},\quad t>0.
\]
The associated exit-time Laplace transform is
\[
 \mathbb E_d[e^{-\lambda S}]
 =\frac{\cosh(ad)}{\cosh(a\sqrt{d^2+2\lambda})},\qquad\lambda\ge0.
\]
These are standard independent first-exit identities, not assumptions about the unknown drift distribution. Their hypotheses hold for each fixed-drift experiment in the task: the diffusion coefficient is one, the starting point is zero, and the boundaries are fixed and symmetric. Conditioning the given model on its drift uses exactly this kernel because its Brownian motion is independent of the drift.

Summing the joint density over \(y\) gives
\[
 f_{d,a}(t)=\cosh(ad)e^{-d^2t/2}f_{0,a}(t).
\]
Dividing the joint density by this marginal shows that the conditional choice probability is independent of \(t\). Thus \(Y\) and \(S\) are independent under \(\mathbb E_d\), with \(\mathbb E_d[Y]=\tanh(ad)\).

Also \(0<S<\infty\) almost surely. Positivity follows from path continuity and the initial point lying strictly between the boundaries. Finiteness can also be seen directly: for each fixed \(d\), a unit-time Brownian increment greater than \(2a+|d|\) forces an exit during that interval from any unabsorbed starting point. These independent increments give a geometric bound on survival across integer times. Mixing over \(D\) preserves almost-sure finiteness.

Consequently, for every positive \(\lambda\) and every finite nonempty sample,
\[
 0<\ell_n(4\lambda)<\ell_n(\lambda)<1
\]
almost surely. The logarithms are therefore finite, and both boundary estimates, in particular \(\widetilde a_n\), are strictly positive. No projection, exceptional-event redefinition, or sample splitting is needed.

## 2. Weight representations, continuity, and an integrable envelope

For private calculations, write
\[
 J_\beta(t)=\sum_{k\ge0}(-1)^k c_k(\beta)e^{-c_k(\beta)^2/(2t)},
 \quad
 N_\beta(t)=\sum_{k\ge0}\left(\frac{c_k(\beta)^2}{t}-1\right)e^{-c_k(\beta)^2/(2t)},
\]
and
\[
 q_\beta(t)=\sqrt{\frac2\pi}\,t^{-3/2}N_\beta(t).
\]
The standard density formula gives \(f_{0,\beta}(t)=\sqrt{2/\pi}\,t^{-3/2}J_\beta(t)>0\), so the public denominator is nonzero and \(w_\beta=q_\beta/f_{0,\beta}\). On every compact subset of \((0,\infty)^2\), the image series and all their derivatives converge uniformly, because polynomial factors are dominated by their Gaussian tails. Hence the weight is jointly continuous and smooth.

We derive the two spectral representations rather than assume them. The standard shifted Poisson formula used in the source is
\[
 \sum_{j\in\mathbb Z}h(j+\alpha)
 =\sum_{m\in\mathbb Z}e^{2\pi i m\alpha}\widehat h(m),
 \qquad
 \widehat h(\xi)=\int_{\mathbb R}h(x)e^{-2\pi i x\xi}\,dx,
\]
for Schwartz functions \(h\). All applications below use a Gaussian or a modulated Gaussian, so this hypothesis holds. Their series and differentiated series converge uniformly on compact parameter sets.

First put
\[
 \Theta_\beta(t)=\sum_{k\ge0}e^{-(2k+1)^2\beta^2/(2t)}.
\]
Shifted Poisson summation and the Gaussian transform give
\[
 \Theta_\beta(t)=\frac{\sqrt{\pi t/2}}{2\beta}
 \left(1+2\sum_{m\ge1}(-1)^m e^{-m^2\pi^2t/(2\beta^2)}\right).
\]
Since \(N_\beta=-\partial_\beta(\beta\Theta_\beta)\), differentiation yields
\[
 q_\beta(t)=\frac{\pi^2}{\beta^3}
 \sum_{m\ge1}(-1)^{m+1}m^2e^{-m^2\pi^2t/(2\beta^2)}. \tag{1}
\]
For the denominator, the same formula applied to a modulated Gaussian gives
\[
 \Phi_{\beta,t}(\theta)
 :=\sum_{j\in\mathbb Z}e^{-2\beta^2(j+1/2)^2/t}e^{2i\theta(j+1/2)}
 =\sqrt{\frac{\pi t}{2\beta^2}}
 \sum_{m\in\mathbb Z}(-1)^m e^{-t(\theta-\pi m)^2/(2\beta^2)}.
\]
Pairing the terms on the left shows
\(J_\beta(t)=-(\beta/2)\partial_\theta\Phi_{\beta,t}(\pi/2)\).
Differentiating the right and pairing indices \(m=-k\) and \(m=k+1\) therefore gives
\[
 f_{0,\beta}(t)=\frac{\pi}{2\beta^2}
 \sum_{m\ge0}(-1)^m(2m+1)e^{-(2m+1)^2\pi^2t/(8\beta^2)}. \tag{2}
\]
These derivations establish the equivalence of the image and spectral definitions privately; they do not require termwise integration of a divergent spectral-transform series.

Fix a compact interval \(K=[u,v]\subset(0,\infty)\). Factor the leading image term:
\[
 J_\beta(t)=\beta e^{-\beta^2/(2t)}
 \left[1+\sum_{k\ge1}(-1)^k(2k+1)
 e^{-((2k+1)^2-1)\beta^2/(2t)}\right].
\]
The absolute tail tends to zero uniformly over \(\beta\in K\) as \(t\downarrow0\), by domination with the corresponding summable Gaussian tail at any fixed small positive time. Thus, for some \(t_0\in(0,1]\),
\[
 J_\beta(t)\ge\frac u2 e^{-\beta^2/(2t)},\qquad 0<t\le t_0.
\]
Factoring the same exponential from \(N_\beta\), and bounding the remaining sums with polynomially weighted Gaussian tails, gives
\[
 |N_\beta(t)|\le C_K(1+t^{-1})e^{-\beta^2/(2t)}.
\]
Hence \(|w_\beta(t)|\le C_K(1+t^{-1})\) near zero, uniformly on \(K\).

For sufficiently large \(t_1\), the first spectral term dominates uniformly on \(K\) in (1)-(2), giving
\[
 f_{0,\beta}(t)\ge\frac{\pi}{4\beta^2}e^{-\pi^2t/(8\beta^2)},
 \qquad |q_\beta(t)|\le C_K e^{-\pi^2t/(2\beta^2)}.
\]
It follows that
\[
 |w_\beta(t)|\le C_K e^{-3\pi^2t/(8\beta^2)}
 \le C_K e^{-3\pi^2t/(8v^2)},\qquad t\ge t_1.
\]
Joint continuity and positivity of the denominator give a uniform bound on \(K\times[t_0,t_1]\). Enlarging constants produces an envelope \(H_K\) which is bounded by \(C_K(1+t^{-1})\) near zero, bounded on the middle interval, and exponentially decreasing for large \(t\), with
\[
 \sup_{\beta\in K}|w_\beta(t)|\le H_K(t). \tag{3}
\]

Under the population law, the density of \(S\) is
\[
 g_a(t)=\mathbb E[\cosh(aD)e^{-D^2t/2}]f_{0,a}(t)
 \le\cosh(aM)f_{0,a}(t).
\]
The image series gives \(f_{0,a}(t)\le C t^{-3/2}e^{-a^2/(2t)}\) for sufficiently small \(t\). Therefore
\[
 \int_0^{t_0}(1+t^{-1})g_a(t)\,dt
 \le C\int_0^{t_0}(t^{-3/2}+t^{-5/2})e^{-a^2/(2t)}\,dt<\infty.
\]
Away from zero the envelope is bounded. Thus \(\mathbb E[H_K(S)]<\infty\). The same argument works under every fixed drift \(d\), with \(\cosh(aM)\) replaced by the finite constant \(\cosh(ad)\). In particular, \(\mathbb E_d|w_a(S)|<\infty\) for all real \(d\), and \(q_a=w_af_{0,a}\) belongs to \(L^1(0,\infty)\).

## 3. Transform, unbiasedness, and uniqueness

For \(c>0\), put
\[
 h_c(t)=\frac{c}{\sqrt{2\pi}\,t^{3/2}}e^{-c^2/(2t)}.
\]
The Gaussian Laplace pair stated in the source gives, for \(s>0\) and \(r=\sqrt{2s}\),
\[
 \int_0^\infty e^{-st}h_c(t)\,dt=e^{-cr}.
\]
Differentiation in \(c\), justified on compact positive \(c\)-intervals by the Gaussian decay at zero and the factor \(e^{-st}\) at infinity, gives
\[
 -\partial_c h_c(t)=\frac{1}{\sqrt{2\pi}\,t^{3/2}}
 \left(\frac{c^2}{t}-1\right)e^{-c^2/(2t)},
 \quad
 \int_0^\infty e^{-st}[-\partial_c h_c(t)]\,dt=r e^{-cr}. \tag{4}
\]
This is the corrected sign of source L000266, and agrees with its subsequent inverse-transform formula.

We must also justify summing (4). Directly from the Gaussian pair and its derivative,
\[
 \int_0^\infty e^{-st}|\partial_c h_c(t)|\,dt
 \le (r+2/c)e^{-cr}.
\]
For \(c=c_k(a)=(2k+1)a\), the right side is summable for every \(s>0\). Since \(q_a(t)=2\sum_{k\ge0}[-\partial_c h_c(t)]_{c=c_k(a)}\), absolute weighted integrability permits the interchange and gives
\[
 G_a(s):=\int_0^\infty e^{-st}q_a(t)\,dt
 =2\sum_{k\ge0}r e^{-(2k+1)ar}
 =\frac{\sqrt{2s}}{\sinh(a\sqrt{2s})},\qquad s>0. \tag{5}
\]
Since \(q_a\in L^1\), dominated convergence also gives \(G_a(0)=1/a\).

For \(d\ne0\), the fixed-drift law and absolute integrability now yield
\[
 \mathbb E_d[Yw_a(S)]
 =\sinh(ad)G_a(d^2/2)
 =\sinh(ad)\frac{|d|}{\sinh(a|d|)}=d.
\]
At \(d=0\), choice-time independence and \(\mathbb E_0Y=0\) give the same conclusion directly; no division by zero is used. Population absolute integrability was proved in Section 2, so iterated expectation is legitimate and gives
\[
 \mathbb E[Yw_a(S)]=\mathbb E[D]=\mu,
 \qquad \mathbb E[\widehat\mu_n(a)]=\mu.
\]

Let \(g\) be a smooth competitor in the stated admissible class satisfying the identity for every fixed drift. Its integrability at zero drift implies \(g f_{0,a}\in L^1\). For every \(s>0\), take \(d=\sqrt{2s}>0\). The joint law implies
\[
 \int_0^\infty e^{-st}g(t)f_{0,a}(t)\,dt
 =\frac{d}{\sinh(ad)}=G_a(s).
\]
We use the standard injectivity statement for Laplace transforms: if two integrable functions on \((0,\infty)\) have equal transforms at every positive real argument, they are equal almost everywhere. Both functions here are integrable, and their transforms agree on that entire domain. Thus \(g f_{0,a}=q_a\) almost everywhere. Strict positivity of \(f_{0,a}\) and continuity of the weights give \(g=w_a\) everywhere. Notice that the zero-drift identity alone would not identify a weight; uniqueness uses all positive transform arguments.

## 4. Population expansion and bias orders

Now write \(r=\sqrt{2\lambda}\), and set
\[
 C_0=\mathbb E[\cosh(aD)],\qquad C_2=\mathbb E[D^2\cosh(aD)].
\]
Both are finite and \(C_0\ge1\). Uniformly over \(|d|\le M\),
\[
 \sqrt{r^2+d^2}=r+\frac{d^2}{2r}+O(r^{-3}),
 \quad
 e^{-a(\sqrt{r^2+d^2}-r)}=1-\frac{ad^2}{2r}+O(r^{-2}).
\]
Also \(1/\cosh x=2e^{-x}(1+O(e^{-2x}))\) for \(x\ge0\). Substitution into the fixed-drift transform and averaging give
\[
 L_a(\lambda)=2e^{-ar}\left(C_0-\frac{aC_2}{2r}+O(r^{-2})\right),
\]
and hence
\[
 \log L_a(\lambda)=-ar+\log(2C_0)-\frac{aC_2}{2C_0r}+O(r^{-2}). \tag{6}
\]
The remainders are valid for the fixed model, and can be bounded using only \(a\) and \(M\).

Therefore
\[
 -\frac{\log L_a(\lambda)}r-a
 =-\frac{\log(2C_0)}r+O(r^{-2}).
\]
Because \(\log(2C_0)\ge\log2>0\), its absolute value is at least \(\log(2C_0)/(2r)\) for all sufficiently large \(r\). This proves the required one-scale \(\Omega(\lambda^{-1/2})\) bias, as well as its convergence to zero.

Apply (6) at \(\lambda\) and \(4\lambda\), corresponding to \(r\) and \(2r\). The constant term cancels:
\[
 \frac{\log L_a(\lambda)-\log L_a(4\lambda)}r
 =a-\frac{aC_2}{4C_0r^2}+O(r^{-3})
 =a-\frac{aC_2}{8C_0\lambda}+O(\lambda^{-3/2}). \tag{7}
\]
This proves the two-scale upper bias bound. No assumption \(C_2>0\) is needed: when \(D=0\) almost surely, \(C_2=0\), while the one-scale leading coefficient remains \(\log2\).

## 5. Empirical transforms and boundary consistency

For fixed \(c\in\{1,4\}\), set \(X_{n,i}=e^{-c\lambda_n S_i}\). Independence within each row and boundedness give
\[
 \mathbb E\left[\left(\frac{\ell_n(c\lambda_n)}{L_a(c\lambda_n)}-1\right)^2\right]
 =\frac{\operatorname{Var}(X_{n,1})}{nL_a(c\lambda_n)^2}
 \le\frac{L_a(2c\lambda_n)}{nL_a(c\lambda_n)^2}.
\]
The expansion already proved gives
\[
 \frac{L_a(2c\lambda_n)}{nL_a(c\lambda_n)^2}
 =O\left(n^{-1}\exp\{2a(\sqrt2-1)\sqrt{c\lambda_n}\}\right)\longrightarrow0.
\]
Thus Chebyshev's inequality proves relative consistency at both scales. In particular,
\[
 \log\ell_n(c\lambda_n)-\log L_a(c\lambda_n)=o_p(1),\qquad c=1,4,
\]
by continuity of the logarithm at one. Joint control of the two scales follows by a union bound; it does not require independence between them.

The selected source variance-scale lemma is also valid under these same assumptions. At scale \(\lambda\), its conditional variance bound is, uniformly in \(|d|\le M\),
\[
 \operatorname{Var}(e^{-\lambda S}\mid D=d)
 \ge e^{-a\sqrt{M^2+4\lambda}}-4e^{2aM-2a\sqrt{2\lambda}}
 \ge\zeta e^{-2a\sqrt\lambda}
\]
for large \(\lambda\), with \(\zeta>0\). Total variance and the tuning condition give \(n\operatorname{Var}(e^{-\lambda_n S})\to\infty\). A triangular-array CLT is therefore available as in the source, but is unnecessary for the direct relative-variance proof above.

Combining the empirical logarithmic errors with (6)-(7), and dividing by \(\sqrt{2\lambda_n}\to\infty\), proves
\[
 \widehat a_n^{(1)}\xrightarrow{p}a,
 \qquad \widetilde a_n\xrightarrow{p}a.
\]
These are consistency statements, not claims about finite-sample expectations of the boundary estimators.

## 6. Same-sample plug-in consistency

Choose a compact interval \(K\subset(0,\infty)\) containing \(a\) in its interior. Define
\[
 A_n(\beta)=\frac1n\sum_{i=1}^nY_iw_\beta(S_i),
 \qquad A(\beta)=\mathbb E[Yw_\beta(S)].
\]
The continuity and integrable envelope established in Section 2 imply continuity of \(A\) by dominated convergence.

For completeness, a compact-uniform law follows directly. Put
\[
 \omega_\delta(t)=\sup_{\substack{\beta,\gamma\in K\\|\beta-\gamma|\le\delta}}
 |w_\beta(t)-w_\gamma(t)|.
\]
These functions are measurable, by continuity and separability of the compact parameter sets; their suprema can be represented using countable dense subsets. Uniform continuity on \(K\) for each fixed \(t\) gives \(\omega_\delta(t)\to0\), while \(\omega_\delta(t)\le2H_K(t)\). Thus \(\mathbb E\omega_\delta(S)\to0\).

Choose a finite \(\delta\)-net \(\gamma_1,\ldots,\gamma_J\) of \(K\). Then
\[
 \sup_{\beta\in K}|A_n(\beta)-A(\beta)|
 \le\max_j|A_n(\gamma_j)-A(\gamma_j)|
 +\frac1n\sum_{i=1}^n\omega_\delta(S_i)
 +\mathbb E\omega_\delta(S).
\]
For each fixed \(\delta\), all sample averages on the right satisfy the weak law because their summands are i.i.d. and integrable. Letting \(n\to\infty\) and then \(\delta\downarrow0\) proves
\[
 \sup_{\beta\in K}|A_n(\beta)-A(\beta)|\xrightarrow{p}0. \tag{8}
\]

Boundary consistency gives \(\mathbb P(\widetilde a_n\in K)\to1\). On that event,
\[
 |A_n(\widetilde a_n)-A_n(a)|
 \le2\sup_{\beta\in K}|A_n(\beta)-A(\beta)|
 +|A(\widetilde a_n)-A(a)|.
\]
The right side tends to zero in probability by (8), continuity, and boundary consistency. Finally, absolute integrability and unbiasedness give \(A_n(a)\to_p A(a)=\mu\) by the weak law. Therefore
\[
 \widehat\mu_n^{\rm PI}=A_n(\widetilde a_n)\xrightarrow{p}\mu.
\]
This argument explicitly permits the boundary estimator and the weighted average to use the same observations.
