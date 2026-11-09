# Problem

## Setup

Fix one problem with binary answer space \(\mathcal A=\{a^*,a'\}\), where \(a^*\) is the correct answer. For each \(i\), draw an initial answer \(a_i\), then regenerate one continuation after a fixed prefix fraction \(\tau\in(0,1)\) to obtain \(\widetilde a_i\). The resulting pairs \((a_i,\widetilde a_i)\) are i.i.d. Let \(\pi(a)=\Pr(a_i=a)\). For every \(b\) with \(\pi(b)>0\), define
\[
T(b\to a)=\Pr(\widetilde a_i=a\mid a_i=b).
\]
If \(\pi(b)=0\), specify \(T(b\to\cdot)\) arbitrarily as a probability distribution on \(\mathcal A\). Thus \(T\) is a transition probability kernel on the entire answer space. Set
\[
r_C=T(a^*\to a^*),\qquad r_W=T(a'\to a'),\qquad r_C+r_W>0.
\]
For each candidate answer \(a\), define
\[
c_i(a)=\frac{\mathbf 1\{a_i=a\}+\mathbf 1\{\widetilde a_i=a\}}2.
\]
Fix \(w:[0,1]\to\mathbb R_{\ge 0}\) satisfying \(w(0)=0\) and \(w(1)>0\). Define \(V_N(a)=\sum_{i=1}^N w(c_i(a))\), and let the prefix-consistency-weighted estimator choose an answer maximizing \(V_N(a)\). Standard majority voting chooses an answer maximizing the number of initial samples equal to it. At ties, either maximizing answer may be selected using a measurable tie-breaking rule.

## Task

Prove that if
\[
\pi(a^*)>\frac{r_W}{r_C+r_W},
\]
then the prefix-consistency-weighted estimator converges almost surely to \(a^*\) as \(N\to\infty\). Moreover, show that
\[
\frac{r_W}{r_C+r_W}<\pi(a^*)\le\frac12
\]
is a nonempty regime in which this estimator is guaranteed to converge to the correct answer while standard majority voting has no almost-sure correct-selection guarantee, exactly when \(r_C>r_W\).
