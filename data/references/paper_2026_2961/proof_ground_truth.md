# Reference Proof

## Proof Structure

1. Bound the marginal densities and compare the Lebesgue and density-weighted L2 norms.
2. Map the subset-indexed tensor Legendre orthonormal basis to Xi using a bounded triangular operator, treating its constant block separately. Prove that the diagonal blocks and hence the operator are invertible.
3. Establish orthogonality of each nonempty basis element against every L2 function of each strict subset, then pass to component limits.
4. Group the unique basis coefficients and identify the resulting zero-loss constrained decomposition using the assumed uniqueness statement.

## Complete Proof

Let H=L2(Q,lambda). For nonempty S, integration of c1<=f<=c2 over the omitted coordinates gives

c1 2^(p-|S|) <= f_S(x_S) <= c2 2^(p-|S|).

Also f_emptyset=1. Thus every f_S and 1/f_S is bounded. For measurable u,

c1 ||u||_H^2 <= ||u||_L2(mu_f)^2 <= c2 ||u||_H^2.

In particular H and L2(mu_f) have the same equivalence classes and equivalent norms.

The tensor products of normalized Legendre polynomials form an orthonormal basis of H. Index this basis by the supports of its multi-indices: psi_emptyset=2^(-p/2), while for nonempty S,

psi_S^(m_S)(x)=2^(-(p-|S|)/2) product_{j in S} tilde P_{m_j}(x_j),  m_j>=1.

Let V_S be the closed span of the functions with index S and Pi_S its H-orthogonal projection. Then H is the orthogonal direct sum of the finitely many V_S.

Set w_emptyset=2^(p/2), and set w_S=1/f_S for nonempty S. All these weights are positive and bounded above and below by common positive constants. Define T u=sum_S w_S Pi_S u. The triangle inequality and Cauchy-Schwarz over the 2^p subsets give ||T u||_H <= C ||u||_H, so T is bounded. In particular T psi_emptyset=1=xi_emptyset and T psi_S^(m_S)=xi_S^(m_S) for nonempty S.

Write A_{R,S}=Pi_R T|_{V_S}. A function in V_S depends only on x_S, and so does w_S times that function. Hence A_{R,S}=0 unless R is contained in S. For u,v in V_S, the diagonal-block form is

< A_{S,S}u,v >_H = integral_Q w_S(x_S)u(x)v(x) d lambda(x).

It is bounded and coercive, including at S=emptyset. Lax-Milgram on the Hilbert space V_S therefore makes A_{S,S} bijective with bounded inverse. Ordering the finite set of subsets by cardinality makes the block operator triangular; successive block substitution gives a bounded inverse for T. Thus T is a bounded bijection of H, and its inverse is bounded. Xi is the image of an orthonormal basis under T, hence is a Riesz basis of H and, by norm equivalence, of L2(mu_f). Every nu in L2(mu_f) consequently has a unique square-summable coefficient family and an unconditional L2 expansion in Xi.

Now fix nonempty S, T properly contained in S, m_S, and any h in L2(X_T). Since f_T is bounded below, h is also square-integrable with respect to Lebesgue measure on [-1,1]^|T|. Marginalizing outside S and cancelling f_S yields

E[xi_S^(m_S)(X) h(X_T)] = 2^(-(p-|S|)/2) integral_{[-1,1]^|S|} (product_{j in S} tilde P_{m_j}(x_j)) h(x_T) d x_S = 0.

The integrand is integrable; Fubini applies, and integration over any coordinate in the nonempty set S\T gives zero by positive-degree Legendre orthogonality to constants. This includes T=emptyset and h constant. For each S, form nu_S by summing the coefficients indexed by S. The Riesz-basis property gives convergence of each component series in L2 and convergence of their finite sum to nu. Each nu_S depends only on x_S because the corresponding subspace of functions of X_S is closed. Continuity of the inner product extends the displayed orthogonality to nu_S against every h in L2(X_T).

The components therefore satisfy the full hierarchical constraints and sum to nu, giving objective value zero. The assumed uniqueness of the constrained decomposition identifies them with its components. Uniqueness of the Riesz-basis coefficients gives the asserted unique coefficient family. All component equalities are L2 equalities, equivalently almost-sure equalities under the corresponding marginal law.
