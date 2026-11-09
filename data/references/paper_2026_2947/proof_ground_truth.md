# Reference Proof

## Proof Structure

Restrict the map to rectangular diagonal matrices. Sign stabilizers force the image to be diagonal and to vanish in zero-singular-value coordinates. Permutation symmetries make the diagonal rule permutation-equivariant. Extend it by signs and prove continuity across orthant boundaries. Equivariance then gives the spectral representation for every SVD. Derive the full rectangular SVD stabilizer from its two Gram matrices to establish well-definedness, including repeated-value and null-space rotations. The converse follows from transformed SVDs, and continuity follows from compactness and an explicit limiting-SVD argument.

## Complete Proof

Let $r=\min(m,n)$ and let $E(x)$ be the rectangular diagonal embedding. We use the finite-dimensional SVD with full orthogonal factors. The groups $O(m)$ and $O(n)$ are compact: their defining equations make them closed, and their entries are bounded. All continuity statements use the ordinary finite-dimensional topology.

### 1. Restriction to Diagonal Inputs

Assume that $U$ is continuous and bi-orthogonally equivariant. For $x\in[0,\infty)^r$, set $F(x)=U(E(x))$.

Choose diagonal sign matrices $S\in O(m)$ and $T\in O(n)$. Write their diagonal entries as $a_i$ and $b_j$. They stabilize $E(x)$ whenever $a_i=b_i$ for each $i\le r$ with $x_i\ne0$; signs at zero coordinates and at unmatched row or column coordinates are unrestricted. Equivariance then gives
\[
F(x)=SF(x)T^T,\qquad F(x)_{ij}=a_i b_j F(x)_{ij}.
\]
For any entry other than a diagonal entry $(i,i)$ with $i\le r$ and $x_i\ne0$, there is an allowed choice with $a_i b_j=-1$. Indeed, if row $i$ belongs to a nonzero diagonal coordinate and $j\ne i$, flip $a_i$ and its paired $b_i$ only. If row $i$ belongs to a zero or unmatched coordinate, flip $a_i$ alone. This also eliminates the diagonal entries at zero coordinates. Thus
\[
F(x)=E(\psi(x)),\qquad \psi_i(x)=0\ \text{whenever }x_i=0.
\]
The map $\psi:[0,\infty)^r\to\mathbb R^r$ is continuous because $\psi_i(x)=U(E(x))_{ii}$.

For an $r\times r$ permutation matrix $\Pi$, extend it to orthogonal matrices $\widehat\Pi_m$ and $\widehat\Pi_n$ by leaving unmatched coordinates fixed. Then
\[
\widehat\Pi_m E(x)\widehat\Pi_n^T=E(\Pi x).
\]
Equivariance and comparison of diagonal entries yield
\[
\psi(\Pi x)=\Pi\psi(x).
\]
In particular, if $x_i=x_j$, transposing these coordinates fixes $x$, so $\psi_i(x)=\psi_j(x)$.

### 2. The Absolutely Symmetric Extension

For $z\in\mathbb R^r$, choose a signed permutation $R$ satisfying $z=R|z|$, and set
\[
\widetilde\psi(z)=R\psi(|z|).
\]
Such a choice exists using only diagonal signs. To check independence of the choice, write $R=D\Pi$, where $D$ is a diagonal sign matrix and $\Pi$ a permutation matrix. Taking absolute values in $z=D\Pi|z|$ gives $\Pi|z|=|z|$. Consequently, permutation covariance gives $\Pi\psi(|z|)=\psi(|z|)$. At coordinates where $|z_i|>0$, the sign in $D$ is forced to be the sign of $z_i$. At coordinates where $z_i=0$, the corresponding coordinate of $\psi(|z|)$ is zero, so the choice of sign has no effect. This proves well-definedness and also shows that the extension restricts to $\psi$ on the nonnegative orthant.

Equivalently, with $\operatorname{sgn}(0)=0$, its coordinates are
\[
\widetilde\psi_i(z)=\operatorname{sgn}(z_i)\psi_i(|z|).
\]
This formula proves sign covariance: for every diagonal sign matrix $D$, $\widetilde\psi(Dz)=D\widetilde\psi(z)$, with zero coordinates covered by the zero-coordinate property. Together with $|\Pi z|=\Pi|z|$ and permutation covariance of $\psi$, it also gives $\widetilde\psi(\Pi z)=\Pi\widetilde\psi(z)$. Every signed permutation is a product of these transformations, so $\widetilde\psi$ is absolutely symmetric.

We now prove continuity, including orthant boundaries. Let $z_k\to z$. Then $|z_k|\to|z|$ and $\psi(|z_k|)\to\psi(|z|)$. If $z_i\ne0$, its sign is eventually constant, and the coordinate formula gives $\widetilde\psi_i(z_k)\to\widetilde\psi_i(z)$. If $z_i=0$, then $\psi_i(|z|)=0$ and
\[
|\widetilde\psi_i(z_k)|\le |\psi_i(|z_k|)|\longrightarrow0=\widetilde\psi_i(z).
\]
Thus every coordinate converges, proving continuity globally.

### 3. Spectral Representation and the Full SVD Stabilizer

For any SVD $G=P E(\sigma(G))Q^T$, equivariance gives
\[
U(G)=P U(E(\sigma(G)))Q^T
    =P E(\psi(\sigma(G)))Q^T.
\]
Because $U$ is already a fixed map, this equality for every SVD itself establishes independence of the chosen SVD in the necessary direction. We additionally derive the stabilizer description needed to construct a map in the converse.

Fix $s\in[0,\infty)^r$, put $C=E(s)$, and suppose $R\in O(m)$ and $S\in O(n)$ satisfy $RCS^T=C$. Multiplying this equation by its transpose, in both orders, gives
\[
RCC^TR^T=CC^T,\qquad SC^TCS^T=C^TC.
\]
Hence $R$ commutes with $CC^T$ and $S$ commutes with $C^TC$. If $v$ belongs to an eigenspace of either Gram matrix with eigenvalue $\lambda$, commutation shows that its image under the corresponding orthogonal matrix belongs to the same eigenspace. Therefore both matrices preserve each positive singular-value block and their respective complete null spaces. In particular, distinct positive blocks cannot mix with one another or with the null spaces.

For a positive value $d$, let $I_d=\{i:s_i=d\}$. The restriction of $C$ between the corresponding right and left coordinate spaces is $dI$. Restricting $RCS^T=C$ to this block yields
\[
dR_dS_d^T=dI,
\]
so $R_d=S_d$. There is no coupling requirement between the left and right null-space actions, whose dimensions can differ for rectangular matrices.

Suppose $y\in\mathbb R^r$ is constant on each $I_d$ and satisfies $y_i=0$ when $s_i=0$. On a positive block, $E(y)$ is $a_d I$ for some scalar $a_d$, so
\[
R_d(a_d I)S_d^T=a_d R_dR_d^T=a_d I.
\]
Its entire null-space part is zero, including unmatched rectangular coordinates. Thus
\[
R E(y)S^T=E(y).
\]
For $y=\psi(s)$ the required conditions were proved above. If two SVDs have factors $P,Q$ and $P',Q'$, set $R=P^TP'$ and $S=Q^TQ'$. Their equality as factorizations gives $RE(s)S^T=E(s)$, and the identity just proved shows that their output formulas agree. This includes repeated singular values, rank deficiency, the zero matrix, and both rectangular orientations.

### 4. Converse Equivariance

Let $\widetilde\psi:\mathbb R^r\to\mathbb R^r$ be continuous and absolutely symmetric, and let $\psi$ be its restriction to $[0,\infty)^r$. If $s_i=0$, the sign flip of coordinate $i$ fixes $s$, and absolute symmetry forces $\psi_i(s)=-\psi_i(s)$, hence $\psi_i(s)=0$. If $s_i=s_j$, transposing those coordinates fixes $s$, so $\psi_i(s)=\psi_j(s)$. The stabilizer argument in Section 3 therefore applies to this $\psi$ and proves that
\[
U(G)=P E(\psi(\sigma(G)))Q^T
\]
is well-defined for every matrix $G$.

For $A\in O(m)$ and $B\in O(n)$, the factorization
\[
AGB^T=(AP)E(\sigma(G))(BQ)^T
\]
is an SVD: its factors are orthogonal and the ordered nonnegative diagonal is unchanged. Using this factorization and well-definedness gives
\[
U(AGB^T)=A\,U(G)\,B^T.
\]
Thus $U$ is bi-orthogonally equivariant.

### 5. Continuity of the Reconstructed Map

We first justify continuity of the ordered singular-value vector using the SVD and compactness. Suppose $G_k\to G$, choose SVDs $G_k=P_kE(s_k)Q_k^T$, and write $s_k=\sigma(G_k)$. Orthogonal invariance of the Frobenius norm gives $\|s_k\|_2=\|G_k\|_F$, so the vectors $s_k$ are bounded. From any subsequence, compactness and boundedness supply a further subsequence on which $P_k\to P_*$, $Q_k\to Q_*$, and $s_k\to s_*$. The limiting factors are orthogonal, and $s_*$ remains nonnegative and nonincreasing. Passing to the limit in the input factorizations gives
\[
G=P_*E(s_*)Q_*^T.
\]
This is an SVD of $G$, so uniqueness of the ordered singular values gives $s_*=\sigma(G)$. If $s_k$ did not converge to $\sigma(G)$, a subsequence staying a positive distance away would admit the further subsequence just described, a contradiction. Hence $\sigma(G_k)\to\sigma(G)$.

Now take any subsequence of the inputs $G_k$. Compactness supplies a further subsequence along which $P_k\to P_*$ and $Q_k\to Q_*$. Singular-value continuity and passage to the limit give
\[
G=P_*E(\sigma(G))Q_*^T.
\]
The limiting factors therefore form an SVD of the limit matrix. Continuity of $\psi$ gives, along this further subsequence,
\[
U(G_k)=P_kE(\psi(\sigma(G_k)))Q_k^T
\longrightarrow P_*E(\psi(\sigma(G)))Q_*^T=U(G),
\]
where the last equality uses SVD-independence. Finally, if the full output sequence failed to converge to $U(G)$, there would be a subsequence and $\varepsilon>0$ with $\|U(G_k)-U(G)\|_F\ge\varepsilon$ throughout. The further convergent subsequence just constructed contradicts that inequality. Thus $U(G_k)\to U(G)$, proving continuity and completing the characterization.
