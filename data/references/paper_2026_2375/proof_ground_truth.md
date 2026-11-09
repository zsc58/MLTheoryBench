# Reference Proof

## Proof Structure

Work conditionally on the information used to construct the predictive densities and prior. In that conditional probability space, the predictive densities and prior are fixed, and the evaluation observations are iid. Decompose mixture negative log loss into weighted component loss minus its Jensen gap. The uniform upper-tail condition for empirical Jensen gaps gives a simultaneous lower bound on their expectations. A simultaneous PAC-Bayes inequality controls expected weighted component loss by its empirical counterpart, KL divergence to the fixed prior, and the sub-Gaussian complexity term. Combining the two bounds cancels the weighted component losses. Finally, integrate the conditional probability statement if an unconditional formulation is desired.

## Complete Proof

Let \(\mathcal H\) contain all training and auxiliary randomness used to construct \(q_1,\ldots,q_K\) and \(\pi\). Condition on \(\mathcal H\). By the setup, the predictive densities and prior are then fixed, the evaluation observations are iid, and \(\widetilde Y\) is an independent observation from the same conditional distribution. All expectations and probabilities below are conditional on \(\mathcal H\).

Write
\[
X_{ik}=-\log q_k(Y_i),\qquad X_k=-\log q_k(\widetilde Y),
\]
and define
\[
J_i(w)=\sum_k w_kX_{ik}+\log\!\left(\sum_k w_ke^{-X_{ik}}\right),
\qquad
J(w;\widetilde Y)=\sum_k w_kX_k+\log\!\left(\sum_k w_ke^{-X_k}\right).
\]
Thus, pointwise,
\[
-\log\!\left(\sum_k w_kq_k(Y_i)\right)
=\sum_kw_kX_{ik}-J_i(w).
\]
If
\[
R(w)=\mathbb E\left[-\log\!\left(\sum_k w_kq_k(\widetilde Y)\right)\right]
\quad\text{and}\quad
G(w)=\mathbb E J(w;\widetilde Y),
\]
then
\[
R(w)=\sum_kw_k\mathbb E X_k-G(w).
\]

Set
\[
B=\sqrt{2ns''\log(2/\delta)}.
\]
The conditional uniform upper-tail condition, applied with \(t=B\), implies that with conditional probability at least \(1-\delta/2\), simultaneously for every \(w\in\Delta_K\),
\[
nG(w)\ge \sum_{i=1}^nJ_i(w)-B.
\tag{1}
\]

Conditionally on \(\mathcal H\), the predictive densities and prior are fixed, and the component losses are \(s\)-sub-Gaussian. The standard simultaneous PAC-Bayes inequality therefore gives, with conditional probability at least \(1-\delta/2\), for every \(w\in\Delta_K\),
\[
n\sum_kw_k\mathbb E X_k
\le \sum_{i=1}^n\sum_kw_kX_{ik}+\operatorname{KL}(w\|\pi)
+\frac{ns^2}{2}+\log\frac{2}{\delta}.
\tag{2}
\]

By a conditional union bound, (1) and (2) hold together with conditional probability at least \(1-\delta\). Subtract (1) from (2). Since
\[
\sum_{i=1}^n\sum_kw_kX_{ik}-\sum_{i=1}^nJ_i(w)
=-\sum_{i=1}^n\log\!\left(\sum_kw_kq_k(Y_i)\right),
\]
we obtain, simultaneously for all \(w\in\Delta_K\),
\[
nR(w)\le \operatorname{KL}(w\|\pi)
-\sum_{i=1}^n\log\!\left(\sum_kw_kq_k(Y_i)\right)
+\frac{ns^2}{2}+\log\frac{2}{\delta}
+\sqrt{2ns''\log\frac{2}{\delta}}.
\]
The first two terms on the right are \(\widehat F(w)\), proving the claim conditionally on \(\mathcal H\). Since the conditional failure probability is at most \(\delta\) almost surely, the corresponding unconditional statement also follows by averaging.
