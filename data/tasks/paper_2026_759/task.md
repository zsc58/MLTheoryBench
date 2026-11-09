# Problem

## Setup

Fix an input x and an EOS-terminated autoregressive model on a finite token vocabulary V that includes the EOS token. For every integer time t >= 1 and prefix h=(x,y_{<t}), write
\[
p(v)=p_\theta(v\mid h),\qquad \sum_{v\in V}p(v)=1.
\]
Let \(\alpha\geq 1\). A prefix-only proposal is any probability distribution \(q(v\mid h)\) determined from the current prefix alone. It is support-compatible if \(q(v\mid h)>0\) whenever \(p(v)>0\). Define
\[
Z(h)=\sum_{u\in V}p(u)^\alpha,
\qquad
\omega(v;h)=
\begin{cases}
p(v)^\alpha/q(v\mid h), & p(v)>0,\\
0, & p(v)=0.
\end{cases}
\]
For a real logit vector \(\ell\in\mathbb R^V\), define
\[
\operatorname{softmax}(\ell)(v)=\frac{\exp(\ell(v))}{\sum_{u\in V}\exp(\ell(u))}.
\]
Temperature sampling from logits \(\ell\) at temperature \(\tau>0\) means drawing from \(\operatorname{softmax}(\ell/\tau)\).

## Task

Prove that for every time t and realized prefix h, among all support-compatible prefix-only proposals q, the unique minimizer of
\[
\operatorname{Var}_{v\sim q(\cdot\mid h)}[\omega(v;h)]
\]
is
\[
q^*(v\mid h)=\frac{p(v)^\alpha}{\sum_{u\in V}p(u)^\alpha}.
\]
Under this proposal the incremental weight is constant over the support of p and the conditional variance is zero. Moreover, if \(p(v)=\operatorname{softmax}(\ell(h))(v)\) for a real logit vector \(\ell(h)\in\mathbb R^V\), then q* is temperature sampling with \(\tau=1/\alpha\).
