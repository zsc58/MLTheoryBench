# Reference Proof

## Proof Structure and Obligations

We prove boundedness and measurability of the loss class and estimator, derive uniform convergence using finite-dimensional VC control and an entropy bound, and then combine empirical optimality with separation of the unique population minimizer. All parameters and the sampling law are fixed as the sample size grows.

The source's later concentration manipulation is not used: its expected uniform-deviation estimate already implies convergence in probability by Markov's inequality. The invalid interchange of centering and taking a supremum is recorded as a local source repair in the provenance.

## 1. Boundedness, continuity, and measurability

Put
\[
K=\{\mu\in\mathcal X:\|\mu\|_2\le B\},\qquad \mathcal M=K^k,
\]
and let \(A=\sup_{x\in\mathcal X}\|x\|_2<\infty\). The set \(K\) is nonempty and compact. For
\[
g_\mu(x,r)=\sum_{j=1}^p[r_j(x_j-\mu_j)^2+(1-r_j)\lambda\mu_j^2],
\]
we have, uniformly over \(\mu\in K\),
\[
0\le g_\mu(x,r)\le (A+B)^2+\lambda B^2=:H.
\]
Here \(H>0\), since \(B>0\). The same constant bounds \(\ell_\lambda(M;x,r)=\min_l g_{\mu_l}(x,r)\). In particular, the envelope is square-integrable. Compact support already supplies this property; no additional use of sub-Gaussianity is necessary.

For each observation, the loss is continuous in \(M\), being a finite minimum of continuous functions. It is measurable in the observation. Dominated convergence therefore makes \(L^\lambda\) continuous, and \(\widehat L_n^\lambda\) is continuous for every sample. Compactness gives existence of their minima.

Choose a countable dense subset \(D=\{V_1,V_2,\ldots\}\) of \(\mathcal M\), repeating points if necessary. Continuity implies that suprema of the absolute empirical deviations over \(\mathcal M\) equal suprema over \(D\), so those suprema are measurable. It also makes the loss class pointwise separable.

For completeness, the unique empirical minimizer has a measurable version. For fixed \(n\), the random variable \(a_n=\inf_s\widehat L_n^\lambda(V_s)\) is measurable. For each positive integer \(m\), select the first index \(s\) with \(\widehat L_n^\lambda(V_s)<a_n+1/m\). This produces a measurable approximate minimizer. On the event of uniqueness, compactness and continuity imply that every subsequential limit of these approximate minimizers is the unique minimizer, and hence that the sequence converges to it. Define the estimator by this measurable limit where it exists and by a fixed point of \(\mathcal M\) otherwise. This agrees almost surely with the assumed unique empirical minimizer. Moreover, all sample losses, and thus this construction, depend only on the indicators and the observed coordinates.

## 2. Complexity control

Let \(\mathcal G=\{g_\mu:\mu\in K\}\) and \(\mathcal H=\{\ell_\lambda(M;\cdot):M\in\mathcal M\}\). Expanding gives
\[
g_\mu(x,r)=\sum_jr_jx_j^2-2\sum_j\mu_jr_jx_j+(1-\lambda)\sum_j\mu_j^2r_j+\lambda\sum_j\mu_j^2.
\]
Consequently, \(\mathcal G\) lies in the span of the \(3p+1\) functions \(r_jx_j^2,r_jx_j,r_j\), and \(1\).

We use two standard independent VC facts: a vector space of real measurable functions of dimension at most \(d\) has VC-subgraph dimension at most \(d\); and a VC-subgraph class of dimension at most \(d\ge1\), bounded by a constant envelope \(H>0\), satisfies
\[
N(uH,\mathcal G,L_2(Q))\le (C_d/u)^{2d},\qquad 0<u\le1,
\]
for every probability measure \(Q\), where \(C_d\ge e\) depends only on \(d\). Here \(N\) denotes the covering number. These facts apply with \(d=3p+1\), since the base functions are measurable and the bound \(H\) was verified above.

We derive the corresponding bound for minima instead of merely citing a comparison principle. For any two lists of functions,
\[
|\min_l g_l-\min_l h_l|\le\max_l|g_l-h_l|\le\sum_l|g_l-h_l|.
\]
Taking an \(L_2(Q)\) cover of \(\mathcal G\) at radius \(uH/k\), and forming all ordered \(k\)-tuples of its centers, therefore covers \(\mathcal H\) at radius \(uH\). Thus
\[
N(uH,\mathcal H,L_2(Q))\le N(uH/k,\mathcal G,L_2(Q))^k
\le (C_dk/u)^{2dk}.
\]

## 3. Uniform convergence

We use the following standard independent consequence of symmetrization and the entropy integral. For a pointwise-separable measurable class \(\mathcal F\), bounded in absolute value by a constant \(H>0\), and iid observations with law \(P\),
\[
\mathbb E\sup_{f\in\mathcal F}|P_nf-Pf|
\le \frac{CH}{\sqrt n}\left[1+\int_0^1\sqrt{\log\left(\sup_QN(uH,\mathcal F,L_2(Q))\right)}\,du\right],
\]
where \(C\) is universal and the supremum can be taken over finitely supported probability measures \(Q\). The additive constant accommodates a reference function when zero is not in the class.

The observations \((X_i,R_i)\) are iid under the stated sampling model. All measurability, separability, and bounded-envelope hypotheses were verified in Section 1. The covering bound from Section 2 gives
\[
\int_0^1\sqrt{\log\left(\sup_QN(uH,\mathcal H,L_2(Q))\right)}\,du
\le \sqrt{2dk}\int_0^1\sqrt{\log(C_dk)+\log(1/u)}\,du<\infty.
\]
For example, use \(\sqrt{a+b}\le\sqrt a+\sqrt b\) and \(\sqrt{\log(1/u)}\le1+\log(1/u)\), whose integral is finite. Consequently, for a finite constant \(C_*\) depending only on the fixed envelope and dimensions,
\[
\Delta_n:=\sup_{M\in\mathcal M}|\widehat L_n^\lambda(M)-L^\lambda(M)|,
\qquad \mathbb E\Delta_n\le C_*/\sqrt n.
\]
Markov's inequality now yields, for every \(\eta>0\),
\[
\Pr(\Delta_n>\eta)\le C_*/(\eta\sqrt n)\longrightarrow0.
\]
This closes the uniform-convergence obligation without an additional concentration theorem. If the loss is truncated using its envelope at \(\sqrt n\), its discarded part is identically zero for \(n\ge H^2\); there is no unresolved tail argument.

## 4. Excess risk

Empirical optimality and the definition of \(\Delta_n\) give
\[
\begin{aligned}
0\le L^\lambda(\widehat M_n^\lambda)-L^\lambda(M^{*,\lambda})
&=[L^\lambda(\widehat M_n^\lambda)-\widehat L_n^\lambda(\widehat M_n^\lambda)]\\
&\quad+[\widehat L_n^\lambda(\widehat M_n^\lambda)-\widehat L_n^\lambda(M^{*,\lambda})]\\
&\quad+[\widehat L_n^\lambda(M^{*,\lambda})-L^\lambda(M^{*,\lambda})]
\le2\Delta_n.
\end{aligned}
\]
Hence the population excess risk converges to zero in probability.

## 5. Separation and parameter convergence

Fix \(\varepsilon>0\) and define
\[
A_\varepsilon=\{M\in\mathcal M:\|\operatorname{vec}(M)-\operatorname{vec}(M^{*,\lambda})\|_2\ge\varepsilon\}.
\]
If this set is empty, the requested probability is zero for every \(n\). Otherwise it is compact. Continuity of \(L^\lambda\) and uniqueness of its minimizer imply
\[
\delta_\varepsilon=\min_{M\in A_\varepsilon}[L^\lambda(M)-L^\lambda(M^{*,\lambda})]>0.
\]
Indeed, a zero minimum would give a second minimizer at distance at least \(\varepsilon\).

Therefore
\[
\begin{aligned}
\Pr(\|\operatorname{vec}(\widehat M_n^\lambda)-\operatorname{vec}(M^{*,\lambda})\|_2>\varepsilon)
&\le\Pr(2\Delta_n\ge\delta_\varepsilon)\\
&\le\frac{2\mathbb E\Delta_n}{\delta_\varepsilon}\longrightarrow0.
\end{aligned}
\]
This is the required convergence in probability.

The proof does not exclude all-missing masks or require positive \(\lambda\) or \(\lambda^*\). It applies whenever the stated uniqueness hypotheses hold, including singleton parameter spaces. Uniqueness is used for ordered center matrices exactly as stated, not merely modulo permutations. All theorem-critical obligations are closed.
