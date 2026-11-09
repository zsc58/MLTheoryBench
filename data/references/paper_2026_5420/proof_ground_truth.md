# Reference Proof

## Proof Structure

1. Establish a simultaneous PAC-Bayes-Chernoff inequality for the weighted multi-task generalisation gap by factoring exponential moments, deriving the survival-function estimate, and applying change of measure.
2. Insert the assumed CGF estimates and optimize to obtain a population input-gradient bound.
3. Repeat the argument for weighted squared input-gradient losses, deriving their bounded-variable CGF estimate and the empirical-to-population correction.
4. Intersect the two events and substitute, including the zero-energy and extended-integral cases.

## Complete Proof

Fix the prior and a confidence level \(\delta\in(0,1)\). If a prior is obtained using randomness independent of the samples, the same argument applies conditionally on that prior. No event uniform over different priors is asserted.

### 1. Fixed-parameter multi-task Chernoff bound

Write
\[
Z_i(\theta,x)=R_i(\theta)-\ell_i(\theta,x),\qquad
g_\theta(S)=\frac1M\sum_i\sum_{j=1}^{m_i}Z_i(\theta,X_{i,j}),
\]
and
\[
\overline\Lambda_\theta(\lambda)=\frac1M\sum_i m_i\Lambda_i(\theta,\lambda).
\]
For each fixed \(\theta\), the variables in this sum are independent. Thus, for every \(\lambda>0\),
\[
\mathbb E_S e^{M\lambda g_\theta(S)}
=\prod_i\prod_{j=1}^{m_i}\mathbb E_{D_i}e^{\lambda Z_i(\theta,X)}
=e^{M\overline\Lambda_\theta(\lambda)}.
\]
Markov's inequality gives, for every real \(a\),
\[
\Pr\{g_\theta(S)\ge a\}
\le e^{-M(\lambda a-\overline\Lambda_\theta(\lambda))}.
\]
The centered CGFs are nonnegative by Jensen's inequality. The public hypotheses also give
\[
0\le\overline\Lambda_\theta(\lambda)
\le\frac{\lambda^2}{2M}\sum_i m_iC_iL_i.
\]
In particular, these CGFs are finite for every positive \(\lambda\), continuous there, and tend to zero as \(\lambda\downarrow0\). Define the one-sided transform
\[
H_\theta(a)=\sup_{\lambda>0}\{\lambda a-\overline\Lambda_\theta(\lambda)\}.
\]
It is nonnegative and nondecreasing in \(a\), and equals zero for \(a\le0\). The supremum can be taken over positive rationals, so its composition with the jointly measurable gap is measurable. Optimizing the preceding Markov bound yields
\[
\Pr\{g_\theta(S)\ge a\}\le e^{-M H_\theta(a)}.
\]
No independence of transformed observations under a data-dependent posterior has been used: independence is used only at fixed \(\theta\).

### 2. Survival estimate and change of measure

Here is a derivation of the specialized exponential-moment estimate, rather than an appeal to an external PAC-Bayes-Chernoff result. For \(t\ge0\), the set
\[
A_t=\{a:H_\theta(a)>t\}
\]
is an upper ray, possibly empty. If its lower endpoint belongs to it, apply the preceding tail bound at that endpoint. Otherwise take a decreasing sequence of points in \(A_t\) approaching its lower endpoint. The events \(\{g_\theta\ge a\}\) along this sequence increase to \(\{H_\theta(g_\theta)>t\}\). In either case, using continuity of probability for increasing events,
\[
\Pr\{H_\theta(g_\theta)>t\}\le e^{-Mt}.
\]
This argument includes atoms and degenerate gaps and requires no strictly increasing inverse.

For \(0<q<M\), Tonelli's theorem now gives
\[
\begin{aligned}
\mathbb E_S e^{qH_\theta(g_\theta)}
&=1+q\int_0^\infty e^{qt}\Pr\{H_\theta(g_\theta)>t\}\,dt\\
&\le1+q\int_0^\infty e^{-(M-q)t}\,dt
=\frac{M}{M-q}.
\end{aligned}
\]
Equivalently, the survival formula for \(W=e^{qH_\theta(g_\theta)}\ge1\) is \(\mathbb EW=1+\int_1^\infty\Pr(W>u)\,du\). The initial 1 must not be omitted.

For any \(\varepsilon\in(0,1)\), integrate over the sample-independent prior and apply Markov's inequality. With probability at least \(1-\varepsilon\),
\[
\mathbb E_\pi e^{qH_\theta(g_\theta(S))}
\le\frac{M}{(M-q)\varepsilon}.
\tag{1}
\]
This is a measurable event depending only on the prior average, not on a chosen posterior.

We use the variational inequality in its following precise form: for a nonnegative measurable \(h\) with \(\mathbb E_\pi e^h<\infty\), and any \(\rho\ll\pi\) with finite KL,
\[
\mathbb E_\rho h\le\mathrm{KL}(\rho\|\pi)+\log\mathbb E_\pi e^h.
\]
For completeness, apply nonnegativity of relative entropy to the probability measure with density \(e^{h_n}/\mathbb E_\pi e^{h_n}\) relative to \(\pi\), where \(h_n=\min(h,n)\). This gives the displayed inequality for \(h_n\); monotone convergence gives it for \(h\). Nonnegativity of relative entropy follows from convexity of \(u\log u\). Thus all hypotheses of the variational inequality are verified on (1).

Consequently, on the same event, simultaneously for every finite-KL posterior,
\[
\mathbb E_\rho H_\theta(g_\theta(S))
\le\frac{\mathrm{KL}(\rho\|\pi)+\log\{M/((M-q)\varepsilon)\}}q.
\tag{2}
\]

### 3. Shared parameter and posterior expectation

The transform depends on \(\theta\), so a Jensen argument using one fixed transform is not appropriate. Instead, directly use its defining inequality: for every \(\lambda>0\),
\[
\lambda g_\theta(S)-\overline\Lambda_\theta(\lambda)
\le H_\theta(g_\theta(S)).
\tag{3}
\]
The uniform bound on \(\overline\Lambda_\theta(1)\), together with (2) and (3), shows that \(\mathbb E_\rho(g_\theta(S))_+<\infty\) for every finite-KL posterior on this event. Hence its posterior gap is defined and belongs to \([-\infty,\infty)\). If that gap is \(-\infty\), the desired upper bound is immediate. Otherwise it is finite, and integrating (3) is justified. Setting \(q=M-1\) gives
\[
\operatorname{gen}(\rho,S)
\le\frac{\mathrm{KL}(\rho\|\pi)+\log(M/\varepsilon)}{\lambda(M-1)}
+\frac1{M\lambda}\sum_i m_i\mathbb E_\rho\Lambda_i(\theta,\lambda).
\]
This holds for every positive \(\lambda\) on the same event; thus its infimum over \(\lambda>0\) is also a valid bound. There is no union bound over tuning parameters or posteriors. This argument will also apply to the bounded transformed losses below, whose finite CGFs and measurability will be explicitly checked.

### 4. Population-gradient bound

Apply the preceding result with \(\varepsilon=\delta/2\). Let
\[
A=\mathrm{KL}(\rho\|\pi)+\log(2M/\delta),\qquad
K=\frac{MA}{M-1},
\]
and introduce the private intermediate quantity
\[
G(\rho)=\sum_i m_iC_i\mathbb E_\rho\mathbb E_{D_i}
\|\nabla_x\ell_i(\theta,X)\|_2^2.
\]
It satisfies \(0\le G(\rho)\le\sum_i m_iC_iL_i<\infty\). The assumed CGF bound yields, simultaneously for finite-KL posteriors on an event of probability at least \(1-\delta/2\),
\[
\operatorname{gen}(\rho,S)
\le\inf_{\lambda>0}\left\{\frac{A}{\lambda(M-1)}+\frac{\lambda G(\rho)}{2M}\right\}
=\frac1M\sqrt{2KG(\rho)}.
\tag{4}
\]
For \(G(\rho)>0\), the equality follows by minimizing the two positive terms. For \(G(\rho)=0\), let \(\lambda\to\infty\), so the infimum is zero without dividing by \(G(\rho)\).

The generic oracle confidence parameter is \(\varepsilon\), with logarithm \(\log(M/\varepsilon)\). It is specialized to \(\delta/2\) exactly once. This yields \(\log(2M/\delta)\), not \(\log(4M/\delta)\).

### 5. Empirical control of the gradient energy

Put
\[
Y_i(\theta,x)=\|\nabla_x\ell_i(\theta,x)\|_2^2,
\qquad U_i(\theta,x)=C_iY_i(\theta,x),
\qquad V=\sum_i m_iC_i^2L_i^2.
\]
These are jointly measurable losses, and \(0\le U_i\le b_i:=C_iL_i\). Their fixed-parameter transformed samples retain the required independence.

The bounded-variable CGF estimate can be derived directly. If \(0\le U\le b\), set \(F(t)=\log\mathbb E e^{t(\mathbb EU-U)}\). Boundedness permits differentiation. Its second derivative is the variance of \(U\) under the exponentially tilted probability distribution. That variance is at most \(b^2/4\), since \(\operatorname{Var}(U)\le\mathbb E(U-b/2)^2\le b^2/4\) under every distribution supported on \([0,b]\). As \(F(0)=F'(0)=0\), integration twice gives
\[
\log\mathbb E e^{t(\mathbb EU-U)}\le\frac{t^2b^2}{8}
\qquad(t>0).
\]
Therefore the centered CGFs of \(U_i\) obey
\[
\Lambda_i^U(\theta,\lambda)
\le\frac{\lambda^2C_i^2L_i^2}{8}.
\]
They are finite and continuous and satisfy all requirements used in steps 1-3. Applying that argument to \(U_i\), with confidence \(\delta/2\), produces a second event of probability at least \(1-\delta/2\), on which all finite-KL posteriors satisfy
\[
\begin{aligned}
G(\rho)-\widehat G(\rho,S)
&\le\inf_{\lambda>0}\left\{\frac{K}{\lambda}+\frac{\lambda V}{8}\right\}\\
&=\sqrt{\frac{VK}{2}}.
\end{aligned}
\tag{5}
\]
Indeed, the sample-weighted gap for \(U_i\) is exactly \((G-\widehat G)/M\); multiplying its bound by \(M\) yields the first line. The infimum is attained at \(\lambda=\sqrt{8K/V}\). Here \(V>0\) because the sample sizes and the stated constants are positive. Since \(L=\sqrt{2V}\), the correction in (5) equals \(L\sqrt K/2\).

### 6. Combination and posterior domain

The intersection of the two events has probability at least \(1-\delta\); independence between these events is unnecessary. On it, (4)-(5) give, for every finite-KL posterior with finite gap,
\[
\begin{aligned}
\operatorname{gen}(\rho,S)
&\le\frac1M\sqrt{2K\left(\widehat G(\rho,S)+\tfrac12L\sqrt K\right)}\\
&=\frac1M\sqrt{2\widehat G(\rho,S)K+LK^{3/2}}.
\end{aligned}
\]
Finite-KL posteriors with gap \(-\infty\) satisfy the same inequality immediately. Step 3 ensures that every finite-KL posterior has a defined gap on this event. Finally, an infinite-KL posterior whose signed gap is defined satisfies the asserted extended-real inequality because the right-hand side is defined to be \(+\infty\). The result is therefore simultaneous for exactly the posterior domain in the public statement.

All obligations are closed: the specialized survival estimate is derived rather than imported; the variational inequality and bounded-variable CGF estimate are justified; the shared-parameter passage, confidence allocation, normalization, zero-energy case, and extended-integral cases are explicit.
