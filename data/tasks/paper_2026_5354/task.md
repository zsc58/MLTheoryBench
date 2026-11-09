# Problem

## Setup

Fix an integer \(C\ge 2\). Scores are vectors \(z\in\mathbb R^C\), labels lie in \(\{1,\ldots,C\}\), and a loss is a function
\[
L:\mathbb R^C\times\{1,\ldots,C\}\to\mathbb R.
\]
For a permutation \(\pi\) of the classes, define \((\pi z)_j=z_{\pi^{-1}(j)}\). The loss is:

- **permutation invariant** if \(L(\pi z,\pi(y))=L(z,y)\) for every \(z,y,\pi\);
- **symmetric** if \(\sum_{y=1}^C L(z,y)\) is constant as a function of \(z\);
- **non-increasing** if, with all other coordinates fixed, \(L(z,y)\) is non-increasing in the target coordinate \(z_y\);
- **nontrivial** if it is not constant on \(\mathbb R^C\times\{1,\ldots,C\}\).

Define the centered linear loss
\[
U(z,y)=-z_y+\frac1C\sum_{k=1}^C z_k.
\]

For \(z^\star\in\mathbb R^C\), when every map \(z\mapsto L(z,y)\) is differentiable at \(z^\star\), define its first-order affine approximation by
\[
A(z,y)=L(z^\star,y)+\nabla_zL(z^\star,y)^\top(z-z^\star).
\]

## Task

Prove the following two-part characterization.

**(a) Global uniqueness.** A loss is convex in \(z\) for every label, nontrivial, non-increasing, permutation invariant, and symmetric if and only if there exist constants \(a\in\mathbb R\) and \(b>0\) such that
\[
L(z,y)=a+bU(z,y)
\qquad\text{for all }z,y.
\]

**(b) Local universality.** Let \(L\) be non-increasing, permutation invariant, and symmetric, without assuming convexity. Suppose that for some \(t\in\mathbb R\), every \(L(\cdot,y)\) is differentiable at the equal-score vector \(z^\star=t\mathbf 1\), and that \(\nabla_zL(z^\star,y)\ne0\) for at least one label \(y\). Prove that there exist constants \(a\in\mathbb R\) and \(b>0\) such that its first-order approximation satisfies
\[
A(z,y)=a+bU(z,y)
\qquad\text{for all }z,y.
\]
