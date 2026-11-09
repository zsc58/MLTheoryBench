# Problem

## Setup

Fix a prediction target $i$. For each intervention $a$, let $Z_{a,i}\in\{0,1\}$ indicate whether $a$ affects target $i$; call $a$ safe when $Z_{a,i}=0$. Write $Y^{(a)}\in\mathbb R$ for the scalar outcome of this target and $X^{(a)}$ for its covariates. Let $\widehat f_i$ be a real-valued measurable predictor fitted using a separate training set of interventions.

Fix a selected calibration index set $C$ of size $n\ge1$, disjoint from the training interventions, and a test intervention $a^*$ outside both sets with $Z_{a^*,i}=0$. Let
\[
S=\{a\in C:Z_{a,i}=0\},\qquad m=|S|.
\]
The index sets and their sizes are fixed in the probability statements below. For each calibration or test intervention define the absolute residual score
\[
R^{(a)}=\left|Y^{(a)}-\widehat f_i(a,X^{(a)})\right|,
\qquad R^*=R^{(a^*)}.
\]
Assume that the scores $\{R^{(a)}:a\in S\}$ together with $R^*$ are exchangeable. Scores from $C\setminus S$ may be contaminated arbitrarily. Define the contamination fraction
\[
\delta=\frac{|C\setminus S|}{|C|}=\frac{n-m}{n}.
\]
For $\alpha\in(0,1)$, let
\[
k=\left\lceil(n+1)(1-\alpha)\right\rceil
\]
and let $q_\alpha$ be the $k$-th order statistic of the $n$ calibration scores $\{R^{(a)}:a\in C\}$ after adjoining one value $+\infty$. Order statistics count repeated values with multiplicity. An interval with radius $+\infty$ means the whole real line.

## Task

Prove that, for every joint distribution or placement of the contaminated scores consistent with the stated exchangeability assumption,
\[
\mathbb P\!\left\{Y^{(a^*)}\in\left[\widehat f_i(a^*,X^{(a^*)})-q_\alpha,\,\widehat f_i(a^*,X^{(a^*)})+q_\alpha\right]\right\}
\ge1-\alpha-g(\delta,n),
\]
where, for $d\in[0,1]$,
\[
g(d,n)=\frac{dn}{(1-d)n+1}.
\]
Moreover, if an available upper bound $\bar\delta\in[0,1]$ satisfies $\bar\delta\ge\delta$, define $\alpha_c=\alpha-g(\bar\delta,n)$. The upper bound may be random, in which case its stated range and inequality must hold almost surely. When $\alpha_c>0$, form the same order-statistic interval using level $\alpha_c$; when $\alpha_c\le0$, use the whole real line. Prove that the resulting interval has coverage at least $1-\alpha$.
