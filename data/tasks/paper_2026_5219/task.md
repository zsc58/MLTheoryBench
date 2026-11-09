# Problem

## Setup

Let \(d\ge 2\) be an integer, \(N=\{1,\ldots,d\}\), \(b,x\in\mathbb R^d\), and let \(f:\mathbb R^d\to\mathbb R\). For \(A\subseteq N\), write
\[
f(A;x)=f(x_A,b_{N\setminus A}).
\]
For \(A\subseteq N\), let \(z^A(t)\), \(0\le t\le 1\), have coordinates \(b_k+t(x_k-b_k)\) for \(k\in A\), and \(b_k\) otherwise.

Assume that, for every nonempty \(A\subseteq N\) and every \(i\in A\), the ordinary partial derivative \(\partial_i f(z^A(t))\) exists for every \(t\in[0,1]\), is Lebesgue measurable as a function of \(t\), and satisfies
\[
\int_0^1\left|\partial_i f(z^A(t))\right|\,dt<\infty.
\]
All path integrals below are Lebesgue integrals.

For \(i\in A\), define the Shapley and integrated-gradient attributions on the restriction to \(A\) by
\[
\operatorname{SV}_i(A)=\sum_{T\subseteq A\setminus\{i\}}
 \frac{|T|!(|A|-|T|-1)!}{|A|!}
 \bigl[f(T\cup\{i\};x)-f(T;x)\bigr],
\]
\[
\operatorname{IG}_i(A)=(x_i-b_i)\int_0^1\partial_i f(z^A(t))\,dt.
\]

For either \(\phi\in\{\operatorname{SV},\operatorname{IG}\}\), define its directed meta-attribution by
\[
\mathcal M^\phi_{j\to i}
=\sum_{S\subseteq N\setminus\{i,j\}}
\frac{\phi_i(S\cup\{i,j\})-\phi_i(S\cup\{i\})}
{(d-1)\binom{d-2}{|S|}}
\quad (i\ne j),
\]
and set \(\mathcal M^\phi_{i\to i}=\phi_i(\{i\})\).

Define a symmetric singleton-and-pair quantity \(\Theta\) by
\[
\Theta_{\{i\}}=f(\{i\};x)-f(\varnothing;x)
\]
and, for \(i\ne j\),
\[
\Theta_{\{i,j\}}
=\sum_{S\subseteq N\setminus\{i,j\}}
\frac{2}{d\binom{d-1}{|S|}}
\sum_{T\subseteq\{i,j\}}(-1)^{|T|}f(S\cup T;x).
\]

Define directed path-based quantities, for \(i\ne j\), by
\[
\mathcal P_{j\to i}
=\sum_{S\subseteq N\setminus\{i,j\}}
\frac{\operatorname{IG}_i(S\cup\{i,j\})-
\operatorname{IG}_i(S\cup\{i\})}
{(d-1)\binom{d-2}{|S|}},
\]
together with
\[
\mathcal P_i=f(\{i\};x)-f(\varnothing;x),
\qquad
\mathcal P_{\{i,j\}}=\mathcal P_{i\to j}+\mathcal P_{j\to i}.
\]

## Task

Prove that, for every distinct \(i,j\in N\),
\[
\Theta_{\{i\}}=\mathcal M^{\operatorname{SV}}_{i\to i},
\qquad
\Theta_{\{i,j\}}=\mathcal M^{\operatorname{SV}}_{j\to i}
+\mathcal M^{\operatorname{SV}}_{i\to j},
\]
and
\[
\mathcal P_i=\mathcal M^{\operatorname{IG}}_{i\to i},
\qquad
\mathcal P_{\{i,j\}}=\mathcal M^{\operatorname{IG}}_{j\to i}
+\mathcal M^{\operatorname{IG}}_{i\to j}.
\]
