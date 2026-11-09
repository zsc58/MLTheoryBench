# Reference Proof

## Proof Structure

We first show that universality of the shared-encoder architecture implies density of the indexed architecture with the same latent dimension. We then construct two fixed disjoint compact sets such that every subthreshold indexed latent map has a collision between them. Alternating finite differences propagate equalities from an axis subset to a full finite grid; Borsuk-Ulam supplies the axis equalities. A single continuous function separating the fixed compact sets proves non-density.

The argument applies to arbitrary continuous encoders and decoders, as in the public task. It does not assume that the minimum dimension for this continuous class equals the minimum for the source's MLP subclass.

## Complete Proof

Set
\[
D=d(n-k),\qquad s=\left\lceil(D+1)^{1/k}\right\rceil,
\qquad q=s^k-(s-1)^k.
\]
Here \(D\ge1\), \(s\ge2\), and \(q\ge1\). We show that every admissible integer latent dimension \(M\) satisfying \(Mq<D\) fails to be universal.

### 1. Reduction to the indexed architecture

An indexed function of latent dimension \(M\) has the form
\[
\rho\!\left(\sum_{i_1,\ldots,i_k=1}^n
\phi_{i_1,\ldots,i_k}(z_{i_1},\ldots,z_{i_k})\right),
\]
where the tuple-dependent maps \(\phi_{i_1,\ldots,i_k}:K^k\to\mathbb R^M\) and the decoder \(\rho:\mathbb R^M\to\mathbb R\) are continuous. Write \(M_{\rm ind}(d,n,k)\) for the least dimension at which this class is dense in \(C(K^n)\).

Choose pairwise disjoint closed nondegenerate cubes \(C_1,\ldots,C_n\subset(0,1)^d\) and affine homeomorphisms \(T_j:K\to C_j\). Put
\[
T(z)=(T_1z_1,\ldots,T_nz_n),\qquad L=T(K^n).
\]
For a permutation \(\sigma\), let
\(P_\sigma(y_1,\ldots,y_n)=(y_{\sigma(1)},\ldots,y_{\sigma(n)})\), and set
\[
U=\bigcup_{\sigma\in\mathfrak S_n}P_\sigma L.
\]
The permuted copies are pairwise disjoint compact sets: distinct permutations put different cube labels in at least one coordinate.

Fix an arbitrary \(g\in C(K^n)\). Define \(h:U\to\mathbb R\) by
\[
h\bigl(T_{\sigma(1)}z_{\sigma(1)},\ldots,
T_{\sigma(n)}z_{\sigma(n)}\bigr)=g(z_1,\ldots,z_n).
\]
Both the cube labels and their associated coordinates move under the permutation. Each configuration in \(U\) determines exactly one point in each cube, and therefore a unique labeled tuple \(z\). Thus \(h\) is well defined, continuous on each compact component and hence on their finite disjoint union, and invariant under coordinate permutations.

We use the Tietze extension theorem in the following standard form: a continuous real-valued function on a closed subset of a normal space extends continuously to the whole space. Here \(K^n\) is a compact metric space and hence normal, \(U\) is closed, and \(h\) is continuous. Consequently, there is \(H\in C(K^n)\) with \(H|_U=h\). Define
\[
f(x)=\frac1{n!}\sum_{\sigma\in\mathfrak S_n}H(P_\sigma x).
\]
Then \(f\) is continuous and symmetric. For every \(z\in K^n\), every summand at \(x=T(z)\) equals \(g(z)\), so
\[
f(T_1z_1,\ldots,T_nz_n)=g(z).
\]

Suppose the shared-encoder class of dimension \(M\) is dense in \(C_{\rm sym}(K^n)\). Given any accuracy \(\eta>0\), choose continuous \(\Phi:K^k\to\mathbb R^M\) and \(\rho:\mathbb R^M\to\mathbb R\) whose pooled function approximates \(f\) uniformly within \(\eta\). Restricting to \(L\) gives an approximation to \(g\) of the same accuracy. Indeed, for \(I=(i_1,\ldots,i_k)\), define
\[
\phi_I(u_1,\ldots,u_k)
=\Phi(T_{i_1}u_1,\ldots,T_{i_k}u_k).
\]
These maps are continuous, including for tuples with repeated indices, and the restricted approximant is indexed. Therefore density of the shared-encoder class implies density of the indexed class at the same \(M\). This permits the encoder to depend on both the target and the desired accuracy; no fixed-feature assumption is made.

### 2. Alternating finite-difference rigidity

Let
\[
\Psi(x_1,\ldots,x_n)
=\sum_{i_1,\ldots,i_k=1}^n
\phi_{i_1,\ldots,i_k}(x_{i_1},\ldots,x_{i_k})
\]
be an arbitrary indexed latent map. For \(a_j,y_j\in\mathbb R^d\) with \(a_j+\eta_jy_j\in K\) for \(\eta_j\in\{0,1\}\), consider
\[
\sum_{\eta\in\{0,1\}^k}(-1)^{|\eta|}
\Psi(a_1+\eta_1y_1,\ldots,a_k+\eta_ky_k,
 x_{k+1},\ldots,x_n).
\]
Any tuple summand omitting one of the first \(k\) variables cancels by pairing terms that differ only in the corresponding component of \(\eta\). A surviving summand must involve all of the first \(k\) variables. Since it has only \(k\) argument slots, it cannot also involve a tail variable. Thus the entire alternating sum is independent of \(x_{k+1},\ldots,x_n\). This reasoning also handles repeated indices: a tuple containing repetitions cannot contain all \(k\) distinct base indices and therefore cancels.

### 3. Propagation from the axes to the grid

Choose a finite \(G\subset K\) with \(0\in G\) and \(|G|=s\), which is possible because \(d\ge1\) and \(K\) is infinite. Set
\[
A=\{(y_1,\ldots,y_k)\in G^k:
 y_j=0\text{ for at least one }j\}.
\]
Its complement in \(G^k\) is \((G\setminus\{0\})^k\), so \(|A|=q\).

Suppose tails \(t,t'\in K^{n-k}\) satisfy
\[
\Psi(x_b,t)=\Psi(x_b,t')\qquad(x_b\in A).
\]
For \(z=(z_1,\ldots,z_k)\in G^k\setminus A\), apply the preceding finite-difference identity with all base points zero and increments \(z_j\). Its vertices are
\((\eta_1z_1,\ldots,\eta_kz_k)\). Every vertex except \(z\) belongs to \(A\). The alternating sums for tails \(t\) and \(t'\) agree because they are independent of the tail. Subtracting them cancels all vertices except \(z\), whose coefficient is \((-1)^k\ne0\). Hence
\[
\Psi(z,t)=\Psi(z,t').
\]
Together with the assumption on \(A\), this proves equality at every point of \(G^k\).

### 4. Fixed obstruction sets and their collision property

Identify the tail space with \(K^{n-k}=[0,1]^D\). Let
\[
S^{D-1}=\{u\in\mathbb R^D:\|u\|_2=1\},\qquad
c=(1/2,\ldots,1/2),
\]
choose \(0<\varepsilon<1/2\), and define
\[
\delta(u)=c+\varepsilon u.
\]
This is an injective continuous map into the interior of \(K^{n-k}\), with \(\delta(-u)=c-\varepsilon u\).

We explicitly construct a closed cover \(B_1,\ldots,B_{D+1}\) of \(S^{D-1}\) with no antipodal pair in any member. Choose the vertices \(v_1,\ldots,v_{D+1}\in\mathbb R^D\) of a centered regular simplex. For example, take the vectors
\(e_r-\mathbf1/(D+1)\) in the \(D\)-dimensional hyperplane of \(\mathbb R^{D+1}\) whose coordinates sum to zero, and identify that hyperplane isometrically with \(\mathbb R^D\). For every fixed \(r\), the differences \(v_r-v_j\), \(j\ne r\), span \(\mathbb R^D\). Define
\[
B_r=\{u\in S^{D-1}:\langle u,v_r\rangle
\ge\langle u,v_j\rangle\text{ for every }j\}.
\]
Each \(B_r\) is closed and therefore compact, and the sets cover the sphere because a finite collection of real numbers has a maximum. If both \(u\) and \(-u\) belong to \(B_r\), the two systems of inequalities imply
\[
\langle u,v_r-v_j\rangle=0\qquad\text{for every }j.
\]
The spanning property forces \(u=0\), contrary to \(u\in S^{D-1}\). Thus \(B_r\cap(-B_r)=\varnothing\). This construction remains valid for \(D=1\).

Since \(|G^k|=s^k\ge D+1\), choose an injection
\[
\chi:\{1,\ldots,D+1\}\longrightarrow G^k.
\]
Before selecting any indexed latent map, fix the sets
\[
E^+=\bigcup_{r=1}^{D+1}
\{(\chi(r),\delta(u)):u\in B_r\},
\qquad
E^-=\bigcup_{r=1}^{D+1}
\{(\chi(r),\delta(-u)):u\in B_r\}.
\]
They are nonempty compact subsets of \(K^n\), since the sphere is nonempty, the \(B_r\) cover it, and each set is a finite union of continuous images of compact sets. They depend only on the fixed geometric choices, not on an encoder or decoder.

They are disjoint. Indeed, an intersection would give
\[
(\chi(r),\delta(u))=(\chi(j),\delta(-v)),
\qquad u\in B_r,\quad v\in B_j.
\]
Injectivity of \(\chi\) gives \(r=j\), and injectivity of \(\delta\) gives \(u=-v\), contradicting \(B_r\cap(-B_r)=\varnothing\).

Now assume \(Mq<D\), and fix an arbitrary indexed latent map \(\Psi\). Enumerate the finite set \(A\) and define
\[
F:S^{D-1}\longrightarrow\mathbb R^{Mq},\qquad
F(u)=\bigl(\Psi(x_b,\delta(u))\bigr)_{x_b\in A}.
\]
The map is continuous because \(\Psi\) and \(\delta\) are continuous and the concatenation has finitely many components.

We use the standard Borsuk-Ulam consequence that a continuous map \(S^\ell\to\mathbb R^m\), with integers \(0\le m\le\ell\), takes equal values at some antipodal pair. The lower-dimensional codomain case follows by padding with zero coordinates; when \(\ell=m=0\), the conclusion is immediate. Here \(\ell=D-1\), \(m=Mq\), and the integer inequality \(Mq<D\) gives \(m\le\ell\). Consequently, some \(u_*\in S^{D-1}\) satisfies
\[
\Psi(x_b,\delta(u_*))=\Psi(x_b,\delta(-u_*))
\qquad(x_b\in A).
\]
Step 3 propagates this equality to every \(x_b\in G^k\). Choose \(r\) with \(u_*\in B_r\). Then
\[
x^+=(\chi(r),\delta(u_*))\in E^+,
\qquad x^-=(\chi(r),\delta(-u_*))\in E^-,
\]
and \(\Psi(x^+)=\Psi(x^-)\).

The witness \(u_*\), the label \(r\), and the colliding pair may depend on \(\Psi\), but the sets \(E^+,E^-\) do not. Thus we have proved the required quantifier order: there exist fixed disjoint compact sets such that every indexed latent map of this dimension has a collision between them.

### 5. A single separating target proves non-density

Using those fixed sets, define
\[
g_0(x)=\frac{\operatorname{dist}(x,E^-)}
{\operatorname{dist}(x,E^+)+\operatorname{dist}(x,E^-)}.
\]
Distances are Euclidean distances in \(\mathbb R^{dn}\). Both sets are nonempty and closed, and their disjointness implies that the denominator is positive at every point. Thus \(g_0\in C(K^n)\), with \(g_0=1\) on \(E^+\) and \(g_0=0\) on \(E^-\). In particular, \(g_0\) is independent of the indexed encoder and decoder.

For any indexed latent map \(\Psi\) of dimension \(M\) and any continuous decoder \(\rho\), choose the colliding pair from Step 4 and put
\(a=\rho(\Psi(x^+))=\rho(\Psi(x^-))\). Then
\[
2\|g_0-\rho\circ\Psi\|_\infty
\ge |1-a|+|a|\ge1.
\]
Hence
\[
\forall\Psi\ \forall\rho,\qquad
\|g_0-\rho\circ\Psi\|_\infty\ge\tfrac12.
\]
The indexed class is therefore not dense whenever \(Mq<D\).

### 6. Integer threshold and transfer

Every integer \(M<\lceil D/q\rceil\) satisfies \(Mq<D\). Step 5 excludes all such indexed dimensions, so
\[
M_{\rm ind}(d,n,k)\ge\left\lceil\frac Dq\right\rceil.
\]
Step 1 implies that every universal shared-encoder dimension is also a dense indexed dimension. Therefore
\[
M_{\rm univ}(d,n,k)\ge M_{\rm ind}(d,n,k)
\ge\left\lceil\frac{d(n-k)}{s^k-(s-1)^k}\right\rceil,
\qquad s=\left\lceil(d(n-k)+1)^{1/k}\right\rceil.
\]
The parameter range ensures that no denominator vanishes. For \(k=1\), \(q=1\), and the same proof applies. When \(D=1\), the asserted bound is \(1\); it is automatic if latent dimensions start at \(1\), and if dimension \(0\) is allowed it is excluded by the same argument, using the trivial map \(S^0\to\mathbb R^0\). No case with \(k=n\) is part of the claimed range.
