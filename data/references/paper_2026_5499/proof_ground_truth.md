# Reference Proof

## Proof Structure

We establish conditional pair-test guarantees from fresh Bernoulli observations, including an explicit expected stopping-time bound. We then prove tournament correctness and cost with integer rounding retained. The sibling blocks partition the real arms, allowing capture of the Condorcet arm at its unique entry level and preservation through the entry merge and every later merge. Finally, the capacity-weighted confidence allocation and the merge-cost calculation give the required unconditional linear-in-N expectation.

## Complete Proof

### step_001: Conditional concentration

Condition on the history immediately before a PairTest invocation and on its ordered input pair. Those inputs are then fixed. The fresh-observation model makes the potential observations for this call an iid Bernoulli sequence with mean \(p=\pi_{u,v}\). An infinite potential sequence may be used for analysis; samples after stopping are not observed by the procedure.

The standard independent result used here is Bernoulli Hoeffding concentration: for independent Bernoulli variables of common mean p, their empirical mean \(\widehat\pi_n\), and \(x>0\),
\[
\Pr(\widehat\pi_n-p\ge x)\le e^{-2nx^2},\qquad
\Pr(\widehat\pi_n-p\le-x)\le e^{-2nx^2}.
\]
Consequently the two-sided probability is at most \(2e^{-2nx^2}\). Its independence, boundedness, and common-mean hypotheses hold after the above conditioning. This is the external standard-independent dependency theory_030, used by the source at L000314-L000316 and L000347-L000349.

With the prescribed radius,
\[
\Pr\{|\widehat\pi_n-p|\ge c(n,\delta)\}
\le\frac{\delta}{n(n+1)}.
\]
A union bound and the telescoping identity \(\sum_{n\ge1}1/[n(n+1)]=1\) show that
\[
\mathcal E_\delta:=\{\forall n\ge1:\ |\widehat\pi_n-p|<c(n,\delta)\}
\]
has conditional probability at least \(1-\delta\). The same assertion therefore holds unconditionally.

### step_002: Pair-test correctness

Suppose \(p=1/2+\gamma\), where \(\gamma>0\). If the test returns v at time \(\tau\), then \(\widehat\pi_\tau<1/2-c(\tau,\delta)\), implying
\[
p-\widehat\pi_\tau>\gamma+c(\tau,\delta)>c(\tau,\delta).
\]
This contradicts \(\mathcal E_\delta\). Moreover, on that event the test does stop: since \(c(n,\delta)\to0\), choose n with \(c(n,\delta)<\gamma/2\). If it has not already stopped, then
\[
\widehat\pi_n-1/2>\gamma-c(n,\delta)>c(n,\delta),
\]
forcing stopping at or before n. The opposite sign of \(p-1/2\) is symmetric. Thus the conditional probability of returning the better arm is at least \(1-\delta\). The next step also proves almost-sure termination without conditioning on \(\mathcal E_\delta\).

### step_003: Explicit stopping-time bound

Let \(\gamma=|p-1/2|\in(0,1/2]\) and
\[
A=\log(1/\delta)+\log(1/\gamma)+1,\qquad
n_0=\left\lceil64A/\gamma^2\right\rceil.
\]
We verify \(c(n,\delta)\le\gamma/2\) for every \(n\ge n_0\). Write \(a=\log(1/\delta)\) and \(d=\log(1/\gamma)\), so \(A=a+d+1\ge1\). Since \(n_0\le128A/\gamma^2\),
\[
\begin{aligned}
\log(4/\delta)+2\log n_0
&\le16\log2+a+2\log A+4d\\
&\le(16\log2+6)A
<32A
\le n_0\gamma^2/2.
\end{aligned}
\]
Here \(a+4d\le4A\) and \(\log A\le A\). The function
\[
f(x)=x\gamma^2/2-2\log x-\log(4/\delta)
\]
has nonnegative derivative for \(x\ge4/\gamma^2\), which includes \([n_0,\infty)\). Hence, using \(n+1\le2n\),
\[
\log(2n(n+1)/\delta)\le\log(4/\delta)+2\log n\le n\gamma^2/2
\]
for every \(n\ge n_0\), proving the desired radius bound.

For \(p=1/2+\gamma\), nontermination by n implies
\[
\{\tau>n\}\subseteq\{|\widehat\pi_n-1/2|\le c(n,\delta)\}
\subseteq\{\widehat\pi_n-p\le-\gamma/2\}.
\]
Therefore \(\Pr(\tau>n)\le e^{-n\gamma^2/2}\) for \(n\ge n_0\). The other sign uses the upper-tail version. The tail-sum formula gives
\[
\mathbb E\tau\le n_0+\sum_{n\ge n_0}e^{-n\gamma^2/2}
\le n_0+4/\gamma^2
\le69A/\gamma^2,
\]
where \(1-e^{-x}\ge x/2\) for \(0<x\le1\) bounds the geometric tail. In particular, \(\tau<\infty\) almost surely.

Every distinct-arm pair has \(\gamma\ge\Delta\), so, with a universal constant \(C_{dt}\),
\[
\mathbb E[\tau\mid\text{pre-call history}]
\le C_{dt}\Delta^{-2}\bigl(\log(1/\delta)+\log(1/\Delta)+1\bigr).
\]
This is a conditional bound for adaptively selected inputs and an unconditional cost bound, not a bound restricted to successful tests.

### step_004: Knockout correctness and cost

Fix a nonempty candidate set S of size m and \(\delta\in(0,1)\). A singleton returns its only member with zero comparisons. For \(m\ge2\), consider a member w that beats all other members, if such a member exists. In each round r, w participates in at most one test. Conditional on the history immediately before that test, its chance of losing is at most \(\delta_r\), by step_002. If it receives a bye, its elimination probability is zero. Hence
\[
\Pr(w\text{ is eliminated})\le\sum_{r\ge1}\frac{6\delta}{\pi^2r^2}=\delta.
\]
If never eliminated, w is the returned representative. No independence between elimination events is required.

For cost, let \(R=\lceil\log_2m\rceil\), let \(X_{r-1}\) be the active set before round r, and let \(K_r\) be its number of tests. The size recursion is deterministic:
\[
|X_{r-1}|=\left\lceil m/2^{r-1}\right\rceil,\qquad
K_r=\left\lfloor |X_{r-1}|/2\right\rfloor\le m/2^r+1/2.
\]
For \(1\le r\le R\), \(2^r\le2^R<2m\), so
\[
K_r\le2m/2^r.
\]
The stronger unrounded claim \(K_r\le m/2^r\) is not valid for arbitrary m and is not used. Exactly one arm is removed per test, so \(\sum_{r=1}^R K_r=m-1\). Also,
\[
\sum_{r=1}^R K_r\log r
\le2m\sum_{r\ge1}\frac{\log r}{2^r}
\le2m\sum_{r\ge1}\frac{r}{2^r}=4m.
\]
The last series is obtained from the geometric series. All these counts hold independently of the duel outcomes.

By step_003, conditioning before each test and then taking expectations, the expected cost of a round-r test is at most a universal multiple of
\[
\Delta^{-2}\bigl(\log(1/\delta)+2\log r+\log(1/\Delta)+1\bigr).
\]
Here the constant \(\log(\pi^2/6)\) in \(\log(1/\delta_r)\) is absorbed into the universal constant. Summation using the two preceding count bounds yields
\[
\mathbb E[\mathrm{cost}(\mathrm{Knockout}(S,\delta))]
\le C_{bkt}m\Delta^{-2}\bigl(\log(1/\delta)+\log(1/\Delta)+1\bigr).
\]
This cost bound requires no dominant arm in S and also covers m=1. Each tournament terminates almost surely. The same conclusions hold conditionally on a pre-tournament history that fixes S, because all subsequent samples are fresh.

### step_005: Tree geometry, domains, and execution

Let \(m_h=|Q_h(b)|\). The two child subtrees of each ancestor give
\[
U_h(b)=U_{h-1}(b)\sqcup Q_h(b).
\]
Iterating from \(U_0(b)=\{b\}\) to \(U_L(b)=[N]\) proves
\[
[N]=\{b\}\sqcup\bigsqcup_{h=1}^LQ_h(b),\qquad
\sum_hm_h=N-1.
\]
The completed bracket has \(2^{h-1}\) positions in the sibling subtree at level h, so
\[
0\le m_h\le\bar m_h=2^{h-1},\qquad
\sum_h\bar m_h=M-1.
\]
These are derived facts, not additional assumptions on the public task.

Because \(N\ge2\), we have \(M\ge2\) and \(L\ge1\). Thus every \(\beta_h\) and \(\eta_h\) is positive and less than 1. Tournament round confidences also lie in (0,1). Empty blocks are skipped, and singleton tournaments use no pair tests.

Inductively, the incumbent after level h belongs to \(U_h(b)\). Therefore an incumbent before a nonempty merge and the representative from \(Q_h(b)\) are distinct real arms. No pair test compares an arm with itself or with a formal bye. A completed level with \(m_h>0\) uses \(m_h-1\) tournament pair tests and one merge pair test. Thus the execution has exactly \(N-1\) pair-test calls on termination; induction over this finite execution and step_003 show that it terminates almost surely.

Define privately for the analysis \(h_* =0\) if \(b=w^*\); otherwise let \(h_*\) be the unique level whose sibling block contains \(w^*\). Its existence and uniqueness follow from the proved partition.

### step_006: Capture and preservation, including the entry merge

If \(h_*=0\), the initial incumbent is \(w^*\). If every invoked merge containing it returns it, empty levels carry it forward and all other levels preserve it.

If \(h_*>0\), suppose the tournament on \(Q_{h_*}(b)\) returns \(w^*\). At this point it is a representative, not yet necessarily the incumbent. The merge at level \(h_*\) must also return \(w^*\); this makes it the incumbent at that level. Thereafter, empty levels carry it forward, and any invoked merge containing it preserves it when that merge is correct. Thus it suffices that the capture tournament succeeds and all invoked merges containing \(w^*\) at levels \(h\ge\max\{1,h_*\}\), including the entry level, return it. No correctness is required of earlier merges or of tournaments on blocks lacking \(w^*\).

### step_007: Total success probability

If \(h_*>0\), \(w^*\) dominates every other member of its entry block. By step_004 and conditioning on the history before the block tournament, its capture failure probability is at most \(\beta_{h_*}\). If \(h_*=0\), there is no capture failure.

For each level h, let \(F_h\) be the event that a merge is invoked with \(w^*\) as an input but returns the other input. Conditional on the history after the block tournament and before the prospective merge, the invocation status and inputs are fixed. Step_002 and fresh samples give \(\Pr(F_h)\le\eta_h\); for an empty block \(F_h\) is impossible. Step_006 therefore implies
\[
\begin{aligned}
\Pr(\mathrm{output}\ne w^*)
&\le\mathbf1\{h_*>0\}\beta_{h_*}+\sum_{h=1}^L\eta_h\\
&\le\sum_{h=1}^L\beta_h+\sum_{h=1}^L\eta_h\\
&=\frac{\varepsilon}{2}\frac{M-1}{M-1}+\frac{\varepsilon}{2}
=\varepsilon.
\end{aligned}
\]
This includes the case \(b=w^*\), empty blocks, and singleton capture tournaments.

### step_008: Unconditional expected comparison count

Let \(T_h^{sub}\) and \(T_h^{merge}\) count elementary comparisons in the level-h tournament and merge, respectively, with both zero for an empty block. Then the total count is their finite sum. Step_004 gives
\[
\sum_h\mathbb E T_h^{sub}
\le C_{bkt}\Delta^{-2}\sum_hm_h\bigl(\log(1/\beta_h)+\log(1/\Delta)+1\bigr).
\]
The confidence-dependent sum is
\[
\sum_hm_h\log(1/\beta_h)
=(N-1)\log(2/\varepsilon)+\sum_hm_h\log\frac{M-1}{\bar m_h}.
\]
All logarithms in the last sum are nonnegative, so the capacity bound implies
\[
\begin{aligned}
\sum_hm_h\log\frac{M-1}{\bar m_h}
&\le\sum_{h=1}^L2^{h-1}(L-h+1)\log2\\
&=M\log2\sum_{j=1}^L\frac{j}{2^j}
\le2M\log2.
\end{aligned}
\]
Consequently the tournament contribution is at most
\[
C M\Delta^{-2}\bigl(\log(1/\varepsilon)+\log(1/\Delta)+1\bigr).
\]

There are at most L merges. Their inputs can be random, but the conditional bound in step_003 applies before each fresh test. Taking expectations yields
\[
\sum_h\mathbb E T_h^{merge}
\le C L\Delta^{-2}\bigl(\log(2L/\varepsilon)+\log(1/\Delta)+1\bigr).
\]
Here \(L\le M\) and \(L\log(2L)\le4M\): indeed \(\log(2L)\le2L\) and \(L^2\le2^{L+1}\), the latter checked at L=1,2,3 and then proved by induction. Expanding \(\log(2L/\varepsilon)\) therefore bounds the merge contribution by the same M-linear expression.

Finally \(N\le M<2N\), so adding the two contributions gives
\[
\mathbb E[\mathrm{comparisons}]
\le C N\Delta^{-2}\bigl(\log(1/\varepsilon)+\log(1/\Delta)+1\bigr).
\]
The numerical constants are independent of the preference matrix, fixed bracket and placement, starting arm, confidence, and N. The calculation does not condition on successful identification, so it includes all failure paths.

## Obligation Closure

Steps step_001 through step_008 close, respectively, the concentration, pair correctness, boundary inversion and integrability, rounded tournament analysis, geometric and algorithmic definition closure, deterministic capture, probabilistic correctness, and unconditional comparison-cost obligations. The only external probabilistic input is the explicitly stated standard-independent Bernoulli Hoeffding inequality, whose hypotheses are checked in step_001. The remaining series and estimates are elementary and displayed above. The source's partition and complete algorithm definitions are retained as theory_010 and theory_011, and the concentration dependency as theory_030. There is no unresolved private proof obligation.
