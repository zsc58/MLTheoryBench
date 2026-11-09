# Problem

## Setup

Let `N\ge2` data points be partitioned into `K\ge2` indexed clusters with initial sizes `n_1,\ldots,n_K\ge1` and `\sum_i n_i=N`. During reassignment, indexed clusters may become empty. Define
\[
Q=\sum_{j=1}^K n_j^2,
\qquad
S=\frac{Q}{N},
\qquad
S_i=\frac{Q-n_i^2}{N-n_i}
\]
whenever `n_i<N`.  For a state with at least two nonempty clusters, define
\[
U=\sum_{i=1}^K\frac{n_i}{N}\left(1-\frac{|n_i-S_i|}{N}\right).
\]
Empty indexed clusters contribute zero.  If a state has exactly one nonempty cluster, set `U=0`.

A reassignment of `m` points means moving those points one at a time to (possibly different) indexed clusters; write `m=\varepsilon N`, where `\varepsilon\in[0,1]` and `m` is an integer.

## Task

Prove that for every such reassignment, the initial and final scores satisfy
\[
\Delta U=0\quad\text{when }\varepsilon=0,
\qquad\text{and}\qquad
|\Delta U|<3\varepsilon\quad\text{when }\varepsilon>0.
\]
In particular, `|\Delta U|\le3\varepsilon` for all admissible `\varepsilon`.
