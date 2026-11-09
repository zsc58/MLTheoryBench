# Reference Proof

## Proof Structure

For each tree, identify the nodes whose parent edges separate the two reached leaves. The squared difference of each non-root embedding coordinate is its edge weight exactly on those separating nodes, while the root coordinate cancels. The audited edge-sum identity then gives the tree path distance. Concatenation and global normalization give the forest isometry. Cauchy-Schwarz yields the score Lipschitz bound, and a strict margin-radius inequality preserves the classification sign.

## Complete Proof

Fix a tree indexed by `j` and two inputs `x,x'`. Let `P_j(x,x')` be the non-root nodes whose parent edges lie on the unique path joining the leaves reached by `x` and `x'`. By the zero-leaf assumption and the definition `eta_j(v)=(q_j(parent(v))+q_j(v))/2`, summing the edge weights along that leaf-to-leaf path telescopes to the sum of the internal node weights. Hence
\[
 d_j(x,x')=\sum_{v\in P_j(x,x')}\eta_j(v).
\]

The root coordinate of the tree embedding is constant, so it contributes zero to the squared feature difference. For a non-root node `v`, the coordinate is `sqrt(eta_j(v)) 1{x in S_{j,v}}`. Its squared difference between `x` and `x'` is therefore `eta_j(v)` when exactly one input belongs to `S_{j,v}`, and zero otherwise. Exactly-one membership is equivalent to the parent edge of `v` separating the two reached leaves, so
\[
 \|\phi_j(x)-\phi_j(x')\|_2^2
 =\sum_{v\in P_j(x,x')}\eta_j(v)=d_j(x,x').
\]

The forest embedding is the concatenation of the tree embeddings, hence squared Euclidean distances add:
\[
 \|\Phi(x)-\Phi(x')\|_2^2=\sum_j d_j(x,x')=D(x,x').
\]
Since `psi=Phi/sqrt(M)` and `rho=D/M`, where `M>0`,
\[
 \|\psi(x)-\psi(x')\|_2^2=\rho(x,x').
\]

For `g(x)=b+\langle w,\psi(x)\rangle`, the intercept cancels and Cauchy-Schwarz gives
\[
 |g(x)-g(x')|
 \le \|w\|_2\,\|\psi(x)-\psi(x')\|_2
 =\|w\|_2\sqrt{\rho(x,x')}.
\]
If `y in {-1,1}` and `m=y g(x)>0`, then for any `x'` satisfying `rho(x,x')<(m/\|w\|_2)^2` (with the zero-weight case being constant-score and therefore trivially robust), the bound implies `|g(x')-g(x)|<m`. Thus `y g(x') >= y g(x)-|g(x')-g(x)|>0`, so the predicted sign at `x'` equals that at `x`.
