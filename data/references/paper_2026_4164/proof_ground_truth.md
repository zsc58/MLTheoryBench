# Reference Proof

## Proof Structure

Use the independent split to condition on the score-learning information. Establish the randomized-rank identity under a fixed test-membership configuration as well as under a single null test event. Condition additionally on the unordered multiset of null scores to handle arbitrary ties. Compare the deterministic p-value with the randomized one. Finally, apply the standard fixed-null-set BY and BH theorems conditional on the test-membership configuration, then average.

## Complete Proof

Write \(W=(Z_{n+1},\ldots,Z_{n+m})\). If \(\Pr(Z=0)=0\), every test response belongs to the target set almost surely, so the FDR of either procedure is zero. The conditional null-validity statements have no positive-probability null event on which to be asserted. Henceforth suppose \(\Pr(Z=0)>0\).

### 1. Conditional null-score exchangeability

Fix a configuration \(w\in\{0,1\}^m\) with \(\Pr(W=w)>0\), and let
\[
I_0(w)=\{j:w_j=0\}.
\]
If this set is empty, the conditional false discovery proportion is zero. Otherwise fix \(j\in I_0(w)\).

Let \(\mathcal H\) contain the split, the score-learning observations, and any independent randomization used to learn the score. Conditional on \(\mathcal H\), the score is fixed. Because the partition is fixed or drawn independently of the observations, the remaining calibration and test observations have their original independent sampling laws before conditioning on their membership indicators.

Conditional on \(W=w\), the test observations remain mutually independent, with each observation having its distribution conditional on its specified membership indicator. In particular, \(X_{n+j}\) has law \(P_{X\mid Z=0}\). This conditioning does not alter the calibration or score-learning laws.

Conditional additionally on a calibration membership pattern \(C_0=C\), the covariates \(X_i\), \(i\in C\), are independent draws from \(P_{X\mid Z=0}\), independent of \(X_{n+j}\). Consequently, conditional on \(\mathcal H\), \(W=w\), and \(N_0=k\), the \(k\) null calibration scores and the null test score are exchangeable. Indeed, each pattern with \(|C|=k\) gives the same product law for these scores when the calibration indices are listed in increasing order. Only conditioning events of positive probability and almost-sure values of the conditioned information are used.

### 2. Exact randomized validity, including ties

Under this conditional law, write
\[
B_j=\#\{i\in C_0:s(X_i)>s(X_{n+j})\},\qquad
E_j=\#\{i\in C_0:s(X_i)=s(X_{n+j})\}.
\]
Then
\[
\widetilde p_j=\frac{B_j+U_j(1+E_j)}{k+1}.
\]
Condition further on the unordered multiset of the \(k+1\) scores. Let its distinct values, ordered from largest to smallest, have multiplicities \(r_1,\ldots,r_L\), and put \(b_\ell=\sum_{h<\ell}r_h\). Exchangeability implies that the distinguished test score belongs to block \(\ell\) with conditional probability \(r_\ell/(k+1)\).

On this event, \(B_j=b_\ell\) and \(1+E_j=r_\ell\). Independence of \(U_j\) from all information used to construct the scores therefore makes \(\widetilde p_j\) uniform on
\[
\left[\frac{b_\ell}{k+1},\frac{b_\ell+r_\ell}{k+1}\right].
\]
These intervals cover \([0,1]\), overlap only at endpoints, and have lengths equal to their mixture probabilities. Their mixture is exactly uniform on \([0,1]\). Averaging over the multiset gives
\[
\Pr(\widetilde p_j\le t\mid\mathcal H,W=w,N_0=k)=t,
\qquad 0\le t\le1.
\]
For \(k=0\), this also follows immediately from \(\widetilde p_j=U_j\).

Average over \(\mathcal H\) and then over configurations \(w\) with \(w_j=0\), retaining the conditioning on \(N_0\). This proves
\[
\Pr(\widetilde p_j\le t\mid Z_{n+j}=0,N_0)=t
\]
almost surely under the null-event law, as required.

### 3. Conservative deterministic validity

Pointwise,
\[
p_j=\frac{1+B_j+E_j}{N_0+1}
\ge\frac{B_j+U_j(1+E_j)}{N_0+1}
=\widetilde p_j,
\]
since \(0\le U_j\le1\). It follows that
\[
\Pr(p_j\le t\mid\mathcal H,W=w,N_0=k)\le t.
\]
Averaging proves both the stated marginal null validity
\[
\Pr(p_j\le t\mid Z_{n+j}=0)\le t
\]
and the configuration-wise validity needed below:
\[
\Pr(p_j\le t\mid W=w)\le t\quad\text{for every }j\in I_0(w).
\]
When \(N_0=0\), the deterministic p-values all equal one, which is consistent with these inequalities.

### 4. Multiple testing under a fixed null configuration

The audited standard-independent multiple-testing results are as follows. For a vector \(P\in[0,1]^m\) with a fixed null set \(I_0\), assume \(\Pr(P_i\le t)\le t\) for every \(i\in I_0\) and \(t\in[0,1]\). BY with critical values \(qr/(mc_m)\) controls
\[
\mathbb E\left[\frac{|S\cap I_0|}{1\vee|S|}\right]\le\frac{q|I_0|}{m}
\]
under arbitrary joint dependence. BH with critical values \(qr/m\) has the same bound if the full vector is PRDS on \(I_0\), with PRDS defined in the task. These statements also apply under a conditional probability law when their hypotheses hold under that law.

Apply BY under the law conditional on \(W=w\). The null set \(I_0(w)\) is now fixed, all p-values lie in \([0,1]\), and the preceding step verifies super-uniformity for every null coordinate under this same law. No dependence hypothesis is required. Thus
\[
\mathbb E\left[\left.\frac{|S_{\rm BY}\cap I_0(w)|}{1\vee|S_{\rm BY}|}\right|W=w\right]
\le \frac{q|I_0(w)|}{m}\le q.
\]
For BH, the task's PRDS assumption supplies the remaining hypothesis under precisely the law conditional on \(W=w\). Hence
\[
\mathbb E\left[\left.\frac{|S_{\rm BH}\cap I_0(w)|}{1\vee|S_{\rm BH}|}\right|W=w\right]
\le \frac{q|I_0(w)|}{m}\le q.
\]
Neither application assumes PRDS conditional on \(\mathcal H\), \(N_0\), or the realized calibration scores. The marginal validity used here has already been averaged over that information.

Finally average over \(W\). Since \(I_0(W)\) is exactly the set of test responses outside the target set, the resulting expectations are the FDRs defined in the task. This proves both conclusions.

## Obligation Closure

The conditional sampling law and null exchangeability are derived from the stated i.i.d. model and independent split. Exact randomized validity is derived by conditioning on the unordered score multiset. Deterministic validity follows from a pointwise inequality. The random-null-set issue is resolved by configuration-wise conditional validity. The final two bounds use the explicitly stated standard-independent BY and PRDS-BH results with all hypotheses verified. No unresolved proof obligation remains.
