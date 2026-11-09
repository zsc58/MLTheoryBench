# Problem

## Setup

Let \(X_1,\ldots,X_n\) be independent random variables taking values in a measurable space \(\mathcal X\). Let \(f:\mathcal X^n\to\mathbb R\) be measurable. For each coordinate let \(X_i'\) be an independent copy of \(X_i\), independent of all the other variables, and let \(H_i:\mathcal X^2\to[0,\infty)\) be deterministic and measurable. Assume the replace-one bound
\[
\bigl|f(X_1,\ldots,X_i,\ldots,X_n)-f(X_1,\ldots,X_i',\ldots,X_n)\bigr|
\le H_i(X_i,X_i')\quad\text{a.s.}
\]
for every \(i\), and that for some real \(p\ge2\), \(\mathbb E[H_i(X_i,X_i')^p]<\infty\) for all \(i\). Define
\[
A_r:=\sum_{i=1}^n\mathbb E\bigl[H_i(X_i,X_i')^r\bigr],\qquad r\in\{2,p\}.
\]

## Task

Prove that for every \(z>0\),
\[
\mathbb P\!\left(\left|f(X_1,\ldots,X_n)-\mathbb Ef(X_1,\ldots,X_n)\right|>z\right)
\le 4\left(\frac{4(p+2)}p\right)^p\frac{A_p}{z^p}
+2\exp\!\left(-\frac{z^2}{2(p+2)^2e^pA_2}\right).
\]
When \(A_2=0\), interpret the exponential term as zero (and the left-hand side is then zero).
