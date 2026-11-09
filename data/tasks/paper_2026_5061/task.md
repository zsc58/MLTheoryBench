# Problem

## Setup

Let n and d be positive integers with n >= d. Let A be an n x d real matrix of full column rank, and let y be an n x 1 real response vector. The ordinary least-squares prediction is

A(A^T A)^(-1)A^T y.

For matrices W_Q, W_K, W_V, W_FFN in R^{d x d} and W_P in R^{d x 1}, define the output of a single-layer linear-attention Transformer on A by

T(A; W_Q,W_K,W_V,W_FFN,W_P)
 = (1/n)(A W_Q)(A W_K)^T(A W_V)W_FFN W_P.

## Task

Prove that for every such A and y, there exist explicitly constructible parameter matrices W_Q, W_K, W_V, W_FFN, and W_P for which

T(A; W_Q,W_K,W_V,W_FFN,W_P) = A(A^T A)^(-1)A^T y.
