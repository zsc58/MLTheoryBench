# Problem

## Setup

Let \(F\) be a finite set of features or feature groups equipped with a partial order \(\prec\), representing known directional constraints.  An order-respecting permutation is a permutation \(\pi\) of \(F\) in which \(a\prec b\) implies that \(a\) appears before \(b\).  Choose \(\pi\) uniformly from all order-respecting permutations.

For a feature \(i\in F\), let \(\operatorname{Pre}_\pi(i)\) be the set of features before \(i\) in \(\pi\).  Let \(v:2^F\to\mathbb R\) be arbitrary, and define
\[
 \phi_i=\mathbb E\bigl[v(\operatorname{Pre}_\pi(i)\cup\{i\})-v(\operatorname{Pre}_\pi(i))\bigr].
\]

A subset \(A\subseteq F\) respects the order if it is a down-set: whenever \(b\in A\) and \(a\prec b\), then \(a\in A\).  For \(S\subseteq F\setminus\{i\}\), call \(S\) admissible for \(i\) when both \(S\) and \(S\cup\{i\}\) are down-sets.

For \(A\subseteq F\), let \(L(A)\) be the number of order-respecting permutations of the order induced on \(A\), with \(L(\varnothing)=1\).

For the modular rules below, consider pairwise disjoint subsets \(A_1,\ldots,A_r\) of \(F\), called modules. They are unrelated if no elements of distinct modules are comparable. They are fully ordered if every element of \(A_j\) precedes every element of \(A_k\) whenever \(j<k\). A relation-free module has no comparable distinct elements; a completely ordered module is a chain.

## Task

Prove the following integrated theorem.

For every \(i\in F\) and every admissible \(S\subseteq F\setminus\{i\}\),
\[
 \Pr\{\operatorname{Pre}_\pi(i)=S\}
 =\frac{L(S)\,L(F\setminus(S\cup\{i\}))}{L(F)},
\]
and this probability is zero for non-admissible \(S\).  Consequently,
\[
 \phi_i=
 \sum_{\substack{S\subseteq F\setminus\{i\}:\\S,\,S\cup\{i\}\text{ are down-sets}}}
 \frac{L(S)\,L(F\setminus(S\cup\{i\}))}{L(F)}
 \bigl[v(S\cup\{i\})-v(S)\bigr].
\]

Also prove that the counts used in these weights are recursively computable by
\[
 L(A)=\sum_{a\in\operatorname{Min}(A)}L(A\setminus\{a\})
 \quad(A\ne\varnothing),
\]
where \(\operatorname{Min}(A)\) denotes the minimal elements of the induced order.  Derive the associated modular rules: unrelated modules interleave with the multinomial factor, fully ordered modules have multiplicative counts, a relation-free module of size \(m\) has count \(m!\), and a completely ordered module has count \(1\).
