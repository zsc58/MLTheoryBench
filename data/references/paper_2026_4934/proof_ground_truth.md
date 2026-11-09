# Reference Proof

## Proof Structure

Derive the empirical energy representation of CRPS directly from its integral definition. For each held-out response, express its leave-one-out score through the distances to the retained responses and the retained sample's ordered pairwise distance sum. Sum these expressions and use the counting identities between ordered and unordered pairwise sums to obtain the claimed scalar cost.

The theorem-critical obligations are: (1) establish the empirical energy identity with its domain and normalizations; (2) establish the ordered-pair deletion identity; and (3) sum and simplify without excluding repeated responses, zero dispersion, or the boundary case \(m=2\). Each obligation is derived below; no external theorem is needed.

## Complete Proof

### 1. Derive the empirical energy identity

Let \(r\ge1\) be an integer, let \(z_1,\dots,z_r,y\in\mathbb R\), and write
\[
H_i(t)=\mathbf1\{t\ge z_i\},\qquad H_y(t)=\mathbf1\{t\ge y\},\qquad G(t)=\frac1r\sum_{i=1}^r H_i(t).
\]
For any real \(u,v\), the function \((\mathbf1\{t\ge u\}-\mathbf1\{t\ge v\})^2\) is the indicator of the interval between \(u\) and \(v\), up to endpoints. Consequently,
\[
\int_{\mathbb R}(\mathbf1\{t\ge u\}-\mathbf1\{t\ge v\})^2\,dt=|u-v|.
\]
Expanding the squares gives the pointwise identity
\[
(G-H_y)^2
=\frac1r\sum_{i=1}^r(H_i-H_y)^2
-\frac1{2r^2}\sum_{i=1}^r\sum_{j=1}^r(H_i-H_j)^2.
\]
Indeed, the first term on the right expands to \(r^{-1}\sum_i H_i^2-2GH_y+H_y^2\), while the second expands to \(r^{-1}\sum_i H_i^2-G^2\).

All the squared differences vanish outside the bounded interval containing \(z_1,\dots,z_r,y\). They are measurable and integrable, so integrating the finite sums is legitimate. Thus
\[
\operatorname{CRPS}(G,y)
=\frac1r\sum_{i=1}^r|z_i-y|
-\frac1{2r^2}\sum_{i=1}^r\sum_{j=1}^r|z_i-z_j|.
\]
This identity includes \(r=1\) and repeated values. The empirical distribution has finite first absolute moment because it has finitely many real atoms.

### 2. Apply the identity to each held-out observation

Let
\[
d_k=\sum_{\ell\ne k}|y_\ell-y_k|,
\qquad
D=\sum_{a\ne b}|y_a-y_b|,
\qquad
W=\sum_{1\le a<b\le m}|y_a-y_b|.
\]
Here the sums are over observation indices, so repeated values retain their multiplicity. Symmetry gives \(D=2W\).

For the empirical CDF \(F_{-k}\) of the \(m-1\) responses other than observation \(k\), the identity just proved, with \(r=m-1\ge1\), gives
\[
\operatorname{CRPS}(F_{-k},y_k)
=\frac{d_k}{m-1}-\frac{1}{2(m-1)^2}
\sum_{\substack{a\ne b\\a,b\ne k}}|y_a-y_b|.
\]
The diagonal terms of the double sum vanish. Deleting index \(k\) from the ordered off-diagonal sum removes the pairs \((k,\ell)\) and \((\ell,k)\), whose total contribution is \(2d_k\). Hence
\[
\operatorname{CRPS}(F_{-k},y_k)
=\frac{d_k}{m-1}-\frac{D-2d_k}{2(m-1)^2}.
\]

### 3. Sum and simplify

Every ordered pair of distinct indices occurs exactly once in \(\sum_k d_k\). Therefore \(\sum_k d_k=D\), and
\[
\begin{aligned}
\operatorname{Cost}(B)
&=\sum_{k=1}^m\operatorname{CRPS}(F_{-k},y_k)\\
&=\frac{D}{m-1}-\frac{mD-2D}{2(m-1)^2}\\
&=\frac{2D(m-1)-(m-2)D}{2(m-1)^2}\\
&=\frac{mD}{2(m-1)^2}\\
&=\frac{mW}{(m-1)^2}.
\end{aligned}
\]
All denominators are positive for \(m\ge2\). At \(m=2\), the retained off-diagonal sum is empty and equals zero, as required by the same derivation. No step divides by a distance or by \(W\), so ties and the case \(W=0\) are included. This proves the identity for every bin in the stated domain.
