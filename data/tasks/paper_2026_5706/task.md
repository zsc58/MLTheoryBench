# Problem

## Setup

Fix an integer \(G\ge 2\) and a prompt \(x\). Independently sample responses \(Y_1,\ldots,Y_G\) from a differentiable policy \(\pi_\theta(\cdot\mid x)\). Each response has a binary reward \(R_i\in\{0,1\}\). Define
\[
 K=\sum_{i=1}^G R_i,\qquad M=\frac KG,
 \qquad S=\left(\frac1G\sum_{i=1}^G(R_i-M)^2\right)^{1/2}
       =\frac{\sqrt{K(G-K)}}G.
\]
For a non-unanimous group, define
\[
 A_i=\frac{R_i-M}{S},\qquad
 S_i=\nabla_\theta\log\pi_\theta(Y_i\mid x),
 \qquad U=\frac1G\sum_{i=1}^G A_iS_i.
\]
Also define the conditional sample means
\[
 \overline S_+=\frac1K\sum_{R_i=1}S_i,
 \qquad
 \overline S_-=\frac1{G-K}\sum_{R_i=0}S_i.
\]
For \(K\in\{0,G\}\), set the contrastive update \(U\) to zero. The update is the on-policy gradient at the initial surrogate step; clipping and regularization terms are not included.

In the scalar Bernoulli-logit specialization, the policy samples \(Y_i\in\{0,1\}\), the reward is \(R_i=Y_i\), and
\[
 p=\mathbb P_\theta(Y_i=1)=\frac1{1+e^{-\theta}},
 \qquad S_i=Y_i-p.
\]

## Task

Prove the following integrated theorem.

For every realized group,
\[
 U=S(\overline S_+-\overline S_-)
\]
when \(0<K<G\), with both sides understood as zero for a unanimous group. This update is unchanged if a common action-independent baseline is subtracted from every reward before the group mean and standard deviation are formed.

Moreover, in the scalar Bernoulli-logit specialization,
\[
 \mathbb E[U]
 =\frac1G\sum_{k=1}^{G-1}\binom Gk p^k(1-p)^{G-k}\sqrt{k(G-k)}.
\]
For every fixed \(p\in(0,1)\), as \(G\to\infty\),
\[
 \mathbb E[U]
 =\sqrt{p(1-p)}\left(1-\frac{1}{8Gp(1-p)}+O(G^{-2})\right).
\]
Finally, show that the leading term \(\sqrt{p(1-p)}\) is the derivative with respect to \(\theta\) of \(2\arcsin\sqrt{p(\theta)}\).
