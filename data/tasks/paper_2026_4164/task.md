# Problem

## Setup

Let \((X,Y)\) have distribution \(P_{XY}\), and fix a measurable target set \(A\) in the response space and a level \(q\in(0,1)\). Write \(Z=\mathbf 1\{Y\in A\}\).

Let \(n\) be the finite number of labeled observations and let \(m\ge1\) be an integer. All pairs \((X_i,Y_i)\), \(1\le i\le n+m\), including the unobserved test responses, are mutually i.i.d. draws from \(P_{XY}\). Write \(Z_i=\mathbf 1\{Y_i\in A\}\). The labeled indices \(\{1,\ldots,n\}\) are partitioned into disjoint score-learning and calibration samples. The partition is fixed independently of the observations, or drawn using randomization independent of them. The test covariates \(X_{n+1},\ldots,X_{n+m}\) are observed while their responses are hidden.

A measurable real-valued score \(s:\mathcal X\to\mathbb R\) is constructed measurably using only the score-learning data and, if needed, auxiliary randomization independent of all observations and the split. It uses neither calibration observations nor test covariates or responses.

Let
\[
C_0=\{i\text{ in the calibration sample}:Y_i\notin A\},\qquad N_0=|C_0|.
\]
For each test index \(j\in\{1,\ldots,m\}\), define
\[
p_j=\frac{1+\#\{i\in C_0:s(X_i)\ge s(X_{n+j})\}}{N_0+1}.
\]
Let each \(U_j\sim\mathrm{Unif}[0,1]\) be independent of all observations and all randomization used for splitting or score learning, and define
\[
\widetilde p_j=
\frac{\#\{i\in C_0:s(X_i)>s(X_{n+j})\}
+U_j\bigl(1+\#\{i\in C_0:s(X_i)=s(X_{n+j})\}\bigr)}{N_0+1}.
\]

Assume that, conditional on \(Y\notin A\), the covariates of all calibration observations in \(C_0\) and any test observation whose response is outside \(A\) are exchangeable.

For a selected set \(S\subseteq\{1,\ldots,m\}\), define
\[
\operatorname{FDR}(S)=\mathbb E\left[\frac{\#\{j\in S:Y_{n+j}\notin A\}}{1\vee |S|}\right],
\]
where \(a\vee b=\max\{a,b\}\).

For ordered p-values \(p_{(1)}\le\cdots\le p_{(m)}\), BH at level \(q\) rejects all \(p_j\le q\widehat r/m\), where \(\widehat r\) is the largest \(r\in\{1,\ldots,m\}\) such that \(p_{(r)}\le qr/m\), with no rejection if no such \(r\) exists. BY is the same procedure with \(q\) replaced by \(q/c_m\), where \(c_m=\sum_{r=1}^m1/r\).

For a random vector \(P\in[0,1]^m\) and a fixed index set \(I_0\), PRDS on \(I_0\) means the following: for every coordinatewise increasing Borel set \(D\subseteq[0,1]^m\) and every \(i\in I_0\), the conditional probability \(\Pr(P\in D\mid P_i=u)\) admits a version nondecreasing in \(u\) on the support of \(P_i\). A set is coordinatewise increasing if \(x\in D\) and \(y\ge x\) coordinatewise imply \(y\in D\).

Here null membership is random. Accordingly, the PRDS condition in the claim below means that, for every \(w\in\{0,1\}^m\) with positive probability for \(W=(Z_{n+1},\ldots,Z_{n+m})\), the law of the full vector \((p_1,\ldots,p_m)\) conditional on \(W=w\) is PRDS on \(I_0(w)=\{j:w_j=0\}\).

Conditional statements involving a null event are asserted only when that event has positive probability. Statements additionally conditional on \(N_0\) hold almost surely under that null-event conditional law.

## Task

Prove the following integrated claim. For every test index \(j\) and every \(t\in[0,1]\),
\[
\Pr\!\left(p_j\le t\mid Y_{n+j}\notin A\right)\le t,
\]
and, conditional also on \(N_0\),
\[
\Pr\!\left(\widetilde p_j\le t\mid Y_{n+j}\notin A,N_0\right)=t.
\]
Consequently, applying BY at level \(q\) to \((p_1,\ldots,p_m)\) controls FDR at most \(q\) under arbitrary dependence. Applying BH at level \(q\) also controls FDR at most \(q\) whenever the p-values satisfy the PRDS condition defined above.
