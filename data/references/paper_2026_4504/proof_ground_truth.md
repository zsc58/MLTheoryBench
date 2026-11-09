# Reference Proof

## Scope and Source Repairs

The public task explicitly assumes the uniform continuity property used below. This proof does not derive that property from a Transformer architecture or claim to reconstruct the external continuity theorem cited by the source.

The source's supporting proof contains an incorrect signed estimate for the absolute log-perplexity discrepancy and does not choose its continuity tolerance in response to the desired discrepancy. The proof below repairs these locally by choosing a sufficiently small tolerance and using the probability floor to control logarithms. The source also applies a strict-margin lemma with a potentially non-strict margin; an application through that lemma must instead use, for example, half the available positive margin. The direct proof below avoids that strictness error.

## Proof Structure

The confidence hypothesis bounds the log-perplexity of every correct prefix. The assumed continuity property is applied to a one-bit perturbation of each sufficiently long prefix. The resulting greedy history is unchanged, so the perturbed input is copied incorrectly. The uniform probability lower bound and continuity control the log-probability discrepancy; averaging makes it smaller than the prescribed tolerance.

## Complete Proof

Write \(a_N=(a_1,\ldots,a_N)\). All probabilities are the model's raw probabilities on \(V=\{0,1,\mathtt{|}\}\); greedy selection is restricted to the two bits. A bit with probability greater than \(1/2\) is necessarily the unique greedy choice among those bits, since their probabilities have sum at most one.

By the confidence assumption, the greedy output on input \(a_N\) at every step is \(a_k\), since
\[
q_{a_N,k}(a_k)\ge 1-g>1/2.
\]
Consequently
\[
\operatorname{ppl}_T(a_N)\le -\log(1-g).
\]
This also shows that the confidence condition expressed along greedy histories agrees with the source condition expressed along the correct prefix history.

Fix \(\varepsilon>0\). Put \(L=-\log\lambda\), which is finite and nonnegative, and choose
\[
0<\eta<\min\{1/2-g,\lambda\varepsilon/2\}.
\]
The public continuity hypothesis gives a single \(\delta>0\), independent of input length and common history, for this \(\eta\). Choose an integer \(N_0\ge2\) such that
\[
1/N_0<\delta,\qquad L/N_0<\varepsilon/2.
\]

For any \(N\ge N_0\), let \(c_N\) equal \(a_N\) except at its first coordinate, which is flipped. These inputs have the same final bit and relative Hamming distance \(1/N<\delta\).

We prove inductively that greedy decoding on \(c_N\) produces \(a_1,\ldots,a_N\). At the empty history, continuity gives
\[
p_T(a_1\mid c_N\mathtt{|})
\ge p_T(a_1\mid a_N\mathtt{|})-\eta
\ge1-g-\eta>1/2.
\]
Thus its first greedy bit is \(a_1\). If its preceding output is \(a_1\cdots a_{k-1}\), the two runs have the same preceding history, and continuity gives
\[
p_T(a_k\mid c_N\mathtt{|}a_1\cdots a_{k-1})
\ge p_T(a_k\mid a_N\mathtt{|}a_1\cdots a_{k-1})-\eta
\ge1-g-\eta>1/2.
\]
Its next greedy bit is therefore \(a_k\). The entire output on \(c_N\) is \(a_N\ne c_N\), so \(c_N\) is not correctly copied.

For \(u,v\in[\lambda,1]\), integrating \(1/t\) between \(u\) and \(v\) gives
\[
|\log u-\log v|\le |u-v|/\lambda.
\]
For \(k\ge2\), the target bits agree and the histories just proved are common. Hence
\[
\left|\log q_{c_N,k}(a_k)-\log q_{a_N,k}(a_k)\right|
\le\eta/\lambda.
\]
At the first coordinate the two target bits differ, but both log probabilities belong to \([\log\lambda,0]\), so their absolute difference is at most \(L\). Applying the triangle inequality to the two averaged sums yields
\[
\left|\operatorname{ppl}_T(c_N)-\operatorname{ppl}_T(a_N)\right|
\le\frac{(N-1)\eta/\lambda+L}{N}
\le\eta/\lambda+L/N
<\varepsilon.
\]
Combining this with the baseline bound proves
\[
\operatorname{ppl}_T(c_N)<-\log(1-g)+\varepsilon.
\]
The threshold was chosen before \(N\), and the construction works for every \(N\ge N_0\), as required.

## Obligation Closure

All obligations of the stated conditional task are derived above. No stochastic experiment, parameter-gradient result, or iso-perplexity result is used. There are no unresolved private proof obligations.
