# Reference Proof

## Proof Structure

Use the componentwise form of the exact update to expand the weighted loss. Then substitute the constrained predictor and verify that every copied-coordinate residual vanishes identically.

## Complete Proof

For every deterministic history \(h=(h_0,\ldots,h_M)\), the definition of \(T\) gives
\[
[T(h)]_j=h_{j+1}\quad(0\le j<M),
\qquad [T(h)]_M=F(h).
\]
Consequently, for any admissible \(Q\),
\[
\begin{aligned}
\mathcal L(Q)
&=\mathbb E\!\left[\sum_{j=0}^M a_j\|Q_j(Z)-[T(Z)]_j\|_2^2\right]\\
&=\mathbb E\!\left[\sum_{j=0}^{M-1}a_j\|Q_j(Z)-Z_{j+1}\|_2^2\right]
 +\mathbb E\!\left[a_M\|Q_M(Z)-F(Z)\|_2^2\right].
\end{aligned}
\]
The stated integrability permits the finite sum to be separated in this way.

Now let \(Q=B_g\). For every \(0\le j<M\), the \(j\)-th component of \(B_g(h)\) is \(h_{j+1}\). Hence
\[
[B_g(Z)]_j-Z_{j+1}=0\qquad(0\le j<M)
\]
almost surely. Its final component is \([B_g(Z)]_M=g(Z)\). Substitution into the preceding identity therefore yields
\[
\mathcal L(B_g)=\mathbb E\!\left[a_M\|g(Z)-F(Z)\|_2^2\right],
\]
which proves both assertions.
