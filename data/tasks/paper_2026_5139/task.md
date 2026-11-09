# Problem

## Setup

Let \(X\) be a Polish space. For a binary function \(h:X\to\{0,1\}\), a target \(c:X\to\{0,1\}\), and a sample \(S=(x_1,\ldots,x_m)\in X^m\) of length \(m\in\{0,1,2,\ldots\}\), write
\[
\operatorname{err}_c(h;S)=
\begin{cases}
\displaystyle\frac1m\sum_{i=1}^m\mathbf1\{h(x_i)\ne c(x_i)\},&m\geq1,\\
0,&m=0.
\end{cases}
\]
For \(S,T\in X^m\), define the one-sided ghost gap
\[
\Gamma_h^c(S,T)=\operatorname{err}_c(h;T)-\operatorname{err}_c(h;S).
\]
For a class \(\mathcal C\) of binary functions and \(\epsilon\in\mathbb R\), let
\[
E_{\mathcal C,c,m,\epsilon}
 =\{(S,T)\in X^m\times X^m:\exists h\in\mathcal C,
 \Gamma_h^c(S,T)\geq\epsilon/2\}.
\]

Say that \(\mathcal C\) has the event-completion property if, for every Borel measurable target \(c\), every \(m\in\{0,1,2,\ldots\}\), every \(\epsilon>0\), and every Borel probability measure \(P\) on \(X\), the set \(E_{\mathcal C,c,m,\epsilon}\) is measurable in the completion of \(P^m\otimes P^m\).

Say that \(\mathcal C\) has the supremum-Borel property if, for every target \(c:X\to\{0,1\}\) and every \(m\in\{0,1,2,\ldots\}\), the map
\[
(S,T)\longmapsto \sup_{h\in\mathcal C}\Gamma_h^c(S,T)
\]
is Borel measurable from \(X^m\times X^m\) into the extended real line with its Borel \(\sigma\)-algebra. Here the supremum of the empty set is \(-\infty\).

Let \(\Theta\) be a standard Borel space and let \(e:\Theta\times X\to\{0,1\}\) be jointly Borel measurable. Put
\[
\mathcal C_e=\{x\mapsto e(\theta,x):\theta\in\Theta\}.
\]

Finally, let \(A\subseteq\mathbb R\) be analytic and non-Borel, and define the class on \(\mathbb R\)
\[
\mathcal C_A=\{0\}\cup\{\mathbf1_{\{a\}}:a\in A\}.
\]

## Task

Prove the following integrated claim.

1. \(\mathcal C_e\) has the event-completion property. In fact, for every Borel measurable \(c\), every \(m\in\{0,1,2,\ldots\}\), and every \(\epsilon\in\mathbb R\), the event \(E_{\mathcal C_e,c,m,\epsilon}\) is analytic in \(X^m\times X^m\), and hence is measurable in the completion of every finite Borel measure on that space.

2. \(\mathcal C_A\) has the event-completion property, but does not have the supremum-Borel property.
