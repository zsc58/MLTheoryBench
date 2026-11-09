# Problem

## Setup

Let I be a finite nonempty index set, let Z be an embedding space, and let A be a set of categorical attributes. Each sample i in I has an embedding z_i in Z and an attribute a_i in A. Let s: Z x Z -> R be a symmetric similarity function, and let alpha be a real number such that s(z_i,z_i) >= alpha for every i in I. Define i~j iff s(z_i,z_j) >= alpha and a_i = a_j, and define B(i) = {j in I: i~j}. Thus ~ is reflexive and symmetric.

Let C_1,...,C_K be a partition of I into nonempty initial clusters, with K >= 1. For each k define the candidate family F_k = {B(i) intersect C_k: i in C_k}. Initialize R_k = emptyset and U_k = C_k. While U_k is nonempty, choose any r in C_k maximizing |B(r) intersect U_k|, add r to R_k, assign all points in B(r) intersect U_k to r, and remove those points from U_k. Continue until U_k is empty. Let R be the union of all R_k. Finally, let OPT_k be the minimum cardinality of a subfamily of F_k whose union is C_k.

## Task

Prove that this procedure terminates and, for every k, every sample i in C_k assigned to representative r in R_k satisfies
\[
s(z_i,z_r)\ge\alpha\quad\text{and}\quad a_i=a_r,
\]
and the number of representatives obeys
\[
|R_k|\le (1+\ln |C_k|)\,OPT_k.
\]
