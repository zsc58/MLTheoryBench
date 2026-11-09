# Problem

## Setup

Let `d >= 1`, let `[d]={1,...,d}`, and let `x=(x_1,...,x_d)` be a data vector. For each subset `S\subseteq[d]` and each `j\notin S`, let

\[
q_\theta(x_j\mid x_S)
\]

be an autoregressive conditional likelihood, with all logarithms below well-defined. Let `Pi=(Pi_1,...,Pi_d)` be a uniformly random permutation of `[d]`, and define the revealed prefix set

\[
S_k(\Pi)=\{\Pi_1,...,\Pi_k\},\qquad S_0(\Pi)=\varnothing.
\]

The order-averaged autoregressive training objective for `x` is

\[
J_\theta(x)=\mathbb E_\Pi\left[\sum_{r=1}^d
\log q_\theta\bigl(x_{\Pi_r}\mid x_{S_{r-1}(\Pi)}\bigr)\right].
\]

For an integer `k`, write `\mathrm{Unif}\binom{[d]}k` for the uniform distribution over all `k`-element subsets of `[d]`. A masking context is called MCAR-style here when its random observed index set is sampled independently of the data values.

## Task

Prove the following theorem. If `K` is uniform on `{0,...,d-1}` and, conditional on `K`, `S\sim\mathrm{Unif}\binom{[d]}K`, then

\[
J_\theta(x)
=
\mathbb E_K\mathbb E_{S\sim\mathrm{Unif}\binom{[d]}K}
\left[
\frac{d}{d-K}\sum_{j\notin S}\log q_\theta(x_j\mid x_S)
\right].
\]

Consequently, the random variable inside the expectation is an unbiased single-iteration training objective, and its iteration samples a value-independent observed subset `S` and predicts all entries in its complementary mask. In this sense, training under the uniform order prior implicitly simulates MCAR-style imputation.
