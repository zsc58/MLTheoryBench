# Reference Proof

## Proof Structure

1. Rewrite the objective as a linear term plus relative-entropy regularization and construct the normalized Gibbs candidate.
2. Use the relative-entropy identity to establish existence and optimality.
3. Verify the normalization-constrained first-order equation and solve it for the candidate's density.
4. Use equality conditions for relative entropy (equivalently, strict convexity) to prove uniqueness.

## Complete Proof

Let
\[
J(p)=\int_M p(m)G(m)\,d\mu(m)+\tau\,\mathrm{KL}(p\|p_0),
\qquad
\mathrm{KL}(p\|p_0)=\int_M p(m)\log\frac{p(m)}{p_0(m)}\,d\mu(m),
\]
for probability densities \(p\) with respect to \(\mu\), with the value \(+\infty\) when the integral is not finite. Since \(M\) is compact, \(G\) and the strictly positive continuous function \(p_0\) are bounded, and \(\log p_0\) is well defined and bounded. Define
\[
Z=\int_M e^{-G(u)/\tau}p_0(u)\,d\mu(u).
\]
The integrand is strictly positive and bounded on the compact space, and \(p_0\) is a probability density, so \(0<Z<\infty\). Set
\[
p_\tau(m)=\frac{e^{-G(m)/\tau}p_0(m)}{Z}.
\]
Then \(p_\tau\) is a probability density and has finite objective value.

For every admissible density \(p\), including the case of infinite relative entropy, direct expansion gives
\[
\begin{aligned}
\tau\,\mathrm{KL}(p\|p_\tau)
&=\tau\int_M p\log\frac{p}{p_0}\,d\mu
  +\int_M pG\,d\mu+\tau\log Z\\
&=J(p)+\tau\log Z.
\end{aligned}
\]
Thus
\[
J(p)=\tau\,\mathrm{KL}(p\|p_\tau)-\tau\log Z.
\]
Nonnegativity of relative entropy implies \(J(p)\ge -\tau\log Z=J(p_\tau)\), so a minimizer exists and is \(p_\tau\).

For completeness, the normalization-constrained first variation yields the same form. For any bounded perturbation \(h\) with \(\int_M h\,d\mu=0\), and sufficiently small \(\varepsilon\) so that \(p_\tau+\varepsilon h>0\), stationarity gives
\[
0=\left.\frac{d}{d\varepsilon}J(p_\tau+\varepsilon h)\right|_{\varepsilon=0}
=\int_M h\bigl(G+\tau(1+\log p_\tau-\log p_0)\bigr)\,d\mu.
\]
Hence the bracket is constant (the Lagrange multiplier for \(\int p=1\)): for some \(\lambda\),
\[
G(m)-\tau\log p_0(m)+\tau(1+\log p_\tau(m))+\lambda=0.
\]
Solving gives \(p_\tau(m)=C e^{-G(m)/\tau}p_0(m)\); imposing total mass one gives \(C=Z^{-1}\), exactly the displayed formula.

Finally, \(\mathrm{KL}(p\|p_\tau)=0\) holds only when \(p=p_\tau\) \(\mu\)-almost everywhere. Therefore the minimizer is unique (also reflected by strict convexity of the entropy term on the convex set of densities).
