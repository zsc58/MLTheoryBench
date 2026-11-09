# Problem

## Setup

Let \(\Xi\) be a context set, fix \(\xi\in\Xi\), and let \(p:\Xi\to\mathbb R^m\) be a predictor. Let \(A\in\mathbb R^{m\times n}\) and \(c\in\mathbb R^n\) be deterministic, and let \(b,\widehat b\in\mathbb R^m\), with \(\widehat b=p(\xi)\). Consider the primal-dual pair
\[
\min_{x\ge0}\{c^\top x:Ax\ge b\},\qquad
\max_{y\ge0}\{b^\top y:A^\top y\le c\}.
\]
Assume \((x^\ast,y^\ast)\) is an optimal primal-dual pair for the true right-hand side \(b\), and \(y^\ast\ne0\). Write \(a_j^\top\) for the \(j\)-th row of \(A\), and define
\[
J^=(x^\ast)=\{j:a_j^\top x^\ast=b_j\},\qquad
J^+(y^\ast)=\{j:y_j^\ast>0\}.
\]
Define the predicted feasible-pair set
\[
\widehat S(\xi;p)=\{(x,y):Ax\ge\widehat b,\ x\ge0,\ A^\top y\le c,\ y\ge0\},
\]
and the predicted optimal-pair set
\[
\widehat S^\ast(\xi;p)=\{(x,y)\in\widehat S(\xi;p):c^\top x=\widehat b^\top y\}.
\]

## Task

Prove the following integrated characterization for \((x^\ast,y^\ast)\):

1. If \(b\ge\widehat b\) componentwise, then \((x^\ast,y^\ast)\in\widehat S(\xi;p)\). If there exists \(j'\in J^=(x^\ast)\) with \(b_{j'}<\widehat b_{j'}\), then \((x^\ast,y^\ast)\notin\widehat S(\xi;p)\).
2. Conditional on \((x^\ast,y^\ast)\in\widehat S(\xi;p)\),
\[
(x^\ast,y^\ast)\in\widehat S^\ast(\xi;p)
\quad\Longleftrightarrow\quad
\widehat b_j=b_j\ \text{for every }j\in J^+(y^\ast).
\]
