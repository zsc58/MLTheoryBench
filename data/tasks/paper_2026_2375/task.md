# Problem

## Setup

Let \(\mathcal H\) denote all training and auxiliary randomness used to construct the predictive densities and the prior. Assume \(\mathcal H\) is independent of the evaluation observations, and condition on \(\mathcal H\) throughout. Thus \(q_1,\ldots,q_K\) and \(\pi\) are fixed in the conditional probability space. Let \(K\ge1\) and \(n\ge1\) be integers, let
\(\Delta_K=\{w\in[0,1]^K:\sum_kw_k=1\}\), and let
\(q_1,\ldots,q_K\) be strictly positive predictive densities. Let \(Y_1,\ldots,Y_n\) be iid evaluation observations conditional on \(\mathcal H\), and let \(\widetilde Y\) be an independent observation from the same conditional distribution. A prior \(\pi\in\Delta_K\), with positive coordinates, is fixed conditional on \(\mathcal H\). It may be the optimism-penalizing prior
\[
\pi_k=\frac{e^{-o_k}}{\sum_j e^{-o_j}},
\qquad
 o_k=-\sum_{i=1}^m\log q_k(B_i)+\sum_{i=1}^m\log q_k(A_i),
\]
for auxiliary data \((A_i,B_i)\) included in \(\mathcal H\) and independent of the evaluation sample.

All expectations and probabilities below are conditional on \(\mathcal H\). For \(w\in\Delta_K\), define the empirical divergence-style mixture objective
\[
\widehat F(w)=\operatorname{KL}(w\|\pi)-\sum_{i=1}^n\log\!\left(\sum_{k=1}^K w_kq_k(Y_i)\right).
\]
Define the pointwise Jensen gap
\[
J(w;z)= -\sum_{k=1}^K w_k\log q_k(z)+\log\!\left(\sum_{k=1}^K w_kq_k(z)\right).
\]

Assume that there is \(s>0\) such that each component negative log score \(-\log q_k(\widetilde Y)\) is conditionally sub-Gaussian with parameter \(s\): for every \(\lambda\in\mathbb R\),
\[
\mathbb E e^{\lambda(-\log q_k(\widetilde Y)-\mathbb E[-\log q_k(\widetilde Y)])}
\le e^{\lambda^2s^2/2}.
\]
Assume also that there is \(s''>0\) such that the evaluation sample satisfies the conditional uniform Jensen-gap upper-tail condition
\[
\Pr\!\left(
\sup_{w\in\Delta_K}\left\{\sum_{i=1}^nJ(w;Y_i)
-n\mathbb EJ(w;\widetilde Y)\right\}>t\right)
\le \exp\!\left(-\frac{t^2}{2ns''}\right)
\qquad(t\ge0).
\]

## Task

Prove that for every \(\delta\in(0,1]\), with conditional probability at least
\(1-\delta\) over \(Y_1,\ldots,Y_n\), simultaneously for all \(w\in\Delta_K\),
\[
 n\,\mathbb E\left[-\log\!\left(\sum_{k=1}^K w_kq_k(\widetilde Y)\right)\right]
\le \widehat F(w)+\frac{ns^2}{2}+\log\frac{2}{\delta}
 +\sqrt{2ns''\log\frac{2}{\delta}}.
\]
