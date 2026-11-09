# Reference Proof

## Scope and Obligations

The result concerns the supports of individual averaged Taylor coefficients and their exposed faces. It does not require convergence of an infinite Taylor series, an exchange of large-system limits with time evolution, or a claim that a signed polynomial always has numerical magnitude comparable to the power of its largest monomial weight.

The proof closes six obligations: (1) the correctly normalized expansion and sign structure; (2) Gaussian evaluation and surviving-index counts; (3) realizability of every claimed frontier point; (4) a global bound together with domination of every unlisted point; (5) the population normalization and low-order cases; and (6) geometry and complete regime classification. The only external result used is the centered Gaussian pairing formula, stated below. The needed merging and pairing constructions are derived explicitly.

## Step 1: Normalized Expansion and Sign Structure

Let
\[
A=U^TU,\qquad B=XX^T,
\]
and define
\[
D=\operatorname{Tr}(A^2),\quad R=\operatorname{Tr}(A),\quad
\widehat D=\operatorname{Tr}(A^2B),\quad
\widehat R=\operatorname{Tr}(AB),\quad
\widehat F=\operatorname{Tr}(B).
\]
Then
\[
L=\frac{D/2-R}{p}+\frac12,\qquad
\widehat L=\frac{\widehat D/2-\widehat R}{pm}+\frac{\widehat F}{2pm}.
\]
The second constant is random before averaging, but \(\mathbb E\widehat F=pm\). Both constant terms have zero weight gradient.

For scalar functions of \(U\), write
\[
G\star H=\langle\nabla_U G,\nabla_U H\rangle_F.
\]
Put \(G_0=D/2-R\), \(\widehat G_0=\widehat D/2-\widehat R\), and recursively define
\[
G_s=G_{s-1}\star\widehat G_0,\qquad
\widehat G_s=\widehat G_{s-1}\star\widehat G_0.
\]
These are sequential products, not associative powers. The chain rule along the prescribed empirical gradient flow gives
\[
\frac{d^sL}{dt^s}=\frac{(-\eta)^s}{p^{s+1}m^s}G_s\quad(s\ge1),\qquad
\frac{d^s\widehat L}{dt^s}=\frac{(-\eta)^s}{p^{s+1}m^{s+1}}\widehat G_s\quad(s\ge1).
\]
The right gradient in the chain rule is always that of the training loss, including when the observed loss is the population loss. Consequently, with expectation evaluated at initialization,
\[
Y_s=\frac1p\mathbb E G_s,\qquad
\widehat Y_s=\frac1{pm}\mathbb E\widehat G_s\qquad(s\ge0).
\]
For \(s=0\), these formulas describe the model-dependent coefficient after separating the averaged constant \(1/2\).

A trace word has an index-sum representation as a ring. Its vertices are summation indices of types \(p,n,m\); its edges are matrix entries of \(U\) or \(X\). Differentiating with respect to an entry of \(U\) deletes its edge while retaining the endpoint indices. Summing the product of two such derivatives identifies the corresponding \(p\)-endpoints and \(n\)-endpoints. Thus a term in \(G\star H\) is obtained by cutting one \(U\)-edge from each ring and joining the resulting paths. It is again a connected ring. Each such merger removes two \(U\)-edges and reduces both the total \(p\)-vertex count and total \(n\)-vertex count by one; it does not reduce the total \(m\)-vertex count.

Expand a sequential product into choices of \(D\)-type and \(R\)-type factors. Let \(d=s_D\) count the former among the \(s+1\) factors. There are \(s+1-d\) latter factors. Set
\[
N=d+1.
\]
Every resulting ring has \(N\) vertices of type \(n\), \(2N\) edges of type \(U\), and the following remaining counts:
\[
\begin{array}{c|c|c|c}
& m\text{-vertices}&p\text{-vertices}&X\text{-edges}\\ \hline
\text{training}&M=s+1&N+M&2M\\
\text{population}&M=s&N+M&2M.
\end{array}
\]
The population formula includes \(M=0\) at \(s=0\).

For fixed \(d\), all expansion terms have sign \((-1)^{s+1-d}\), multiplied by the positive factor \(2^{-d}\) and positive differentiation multiplicities. Their common \(U\)-degree is \(2(d+1)\). This degree will make the sign consistent for every fixed resulting variance exponent.

## Step 2: Gaussian Evaluation and Polynomial Supports

For centered jointly Gaussian variables, an odd product has expectation zero, and an even product has expectation equal to the sum, over all pair partitions, of products of covariances. In the present independent arrays,
\[
\mathbb E[U_{ai}U_{bj}]=\sigma^2\delta_{ab}\delta_{ij},\qquad
\mathbb E[X_{i\ell}X_{jk}]=\delta_{ij}\delta_{\ell k},\qquad
\mathbb E[U_{ai}X_{j\ell}]=0.
\]
All hypotheses are satisfied by the initialization and sampling model. Every coefficient is a finite sum of expectations of polynomials, so the Gaussian moments involved are finite.

A nonzero pairing therefore pairs only edges of the same matrix type and identifies their corresponding endpoint indices. If the resulting numbers of index classes are \(V_p,V_n,V_m\), its contribution before loss normalization is
\[
p^{V_p}n^{V_n}m^{V_m}\sigma^{2N}.
\]
The normalized exponents are
\[
(q_p,q_n,q_m,q_\sigma)=
\begin{cases}
(V_p-1,V_n,V_m-1,2N),&\text{training},\\
(V_p-1,V_n,V_m,2N),&\text{population}.
\end{cases}
\]
There is always a \(p\)-vertex. A training ring also always has an \(m\)-vertex. Thus division by \(p\), or by \(pm\), leaves polynomial exponents. When the population ring has \(M=0\), its sample exponent is zero.

Each Wick contribution has nonnegative coefficient before the sign from Step 1. Since \(q_\sigma=2(d+1)\) determines \(d\), contributions to the same monomial all have the same sign. They cannot cancel when like monomials are collected. It consequently suffices for realizability to exhibit one valid sequential merger and one valid pairing.

## Step 3: Realizability, Including the Merger Construction

First verify that a ring with contiguous \(U\)- and \(X\)-arcs is available for every required \(d\). For integers \(N\ge1\), \(M\ge0\), let
\[
F_{N,M}=\operatorname{Tr}(A^N B^M),\qquad B^0=I_p.
\]
Direct differentiation gives
\[
\nabla_U F_{N,M}=2U\sum_{j=0}^{N-1}A^jB^MA^{N-1-j}.
\]
The sum is symmetric, as can be seen by transposing and replacing \(j\) by \(N-1-j\). For \(e\in\{1,2\}\), the scalar product with \(\nabla_U F_{e,1}\) is a positive sum of trace words. Choosing \(j=0\) in the first sum and the index \(e-1\) in the second gives the term
\[
4\operatorname{Tr}(B^M A^{N+e-1}B)
=4F_{N+e-1,M+1}.
\]
Thus appending a training \(R\)-factor or \(D\)-factor can preserve the form \(F_{N,M}\), increasing \(N\) by zero or one and increasing \(M\) by one. Starting with the appropriate first factor, induction produces
\[
F_{d+1,s+1}\quad\text{for training},\qquad
F_{d+1,s}\quad\text{for population}.
\]
This also works when the first population factor has no \(X\)-edges. The matrix differentiation verifies the required merger using the same ring operation as Step 1, without assuming its existence.

Now suppose \(M\ge1\). In the ring of \(F_{N,M}\), the \(N\) vertices of type \(n\) occur along one arc and the \(M\) vertices of type \(m\) along the other. Fix any
\[
1\le r\le N,\qquad 1\le k\le M.
\]
Along the \(n\)-arc, choose \(N-r\) successive internal \(p\)-vertices between neighboring \(n\)-vertices. At each chosen \(p\)-vertex, pair its two incident \(U\)-edges. The covariance identifies the two neighboring \(n\)-indices, while the shared \(p\)-index remains an independent index. The chosen pairs are disjoint. They leave \(r\) distinct \(n\)-classes and \(N-r\) separate \(p\)-leaves attached to those classes.

Perform the same operation at \(M-k\) successive internal \(p\)-vertices of the \(m\)-arc, using \(X\)-edge pairs. It leaves \(k\) distinct \(m\)-classes and \(M-k\) additional \(p\)-leaves. Ignore these already paired leaf edges temporarily. In the remaining ring, pair the two remaining incident edges at each \(n\)- or \(m\)-vertex. Each pair has a common \(n\)- or \(m\)-endpoint and identifies its two \(p\)-endpoints. Going around this ring identifies all remaining \(p\)-vertices into one class, without merging the \(r\) distinct \(n\)-classes, the \(k\) distinct \(m\)-classes, or any of the previously preserved \(p\)-leaves.

This is a pairing of every original edge exactly once. It gives
\[
V_n=r,\qquad V_m=k,\qquad
V_p=(N-r)+(M-k)+1.
\]
For training, take \(N=d+1\), \(M=s+1\), \(r=q_n\), and \(k=q_m+1\). After division by \(pm\), the resulting exponent is
\[
\bigl(s+d-q_n-q_m+1,\ q_n,\ q_m,\ 2(d+1)\bigr)
\]
for every \(1\le q_n\le d+1\) and \(0\le q_m\le s\).

For population orders \(s\ge1\), take \(N=d+1\), \(M=s\), \(r=q_n\), and \(k=q_m\). Division is only by \(p\), giving exactly the same exponent formula, now for \(1\le q_m\le s\). Sign consistency from Step 1 ensures that every constructed monomial is present in the collected polynomial.

## Step 4: Optimality and the Converse Domination Argument

Consider any Wick pairing of any connected ring having \(2(N+M)\) edges. Identify endpoints according to the pairing and retain one edge for each pair. The resulting multigraph is connected and has \(N+M\) edges. Every connected finite multigraph with \(E\) edges has at most \(E+1\) vertices: a spanning tree uses one edge for every vertex after the first. Therefore
\[
V_p+V_n+V_m\le N+M+1.
\]
Contractions cannot increase the number of vertices of any type. In a training ring,
\[
1\le V_n\le d+1,\qquad 1\le V_m\le s+1.
\]
Substituting \(V_p=q_p+1\), \(V_n=q_n\), and \(V_m=q_m+1\) into the graph bound yields
\[
q_p\le s+d-q_n-q_m+1,
\quad 1\le q_n\le d+1,
\quad 0\le q_m\le s.
\]
For each permitted pair \((q_n,q_m)\), Step 3 realizes equality. Consequently, every exponent with strict inequality is dominated by the realized exponent with the same \(q_\sigma,q_n,q_m\) and maximal \(q_p\). This is the required converse: it excludes all additional Pareto points.

Conversely, two distinct realized equality points with the same \(d\) have the same sum
\[
q_p+q_n+q_m=s+d+1.
\]
Neither can dominate the other. Points with different \(d\) have different \(q_\sigma\) and cannot dominate one another under the specified order. Hence the training Pareto set is exactly the displayed set in the task.

For population orders \(s\ge1\), use \(M=s\) and \(V_m=q_m\), with \(1\le q_m\le s\). The same bound gives
\[
q_p\le s+d-q_n-q_m+1.
\]
The population construction realizes equality for every allowed \(q_n,q_m\). The same domination and constant-sum arguments prove the claimed population Pareto formula.

## Step 5: Population Normalization and Low Orders

The change in the sample exponent is not justified merely by saying that the first factor loses its data edges: one must also use the different normalization. Training rings have \(s+1\) sample vertices before pairing and are divided by \(pm\); population rings have \(s\) sample vertices and are divided only by \(p\). For \(s\ge1\), at least one population sample-index class survives, so \(q_m=0\) is impossible. The construction and bound above show that this excludes precisely that training boundary and nothing else.

For \(s=0\), independence gives
\[
\mathbb E_X[\widehat D\mid U]=mD,\qquad
\mathbb E_X[\widehat R\mid U]=mR.
\]
Therefore \(Y_0=\widehat Y_0\). More explicitly, \(\mathbb E R=pn\sigma^2\). In the four-entry expansion of \(D\), the three Gaussian pairings contribute \(pn^2\sigma^4\), \(pn\sigma^4\), and \(p^2n\sigma^4\), respectively. Hence
\[
Y_0=\widehat Y_0=-n\sigma^2+\frac12n(p+n+1)\sigma^4.
\]
Its Pareto indices are
\[
(0,1,0,2),\qquad (1,1,0,4),\qquad (0,2,0,4),
\]
which agree with the asserted formula at \(s=0\). The remaining variance-four monomial, with index \((0,1,0,4)\), is dominated.

## Step 6: Geometry and Exhaustive Formal Regimes

Use coordinates \((d,r,z)=(s_D,q_n,q_m)\). The exponent map is the injective affine map
\[
(d,r,z)\longmapsto (s+d-r-z+1,r,z,2(d+1)).
\]
The convex hull in these coordinates is the Cartesian product of the triangle
\[
T_s=\{(d,r):0\le d\le s+1,\ 1\le r\le d+1\}
\]
with \([0,s]\) for training, and with \([1,s]\) for population when \(s\ge1\). Each product's vertices are among the stated integer indices, so its convex hull is exactly this product, not merely contained in it. For population order zero use the equality with the training set.

The triangle is nondegenerate for every \(s\ge0\). The training interval has positive length exactly when \(s\ge1\), and the population interval exactly when \(s\ge2\). This proves the prism and triangle assertions. Fixed-\(d\) sections are generally rectangles or degenerate rectangles; it is the full \((d,r)\)-domain that forms the triangular base.

For any admissible scaling vector, domination by a distinct exponent with the same variance coordinate strictly increases its weight, because all three dimension exponents are positive. Thus leading indices lie in the Pareto set, and maximization can be performed on its convex hull.

On the affine exponent parameterization, the weight is
\[
q^T\alpha=(s+1)\alpha_p+2\alpha_\sigma
+d(\alpha_p+2\alpha_\sigma)
+r(\alpha_n-\alpha_p)
+z(\alpha_m-\alpha_p).
\]
Put
\[
\beta_D=\alpha_p+2\alpha_\sigma,\qquad
\beta_n=\alpha_n-\alpha_p,\qquad
\beta_m=\alpha_m-\alpha_p.
\]
In a nondegenerate prism, its five facets and the conditions for exactly that facet to maximize the weight are:

| Facet | Conditions | Regime |
|---|---|---|
| \(z=s\) | \(\beta_D=\beta_n=0,\ \beta_m>0\) | Large-data |
| \(z=0\) for training, \(z=1\) for population | \(\beta_D=\beta_n=0,\ \beta_m<0\) | Small-data |
| \(r=d+1\) | \(\beta_D+\beta_n=0,\ \beta_n>0,\ \beta_m=0\) | Mean-field |
| \(r=1\) | \(\beta_D=0,\ \beta_n<0,\ \beta_m=0\) | Narrow-latent |
| \(d=s+1\) | \(\beta_D>0,\ \beta_n=\beta_m=0\) | Free |

For example, constancy along \(r=d+1\) requires \(\beta_D+\beta_n=0\); \(\beta_n>0\) then strictly favors that side over the interior, and \(\beta_m=0\) retains the entire height interval. The other four conditions follow by the same direct maximization on the triangle and interval. Substitution gives precisely the five scaling conditions in the public task.

No possible exposing direction is lost because of positivity of \(\alpha_p,\alpha_n,\alpha_m\). Given any real triple \((\beta_D,\beta_n,\beta_m)\), choose \(c>\max\{0,-\beta_n,-\beta_m\}\) and set
\[
\alpha_p=c,\quad \alpha_n=c+\beta_n,\quad
\alpha_m=c+\beta_m,\quad
\alpha_\sigma=(\beta_D-c)/2.
\]
This is admissible and induces the prescribed functional. All faces are therefore attainable. The prism has exactly the two end facets and three side facets listed above. A linear functional selects either the full prism, a facet, an edge, or a vertex. Every edge or vertex is a nonempty intersection of facets; a positive sum of the corresponding exposing functionals exposes that intersection. Hence lower-dimensional extremes are exactly combinations in the geometric sense stated in the task, not simultaneous satisfaction of incompatible facet-only scaling equalities.

The nondegenerate products at different orders have the same maximizing-face structure: the triangular inequalities have the same orientations, and changing the positive interval length or its lower endpoint does not change its maximizing endpoint or full-interval choices. The low-order triangles merely collapse the height direction. Thus the joint sequence of coefficient leading sets has exactly the claimed five basic extreme regimes and their lower-dimensional combinations. This is a classification of formal coefficients, with no additional assertion about convergence of loss trajectories.

## Source-Repair Notes

The proof uses the derivative normalization fixed by the formal series and the source's full derivative formulas, not the inconsistent shorthand at L000055. Expectations and evaluation at initialization are restored in the coefficient identities at L000435/L000438; the separated training target is averaged as at L000432. The trace expansion at L000362 uses the closing factors \(X_{i''\ell}X_{i\ell}\). The low-order geometry is qualified according to the theorem's own integer ranges. The realizability and optimality arguments are completed locally without any unproved specialized dependency.
