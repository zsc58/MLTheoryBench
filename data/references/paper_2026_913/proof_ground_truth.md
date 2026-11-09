# Reference Proof

## Proof Structure

The quadratic objective is concave under the stated conditional negative semidefiniteness condition. Extreme couplings are exactly those whose bipartite support graph is acyclic. A terminating cycle-splitting construction expresses every coupling as a finite convex combination of extreme couplings, so concavity supplies an extreme minimizer. Its acyclic support gives the support bound. With equal uniform marginals, the acyclic-support characterization forces every extreme coupling to be a scaled permutation matrix, yielding the final equality.

## Complete Proof

Let
\[
f(A)=\langle K\otimes A,A\rangle,
\qquad A\in\mathbb R^{n\times m}.
\]
The matrix \(\gamma^0=\mu\nu^\top\) belongs to \(\Gamma(\mu,\nu)\), since its row sums are \(\mu\) and its column sums are \(\nu\). Thus the feasible set is nonempty, even when some marginal entries vanish. It is closed, and every feasible entry lies in \([0,1]\), so it is compact. It is also convex. The function \(f\) is a polynomial with finite real coefficients, hence continuous. Therefore a minimizer \(\gamma^*\) exists.

For \(\gamma_1,\gamma_2\in\Gamma(\mu,\nu)\) and \(t\in[0,1]\), symmetry of \(K\) gives
\[
f(t\gamma_1+(1-t)\gamma_2)
=t f(\gamma_1)+(1-t)f(\gamma_2)
-t(1-t)\langle K\otimes(\gamma_1-\gamma_2),\gamma_1-\gamma_2\rangle.
\]
The stated assumption makes the last quadratic form nonpositive. Consequently,
\[
f(t\gamma_1+(1-t)\gamma_2)\ge t f(\gamma_1)+(1-t)f(\gamma_2),
\]
so \(f\) is concave on \(\Gamma(\mu,\nu)\).

We next characterize extreme couplings. Associate to a coupling \(\gamma\) the finite bipartite graph whose vertices are the disjoint row and column vertex sets and whose edges are the pairs in \(\operatorname{supp}(\gamma)\). An extreme coupling is one that cannot be expressed as \(t\gamma_1+(1-t)\gamma_2\) with distinct feasible couplings and \(0<t<1\).

If the support graph contains a cycle, take a simple cycle. Because the graph is bipartite, the cycle has even length. Assign alternating signs \(+1,-1\) to its edges and zero elsewhere, obtaining a nonzero matrix \(H\in\mathbb R^{n\times m}\). Each cycle vertex is incident to one edge of each sign, so
\[
H\mathbf 1_m=0,
\qquad H^\top\mathbf 1_n=0.
\]
Choose
\[
0<\varepsilon<\min_{(i,j)\text{ on the cycle}}\gamma_{ij}.
\]
Then \(\gamma+\varepsilon H\) and \(\gamma-\varepsilon H\) are nonnegative, have the same marginals as \(\gamma\), and are distinct. Their midpoint is \(\gamma\), so \(\gamma\) is not extreme.

Conversely, suppose \(\gamma\) is not extreme. Write
\[
\gamma=t\gamma_1+(1-t)\gamma_2,
\qquad 0<t<1,
\]
with distinct feasible couplings, and put \(H=\gamma_1-\gamma_2\ne0\). This matrix has zero row and column sums. If \(\gamma_{ij}=0\), nonnegativity and the strictly positive mixture coefficients force \((\gamma_1)_{ij}=(\gamma_2)_{ij}=0\). Hence every nonzero entry of \(H\) lies in \(\operatorname{supp}(\gamma)\).

Consider the graph of the nonzero entries of \(H\). Every vertex incident to an edge has degree at least two: otherwise its row or column sum would equal a single nonzero entry and could not vanish. Starting along any edge, continue at each vertex along an edge different from the one just traversed. This produces a nonbacktracking walk that cannot terminate. Since the graph is finite, some vertex repeats. Stop at the first repetition; the segment between its two occurrences is a simple cycle. It is not a two-edge immediate reversal because the walk is nonbacktracking. All its edges belong to \(\operatorname{supp}(\gamma)\). Thus a non-extreme coupling has a support cycle. Together with the preceding perturbation argument, this proves that a coupling is extreme if and only if its support graph is acyclic. Isolated vertices caused by zero marginal entries cause no difficulty.

We now derive the finite extreme-point decomposition rather than leave it as an unproved internal dependency. Proceed by induction on the number of positive entries of a coupling \(\gamma\). If its support is acyclic, it is already extreme. Otherwise, choose a simple support cycle and its alternating matrix \(H\). Let
\[
a=\min_{H_{ij}=-1}\gamma_{ij}>0,
\qquad
b=\min_{H_{ij}=+1}\gamma_{ij}>0,
\]
and define
\[
\gamma^+=\gamma+aH,
\qquad
\gamma^-=\gamma-bH,
\qquad
\lambda=\frac{b}{a+b}.
\]
Both perturbed matrices are feasible. In \(\gamma^+\), only entries with \(H_{ij}=-1\) decrease, and the choice of \(a\) keeps them nonnegative and makes at least one zero. The corresponding statement holds for \(\gamma^-\) and \(b\). No entry outside the original support becomes positive. Thus each perturbed coupling has strictly fewer positive entries than \(\gamma\). Moreover,
\[
\lambda\gamma^++(1-\lambda)\gamma^-=
\gamma+\bigl(\lambda a-(1-\lambda)b\bigr)H=
\gamma.
\]
Apply the induction hypothesis to \(\gamma^+\) and \(\gamma^-\), then combine their decompositions. The support count strictly decreases at every recursive step, so the construction terminates after finitely many steps. It expresses every coupling as a finite convex combination of extreme couplings.

Apply this result to the minimizer already obtained:
\[
\gamma^*=\sum_r\lambda_r e_r,
\qquad
\lambda_r\ge0,
\qquad
\sum_r\lambda_r=1,
\]
where each \(e_r\) is extreme. Repeated application of the two-point concavity inequality gives
\[
f(\gamma^*)\ge\sum_r\lambda_r f(e_r).
\]
Every \(e_r\) is feasible, so \(f(e_r)\ge f(\gamma^*)\). The two inequalities force equality for every term with positive weight. In particular, some extreme coupling is also minimizing.

An acyclic graph on the \(n+m\) row and column vertices has at most \(n+m-1\) edges. Indeed, start with \(n+m\) isolated vertices and add its edges. Each added edge joins two different components; otherwise it would create a cycle. Thus each edge decreases the number of components by one, and at least one component remains. Applying this to the extreme minimizer proves
\[
|\operatorname{supp}(\gamma)|\le n+m-1.
\]
This argument includes isolated vertices and the cases \(n=1\) or \(m=1\).

Now suppose \(n=m\) and \(\mu=\nu=(1/n)\mathbf 1_n\). Every row and column of a coupling has total mass \(1/n>0\). Let \(\gamma\) be extreme. Its support graph is acyclic, and every vertex has positive degree. Each component is therefore a finite tree with at least one edge. Choose a leaf in a component. Its unique incident edge has mass \(1/n\). The adjacent vertex also has total incident mass \(1/n\), so it cannot have any other positive incident edge. Both endpoints consequently have degree one, and their edge forms the entire component. Hence every component consists of a single edge. The support is a perfect matching, and \(\gamma\) is \((1/n)\) times a permutation matrix. Conversely, every such scaled permutation is feasible and has a matching, hence acyclic, support, so it is extreme. The same argument applies when \(n=1\).

The minimizing extreme coupling is therefore a scaled permutation. Since scaled permutation couplings are a subset of \(\Gamma(\mu,\nu)\), and one of them attains the global minimum,
\[
\mathsf{GW}(K,\mu,\nu)
=\min_{\gamma\in\Gamma(\mu,\nu)}f(\gamma)
=\min_{\gamma\in\mathsf{Perm}_n}f(\gamma).
\]

## Proof-Obligation Audit

All theorem-critical obligations are closed: nonemptiness and compactness of the feasible set; continuity and attainment; CND-induced concavity; both directions of the acyclic-support characterization; finite extreme-point decomposition with termination; attainment at an extreme coupling; the forest edge bound; the scaled-permutation characterization under equal uniform marginals; and equality of the two minima. Each is derived above. No paper-specific theorem or specialized external method is left as an unresolved proof dependency.
