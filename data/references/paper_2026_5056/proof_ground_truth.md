# Reference Proof

## Proof Structure

Count the monomials with individual exponents below k and with at most d exponents at least ell. Prove that their restrictions span all real-valued functions on H. The induction uses a fixed upper bound on dimension, so it applies to projections and subclasses even when their dimensions decrease. At each removal step, project the current class before deleting the selected point, construct a polynomial separating that point from the other current points, and then delete it. The resulting lower-triangular evaluation matrix proves both spanning and the cardinality bound. Finally, verify an extremal class and all admissible boundary cases.

## Complete Proof

Throughout, pseudo-cubes are nonempty, and neighbors must differ in the specified coordinate. Empty products are one, and zeroth powers, including 0^0, are one.

### step_001 — Allowed monomials and their count

For an integer m>=0 and a fixed integer D>=0, let M(m,D) be the monomials x^e with e in {0,...,k-1}^m and at most D coordinates j satisfying e_j>=ell. Call such coordinates high. To choose a monomial with exactly i high coordinates, choose those coordinates, choose one of k-ell exponents on each high coordinate, and choose one of ell exponents on each other coordinate. Therefore

|M(m,D)| = sum_{i=0}^{min(D,m)} binom(m,i)(k-ell)^i ell^(m-i).

For m=n and D=d this is exactly the claimed bound. This counting argument also covers ell=k: there are no high exponents, and only the i=0 term is nonzero.

### step_002 — Interpolation and the inductive removal construction

Fix k, ell, and D. We prove by induction on m that, for every A subseteq [k]^m with ell-DS dimension at most D, the restrictions of M(m,D) span R^A, the vector space of all real-valued functions on A. This assertion uses an upper bound on dimension, not a requirement that the dimension equal D.

If A is empty, R^A is the zero vector space and the assertion is immediate.

If m<=D, all monomials with coordinate exponents below k are allowed. For each a in A define

L_a(x) = product_{j=1}^m product_{t in [k], t!=a_j} (x_j-t)/(a_j-t).

The denominators are nonzero because the alphabet consists of distinct real numbers. Each L_a has degree at most k-1 in each coordinate and equals one at a and zero at every other point of [k]^m. Consequently, for every f:A->R, the polynomial sum_{a in A} f(a)L_a restricts to f on A. This also covers m=0, where the full grid consists of the single empty tuple and the interpolation product is one.

Now suppose m>D and assume the spanning assertion in smaller ambient dimensions. Start with the current class G=A. Every subclass of A has ell-DS dimension at most D: any pseudo-cube in a restriction of a subclass is also contained in the corresponding restriction of A.

At each step with G nonempty, G cannot be an (ell+1)-pseudo-cube on all m coordinates, since this would give dimension at least m>D. Thus there are h in G and a coordinate j such that h has fewer than ell neighbors in direction j within G.

Before deleting h, form the projection P=G|_{I_m\{j}}. In particular h_{-j} belongs to P. Every coordinate set shattered by P is also shattered by G, because their restrictions to those coordinates coincide. Hence P has ell-DS dimension at most D. Relabeling its m-1 coordinates if necessary, the induction hypothesis gives a polynomial q in the coordinates other than j whose monomials satisfy the restrictions defining M(m-1,D), and such that

q(h_{-j})=1, and q(u)=0 for every u in P distinct from h_{-j}.

Let T be the set of j-coordinate values of the neighbors of h within G, and set r=|T|. Neighbors agreeing off j have distinct j-coordinate values, so r<ell and h_j is not in T. Define

s(t) = product_{a in T} (t-a)/(h_j-a),

p_h(x) = q(x_{-j})s(x_j).

All denominators are nonzero. Also s(h_j)=1 and s(a)=0 for each a in T. Thus p_h(h)=1. If g in G differs from h off coordinate j, then q(g_{-j})=0. If g differs from h only at j, then g_j belongs to T and s(g_j)=0. Therefore p_h(g)=0 for every g in G other than h.

The polynomial s has degree r<ell<=k. Expanding q(x_{-j})s(x_j) preserves the individual exponent bounds below k and introduces no high exponent in coordinate j. Thus p_h is a linear combination of monomials in M(m,D).

Now delete h from G and repeat. Dimension cannot increase under deletion, so the same argument applies to every subsequent nonempty current class. The procedure terminates after |A| steps.

### step_003 — Triangularity, spanning, and the bound

Write the removal order as h_1,...,h_N, where N=|A|, and write p_1,...,p_N for the corresponding polynomials. The construction gives

p_a(h_a)=1, and p_a(h_b)=0 whenever a<b.

Thus the matrix with row a and column b equal to p_a(h_b) is lower triangular with diagonal entries one. To see independence directly, suppose sum_a c_a p_a vanishes on A. Evaluation at h_N gives c_N=0; evaluation at h_{N-1} then gives c_{N-1}=0; continuing backwards gives every coefficient zero.

The point indicators on A form a basis of R^A, so dim(R^A)=N. The N independent restrictions p_a therefore form a basis of R^A. Every p_a belongs to the span of the restricted monomials in M(m,D). Hence these monomials span R^A, completing the induction. In particular,

|A| = dim(R^A) <= |M(m,D)|.

Applying this with m=n, A=H, and D=d proves the desired inequality. The empty-class case was included in the induction.

### step_004 — Equality and exact dimension

First suppose ell<k. Define

H* = {x in [k]^n : at most d coordinates j satisfy x_j>=ell}.

Partitioning H* by the number i of coordinates at least ell gives

|H*| = sum_{i=0}^d binom(n,i)(k-ell)^i ell^(n-i).

For a coordinate set U of size d, the restriction H*|_U contains {0,...,ell}^U: extend any such pattern by zeros outside U. This product is nonempty, and each point has exactly ell neighbors in every coordinate direction within the product. It is therefore an (ell+1)-pseudo-cube, proving dimension at least d. When d=0, the same statement uses the singleton pattern on the empty coordinate set.

For the opposite inequality, suppose some S with |S|>d is shattered, and choose a nonempty (ell+1)-pseudo-cube B contained in H*|_S. Choose d+1 distinct coordinates of S and an initial point of B. Process the chosen coordinates one at a time. In the fiber of the current point in the next coordinate, the current point and its at least ell neighbors realize at least ell+1 distinct symbols. Since only ell symbols are below ell, at least one of these points has that coordinate at least ell. Move to such a point, or keep the current point if it already has the desired value. All previously processed coordinates are unchanged. After d+1 steps, a point of B has at least d+1 high coordinates. This is impossible because every restriction of a point of H* has at most d high coordinates. Thus no S of size greater than d is shattered, and the dimension of H* is exactly d. This argument includes d=n, for which there is no coordinate set of size greater than d.

If ell=k, a point has at most k-1 distinct neighbors in any coordinate direction, even in the full grid. Consequently no nonempty coordinate set can be shattered by any class, so the only admissible dimension is zero. Taking H*=[k]^n gives dimension zero and size k^n, equal to the right-hand side for d=0. This also covers k=1.

If n=0, the only possible dimension is zero, the full grid is the singleton empty tuple, and the sum is one. Taking that singleton gives equality.

## Source Audit and Obligation Closure

The monomial count follows L000087-L000096. The interpolation formula and removal construction follow L000098-L000110, with the dimension-at-most-D induction and projection-before-deletion made explicit. L000112 prints the zero condition with i>j, but L000107 and L000110 establish zeros for later-removed points, so the correct condition is i<j. This local source correction changes neither triangular invertibility nor the conclusion at L000113. The extremal family is given at L000034-L000039 and its sharpness is asserted at L000058; step_004 supplies the elementary exact-dimension and boundary-case verification.

All theorem-critical obligations are closed: monomial counting; interpolation; inheritance of the dimension upper bound by subclasses and projections; existence of a deficient coordinate at every removal step; nonzero interpolation denominators; preservation of allowed exponents; finite termination; triangular independence and spanning; and equality with exact dimension for every admissible parameter choice. No specialized external result or unresolved proof dependency is used.
