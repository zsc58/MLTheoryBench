# Reference Proof

## Proof Structure

Expand the quadratic forms into ordered-pair sums, derive the weighted-pair average, impose the complete-network normalization to identify the only possible denominator, and regroup the pair sums by the number of ordered links to obtain the density-assortativity factorization.

## Complete Proof

Let C = 11^T - I. Since A and C have zero diagonal,
\[
w^T A w = \sum_{i\ne j} w_i w_j A_{ij},\qquad
w^T C w = \sum_{i\ne j} w_i w_j C_{ij}.
\]
For C, using \(\sum_i w_i=1\),
\[
w^T C w = w^T11^Tw-w^Tw = (\sum_i w_i)^2-\sum_iw_i^2 = 1-\sum_iw_i^2.
\]
Therefore, on the nondegenerate domain,
\[
\Psi(w,A)=\frac{\sum_{i\ne j}w_iw_jA_{ij}}{\sum_{i\ne j}w_iw_j}.
\]
The coefficients \(w_iw_j/\sum_{k\ne\ell}w_kw_\ell\) are nonnegative and sum to one, so this is the weighted average of the entries \(A_{ij}\) over ordered pairs.

Now consider any index \(\Psi_D(w,M)=w^TMw/D(w)\) with \(D(w)>0\) on every simplex vector having at least two positive components. If the complete-network value is one for every such w, then
\[
1=\Psi_D(w,C)=\frac{w^TCw}{D(w)},
\]
so necessarily \(D(w)=w^TCw=1-\sum_iw_i^2\). Thus the 1-HHI denominator is unique (on its admissible domain).

Finally, let \(L=\sum_{i\ne j}A_{ij}\ge1\), \(\delta(A)=L/[n(n-1)]\),
\[
E_{\rm link}[w_iw_j]=\frac1L\sum_{i\ne j:A_{ij}=1}w_iw_j,
\quad
E_{\rm all}[w_iw_j]=\frac1{n(n-1)}\sum_{i\ne j}w_iw_j.
\]
The weighted-average formula gives
\[
\Psi(w,A)=\frac{\sum_{i\ne j:A_{ij}=1}w_iw_j}{\sum_{i\ne j}w_iw_j}
=\frac{L}{n(n-1)}\frac{E_{\rm link}[w_iw_j]}{E_{\rm all}[w_iw_j]}
=\delta(A)\frac{E_{\rm link}[w_iw_j]}{E_{\rm all}[w_iw_j]}.
\]
All denominators are positive by the stated nondegeneracy and \(L\ge1\), completing the proof.
