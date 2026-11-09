# Problem

## Setup

Let \(N\) and \(T\) be positive integers. There are \(N\) available arms, indexed by \(v\in\{1,\ldots,N\}\), and a fixed known orthogonal matrix \(Q\in\mathbb R^{N\times N}\). Arm \(v\) has feature vector \(x_v\in\mathbb R^N\), whose coordinates are the \(v\)-th row of \(Q\), so \(\|x_v\|_2\le1\). Let the fixed known regularizer be
\[
0<\lambda=\lambda_1\le\lambda_2\le\cdots\le\lambda_N,
\qquad \Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_N).
\]
For a positive-definite matrix \(M\), write \(\|z\|_M=\sqrt{z^\top Mz}\). Fix finite known constants \(R,C\ge0\) and a confidence level \(\delta\in(0,1)\).

The unknown vector \(\alpha^*\in\mathbb R^N\) is fixed. Let \(\mathcal F_{t-1}\) denote the history available before round \(t\), consisting of past actions and observed rewards, together with policy randomization available before that round. The chosen arm \(\pi_t\) is \(\mathcal F_{t-1}\)-measurable. After choosing it, the policy observes its reward
\[
r_t=x_{\pi_t}^{\top}\alpha^*+\epsilon_t,
\qquad
\mathbb E[e^{\eta\epsilon_t}\mid\mathcal F_{t-1}]\le e^{\eta^2R^2/2}\quad(\eta\in\mathbb R),
\qquad 1\le t\le T.
\]
Assume \(\|\alpha^*\|_\Lambda\le C\) and \(x_v^{\top}\alpha^*\in[-1,1]\) for every arm. Define
\[
d=\max\left\{k\in\{1,\ldots,N\}:(k-1)\lambda_k\le \frac{T}{\log(1+T/\lambda)}\right\},
\qquad L=\log(1+T/\lambda).
\]
For \(1\le t\le T+1\), let
\[
V_t=\Lambda+\sum_{s=1}^{t-1}x_{\pi_s}x_{\pi_s}^{\top},
\qquad
\widehat\alpha_t=V_t^{-1}\sum_{s=1}^{t-1}x_{\pi_s}r_s,
\]
where an empty sum is zero, and set \(c=2R\sqrt{dL+2\log(1/\delta)}+C\). At each round \(1\le t\le T\), the policy chooses any history-measurable maximizer
\[
\pi_t\in\arg\max_v\left\{x_v^{\top}\widehat\alpha_t+c\,\|x_v\|_{V_t^{-1}}\right\}.
\]
Define pseudo-regret
\[
R_T=\sum_{t=1}^T\left(\max_v x_v^{\top}\alpha^*-x_{\pi_t}^{\top}\alpha^*\right).
\]

## Task

Prove that, with probability at least \(1-\delta\),
\[
R_T\le\bigl[4R\sqrt{d\log(1+T/\lambda)+2\log(1/\delta)}+2C+2\bigr]
\sqrt{4dT\log(1+T/\lambda)}.
\]
