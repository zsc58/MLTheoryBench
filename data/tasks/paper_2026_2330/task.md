# Problem

## Setup

Let \((F,\le)\) and \((R,\le)\) be posets, each with a bottom and a top element. For \(S\subseteq R\), write
\[
\uparrow S=\{r\in R:\text{ there is }s\in S\text{ with }s\le r\}.
\]
An antichain is a subset whose distinct elements are incomparable.

Let \(I\) be a Polish space with a full-support Borel probability measure \(\mu\), and let
\[
p:I\to F,\qquad r:I\to R
\]
be functionality and resource maps. Assume that, for every \(g\in F\), the set
\[
\{r(i):i\in I,\ g\le p(i)\}
\]
is nonempty and every element of this set lies above a minimal element of the same set. Fix \(f\in F\), and let \(O\subseteq R\) be the antichain of minimal elements of
\[
\{r(i):i\in I,\ f\le p(i)\}.
\]

A finite valid history \(H\) is a finite set of queried triples \((i,p(i),r(i))\), with distinct implementations. Define \(M_f(H)\) to be the antichain of minimal resources among entries satisfying \(f\le p(i)\).

For every implementation \(i\) and every finite valid history \(H\), suppose given optimistic estimates
\[
\widehat p(i,H)\in F,\qquad \widehat r(i,H)\in R
\]
satisfying
\[
p(i)\le\widehat p(i,H),\qquad \widehat r(i,H)\le r(i).
\]
For a history \(H\), define the admissible set
\[
A(H)=\left\{i\in I:\begin{array}{l}
i\text{ has not been queried in }H,\\
f\le\widehat p(i,H),\\
\widehat r(i,H)\notin\uparrow M_f(H)
\end{array}\right\}.
\]
Assume that \(A(H)\) is Borel and has positive \(\mu\)-measure for every finite valid history \(H\).

Specify measurable dependence of acceptance on the queried implementations as follows. For \(n\ge0\), let
\[
D_n=\{(i_1,\ldots,i_n)\in I^n:i_1,\ldots,i_n\text{ are distinct}\},
\qquad
H(i_1,\ldots,i_n)=\{(i_j,p(i_j),r(i_j)):1\le j\le n\}.
\]
Here \(D_0\) consists of the empty tuple and its associated history is empty. Assume that, for every \(n\ge0\),
\[
G_n=\{((i_1,\ldots,i_n),i)\in D_n\times I:
 i\in A(H(i_1,\ldots,i_n))\}
\]
is Borel in \(D_n\times I\).

Start with \(H_0=\varnothing\). At round \(t=0,1,2,\ldots\), draw fresh independent proposals with law \(\mu\) until a point of \(A(H_t)\) is obtained, query that point, and append its true triple to form \(H_{t+1}\). All proposal draws are independent across rounds as well as within each round. The procedure has no sample budget.

For \(r_*\in O\), define its witness set by
\[
W_{r_*}=\{i\in I:f\le p(i),\ r(i)=r_*\}.
\]

## Task

Prove the following integrated theorem.

Almost surely, for every \(r_*\in O\) and every \(i_*\in W_{r_*}\), exactly one of these alternatives holds:

1. \(i_*\) is queried at a finite round;
2. \(i_*\) is never queried and is not admissible at some finite round;
3. \(i_*\) is never queried and remains admissible at every round.

In either of the first two alternatives, \(r_*\in\uparrow M_f(H_t)\) at some finite round \(t\).

Moreover, assume that \(O\) is finite and that every \(W_r\), \(r\in O\), is Borel with \(\mu(W_r)>0\). Prove that almost surely there is a finite random \(N_0\) such that, for every \(t\ge N_0\),
\[
\uparrow M_f(H_t)=\uparrow O.
\]
