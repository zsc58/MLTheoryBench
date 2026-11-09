# Problem

## Setup

Let \(d\) and \(K\) be positive integers, and let \((Z,Y)\) have a joint distribution on \(\mathbb R^d\times\{1,\ldots,K\}\). Write \(P_X\) for the feature marginal and \(X=\operatorname{supp}(P_X)\). Assume that, for every class of positive probability, the conditional feature distribution given that class has a density with respect to \(d\)-dimensional Lebesgue measure.

A probability kernel is a continuous map \(r:X\to\Delta^{K-1}\), where
\[
\Delta^{K-1}=\{u\in[0,1]^K:\textstyle\sum_{k=1}^K u_k=1\}.
\]
Let \(q(k|x)\) be a continuous version of the true conditional label kernel. Assume \(q\) is complete: for every \(\alpha\in\mathbb R^K\), if
\[
\sum_{k=1}^K\alpha_k q(k|x)=0\qquad\text{for every }x\in X,
\]
then \(\alpha=0\).

For a continuous candidate kernel \(p\), define
\[
s_k=\mathbb E_{Z\sim P_X}[p(k|Z)].
\]
The domain of the normalized score consists of those candidate kernels for which \(s_k>0\) for every \(k\). On this domain, define
\[
S(p,x,k)=-\log\frac{p(k|x)}{s_k},
\]
where \(-\log 0=+\infty\). Define its population risk under the true kernel by
\[
R(p;q)=\mathbb E_{Z\sim P_X}\mathbb E_{Y\sim q(\cdot|Z)}[S(p,Z,Y)].
\]
In the inner label expectation, a label of probability zero contributes zero, including when its score is \(+\infty\).

## Task

Prove that \(R(p;q)\ge R(q;q)\) for every continuous candidate kernel in the stated score domain, and that equality holds if and only if \(p(k|x)=q(k|x)\) for all \(k\) and all \(x\in X\). Conclude that this non-local scoring rule is strictly proper for complete true kernels on this domain.
