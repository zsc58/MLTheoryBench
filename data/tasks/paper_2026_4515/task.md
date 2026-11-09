# Problem

## Setup

A document is \(D=(P,C,Y)\), where \(P\) is a prompt, \(C\) is a finite set of claims, and \(Y(c)\in\{0,1\}\) indicates whether claim \(c\) is factual. Let
\[
A(D)=\{c\in C:Y(c)=1\}.
\]
Let \(n\ge1\) be an integer and let \(D_1,\ldots,D_{n+1}\) be i.i.d. documents. Let \(U_1,\ldots,U_{n+1}\) be independent uniform random variables on \((0,1)\), independent of all the documents.

Fix a measurable estimated factuality-score function \(\hat p(P,c)\in[0,1]\) and a measurable grouping function \(g(P,C)\in\{1,\ldots,K\}\), where \(K\ge1\) is finite. These functions are fixed independently of the calibration and test documents. Fix also a measurable rule for resolving equal claim scores, using only the prompt, claim set, and scores, identically for all documents.

For a score function \(p\), threshold \(\tau\in[0,1]\), and \(u\in(0,1)\), define a retained claim set \(F(p,\tau,u;P,C)\) as follows. Write \(N=|C|\), and order the claims as \(c_{(1)},\ldots,c_{(N)}\) by decreasing \(p(P,c)\), using the fixed tie rule. Define
\[
\Pi_0=1,\qquad \Pi_j=\prod_{\ell=1}^{j}p(P,c_{(\ell)})\quad(1\le j\le N),
\]
and
\[
L=L(p,\tau;P,C)
=\max\bigl(\{0\}\cup\{j\in\{1,\ldots,N\}:\Pi_j>\tau\}\bigr).
\]
Set
\[
\gamma=\gamma(p,\tau;P,C)=
\begin{cases}
\dfrac{\Pi_L-\tau}{\Pi_L-\Pi_{L+1}},&L<N\text{ and }\Pi_L>\Pi_{L+1},\\[6pt]
0,&\text{otherwise}.
\end{cases}
\]
The filter is
\[
F(p,\tau,u;P,C)=
\begin{cases}
\{c_{(j)}:1\le j\le L+1\},&u<\gamma,\\
\{c_{(j)}:1\le j\le L\},&u\ge\gamma.
\end{cases}
\]
A prefix of length zero is the empty set. These conventions also apply when \(C\) is empty.

Write \(G_i=g(P_i,C_i)\) and \(A_i=A(D_i)\). For \(i=1,\ldots,n+1\), define
\[
E_i=\inf\{\tau\in[0,1]:F(\hat p,\tau,U_i;P_i,C_i)\subseteq A_i\}.
\]
Fix \(\alpha\in(0,1)\). For each group \(k\), let
\[
I_k=\{i\le n:G_i=k\},\qquad m_k=|I_k|,\qquad
r_k=\lceil(m_k+1)(1-\alpha)\rceil.
\]
Sort the scores \(E_i\) with \(i\in I_k\) increasingly, counting repetitions. Let \(q_k\) be their \(r_k\)-th order statistic when \(r_k\le m_k\), and set \(q_k=1\) when \(r_k=m_k+1\). Define
\[
F_{n,\alpha}(P_{n+1},C_{n+1})
=F(\hat p,q_{G_{n+1}},U_{n+1};P_{n+1},C_{n+1}).
\]

## Task

Prove that for every group \(k\) with \(\Pr(g(P_{n+1},C_{n+1})=k)>0\),
\[
\Pr\!\left(F_{n,\alpha}(P_{n+1},C_{n+1})\subseteq A_{n+1}\mid g(P_{n+1},C_{n+1})=k\right)\ge1-\alpha.
\]
