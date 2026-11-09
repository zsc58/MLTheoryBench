# Reference Proof

## Proof Structure

For each pivot and label subset, express the shifted logit discrepancy as a shifted-unembedding matrix applied to the representation residual defined by the corresponding linear map. A combinatorial averaging identity converts the average squared shifted discrepancies into the squared logit distance. Singular-value bounds for every shifted-unembedding matrix then give the two-sided comparison with the representation dissimilarity. All integration uses nonnegative measurable functions, so infinite distances are allowed.

## Complete Proof

Write Delta(x) = u(x) - u'(x), where u and u' are the centered k-dimensional logit vectors. For a pivot i and a subset J of m labels not containing i, let L = L_{i,J} and L' = L'_{i,J}. By definition, the coordinate indexed by j of L^T f(x) is (g(j)-g(i))^T f(x), and likewise for L'. Hence

L^T f(x) - L'^T f'(x) = L^T (f(x) - A_{i,J} f'(x)),

because A_{i,J} = L^{-T}L'^T and therefore L^T A_{i,J} = L'^T. The coordinate indexed by j is Delta_j(x)-Delta_i(x).

For fixed i, there are binom(k-1,m) admissible subsets J. Each j different from i belongs to binom(k-2,m-1) of them. Their ratio is m/(k-1), including when m=k-1. Therefore, pointwise in x,

average_J ||L_{i,J}^T(f-A_{i,J}f')||^2
 = (m/(k-1)) sum_{j != i} (Delta_j-Delta_i)^2.

Since both logit vectors are centered, sum_j Delta_j = 0. Expanding the finite double sum gives

sum_i sum_{j != i} (Delta_j-Delta_i)^2
 = sum_i sum_j (Delta_j-Delta_i)^2
 = 2k sum_j Delta_j^2 - 2(sum_j Delta_j)^2
 = 2k ||Delta||^2.

Averaging the subset identity over the k pivots yields the pointwise identity

average_{i,J} ||L_{i,J}^T(f-A_{i,J}f')||^2
 = (2m/(k-1)) ||Delta||^2.

The embeddings are measurable and all matrices are fixed and finite. Thus the squared norms are nonnegative measurable functions. Integration commutes with this finite average, even when the resulting integrals are infinite. We obtain

average_{i,J} E ||L_{i,J}^T(f-A_{i,J}f')||^2
 = (2m/(k-1)) d_logit^2.

There are finitely many admissible pairs (i,J), and at least one because 1 <= m <= k-1. Every L_{i,J} is an invertible finite m-by-m matrix. Consequently

0 < sigma_min <= sigma_max < infinity.

For completeness, write an SVD L=UDV^T, with U,V orthogonal and D diagonal with positive entries s_1,...,s_m. For any r in R^m,

||L^T r||^2 = ||DU^T r||^2 = sum_{a=1}^m s_a^2 (U^T r)_a^2.

Since sigma_min <= s_a <= sigma_max and ||U^T r||=||r||, this proves

sigma_min^2 ||r||^2 <= ||L_{i,J}^T r||^2 <= sigma_max^2 ||r||^2

for every residual r and every pair (i,J).

Apply these inequalities to r=f(x)-A_{i,J}f'(x), integrate, and average over all pairs. Using the preceding identity and the definition of d_rep gives

sigma_min^2 d_rep^2 <= (2m/(k-1)) d_logit^2 <= sigma_max^2 d_rep^2.

All constants are positive and finite. Division by these constants and taking nonnegative square roots are valid in [0,+infinity]. Setting C=sqrt(2m/(k-1)) therefore proves

(C/sigma_max) d_logit <= d_rep <= (C/sigma_min) d_logit.

This argument includes zero distances without division by a distance. It also includes infinite distances: the squared comparison forces either both distances to be finite or both to be infinite. No separate finite-moment assumption or subtraction of infinite integrals is used.

## Source Audit Notes

The source's weighted-residual argument is equivalent to the direct matrix argument above: with L=UDV^T and B=D^{-1}U^T, one has B^{-T}=DU^T and L^T=VDU^T, so ||B^{-T}r||=||L^T r||. The source's final supporting-identity display at L003778-L003779 must have expectation on both sides; its pointwise version is already stated at L003746. At L003929-L003930 the right side must be square-rooted along with the left, yielding sqrt(J/(2N)) d_rep. These local display repairs preserve the proof and theorem. The log-probability and Aitchison notation repairs recorded under theory_007 are not additional premises of this proof. All theorem-critical obligations are explicitly closed above.
