# Reference Proof

## Proof Structure

First justify conditional expectations and the measurable-multiplier rule for nonnegative variables, allowing infinite conditional expectations. Next identify coordinate densities, pulled back to the instance space, with conditional expectations of a joint density. Apply these facts to obtain both equations in the forward direction. Conversely, the first equation normalizes the factor product, and the two equations identify the marginals of the probability measure defined by that product.

## Complete Proof

Write \(\mathcal G_X=\sigma(X)\) and \(\mathcal G_Y=\sigma(Y)\). All products of extended nonnegative quantities use \(0\cdot\infty=0\).

### Nonnegative conditional expectations and multipliers

For a nonnegative random variable \(T\) and a sub-sigma-algebra \(\mathcal C\), the extended conditional expectation can be constructed as
\[
U=\lim_{n\to\infty}\mathbb E_P[T\wedge n\mid\mathcal C].
\]
Choose versions for which the sequence is nondecreasing outside one null set. By monotone convergence, for every \(D\in\mathcal C\),
\[
\int_D U\,dP=\lim_n\int_D(T\wedge n)\,dP=\int_D T\,dP.
\]
Thus \(U\) satisfies the defining test-event property of the nonnegative conditional expectation, even when some integrals are infinite.

If \(Z\) is a finite-valued nonnegative \(\mathcal C\)-measurable random variable, then
\[
\mathbb E_P[ZT\mid\mathcal C]=Z\mathbb E_P[T\mid\mathcal C]
\quad P\text{-a.s.}
\]
Indeed, for nonnegative simple \(Z\), the defining test-event identity gives, for every \(D\in\mathcal C\),
\[
\int_D ZU\,dP=\int_D ZT\,dP.
\]
For general \(Z\), choose nonnegative simple functions increasing to \(Z\) and apply monotone convergence to both sides. The resulting identity says precisely that the \(\mathcal C\)-measurable random variable \(ZU\) is a conditional expectation of \(ZT\). This also covers the set where \(Z=0\) and \(U=\infty\). Taking \(D=\Omega\) yields
\[
\mathbb E_P[ZT]=\mathbb E_P[Z\mathbb E_P[T\mid\mathcal C]].
\]
These arguments use the ordinary monotone convergence theorem for increasing sequences of nonnegative measurable functions; the nonnegativity and monotonicity hypotheses have been supplied explicitly.

### Restriction and coordinate densities

Suppose \(R\ll P\) is a probability measure with density \(u\). For every \(D\in\mathcal C\),
\[
\int_D\mathbb E_P[u\mid\mathcal C]\,dP=\int_Du\,dP=R(D).
\]
Consequently, \(\mathbb E_P[u\mid\mathcal C]\) is the Radon–Nikodym density of \(R|\mathcal C\) with respect to \(P|\mathcal C\).

If \(r=dR_X/dP_X\), then for every \(H\in\mathcal H\),
\[
\int_{\{X\in H\}}r(X)\,dP
=\int_Hr\,dP_X
=R_X(H)
=R(X^{-1}(H)).
\]
Every event in \(\mathcal G_X\) is of the form \(X^{-1}(H)\), so \(r(X)\) is also the density of \(R|\mathcal G_X\) with respect to \(P|\mathcal G_X\). Uniqueness of Radon–Nikodym derivatives gives
\[
r(X)=\mathbb E_P[u\mid\mathcal G_X]\quad P\text{-a.s.}
\]
The same argument applies to the label coordinate. In particular, coordinate densities are functions on their coordinate spaces, while their compositions with \(X\) or \(Y\) are restriction densities on \(\Omega\).

### Forward direction

Suppose \(Q\) has the prescribed marginals and
\[
f=a(X)b(Y)=\frac{dQ}{dP}.
\]
The restriction calculation and the nonnegative multiplier rule give
\[
h(X)=\mathbb E_P[f\mid\mathcal G_X]
=a(X)\mathbb E_P[b(Y)\mid\mathcal G_X],
\]
because \(a(X)\) is finite-valued, nonnegative and \(\mathcal G_X\)-measurable. Similarly,
\[
g(Y)=\mathbb E_P[f\mid\mathcal G_Y]
=b(Y)\mathbb E_P[a(X)\mid\mathcal G_Y].
\]
Both equalities hold \(P\)-almost surely. No separate integrability of either factor is required.

### Converse: normalization and construction

Suppose the two displayed equations in the task hold. The nonnegative multiplier identity gives
\[
\mathbb E_P[a(X)b(Y)]
=\mathbb E_P\!\left[a(X)\mathbb E_P[b(Y)\mid\mathcal G_X]\right]
=\mathbb E_P[h(X)]
=\int h\,dP_X
=1.
\]
Thus \(f=a(X)b(Y)\) is nonnegative, measurable and integrable, with total mass one. For \(D\in\mathcal F\), define
\[
Q(D)=\int_D f\,dP.
\]
Integration against a nonnegative measurable function defines a measure: countable additivity follows by monotone convergence applied to partial sums of indicators of disjoint events. The total-mass identity makes this measure a probability measure. It is absolutely continuous with respect to \(P\), and \(dQ/dP=f\), so it is an FJS law with the specified factors.

### Converse: verification of both marginals

For every \(H\in\mathcal H\),
\[
\begin{aligned}
Q_X(H)
&=Q(X^{-1}(H))\\
&=\mathbb E_P[\mathbf1_{\{X\in H\}}a(X)b(Y)]\\
&=\mathbb E_P[\mathbf1_{\{X\in H\}}a(X)\mathbb E_P[b(Y)\mid\mathcal G_X]]\\
&=\mathbb E_P[\mathbf1_{\{X\in H\}}h(X)]\\
&=\int_Hh\,dP_X=\mu(H).
\end{aligned}
\]
Here the multiplier is \(\mathbf1_{\{X\in H\}}a(X)\), which is finite-valued, nonnegative and \(\mathcal G_X\)-measurable. Hence \(Q_X=\mu\).

Likewise, for every \(G\in\mathcal G\),
\[
\begin{aligned}
Q_Y(G)
&=Q(Y^{-1}(G))\\
&=\mathbb E_P[\mathbf1_{\{Y\in G\}}a(X)b(Y)]\\
&=\mathbb E_P[\mathbf1_{\{Y\in G\}}b(Y)\mathbb E_P[a(X)\mid\mathcal G_Y]]\\
&=\mathbb E_P[\mathbf1_{\{Y\in G\}}g(Y)]\\
&=\int_Gg\,dP_Y=\nu(G).
\end{aligned}
\]
Thus \(Q_Y=\nu\), completing the equivalence.

## Proof-Obligation Audit

- Extended nonnegative conditional expectations and the measurable-multiplier rule: derived by truncation, simple-function approximation and monotone convergence.
- Restriction-density and coordinate-density identification: derived by test events and Radon–Nikodym uniqueness.
- Both necessary equations: derived using the multiplier rule and the prescribed marginals.
- Product normalization and construction of an absolutely continuous probability measure: explicitly established.
- Both prescribed marginals: checked on all measurable coordinate events with correctly typed integrals.

No unresolved proof obligation remains.
