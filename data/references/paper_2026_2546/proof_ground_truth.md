# Reference Proof

## Proof Structure

1. Interpret the R-transform on inverse branches determined by the specified initial Stieltjes transform near infinity.
2. Establish the rational reparameterization on a nonempty open set near infinity in each half-plane, then extend it using holomorphy and nonvanishing of the decompressed Stieltjes transform.
3. Clear denominators, expand binomially, and collect the finite coefficient formula.
4. Prove that the resulting polynomial is nonzero and conclude algebraicity.

## Complete Proof

Write
\[
P(z,m)=\sum_{i=0}^{d_z}\sum_{j=0}^{d_m}p_{ij}z^i m^j,
\qquad P\not\equiv0,
\]
and fix a realizable \(\tau\ge1\). Set \(c=(\tau-1)/\tau\).

### Inverse-branch interpretation

The R-transform in the setup is obtained by locally inverting the specified initial physical transform near infinity, separately in the two half-planes. On the corresponding inverse branch, write \(Z(M)\) for the initial spectral coordinate with
\[
m(Z(M))=M.
\]
Its defining R relation is
\[
R(-M)=Z(M)+\frac1M,
\qquad
Z(M)=R(-M)-\frac1M.
\]
Thus, wherever this inverse branch is initially defined,
\[
P(Z(M),M)=0.
\]
The finitely many exceptional coordinates in the initial algebraic assumption do not affect this identity: the composition is holomorphic locally and extends across any such coordinate at which the physical transform is holomorphic.

For completeness, local invertibility near infinity follows from the stated normalization. In a fixed cone about either imaginary semiaxis, apply Cauchy's derivative estimate to the holomorphic remainder in
\(m(z)=-1/z+O(z^{-2})\), using discs of radius proportional to \(|z|\) that stay in the same half-plane. This gives
\[
m'(z)=z^{-2}+O(z^{-3}).
\]
Consequently \(m'(z)\ne0\) sufficiently far out in these cones. The holomorphic inverse function theorem, which states that a holomorphic function with nonzero derivative has a holomorphic local inverse, therefore applies. The normalization fixes the inverse branches approaching infinity. The decompression identity in the setup uses precisely these corresponding inverse branches, not an arbitrary choice among values of a multivalued R-transform.

### Rational relation and analytic extension

On a nonempty open set near infinity in either half-plane, put \(\omega=m_\tau(z)\) and \(M=\tau\omega\). The normalization gives \(M\to0\) there, so the inverse-branch decompression identity gives
\[
R(-M)=z+\frac1\omega.
\]
Hence
\[
Z(M)=z+\frac1\omega-\frac1{\tau\omega}
=z+\frac{\tau-1}{\tau\omega},
\]
and therefore
\[
P\!\left(z+\frac{\tau-1}{\tau m_\tau(z)},\,\tau m_\tau(z)\right)=0
\]
on those open sets.

To extend this relation, write
\[
m_\tau(z)=\int_{\mathbb R}\frac1{x-z}\,\nu_\tau(dx).
\]
For \(z=u+iv\), \(v\ne0\),
\[
\Im m_\tau(z)=v\int_{\mathbb R}\frac1{(x-u)^2+v^2}\,\nu_\tau(dx).
\]
The integral is strictly positive because \(\nu_\tau\) is a probability measure. Thus \(m_\tau(z)\ne0\) throughout both half-planes. The transform is holomorphic there: on a neighborhood separated from the real axis, the Cauchy kernel and its derivative are bounded uniformly in \(x\), so differentiation under the integral is justified.

It follows that
\[
H_\tau(z)=P\!\left(z+\frac{c}{m_\tau(z)},\,\tau m_\tau(z)\right)
\]
is holomorphic on each half-plane. It vanishes on a nonempty open subset of each. The identity theorem, which says that a holomorphic function vanishing on a nonempty open subset of a connected domain vanishes on that domain, therefore yields \(H_\tau\equiv0\) on both half-planes. This proves the requested rational relation at every point of the stated physical domain, including points exceptional only for a chosen algebraic presentation.

This argument does not assert that \(\tau m_\tau(z)\) is always a value of the original physical sheet at the shifted coordinate. Only the initially matched inverse branch and the continued algebraic relation are used. Nor is uniqueness among the roots of an arbitrary P inferred from Herglotz normalization: the physical transforms are already specified by their probability measures.

### Polynomial extension and coefficients

For \(m\ne0\), define
\[
Q_\tau(z,m)=m^{d_z}P\!\left(z+\frac{c}{m},\,\tau m\right).
\]
The binomial theorem gives
\[
Q_\tau(z,m)=\sum_{i=0}^{d_z}\sum_{j=0}^{d_m}p_{ij}
\sum_{k=0}^{i}\binom{i}{k}\tau^j c^k
z^{i-k}m^{d_z+j-k}.
\]
Since \(k\le i\le d_z\), every exponent of \(m\) is nonnegative. This finite sum is a polynomial and provides the unique polynomial extension of the rational expression to \(m=0\).

Writing
\[
Q_\tau(z,m)=\sum_{a=0}^{d_z}\sum_{b=0}^{d_z+d_m}q_{ab}(\tau)z^a m^b,
\]
we obtain, for these nonnegative integer indices,
\[
q_{ab}(\tau)=
\sum_{\substack{i=a,\ldots,d_z\\j=b-d_z+i-a\in\{0,\ldots,d_m\}}}
 p_{ij}\binom{i}{a}\tau^j
 \left(\frac{\tau-1}{\tau}\right)^{i-a}.
\]
An empty sum is zero. At \(\tau=1\), a factor with exponent zero is one and a positive power of \((\tau-1)/\tau\) is zero. Thus the same expression covers the endpoint and gives \(Q_1(z,m)=m^{d_z}P(z,m)\).

### Nontriviality and algebraic closure

The polynomial \(Q_\tau\) is not identically zero. Indeed, the rational coordinate substitution
\[
(Z,M)=\left(z+\frac{c}{m},\,\tau m\right)
\]
has rational inverse
\[
(z,m)=\left(Z-\frac{\tau-1}{M},\,\frac{M}{\tau}\right),
\]
since \(\tau\ne0\). If \(Q_\tau\) were the zero polynomial, then division by \(m^{d_z}\) in the rational function field and substitution of this inverse would imply \(P(Z,M)\equiv0\), contradicting the assumption on P.

Finally, substituting \(m=m_\tau(z)\) into the polynomial expression and using the rational relation gives
\[
Q_\tau(z,m_\tau(z))=0
\qquad(z\in\mathbb C\setminus\mathbb R).
\]
Because this is a nonzero polynomial relation, \(m_\tau\) is algebraic. If the physical branch is also evaluated at a finite regular continuation point or has a finite boundary limit, the polynomial relation passes to that value by continuity. Such additional values are not needed for the task's stated nonreal domain; poles are not finite graph points.
