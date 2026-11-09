# Problem

## Setup

Let `n>=2` items have positive weights `w_1,...,w_n` satisfying

`max_i w_i/min_i w_i <= h`,

where `h` is fixed. For distinct items define

`b_{ij}=w_j/(w_i+w_j)`.

Independently for each unordered pair `{i,j}`, an observation edge is present with probability `a_{ij}=a_{ji}`. Assume that, for some `rho=rho_n in (0,1]` and fixed `s>1`,

`a_{ij} in [rho,1]`,

and, for every `i`,

`n sum_{j!=i} a_{ij}^2 <= s (sum_{j!=i}a_{ij})^2`.

Conditional on the observation graph, comparison outcomes are mutually independent across all present unordered edges and repetitions, and are independent of the graph. For every present edge `{i,j}` and every repetition `ell=1,...,k`, let `Y_{ij}^{(ell)}` denote the indicator that item `j` defeats item `i`. Thus

`Pr(Y_{ij}^{(ell)}=1)=b_{ij}` and `Y_{ji}^{(ell)}=1-Y_{ij}^{(ell)}`.

Set

`hat b_{ij}=k^{-1}sum_{ell=1}^k Y_{ij}^{(ell)}`

on a present edge, and set `hat b_{ij}=0` on an absent edge.

Let

`r_i=w_i/(sum_l w_l)`.

For a realised observation graph with positive maximum degree `D`, define a Markov matrix `P` by

`P_{ij}=b_{ij}/D` on present off-diagonal edges, `P_{ij}=0` on absent off-diagonal edges, and `P_{ii}=1-sum_{j!=i}P_{ij}`.

Define `hat P` in the same way with `b_{ij}` replaced by `hat b_{ij}`. If `D=0`, set `P=hat P=I`. Let `hat r` be the stationary distribution of `hat P` having minimum Euclidean norm; this selects a unique vector even if the stationary distribution is not otherwise unique.

Let `lambda_2(P)` be the eigenvalue of `P` with second-largest absolute value, counting multiplicities and taking the trivial eigenvalue `1` first. Fix `0<gamma<1` and assume

`Pr(1-|lambda_2(P)|<=gamma)<=n^{-5}`.

## Task

Prove that there are constants `c_0,c_1,c_2>0`, with `c_0` allowed to depend on `h,gamma` and satisfying `c_0>=10240h^2/gamma^2`, and `c_1,c_2` depending only on `h,s`, such that, whenever

`n rho>=c_0 log n` and integer `k>=5`, then for all sufficiently large `n`,

`||hat r-r||_infinity/||r||_infinity <= (c_1/gamma+c_2) sqrt(log n/(n rho k))`

with probability at least `1-O(n^{-5})`.
