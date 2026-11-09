# Problem

## Setup

Let \(K\) be a positive integer and let \(\mathcal Y=\{1,\ldots,K\}\). Write
\[
\Delta^{K-1}=\left\{p\in[0,1]^K:\sum_{a=1}^K p_a=1\right\}
\]
for the probability simplex.

Let \(Y\) take values in \(\mathcal Y\). Let \(X\) be the model-observed input, taking values in a measurable space \(\mathcal X\), let \(G\) be a measurable grouping variable representing the information partition used by a human, and let \(A\in\mathcal Y\) be the human's sampled prediction. Let \(f:\mathcal X\to\Delta^{K-1}\) be a measurable probabilistic predictor, with coordinates \(f_a(X)\).

A measurable \(\Delta^{K-1}\)-valued random predictor \(q\) is **generalized calibrated with respect to \(G\)** if
\[
q=\Pr(Y\mid q,G)=\Pr(Y\mid q)
\]
almost surely, where these equalities are equalities of conditional label distributions.

Assume the model is calibrated and measurable with respect to some grouping \(\Phi_f(X)\):
\[
f_a(X)=\Pr(Y=a\mid \Phi_f(X))\qquad\text{almost surely for every }a\in\mathcal Y.
\]
Assume the human predictive distribution is calibrated with respect to \(G\), and that the sampled prediction is conditionally independent of \((Y,f(X))\) given \(G\):
\[
\Pr(A=a\mid G)=\Pr(Y=a\mid G)\qquad\text{almost surely for every }a\in\mathcal Y,
\qquad A\perp (Y,f(X))\mid G.
\]

Write \(M=f(X)\), and choose a measurable version of the Bayes-optimal combination rule
\[
g^*:\mathcal Y\times\Delta^{K-1}\to\Delta^{K-1},
\qquad g^*(A,M)=\Pr(Y\mid A,M)\quad\text{almost surely}.
\]
Suppose this version of \(g^*\) is injective on the support of \((A,M)\). Support is taken in the product of the discrete topology on \(\mathcal Y\) and the usual Euclidean topology on \(\Delta^{K-1}\); measurability of the combination rule uses the associated Borel structures.

## Task

Prove the following claim. Suppose there are two distinct values \(S_1,S_2\) of \(G\), a model-output value \(v\), and labels \(a',a''\in\mathcal Y\) such that, for each \(i\in\{1,2\}\),
\[
\Pr(A=a'\mid G=S_i)>0,
\qquad
\Pr(M=v,G=S_i)>0,
\]
and
\[
\Pr(Y=a''\mid M=v,G=S_1)
\ne
\Pr(Y=a''\mid M=v,G=S_2).
\]
Then \(g^*(A,M)\) is not generalized calibrated with respect to \(G\).
