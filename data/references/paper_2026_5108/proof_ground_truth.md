# Reference Proof

## Proof Obligations

1. Verify that the pushforward laws and the sets used in the exact-dimensional conclusion are measurable, and cover zero ball masses and constant maps.
2. Establish the Lipschitz ball inclusion and pushforward-mass comparison.
3. Handle the negative logarithmic denominator and constant-radius rescaling for both upper and lower limits, including infinite values.
4. Apply the comparison to every layer and transfer the output exact-dimensional full-measure set back to the input law.

## Complete Proof

### Well-definedness and measurability

Each T_l is continuous, hence Borel measurable. Thus the recursive pushforwards are Borel probability measures.

For any Borel probability measure rho and 0<r<1, put
\[
q_{\rho,z}(r)=\frac{\log\rho(B(z,r))}{\log r}\in[0,+\infty],
\]
using log(0)=-infinity. All subsequent inequalities and limits use this extended-real convention.

For fixed r>0, the function z -> rho(B(z,r)) is lower semicontinuous. Indeed, if z_j -> z and 0<s<r, then B(z,s) is contained in B(z_j,r) for all sufficiently large j. Consequently,
\[
\liminf_j\rho(B(z_j,r))\geq\rho(B(z,s)).
\]
Letting s increase to r and using continuity of a measure under increasing unions proves the assertion. In particular, the ball-mass functions and q_{rho,z}(r) are Borel measurable in z.

The upper and lower limits defining the dimensions can be taken along r=2^{-k}. To see this, if 2^{-(k+1)}<r\leq2^{-k}, monotonicity of ball masses gives
\[
\frac{k}{k+1}q_{\rho,z}(2^{-k})
\leq q_{\rho,z}(r)
\leq\frac{k+1}{k}q_{\rho,z}(2^{-(k+1)}).
\]
These inequalities, together with the dyadic subsequence itself, identify both full limits with their respective dyadic limsup and liminf. Therefore the upper and lower dimensions are Borel measurable extended-real functions. In particular, the set where both equal a specified constant is Borel measurable.

### Comparison for a single layer

Fix l in {1,...,L}, and abbreviate
\[
f=T_l,\qquad \mu=\rho_{l-1},\qquad \nu=\rho_l=f_\#\mu.
\]
Choose a finite Lipschitz constant C>=1 for f. Such a choice is always possible by increasing any Lipschitz constant; it also covers constant maps, so there is no division by a zero Lipschitz constant.

Fix x and put y=f(x). For every r>0, Lipschitz continuity gives
\[
f(B(x,r/C))\subseteq B(y,r).
\]
It follows that
\[
\nu(B(y,r))
=\mu\bigl(f^{-1}(B(y,r))\bigr)
\geq\mu(B(x,r/C)).
\]
For 0<r<1, taking logarithms and dividing by the negative number log r reverses the inequality:
\[
q_{\nu,y}(r)
\leq\frac{\log\mu(B(x,r/C))}{\log r}.
\]
This remains valid if either ball mass is zero, with the stated extended-real convention.

Set t=r/C. The right-hand side becomes
\[
q_{\mu,x}(t)\frac{\log t}{\log t+\log C}.
\]
The second factor is positive for the radii under consideration and tends to 1 as t decreases to zero. Since q_{mu,x}(t) is nonnegative, multiplying it by this factor preserves its limsup and liminf, including infinite values: for every epsilon in (0,1), the product is eventually between (1-epsilon)q_{mu,x}(t) and (1+epsilon)q_{mu,x}(t), after which epsilon can decrease to zero.

The change of variables r=Ct runs through all sufficiently small positive radii. Taking limsups and liminfs therefore proves
\[
\overline d_\nu(f(x))\leq\overline d_\mu(x),
\qquad
\underline d_\nu(f(x))\leq\underline d_\mu(x).
\]
The argument works for every x with the extended-real definitions, and hence in particular for mu-almost every x. Wherever both ordinary pointwise dimensions exist, substituting their common upper and lower values gives
\[
d_\nu(f(x))\leq d_\mu(x).
\]
Applying this argument separately to every l proves all the requested layer-wise comparisons.

### Exact-dimensional laws

Suppose rho_l is exact-dimensional with dimension a_l for every l=0,...,L. Let
\[
E_l=\{z:\underline d_{\rho_l}(z)=\overline d_{\rho_l}(z)=a_l\}.
\]
The measurability argument above shows that E_l is Borel, and exact-dimensionality gives rho_l(E_l)=1. For each l>=1, the pushforward identity gives
\[
\rho_{l-1}(T_l^{-1}(E_l))=\rho_l(E_l)=1.
\]
Hence E_{l-1} intersected with T_l^{-1}(E_l) has rho_{l-1}-measure one. On that intersection the pointwise comparison reads
\[
a_l\leq a_{l-1}.
\]
This proves the conclusion for every l=1,...,L. All proof obligations are closed.
