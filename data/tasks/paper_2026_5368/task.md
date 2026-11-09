# Problem

## Setup

Let \(K\ge 2\) and \(p\ge 1\) be integers. Let \(\mathcal Z\subseteq\mathbb R^p\) be a feature space equipped with its trace Borel sigma-algebra. In each of two domains with joint probability laws \(P\) and \(Q\), let \(Z\) take values in \(\mathcal Z\), and let \(L=(L_1,\ldots,L_K)\) be a one-hot \(K\)-class label.

Let \(g\) be the same fixed deterministic measurable classifier in both domains, with output
\[
R=g(Z)\in\{r\in[0,1]^K:\textstyle\sum_{k=1}^K r_k=1\}.
\]
Fix the same deterministic measurable tie-breaking rule in both domains, and define
\[
A=\operatorname*{argmax}_{1\le k\le K}R_k,\qquad M=R_A=\max_{1\le k\le K}R_k.
\]

Assume covariate shift: the feature marginal laws satisfy \(P_Z\ne Q_Z\), while the conditional label laws admit common measurable posterior functions \(\eta_k:\mathcal Z\to[0,1]\), with \(\sum_{k=1}^K\eta_k(z)=1\), such that
\[
\eta_k(Z)=\Pr_d(L_k=1\mid Z)\quad d\text{-almost surely},\qquad d\in\{P,Q\},\quad k=1,\ldots,K.
\]
Write \(\eta_A(Z)=\eta_{A(Z)}(Z)\).

For each score statistic \(T\in\{M,R_1,\ldots,R_K\}\), let \(\mu_{d,T}\) denote its distribution under domain \(d\). Choose any finite nonnegative Borel measure \(\nu_T\) on \([0,1]\) such that
\[
\nu_T\ll\mu_{P,T}\quad\text{and}\quad\nu_T\ll\mu_{Q,T}.
\]
Here \(\nu\ll\mu\) means that \(\mu(B)=0\) implies \(\nu(B)=0\) for every Borel set \(B\). Conditional probabilities and conditional expectations below are represented by arbitrary measurable versions as functions of the conditioning score.

## Task

Prove the following integrated characterization for every choice of comparison measures specified above.

1. The top-label conditional correctness probabilities agree across domains,
\[
\Pr_P(L_A=1\mid M=m)=\Pr_Q(L_A=1\mid M=m)
\]
for \(\nu_M\)-almost every \(m\), if and only if
\[
\mathbb E_P[\eta_A(Z)\mid M=m]=\mathbb E_Q[\eta_A(Z)\mid M=m]
\]
for \(\nu_M\)-almost every \(m\).

2. For every class \(k\), the class-wise conditional probabilities agree across domains,
\[
\Pr_P(L_k=1\mid R_k=r)=\Pr_Q(L_k=1\mid R_k=r)
\]
for \(\nu_{R_k}\)-almost every \(r\), if and only if, for every class \(k\),
\[
\mathbb E_P[\eta_k(Z)\mid R_k=r]=\mathbb E_Q[\eta_k(Z)\mid R_k=r]
\]
for \(\nu_{R_k}\)-almost every \(r\).
