# Reference Proof

## Proof Structure

1. Verify the integrability consequences of the path and model assumptions.
2. Express the log-density-ratio error as the time integral of the score error, apply Cauchy--Schwarz, and transfer the terminal expectation to the intermediate densities.
3. Derive the fitting-loss/surrogate identity by integrating the product of the density and model score, retaining both endpoint terms.
4. Use normalization to identify the marginal score's second moment with its variance almost everywhere in time.
5. Combine the identities and state the joint-reduction interpretation with the multiplicative constant fixed.

## Complete Proof

Fix an admissible parameter and write \(f(x,t)=s_\theta(x,t)\) and \(s(x,t)=s^{(t)}(x,t)\). Set
\[
A=\int_0^1\mathbb E_{p_t}[f(X,t)^2]dt,
\qquad
B=\int_0^1\mathbb E_{p_t}[|\partial_t f(X,t)|]dt.
\]
Both are finite by admissibility.

### Regularity and finiteness

For each \(x\), the Lipschitz function \(t\mapsto\log p_t(x)\) is absolutely continuous. The fundamental theorem for absolutely continuous functions states that its increments equal the integrals of its almost-everywhere derivative. In particular,
\[
|s(x,t)|\le L\quad\text{for almost every }t,
\qquad
e^{-L}p_0(x)\le p_t(x)\le e^Lp_0(x).
\]
Spatial measurability of each density and time continuity give joint measurability of the density path. Difference quotients give measurable versions of the score. Fubini shows that its almost-everywhere derivative and bound also hold outside a product-null set.

The chain rule for absolutely continuous functions gives
\[
\partial_t p_t(x)=p_t(x)s(x,t),
\qquad
|\partial_t p_t(x)|\le Le^Lp_0(x)
\]
almost everywhere. Thus the density derivatives are integrable over space and time. Also the measure \(p_t(x)\,dx\,dt\) has total mass one, so Cauchy--Schwarz yields
\[
\int_0^1\mathbb E_{p_t}|f|dt\le\sqrt A,
\qquad
\int_0^1\mathbb E_{p_t}|sf|dt\le L\sqrt A.
\]
Consequently the fitting loss is finite, since
\[
\mathcal L_{\rm fit}\le 2L^2+2A.
\]
The surrogate is a finite real number by the assumptions on \(A\), \(B\), and the endpoint values. The variance integral is well-defined and at most \(L^2\). Values assigned to derivatives on null sets do not change these integrals.

### Error reduction and density-ratio transfer

For almost every \(x\), the fundamental theorem gives
\[
\ell(x)-\widehat\ell_\theta(x)
=\int_0^1\bigl(s(x,t)-f(x,t)\bigr)dt.
\]
Write \(\varepsilon(x,t)=s(x,t)-f(x,t)\). Cauchy--Schwarz on the unit time interval gives
\[
|\ell(x)-\widehat\ell_\theta(x)|^2
\le\int_0^1|\varepsilon(x,t)|^2dt.
\]
All the densities are strictly positive, so spatial Lebesgue-null exceptional sets are null for the terminal law as well. Tonelli applies to the measurable nonnegative squared error, and positivity permits the change of density:
\[
\mathbb E_{p_1}|\ell(X)-\widehat\ell_\theta(X)|^2
\le\int_0^1\mathbb E_{p_t}
\left[|\varepsilon(X,t)|^2\frac{p_1(X)}{p_t(X)}\right]dt.
\]
The Lipschitz assumption implies
\[
\log p_1(x)-\log p_t(x)\le L(1-t),
\qquad
\frac{p_1(x)}{p_t(x)}\le e^{L(1-t)}\le e^L.
\]
Therefore
\[
\mathbb E_{p_1}|\ell(X)-\widehat\ell_\theta(X)|^2
\le e^L\mathcal L_{\rm fit}(\theta).
\]
This also proves finiteness of the terminal squared error.

### Integration-by-parts decomposition

For almost every \(x\), both \(p_t(x)\) and \(f(x,t)\) are absolutely continuous in time. Their product is absolutely continuous, with derivative
\[
\partial_t\bigl(p_t(x)f(x,t)\bigr)
=p_t(x)\partial_t f(x,t)+p_t(x)s(x,t)f(x,t).
\]
Its derivative is absolutely integrable over space and time because its integral in absolute value is at most \(B+L\sqrt A\). The endpoint products are spatially integrable by admissibility. We may therefore integrate the pointwise fundamental-theorem identity in \(x\) and use Fubini for the signed derivative. This yields
\[
\mathbb E_{p_1}f(X,1)-\mathbb E_{p_0}f(X,0)
=\int_0^1\mathbb E_{p_t}[\partial_t f+sf]dt.
\]
Equivalently,
\[
\int_0^1\mathbb E_{p_t}[sf]dt
=\mathbb E_{p_1}f(X,1)-\mathbb E_{p_0}f(X,0)
-\int_0^1\mathbb E_{p_t}[\partial_t f]dt.
\]
All terms in the square expansion are integrable. Substituting this identity into that expansion gives
\[
\begin{aligned}
\mathcal L_{\rm fit}(\theta)
&=\int_0^1\mathbb E_{p_t}[s^2+f^2-2sf]dt\\
&=\mathcal L_{\rm ibp}(\theta)
+\int_0^1\mathbb E_{p_t}[s^2]dt.
\end{aligned}
\]
This uses exactly the full surrogate normalization stated in the problem.

### Normalization and variance

For every \(0\le a<b\le1\), the fundamental theorem applied to \(p_t(x)\), followed by Fubini using \(|\partial_t p_t(x)|\le Le^Lp_0(x)\), gives
\[
\int_a^b\mathbb E_{p_t}s(X,t)dt
=\int_{\mathbb R^d}\bigl(p_b(x)-p_a(x)\bigr)dx=0.
\]
The integrable function \(t\mapsto\mathbb E_{p_t}s(X,t)\) therefore has zero integral on every interval and is zero almost everywhere. Thus, for almost every \(t\),
\[
\operatorname{Var}_{p_t}(s(X,t))
=\mathbb E_{p_t}[s(X,t)^2]
-\bigl(\mathbb E_{p_t}s(X,t)\bigr)^2
=\mathbb E_{p_t}[s(X,t)^2].
\]
It follows that
\[
\mathcal L_{\rm fit}(\theta)=\mathcal L_{\rm ibp}(\theta)+V.
\]
Combining this equality with the error bound proves
\[
\mathbb E_{p_1}|\ell(X)-\widehat\ell_\theta(X)|^2
\le e^L\bigl[\mathcal L_{\rm ibp}(\theta)+V\bigr].
\]
No division by \(L\) occurs. When \(L=0\), the path is constant, the marginal score and \(V\) vanish, and all the same arguments remain valid.

### Interpretation

With \(L\) held fixed, \(e^L\) is a positive constant. A simultaneous nonincrease of \(\mathcal L_{\rm ibp}\) and \(V\) gives a nonincrease of their sum and hence of the displayed upper bound; a strict decrease in their sum gives a strict decrease in that bound. In a comparison of designable paths, this statement applies when the paths satisfy the Lipschitz condition with the same chosen \(L\). It does not prove that reducing \(V\) alone reduces the bound, that \(L\) decreases, that the two terms have simultaneous separate minimizers, or that the actual estimation error must decrease. The surrogate itself need not be nonnegative; its sum with \(V\) is the nonnegative fitting loss.

## Dependency and Normalization Audit

The error transfer reconstructs the relevant upstream bound directly. The loss decomposition reconstructs the STSM/TSM fragment of the internal-support proposition directly, rather than treating a citation as proof. The main-text surrogate and the public task have the full normalization. The source's half-normalized appendix definition requires a factor of two in its corresponding loss identity; this local repair is recorded in theory_005. The CTSM portion, conditional-score risks, restricted-model optimum claims, and excluded closed-form path-variance formulas are not used. There are no unresolved theorem-critical proof obligations.
