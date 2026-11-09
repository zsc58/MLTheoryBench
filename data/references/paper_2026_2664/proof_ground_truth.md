# Reference Proof

## Theorem-Critical Obligations

1. Verify that the prescribed geometric path distance has a well-defined metric realization, and derive the cell-edge bound and domination by the address-tree metric.
2. Derive the tail bound for every finite vertex, extend it to the completion, and establish compactness using finite nets.
3. Construct a vector-valued ReLU interpolant on the distinct finite-window parent centers, with explicit network complexity. Do not regard the specialized external citation as a completed derivation.
4. Prove exact recursive agreement of centers and cells through the chosen level.
5. Verify the choice of truncation depth and the finite-window and epsilon-dependent complexity bounds, including their conventions and constant dependencies.

All five obligations are closed below.

## Complete Proof

### Metric Realization and Edge Bounds

Write V_geo for the quotient of address vertices by equality of both center and cell. Retain each genealogical edge after projection into V_geo with its own weight, permitting parallel edges and zero weights. The infimum of lengths of finite undirected walks defines a finite pseudometric rho_cell: connectivity gives finiteness, reversal gives symmetry, concatenation gives the triangle inequality, and the empty walk gives zero diagonal. Identify vertices at zero rho_cell distance. If v and v' have zero distance, the triangle inequality gives rho_cell(v,w)=rho_cell(v',w), so distance is independent of representatives. The induced distance separates distinct equivalence classes by definition and is therefore a metric d_cell. Its completion is X_cell.

For an edge whose parent alpha has depth ell, its cell weight is

\[
w_{\rm cell}(\alpha,\alpha k)=s^\ell\lambda_{\max}d_{H,p}(C_\alpha,C_{\alpha k}).
\]

The recursive rule gives C_{alpha k} subset C_alpha subset C_empty. Both cells are nonempty, and the root ball has ell_p diameter 2 lambda_max. Thus

\[
d_{H,p}(C_\alpha,C_{\alpha k})\leq\operatorname{diam}_p(C_\alpha)\leq2\lambda_{\max},
\qquad
w_{\rm cell}(\alpha,\alpha k)\leq2\lambda_{\max}^2s^\ell.
\]

The corresponding address-tree edge has weight s^{ell+1}, hence its cell weight is at most (2 lambda_max^2/s) times its tree weight. Projecting the unique tree path and using the infimum defining the cell distance proves

\[
d_{\rm cell}(\pi u,\pi v)\leq\frac{2\lambda_{\max}^2}{s}d_{\rm tree}(u,v).
\]

Here pi includes both geometric identification and zero-distance metric identification. No positive cell-edge assumption is needed. The source CFG bounds are Euclidean; an ell_p residual estimate, if needed, would require the norm-comparison factor. It is not needed for the cell-edge argument.

### Tail Bound and Compactness

Let Y_L be the image in X_cell of all address vertices through level L, carrying the restriction of the full metric. It is finite and nonempty. A vertex represented by an address of depth m>L is connected to its depth-L ancestor by projected edges whose total length is bounded by

\[
\sum_{\ell=L}^{m-1}2\lambda_{\max}^2s^\ell\leq\tau_L,
\qquad
\tau_L=\frac{2\lambda_{\max}^2s^L}{1-s}.
\]

Vertices represented at depth at most L already lie in Y_L. Therefore every vertex of the metrized full space has distance at most tau_L from Y_L.

The function z -> dist(z,Y_L) is 1-Lipschitz by the triangle inequality. Every point of the completion is a limit of vertices, so this same bound holds throughout X_cell. Since Y_L is a subset of X_cell, the reverse directed Hausdorff distance is zero. Consequently

\[
d_H^{\overline d_{\rm cell}}(Y_L,X_{\rm cell})\leq\tau_L.
\]

For each eta>0, choose L with tau_L<eta. Then the finite set Y_L is an eta-net for X_cell. Thus X_cell is totally bounded. It is complete by construction, and is compact: from any sequence, successively select infinite subsequences in one member of finite covers by balls of radii tending to zero; the diagonal subsequence is Cauchy and converges by completeness. This is the standard complete-plus-totally-bounded compactness argument, with both hypotheses verified.

### Finite-Window Geometry

Fix L>=2. Let S_L be the set of distinct centers with address depths 0 through L-1, and set N=|S_L|. Removing repeated centers causes no inconsistent outputs because r is a function. Counting addresses gives

\[
N\leq M_L:=\sum_{\ell=0}^{L-1}K^\ell=\frac{K^L-1}{K-1}.
\]

For an address alpha of depth m<=L-1, telescoping the center recursion and using the Euclidean CFG bound gives

\[
\|x_\alpha-x_0\|_2\leq\lambda_{\max}\sum_{j=1}^{m}s^j\leq\frac{\lambda_{\max}s(1-s^{L-1})}{1-s}.
\]

Hence

\[
\operatorname{diam}_2(S_L)\leq\frac{2\lambda_{\max}s(1-s^{L-1})}{1-s}.
\]

When N>=2, the minimum nonzero Euclidean separation delta_{0,L} is positive because S_L is finite. Dividing the last estimate by this separation proves that the Euclidean aspect ratio is at most B_L and B_L>=1. For a singleton, the stated B_L=1 convention is used without evaluating a minimum over an empty set. In the present source contract, L>=2 and nonzero separated root residuals in fact ensure multiple distinct parents, but the convention also covers the general interpolation endpoint.

### Explicit ReLU Interpolation

Enumerate S_L as distinct inputs z_1,...,z_N and vectorize the prescribed outputs y_i=r(z_i) in R^{dK}. For N=1, the constant affine output y_1 interpolates the sole input.

For N>=2, choose a in R^d such that a dot (z_i-z_j) is nonzero for every i!=j. Such an a exists: the forbidden set is a finite union of proper linear hyperplanes, which cannot exhaust R^d. One elementary justification is that the product of their nonzero defining linear polynomials is a nonzero polynomial and cannot vanish identically on R^d. Order the inputs so that t_i=a dot z_i satisfy t_1<...<t_N. Define vector slopes

\[
b_i=\frac{y_{i+1}-y_i}{t_{i+1}-t_i},\qquad i=1,\ldots,N-1.
\]

For scalar t set

\[
h(t)=y_1+b_1(t-t_1)+\sum_{i=2}^{N-1}(b_i-b_{i-1})\operatorname{ReLU}(t-t_i).
\]

This function takes value y_1 at t_1. On every interval [t_i,t_{i+1}] its slope is b_i, because the slope increments telescope. Induction over the intervals gives h(t_i)=y_i for every i. Empty sums are allowed when N=2.

Implement the linear term t as ReLU(t)-ReLU(-t). The remaining N-2 hinge terms are already ReLU units. Thus h(a dot x) is a ReLU MLP with one hidden layer of width at most N and an affine output in R^{dK}. Reshape that output to R^{d x K}. The resulting predictor r_hat_L satisfies

\[
\widehat r_L(x_\alpha)=r(x_\alpha),\qquad |\alpha|\leq L-1.
\]

Its width is O(N)=O(K^L), depth is bounded by a universal constant, and its parameter count is O(N(d+dK)+dK). The construction uses unrestricted real weights, exactly as in the supplied network definition; no weight-size or precision bound is being asserted. In particular, bounded depth is at most

\[
O\!\left(K^{3L/2}\sqrt{L\log K}\left[1+\frac{\log_+(B_L)}{L\log K}\right]\right),
\]

because K>=2, L>=2, and the bracket is at least one. This closes the required interpolation and complexity obligation directly. The source's specialized external interpolation theorem is not used as a black box or represented as independently proved.

### Exact Recursive Agreement

Roll out r_hat_L with the same root, scale, and Voronoi rule. The root center and cell agree. Assume agreement through level ell<L. Every level-ell parent center belongs to S_L, so the interpolated field value equals the true field value at that center. The child-center formula therefore gives identical children. The parent cell and all sibling child centers are identical in both constructions, so the defining Voronoi inequalities give identical child cells, including all ties. Induction proves exact address-level equality of centers and cells through level L. Their geometric and metric images are consequently the same Y_L.

This conclusion identifies the rollout's centers, cells, and image truncation. It does not substitute the intrinsic path metric of a finite graph for the restriction of the full metric used in Y_L.

### Choice of Accuracy and Rates

Put A=2 lambda_max^2/(1-s) and q=log(A/epsilon)/(-log s). For the prescribed L_epsilon=max{2,ceil q}, we have L_epsilon>=q. Since s is in (0,1),

\[
A s^{L_\varepsilon}\leq A s^q=\varepsilon.
\]

The tail bound therefore gives the required completed-space Hausdorff error. The interpolation and induction above give exact rollout agreement through this same level and the stated finite-L width and depth upper bounds.

Writing gamma=log K/(-log s), the ceiling and maximum imply

\[
K^{L_\varepsilon}\leq\max\{K^2,K(A/\varepsilon)^\gamma\}=O(\varepsilon^{-\gamma}).
\]

As epsilon decreases to zero, L_epsilon log K=gamma log(1/epsilon)+O(1). Substitution into the displayed finite-L depth upper bound yields

\[
\widetilde O\!\left(\varepsilon^{-3\gamma/2}\left[1+\frac{\log_+(B_{L_\varepsilon})}{\log(1/\varepsilon)}\right]\right).
\]

If B_{L_epsilon} is polynomially bounded in 1/epsilon, its positive logarithm is O(log(1/epsilon)), giving the stated simplified rate. The constructed bounded-depth network also satisfies these weaker bounds directly. Constants are independent of epsilon, the field values, center separations, and weight magnitudes, and may depend only on the fixed parameters specified in the public task.

## Source Repairs and GT Completeness

The source's literal geometric path distance requires canonical zero-distance metric identification; this preserves all distance values and the proof above. The external interpolation formulas require a separate singleton case, and their raw width substitution must retain 12 rather than 2. These local repairs are recorded in provenance. The complete frozen target has been proved without reliance on the unavailable specialized external proof. There are no unresolved theorem-critical GT obligations.
