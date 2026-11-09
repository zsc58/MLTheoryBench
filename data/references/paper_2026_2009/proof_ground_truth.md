# Reference Proof

## Proof Structure

Construct an open dense set of positive probability-density tuples whose coordinate-ratio map is an embedding, using Whitney's generic embedding theorem, homeomorphic coordinate changes on positive functions, and componentwise normalization. Then prove transport-map recovery by cancelling Jacobians in pushforward ratios, and vector-field recovery by subtracting normalized weighted-divergence identities and using the differential of a logarithmic ratio embedding.

## Audited External Input

The standard independent Whitney generic embedding theorem used here states: if M is a smooth compact d-dimensional manifold and k>=2d+1, the C^1 embeddings M into R^k form an open dense subset of C^1(M,R^k), with its C^1 topology. The public assumptions give a smooth compact M, and the integer inequality m>2d+1 gives m-1>=2d+1. No paper-specific external theorem is needed.

## Complete Proof

Write μ_M and μ_N for the fixed Riemannian volume measures. If M is empty, then P^1_+(M) is empty, so D=∅ is open and dense in the empty tuple space and both assertions hold vacuously. Henceforth assume M is nonempty.

### 1. Generic ratio embeddings before normalization

Let A=C^1_+(M) be the strictly positive real-valued C^1 functions on M, and let P=P^1_+(M). Since M is compact, every function in A has a positive minimum. Consequently A is open in C^1(M), and every Y in A has a finite, strictly positive integral against μ_M.

For Y=(Y_1,...,Y_m) in A^m define
\[
R_Y=(Y_1/Y_m,\ldots,Y_{m-1}/Y_m).
\]
By the stated Whitney theorem, the set W of embeddings M into R^{m-1} is open and dense in C^1(M,R^{m-1}). Therefore
\[
W_+=W\cap A^{m-1}
\]
is open and dense in A^{m-1}: the positive-function space is itself an open subset of the ambient C^1 space.

The map
\[
F(Y)=(Y_1Y_m,\ldots,Y_{m-1}Y_m,Y_m)
\]
is a homeomorphism of A^m, with inverse
\[
F^{-1}(Z)=(Z_1/Z_m,\ldots,Z_{m-1}/Z_m,Z_m).
\]
Indeed, multiplication is continuous in the C^1 topology by the product rule. Division is continuous near any positive denominator because compactness bounds that denominator away from zero, and the quotient rule controls its first derivative. These facts prove continuity of both displayed maps.

The coordinate projection π:A^m→A^{m-1} is continuous and open: finite products of C^1 spaces have their product topology, and projecting a basic product-open neighborhood gives an open neighborhood. Hence Λ=π∘F^{-1}, which sends Y to R_Y, is continuous and open. It follows that
\[
Q=\Lambda^{-1}(W_+)=\{Y\in A^m:R_Y\text{ is an embedding}\}
\]
is open and dense in A^m. Openness follows from continuity. For density, any nonempty open U⊆A^m has nonempty open image Λ(U), which meets W_+; thus U meets Q.

### 2. Normalization and the common generic set

For Y∈A^m put
\[
a_j(Y)=\int_M Y_j\,d\mu_M,
\qquad I(Y)_j=Y_j/a_j(Y).
\]
All a_j(Y) are finite and positive. Integration is continuous in C^1, since
\[
\left|\int_M(Y_j-Z_j)\,d\mu_M\right|
\leq\mu_M(M)\|Y_j-Z_j\|_{C^0}.
\]
Therefore I:A^m→P^m is continuous. It is surjective because I(ρ)=ρ for ρ∈P^m.

Define
\[
D=Q\cap P^m.
\]
This set is relatively open in P^m. Moreover,
\[
R_{I(Y)}=
\left(\frac{a_m(Y)}{a_1(Y)}\frac{Y_1}{Y_m},\ldots,
\frac{a_m(Y)}{a_{m-1}(Y)}\frac{Y_{m-1}}{Y_m}\right).
\]
Every factor a_m(Y)/a_j(Y) is positive. Positive coordinate scaling is a linear diffeomorphism of the target and preserves embeddings. Thus I(Q)⊆D. Conversely, every ρ∈D belongs to Q and is fixed by I, so D⊆I(Q). Hence D=I(Q).

To verify density directly, let V be a nonempty relatively open subset of P^m. Surjectivity and continuity make I^{-1}(V) a nonempty open subset of A^m. Since Q is dense, choose Y∈Q∩I^{-1}(V). Then I(Y)∈D∩V. Thus D is dense, and therefore generic, in P^m.

For any ρ∈D the map
\[
\Phi_\rho=(\log(\rho_1/\rho_m),\ldots,
\log(\rho_{m-1}/\rho_m))
\]
is also an embedding. Indeed, R_ρ takes values in the positive orthant and componentwise logarithm is a diffeomorphism from that orthant to R^{m-1}. Composition preserves injectivity, injectivity of the differential, and the homeomorphism property.

### 3. Recovery from pushforwards

Fix ρ∈D and f,g∈Diff^1(M,N), and assume f_#ρ_j=g_#ρ_j for all j. Let J_{f^{-1}}(y)>0 and J_{g^{-1}}(y)>0 denote the absolute Jacobians of the inverse maps, computed relative to the fixed Riemannian volumes. Change of variables gives the continuous densities
\[
p_{f,j}(y)=\rho_j(f^{-1}y)J_{f^{-1}}(y),
\qquad
p_{g,j}(y)=\rho_j(g^{-1}y)J_{g^{-1}}(y).
\]
Only continuity of these pushed-forward densities is asserted or needed; a C^1 diffeomorphism need not push a C^1 density to a C^1 density.

Equality of the pushforward measures implies p_{f,j}=p_{g,j} μ_N-almost everywhere. These functions are continuous, so the equality holds everywhere: a nonzero continuous difference would have constant strict sign on some nonempty open neighborhood, which has positive Riemannian volume.

Divide the equality for each j<m by the equality for j=m. The denominators are strictly positive, and the Jacobians cancel, yielding
\[
R_\rho(f^{-1}y)=R_\rho(g^{-1}y)
\qquad(y\in N).
\]
Injectivity of R_ρ gives f^{-1}=g^{-1}, hence f=g. If Diff^1(M,N) is empty, this implication is vacuous and requires no change to D.

### 4. Recovery from weighted divergences

Fix v,w∈𝔛^1(M) satisfying the stated equalities, and set u=v-w. By linearity,
\[
\operatorname{div}(\rho_j u)=0\qquad(1\leq j\leq m).
\]
The Riemannian divergence obeys the product rule
\[
\operatorname{div}(\rho_j u)
=\rho_j\operatorname{div}u+d\rho_j(u).
\]
For completeness, in a smooth coordinate chart with volume density q and vector components u^a, expand
\[
q^{-1}\sum_{a=1}^d\partial_a(q\rho_j u^a)
=\rho_j q^{-1}\sum_{a=1}^d\partial_a(q u^a)
+\sum_{a=1}^d(\partial_a\rho_j)u^a.
\]
The smooth metric and C^1 functions and fields justify all derivatives. In dimension zero the sums are empty and the identity still holds.

Dividing by ρ_j>0 gives
\[
0=\rho_j^{-1}\operatorname{div}(\rho_j u)
=\operatorname{div}u+d(\log\rho_j)(u).
\]
Subtract the equation with j=m from each equation with j<m. At every x∈M this yields
\[
d\Phi_{\rho,x}(u(x))=0.
\]
Since Φ_ρ is an embedding, its differential is injective at every point. Thus u(x)=0 for every x, so v=w.

The same set D works for every pair f,g and every pair v,w, establishing both conclusions with the required quantifier order.
