# Reference Proof

## Proof Structure

First check that the aggregation and confidence are well-defined even when the answer space is not finite. For a fixed threshold, compute the probabilities of retaining a correct and an erroneous vote. Conditional probability expresses selective accuracy as their ratio. Subtracting the baseline accuracy and using the definition of the survival gap gives an exact gain identity. Since the retained event has positive probability, its denominator is positive, so the sign of the gain is exactly the sign of the gap. This proves both the improvement and converse claims, pointwise in the threshold.

## Complete Proof

There are at most m answers with nonzero vote totals, since every nonzero total must belong to an answer output by a sampled path. All weights are positive finite real numbers, so the maximum vote total exists and
\[
\sum_{a\in\mathcal A}V_a=\sum_{i=1}^m w_i\in(0,\infty).
\]
Consequently, the chosen answer is well-defined under the fixed tie rule and \(0<C\le1\). The measurability assumptions make the probability events below well-defined. In particular, every positive threshold with positive retained probability is less than 1; thresholds at least 1 retain nothing.

Fix any \(\tau>0\) such that \(\Pr(C>\tau)>0\). Since \(0<p<1\), both correctness strata have positive probability, and their conditional survival probabilities are defined. By the definitions of \(p\), \(S_1\), and \(S_0\),
\[
\Pr(\hat A=T, C>\tau)=pS_1(\tau),
\qquad
\Pr(\hat A\ne T, C>\tau)=(1-p)S_0(\tau).
\]
The correctness and error events partition the sample space. Therefore
\[
A(\tau)=\Pr(\hat A=T\mid C>\tau)
 =\frac{pS_1(\tau)}{pS_1(\tau)+(1-p)S_0(\tau)}.
\]
The denominator is \(\Pr(C>\tau)>0\). Since \(D(\tau)=S_1(\tau)-S_0(\tau)\), we have \(S_0(\tau)=S_1(\tau)-D(\tau)\), and hence
\[
pS_1+(1-p)S_0=S_1-(1-p)D.
\]
Subtracting \(p\) from the conditional-accuracy expression gives
\[
A(\tau)-p
=\frac{pS_1-p[pS_1+(1-p)S_0]}{pS_1+(1-p)S_0}
=\frac{p(1-p)(S_1-S_0)}{pS_1+(1-p)S_0}
=\frac{p(1-p)D(\tau)}{S_1(\tau)-(1-p)D(\tau)}.
\]
Because \(0<p<1\) and the denominator is positive, the sign of \(A(\tau)-p\) is exactly the sign of \(D(\tau)\). Thus \(D(\tau)>0\) if and only if \(A(\tau)>p\); \(D(\tau)\le0\) gives \(A(\tau)\le p\); and equality occurs exactly when \(D(\tau)=0\). Applying this pointwise to every positive threshold with positive retained probability proves the final all-threshold statement.
