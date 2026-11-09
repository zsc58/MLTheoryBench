# Problem

## Setup

Let \(m,n\ge2\) be integers, let \(\beta\in[0,1/2)\), and set \(c=1/2-\beta\). For \(W\in\mathbb R^{m\times n}\), define
\[
F(W)=c\lvert W_{11}+W_{22}\rvert+\lvert W_{11}-W_{22}\rvert.
\]

For a nonzero matrix \(A\in\mathbb R^{m\times n}\) of rank \(r\), take a reduced singular-value decomposition \(A=U\Sigma V^\top\) in which \(U\in\mathbb R^{m\times r}\) and \(V\in\mathbb R^{n\times r}\) have orthonormal columns and \(\Sigma\in\mathbb R^{r\times r}\) contains exactly the positive singular values. Define
\[
\operatorname{polar}(A)=UV^\top,
\qquad \operatorname{polar}(0)=0.
\]
Consider either of the following procedures. In both, \(M_{-1}=0\), and at time \(t\ge0\), choose any \(G_t\in\partial F(W_t)\) and set
\[
M_t=\beta M_{t-1}+(1-\beta)G_t.
\]

- **Algorithm A:** \(W_{t+1}=W_t-\lambda_t\operatorname{polar}(M_t)\).
- **Algorithm B:** \(W_{t+1}=W_t-\lambda_t\lVert M_t\rVert_*\operatorname{polar}(M_t)\), where \(\lVert\cdot\rVert_*\) is the nuclear norm.

Fix arbitrary functions
\[
\Phi_t:(\mathbb R^{m\times n})^{t+1}\longrightarrow(0,\infty),
\qquad t\ge0,
\]
and take
\[
\lambda_t=\Phi_t(G_0,\ldots,G_t).
\]
The functions are fixed before the initialization is chosen.

## Task

Prove the following integrated claim. The function \(F\) is convex and \(\sqrt{2(1+c^2)}\)-Lipschitz with respect to the Frobenius norm, and its minimizer set is
\[
\{W\in\mathbb R^{m\times n}:W_{11}=W_{22}=0\}.
\]
Moreover, for either Algorithm A or Algorithm B and for every fixed collection of history-dependent positive-step functions \((\Phi_t)_{t\ge0}\), there is a Lebesgue-measure-zero set \(N\subset\mathbb R^{m\times n}\) such that, from every \(W_0\notin N\), every sequence of iterates satisfying the specified procedure cannot converge to a minimizer of \(F\).
