# Problem

## Setup

Let \(N\ge4\). Let \(\mathcal X\) and \(\mathcal Y\) be sets equipped with fixed real-valued functions \(d_X:\mathcal X\times\mathcal X\to\mathbb R\) and \(d_Y:\mathcal Y\times\mathcal Y\to\mathbb R\), and let \(X=(x_1,\ldots,x_N)\in\mathcal X^N\) and \(Y=(y_1,\ldots,y_N)\in\mathcal Y^N\) be paired representations. For a set equipped with such a function \(d\), define
\[
O_d(a,b,c,e)=\operatorname{sign}(d(a,b)-d(c,e)),
\qquad
O_d^\Delta(a,b,c)=O_d(a,b,a,c)=\operatorname{sign}(d(a,b)-d(a,c)),
\]
with values in \(\{-1,0,1\}\). Let \([N]^r_{\ne}\) denote ordered \(r\)-tuples of distinct indices and \((n)_r=n(n-1)\cdots(n-r+1)\).

Define
\[
\operatorname{TSI}(X,Y)=\frac{1}{(N)_3}
\sum_{(i,j,k)\in[N]^3_{\ne}}
\mathbf 1\{O^\Delta_{d_X}(x_i,x_j,x_k)=O^\Delta_{d_Y}(y_i,y_j,y_k)\},
\]
and
\[
\operatorname{QSI}(X,Y)=\frac{1}{(N)_4}
\sum_{(i,j,k,l)\in[N]^4_{\ne}}
\mathbf 1\{O_{d_X}(x_i,x_j,x_k,x_l)=O_{d_Y}(y_i,y_j,y_k,y_l)\}.
\]

Choose an unchanged index set \(U\subseteq[N]\) with \(m=|U|\ge4\), and let \(V=[N]\setminus U\). Let \(X_U,Y_U\) be the restrictions to the paired indices in U. Let \(T:\mathcal X\to\mathcal X\) be arbitrary, and form \(X'=(x'_1,\ldots,x'_N)\) by setting \(x'_i=x_i\) for \(i\in U\) and \(x'_i=T(x_i)\) for \(i\in V\). Set
\[
c_3=\frac{(m)_3}{(N)_3},\qquad c_4=\frac{(m)_4}{(N)_4}.
\]

## Task

Prove the following integrated robustness theorem. For \(S_3=\operatorname{TSI}\) and \(S_4=\operatorname{QSI}\),
\[
|S_r(X_U,Y_U)-S_r(X',Y)|\le1-c_r,
\qquad
|S_r(X,Y)-S_r(X',Y)|\le1-c_r,
\qquad r\in\{3,4\}.
\]
In particular, for fixed \(r\), these deviations converge to zero whenever \(|V|/N\to0\).
