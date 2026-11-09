# Reference Proof

## Audited Proof Obligations

1. The score and empirical-tube events are measurable for the specified measure-valued predictor and fixed spherical sliced discrepancy.
2. Exchangeability gives the ambient score bound, including tied scores and a quantile rank exceeding the calibration size.
3. Empirical-tube failure forces every cover cell containing the test target to contain no training target.
4. The iid target assumption gives the relevant occupancy probabilities; a finite union bound works without disjointness or positive cell masses.
5. A final union bound combines the two failure probabilities without any independence assumption between them.

All five obligations are closed below. The standard split-conformal result indexed by theory_004 is also derived directly, so no external proof obligation remains.

## Proof Structure

Bound noncoverage of the intersection by the union of ambient score failure and empirical-tube failure. Control the first by exchangeable ranks. For the second, use the diameter condition and iid empty-cell probabilities, then sum over the finite cover.

## Complete Proof

The great-circle projections, empirical-measure map, and predictor are measurable. Wasserstein distance on the compact circle is a measurable function of its probability-measure arguments. Thus the fixed integral or finite average defining d, the scores, their order statistics, and the finite minimum defining d_M give measurable events. All distances are finite: the circle's geodesic distance is at most pi.

Write
\[
S_{n+1}=S(Y_{n+1},f(X_{n+1})),\qquad
E_s=\{S_{n+1}>\tau_\alpha\},\qquad
E_m=\{d_M(Y_{n+1})>\varepsilon\}.
\]
By the definition of the prediction set,
\[
\Pr(Y_{n+1}\notin C_\alpha(X_{n+1}))
\leq \Pr(E_s)+\Pr(E_m).
\]

### Ambient score failure

The predictor and discrepancy are fixed, so exchangeability of the calibration and test pairs implies exchangeability of \(S_1,\ldots,S_{n+1}\). Put
\[
k=\lceil(n+1)(1-\alpha)\rceil.
\]
If \(k=n+1\), the cutoff is \(+\infty\), and \(\Pr(E_s)=0\).

Otherwise, introduce independent uniform random variables \(U_1,\ldots,U_{n+1}\), independent of the data, solely for the proof. Order the pairs \((S_i,U_i)\) lexicographically. They are exchangeable and almost surely distinct. Consequently, the rank \(R\) of the test pair is uniform on \(\{1,\ldots,n+1\}\): for each possible rank, exactly one index occupies it, and exchangeability assigns equal probability to each index.

On \(E_s\), at least \(k\) calibration scores are strictly smaller than \(S_{n+1}\), so \(R>k\), regardless of ties among other scores. Hence
\[
\Pr(E_s)\leq\Pr(R>k)
=\frac{n+1-k}{n+1}\leq\alpha.
\]
The auxiliary uniforms do not change the prediction set.

### Empirical-tube failure

Put \(p_j=Q(A_j)\). Almost surely, \(Y_{n+1}\in M\), and the cover therefore contains the test target in at least one cell. If \(Y_{n+1}\in A_j\) and a training target \(Y_i^0\in A_j\), the diameter assumption gives
\[
d(Y_{n+1},Y_i^0)\leq\varepsilon,
\]
which implies \(d_M(Y_{n+1})\leq\varepsilon\). Thus, up to the null event that the test target lies outside \(M\),
\[
E_m\subseteq\bigcup_{j=1}^{N_\varepsilon}
\{Y_{n+1}\in A_j,\ Y_i^0\notin A_j\text{ for every }i\leq n_0\}.
\]
Because the training targets and the test target are iid with law \(Q\),
\[
\Pr(Y_{n+1}\in A_j,\ Y_i^0\notin A_j\ \forall i)
=p_j(1-p_j)^{n_0}.
\]
This calculation is unconditional and remains valid for zero-mass cells; there is no conditioning on an event of probability zero. Since \(p_j\geq\beta_\varepsilon\),
\[
p_j(1-p_j)^{n_0}
\leq p_j(1-\beta_\varepsilon)^{n_0}.
\]
The finite union bound and \(\sum_jp_j\leq N_\varepsilon\) yield
\[
\Pr(E_m)
\leq (1-\beta_\varepsilon)^{n_0}\sum_{j=1}^{N_\varepsilon}p_j
\leq N_\varepsilon(1-\beta_\varepsilon)^{n_0}.
\]
No disjointness of the cells is assumed. Since \(n_0\geq1\), the calculation also covers \(\beta_\varepsilon=1\); when \(\beta_\varepsilon=0\), the displayed bound is valid, though possibly vacuous.

### Final coverage bound

Combining the two failure bounds gives
\[
\Pr\bigl(Y_{n+1}\in C_\alpha(X_{n+1})\bigr)
\geq1-\alpha-N_\varepsilon(1-\beta_\varepsilon)^{n_0}.
\]
Neither independence of the test target from calibration nor independence of the two failure events is needed. A negative right-hand side causes no difficulty. This proves the claim.
