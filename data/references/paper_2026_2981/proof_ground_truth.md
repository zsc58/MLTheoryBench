# Reference Proof

## Proof Structure

1. Identify least-squares capacity with squared orthogonal projection onto the readout span.
2. Lift the input basis into the tensor-product input/noise space and apply Parseval completeness.
3. Show that a genuinely noise-dependent readout has strictly less than unit projection mass onto the input-only subspace.
4. Sum the resulting bounds, treating both linearly dependent and independent readouts.

## Complete Proof

Let \(\mathcal H=\mathcal H_u\otimes\mathcal H_\epsilon\), let \(\mathcal S=\operatorname{span}\{X_1,\ldots,X_K\}\), and let \(P_{\mathcal S}\) be the orthogonal projector onto \(\mathcal S\). For any nonzero target \(f\in\mathcal H_u\), identified with \(f(u)z_1(\epsilon)=f(u)\), the minimum mean-squared error over linear combinations of the readouts is attained by the orthogonal projection \(P_{\mathcal S}f\). Indeed, after an invertible whitening transformation of any full-rank readout Gram matrix, the transformed readouts are orthonormal and span the same subspace; least-squares coefficients are their inner products with \(f\). The same conclusion holds on the support when the Gram matrix is singular, using the Moore--Penrose solution. Consequently,
\[
 C(f,\mathcal S)=\frac{\|P_{\mathcal S}f\|^2}{\|f\|^2}.
\]

Let \(d=\dim\mathcal S\le K\), and choose an orthonormal basis \(q_1,\ldots,q_d\) of \(\mathcal S\). Since \(\{y_lz_m:l,m\}\) is a complete orthonormal basis of \(\mathcal H\), Parseval gives, for every \(j\),
\[
 \sum_{l,m}|\langle y_lz_m,q_j\rangle|^2=\|q_j\|^2=1.
\]
Therefore the input-basis capacities satisfy
\[
 \sum_l C(y_l,\mathcal S)
 =\sum_l\sum_{j=1}^d|\langle y_lz_1,q_j\rangle|^2
 =\sum_{j=1}^d a_j,
 \quad a_j:=\sum_l|\langle y_lz_1,q_j\rangle|^2\le1.
\]

If \(d<K\), this immediately yields \(\sum_l C(y_l,\mathcal S)\le d<K\). Suppose instead that \(d=K\). Because the system is genuinely noisy, \(\mathcal S\) is not contained in the input-only subspace \(\mathcal H_u\otimes\operatorname{span}\{z_1\}\). Hence an orthonormal basis of \(\mathcal S\) can be chosen with at least one vector, say \(q_1\), having a nonzero component along some \(y_lz_m\) with \(m\ne1\). Parseval then implies
\[
 a_1=\sum_l|\langle y_lz_1,q_1\rangle|^2
 =1-\sum_{m\ne1}\sum_l|\langle y_lz_m,q_1\rangle|^2<1.
\]
All other \(a_j\le1\), so
\[
 \sum_l C(y_l,\mathcal S)=\sum_{j=1}^K a_j<K.
\]
Combining the two cases proves the claim.
