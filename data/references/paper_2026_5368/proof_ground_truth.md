# Reference Proof

## Proof Structure and Obligations

The proof must close four obligations: identify the common feature-conditional posteriors; identify feature-conditional correctness for the deterministic predicted class; condition the resulting identities on the relevant score within each domain; and transport the domain-specific almost-everywhere identities to the stated comparison measures before establishing both equivalences.

The selected source provides these arguments through theory_003, theory_006, and theory_007. The standard conditional-expectation facts used below are the independently applicable background result theory_014. No canonical calibration theorem, calibration-to-score assumption, estimation bound, or optimization result is needed.

## Standard Conditional-Expectation Facts

For an integrable random variable \(U\) and sigma-algebras \(\mathcal H\subseteq\mathcal G\),
\[
\mathbb E[\mathbb E[U\mid\mathcal G]\mid\mathcal H]
=\mathbb E[U\mid\mathcal H]\quad\text{almost surely}.
\]
Indeed, for every \(B\in\mathcal H\), the integrals over \(B\) of the left side, of \(\mathbb E[U\mid\mathcal G]\), and of \(U\) agree. Conditional-expectation uniqueness gives the assertion. Conditional expectation is linear for finite sums, and a bounded \(\mathcal G\)-measurable factor \(H\) can be pulled out:
\[
\mathbb E[HU\mid\mathcal G]=H\mathbb E[U\mid\mathcal G]\quad\text{almost surely}.
\]
A conditional event probability is the conditional expectation of its indicator. For a real-valued conditioning statistic \(T\), measurable functions representing the same conditional expectation agree almost everywhere under the law of \(T\), not necessarily at every score value.

All these facts apply here: the label indicators and posterior probabilities are bounded, and the measurable classifier and tie-breaking rule make \(A\), \(M\), and each \(R_k\) measurable functions of \(Z\). Thus the score sigma-algebras are contained in \(\sigma(Z)\).

## Complete Proof

### 1. Common posteriors and predicted-class correctness

Fix \(d\in\{P,Q\}\). The covariate-shift assumption supplies the same functions \(\eta_k\) in both domains, and
\[
\mathbb E_d[L_k\mid Z]=\eta_k(Z)\quad d\text{-almost surely},\qquad k=1,\ldots,K.
\]
Here \(L_k\) is the indicator of \(\{L_k=1\}\). Since there are finitely many classes, the identities may be used simultaneously outside a single \(d\)-null set.

Because \(A\) is a deterministic measurable function of \(Z\),
\[
\mathbf 1\{L_A=1\}=\sum_{k=1}^K\mathbf 1\{A=k\}L_k.
\]
Finite linearity and the measurable-factor property therefore give
\[
\begin{aligned}
\mathbb E_d[\mathbf 1\{L_A=1\}\mid Z]
&=\sum_{k=1}^K\mathbf 1\{A=k\}\mathbb E_d[L_k\mid Z]\\
&=\sum_{k=1}^K\mathbf 1\{A=k\}\eta_k(Z)
=\eta_A(Z)
\end{aligned}
\]
\(d\)-almost surely. This explicitly verifies that the same feature-conditional correctness function is used in both domains.

### 2. Domain-specific score identities

Since \(\sigma(M)\subseteq\sigma(Z)\), the tower property gives
\[
\Pr_d(L_A=1\mid M)
=\mathbb E_d[\eta_A(Z)\mid M]\quad d\text{-almost surely}.
\]
Consequently, for the measurable versions appearing in the task,
\[
\Pr_d(L_A=1\mid M=m)
=\mathbb E_d[\eta_A(Z)\mid M=m]
\]
for \(\mu_{d,M}\)-almost every \(m\).

Likewise, \(\sigma(R_k)\subseteq\sigma(Z)\), so for each class \(k\),
\[
\Pr_d(L_k=1\mid R_k)
=\mathbb E_d[\eta_k(Z)\mid R_k]\quad d\text{-almost surely}.
\]
As functions of the conditioning value, this says
\[
\Pr_d(L_k=1\mid R_k=r)
=\mathbb E_d[\eta_k(Z)\mid R_k=r]
\]
for \(\mu_{d,R_k}\)-almost every \(r\). These statements have been established separately under both domains; no comparison of random variables defined under different laws is being presumed.

### 3. Comparison measures and both equivalences

For the top-label identity, let \(N_{P,M}\) and \(N_{Q,M}\) be measurable exceptional sets under the respective score laws. Absolute continuity gives
\[
\nu_M(N_{P,M})=\nu_M(N_{Q,M})=0.
\]
Outside their union, each domain's conditional correctness probability equals its own displayed conditional posterior expectation. At each such score value, equality of the two correctness probabilities is therefore equivalent to equality of the two posterior expectations. Hence one equality holds \(\nu_M\)-almost everywhere if and only if the other does. This proves clause 1 in both directions.

For each fixed class \(k\), apply the same argument to the two exceptional sets for the identities conditioned on \(R_k\). They are both \(\nu_{R_k}\)-null because \(\nu_{R_k}\ll\mu_{P,R_k},\mu_{Q,R_k}\). Thus, for this class, equality of the domain-specific class probabilities \(\nu_{R_k}\)-almost everywhere is equivalent to equality of the corresponding posterior expectations \(\nu_{R_k}\)-almost everywhere. Taking the conjunction over the finite set of classes proves clause 2 in both directions.

The argument applies to arbitrary measurable versions: replacing a domain-specific version changes it only on a set null for its score law, and thus also null for the corresponding comparison measure.

## Boundary and Scope Checks

No division by the probability of a score event is used. Constant scores, atoms, score endpoints, zero or one posterior values, and ties handled by the fixed measurable rule are all covered. If a pair of score laws is mutually singular, every measure absolutely continuous with respect to both is zero, and the corresponding almost-everywhere claims are vacuous. This is consistent with the absence of a version-independent cross-domain comparison on exclusively domain-specific score mass. Neither source/target support inclusion nor perfect calibration in either domain is required. The source assumption that feature marginals differ is preserved, although the conditional-expectation argument does not need to use that inequality.

All theorem-critical obligations are closed; there is no unresolved reference-proof dependency.
