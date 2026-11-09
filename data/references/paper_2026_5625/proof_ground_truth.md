# Reference Proof

## Proof Structure and Obligations

For Gaussian posteriors centered at each parameter, decompose the deterministic generalization gap into a Gibbs generalization gap and a population-minus-empirical Jensen-gap process. Control the Gibbs gap on one sample event. Control the Jensen-gap process by the Jacobian/Hessian quadratic metric, comparison with an ellipsoidal Gaussian process, and uniform empirical Rademacher generalization on a second event.

The theorem-critical obligations are: the centered-loss exponential-moment estimate and finite-risk domain; a simultaneous PAC-Bayes inequality; the exact Jensen-gap decomposition; the directional-derivative and quadratic-metric bounds; the process comparison and trace calculation; the envelope-based uniform concentration estimate; and the final confidence allocation. All are closed below. The nonstandard external dependency theory_001 is derived rather than treated as closed by citation. The standard-independent comparison result theory_025 is stated explicitly and its hypotheses are verified. The application recorded as theory_034 is also reconstructed with explicit constants.

## 1. Centering, Exponential Moments, and Integrability

Put \(b_0=L(0,y)\), which is independent of \(y\), and write \(\widetilde L(z,y)=L(z,y)-b_0\). Then
\[
|\widetilde L(h_v(x),y)|\le\ell a_v.
\]
Consequently every individual deterministic population risk is finite. Centering changes neither an individual generalization gap nor a Jensen gap.

We use the elementary bounded-variable exponential estimate
\[
\mathbb E e^{t(Z-\mathbb EZ)}\le e^{t^2(b-a)^2/8}\quad\text{if }Z\in[a,b].
\]
For completeness, the logarithm of the left-hand side has value and first derivative zero at zero. Its second derivative is the variance of \(Z\) under exponential tilting. This variance is at most \((b-a)^2/4\), since the squared distance to the midpoint of \([a,b]\) is at most that quantity. Integrating the second-derivative bound proves the estimate for every real \(t\).

Applying this estimate independently to the \(n\) centered losses gives, for each fixed \(v\),
\[
\mathbb E_S\exp\{\lambda(L_D(h_v)-L_S(h_v))\}
\le\exp\!\left(\frac{\lambda^2\ell^2a_v^2}{2n}\right).
\]
Set
\[
K=\mathbb E_{v\sim P}\exp\!\left(\frac{\lambda^2\ell^2a_v^2}{2n}\right)\in[1,\infty].
\]
Thus the source exponential-moment quantity satisfies \(\Psi(\lambda,n)\le\log K\).

If \(K=\infty\), the requested result is pointwise vacuous. Likewise, for any center with \(\mathrm{KL}(Q_w\|P)=\infty\), its requested bound is vacuous. If \(\ell=0\), then \(L(z,y)=b_0\) for every \(z,y\), so all deterministic generalization gaps are zero and the conclusion follows from nonnegativity of the displayed penalties. We henceforth treat \(\ell>0\), \(K<\infty\), and centers of finite KL.

Here is the entropy inequality needed both for integrability and for PAC-Bayes. If \(Q\ll P\), \(r=dQ/dP\), \(\mathrm{KL}(Q\|P)<\infty\), and \(\phi\) is bounded, Jensen's inequality gives
\[
\mathbb E_Q\phi-\mathrm{KL}(Q\|P)
=\mathbb E_Q\log(e^\phi/r)
\le\log\mathbb E_Q(e^\phi/r)
\le\log\mathbb E_Pe^\phi.
\]
Let \(t_0=\lambda^2\ell^2/(2n)>0\) and apply this to \(\phi=t_0\min(a_v^2,N)\). Monotone convergence yields
\[
t_0\mathbb E_Qa_v^2\le\mathrm{KL}(Q\|P)+\log K<\infty.
\]
Therefore \(\mathbb E_Qa_v<\infty\). In particular,
\[
\mathbb E_{v\sim Q}\mathbb E_{(x,y)\sim D}|L(h_v(x),y)|
\le |b_0|+\ell\mathbb E_Qa_v<\infty,
\]
and the analogous empirical absolute integral is finite. These conclusions justify the Gibbs risks and all exchanges of posterior and data expectations in the nonvacuous part of the proof. No additional posterior moment assumption is imposed on the public task.

## 2. Simultaneous Gibbs Bound and Exact Decomposition

Define the sample-measurable nonnegative random variable
\[
W(S)=\mathbb E_{v\sim P}\exp\{\lambda(L_D(h_v)-L_S(h_v))\}.
\]
Tonelli's theorem and the preceding estimate give \(\mathbb E_SW(S)\le K\). Markov's inequality therefore gives an event \(E_1\) of probability at least \(1-\delta/2\) on which
\[
W(S)\le 2K/\delta.
\]
On this single event, apply the entropy inequality with \(\phi(v)=\lambda(L_D(h_v)-L_S(h_v))\). The extension from bounded \(\phi\) follows by two-sided truncation: \(\phi\) is absolutely integrable under each finite-KL posterior by Section 1, while \(e^{\max(-N,\min(\phi,N))}\le1+e^\phi\), which is integrable under \(P\) on \(E_1\). It follows simultaneously for every such posterior that
\[
\mathbb E_Q L_D(h_v)-\mathbb E_Q L_S(h_v)
\le\frac{\mathrm{KL}(Q\|P)+\log(2K/\delta)}{\lambda}.
\]
Uniformity in \(Q\) requires no union bound: the event bounds the same prior integral before any posterior is chosen. In particular it allows a sample-dependent center \(w\).

Privately define
\[
F(w;x,y)=L(h_w(x),y)-\mathbb E_{v\sim Q_w}L(h_v(x),y),
\qquad F_i(w)=F(w;x_i,y_i),
\]
and
\[
\Omega_w=\mathbb E_DF(w;x,y)-\frac1n\sum_{i=1}^nF_i(w).
\]
The integrability proved above and Fubini's theorem give the exact identity
\[
L_D(h_w)-L_S(h_w)
=\mathbb E_{v\sim Q_w}[L_D(h_v)-L_S(h_v)]+\Omega_w.
\]
Thus, on \(E_1\), every nonvacuous center satisfies
\[
L_D(h_w)\le L_S(h_w)+\Omega_w
+\frac{\mathrm{KL}(Q_w\|P)+\log(2K/\delta)}{\lambda}.
\]

## 3. Directional Derivatives and the Quadratic Metric

Fix a sample satisfying the samplewise assumptions. Write \(z_i(w)=h_w(x_i)\) and \(g_i(w)=\nabla_zL(z_i(w),y_i)\). Differentiability and Lipschitzness imply \(\|g_i(w)\|_2\le\ell\). Differentiating under the Gaussian integral and adding and subtracting \(J_i(w)^T\mathbb E_ug_i(w+\sigma u)\) gives
\[
\nabla F_i(w)
=J_i(w)^T\big(g_i(w)-\mathbb E_ug_i(w+\sigma u)\big)
+\mathbb E_u\big[(J_i(w)-J_i(w+\sigma u))^Tg_i(w+\sigma u)\big].
\]
For \(v\in\mathbb R^m\), call the two directional contributions \(T_{1,i}(w,v)\) and \(T_{2,i}(w,v)\), respectively.

The fundamental theorem of calculus for the score map gives
\[
z_i(w+\sigma u)-z_i(w)=\sigma\int_0^1J_i(w+t\sigma u)u\,dt.
\]
Jensen's inequality and the exact definition of \(A_{i,\sigma}\) imply
\[
\mathbb E_u\|z_i(w+\sigma u)-z_i(w)\|_2^2\le\sigma^2A_{i,\sigma}.
\]
Consequently smoothness of the loss and the unperturbed Jacobian bound yield
\[
|T_{1,i}(w,v)|
\le\beta\|J_i(w)v\|_2\,\mathbb E_u\|z_i(w+\sigma u)-z_i(w)\|_2
\le\beta\sigma\sqrt{A_{i,\sigma}}\sqrt{v^TG_iv}.
\]

For the second contribution,
\[
|T_{2,i}(w,v)|
\le\ell\sqrt{\mathbb E_u\|(J_i(w+\sigma u)-J_i(w))v\|_2^2}.
\]
The \(k\)-th coordinate of the Jacobian difference applied to \(v\) is
\[
\big((J_i(w+\sigma u)-J_i(w))v\big)_k
=\sigma\int_0^1u^TH_{i,k}(w+t\sigma u)v\,dt.
\]
Applying Jensen, summing over \(k\), and taking the Gaussian expectation gives
\[
\mathbb E_u\|(J_i(w+\sigma u)-J_i(w))v\|_2^2
\le\sigma^2v^TB_{i,\sigma}(w)v
\le\sigma^2v^TB_{i,\sigma}v.
\]
Therefore
\[
|\langle\nabla F_i(w),v\rangle|^2
\le2T_{1,i}(w,v)^2+2T_{2,i}(w,v)^2
\le2\sigma^2v^T(\beta^2A_{i,\sigma}G_i+\ell^2B_{i,\sigma})v.
\]
The Gaussian paths in these estimates range over all of \(\mathbb R^m\). Only the centers and the segment between two centers must lie in \(\Theta\); no bounded-support replacement of the Gaussian is made.

For \(w_1,w_2\in\Theta\), apply the directional bound along their segment, which is contained in \(\Theta\). Equivalently, apply the one-dimensional mean value theorem to the restriction of \(F_i\) to that segment. With \(v=w_1-w_2\), this gives
\[
(F_i(w_1)-F_i(w_2))^2
\le2\sigma^2v^T(\beta^2A_{i,\sigma}G_i+\ell^2B_{i,\sigma})v.
\]
Thus the privately defined pseudometric
\[
d_S(w_1,w_2)^2=\sum_{i=1}^n(F_i(w_1)-F_i(w_2))^2
\]
satisfies
\[
d_S(w_1,w_2)^2\le(w_1-w_2)^TM_{S,\sigma}(w_1-w_2),
\qquad
M_{S,\sigma}=2\sigma^2\sum_{i=1}^n(\beta^2A_{i,\sigma}G_i+\ell^2B_{i,\sigma}).
\]
This matrix is finite and positive semidefinite.

## 4. Process Comparison and the Trace Bound

Let \(\mathcal F_\sigma=\{F(w;\cdot):w\in\Theta\}\), and use the normalization
\[
\widehat{\mathfrak R}_S(\mathcal F_\sigma)
=\frac1n\mathbb E_\varepsilon\sup_{w\in\Theta}\sum_{i=1}^n\varepsilon_iF_i(w),
\]
where the signs are independent and symmetric. There is no absolute value inside this supremum.

Conditional on the sample, put \(X_w=\sum_i\varepsilon_iF_i(w)\). For an increment \(Z=X_{w_1}-X_{w_2}\), independence gives
\[
\mathbb E_\varepsilon e^{tZ}
=\prod_i\cosh\big(t(F_i(w_1)-F_i(w_2))\big)
\le e^{t^2d_S(w_1,w_2)^2/2}.
\]
If \(d=d_S(w_1,w_2)>0\), Chernoff's inequality yields \(\mathbb P(|Z|>r)\le2e^{-r^2/(2d^2)}\). Hence
\[
\mathbb E e^{Z^2/(6d^2)}
\le1+\int_1^\infty2t^{-3}\,dt=2.
\]
With \(\|Z\|_{\psi_2}=\inf\{s>0:\mathbb E e^{Z^2/s^2}\le2\}\), this proves \(\|Z\|_{\psi_2}\le\sqrt6\,d\). If \(d=0\), the increment is identically zero.

The standard-independent comparison theorem used here is: for separable centered processes \((U_t)\) and \((V_t)\), with \(V\) Gaussian, if \(\|U_t-U_s\|_{\psi_2}\le K_0\|V_t-V_s\|_{L_2}\) for every pair, then
\[
\mathbb E\sup_tU_t\le C_{\rm cmp}K_0\,\mathbb E\sup_tV_t
\]
for a universal numerical constant \(C_{\rm cmp}>0\). This is the standard-independent result recorded as theory_025.

Take \(g\sim\mathcal N(0,I_m)\) and \(Y_w=\langle g,M_{S,\sigma}^{1/2}w\rangle\). Both processes are centered, and
\[
\|Y_{w_1}-Y_{w_2}\|_{L_2}^2
=(w_1-w_2)^TM_{S,\sigma}(w_1-w_2).
\]
The required increment comparison holds with \(K_0=\sqrt6\). Continuity of the finitely many \(F_i\) on the compact parameter ball gives separability and finite measurable suprema. One may also replace \(X_w\) by \(X_w-X_0\): this anchors the process at zero without changing its expected supremum.

The comparison theorem and Cauchy--Schwarz give
\[
\widehat{\mathfrak R}_S(\mathcal F_\sigma)
\le\frac{C_{\rm cmp}\sqrt6}{n}\mathbb E_g\sup_{\|w\|_2\le R}\langle M_{S,\sigma}^{1/2}g,w\rangle
=\frac{C_{\rm cmp}\sqrt6 R}{n}\mathbb E_g\|M_{S,\sigma}^{1/2}g\|_2
\le\frac{C_{\rm cmp}\sqrt6 R}{n}\sqrt{\operatorname{tr}M_{S,\sigma}}.
\]
Since
\[
\operatorname{tr}M_{S,\sigma}
=2\sigma^2n(\beta^2J_{S,\sigma}+\ell^2H_{S,\sigma}),
\]
choosing the universal constant \(c=\sqrt{12}\,C_{\rm cmp}\) proves
\[
\widehat{\mathfrak R}_S(\mathcal F_\sigma)
\le\frac{cR\sigma}{\sqrt n}\sqrt{\beta^2J_{S,\sigma}+\ell^2H_{S,\sigma}}.
\]
No inverse of \(M_{S,\sigma}\) is used. Singular matrices and \(R=0\) are therefore included. If the metric vanishes, the process is constant in its index and its expected supremum is zero.

## 5. Uniform Jensen-Gap Generalization

Set \(b=\sigma^2B\). The class \(\mathcal F_\sigma\) is fixed independently of the sample and satisfies \(|F(w;x,y)|\le b\). Its members are measurable. The differentiation hypotheses give continuity in \(w\) for almost every data point; the uniform envelope then gives continuity of the population means by dominated convergence. A fixed countable dense subset of \(\Theta\) thus determines the suprema below up to a null set, establishing the measurability needed for concentration and symmetrization.

Here is an explicit reconstruction of the bounded-class estimate. For any fixed measurable separable class \(\mathcal F\subset[-b,b]\), let
\[
\Phi(S)=\sup_{f\in\mathcal F}\left(\mathbb E_Df-\frac1n\sum_if(z_i)\right).
\]
An independent ghost sample, Jensen's inequality, random swapping of each original/ghost pair, and subadditivity of the supremum give
\[
\mathbb E_S\Phi(S)
\le\mathbb E_{S,S'}\sup_f\frac1n\sum_i(f(z'_i)-f(z_i))
\le2\mathbb E_S\widehat{\mathfrak R}_S(\mathcal F).
\]
Changing one observation changes each of \(\Phi(S)\) and \(\widehat{\mathfrak R}_S(\mathcal F)\) by at most \(2b/n\).

The bounded-differences inequality used at this point follows from the bounded-variable exponential estimate in Section 1. For a function of independent observations whose coordinate oscillations are at most \(c_i\), its Doob martingale differences have conditional range lengths at most \(c_i\). Conditional application of that estimate and iteration yield an exponential bound \(\exp(t^2\sum_i c_i^2/8)\). Chernoff optimization gives upper and lower tails bounded by \(\exp(-2r^2/\sum_i c_i^2)\).

Apply these tails to \(\Phi\) and to the lower deviation of \(\widehat{\mathfrak R}_S\), each with failure probability \(\eta/2\). With probability at least \(1-\eta\),
\[
\Phi(S)
\le2\widehat{\mathfrak R}_S(\mathcal F)+3b\sqrt{\frac{2\log(2/\eta)}n}
\le2\widehat{\mathfrak R}_S(\mathcal F)+8b\sqrt{\frac{2\log(4/\eta)}n}.
\]
This proves, with an explicit conservative constant, the precise application recorded as theory_034. If \(b=0\), its assertion is immediate without any division by a coordinate oscillation.

Apply the estimate to \(\mathcal F_\sigma\) with \(\eta=\delta/2\), and substitute Section 4. This gives an event \(E_2\) of probability at least \(1-\delta/2\) on which, simultaneously for all \(w\in\Theta\),
\[
\Omega_w
\le\frac{2cR\sigma}{\sqrt n}\sqrt{\beta^2J_{S,\sigma}+\ell^2H_{S,\sigma}}
+8\sigma^2B\sqrt{\frac{2\log(8/\delta)}n}.
\]
The sample-dependent matrices only upper-bound the empirical complexity after the class has been fixed; they do not make the function class sample-dependent.

## 6. Combination and Boundary Cases

The event \(E_1\cap E_2\), intersected with the probability-one samplewise-assumption event, has probability at least \(1-\delta\). For every center of finite KL, substitute the bound on \(\Omega_w\) into Section 2 and expand \(K\). This gives exactly
\[
L_D(h_w)\le L_S(h_w)
+\frac{2cR\sigma}{\sqrt n}\sqrt{\beta^2J_{S,\sigma}+\ell^2H_{S,\sigma}}
+8\sigma^2B\sqrt{\frac{2\log(8/\delta)}n}
+\frac{\mathrm{KL}(Q_w\|P)+\log\!\left(\frac2\delta\mathbb E_{v\sim P}e^{\lambda^2\ell^2a_v^2/(2n)}\right)}{\lambda}.
\]
Centers of infinite KL satisfy the extended-real bound automatically. Infinite prior moment and zero Lipschitz constant were handled in Section 1. The proof permits \(n=1\), \(R=0\), \(\beta=0\), singular metric matrices, and \(\delta=1\); the internal confidence parameters are still strictly between zero and one. The scale \(\sigma\) is positive and fixed, as in the source. The constant \(c\) is chosen universally, not supplied arbitrarily and not optimized after observing the sample.

All theorem-critical obligations are closed; no private ground-truth quality warning remains.
