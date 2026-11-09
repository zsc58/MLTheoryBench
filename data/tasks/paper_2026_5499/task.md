# Problem

## Setup

Let \(N\ge2\) be an integer and \([N]=\{1,\ldots,N\}\) the set of real arms. The fixed preference probabilities satisfy \(\pi_{i,j}\in(0,1)\), \(\pi_{i,j}=1-\pi_{j,i}\), and \(\pi_{i,i}=1/2\). When an ordered pair of distinct arms \((i,j)\) is compared, the newly generated outcome, conditional on the preceding observation history and the selected pair, has distribution \(\mathrm{Bernoulli}(\pi_{i,j})\); outcome 1 means that i wins. Every subroutine uses fresh outcomes, not previously observed outcomes reused as samples.

Assume a unique Condorcet arm \(w^*\) satisfies \(\pi_{w^*,j}>1/2\) for every \(j\ne w^*\). Define the global gap
\[
\Delta:=\min_{i\ne j}|\pi_{i,j}-1/2|>0.
\]
All logarithms without a subscript are natural.

For distinct \(u,v\in[N]\) and \(\delta\in(0,1)\), each invocation of **PairTest(u,v,\(\delta\))** starts its own sample count at zero. Let \(\widehat\pi_n\) be the empirical mean of the first n outcomes generated in that invocation, with 1 indicating a win by u. Define, for integers \(n\ge1\),
\[
c(n,\delta):=\sqrt{\frac{\log(2n(n+1)/\delta)}{2n}}.
\]
PairTest samples the pair until the first n for which \(|\widehat\pi_n-1/2|>c(n,\delta)\), then returns u if \(\widehat\pi_n>1/2\) and v otherwise.

**Knockout(S,\(\delta\))**, for a nonempty set \(S\subseteq[N]\) and \(\delta\in(0,1)\), maintains active representatives, initially the members of S. In each round \(r=1,2,\ldots\), it pairs active representatives in a fixed deterministic order, runs PairTest on each pair with confidence \(\delta_r=6\delta/(\pi^2r^2)\), retains each winner and gives one representative a bye if needed, and repeats until one representative remains. That representative is returned. If S is a singleton, it is returned without comparisons.

Let \(M=2^{\lceil\log_2N\rceil}\) and \(L=\log_2M\). Fix a deterministic full balanced binary bracket with M leaf positions and a fixed placement of the N real arms in distinct positions, chosen without using comparison observations. The remaining positions are formal byes: they are not arms and generate no comparisons. Fix a starting arm \(b\in[N]\). Let \(U_h(b)\) be the real arms in the subtree of the ancestor h edges above the leaf containing b, with \(U_0(b)=\{b\}\). Define
\[
Q_h(b)=U_h(b)\setminus U_{h-1}(b),\qquad \bar m_h=2^{h-1},\qquad h=1,\ldots,L.
\]

**TreeIdentify(b,\(\varepsilon\))**, for \(\varepsilon\in(0,1)\), uses this fixed bracket and starts with incumbent b. At each level \(h=1,\ldots,L\), if \(Q_h(b)\) is nonempty, it runs Knockout\((Q_h(b),\beta_h)\), where
\[
\beta_h=\frac{\varepsilon}{2}\frac{\bar m_h}{M-1},
\]
and replaces the incumbent by the result of PairTest(incumbent, returned representative, \(\eta_h\)), where
\[
\eta_h=\frac{\varepsilon}{2L}.
\]
If \(Q_h(b)\) is empty, it carries the incumbent forward without comparisons. It returns the final incumbent.

## Task

Prove that, for every \(N\ge2\), every preference matrix satisfying the setup, every fixed bracket and arm placement described above, every starting arm b, and every \(\varepsilon\in(0,1)\), TreeIdentify\((b,\varepsilon)\) returns \(w^*\) with probability at least \(1-\varepsilon\), and its expected number of pairwise comparisons satisfies
\[
\mathbb E[\mathrm{comparisons}]\le C N\Delta^{-2}\bigl(\log(1/\varepsilon)+\log(1/\Delta)+1\bigr)
\]
for a universal constant C independent of N, the preference matrix, the bracket and arm placement, b, and \(\varepsilon\).
