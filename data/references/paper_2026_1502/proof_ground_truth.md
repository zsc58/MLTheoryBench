# Reference Proof

## Obligations and proof structure

We establish dual attainment and the certificate pairing for each existing minimizer, localize its support, derive the correct binary-activation formula on each relative stratum, characterize saturation points by a local extremum argument, and prove the requested cardinality bound. The counting argument does not assume general position or infer a maximum of layer counts from their union.

## 1. Dual optimizers and certificate pairing

Write
\[
\phi(w)=\bigl(\sigma(\langle w,x^1\rangle),\ldots,\sigma(\langle w,x^n\rangle)\bigr).
\]
This is continuous on the compact sphere. The adjoint identity follows by interchanging a finite sum and an integral:
\[
\langle p,K\nu\rangle=\int K_*p\,d\nu.
\]

For completeness, interpolation dual attainment can be established in finite dimensions. Let
\[
C=\operatorname{conv}\{\phi(w),-\phi(w):w\in S^{d-1}\},\qquad V=\operatorname{span}C.
\]
The convex hull is compact: an affine-dependence elimination reduces every convex combination to at most \(n+1\) terms, so this hull is the image of a compact set of points and simplex weights. Moreover,
\[
C=\{K\nu:\|\nu\|_{\rm TV}\le1\}.
\]
Indeed, finite convex combinations give signed atomic measures of TV at most one; conversely, integrating the polar decomposition of a signed measure gives a limit of such convex combinations, with any unused mass assigned to \(0\in C\). Compactness closes the hull. Since \(C\) is symmetric and spans \(V\), it contains a neighborhood of zero relative to \(V\): choose a basis from \(C\) and use the convex hull of its positive and negative vectors.

Let \(\mu\) be an interpolation minimizer. If \(y_0=0\), then \(\mu=0\), and \(p=0\) is a dual optimizer. Otherwise put \(t=\|\mu\|_{\rm TV}>0\) and \(z=y_0/t\). The point \(z\) belongs to the relative boundary of \(C\); otherwise a slightly larger positive multiple of \(z\) would still belong to \(C\), giving an interpolating measure of TV less than \(t\).

Here is an explicit supporting-functional argument. For \(\varepsilon>0\), the point \((1+\varepsilon)z\) is outside \(C\), by minimality of \(t\). Choose a nearest point \(q_\varepsilon\in C\) and set
\[
h_\varepsilon=\frac{(1+\varepsilon)z-q_\varepsilon}{\|(1+\varepsilon)z-q_\varepsilon\|_2}.
\]
Differentiating squared distance along segments in \(C\) gives
\(\langle h_\varepsilon,c-q_\varepsilon\rangle\le0\) for all \(c\in C\). Also \(q_\varepsilon\to z\). Passing to a subsequence of the unit vectors in \(V\) gives a unit vector \(h\in V\) with
\[
\langle h,c\rangle\le\langle h,z\rangle=:a\qquad(c\in C).
\]
The neighborhood of zero contained in \(C\) implies \(a>0\). Thus \(p=h/a\), viewed as a vector in \(\mathbb R^n\), satisfies \(\|K_*p\|_\infty\le1\) and
\[
\langle y_0,p\rangle=t=\|\mu\|_{\rm TV}.
\]
For any feasible interpolation measure \(\nu\) and any feasible dual vector \(q\),
\(\langle y_0,q\rangle=\int K_*q\,d\nu\le\|\nu\|_{\rm TV}\). Consequently \(p\) is a dual optimizer. No uniqueness of this optimizer is asserted.

Now let \(\mu\) be a regularized minimizer and put
\[
p=\frac{y_\zeta-K\mu}{\lambda}.
\]
For any finite signed measure \(\nu\), apply minimality to \((1-s)\mu+s\nu\), use convexity of TV, divide by \(s>0\), and let \(s\downarrow0\). This yields
\[
\|\nu\|_{\rm TV}\ge\|\mu\|_{\rm TV}+\langle p,K\nu-K\mu\rangle.
\]
Taking \(\nu=0\) and \(\nu=2\mu\) gives
\(\langle p,K\mu\rangle=\|\mu\|_{\rm TV}\). The remaining inequality becomes \(\langle p,K\nu\rangle\le\|\nu\|_{\rm TV}\); taking \(\nu=\pm\delta_w\) proves dual feasibility.

The displayed regularized dual is scaled relative to the primal. The exact identity, for any dual-feasible \(q\), is
\[
\begin{aligned}
&\frac12\|K\nu-y_\zeta\|_2^2+\lambda\|\nu\|_{\rm TV}
-\lambda\left(\langle y_\zeta,q\rangle-\frac\lambda2\|q\|_2^2\right)\\
&\quad=\frac12\|K\nu-y_\zeta+\lambda q\|_2^2
+\lambda\bigl(\|\nu\|_{\rm TV}-\langle q,K\nu\rangle\bigr)\ge0.
\end{aligned}
\]
For \((\nu,q)=(\mu,p)\) equality holds. Hence \(p\) is a dual optimizer. Strict concavity of the dual objective on its convex feasible set makes this regularized optimizer unique.

For either problem, we have therefore obtained a continuous function \(\eta=K_*p\) with
\[
\|\eta\|_\infty\le1,\qquad \int\eta\,d\mu=\|\mu\|_{\rm TV}.
\]
Writing \(d\mu=h\,d|\mu|\), where \(h\in\{-1,1\}\) almost everywhere, gives
\(\int(1-\eta h)\,d|\mu|=0\). The integrand is nonnegative. Thus \(\eta=h\) almost everywhere with respect to \(|\mu|\), and continuity implies
\[
\operatorname{supp}\mu\subseteq E:=\{w:|\eta(w)|=1\}.
\]

## 2. Relative strata and atom locations

Every point of the sphere belongs to exactly one stratum \(S_{J,\pi}\), where \(J\) consists of its nonzero inner-product indices and \(\pi_i\in\{0,1\}\) records positivity. Define
\[
z_{J,\pi}=\operatorname{Proj}_{L_J}\left(\sum_{i\in J}p_i\pi_i x^i\right).
\]
On this stratum and its relative closure,
\[
\eta(w)=\sum_{i\in J}p_i\pi_i\langle w,x^i\rangle=\langle z_{J,\pi},w\rangle.
\]
This identity is not asserted on the rest of \(L_J\).

Suppose \(w_0\in S_{J,\pi}\) and \(|\eta(w_0)|=1\). For every \(v\in L_J\) with \(\langle v,w_0\rangle=0\), the curve
\[
w(t)=\frac{w_0+t v}{\|w_0+t v\|_2}
\]
remains in the same relative stratum for sufficiently small \(|t|\). Since \(\eta\) is globally bounded between \(-1\) and \(1\), its derivative along this curve vanishes at zero. Hence \(\langle z_{J,\pi},v\rangle=0\) for every such \(v\), and
\[
z_{J,\pi}=\langle z_{J,\pi},w_0\rangle w_0=\eta(w_0)w_0.
\]
This also covers \(\dim L_J=1\); in that case every vector in \(L_J\) is already parallel to \(w_0\). Thus \(z_{J,\pi}\ne0\), \(\|z_{J,\pi}\|_2=1\), and
\[
w_0=\operatorname{sgn}(\eta(w_0))\frac{z_{J,\pi}}{\|z_{J,\pi}\|_2}.
\]

On the stratum closure, Cauchy-Schwarz now shows that another unit-level point could only be \(-w_0\). But saturation entails a nonzero active ReLU term, so at least one index with \(\pi_i=1\) has \(\langle w_0,x^i\rangle>0\). Its opposite violates the corresponding weak sign inequality. Therefore the stratum closure has no other saturation point. If \(J=\varnothing\), the certificate is zero on the stratum and no saturation is possible.

There are at most \(3^n\) ternary sign patterns, so \(E\) is finite. Support localization already proves that \(\mu\) is a finite signed sum of Dirac masses, with the asserted locations. For \(\mu=0\), use the empty sum.

## 3. The geometric bound

We prove the requested bound without the source's invalid maximum-over-layers inference.

Partition the coefficient indices into
\[
I_+=\{i:p_i>0\},\qquad I_-=\{i:p_i<0\},\qquad a=|I_+|,\quad b=|I_-|.
\]
Suppose first that \(a>0\). On the closure \(C_+\) of any full-dimensional region formed by the hyperplanes indexed by \(I_+\), the function
\(A(w)=\sum_{i\in I_+}p_i\sigma(\langle w,x^i\rangle)\)
is linear. The function
\(D(w)=\sum_{i\in I_-}(-p_i)\sigma(\langle w,x^i\rangle)\)
is subadditive, directly from \(\sigma(s+t)\le\sigma(s)+\sigma(t)\). Hence, on this closed cone,
\[
\eta(u+v)=A(u+v)-D(u+v)\ge\eta(u)+\eta(v).
\]
The positively homogeneous extension of the certificate satisfies \(|\eta(v)|\le\|v\|_2\) for every \(v\in\mathbb R^d\). If distinct unit vectors \(u,v\in C_+\) both had certificate value one, we would obtain
\[
2\le\eta(u+v)\le\|u+v\|_2<2,
\]
a contradiction. Thus each such closed region contains at most one positive saturation point. Their closures cover the sphere, including all boundaries, so the number of positive saturation points is at most \(\Xi(a,d)\). If \(a=0\), there are no positive saturation points. Applying the same argument to \(-\eta\) bounds negative saturation points by \(\Xi(b,d)\) when \(b>0\), and by zero otherwise.

For \(d=1\), the sphere has exactly two points and \(\Xi(n,1)=2\), which proves the desired bound immediately. Suppose \(d\ge2\). The elementary central-arrangement formula is
\[
\Xi(m,d)=2\sum_{j=0}^{d-1}\binom{m-1}{j},\qquad m\ge1,
\]
with binomial coefficients outside their range interpreted as zero. To recall its justification, adding a hyperplane creates at most as many new regions as the preceding hyperplanes induce within it. For \(m,d\ge2\), this gives the deletion/restriction recurrence with the two smaller counts. The initial counts for one hyperplane and for dimension one are both two. Induction gives the displayed upper bound by Pascal's identity; central arrangements in general position attain the recurrence and therefore the bound. Such positions can be obtained by choosing normals successively outside the finitely many forbidden linear subspaces. No general-position assumption is made about the actual data.

If \(a,b\ge1\), this formula gives
\[
\Xi(a,d)+\Xi(b,d)\le\Xi(a+b,d).
\]
Indeed, partition a set of \(a+b-1\) elements into blocks of sizes \(a-1\), \(b-1\), and one. For every \(j\ge1\), its \(j\)-element subsets include those lying wholly in either of the first two blocks. At \(j=1\) there is one extra singleton, exactly compensating for the extra constant term on the left. This proves the inequality after summing through \(d-1\). If just one coefficient group is nonempty, only its region count contributes. If both are empty, \(E\) is empty. By monotonicity of the region formula, all cases give
\[
|E|\le\Xi(n,d)\le\max_{0\le k\le n}\binom nk\Xi(n-k,d-k)=B(n,d).
\]
The last inequality uses the \(k=0\) term. Thus every minimizer has at most \(B(n,d)\) atoms. This proof is valid for repeated hyperplanes, dependent normals, and vanishing dual coordinates.

For the corrected private source statement about nonzero absolute maxima, apply the same argument to \(\eta/\|\eta\|_\infty\). If \(\eta=0\), its unit level set is empty, while its absolute-maximum set is the whole sphere.

## 4. Consequences and edge cases

There are at most \(2^m\) strict sign patterns for \(m\) hyperplanes. This and the stated zero-dimensional conventions give
\[
B(n,d)\le\max_k\binom nk2^{n-k}\le\sum_{k=0}^n\binom nk2^{n-k}=3^n.
\]
For fixed \(d\) and \(n>d\), terms with \(k>d\) vanish, and the \(k=d\) term also vanishes because \(n-d>0\) and \(\Xi(n-d,0)=0\). For \(0\le k<d\), the central-region formula gives, for a constant depending only on \(d\),
\[
\Xi(n-k,d-k)\le C_d(n-k)^{d-k},\qquad \binom nk\le n^k.
\]
Therefore \(B(n,d)\le C_d n^d\), and the required atom bound is uniform over the data, labels, and regularization parameter.

If interpolation is infeasible there is no interpolation minimizer to which the assertion applies. Zero labels and zero minimizers are covered without a nonzero-certificate assumption. All divisions in the atom formula concern actual atoms and have nonzero denominators by Section 2. The interpolation and regularized arguments use their own dual optimizers and do not identify them.
