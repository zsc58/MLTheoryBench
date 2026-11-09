# Problem

## Setup

Let `X` be an input space and let `j=1,...,J` index a finite collection of rooted binary trees. Tree `j` has finitely many nodes, directed parent-to-child edges, and measurable regions `S_{j,v} subseteq X` such that the root region is `X` and the two child regions are disjoint and partition their parent's region. Every input reaches a leaf `ell_j(x)`; write `sigma_j(x,x')` for the unique node path joining the two reached leaves.

Assign each node a nonnegative weight `q_j(v)`, and assume every leaf has weight zero. Define the tree path distance
\[
 d_j(x,x')=\sum_{v\in\sigma_j(x,x')}q_j(v).
\]
For each non-root node define the edge weight
\[
 eta_j(v)=\frac{q_j(parent(v))+q_j(v)}{2}.
\]
The root-incoming edge has weight zero by convention. Let `phi_j(x)` have one constant root coordinate `sqrt(q_j(root)/2)` and, for every non-root node, coordinate `sqrt(eta_j(v)) 1{x in S_{j,v}}`. Concatenate these vectors over all trees to obtain `Phi(x)`. Let
\[
 M=\sum_{j=1}^J\sum_v q_j(v)>0,\qquad psi(x)=\Phi(x)/\sqrt M,
\]
and define the normalized forest pseudodistance `rho(x,x')=(sum_j d_j(x,x'))/M`.

For parameters `b in R` and `w` in the embedding space, define the linear score `g(x)=b+<w,psi(x)>`.

## Task

Prove that for all `x,x' in X`,
\[
 \|\Phi(x)-\Phi(x')\|_2^2=\sum_{j=1}^J d_j(x,x')
 \quad\text{and}\quad
 \|\psi(x)-\psi(x')\|_2^2=\rho(x,x').
\]
Consequently, prove the deterministic Lipschitz bound
\[
 |g(x)-g(x')|\le \|w\|_2\sqrt{\rho(x,x')}.
\]
Finally, for a label `y in {-1,1}` with signed margin `m=y g(x)>0`, prove that every `x'` with `rho(x,x')<(m/\|w\|_2)^2` has the same predicted sign as `x` (and note that a zero weight vector gives a constant score and is trivially robust).
