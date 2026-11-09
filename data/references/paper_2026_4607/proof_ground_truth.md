# Reference Proof

## Proof Structure

Expand the conditional mutual information by entropy identities; use the conditional bijection between binary predictions and error indicators; apply the mutual-information chain rule to isolate marginal error dependence and the label-dependence correction; then simplify under joint independence of the error vector and the label.

## Complete Proof

Fix `S` and `j` with `j` not in `S`. By the entropy definition of conditional mutual information,
\[
\Delta(j\mid S)=H(X_j\mid X_S)-H(X_j\mid X_S,Y).
\]
The first term is
\[
H(X_j\mid X_S)=H(X_j)-I(X_j;X_S).
\]
For every fixed value of `Y`, the map from the prediction vector to the error vector is bijective: componentwise, `E_i=1{X_i != Y}` and equivalently `X_i=Y(-1)^{E_i}`. Thus conditional entropy is invariant under this (joint) bijection, giving
\[
H(X_j\mid X_S,Y)=H(E_j\mid E_S,Y).
\]
Also, conditioning on `Y` gives a bijection between `X_j` and `E_j`, so
\[
H(X_j)-H(E_j\mid Y)=I(Y;X_j).
\]
Using \(H(E_j\mid E_S,Y)=H(E_j\mid Y)-I(E_j;E_S\mid Y)\), we obtain
\[
\Delta(j\mid S)=I(Y;X_j)-I(X_j;X_S)+I(E_j;E_S\mid Y).
\]
Apply the mutual-information chain rule to \(I(E_j;E_S,Y)\) in the two orders:
\[
I(E_j;E_S)+I(E_j;Y\mid E_S)
=I(E_j;Y)+I(E_j;E_S\mid Y).
\]
Therefore
\[
I(E_j;E_S\mid Y)=I(E_j;E_S)+I(E_j;Y\mid E_S)-I(E_j;Y),
\]
which, with the definition of \(\Lambda_j(S)\), proves
\[
\Delta(j\mid S)=I(Y;X_j)-I(X_j;X_S)+I(E_j;E_S)+\Lambda_j(S).
\]
If the entire error vector is jointly independent of `Y`, then both \(I(E_j;Y)=0\) and \(I(E_j;Y\mid E_S)=0\), since the joint law of \((E_j,E_S)\) factors from `Y`. Hence \(\Lambda_j(S)=0\), and the stated accuracy-minus-redundancy-plus-error-correlation formula follows.
