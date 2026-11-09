# Reference Proof

## Proof Structure

Identify the critical points and Morse indices, determine the sublevel homotopy types including critical levels, verify the inclusion-induced homology maps, and read off the persistence intervals. The finite lengths telescope.

## Complete Proof

Write \(\mathbb F\) for the fixed coefficient field and use ordinary homology. Coordinates throughout are in the given orthonormal eigenbasis, so
\[
f(x)=\sum_{i=1}^n\lambda_i x_i^2,
\qquad \sum_{i=1}^n x_i^2=1.
\]

### step_001: Critical points and indices

A constrained critical point satisfies \(Mx=\mu x\). Because the eigenvalues are distinct, the critical points are precisely \(\pm e_i\), and their critical values are \(\lambda_i\). For a tangent vector \(v\perp e_i\), the restricted Hessian is
\[
\operatorname{Hess}_{S^{n-1}}f(v,v)
=2\sum_{j\ne i}(\lambda_j-\lambda_i)v_j^2.
\]
The same formula holds at \(-e_i\). The Hessian is nondegenerate, with exactly \(i-1\) negative eigenvalues. Thus both points at level \(\lambda_i\) have Morse index \(i-1\).

### step_002: Morse-theoretic context

The standard Morse facts relevant here are that, for a smooth function on a compact manifold, inclusions between sublevels separated by no critical value are homotopy equivalences, and crossing a level containing nondegenerate critical points attaches one handle of the corresponding index for each critical point. The sphere is compact and smooth, the quadratic form is smooth, and the preceding calculation verifies nondegeneracy and the indices. Thus these facts apply, with two index-\((i-1)\) handles at \(\lambda_i\). Handle counts alone do not determine the persistence maps. We establish both the topology and the maps directly below, so no unspecified attaching-map argument is needed.

### step_003: Sublevels, including critical levels

For \(c<\lambda_1\), the minimum-eigenvalue bound gives \(X_c=\varnothing\). For \(c\ge\lambda_n\), the maximum-eigenvalue bound gives \(X_c=S^{n-1}\).

For \(1\le k\le n-1\), define
\[
E_k=\operatorname{span}(e_1,\ldots,e_k),
\qquad C_k=E_k\cap S^{n-1}.
\]
Fix any \(c\) with \(\lambda_k\le c<\lambda_{k+1}\). Write \(x=y+z\), where \(y\in E_k\) and \(z\in E_k^\perp\), and put \(a=\|y\|\). For every \(x\in X_c\), we have \(a>0\): otherwise \(f(x)\ge\lambda_{k+1}>c\). Also \(C_k\subseteq X_c\), since the Rayleigh quotient on \(E_k\) is at most \(\lambda_k\).

For \(0\le t\le1\), set
\[
H_t(x)=\frac{\sqrt{a^2+t(1-a^2)}}{a}\,y+\sqrt{1-t}\,z.
\]
This formula is continuous on \(X_c\times[0,1]\), including where \(z=0\), and its values have norm one. When \(z\ne0\), let
\[
\alpha=(y/a)^{\mathsf T}M(y/a),
\qquad \beta=(z/\|z\|)^{\mathsf T}M(z/\|z\|).
\]
Then \(\alpha\le\lambda_k<\lambda_{k+1}\le\beta\). Writing \(a_t^2=a^2+t(1-a^2)\), we obtain
\[
f(H_t(x))=a_t^2\alpha+(1-a_t^2)\beta
\le a^2\alpha+(1-a^2)\beta=f(x)\le c.
\]
When \(z=0\), the point is fixed. Consequently \(H_t\) is a strong deformation retraction onto \(C_k\cong S^{k-1}\), with endpoint map \(x\mapsto y/\|y\|\). In particular, this conclusion holds at \(c=\lambda_k\), not only at regular levels.

Set \(C_n=S^{n-1}\). We have therefore proved the complete description
\[
X_c=\varnothing\quad(c<\lambda_1),\qquad
X_c\simeq C_k\cong S^{k-1}\quad(\lambda_k\le c<\lambda_{k+1}),
\qquad X_c=C_n\quad(c\ge\lambda_n).
\]

### step_004: Filtration maps and all intervals

For \(c\ge\lambda_1\), let \(k(c)\) be the number of eigenvalues at most \(c\). The inclusions
\[
i_c:C_{k(c)}\longrightarrow X_c
\]
are homotopy equivalences by step_003, or identities when \(k(c)=n\). If \(\lambda_1\le c\le d\), write \(k=k(c)\), \(\ell=k(d)\), and let \(j_{k\ell}:C_k\hookrightarrow C_\ell\) be the coordinate-sphere inclusion. The inclusions satisfy the exact identity
\[
(X_c\hookrightarrow X_d)\circ i_c=i_d\circ j_{k\ell}.
\]
Since the maps induced by \(i_c\) and \(i_d\) on homology are isomorphisms, this identifies every persistence map with the map induced by \(j_{k\ell}\). In particular, all maps within one half-open spectral range are isomorphisms, including maps starting at its left endpoint.

The homology groups used here are elementary: \(H_0(S^0;\mathbb F)=\mathbb F^2\), with no positive-degree homology; for \(m\ge1\), \(H_0(S^m;\mathbb F)=\mathbb F\), \(H_m(S^m;\mathbb F)=\mathbb F\), and all other positive-degree groups vanish. For example, these follow from the CW structure with one zero-cell and one m-cell for \(m\ge1\); its cellular differentials vanish, including for the circle because the two ends of its one-cell meet the same zero-cell.

Suppose first that \(n\ge2\). On \(C_1=\{e_1,-e_1\}\), let \(p\) and \(q\) be the two point classes in \(H_0\). For every \(\ell\ge2\), \(C_\ell\) is path connected, so its inclusion map sends both \(p\) and \(q\) to the same nonzero component generator. The basis \(p,q-p\), valid over every field, therefore exhibits one component class persisting forever and one disappearing at \(\lambda_2\). All later degree-zero maps are isomorphisms. The degree-zero intervals are precisely
\[
[\lambda_1,\infty),\qquad [\lambda_1,\lambda_2).
\]

For each positive degree \(r\) with \(1\le r\le n-2\), homology is one-dimensional exactly when \(k(c)=r+1\), namely on
\[
\lambda_{r+1}\le c<\lambda_{r+2}.
\]
The maps within that range are isomorphisms, and the groups outside that range vanish. Thus this degree contributes exactly \([\lambda_{r+1},\lambda_{r+2})\). In degree \(n-1\), homology is zero below \(\lambda_n\) and one-dimensional with identity maps from \(\lambda_n\) onward. It contributes \([\lambda_n,\infty)\). This also covers \(n=2\): the positive finite-degree range is empty, while the degree-one class is born at \(\lambda_2\).

For \(n=1\), the sphere is \(S^0\), and \(f\) is constant with value \(\lambda_1\). The filtration is empty below that value and is the same two-point space at every subsequent parameter. Hence it has two copies of \([\lambda_1,\infty)\) in degree zero and no finite intervals, exactly as the target states.

These explicit descriptions of the groups and all their maps give the interval decompositions themselves, not merely the Betti numbers at regular parameters. They also exclude extra intervals or classes supported only at critical levels. Altogether the finite intervals are exactly
\[
[\lambda_k,\lambda_{k+1})\text{ in degree }k-1,
\qquad k=1,\ldots,n-1,
\]
with the two infinite intervals specified in the problem.

### step_005: Total finite persistence

Summing the lengths, with multiplicity, gives
\[
\sum_{k=1}^{n-1}(\lambda_{k+1}-\lambda_k)
=\lambda_n-\lambda_1.
\]
For \(n=1\), the sum is empty and both sides are zero. This proves the total finite persistence claim in every case.
