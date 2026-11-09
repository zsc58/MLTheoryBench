# Problem

## Setup

Let `C,D` be positive integers and let `X` be an input set. Fix a feature map `h:X\to\mathbb R^D` satisfying `\|h(x)\|_2\le R` for every `x\in X`, where `R\ge0`. Let `W,\widetilde W\in\mathbb R^{C\times D}`, with `\widetilde W` a low-rank approximation of `W`, and let `b\in\mathbb R^C` be a common bias vector. Define

`z(x)=Wh(x)+b`, `\widetilde z(x)=\widetilde W h(x)+b`.

For `u\in\mathbb R^C`, define the softmax vector by

`\sigma_i(u)=\dfrac{e^{u_i}}{\sum_{j=1}^C e^{u_j}},\qquad i=1,\ldots,C`.

Set `p(x)=\sigma(z(x))` and `\widetilde p(x)=\sigma(\widetilde z(x))`. For a matrix `A`, `\|A\|_2` denotes its induced Euclidean operator (spectral) norm.

## Task

Prove that, uniformly for every `x\in X`,

`\|\widetilde p(x)-p(x)\|_\infty\le \frac12 R\|\widetilde W-W\|_2`.

Equivalently, for every class `c\in\{1,\ldots,C\}` and every `x\in X`,

`|\widetilde p_c(x)-p_c(x)|\le \frac12 R\|\widetilde W-W\|_2`.
