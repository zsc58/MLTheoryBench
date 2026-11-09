# Reference Proof

## Proof Structure and Obligations

The public theorem has the following obligations: establish the real peripheral decomposition and characterize stable quotients; identify the prescribed gauge slice with the peripheral quotient and solve the reward equation uniquely; establish the Cesaro projection and the unique normalized bias; and derive the unique peripheral correction and all three comparison identities. The quotient contraction construction is retained as supporting material, not as an additional public conclusion. Each obligation is discharged below.

The attached anchor-basis support is audited separately at the end. Its definitions and repaired Fourier argument are private dependency documentation. Neither construction of anchors nor proof of the anchor-basis result is required from a solver of the public task.

## Complete Proof

Write \(V=\mathbb R^n\), and complexify spaces and operators when discussing eigenvalues. The spectral radius of the unique operator on the zero vector space is understood to be zero. All assertions concerning invertibility on that space have their usual vacuous meaning.

### 1. Peripheral decomposition, stable quotients, and minimality

Since \(P\) is row-stochastic, every power is row-stochastic and \(\|P^t\|_\infty=1\) for every integer \(t\geq0\). The same bound holds for its action on complex vectors with the coordinate sup norm. In particular, every eigenvalue has modulus at most one.

The finite-dimensional primary decomposition theorem gives
\[
V_{\mathbb C}=E_{\mathrm{per}}\oplus E_{\mathrm{s}},\qquad
E_{\mathrm{per}}=\bigoplus_{|\lambda|=1}E_\lambda,
\]
where \(E_{\mathrm{s}}\) is the sum of the remaining primary spaces. Each summand is invariant. For a real matrix, conjugation preserves both of these sums, so \(E_{\mathrm{per}}=\mathcal K_{\mathbb C}\); in particular \(\mathcal K\) is real and \(P\)-invariant. The restriction to \(E_{\mathrm{s}}\) has spectral radius below one.

For completeness, the primary decomposition also supplies polynomial spectral projections: the powers of the distinct linear factors of the minimal polynomial are pairwise coprime, so polynomial Bezout identities produce a polynomial in \(P_{\mathbb C}\) that is the identity on any specified primary component and zero on the others. Thus every \(P_{\mathbb C}\)-invariant subspace is preserved by these projections.

Let \(L\subseteq V\) be real and \(P\)-invariant. It follows that
\[
L_{\mathbb C}=\bigoplus_\lambda (L_{\mathbb C}\cap E_\lambda).
\]
If \(\mathcal K\subseteq L\), the complexified quotient is naturally
\[
(V/L)_{\mathbb C}\cong E_{\mathrm{s}}/(L_{\mathbb C}\cap E_{\mathrm{s}}).
\]
In a basis adapted to an invariant subspace, the representing matrix is block triangular, with the restriction and quotient matrices on the diagonal. Its characteristic polynomial is the product of theirs. Consequently the spectrum of this quotient is contained in the spectrum of \(P_{\mathbb C}|_{E_{\mathrm{s}}}\), and its spectral radius is below one. This includes the zero quotient.

Conversely, if \(\mathcal K\nsubseteq L\), then for some \(|\lambda|=1\), the image of \(E_\lambda\) in \(V_{\mathbb C}/L_{\mathbb C}\) is nonzero. This image is isomorphic to
\[
E_\lambda/(E_\lambda\cap L_{\mathbb C}).
\]
The induced operator there is \(\lambda I+N\), with \(N\) nilpotent. A nilpotent operator on a nonzero finite-dimensional space has a nonzero kernel, so \(\lambda\) is an eigenvalue on this image and hence of the full quotient operator. Therefore \(\rho(\overline P_L)\geq1\).

We have proved
\[
\rho(\overline P_L)<1\quad\Longleftrightarrow\quad\mathcal K\subseteq L.
\]
Since \(\mathcal K\) itself is invariant, it produces a stable quotient and is contained in every invariant subspace that does so. It is the unique least such subspace and therefore the unique inclusion-minimal one.

### 2. Supporting quotient contraction

Set \(A=\overline P_{\mathcal K}\). If \(V/\mathcal K=\{0\}\), its unique norm and any \(\gamma\in(0,1)\) give the desired contraction inequality.

Otherwise choose \(\rho(A)<\gamma<1\), choose real coordinates on the quotient, and put \(B=A/\gamma\). Then \(\rho(B)<1\). Powers of a Jordan block with eigenvalue of modulus less than one are finite sums of polynomial factors in \(t\) times geometrically decaying factors; a block with eigenvalue zero is eventually zero. Thus \(\sum_{t\geq0}\|B^t\|^2\) converges in any fixed matrix norm. It follows that
\[
H=\sum_{t=0}^{\infty}(B^{\mathsf T})^tB^t
\]
converges. Its terms are positive semidefinite and its zeroth term is the identity, so \(H\) is positive definite. Shifting the convergent series gives
\[
B^{\mathsf T}HB=H-I\preceq H.
\]
The quadratic norm \(\|z\|_q=(z^{\mathsf T}Hz)^{1/2}\) therefore satisfies
\[
\|Az\|_q\leq\gamma\|z\|_q.
\]
Its pullback \(\|x\|_q:=\|[x]_{\mathcal K}\|_q\) is a seminorm with kernel exactly \(\mathcal K\), and \(\|Px\|_q\leq\gamma\|x\|_q\).

### 3. Gauge-fixed reward decomposition

Because \(\rho(A)<1\), the operator \(I-A\) is invertible. Hence
\[
q=[r]_{\mathcal K}+Aq
\]
has the unique solution \(q=(I-A)^{-1}[r]_{\mathcal K}\).

The quotient map restricts to an isomorphism from \(\operatorname{ran}G\) onto \(V/\mathcal K\). Indeed, a vector in both \(\operatorname{ran}G\) and \(\ker G\) is zero, since \(G\) acts as the identity on its range. This proves injectivity. Also
\[
G(x-Gx)=Gx-G^2x=0,
\]
so \(x-Gx\in\mathcal K\) and \([Gx]_{\mathcal K}=[x]_{\mathcal K}\), proving surjectivity.

Let \(v\in\operatorname{ran}G\) be the unique representative of \(q\). Its quotient equation implies
\[
[v]_{\mathcal K}=[r+Pv]_{\mathcal K}.
\]
Applying \(G\) to their difference gives \(v=G(r+Pv)\). Define
\[
g=r-(I-P)v.
\]
The same quotient equality gives \(g\in\mathcal K\), and hence \(r=g+(I-P)v\).

If another pair \((g',v')\in\mathcal K\times\operatorname{ran}G\) satisfies this equation, then
\[
(I-A)[v']_{\mathcal K}=[r]_{\mathcal K}.
\]
Invertibility yields \([v']_{\mathcal K}=[v]_{\mathcal K}\), and injectivity on the gauge slice yields \(v'=v\), followed by \(g'=g\). Conversely, any fixed point \(v'=G(r+Pv')\) belongs to the gauge slice and gives a residual in \(\ker G=\mathcal K\), so it is this same pair. This proves the stated equivalence and uniqueness without requiring \(G\) to commute with \(P\).

### 4. Cesaro projection and normalized bias

Power boundedness excludes a nontrivial Jordan block at a unit-modulus eigenvalue. Indeed, such a block provides vectors \(u\ne0\) and \(w\) with
\[
(P_{\mathbb C}-\lambda I)u=0,\qquad (P_{\mathbb C}-\lambda I)w=u.
\]
Then
\[
P_{\mathbb C}^tw=\lambda^tw+t\lambda^{t-1}u,
\]
whose norm is at least \(t\|u\|-\|w\|\), contradicting power boundedness. Thus peripheral eigenvalues are semisimple.

On the eigenvalue-one space the Cesaro averages are the identity. On an eigenspace with \(|\lambda|=1\) and \(\lambda\ne1\), their scalar multiplier is
\[
\frac{1-\lambda^T}{T(1-\lambda)}\longrightarrow0.
\]
On the strictly stable primary space, powers tend to zero by the same Jordan-block calculation used above, so their Cesaro averages also tend to zero. This proves existence of \(C\), which is the projection onto the eigenvalue-one space along the other primary components. In particular,
\[
C^2=C,\qquad CP=PC=C,\qquad \operatorname{ran}C=\ker(I-P)\subseteq\mathcal K.
\]

Set \(\rho=Cr\). Then \(r-\rho\in\ker C\). The operator \(I-P\) maps \(\ker C\) to itself. If \(x\in\ker C\) and \((I-P)x=0\), then \(x\in\operatorname{ran}C\), so \(x=Cx=0\). This restriction of \(I-P\) is therefore injective and, in finite dimension, bijective. There is a unique \(h\in\ker C\) such that
\[
(I-P)h=r-\rho.
\]
This is exactly the unique normalized bias.

### 5. Exact gain-bias comparison

Apply \(C\) to \(r=g+(I-P)v\). Since \(C(I-P)=0\),
\[
Cg=Cr=\rho.
\]
Both \(g\) and \(\rho\) belong to \(\mathcal K\), and \(C(g-\rho)=0\). Thus
\[
g-\rho\in W:=\mathcal K\cap\ker C.
\]
The operator \(I-P\) maps \(W\) into itself, because both defining spaces are invariant. Its restriction is injective by the preceding argument and therefore bijective, including when \(W=\{0\}\). Consequently there is a unique \(\psi\in W\) with
\[
g=\rho+(I-P)\psi.
\]
Comparing the two expressions for \(r\) gives
\[
(I-P)(h-v-\psi)=0.
\]
Hence \(h-v-\psi\in\operatorname{ran}C\). Applying \(C\), using \(Ch=C\psi=0\), yields
\[
h-v-\psi=C(h-v-\psi)=-Cv,
\]
so
\[
h=v+\psi-Cv.
\]
Since \(Gv=v\), \(G\psi=0\), and \(Cv\in\mathcal K=\ker G\), it follows that \(Gh=v\). Finally,
\[
(I-G)h=h-v=\psi-Cv,
\]
and \((I-P)Cv=0\), giving
\[
g=\rho+(I-P)(I-G)h.
\]
All public conclusions are proved. In particular, if \(\mathcal K=V\), the quotient and gauge slice are zero, \(G=0\), and the argument gives \(v=0\), \(g=r\), with the same normalized-bias comparison. No positive quotient dimension or nonzero correction space was assumed.

## Private Audit of Attached Anchor-Basis Support

This section closes the already-attached support record theory_015 and its omitted definition dependency theory_014. It is not an additional public task or scoring requirement.

### Definitions and audited independent background

Decompose the finite chain into transient states \(\mathsf T\) and closed irreducible recurrent classes \(F_1,\ldots,F_m\). Let \(\mathsf F=\bigcup_iF_i\). A class \(F_i\) of period \(d_i\) has cyclic sets \(C_{i,0},\ldots,C_{i,d_i-1}\), indexed so that transitions advance the phase by one modulo \(d_i\). Choose \(a_{i,k}\in C_{i,k}\).

The independent finite-chain facts used here, recorded in theory_018, are: the recurrent set is reached almost surely from every transient state; the transient block has spectral radius below one; and a finite irreducible stochastic block of period \(d_i\) has precisely the \(d_i\)-th roots of unity as peripheral eigenvalues, each of algebraic multiplicity one. Their hypotheses hold because \(P\) is a finite stochastic matrix and the blocks are its closed irreducible classes. If there are no transient states, the transient block is absent and the corresponding spectral assertion is vacuous.

For \(\tau=\inf\{t\geq0:X_t\in\mathsf F\}\), define \(b_{i,k}\) to be the indicator of \(C_{i,k}\) on recurrent states, and for transient \(s\) define
\[
b_{i,k}(s)=\mathbb P_s\{\operatorname{cls}(X_\tau)=i,\ \operatorname{phase}(X_\tau)-\tau\equiv k\pmod{d_i}\}.
\]
The phase condition is considered on the event that the terminal class is \(i\). Almost-sure absorption makes these well-defined probabilities. The events partition the possible terminal class-offset pairs, so the coordinates are nonnegative and sum to one. Define
\[
(\Pi x)(s)=x(s)-\sum_{i,k}x(a_{i,k})b_{i,k}(s).
\]

### Cyclic action and projection

For a recurrent state in \(F_i\), the deterministic phase advance gives \((Pb_{i,k})(s)=b_{i,k-1}(s)\). For a recurrent state in another class, both sides are zero. For a transient start, condition on \(X_1\). The remaining hitting time is \(\tau-1\), so the terminal phase minus that remaining time is the original offset plus one. The event defining \(b_{i,k}(X_1)\) therefore corresponds to original offset \(k-1\). Taking expectations yields
\[
Pb_{i,k}=b_{i,k-1\bmod d_i}.
\]
At anchors,
\[
b_{i,k}(a_{j,\ell})=\mathbf1\{(i,k)=(j,\ell)\}.
\]
Thus the basis functions are linearly independent, \(\Pi x\) vanishes at every anchor, and applying \(\Pi\) again changes nothing. Hence \(\Pi^2=\Pi\). The anchor identity also shows that \(\Pi\) kills every linear combination of the \(b_{i,k}\). Conversely, \(\Pi x=0\) expresses \(x\) as just such a combination. Therefore
\[
\ker\Pi=\mathcal B:=\operatorname{span}_{\mathbb R}\{b_{i,k}\},\qquad
\dim_{\mathbb R}\mathcal B=\sum_i d_i.
\]

### Repaired Fourier inclusion and dimension equality

Let \(\omega_i=e^{2\pi\mathrm i/d_i}\) and
\[
\psi_{i,\ell}=\sum_{k=0}^{d_i-1}\omega_i^{\ell k}b_{i,k},\qquad 0\leq\ell<d_i.
\]
The cyclic action and a change of index give
\[
P_{\mathbb C}\psi_{i,\ell}=\omega_i^\ell\psi_{i,\ell}.
\]
These vectors are nonzero, for example by evaluation at \(a_{i,0}\), so they lie in \(E_{\mathrm{per}}\).

The corrected inverse Fourier step is
\[
b_{i,k}=\frac1{d_i}\sum_{\ell=0}^{d_i-1}\omega_i^{-\ell k}\psi_{i,\ell}.
\]
The coefficients here are generally complex. This proves \(b_{i,k}\in E_{\mathrm{per}}\); since \(b_{i,k}\) is real-valued, it follows that \(b_{i,k}\in E_{\mathrm{per}}\cap\mathbb R^n=\mathcal K\). Thus \(\mathcal B\subseteq\mathcal K\). This replaces the incorrect assertion at source L001106 that the inverse Fourier coefficients are real.

Finally, order the states so that
\[
P=\begin{pmatrix}Q&R\\0&\operatorname{diag}(P_1,\ldots,P_m)\end{pmatrix}.
\]
The block-triangular characteristic polynomial and the audited background facts show that the total algebraic multiplicity of peripheral eigenvalues is \(\sum_i d_i\). Hence \(\dim_{\mathbb C}E_{\mathrm{per}}=\sum_i d_i\). Conjugation invariance gives \(E_{\mathrm{per}}=\mathcal K_{\mathbb C}\), so \(\dim_{\mathbb R}\mathcal K=\sum_i d_i\). The inclusion and equal dimensions prove \(\mathcal B=\mathcal K\), and therefore \(\ker\Pi=\mathcal K\).

The attached support statement is consequently valid after this local proof repair. The public proof above does not specialize its arbitrary projection \(G\) to this anchor construction.
