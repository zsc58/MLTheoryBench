# Reference Proof

## Proof Structure

Prove both directions. Separation at the distance of any distinct pair yields injectivity. Conversely, for each fixed threshold, use compactness of the set of pairs at least that far apart and continuity plus injectivity to obtain a positive minimum of the distance ratio.

## Audited Background

The standard independent facts used are: the distance function of a metric space is jointly continuous; a finite product of compact spaces is compact; a closed subset of a compact space is compact; and a continuous real-valued function on a nonempty compact space attains its minimum. For the first fact, the triangle inequality gives
\[
|d(a,b)-d(a',b')|\le d(a,a')+d(b,b').
\]
The hypotheses of the compactness and minimum facts are checked in the proof below. The Riemannian distance on the connected domain is a finite metric inducing its manifold topology.

## Complete Proof

Assume first that for every delta>0 there is epsilon>0 such that f is (delta,epsilon)-separated. If x,y are distinct, set delta=d_M(x,y)>0. Then
\[
\frac{d_N(f(x),f(y))}{d_M(x,y)}>\epsilon,
\]
so d_N(f(x),f(y))>0 and f(x)\ne f(y). Thus f is injective.

Conversely, assume f is continuous and injective. Fix delta>0 and let
\[
C_\delta=\{(x,y)\in M\times M:d_M(x,y)\ge\delta\}.
\]
If C_delta is empty, any epsilon>0 gives separation for this delta. Otherwise, M x M is compact, and C_delta is compact because it is closed. On C_delta the denominator is positive. The function
\[
q(x,y)=\frac{d_N(f(x),f(y))}{d_M(x,y)}
\]
is continuous, since f and the metrics are continuous. Injectivity gives d_N(f(x),f(y))>0 on C_delta, so q is positive there. It therefore attains a positive minimum r. Taking epsilon=r/2, every pair with d_M(x,y)\ge delta satisfies q(x,y)\ge r>epsilon, hence f is (delta,epsilon)-separated. Since delta was arbitrary, the separation property holds for every positive delta.

Therefore f is injective if and only if it satisfies the stated separation condition.

## Closed Proof Obligations

1. For each distinct pair, its finite positive distance is an admissible threshold, and separation makes its image distance positive.
2. For an arbitrary positive threshold, the empty pair set gives vacuous separation; otherwise the pair set is a closed subset of the compact product.
3. On the nonempty pair set, the denominator is at least delta>0, and the ratio is continuous and strictly positive.
4. The minimum theorem applies to this nonempty compact set. The attained minimum is positive because the ratio is positive at the minimizing pair.
5. Choosing epsilon=r/2 yields a strict bound simultaneously for all eligible pairs. Epsilon may depend on delta and the fixed map and metric spaces; it need not work for every delta at once.

## Private Source Audit

The source's standing connectedness assumption at L000017 is retained in the public setup. The source proof at L000275–L000278 invokes a minimizing pair without first treating C_delta=empty. The empty-set branch already present in this reference proof is the local repair recorded under theory_004. It covers thresholds exceeding the diameter and also all thresholds for a singleton domain. No restriction on the positive threshold range is introduced, and no unresolved proof obligation remains.
