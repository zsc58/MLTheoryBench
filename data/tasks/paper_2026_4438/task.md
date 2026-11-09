# Problem

## Setup

A **normalized finite spectral law** is a probability distribution of the form
\[
P=\frac1N\sum_{i=1}^N\delta_{x_i},
\qquad N\geq1,\quad x_i>0,\quad \frac1N\sum_{i=1}^N x_i=1,
\]
where \(N\) is an integer, \(\delta_x\) denotes unit point mass at \(x\), and repeated values among the \(x_i\) are allowed. The integer \(N\) may vary between laws. Thus \(\mathbb E_P[X]=1\).

For real \(t\), set
\[
M_P(t)=\mathbb E_P[X^t],\qquad K_P(t)=\log M_P(t).
\]
Thus
\[
K_P'(0)=\mathbb E_P[\log X].
\]

Fix an arbitrary finite set of positive observation nodes
\[
\mathcal T=\{t_1,\ldots,t_m\}\subset(0,\infty).
\]
An estimator based on these observations is a continuous function \(\Phi:\mathbb R^m\to\mathbb R\), evaluated at
\[
\bigl(K_P(t_1),\ldots,K_P(t_m)\bigr).
\]

## Task

Prove the following integrated impossibility result.

For every finite positive-node set \(\mathcal T\):

1. There exist two normalized finite spectral laws \(P_+\) and \(P_-\) such that
\[
K_{P_+}(t_j)=K_{P_-}(t_j)\quad\text{for all }j=1,\ldots,m,
\]
but
\[
K_{P_+}'(0)\ne K_{P_-}'(0).
\]

2. For every continuous estimator \(\Phi\), there is a sequence of normalized finite spectral laws \((P_n)\) for which the observation vectors
\[
\bigl(K_{P_n}(t_1),\ldots,K_{P_n}(t_m)\bigr)
\]
converge in \(\mathbb R^m\), whereas \(K_{P_n}'(0)\to-\infty\). Consequently,
\[
\left|\Phi\!\left(K_{P_n}(t_1),\ldots,K_{P_n}(t_m)\right)-K_{P_n}'(0)\right|\to\infty.
\]

In particular, finitely many positive log-moment observations cannot support a continuous estimator with uniformly bounded error for \(K_P'(0)\) over normalized finite spectral laws.
