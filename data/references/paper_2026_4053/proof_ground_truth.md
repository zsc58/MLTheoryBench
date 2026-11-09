# Reference Proof

## Contract and obligations

Write \(L=\log(1/\delta)\). All constants below are universal. The learner may use an independent random seed; queries depend only on that seed and preceding observations. Outputs need not belong to the target class. The upper bound must hold for every independent centered noise sequence satisfying the public tail bound. For both lower bounds we use independent \(N(0,\sigma^2)\) noise, which is admissible.

The obligations are: (1) signed-test counting and concentration, including random-design second moments; (2) thresholding and conversion to uniform loss; (3) structured-family separation and adaptive support-search risk, including small dimensions; (4) correctly normalized Gaussian posterior uncertainty, bounded-prior conditioning, and strict high-confidence risk; and (5) assembly with integer budgets and universal constants. All are established below.

## Probability tools and their applicable forms

We use the source's Bernstein inequality: if independent centered variables have magnitude at most \(B\) and total variance at most \(v\), then their sum has tail at most \(2\exp[-c\min(r^2/v,r/B)]\) at threshold \(r>0\). We verify these hypotheses at each application.

The tail-based noise convention entails a universal-constant weighted-sum bound, not necessarily the exact numerical constant printed in the source. Here is a derivation. If \(\xi'\) is an independent copy of a centered \(\xi\), Jensen's inequality gives
\[
\mathbb E e^{\lambda\xi}\leq\mathbb E e^{\lambda(\xi-\xi')}.
\]
The symmetric variable \(\zeta=\xi-\xi'\) satisfies \(\Pr(|\zeta|>u)\leq4e^{-u^2/(8\sigma^2)}\). Integrating its tail gives, for integers \(j\geq1\),
\[
\mathbb E\zeta^{2j}\leq4(8\sigma^2)^j j!.
\]
Symmetry, the power series for cosh, and \((2j)!\geq(j!)^2\) therefore give
\[
\mathbb E e^{\lambda\xi}
\leq1+4\big(e^{8\sigma^2\lambda^2}-1\big)
\leq e^{32\sigma^2\lambda^2}.
\]
Independence and exponential Markov inequality, optimizing the exponential parameter for each tail, yield
\[
\Pr\left(\left|\sum_t b_t\xi_t\right|>r\right)
\leq2\exp\left(-\frac{r^2}{128\sigma^2\sum_t b_t^2}\right).
\tag{1}
\]
When all weights vanish, the sum is zero. This argument works for nonidentically distributed noises as well.

For lower bounds, the source's adaptive Gaussian KL identity is
\[
D(P_f\Vert P_g)=\frac1{2\sigma^2}\sum_{t=1}^m
\mathbb E_f\big[(f(X_t)-g(X_t))^2\big]
\leq\frac{m\|f-g\|_\infty^2}{2\sigma^2}.
\tag{2}
\]
The observation can include the learner's entire random seed. Its distribution is identical under the two targets, and the query rule has the same conditional kernel under both targets. Thus the entropy chain rule leaves only Gaussian response divergences, proving (2) for randomized adaptive learners.

We also use the source's Fano inequality: for a uniform parameter on \(Q\geq2\) alternatives, every decoder has error at least
\[
1-\frac{Q^{-2}\sum_{i,j}D(P_i\Vert P_j)+\log2}{\log Q}.
\tag{3}
\]
All uses below involve explicitly given finite uniform priors and the transcript laws controlled by (2).

Finally, for \(Z\sim N(0,1)\), the source proves that there exists a universal \(b_0>0\) such that
\[
\Pr(|Z|>b_0\sqrt L)\geq2e^{-L},\qquad L\geq\log4.
\tag{4}
\]
Indeed, its Gaussian tail estimate gives \(\Pr(|Z|>u)\geq c u^{-1}e^{-u^2/2}\) for \(u\geq1\). For any fixed \(b<\sqrt2\), the ratio of this lower bound at \(b\sqrt L\) to \(e^{-L}\) tends to infinity. On the remaining compact interval of \(L\)'s, decrease \(b\) and use continuity of the Gaussian tail at zero. The condition \(2e^{-\log4}<1\) ensures the compact-interval step. Gaussian continuity allows either strict or non-strict tail notation.

## 1. Upper bound

Draw \(X_1,\ldots,X_m\) independently and uniformly, independently of the noises. Define
\[
\widetilde\theta_S=\frac1m\sum_{t=1}^mY_t\chi_S(X_t),\qquad e=\widetilde\theta-\theta.
\]
For a vector \(z\), define
\[
\|z\|_{(s),1}=\max_{|A|\leq s}\sum_{S\in A}|z_S|.
\]
Let
\[
G_s=\left\{\sum_{S\in A}\eta_S\chi_S: |A|\leq s,\ \eta_S\in\{-1,1\}\right\}.
\]
Then \(\|z\|_{(s),1}=\max_{g\in G_s}|\sum_Sg_Sz_S|\), where \(g_S\) denotes the Walsh coefficient of \(g\). With \(N=2^n\),
\[
|G_s|=\sum_{j=0}^s\binom Nj2^j\leq(s+1)(2N)^s,
\qquad \log|G_s|\leq Csn.
\tag{5}
\]
The last inequality uses \(1\leq s\leq n\).

For \(g\in G_s\) with \(j\leq s\) terms, orthogonality and boundedness give
\[
\|g\|_\infty\leq j\leq s,\qquad \mathbb E g(X)^2=j\leq s,
\qquad \mathbb E g(X)^4\leq\|g\|_\infty^2\mathbb E g(X)^2\leq s^3.
\tag{6}
\]
The signed coefficient error decomposes as
\[
\sum_Sg_Se_S=D_g+N_g,
\quad D_g=\frac1m\sum_t\big(f(X_t)g(X_t)-\mathbb E[f(X)g(X)]\big),
\quad N_g=\frac1m\sum_t\xi_tg(X_t).
\]
For \(D_g\), the independent centered summands have magnitude at most \(2s\) and variance at most \(\mathbb E f(X)^2g(X)^2\leq s\). Bernstein implies, for \(0<r\leq1\),
\[
\Pr(|D_g|>r)\leq2e^{-cmr^2/s}.
\]
Using (5), a union bound makes every \(|D_g|\leq\epsilon/8\) except with probability \(\delta/3\), provided
\[
m\geq C\epsilon^{-2}s(sn+L).
\tag{7}
\]
Here and below choose \(\epsilon_0\leq1\), and absorb additive logarithms of numerical constants using \(sn\geq1\) and \(L\geq\log4\).

For the empirical second moments, the independent centered variables
\(g(X_t)^2-\mathbb E g(X)^2\) have magnitude at most \(2s^2\) and variance at most \(s^3\). Bernstein at average deviation \(2s\), followed by (5), gives the event
\[
\frac1m\sum_tg(X_t)^2\leq3s\quad\text{for every }g\in G_s
\tag{8}
\]
with probability at least \(1-\delta/3\), if \(m\geq Cs(sn+L)\).

Conditional on any design satisfying (8), the noises remain independent with their original centered tail bounds. Applying (1) to the deterministic weights \(g(X_t)/m\) gives
\[
\Pr(|N_g|>r\mid X_1,\ldots,X_m)
\leq2e^{-cmr^2/(\sigma^2s)}.
\]
Consequently, another union bound makes every \(|N_g|\leq\epsilon/8\) with conditional failure probability at most \(\delta/3\), provided
\[
m\geq C\sigma^2\epsilon^{-2}s(sn+L).
\tag{9}
\]
Together, (7)--(9) imply \(\|e\|_{(s),1}\leq\epsilon/4\) with probability at least \(1-\delta\) when
\[
m\geq C(1+\sigma^2)\epsilon^{-2}s(sn+L).
\tag{10}
\]

Let \(H\) be exactly \(s\) indices of largest empirical magnitude, using a fixed tie-breaking order and allowing selected zero entries. Put \(\widehat\theta=\widetilde\theta\) on \(H\) and zero elsewhere, and write \(T=\operatorname{supp}(\theta)\). Since \(|T|\leq s=|H|\), one can inject \(T\setminus H\) into \(H\setminus T\); every matched selected magnitude is at least the omitted magnitude. Since \(\widetilde\theta=e\) on \(H\setminus T\),
\[
\sum_{S\in T\setminus H}|\theta_S|
\leq\sum_{S\in T\setminus H}|e_S|
 +\sum_{S\in H\setminus T}|e_S|.
\]
It follows that
\[
\|\widehat\theta-\theta\|_1
\leq\sum_{S\in H}|e_S|+\sum_{S\in T\setminus H}|e_S|
 +\sum_{S\in H\setminus T}|e_S|
\leq3\|e\|_{(s),1}\leq4\|e\|_{(s),1}.
\]
Because every Walsh character has magnitude one, the output \(\widehat f=\sum_S\widehat\theta_S\chi_S\) satisfies
\(\|\widehat f-f\|_\infty\leq\|\widehat\theta-\theta\|_1\leq\epsilon\) on the good event. All probability bounds are uniform over the prescribed target and noise classes. Taking the ceiling in (10) and enlarging \(C\) proves the upper bound; its right side is bounded below by a positive universal constant, so rounding is harmless.

## 2. Support-search lower bound

First suppose \(n\geq12\). Set \(k=\min(s,\lfloor n/2\rfloor)\) and \(q=n-k\). Then \(k\geq s/3\), \(q\geq n/2\), and \(q\geq6\). Write \(x=(u,v)\in\{-1,1\}^k\times\{-1,1\}^q\). The parameter is a tuple \(M=(S_1,\ldots,S_k)\) of arbitrary subsets of \([q]\), with repetitions permitted. Define
\[
a=4\epsilon/k,\qquad f_M(u,v)=a\sum_{j=1}^ku_j\chi_{S_j}(v).
\]
The full-cube characters are distinct because they contain different first-block coordinates. Thus each function is \(k\)-sparse and has norm at most \(ak=4\epsilon\leq1\).

For two tuples \(M,T\), let \(J=\{j:S_j\ne T_j\}\) and \(d_H(M,T)=|J|\). For uniform \(V\), each pair of differing characters disagrees with probability \(1/2\), because their product is a nonconstant character. Thus some \(v\) has at least \(|J|/2\) disagreements. Set \(u_j=\chi_{S_j}(v)\). At this point,
\[
f_M(u,v)-f_T(u,v)
=a\sum_j\big(1-\chi_{S_j}(v)\chi_{T_j}(v)\big)
\geq a|J|.
\tag{11}
\]
This proves the required separation.

Put the uniform product prior on the tuple coordinates. Project any learner's output to a nearest member of this finite family, using fixed tie-breaking, to obtain \(\widehat M\). Fix a coordinate \(j\) and condition on all the other hidden coordinates. The remaining coordinate is uniform on \(Q=2^q\) alternatives. Two such alternatives differ pointwise by at most \(2a\), so (2) bounds every conditional pairwise KL by
\[
2ma^2/\sigma^2=32m\epsilon^2/(\sigma^2k^2).
\]
If \(m\leq c\sigma^2ns^2/\epsilon^2\), then \(ns^2\leq18k^2q\). Choosing \(c\) sufficiently small makes the KL at most \((\log Q)/16\). Fano therefore gives
\[
\Pr(\widehat S_j\ne S_j\mid M_{-j})
\geq1-1/16-1/q\geq3/4.
\]
This use of conditioning is only an analysis of the experiment; the actual learner receives no hidden coordinates. The decoder used by the learner is one of the decoders to which the conditional Fano bound applies.

Summing and averaging yields \(\mathbb E d_H(M,\widehat M)\geq3k/4\). Since this distance belongs to \([0,k]\),
\[
\mathbb E d_H(M,\widehat M)
\leq k/2+(k/2)\Pr(d_H(M,\widehat M)>k/2),
\]
so that probability is at least \(1/2\). If the original output has uniform error at most \(\epsilon\), its projection is within \(2\epsilon=ak/2\) of the true family member. By (11) its Hamming error is then at most \(k/2\). Hence the Bayes, and therefore worst-case, uniform-error probability is at least \(1/2\).

For \(1\leq n<12\), the preceding alphabet argument is replaced by a finite case using the same KL/Fano tools. Take sixteen constant functions
\[
f_j(x)=4\epsilon(j-15/2),\qquad j=0,\ldots,15.
\]
They are one-sparse, are bounded by one when \(\epsilon\leq1/30\), and have pairwise distance at least \(4\epsilon\). Their largest pairwise distance is \(60\epsilon\), so (2) bounds pairwise KL by \(1800m\epsilon^2/\sigma^2\). Here \(ns^2\leq1331\). Decreasing the universal \(c\) ensures that \(m\leq c\sigma^2ns^2/\epsilon^2\) makes this KL at most \((\log16)/16\). Fano gives identification error at least \(1-1/16-1/4=11/16\). Projection identifies the true constant whenever uniform estimation error is at most \(\epsilon\). Thus this case also has risk at least \(1/2\).

We have proved the support-search risk bound in every dimension, including \(s=1\), under the original parameter range.

## 3. High-confidence lower bound

Suppose \(L\geq s\). Restrict to
\[
f_\theta(x)=\sum_{j=1}^s\theta_jx_j,\qquad \|\theta\|_1\leq1.
\]
This is a subclass of the target class because \(s\leq n\). The cube realizes all sign patterns on these coordinates, so \(\|f_\theta\|_\infty=\|\theta\|_1\), and the same equality holds for differences within this linear family. No such equality is asserted for arbitrary Walsh supports or arbitrary learner outputs.

Initially use the unconditioned prior
\[
G\sim N(0,I_s),\qquad \theta=\mu G,\qquad
\mu=C_0\epsilon/\sqrt{sL}.
\]
Choose \(C_0\) as a sufficiently large universal constant. Include the learner's independent random seed in the transcript. Conditional on the seed and a realized transcript, its query vectors are fixed. The sequential likelihood for \(G\) is proportional to
\[
\exp\left[-\frac1{2\sigma^2}\sum_t
 (Y_t-\mu\langle X_{t,\leq s},G\rangle)^2\right].
\]
Multiplying by the standard Gaussian prior and completing the square proves that the posterior of \(G\), not of \(\theta\), has covariance
\[
\Sigma=(I_s+\mu^2\sigma^{-2}\sum_tX_{t,\leq s}X_{t,\leq s}^{\mathsf T})^{-1}.
\tag{12}
\]
The covariance of \(\theta\) is \(\mu^2\Sigma\). Formula (12) does not condition on the bounded-prior event.

Every query feature has squared Euclidean norm \(s\). If
\[
m\leq c_1\sigma^2sL/\epsilon^2,\qquad c_1\leq C_0^{-2},
\]
then
\[
\operatorname{tr}(\Sigma^{-1})=s(1+\mu^2m/\sigma^2)\leq2s.
\]
Cauchy--Schwarz on its positive eigenvalues gives
\(\operatorname{tr}(\Sigma)\operatorname{tr}(\Sigma^{-1})\geq s^2\), hence \(\operatorname{tr}(\Sigma)\geq s/2\), for every realized transcript.

Averaging over a uniform sign vector \(\eta\in\{-1,1\}^s\) gives \(\mathbb E_\eta\eta^{\mathsf T}\Sigma\eta=\operatorname{tr}(\Sigma)\). Therefore some sign vector \(\eta^*\) has quadratic form at least \(s/2\). Choose one by a fixed order, and extend it to a cube point by setting the other coordinates to one. At this transcript-dependent point, the posterior prediction variance is at least
\[
\mu^2s/2=C_0^2\epsilon^2/(2L).
\]
The output is fixed given the augmented transcript. A one-dimensional Gaussian places maximal mass in an interval of prescribed length when the interval is centered at its mean; this follows directly from symmetry and the density decreasing away from the mean. Thus, regardless of the output value at this point, its conditional error probability is at least
\[
\Pr\bigl(|Z|>\sqrt{2L}/C_0\bigr)\geq2\delta
\]
by (4), after choosing \(\sqrt2/C_0\leq b_0\). This is also a lower bound on conditional uniform-error probability. Integrating gives unconditioned Bayes risk at least \(2\delta\).

Now let \(B=\{\|\mu G\|_1\leq1\}\). Since \(\|\mu G\|_1=\max_{\eta\in\{-1,1\}^s}\mu\langle\eta,G\rangle\), and each scalar in this maximum is centered Gaussian with variance \(\mu^2s\), the Gaussian exponential tail and a union bound give
\[
\Pr(B^c)\leq2^s\exp\left(-\frac1{2\mu^2s}\right)
=\exp\left(s\log2-\frac{L}{2C_0^2\epsilon^2}\right).
\]
Choose \(\epsilon_0\) so that \(1/(2C_0^2\epsilon_0^2)\geq3\). Since \(s\leq L\), this is at most \(e^{-2L}=\delta^2\leq\delta/2\).

For the error event \(E\), the elementary inequality \(\Pr(E)\leq\Pr(E\mid B)+\Pr(B^c)\) now shows
\[
\Pr(E\mid B)\geq2\delta-\delta/2=3\delta/2>\delta.
\tag{13}
\]
The conditioned prior is supported on the required bounded subclass. Hence every learner below this sample threshold has worst-case error strictly greater than \(\delta\). Conditioning is performed only at this final Bayes-to-minimax step; it is not incorrectly used to assert a Gaussian posterior under a truncated prior.

## 4. Assembly

For \(L\geq s\), the two lower-bound arguments exclude every integer query budget below their respective thresholds, with risk greater than \(\delta\): the first gives at least \(1/2\), and (13) gives at least \(3\delta/2\). The maximum of the two thresholds is at least a universal constant times
\(\sigma^2\epsilon^{-2}(ns^2+sL)\).

For \(L<s\), one has \(sL\leq s^2\leq ns^2\), so the support-search bound alone gives the same conclusion after changing its universal constant. These statements also apply when a threshold is below one, because the arguments include the zero-query budget. Take \(\epsilon_0\) to be the minimum of the universal bounds imposed above. Together with (10), this proves the two inequalities with the requested quantifiers.

If \(\sigma\geq\sigma_0>0\) for a fixed positive universal constant, then \(1+\sigma^2\leq(1+\sigma_0^{-2})\sigma^2\), yielding the stated comparison of rates.

## Audit disposition

The source-local corrections are recorded under theory_005, theory_013, and theory_019. The missing definition closure is theory_017. No specialized external result or unproved paper-specific dependency is needed beyond the standard inequalities stated above. There are no unresolved theorem-critical proof obligations.
