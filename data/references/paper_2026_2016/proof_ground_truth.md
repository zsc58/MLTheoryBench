# Reference Proof

## Proof Structure

1. Normalize the intensity and apply the atomless standard Borel probability-space isomorphism theorem to construct a bilinear digraphon with the same conditional and Poissonized graph laws.
2. Establish the sectional-BV obstruction by extracting bases from regular sections and inverting the resulting linear systems. For an almost-everywhere pullback identity, use Fubini first and obtain BV representatives of the latent coordinates.
3. Prove that a finite-variation map into dimension at least two has an image contained in a Borel Lebesgue-null set, contradicting the absolutely continuous latent law.
4. Establish almost twin-freeness and apply the stipulated directed lifting property to every weakly equivalent kernel.

## Complete Proof

### 1. Representation and graph laws

Let lambda denote Lebesgue probability measure on [0,1]. The measure mu(dx)=rho(x)dx/Lambda is a probability measure and is atomless because it has a Lebesgue density. The set Omega is an uncountable closed subset of R^{2d}, hence a standard Borel space.

The standard independent measure-space theorem used here is: two uncountable standard Borel spaces equipped with atomless Borel probability measures admit a measure-preserving Borel bijection with Borel inverse. Both ([0,1],lambda) and (Omega,mu) satisfy these hypotheses. Choose such a bijection phi and define

W(u,v)=g(phi(u)) dot r(phi(v)).

The coordinate maps are Borel, so W is Borel measurable. Its values lie in [0,1] by nonnegativity of the coordinates and the Euclidean norm bound.

For each n>=0, sample iid uniform labels T_1,...,T_n and set X_i=phi(T_i). The points X_i are iid with law mu. Conditional on these points, the latent and digraphon experiments use exactly the same independent Bernoulli probabilities for every ordered pair (i,j), including i=j. Coupling the Bernoulli trials proves equality of the complete labeled graph laws conditional on n, including isolated vertices. The n=0 case is the empty graph. Mixing these identical conditional laws with the same Poisson(Lambda) probabilities proves equality of the Poissonized laws.

### 2. Basis extraction

The green and red coordinate marginals of mu are absolutely continuous on R^d: extend rho by zero outside Omega and integrate rho/Lambda over the other coordinate block. This follows from Tonelli's theorem and does not require factorization of rho.

We use the following elementary fact. If xi:[0,1]->R^d has an absolutely continuous pushforward law and S has positive measure, then S contains d labels with linearly independent xi-images. Indeed, the inverse image of any proper linear subspace has measure zero. First choose a nonzero image in S. After choosing k<d independent images, remove the inverse image of their proper linear span from S and choose the next label in the remaining nonempty set. This completes the induction. For full-measure S, the stated essential-span assumption also suffices for the same induction.

### 3. The obstruction, including almost-everywhere representatives

Let theta:[0,1]->Omega be any measurable map with theta_*lambda=mu. Write a=g composed with theta and b=r composed with theta. We prove the following private strengthening needed for the lifting step: no sectionally BV kernel V can satisfy

V(u,v)=a(u) dot b(v)

for product-almost every (u,v). The exact-pullback obstruction follows as a special case.

Suppose such V exists. By Fubini, for almost every v the displayed equality holds for almost every u. Intersect this full-measure set with the full-measure set of v for which u->V(u,v) has finite scalar total variation. Call the intersection S_R.

The pushforward law of b is the red marginal of mu. By the basis-extraction argument choose v_1,...,v_d in S_R such that b(v_1),...,b(v_d) form a basis. Let M_R be the invertible matrix whose j-th row is b(v_j)^T, and define, for every u,

A(u)=M_R^{-1}(V(u,v_1),...,V(u,v_d))^T.

Each coordinate of A is a finite linear combination of scalar BV functions, so it is BV. For each selected v_j the defining section agrees almost everywhere with a(u) dot b(v_j). Intersecting these finitely many full-measure sets shows A(u)=a(u) almost everywhere.

Apply the same argument in the other direction. Intersect the full-measure set of u with BV sections v->V(u,v) with the Fubini full-measure set on which the pullback equality holds for almost every v. Extract labels u_1,...,u_d whose vectors a(u_j) form a basis. Inverting the matrix with rows a(u_j)^T gives a vector map B whose coordinates are BV and for which B(v)=b(v) almost everywhere.

Set F(t)=(A(t),B(t)) in R^{2d}. Its vector total variation is finite, since the Euclidean norm of an increment is at most the sum of the absolute coordinate increments. Moreover F=theta almost everywhere, as R^{2d}-valued maps. Consequently F_*lambda=mu, viewing mu as a measure on R^{2d}. Values of F outside Omega on an exceptional null set cause no problem.

We now justify the image-null obstruction directly. Let F:[0,1]->R^m have finite vector total variation L, where m>=2, and put s(t)=Var(F;[0,t]). Additivity of variation implies that for t<t',

||F(t')-F(t)||_2 <= s(t')-s(t).

For epsilon>0, partition [0,L] into at most floor(L/epsilon)+1 half-open intervals of length epsilon, with the final endpoint included. Labels whose s-values lie in one interval have F-images of diameter at most epsilon. Selecting one image point from each nonempty group therefore covers F([0,1]) by at most floor(L/epsilon)+1 closed balls of radius epsilon. Their total m-dimensional volume is at most

c_m (floor(L/epsilon)+1) epsilon^m,

which tends to zero as epsilon decreases to zero, including when L=0. Choosing such finite covers along a sequence epsilon_k decreasing to zero, their intersection is a Borel set H containing F([0,1]) and having m-dimensional Lebesgue measure zero.

For m=2d>=2, absolute continuity gives mu(H)=0. On the other hand, F_*lambda=mu gives mu(H)=lambda(F^{-1}(H))=1, a contradiction.

Thus no sectionally BV kernel can agree product-almost everywhere with this latent pullback. In particular, no exact pullback through a measure-preserving theta is sectionally BV.

### 4. Almost twin-freeness

Suppose u and u' are twins for W. Equality of their rows gives

(g(phi(u))-g(phi(u'))) dot r(phi(t))=0

for almost every t. Because the red marginal has full essential linear span, the green-vector difference must be zero. Equality of their columns and the green marginal span similarly give r(phi(u))=r(phi(u')). Thus phi(u)=phi(u'). Injectivity of phi forces u=u'. In particular W is almost twin-free. A construction using an isomorphism only on conull sets would give the same conclusion outside its exceptional null set.

### 5. Every weakly equivalent kernel

Let U be any digraphon weakly equivalent to W. Apply the directed lifting property expressly assumed in the problem, with the almost twin-free target W. There is a measurable measure-preserving map psi:[0,1]->[0,1] such that

U(u,v)=W(psi(u),psi(v))

for product-almost every (u,v). Put theta=phi composed with psi. For every Borel set E in Omega,

lambda(theta^{-1}(E))=lambda(phi^{-1}(E))=mu(E),

so theta pushes lambda forward to mu. Also

U(u,v)=g(theta(u)) dot r(theta(v))

product-almost everywhere. Section 3 applies directly to this almost-everywhere identity and proves that U cannot be sectionally BV.

This completes the integrated theorem. No claim that pointwise sectional BV is invariant under null modification is used. Nor is almost-everywhere kernel equality used to infer equality of self-loop laws; the graph-law comparison in Section 1 uses the exact constructed kernel.

## Dependency and Repair Audit

- The atomless Borel probability-space isomorphism theorem is standard independent background, with its statement and hypotheses given in Section 1.
- Basis extraction is derived in Section 2, recovering the existing source support theory_028.
- The BV image-null statement is derived by finite covers in Section 3; no specialized geometric-measure-theory theorem is left unexpanded.
- The directed lifting assertion is a primitive hypothesis, not a theorem claimed to follow from an unaudited citation.
- The local source repair to theory_010 is the Fubini-and-BV-representatives argument in Section 3. It preserves the pointwise sectional-BV definition and the source's proof route.
- All theorem-critical obligations are closed; there is no unresolved private GT gap.
