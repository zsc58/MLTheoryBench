# Problem

## Setup

Let \(\mathcal X\) be a data domain contained in a normed space, equipped with the induced distance and its Borel sigma algebra. Write
\[
B(x,r)=\{x'\in\mathcal X:\|x-x'\|\leq r\}.
\]
Let \((X,Y)\) take values in \(\mathcal X\times\{0,1\}\), let \(P_X\) be the marginal law of \(X\), and let
\[
\eta(x)=\mathbb E[Y\mid X=x]
\]
be a measurable version of the posterior on \(\mathcal X\). All random variables, classifiers, and nearest-neighbour selections below are assumed measurable.

For a measurable classifier \(h:\mathcal X\to\{0,1\}\), write
\[
R(h)=\Pr\{h(X)\ne Y\}.
\]
For a classifier constructed from a training sample, this risk is evaluated on a fresh pair \((X,Y)\) independent of that sample, with the sample held fixed. The Bayes classifier is
\[
h_*(x)=\mathbf1\{\eta(x)\geq1/2\}.
\]

Assume that there are constants \(C_d,\lambda,v>0\) and a positive integer \(d\) such that, for every \(x\in\mathcal X\) and \(r>0\),
\[
P_X(B(x,r))\geq\min\{C_d r^d,1\},
\]
and, for all \(x,x'\in\mathcal X\),
\[
|\eta(x)-\eta(x')|\leq\lambda\|x-x'\|^v.
\]
Assume that the class of norm balls in \(\mathcal X\) has finite VC dimension \(V\).

Assume also that there are \(\alpha,\beta,\gamma>0\) such that, for every \(t>0\),
\[
P_X\left\{\left|\eta(X)-\tfrac12\right|\leq t\right\}
\leq\alpha\exp(-\gamma t^{-\beta}). \tag{EB}
\]

For every positive integer \(n\), let \(S=((X_i,Y_i))_{i=1}^n\) be an i.i.d. training sample. Assume that, for an independent query \(X\) with law \(P_X\), the distances \(\|X-X_1\|,\ldots,\|X-X_n\|\) are pairwise distinct almost surely.

For an integer \(1\leq k\leq n\), let \(\widehat\eta_{n,k}(x)\) be the average of the labels of the \(k\) nearest training inputs to \(x\). Use sample index order to break any distance ties, so the estimator is defined everywhere. Let
\[
\widehat h_{n,k}(x)=\mathbf1\{\widehat\eta_{n,k}(x)\geq1/2\}.
\]
Put \(q=2+d/v\).

## Task

Prove the following theorem. There are positive constants \(A,c,N\) and a deterministic integer sequence \((k_n)_{n\geq1}\), depending only on \(n\) and the displayed parameters \(C_d,\lambda,v,d,V,\alpha,\beta,\gamma\), with
\[
1\leq k_n\leq n,
\qquad
k_n=O\left(n^{(\beta+2)/(\beta+q)}\right),
\]
such that, for every integer \(n\) satisfying
\[
n\geq N\qquad\text{and}\qquad n\geq(A\log n)^{1+q/\beta},
\]
we have
\[
\mathbb E_S\left[R(\widehat h_{n,k_n})-R(h_*)\right]
\leq(2+\alpha)\exp\left(-c n^{\beta/(\beta+q)}\right).
\]
The constants and the constant implicit in the Big-O bound may depend only on the displayed parameters, not on the training sample.
