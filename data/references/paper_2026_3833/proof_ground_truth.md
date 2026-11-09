# Reference Proof

## Conventions and obligations

All homology is over \(\mathbb F\). Relative homology is computed from ordinary relative simplicial chains. For a nonempty auxiliary complex, write \(\overline H_0=\widetilde H_0\) and \(\overline H_i=H_i\) for \(i>0\). The relative complexes appearing here have the same vertex set in both entries, so their degree-zero relative chain groups are zero. Their degree-minus-one homology is zero.

The proof must establish: (1) the three matrix-defined auxiliary complexes have the appropriate relative homology; (2) the relative triple gives the claimed pointwise kernel identity; and (3) all integrals are finite, agree with finite barcode lengths, and combine with the stated two-orientation normalization. These obligations are proved below, rather than inferred from a citation to a mapping-cone construction.

If \(n=0\), every auxiliary complex consists of its single additional vertex, and all the relative groups in the statement are zero. Both sides vanish. Hence assume \(n\geq1\).

## 1. Auxiliary complexes and relative homology

We first establish a general comparison directly from the matrix entries. Let \(A,B\) be symmetric nonnegative matrices with zero diagonal and \(B\leq A\) entrywise. At a fixed scale \(\alpha\), set
\[
 L=R_\alpha(A),\qquad J=R_\alpha(B),\qquad S=R_\alpha(T(A,B)).
\]
Label the first-copy vertices \(t_1,\ldots,t_n\), the second-copy vertices \(s_1,\ldots,s_n\), and the additional vertex \(o\). Let \(C\) be the subcomplex induced on the two copies, with \(o\) omitted, and let \(L^t\) be the first-copy copy of \(L\).

The matrix entries give the following exact description. First-copy edges are governed by \(A\), second-copy edges by \(B\), and a mixed edge \(t_r s_s\) is present precisely when \(r\leq s\) and \(A_{rs}\leq\alpha\). In particular, every paired edge \(t_r s_r\) is present. The vertex \(o\) is adjacent to every first-copy vertex and to no second-copy vertex. Consequently,
\[
 S=C\cup(o*L^t),\qquad C\cap(o*L^t)=L^t.
\]

Define \(p:C\to J\) by \(p(t_r)=p(s_r)=r\). This is simplicial: every edge of a projected simplex satisfies the \(B\)-threshold, since \(B\leq A\). We now prove that \(p\) is a homotopy equivalence, rather than merely asserting that \(C\) is a mapping cylinder.

For \(m=n,n-1,\ldots,1\), let \(C_m\) be the subcomplex induced on \(t_1,\ldots,t_m,s_1,\ldots,s_n\). Define \(r_m:C_m\to C_{m-1}\) by sending \(t_m\) to \(s_m\) and fixing all other vertices. For any simplex \(\sigma\) containing \(t_m\), the set \(\sigma\cup\{s_m\}\) is also a simplex:

- If \(t_r\in\sigma\), then \(r\leq m\) and \(A_{rm}\leq\alpha\), so the mixed edge \(t_rs_m\) exists.
- If \(s_s\in\sigma\), then the edge \(t_ms_s\) implies \(m\leq s\) and \(A_{ms}\leq\alpha\). Hence \(B_{ms}\leq\alpha\), giving the edge \(s_ms_s\).
- The paired edge \(t_ms_m\) has weight zero.

All other required edges already belong to \(\sigma\). Since \(S\) is a flag complex, these edge checks prove the assertion. Therefore \(r_m\) is simplicial, is a retraction, and its composite with inclusion is contiguous to the identity. Contiguous simplicial maps induce chain-homotopic maps over every field: the signed prism operator
\[
 P[z_0,\ldots,z_q]=\sum_{j=0}^q(-1)^j
 [f(z_0),\ldots,f(z_j),g(z_j),\ldots,g(z_q)]
\]
with degenerate simplices set to zero satisfies \(\partial P+P\partial=g_\#-f_\#\). Here all its simplices exist by the union-of-images condition just verified. Thus each \(r_m\) is a homotopy equivalence. Their composition is \(p\), with the bottom copy identified with \(J\), so \(p:C\to J\) is a homotopy equivalence.

The restriction \(p|_{L^t}:L^t\to L\) is a simplicial isomorphism. The long exact sequences of the pairs \((C,L^t)\) and \((J,L)\), and their naturality under \(p\), therefore give
\[
 H_i(C,L^t)\cong H_i(J,L).
\]
The standard comparison fact used here is that a map of pairs inducing homology isomorphisms on both the ambient spaces and the subspaces induces an isomorphism on relative homology; it follows from exactness of the two pair sequences. Both hypotheses were established explicitly.

The subcomplex \(D=o*L^t\) is a nonempty contractible cone. The pair sequence for \((S,D)\) gives
\[
 \overline H_i(S)\cong H_i(S,D),\qquad i\geq0.
\]
Moreover, the simplices outside \(D\) are exactly the simplices of \(C\) outside \(L^t\), with the same quotient boundary operators. Hence the relative chain complexes are isomorphic:
\[
 C_*(S,D)\cong C_*(C,L^t).
\]
Combining these statements proves the required comparison
\[
 \overline H_i(R_\alpha(T(A,B)))\cong H_i(R_\alpha(B),R_\alpha(A)),\qquad i\geq0.
\]
This supplies the relative-homology content of the intended mapping-cone model, including the reduced degree-zero convention. For completeness, the algebraic mapping cone of an inclusion \(C_*(L)\hookrightarrow C_*(J)\) maps onto \(C_*(J,L)\) by \((x,y)\mapsto[x]\), where its differential is \((x,y)\mapsto(\partial x+y,-\partial y)\). Its kernel is the cone of the identity on \(C_*(L)\), contracted by \((x,y)\mapsto(0,x)\). Thus this algebraic cone has exactly the relative homology used above; no specialized external construction remains unproved.

Apply the comparison with the three choices
\[
 (A,B)=(A_\vee,a),\qquad (A_\vee,A_\wedge),\qquad (a,A_\wedge).
\]
All satisfy \(B\leq A\). With \(X=X^a_\alpha\), \(I=I_\alpha\), and \(U=U_\alpha\), it follows that
\[
 \overline\beta_i(R_\alpha(M_{\max}(a,b)))=\dim H_i(X,I),
\]
\[
 \overline\beta_i(R_\alpha(M_{\mathrm{sym}}))=\dim H_i(U,I),
\]
\[
 \overline\beta_i(R_\alpha(M_{\min}(a,b)))=\dim H_i(U,X).
\]
Here \(U=R_\alpha(A_\wedge)\); it is not replaced by an ordinary union of simplicial complexes.

## 2. Exactness and the pointwise identity

The inclusions \(I\subseteq X\subseteq U\) give the short exact sequence of relative chain complexes
\[
 0\longrightarrow C_*(X,I)\longrightarrow C_*(U,I)
 \longrightarrow C_*(U,X)\longrightarrow0.
\]
Write
\[
 P_i=H_i(X,I),\qquad Q_i=H_i(U,I),\qquad R_i=H_i(U,X).
\]
The associated long exact sequence contains
\[
 \cdots\to R_{i+1}\xrightarrow{\partial_{i+1}}P_i
 \xrightarrow{\gamma_i^a}Q_i\xrightarrow{q_i}R_i
 \xrightarrow{\partial_i}P_{i-1}\xrightarrow{\gamma_{i-1}^a}Q_{i-1}\to\cdots.
\]
All spaces are finite-dimensional. Put \(p_i=\dim\operatorname{im}\gamma_i^a\) and \(r_i=\dim\operatorname{im}q_i\). Exactness and rank-nullity yield
\[
 \dim P_i=\dim\ker\gamma_i^a+p_i,\qquad
 \dim Q_i=p_i+r_i,
\]
and
\[
 \dim R_i=r_i+\dim\ker\gamma_{i-1}^a.
\]
Subtracting gives
\[
 \dim P_i+\dim R_i-\dim Q_i
 =\dim\ker\gamma_i^a+\dim\ker\gamma_{i-1}^a.
\]
The degree-zero case uses the zero groups in degree minus one. In fact, all three pairs have identical vertex sets in their two entries, so their relative degree-zero chain groups, and hence their \(H_0\), vanish. This agrees with the fact that every auxiliary complex is connected through the zero-weight paths \(o,t_r,s_r\).

Using the comparisons from Section 1 proves, for every \(\alpha\geq0\),
\[
 \overline\beta_i(R_\alpha(M_{\max}(a,b)))+
 \overline\beta_i(R_\alpha(M_{\min}(a,b)))-
 \overline\beta_i(R_\alpha(M_{\mathrm{sym}}))
 =\dim\ker\gamma_i^a(\alpha)+\dim\ker\gamma_{i-1}^a(\alpha).
\]

## 3. Finite persistence and averaging

Let
\[
 D=\max\bigl(\{0\}\cup\{w_{rs},\widetilde w_{rs}:r,s\in V\}\bigr).
\]
This is finite. For \(\alpha\geq D\), each of \(I_\alpha\), \(X^a_\alpha\), and \(U_\alpha\) is the full simplex on \(V\). All three relative complexes are therefore zero. Section 1 shows that every auxiliary complex has zero reduced homology in every degree at these scales. This establishes the necessary eventual acyclicity; connectedness alone would not suffice in positive degrees.

There are only finitely many finite matrix-entry values. Consequently, the Betti functions and kernel-dimension functions are finite-dimensional step functions supported in \([0,D]\). Their integrals are finite, including when \(D=0\). The finite filtrations admit barcode decompositions, and there are no essential positive-dimensional intervals. The single essential degree-zero interval is removed by reduced homology. Thus, almost everywhere,
\[
 \overline\beta_i(K_\alpha)=\sum_{J\text{ a finite degree-}i\text{ interval}}\mathbf1_J(\alpha),
\]
and integration gives the sum of the finite interval lengths. Endpoint conventions and tied filtration values do not affect these integrals.

Integrate the pointwise identity for each of the two indexed orientations and average. The symmetric term appears twice and therefore retains coefficient one; the max and min terms acquire precisely their defining factor \(1/2\). Hence
\[
\mathcal D_{\max,i}+\mathcal D_{\min,i}-\mathcal D_{\mathrm{sym},i}
=
\frac12\sum_{(a,b)}\int_0^\infty
\left(\dim\ker\gamma_i^a(\alpha)+\dim\ker\gamma_{i-1}^a(\alpha)\right)d\alpha.
\]
The argument also covers coincident matrices and zero off-diagonal entries without additional assumptions. All proof obligations are closed.
