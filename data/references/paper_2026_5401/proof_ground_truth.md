# Reference Proof

## Proof Structure

Project each positive-semidefinite matrix onto its observed entries. The weighted loss becomes a strictly convex function on the convex set of attainable projections, so all loss minimizers have the same observed-entry vector. The inner minimizing set is therefore exactly a covariance-completion set. A direct maximum-determinant argument then gives a unique positive-definite outer optimizer, and first-order perturbations of its unspecified entries force the corresponding inverse entries to vanish.

## Complete Proof

Let
\[
P_E(X)=(X_{ij})_{(i,j)\in E},\qquad
F(z)=\sum_{(i,j)\in E}\frac{(z_{ij}-b_{ij})^2}{2v_{ij}},
\]
and let
\[
\mathcal Z=P_E(\mathbb S_+^n).
\]
The set \(\mathcal Z\) is convex because it is the linear image of the convex cone \(\mathbb S_+^n\). Moreover,
\[
\ell(X)=F(P_E(X)).
\]
Since every \(v_{ij}>0\), the Hessian of \(F\) is diagonal with strictly positive diagonal entries. Thus \(F\) is strictly convex.

By assumption, \(\mathcal M\) contains a positive-definite matrix and hence is nonempty. Therefore \(F\) attains its minimum over \(\mathcal Z\). Strict convexity on the convex set \(\mathcal Z\) implies that the minimizing vector is unique; denote it by \(a=(a_{ij})_{(i,j)\in E}\). Indeed, two distinct minimizing vectors would have a midpoint in \(\mathcal Z\) at which strict convexity gives a smaller value.

It follows directly that
\[
\mathcal M
 =\{X\in\mathbb S_+^n:P_E(X)=a\}
 =\{X\in\mathbb S_+^n:X_{ij}=a_{ij}\text{ for all }(i,j)\in E\}.
\]
Thus the outer problem is a positive-semidefinite completion problem with the entries indexed by \(E\) fixed. The assumed positive-definite member of \(\mathcal M\) is a positive-definite completion of these entries.

We now establish existence and uniqueness of the maximum-log-determinant completion. Because all diagonal indices belong to \(E\), every \(X\in\mathcal M\) has the same diagonal \(X_{ii}=a_{ii}\). Positive semidefiniteness gives
\[
|X_{ij}|^2\le X_{ii}X_{jj}=a_{ii}a_{jj},
\]
so \(\mathcal M\) is bounded. It is also closed, being the intersection of the closed positive-semidefinite cone with affine equality constraints. Hence it is compact.

The determinant therefore attains a maximum on \(\mathcal M\). A positive-definite feasible matrix has positive determinant, whereas every singular feasible matrix has determinant zero. Consequently every determinant maximizer is positive definite and also maximizes \(\log\det X\). The function \(\log\det\) is strictly concave on the positive-definite cone. Since \(\mathcal M\) is convex, two distinct maximizers would have a feasible positive-definite midpoint with strictly larger log determinant. Hence the outer optimizer \(X^\star\) is unique.

Finally, fix distinct indices \(i,j\) such that neither \((i,j)\) nor \((j,i)\) belongs to \(E\), and put
\[
H=e_i e_j^{\mathsf T}+e_j e_i^{\mathsf T}.
\]
This perturbation changes no prescribed entry. Since \(X^\star\succ0\), both \(X^\star+tH\) and \(X^\star-tH\) remain positive definite for all sufficiently small positive \(t\), and they remain in \(\mathcal M\). Thus \(t=0\) is an interior maximum of
\(t\mapsto\log\det(X^\star+tH)\), so
\[
0=\left.\frac{d}{dt}\log\det(X^\star+tH)\right|_{t=0}
 =\operatorname{tr}((X^\star)^{-1}H)
 =2Q^\star_{ij}.
\]
Therefore \(Q^\star_{ij}=0\) for every unspecified off-diagonal pair, as claimed.
