# Problem

## Setup

Let \(\mathcal X\) be a Borel subset of a finite-dimensional normed space and let \(\mathcal Y\) be a finite label set of size \(m\ge2\). Let \(P\) be a joint distribution of \((X,Y,S)\), where \(X\in\mathcal X\), \(Y\in\mathcal Y\), and \(S\in2^{\mathcal Y}\). Bags need not contain the true label. We observe an infinite iid sequence \((X_i,S_i)\), but not the true labels. Assume the class of metric balls has finite VC dimension.

For measurable versions of the conditional probabilities, write
\[
q_y(x)=P(Y=y\mid X=x),\qquad
\eta_y(x)=P(y\in S\mid X=x).
\]
Call the distribution label-aligned when the following equality of sets holds for \(P_X\)-almost every \(x\):
\[
\operatorname*{argmax}_{y\in\mathcal Y}\eta_y(x)
=
\operatorname*{argmax}_{y\in\mathcal Y}q_y(x).
\]

Independently of the observations, assign iid priorities \(U_i\sim\mathrm{Uniform}(0,1)\). For a query \(x\), order the first \(n\) training observations by increasing \((\|X_i-x\|,U_i)\), using the priorities only to resolve equal distances. Let \(S_{(i)}(x)\) denote the bag of the \(i\)-th observation in this order, and define
\[
\widehat\eta_{n,k}(y\mid x)
=\frac1k\sum_{i=1}^{k}\mathbf1\{y\in S_{(i)}(x)\}.
\]

For a fixed constant \(c_1>0\), define
\[
\Delta(n,k,\delta)
=c_1\sqrt{\frac{\log n+\log(m/\delta)}{k}}.
\]
The classifier starts with every label active. At iteration \(k=1,2,\ldots\), simultaneously remove each active label \(y\) for which
\[
\max_{z\text{ active}}\widehat\eta_{n,k}(z\mid x)
-\widehat\eta_{n,k}(y\mid x)
\ge\Delta(n,k,\delta_n).
\]
Stop only when a single active label remains or iteration \(T_n\) has been completed. Output any remaining active label, using a measurable selection based only on the observed training sample, priorities, and query. Denote the resulting classifier by \(\widehat h_n\).

The deterministic schedules satisfy \(\delta_n\in(0,1)\), \(T_n\in\{1,\ldots,n\}\), and, for some fixed \(A\in(0,1]\),
\[
T_n\ge An,\qquad
\sum_{n=1}^{\infty}\delta_n<\infty,\qquad
\frac{\log(1/\delta_n)}{T_n}\longrightarrow0.
\]
For a realized measurable classifier \(h\), define its risk using an independent test pair by
\[
R(h)=P(h(X)\ne Y),\qquad
R^*=\inf_{h:\mathcal X\to\mathcal Y\text{ measurable}}R(h).
\]

## Task

Prove that there is a numerical constant \(c_*>0\), independent of the distribution, label-set size, ambient dimension, and schedules, such that for every fixed \(c_1\ge c_*\) the classifier is almost surely Bayes consistent for every label-aligned distribution:
\[
R(\widehat h_n)\longrightarrow R^*.
\]
The almost-sure assertion is with respect to the common infinite training sequence and the independent priorities. It must hold for every measurable final selection allowed above.

Also prove the following minimality statement. There exist two distributions \(P_1,P_2\) in this observation model with identical observable laws
\[
P_1^{X,S}=P_2^{X,S},
\]
with disjoint Bayes-optimal label sets on a set of positive common \(P_X\)-measure, and with \(P_2\) label-aligned. Consequently, no algorithm using only observable \((X,S)\) samples, with any distribution-independent internal randomization, can be Bayes consistent on the full class in this model or on any class containing both \(P_1\) and \(P_2\).
