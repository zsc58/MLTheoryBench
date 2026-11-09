# Problem

## Setup

Let k >= 4 be an integer and let H = C_k be the chordless cycle graph on vertices 1,...,k, with edges (i,i+1) (indices modulo k). Define

C(H) = {X in R^{k x k}: X = X^T, X is positive semidefinite, X_{ii}=1 for all i, and X_{ij}=0 whenever (i,j) is not an edge of H and i != j}.

Thus entries on cycle edges are allowed to be zero. Define the cycle-edge mean

m_H(X) = (1/k) sum_{i=1}^k X_{i,i+1}.

For a threshold t in [-1,1], let F_t(H) = {X in C(H): m_H(X) >= t}.

## Task

Prove the following integrated theorem.

For every X in C(C_k),

m_{C_k}(X) <=
  1/2,                         if k is even,
  1/(2 cos(pi/k)),             if k is odd.

Consequently, F_t(C_k) is empty whenever t is larger than the applicable bound.
