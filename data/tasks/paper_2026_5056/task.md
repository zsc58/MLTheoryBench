# Problem

## Setup

Let \(n,k,\ell\) be integers with \(n\ge 0\) and \(1\le \ell\le k\). Write \([k]=\{0,1,\ldots,k-1\}\) for the alphabet and \(I_n=\{1,\ldots,n\}\) for the coordinate set, with \(I_0=\varnothing\). Identify \([k]^n\) with the functions from \(I_n\) to \([k]\).

Let \(H\subseteq[k]^n\). For \(S\subseteq I_n\), write \(H|_S=\{h|_S:h\in H\}\). An \((\ell+1)\)-pseudo-cube in \([k]^S\) is a nonempty set \(B\subseteq[k]^S\) such that, for every \(b\in B\) and every \(j\in S\), there are at least \(\ell\) distinct elements \(b'\in B\) satisfying \(b'_j\ne b_j\) and \(b'_i=b_i\) for all \(i\in S\setminus\{j\}\).

Say that \(S\) is \(\ell\)-DS-shattered by \(H\) if \(H|_S\) contains an \((\ell+1)\)-pseudo-cube. Define the \(\ell\)-DS dimension of \(H\) as the maximum cardinality of an \(\ell\)-DS-shattered coordinate set, with dimension \(0\) if no such set exists. Suppose this dimension is \(d\), where \(0\le d\le n\).

## Task

Prove the following sharp inequality:
\[
|H|\le \sum_{i=0}^{d}\binom ni (k-\ell)^i\ell^{\,n-i}.
\]
In this sum, use the convention \(0^0=1\).

Moreover, for every such \(n,k,\ell\) and every integer \(d\) satisfying \(0\le d\le n\) and \((\ell<k\text{ or }d=0)\), prove that there exists a class \(H\subseteq[k]^n\) of \(\ell\)-DS dimension exactly \(d\) attaining equality.
