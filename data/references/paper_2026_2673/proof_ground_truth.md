# Reference Proof

## Proof Structure

1. Apply the strong law to the two possible vote totals and identify their population limits.
2. Compute the population objective using the initial and regenerated answer marginals.
3. In the binary case, show that the pooled-mass and self-reproduction differences coincide, yielding the exact margin and threshold.
4. Use the strict margin for eventual almost-sure selection, and compare with standard majority voting, including the endpoint where the initial-answer probabilities are equal.

## Complete Proof

Let \(p=\pi(a^*)\) and \(q=1-p=\pi(a')\). For each sample, write \(a_i\) for the initial answer and \(\widetilde a_i\) for its regenerated answer. The pairs are i.i.d. For every initial state of positive probability, the conditional distribution of \(\widetilde a_i\) is the corresponding row of \(T\). A row on a null initial state is an arbitrarily specified probability distribution; products involving that row and its zero initial probability remain zero. Thus the joint and marginal calculations below also cover \(p=0\) or \(p=1\).

For \(a\in\{a^*,a'\}\), define
\[
c_i(a)=\frac{\mathbf 1\{a_i=a\}+\mathbf 1\{\widetilde a_i=a\}}2,
\qquad V_N(a)=\sum_{i=1}^N w(c_i(a)).
\]
The strong law used here states that the averages of i.i.d. integrable real random variables converge almost surely to their expectation. Its hypotheses hold because the summands are i.i.d. and take only the three finite values \(w(0),w(1/2),w(1)\). Consequently, simultaneously for both answers,
\[
N^{-1}V_N(a)\longrightarrow \Phi_w(a):=\mathbb E[w(c_i(a))]
\quad\text{almost surely}.
\]
Simultaneity follows by intersecting the two probability-one convergence events. No global measurability assumption on the arbitrary function \(w\) is needed: its composition here is a function of a finite-valued measurable score.

For an answer \(a\), let \(\pi^{\to}(a)=\Pr(\widetilde a_i=a)=\sum_b\pi(b)T(b\to a)\). The event \(c_i(a)=1\) has probability \(\pi(a)T(a\to a)\). The event \(c_i(a)=1/2\) has probability
\[
\pi(a)(1-T(a\to a))+\pi^{\to}(a)-\pi(a)T(a\to a)
=\pi(a)+\pi^{\to}(a)-2\pi(a)T(a\to a).
\]
The remaining probability is
\[
\Pr(c_i(a)=0)=1-\pi(a)-\pi^{\to}(a)+\pi(a)T(a\to a).
\]
Using \(w(0)=0\), therefore
\[
\Phi_w(a)=w(1/2)[\pi(a)+\pi^{\to}(a)]+[w(1)-2w(1/2)]\pi(a)T(a\to a).
\]

Set \(D=pr_C-qr_W\), where \(r_C=T(a^*\to a^*)\) and \(r_W=T(a'\to a')\). Each row of \(T\) is a probability distribution on the binary answer space, so the regenerated probabilities are
\[
\pi^{\to}(a^*)=pr_C+q(1-r_W),\qquad
\pi^{\to}(a')=p(1-r_C)+qr_W.
\]
Consequently,
\[
[\pi(a^*)+\pi^{\to}(a^*)]-[\pi(a')+\pi^{\to}(a')]=2D,
\]
and
\[
\pi(a^*)T(a^*\to a^*)-\pi(a')T(a'\to a')=D.
\]
Substituting these identities into the preceding decomposition gives the exact population margin
\[
\Phi_w(a^*)-\Phi_w(a')
=\bigl(2w(1/2)+w(1)-2w(1/2)\bigr)D
=w(1)D.
\]
In particular, this calculation does not require \(w(1)-2w(1/2)\ge0\). Since \(w(1)>0\), the correct answer is the unique population maximizer whenever \(D>0\). As \(r_C+r_W>0\), this is equivalent to
\[
p>\frac{r_W}{r_C+r_W}.
\]
Under this strict inequality the population margin is positive. On the simultaneous strong-law event,
\[
\frac{V_N(a^*)-V_N(a')}{N}\longrightarrow w(1)D>0.
\]
Eventually the normalized difference exceeds \(w(1)D/2\), and hence \(V_N(a^*)>V_N(a')\). Every permitted maximizing selection therefore eventually equals \(a^*\), independently of its choices at earlier ties. This proves almost-sure convergence of the prefix-consistency-weighted estimator to \(a^*\).

For standard majority voting, the initial-answer indicators are i.i.d. bounded random variables. The strong law gives empirical initial-answer frequencies converging almost surely to \(p\) and \(q\). If \(p>1/2\), eventually the correct answer has the strict majority, so standard majority voting converges almost surely to \(a^*\). If \(p<1/2\), eventually the wrong answer has the strict majority, so standard majority voting converges almost surely to \(a'\).

It remains to justify the comparison at \(p=1/2\); a tied limiting frequency alone does not settle estimator convergence. For every odd \(N\), the initial counts cannot tie. Each initial-answer sequence of length \(N\) has probability \(2^{-N}\), and swapping \(a^*\) and \(a'\) gives a bijection between sequences with a strict correct majority and sequences with a strict wrong majority. Thus
\[
\Pr(\widehat a_N^{\mathrm{MV}}=a^*)=\frac12
\qquad\text{for every odd }N,
\]
regardless of the rule at ties for even sample sizes.

If standard majority voting converged almost surely to \(a^*\), it would eventually equal \(a^*\) almost surely because the answer space is finite and discrete. Let
\[
E_m=\{\widehat a_N^{\mathrm{MV}}=a^*\text{ for every }N\ge m\}.
\]
These events increase with \(m\), and eventual almost-sure correctness would imply \(\Pr(\bigcup_m E_m)=1\). Therefore \(\Pr(E_m)\to1\). For every \(N\ge m\), correct-selection probability is at least \(\Pr(E_m)\), which would force correct-selection probabilities to tend to one. This contradicts their value \(1/2\) along odd \(N\). Standard majority voting therefore has no almost-sure correct-selection guarantee at \(p=1/2\).

It follows that every \(p\) in
\[
\frac{r_W}{r_C+r_W}<p\le \frac12
\]
satisfies the prefix-consistency-weighted guarantee but not an almost-sure standard-MV correct-selection guarantee. Because the transition probabilities lie in \([0,1]\) and the denominator is positive, the interval is nonempty exactly when
\[
\frac{r_W}{r_C+r_W}<\frac12
\quad\Longleftrightarrow\quad r_C>r_W.
\]
In that case its length is
\[
\frac12-\frac{r_W}{r_C+r_W}
=\frac{r_C-r_W}{2(r_C+r_W)}>0.
\]

## Boundary Checks and Obligation Closure

The strict threshold cannot hold at \(p=0\). At \(p=1\), the null wrong-state row causes no problem; the strict threshold holds precisely when \(r_C>0\), and the same positive-margin proof applies. If \(r_C=0<r_W\), the threshold is one and no initial success probability satisfies it. If \(r_W=0<r_C\), the threshold is zero and every \(p>0\) satisfies it. The case \(r_C+r_W=0\) is excluded so the displayed ratio is defined. No PC-WMV convergence converse is asserted at equality with its threshold. Every theorem-critical obligation is derived above or follows from the stated strong law with its hypotheses verified; no unresolved private proof obligation remains.
