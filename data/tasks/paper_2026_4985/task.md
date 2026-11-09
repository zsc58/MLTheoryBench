# Problem

## Setup

For positive integers `s,t`, let `M in {+1,-1}^{s x t}` and let `D` be a positive integer. The signed rank-one L1 approximation decision problem asks whether there exist `u in R^s` and `v in R^t` such that

`||M-uv^T||_1 = sum_{i=1}^s sum_{j=1}^t |M_ij-u_i v_j| <= D`.

Assume this signed decision problem is NP-hard, and that every yes-instance has a feasible pair with all coordinates of `u` and `v` in `{+1,-1}`.

For a binary matrix `X in {0,1}^{m x n}` and a positive integer `T`, rank-one L1-NMF asks whether there exist nonnegative vectors `w in R_+^m` and `h in R_+^n` with `||X-wh^T||_1 <= T`.

## Task

Prove that rank-one L1-NMF remains NP-hard when the input matrix is binary. Specifically, given `(M,D)`, construct a binary matrix `X in {0,1}^{2s x 2t}` and threshold `T` in polynomial time such that

`(M,D)` is a yes-instance if and only if `(X,T)` is a yes-instance, and conclude the NP-hardness result.
