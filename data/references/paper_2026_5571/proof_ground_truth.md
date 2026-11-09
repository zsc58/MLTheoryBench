# Reference Proof

## Proof Obligations

1. Verify that the lifted quadratic and linear moments exist, establish their equivariance, and obtain a smooth parameter risk.
2. Prove invariance of the lifted loss under the stabilizer, including its linear term.
3. Transfer this invariance to the parameter block and justify the differential conclusions at arbitrary rank. Do not infer smooth quotient regularity merely from separation of orthogonal orbits by Gram matrices.
4. Justify preservation of rank and the regularity required by the linear matrix equation, prove fundamental-matrix invertibility, and conclude conservation on the solution's interval of existence.
5. Apply the source's smooth, open-domain definition of an integral of motion, with the data law universally quantified.

## Complete Proof

Fix an arbitrary admissible data law \(\mu\), and suppress its subscript on the risk. Put
\[
t_g(x)=\rho_{\mathsf H}(g)T(x),\qquad z_g(y)=\rho_Y(g)y.
\]
Orthogonality gives \(\|t_g(x)\|=\|T(x)\|\) and \(\|z_g(y)\|=\|y\|\). The stated second-moment condition therefore makes
\[
S=\mathbb E_\mu\int_G t_g(x)t_g(x)^*\,dg,
\qquad
L=\mathbb E_\mu\int_G z_g(y)t_g(x)^*\,dg,
\qquad
c=\mathbb E_\mu\|y\|^2
\]
finite. For the cross moment, use
\(\|z_g t_g^*\|_{HS}=\|y\|\|T(x)\|\) and Cauchy–Schwarz. Here \(uv^*\) denotes the linear map \(w\mapsto u\langle v,w\rangle\).

For an arbitrary linear map \(N:\mathsf H\to Y\), expansion of the square gives
\[
\mathcal J(N):=\mathbb E_\mu\int_G\|N t_g(x)-z_g(y)\|^2\,dg
=\operatorname{tr}(NSN^*)-2\langle N,L\rangle_{HS}+c.
\]
All terms are integrable by the estimates just given. Thus \(\mathcal J\) is a finite quadratic polynomial on \(\operatorname{Hom}(\mathsf H,Y)\), and \(R=\mathcal J\circ M\) is smooth on the entire parameter space.

For \(h\in G\), left invariance of Haar measure gives
\[
\rho_{\mathsf H}(h)S\rho_{\mathsf H}(h)^*=S,
\qquad
\rho_Y(h)L\rho_{\mathsf H}(h)^*=L.
\]
For example, conjugating the integrand defining \(S\) replaces \(t_g\) by \(t_{hg}\), and the same replacement applies to both factors defining \(L\). Since \(S=S^*\) and the representations are orthogonal, these identities say precisely that
\[
S\in\operatorname{Sym}^2_G(\mathsf H),\qquad L\in\operatorname{Hom}_G(\mathsf H,Y).
\]

For \(B\in\mathcal H\), cyclicity of trace and the Hilbert–Schmidt inner product yield
\[
\begin{aligned}
\mathcal J(NB)
&=\operatorname{tr}(NB S B^*N^*)-2\langle NB,L\rangle_{HS}+c\\
&=\operatorname{tr}(N S N^*)-2\langle N,LB^*\rangle_{HS}+c\\
&=\mathcal J(N).
\end{aligned}
\]
Applying this to \(N=M(P,\xi)\) and the assumed witness \(B_a\) proves
\[
R(aP,\xi)=R(P,\xi)\qquad(a\in O(V)).
\]
No homomorphism property or regularity of \(a\mapsto B_a\) is needed.

### The invariant-theory background and its precise limitation

The elementary orbit statement appearing in the source can be verified directly. If \(P^*P=Q^*Q\), then \(\ker P=\ker Q\), because \(\|Pw\|^2=\|Qw\|^2\). Consequently the rule \(Pw\mapsto Qw\) is a well-defined linear isometry from \(\operatorname{Ran}P\) onto \(\operatorname{Ran}Q\). Extend it between orthogonal complements to obtain \(a\in O(V)\) with \(Q=aP\). The converse follows from \(a^*a=I\). Hence orthogonal orbits are exactly Gram-matrix fibers.

This establishes set-theoretic factorization of an invariant function through \(P^*P\). It does not, by itself, establish smooth extension of that function to a neighborhood of a singular Gram matrix. The argument below derives the needed differential and ODE conclusions directly, so no unproved smooth-factorization premise is used.

### Differential consequences valid at every rank

Write
\[
F(P,\xi)=\nabla_P R(P,\xi),\qquad U(P,\xi)=\nabla_\xi R(P,\xi).
\]
Differentiating the invariance identity in arbitrary parameter directions, using the product Euclidean metric, gives
\[
F(aP,\xi)=aF(P,\xi),\qquad U(aP,\xi)=U(P,\xi).
\]

At a fixed parameter point let \(E_P=\operatorname{Ran}P\), and let \(a_P\) be the orthogonal map equal to the identity on \(E_P\) and minus the identity on \(E_P^\perp\). Since \(a_PP=P\), gradient equivariance implies \(a_PF=F\). Therefore
\[
\operatorname{Ran}F(P,\xi)\subseteq\operatorname{Ran}P.
\]
Also, for every skew-adjoint operator \(K\) on \(V\), differentiation of \(R(e^{sK}P,\xi)=R(P,\xi)\) at \(s=0\) gives
\[
0=\langle F,KP\rangle_{HS}=\operatorname{tr}(PF^*K).
\]
Orthogonality to all skew-adjoint operators implies that \(PF^*\) is self-adjoint, or equivalently
\[
FP^*=PF^*.
\]

These two identities give an explicit symmetric right multiplier at every rank. Define \(P^\dagger:V\to W\) as the inverse of the bijection
\(P:(\ker P)^\perp\to\operatorname{Ran}P\), extended by zero on \((\operatorname{Ran}P)^\perp\). Put
\[
E=P^\dagger P,\qquad D=P^\dagger F.
\]
Then \(E\) is the orthogonal projector onto \((\ker P)^\perp\), \(ED=D\), and \(PD=F\). Multiplying \(FP^*=PF^*\) on the left by \(P^\dagger\) and on the right by \((P^\dagger)^*\) gives
\[
DE=ED^*.
\]
Consequently
\[
A=D+D^*-DE
\]
is self-adjoint. Since \(P=PE\), we have \(PD^*=PED^*=PDE\), and hence
\[
PA=PD+PD^*-PDE=F.
\]
Thus \(\dot P=-PA\) pointwise. When \(P=0\), the range inclusion already gives \(F=0\), and the construction gives \(A=0\). We have not assumed that this formula is continuous across a rank change; that issue must be addressed before using a fundamental matrix.

### Rank preservation and coefficient regularity

Because \(R\) is smooth, the full vector field \((-F,-U)\) is locally Lipschitz. Its solutions with the same value at a time \(s\) are unique both forward and backward on their common interval. For completeness, locally a bound on the derivative gives a Lipschitz constant \(C\). The distance between two such solutions is bounded by \(C\) times the integral of that distance from \(s\); the elementary integral inequality gives zero distance. Reversing time gives the same conclusion to the left of \(s\), and continuation proves equality on the connected common interval.

Let \((P(t),\xi(t))\) be the given solution on \(J\). For a fixed \(a\in O(V)\), gradient equivariance shows that \((aP(t),\xi(t))\) solves the same coupled ODE. Fix any \(s\in J\), and choose the reflection \(a_s\) that is the identity on \(\operatorname{Ran}P(s)\) and minus the identity on its orthogonal complement. The two solutions agree at \(s\), so uniqueness implies
\[
a_sP(t)=P(t)\qquad(t\in J).
\]
Therefore \(\operatorname{Ran}P(t)\subseteq\operatorname{Ran}P(s)\). Applying the same argument with \(s\) and \(t\) interchanged proves equality. This already establishes the claimed conservation, including zero and rank-deficient initializations.

It also supplies the regularity needed to complete the source's linear-matrix route without circularly assuming rank preservation. The rank is constant on \(J\), and \(P^\dagger(t)\) is continuous there. To verify the latter explicitly at positive rank \(r\), choose \(r\) independent columns of \(P\) near a given time and place them in a matrix \(C\). On that neighborhood write \(P=CH\), where
\[
H=(C^*C)^{-1}C^*P.
\]
The matrix \(C\) has full column rank and \(H\) has full row rank. Direct multiplication verifies
\[
P^\dagger=H^*(HH^*)^{-1}(C^*C)^{-1}C^*.
\]
Every factor varies smoothly on this neighborhood. These local formulas represent the uniquely defined \(P^\dagger\), so they agree where they overlap. Rank zero is immediate. Thus the self-adjoint multiplier \(A(t)\) constructed above is continuous along the trajectory.

### Fundamental matrix and the conclusion

Solve
\[
\dot Q=-QA(t),\qquad Q(0)=I_W,
\]
and
\[
\dot Z=A(t)Z,\qquad Z(0)=I_W.
\]
Continuous coefficients give unique linear-ODE solutions on every compact subinterval of \(J\), and these solutions agree on overlaps. This elementary fact follows, for example, by iterating the integral equations: when \(\|A\|\le C\), the successive iterated integrals are bounded by \((C|t-s|)^k/k!\), which yields convergent solution series and uniqueness. Hence \(Q\) and \(Z\) are defined throughout \(J\).

Differentiating their product gives
\[
\frac{d}{dt}(QZ)=-QAZ+QAZ=0,
\]
so \(QZ=I_W\). A square matrix with a right inverse is invertible; therefore \(Q(t)\) is invertible for every \(t\in J\). Both \(P(t)\) and \(P(0)Q(t)\) solve the same linear equation \(\dot X=-XA(t)\) with the same initial value. Uniqueness gives
\[
P(t)=P(0)Q(t),
\]
and thus again
\[
\operatorname{Ran}P(t)=\operatorname{Ran}P(0).
\]
No assertion is made about an excluded endpoint or a limit as time tends to infinity. Zero-dimensional spaces satisfy the same identities with their unique zero maps and identity operators.

Finally, let \(I\) be smooth on the stated open set \(\Omega\) and depend only on \(\operatorname{Ran}P\). Any two points of a flow segment contained in \(\Omega\) have the same range, so they have the same value of \(I\). Since \(\mu\) was arbitrary, this holds for every admissible data law. Smoothness is required of \(I\) on its own domain; no global smoothness of the range map across rank strata is asserted.

## Closure Summary

The moment expansion, Haar identities, stabilizer invariance, parameter pullback, all-rank differential identities, coupled-flow uniqueness, continuous multiplier, invertible fundamental matrix, and integral-of-motion conclusion have all been explicitly justified. The Gram-orbit background is also derived, but smooth quotient factorization is not used as an unverified premise. There are no unresolved private proof obligations.
