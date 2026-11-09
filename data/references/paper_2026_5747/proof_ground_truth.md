# Reference Proof

## Proof obligations

The proof must establish: the padded event-time formula and forward estimate for arbitrary event counts; exact inversion including the eventless path; the inverse square-root bound for every positive separation parameter; measurable recovery of counting-path laws; existence of the signature expectations; and separation by a finite signature degree. The general signature-determinacy and tree-like-uniqueness citations are not taken as unproved black boxes. Their required special case is derived in Section 4.

## 1. Global forward stability

Write the event times as \(t_1<\cdots<t_m\) and \(s_1<\cdots<s_n\). By symmetry assume \(m\le n\). For the distance calculation pad the first list by \(t_i=T\) for \(m<i\le n\). On \([0,T)\), the difference of the counting functions is the sum of the rank-paired indicator differences. Opposite-signed nonzero summands cannot coexist: if rank \(i\) contributes positively and rank \(j\) negatively, the ordering of the two event lists gives a contradiction, using the \(s\)-ordering when \(i<j\) and the \(t\)-ordering when \(i>j\). Thus the absolute value passes through the sum. Integration gives
\[
D:=d_N(\eta,\xi)=\sum_{i=1}^m|t_i-s_i|+\sum_{i=m+1}^n(T-s_i)=\sum_{i=1}^n|t_i-s_i|.
\]
The endpoint \(T\) has no effect on this integral.

Use the original augmented grids through \(t_{m+1}=T\) and \(s_{n+1}=T\), and write \(\sigma_k=s_k-s_{k-1}\), with \(\sigma_0=0\). For \(0\le k\le m+1\), put \(e_k=t_k-s_k\). Then \(e_0=0\),
\[
\tau_k-\sigma_k=e_k-e_{k-1}\quad(1\le k\le m+1),
\qquad
\sum_{k=0}^{m+1}|\tau_k-\sigma_k|\le2D.
\]
Indeed, each interior error is counted at most twice; if \(m=n\), the last error is zero, and if \(m<n\), it is one of the padded errors in \(D\).

Set \(x=\Phi(\eta)\) and \(y=\Phi(\xi)\). Define \(\widetilde y\) by the nodal values \(\widetilde y(t_k)=\sigma_k\) for \(0\le k\le m+1\), with affine interpolation. These are rank-matched nodal values, not evaluations \(y(t_k)\). For an affine function \(h\) on \([a,b]\), convexity of absolute value gives
\[
\int_a^b|h(u)|\,du\le\frac{b-a}{2}(|h(a)|+|h(b)|).
\]
Summing this estimate for \(x-\widetilde y\), each nodal error has coefficient at most \(T/2\): an interior coefficient is half the sum of two adjacent interval lengths, and an endpoint coefficient is half one interval length. Therefore
\[
\|x-\widetilde y\|_1\le\frac T2\sum_{k=0}^{m+1}|\tau_k-\sigma_k|\le TD.
\]

Define \(\lambda\) to be affine on each \([t_k,t_{k+1}]\), with \(\lambda(t_k)=s_k\) for \(0\le k\le m+1\). It maps \([0,T]\) onto \([0,s_{m+1}]\); it need not map onto \([0,T]\). Each grid interval maps onto the corresponding single interval of the \(s\)-grid, so direct affine substitution proves \(\widetilde y=y\circ\lambda\). Moreover,
\[
\|\lambda-\mathrm{id}\|_\infty=\max_{0\le k\le m+1}|e_k|\le D,
\qquad
\operatorname{TV}(y)=\sum_{k=0}^n|\sigma_{k+1}-\sigma_k|\le2\sum_{k=1}^{n+1}\sigma_k=2T.
\]
For completeness, let \(v_y\) be the total-variation measure of the continuous BV function \(y\), and let \(a=\|\lambda-\mathrm{id}\|_\infty\). Then
\[
|y(\lambda(u))-y(u)|\le v_y([u-a,u+a]\cap[0,T]).
\]
Tonelli's theorem applies to the nonnegative indicator of \(|u-v|\le a\), with Lebesgue measure in \(u\) and the finite measure \(v_y\) in \(v\). It yields
\[
\|y\circ\lambda-y\|_1\le2a\operatorname{TV}(y)\le4TD.
\]
This estimate requires no surjectivity of \(\lambda\). The triangle inequality now gives
\[
d_1(\Phi(\eta),\Phi(\xi))\le5T\,d_N(\eta,\xi).
\]
In particular, \(\Phi\) is continuous and Borel measurable for the stated metrics.

## 2. Exact inversion

For \(x=\Phi(\eta)\), put \(f_x(u)=u-x(u)\). If \(m=0\), then \(x(u)=u\) and \(f_x\equiv0\). If \(m\ge1\), direct evaluation and the affine slopes give
\[
f_x=0\text{ on }[0,t_1],\qquad f_x(t_k)=t_{k-1},\qquad f_x(T)=t_m,
\]
and
\[
f_x'(u)=\frac{\tau_k}{\tau_{k+1}}>0\quad\text{on }(t_k,t_{k+1}),\quad 1\le k\le m.
\]
Thus \(t_1\) is the last zero. Every subsequent event \(t_k\), \(2\le k\le m\), is the unique later hit of the previously recovered level \(t_{k-1}\). After \(t_m\), the level \(t_m\) is reached only at \(T\), not before it.

More precisely, start with the level zero. Record the supremum of its later preterminal level set only if that set is nonempty and its supremum is strictly below \(T\); otherwise stop. Repeat with each recorded time as the next level. For an eventless path the first supremum is \(T\), so nothing is recorded. For a path with events the procedure recovers exactly its finite event list, then stops. This defines \(\Psi\) on \(\Phi(\mathcal N)\) and proves
\[
\Psi\circ\Phi=\mathrm{id}_{\mathcal N},\qquad \Phi\circ\Psi=\mathrm{id}_{\Phi(\mathcal N)}.
\]
Consequently \(\Phi\) is injective and bijective onto its image. Measurability of the inverse is established below by compact restrictions rather than asserted from the hitting-time description.

## 3. Inverse stability on the separated class

Fix \(\delta>0\) and write \(R=T/\delta\). If \(R<1\), the class is empty. If \(1\le R<2\), it contains only the eventless path. The assertion is then vacuous or immediate, with any positive finite constant. Hence assume \(R\ge2\). Every event count is at most \(K=\lfloor R\rfloor-1\).

For a path with at least one event, the preceding slope calculation gives
\[
R^{-1}\le f_x'\le R\quad\text{on }[t_1,T]\text{ piecewise},
\]
whereas \(f_x=0\) on the initial interval. Its restriction to \([t_1,T]\) is a bijection onto \([0,t_m]\), and its inverse \(F_x\) is \(R\)-Lipschitz: summing the lower slope bound between any two points proves this directly. The slope of \(x\) is initially 1 and is subsequently \(1-\tau_k/\tau_{k+1}\), whose absolute value is at most \(R-1\). The eventless embedding has slope 1 and obeys the same bound. Thus, for two embeddings, \(g=x-y\) is \(L=2(R-1)\)-Lipschitz and \(g(0)=0\).

Let \(\epsilon=\|g\|_\infty\). If \(\epsilon>0\), choose \(u_*\) with \(|g(u_*)|=\epsilon\). Since \(g(0)=0\), \(u_*\ge\epsilon/L\). On the interval of length \(\epsilon/(2L)\) immediately to its left, \(|g|\ge\epsilon/2\). Therefore
\[
\epsilon^2\le4L\|g\|_1\le8R\,d_1(x,y).
\]
The same inequality is trivial when \(\epsilon=0\).

First suppose the two paths have the same positive event count \(m\). Set \(a_k=|s_k-t_k|\). If \(s_1\ge t_1\), then
\[
R^{-1}(s_1-t_1)\le f_x(s_1)-f_x(t_1)=f_x(s_1)-f_y(s_1)\le\epsilon.
\]
The other ordering is symmetric, so \(a_1\le R\epsilon\).

For \(\epsilon<\delta\) and \(2\le k\le m\), the following domain checks justify the recursion. We have \(t_k\ge s_1\), since otherwise \(f_y(t_k)=0\) while \(f_x(t_k)=t_{k-1}\ge\delta\), contradicting the sup-norm bound. Also \(|t_m-s_m|\le\epsilon\), by evaluating the backshifts at \(T\), and hence
\[
0\le t_{k-1}\le t_m-\delta<t_m-\epsilon\le s_m.
\]
Thus \(F_y(t_{k-1})\) is defined, and both it and \(t_k=F_x(t_{k-1})\) lie in \([s_1,T]\). The lower slope bound for \(f_y\) gives
\[
|F_y(t_{k-1})-F_x(t_{k-1})|\le R\epsilon.
\]
Using also the Lipschitz bound for \(F_y\),
\[
a_k\le R a_{k-1}+R\epsilon.
\]
Unrolling and summing, using the equal-count distance formula, yields
\[
d_N(\eta,\xi)=\sum_{k=1}^m a_k\le C_m(R)\epsilon,
\qquad C_m(R)=\frac{R^2(R^m-1)}{(R-1)^2}.
\]
For \(\epsilon\ge\delta\), the same conclusion follows from \(d_N\le mT\), because
\[
C_m(R)\delta=\frac{R(R^m-1)}{(R-1)^2}T\ge mT.
\]
Here \((R^m-1)/(R-1)=\sum_{j=0}^{m-1}R^j\ge m\) and \(R/(R-1)\ge1\). Thus the equal-count estimate holds in both perturbation regimes. Combining with the sup-norm estimate gives
\[
d_N(\eta,\xi)\le\sqrt{8R}\,C_m(R)\,d_1(x,y)^{1/2}.
\]
For \(m=0\), both paths are identical, and no rational formula for \(C_0\) is needed.

For different event counts, let \(\mathcal N_\delta^{(m)}\) denote the class with exactly \(m\) events. Its event-time vectors form the compact polytope
\[
\{(t_1,\ldots,t_m):t_k-t_{k-1}\ge\delta,\ T-t_m\ge\delta\},\qquad t_0=0.
\]
The zero-count class is a singleton. On each such class \(d_N\) is exactly the vector \(\ell^1\) metric. Forward continuity makes its image under \(\Phi\) compact in \(d_1\); injectivity makes distinct-count images disjoint. The distance function attains a strictly positive minimum on the product of any two such compact images. There are finitely many classes, with indices \(0,\ldots,K\), and at least two because \(R\ge2\). Consequently the minimum \(\rho\) of their pairwise distances is positive and depends only on \(\delta,T\).

For different counts, \(d_1(x,y)\ge\rho\) and the padded distance formula gives \(d_N\le KT\). Hence
\[
d_N(\eta,\xi)\le\frac{KT}{\sqrt\rho}\,d_1(x,y)^{1/2}.
\]
Taking the maximum of this constant and the finitely many same-count constants proves the required bound, with dependence only on \(\delta,T\).

## 4. Measurability, signature moments, and law separation

### Compact measurable recovery

For integers \(j\ge1\) and \(0\le m\le j-1\), put \(K_{j,m}=\mathcal N_{T/j}^{(m)}\). These are compact subsets of \((\mathcal N,d_N)\) by the preceding polytope argument, and they cover \(\mathcal N\): every finite augmented grid has a strictly positive minimum gap. A continuous injective map from a compact space into a Hausdorff space has a continuous inverse on its image, because images of closed subsets are compact and therefore closed. Applying this to \(\Phi|_{K_{j,m}}\), each image is compact, the full image is a countable union of closed sets, and the inverse is Borel measurable. Explicitly, for an open subset \(U\) of \(\mathcal N\), each \(\Phi(U\cap K_{j,m})\) is relatively open in the compact image \(\Phi(K_{j,m})\), hence Borel; their countable union is \(\Phi(U)\). The same statements hold after adding the fixed time coordinate. This justifies transferring equality or inequality of laws through the embedding.

### Signature measurability and integrability

All nodal values of an embedding lie in \([0,T]\), so \(0\le x(u)\le T\), and Section 1 gives \(\operatorname{TV}(x)\le2T\). For \(X(u)=(u,x(u))\), the positive nonatomic measure
\[
v(du)=du+|dx|(du)
\]
has total mass at most \(3T\). Summing the absolute values of all degree-\(k\) coordinate integrals and dominating their signed measures by the coordinate variation measures gives
\[
\|S^k(X)\|_2\le\sum_{w\in\{1,2\}^k}|S_w(X)|
\le\int_{u_1<\cdots<u_k}v(du_1)\cdots v(du_k)
=\frac{v([0,T])^k}{k!}\le\frac{(3T)^k}{k!}.
\]
The simplex equality follows by permutation symmetry and the fact that coincident-time sets have zero product measure.

Each finite signature level is Borel measurable in \(\eta\). Indeed, on a fixed-count class the increment of the augmented path over its \(i\)-th linear segment is \(\Delta X_i=(t_{i+1}-t_i,\tau_{i+1}-\tau_i)\). Partitioning an ordered integration simplex according to the segments containing its variables gives
\[
S^k(X)=\sum_{r_0+\cdots+r_m=k}
\frac{\Delta X_0^{\otimes r_0}}{r_0!}\otimes\cdots\otimes
\frac{\Delta X_m^{\otimes r_m}}{r_m!}.
\]
This is continuous in the event-time vector. Therefore it is continuous on each \(K_{j,m}\), and Borel on their countable closed cover.

Consequently all the signature expectations in the task exist. In fact, for every probability law on \(\mathcal N\) and every \(r>0\),
\[
\sum_{k=0}^\infty r^k\|\mathbb E S^k(X)\|_2\le e^{3Tr}.
\]
Thus the source's signature convergence conditions are satisfied automatically in this particular representation. The source's separate finite-first-\(d_N\)-moment restriction remains part of the public law domain; it has not been replaced by a finite expected event-count assumption.

### The required determinacy statement, derived

For \(k\ge0\), define the scalar functional
\[
A_k(x)=\int_0^T(T-u)^k x(u)\,du.
\]
Use coordinate 1 for time and coordinate 2 for the scalar path. Integrating the time letters after the first integration variable, then using integration by parts and \(x(0)=0\), gives
\[
S_{2\,1^{k+1}}(X)=\frac1{(k+1)!}\int_0^T(T-u)^{k+1}\,dx(u)
=\frac1{k!}A_k(x).
\]
Both endpoint terms in integration by parts vanish. Moreover,
\[
0\le A_k(x)\le\frac{T^{k+2}}{k+1}.
\]

For any two words, the product of their signature coordinate integrals is the sum of the coordinate integrals obtained by interleaving the words while preserving each word's internal order, counting multiplicities. To verify this identity, apply Fubini to the product of the two finite signed integration measures and partition the product of their ordered simplices according to the ordering of all variables together. Coincident-time sets have zero variation-product measure, since all coordinate variation measures are nonatomic. Repeating the argument proves the corresponding identity for any finite product. It follows that equality of all expected signature coordinates implies equality of all mixed moments of every finite vector \((A_0,\ldots,A_q)\).

Here these bounded mixed moments determine the vector law. A direct justification avoids invoking a specialized determinacy theorem. Rescale its coordinates to \([0,1]\). For a continuous function \(F\) on \([0,1]^d\), the polynomial
\[
B_nF(z)=\sum_{i_1,\ldots,i_d=0}^n F(i_1/n,\ldots,i_d/n)
\prod_{a=1}^d\binom n{i_a}z_a^{i_a}(1-z_a)^{n-i_a}
\]
converges uniformly to \(F\). Indeed, it equals \(\mathbb E F(J_1/n,\ldots,J_d/n)\) for independent binomial variables with parameters \((n,z_a)\). Each normalized variance is at most \(1/(4n)\); Chebyshev's inequality and a union bound give a uniform probability bound \(d/(4nb^2)\) for a coordinate deviation greater than \(b>0\). Uniform continuity of \(F\), followed by this bound, proves uniform convergence. Equality of mixed moments therefore gives equality of integrals of every continuous \(F\). These integrals determine a probability measure on the compact cube: for each closed set \(C\), the continuous functions \(\max(0,1-n\operatorname{dist}(z,C))\) decrease to its indicator, and closed sets form a generating intersection-closed family. Bounded convergence and the finite-measure uniqueness argument give equality of the Borel measures.

Thus equality of expected signatures gives equality of every finite-dimensional distribution of the countable vector
\[
A(x)=(A_0(x),A_1(x),\ldots).
\]
Its law on \(\mathbb R^{\mathbb N_0}\) is determined by these distributions, since finite-coordinate cylinders form a generating intersection-closed family for the product Borel sigma-algebra.

It remains to check that this vector recovers the original law. If \(A(x)=A(y)\), then \(\int_0^T p(u)(x(u)-y(u))\,du=0\) for every polynomial \(p\), because powers of \(T-u\) span the polynomials. The one-dimensional approximation just proved, after rescaling the interval, supplies polynomials converging uniformly to the continuous function \(x-y\). Passing to the limit yields \(\int_0^T(x-y)^2=0\), and continuity gives \(x=y\). By Section 2, \(\eta\mapsto A(\Phi(\eta))\) is therefore injective.

Each coordinate of this map is continuous for \(d_N\), since
\[
|A_k(x)-A_k(y)|\le T^k d_1(x,y).
\]
It is consequently continuous into the product space. On every compact \(K_{j,m}\), it is a homeomorphism onto a compact image. The same countable-compact argument used for \(\Phi\) proves that its full image is Borel and its inverse is Borel measurable. Hence equality of the countable-vector laws implies equality of the original Borel counting-path laws.

We have proved directly that equality of all expected signatures of the augmented embeddings forces \(P=Q\). No general external determinacy or tree-like-uniqueness theorem remains an unclosed obligation. Therefore, if admissible \(P\ne Q\), some finite-degree signature coordinate has different expectations, and the corresponding finite truncation has strictly positive Euclidean discrepancy.

Finally, for a fixed nonnegative integer \(M\), the discrepancy is the Euclidean distance between two finite expected feature vectors. It is finite, nonnegative, symmetric, zero on the diagonal, and satisfies the triangle inequality. Thus it is a pseudometric, including the identically zero case \(M=0\).
