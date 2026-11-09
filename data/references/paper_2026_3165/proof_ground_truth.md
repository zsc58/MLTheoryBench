# Reference Proof

## Proof Structure

Reduce the NP-complete clique problem to a threshold decision for the optimization problem. Verify that restricting the clique inputs to 1<k<n preserves hardness and that the resulting optimization instance has a polynomial-size exact encoding. For a graph adjacency matrix, establish a universal upper bound, show that a k-clique attains the bound at R=1/sqrt(k), and use the simplex quadratic bound in the absence of a k-clique to obtain a uniform strict gap.

## Complete Proof

We use two standard independent results. The clique decision problem, with a graph and a positive integer k as input, is NP-complete. The Motzkin--Straus theorem states that for a nonempty finite simple loopless graph H with adjacency matrix B and clique number omega(H),
\[
\max_{y\ge0,\ \sum_i y_i=1}y^\top B y=1-\frac1{\omega(H)}.
\]
Here nonempty means that the vertex set is nonempty; edges are not required.

The restriction 1<k<n preserves clique NP-hardness. For an input graph with N vertices and 2<=k<=N, append one isolated vertex. This preserves the existence of a k-clique and ensures 1<k<N+1. Inputs with k=1 or k>N can be decided directly and mapped to fixed restricted yes or no instances: respectively, a graph on three vertices with one edge and k=2, or an edgeless graph on three vertices and k=2. This also handles a graph with no vertices. The transformation is polynomial in the input length.

Now let G be a simple undirected loopless graph on n vertices, let 1<k<n, let A=A(G) be its adjacency matrix, and set R=1/sqrt(k). Write
\[
\operatorname{OPT}(A,R)=\max\{x^\top A x:\|x\|_1\le1,\ \|x\|_2=R\}.
\]
The feasible set is nonempty: a vector with first coordinate R and all other coordinates zero is feasible because 0<R<1. The feasible set is closed and bounded, hence compact. The objective is continuous, so the maximum exists and is finite. The convention for infeasible instances therefore has no role in the reduction.

Since A has nonnegative entries, replacing any feasible x by |x| preserves both norms and does not decrease the objective. Thus it suffices to consider x>=0. Because the graph is loopless and every off-diagonal adjacency entry is at most one,
\[
x^\top A x\le\sum_{i\ne j}x_i x_j
=(\|x\|_1)^2-\|x\|_2^2
\le1-R^2.
\]
Hence OPT(A,R)<=1-R^2=1-1/k.

If G contains a clique C of size k, define x_i=1/k for i in C and x_i=0 otherwise. Then ||x||_1=1, ||x||_2=1/sqrt(k)=R, and all ordered pairs of distinct vertices in C are edges. Therefore
\[
x^\top A x=\frac{k(k-1)}{k^2}=1-\frac1k=1-R^2.
\]
Together with the upper bound, this gives OPT(A,R)=1-1/k.

Conversely, suppose G has no k-clique. Its clique number satisfies 1<=omega(G)<=k-1, since n>=3. For any feasible x>=0, let s=||x||_1>0 and y=x/s. Then y lies in the standard simplex. The graph and simplex hypotheses of the Motzkin--Straus theorem hold, so
\[
y^\top A y\le1-\frac1{\omega(G)}\le1-\frac1{k-1}.
\]
Consequently,
\[
x^\top A x=s^2y^\top A y
\le s^2\left(1-\frac1{k-1}\right)
\le1-\frac1{k-1}
<1-\frac1k=1-R^2.
\]
The second inequality uses s<=1 and 1-1/(k-1)>=0. It therefore also holds when k=2, in which case the bound is zero. This is a uniform bound on all feasible nonnegative vectors, and the absolute-value comparison extends it to all feasible vectors. Thus
\[
\operatorname{OPT}(A,R)\le1-\frac1{k-1}<1-\frac1k.
\]
We have proved
\[
\operatorname{OPT}(A(G),1/\sqrt{k})\ge1-1/k
\quad\Longleftrightarrow\quad
G\text{ contains a clique of size }k,
\]
and the optimum equals the threshold whenever the inequality holds.

For completeness, the radius is specified exactly by the input integer k, not by a numerical approximation. The constraint ||x||_2=1/sqrt(k) is equivalently sum_i x_i^2=1/k. Thus the restricted instance can be described using the 0--1 matrix A and the rational squared radius 1/k; the threshold (k-1)/k is also rational. These descriptions have polynomial length and are constructible in polynomial time. Exact computation of the optimum would decide the displayed threshold question and hence the restricted clique problem. Therefore computing the stated optimum is NP-hard.
