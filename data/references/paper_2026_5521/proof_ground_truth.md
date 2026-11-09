# Reference Proof

## Proof Obligations

- **step_001:** Construct the induced graph, prove the fibers are nonempty and the graph is regular, and produce exactly $k$ distinct coordinate groups, including $k=2$.
- **step_002:** Prove each isolated-group deterministic optimum is one and establish the lower bound for every randomized orientation.
- **step_003:** Derive the coordinate-counting inequality with constant $2\sqrt n$.
- **step_004:** Deduce the simultaneous low-degree vertex property in every nonempty remaining induced graph.
- **step_005:** Orient edges from earlier to later removals, prove all group bounds, and compare density with the deterministic benchmark.
- **step_006:** Verify the domains of the definitions and handle empty graphs, edgeless graphs, empty families, and the absence of eligible price groups.

Every ingredient needed for these obligations is justified below. The full attainability direction of the external orientation-density theorem is not needed.

## Domains and an Elementary Density Bound

All graphs and coordinate families are finite. A randomized orientation is a distribution on finitely many deterministic orientations, so all degree expectations are finite and depend only on edge-direction marginals. No independence among different edge directions is required.

If $E(G^S)\ne\varnothing$, every deterministic orientation has an edge tail in $G^S$, so $\operatorname{opt}_S(G)\ge1$. Thus every denominator used in the price is positive. Deterministic minima exist because there are finitely many orientations. For a nonempty eligible family, the randomized objective is the maximum of finitely many continuous linear functions of a distribution on those orientations, after division by fixed positive denominators. A minimizing sequence has a convergent subsequence in the finite probability simplex, and its limit attains the minimum.

We will use the following elementary consequence of the density definition. For any nonempty finite graph $H$, any randomized orientation $\Psi$ of $H$, and any nonempty $W\subseteq V(H)$, every internal edge of $H[W]$ contributes exactly one to the sum of the out-degrees over $W$. Edges leaving $W$ contribute nonnegative additional terms. Consequently,
\[
\sum_{v\in W}\mathbb E[\operatorname{outdeg}_{H,\Psi}(v)]\ge |E(H[W])|.
\]
Taking averages over $W$ and then maximizing over $W$ gives
\[
\max_{v\in V(H)}\mathbb E[\operatorname{outdeg}_{H,\Psi}(v)]\ge\rho(H). \tag{A}
\]
For an empty graph the corresponding inequality holds under the stated zero conventions. This proves directly the only direction of the orientation-density result required here.

## Lower Construction: step_001

Fix integers $n,k\ge2$ with $m=\binom{k}{2}\le n$. Label the first $m$ coordinates by the unordered pairs from $[k]$: write $c_{ij}=c_{ji}\in[m]$ for the coordinate corresponding to $\{i,j\}$. Let $\varepsilon_r$ denote the $r$th coordinate vector of $\mathbb F_2^m$, and let $e_i$ denote the $i$th coordinate vector of $\mathbb F_2^k$. Define
\[
\lambda:\mathbb F_2^m\longrightarrow\mathbb F_2^k,
\qquad \lambda(\varepsilon_{c_{ij}})=e_i+e_j.
\]
All additions in this construction are over $\mathbb F_2$. Put
\[
w_1=0,\qquad w_i=e_1+e_i\quad(2\le i\le k).
\]
These vectors are distinct and satisfy $w_i+w_j=e_i+e_j$ for $i\ne j$. Each is in the image of $\lambda$: use the preimage $0$ for $w_1$ and $\varepsilon_{c_{1i}}$ for $w_i$ when $i\ge2$.

Define the nonempty, disjoint fibers
\[
V_i=\{(x,0^{n-m}):x\in\mathbb F_2^m,\ \lambda(x)=w_i\},
\]
and let $G$ be the subgraph of $Q_n$ induced by $V=\bigcup_{i=1}^k V_i$.

If a vertex in $V_i$ is changed in coordinate $c_{ab}$, its image under $\lambda$ changes to $w_i+e_a+e_b$. This equals some $w_j$ only if $j\ne i$ and
\[
e_a+e_b=w_i+w_j=e_i+e_j.
\]
Equality of these two-coordinate supports implies $\{a,b\}=\{i,j\}$. Conversely, changing coordinate $c_{ij}$ sends a vertex of $V_i$ into $V_j$. Changing a padded coordinate leaves $V$ because all padded coordinates are fixed to zero. Therefore every vertex in $V_i$ has precisely one neighbor in each $V_j$ with $j\ne i$, and $G$ is $(k-1)$-regular.

Initially put
\[
S_i^0=\{c_{ij}:j\ne i\}.
\]
For $k\ge3$, take $S_i=S_i^0$. These groups are pairwise distinct: for $i\ne j$, choose $h\notin\{i,j\}$; then $c_{ih}\in S_i^0\setminus S_j^0$.

For $k=2$, one has $m=1$ and $n\ge2$, so the padded coordinate $r=m+1$ is available. Take
\[
S_1=S_1^0,\qquad S_2=S_2^0\cup\{r\}.
\]
These two coordinate groups are distinct. Since $G$ has no edge in a padded coordinate, $G^{S_i}=G^{S_i^0}$ also in this case. Thus the construction produces exactly $k$ distinct groups throughout the frozen parameter range.

## Isolated Optima and the Randomized Lower Bound: step_002

Fix $i$. The graph $G^{S_i}$ contains all edges of $G$ incident with vertices of $V_i$. Each vertex in $V_i$ has $k-1$ such neighbors; every vertex in another fiber $V_j$ has exactly one such neighbor, obtained by changing coordinate $c_{ij}$. Therefore $G^{S_i}$ is a vertex-disjoint union of stars with centers in $V_i$.

Direct the edges of these stars from leaves to centers and extend the orientation arbitrarily to any remaining edges of $G$. The maximum relevant out-degree is at most one. Since the fibers are nonempty and $k\ge2$, $G^{S_i}$ has an edge, so the maximum relevant out-degree in every deterministic orientation is at least one. Hence
\[
\operatorname{opt}_{S_i}(G)=1.
\]

Let $\Phi$ be any randomized orientation of $G$. By (A) and regularity,
\[
\max_{v\in V}\mathbb E[\operatorname{outdeg}_{G,\Phi}(v)]
\ge\rho(G)
\ge\frac{|E(G)|}{|V(G)|}
=\frac{k-1}{2}.
\]
Choose a vertex $v\in V_i$ attaining at least this expected value. This choice concerns the expectations for the fixed distribution $\Phi$, not a vertex selected after realizing the random orientation. All edges incident with $v$ have coordinates in $S_i$, so for every realization,
\[
\operatorname{outdeg}_{G,\Phi}(v)=\operatorname{outdeg}_{G^{S_i},\Phi}(v).
\]
The required lower bound follows. Since all $k$ denominators equal one, maximizing over the groups and vertices and then minimizing over $\Phi$ proves the asserted lower bound on the price.

## Coordinate-Counting Inequality: step_003

Let $H$ be a nonempty induced subgraph of $Q_n$ without isolated vertices. Write $C_H(v)$ for the set of coordinates of edges incident with $v$. For each $v\in V(H)$, choose a nonempty $T(v)\subseteq C_H(v)$ and put
\[
q_v=\rho(H^{T(v)}).
\]
For each coordinate $r\in[n]$, let $m_r$ be the number of $r$-edges in $H$, and let
\[
a_r=|\{v:r\in T(v)\}|.
\]
Every selected occurrence of coordinate $r$ is at an endpoint of an $r$-edge. Such edges form a matching, because a cube vertex has at most one neighbor in each coordinate. Therefore
\[
a_r\le2m_r,
\qquad
\sum_v\deg_{H^{T(v)}}(v)=\sum_{r=1}^n a_r. \tag{B}
\]
Let $N=|V(H)|$, $A=\sum_r a_r$, and $Q=\sum_v q_v$. By Cauchy–Schwarz and (B),
\[
A^2\le n\sum_r a_r^2
\le2n\sum_r m_ra_r
=2n\sum_v\sum_{r\in T(v)}m_r
=2n\sum_v |E(H^{T(v)})|.
\]
Taking the full vertex set in the density definition gives $|E(H^{T(v)})|\le Nq_v$. Thus
\[
A^2\le2nNQ. \tag{C}
\]
Each $T(v)$ contains an incident coordinate. The endpoints of its corresponding edge form a two-vertex induced subgraph with one edge, so $q_v\ge1/2$. Hence $Q\ge N/2$. Substituting $N\le2Q$ into (C) and taking nonnegative square roots yields
\[
\sum_v\deg_{H^{T(v)}}(v)=A\le2\sqrt n\,Q
=2\sqrt n\sum_v\rho(H^{T(v)}). \tag{D}
\]

## A Simultaneously Suitable Vertex: step_004

We claim that every nonempty induced subgraph $H$ of $Q_n$ has a vertex $v$ satisfying
\[
\deg_{H^S}(v)\le2\sqrt n\,\rho(H^S)
\quad\text{for every }S\in\mathcal S. \tag{E}
\]
If $\mathcal S$ is empty, any vertex satisfies this condition. If $H$ has an isolated vertex, that vertex also satisfies it because all its relevant degrees are zero and density is nonnegative.

Otherwise suppose no vertex satisfies (E). For every $v$, choose a violating group $S(v)$, so
\[
\deg_{H^{S(v)}}(v)>2\sqrt n\,\rho(H^{S(v)}).
\]
Set $T(v)=S(v)\cap C_H(v)$. The strict inequality implies positive degree and therefore $T(v)\ne\varnothing$. Moreover,
\[
\deg_{H^{T(v)}}(v)=\deg_{H^{S(v)}}(v).
\]
Deleting edges cannot increase density: for every vertex subset, the numerator in its density ratio can only decrease. Thus
\[
\rho(H^{T(v)})\le\rho(H^{S(v)}).
\]
It follows that each $v$ satisfies
\[
\deg_{H^{T(v)}}(v)>2\sqrt n\,\rho(H^{T(v)}).
\]
Summing these strict inequalities over the nonempty vertex set contradicts (D). This proves (E).

## Common Orientation and Price: step_005

Starting from $G$, repeatedly remove a vertex satisfying (E) in the current induced graph. Let the removal order be $v_1,\ldots,v_N$. For each edge $\{v_t,v_u\}$ with $t<u$, direct it as
\[
v_t\longrightarrow v_u.
\]
Thus every edge is directed **from its earlier-removed endpoint to its later-removed endpoint**.

Fix $v=v_t$ and let $H$ be the induced graph just before its removal. Edges joining $v$ to already removed vertices point into $v$, whereas edges from $v$ to vertices still in $H$ point out of $v$. Consequently, for every $S\in\mathcal S$,
\[
\operatorname{outdeg}_{G^S,\phi}(v)=\deg_{H^S}(v).
\]
By (E), this is at most $2\sqrt n\,\rho(H^S)$. Since $H^S=G^S[V(H)]$, every vertex subset used to compute $\rho(H^S)$ is also available for computing $\rho(G^S)$. Hence
\[
\operatorname{outdeg}_{G^S,\phi}(v)
\le2\sqrt n\,\rho(H^S)
\le2\sqrt n\,\rho(G^S).
\]
This is a single deterministic orientation satisfying all the required inequalities.

For any deterministic orientation $\psi$ of $G$, apply (A) to its restriction to $G^S$ to obtain
\[
\rho(G^S)\le\max_v\operatorname{outdeg}_{G^S,\psi}(v).
\]
Minimizing over $\psi$ gives
\[
\rho(G^S)\le\operatorname{opt}_S(G).
\]
For each eligible group the denominator is positive. Dividing the common orientation's bound by this denominator gives a ratio at most $2\sqrt n$. The point mass on this deterministic orientation is an admissible randomized orientation, so the minimum defining the price is also at most $2\sqrt n$.

## Degenerate Cases: step_006

If $V(G)=\varnothing$, there is a unique empty orientation, the vertex inequalities are vacuous, and the density and deterministic maximum-degree conventions are zero. If $G$ is nonempty but edgeless, every density and relevant out-degree is zero, and every removal is permitted. An empty group family imposes no orientation constraint. More generally, if no group has a relevant edge, no price is asserted; otherwise all price denominators are positive as proved above. The lower construction has nonempty fibers and relevant edges, so its price is always defined. Its $k=2$ case is covered explicitly without treating repeated coordinate groups as distinct.

## Private Source-Repair Notes

The source encodes an edge orientation by its tail: $\phi(\{u,v\})=u$ represents $u\to v$ at L000063–L000064. Its upper-bound construction at L000159 and L000169 is therefore consistent with the corrected direction above. The former reference proof and rubric mistakenly translated that assignment as an arrow toward the earlier endpoint.

The lower-construction source requires the following local repairs, all recorded under theory_008:

1. At L000139, the sum of the even-parity fiber labels does not have odd parity. What is needed is nonmembership in the selected label set, which follows from the two-coordinate-support comparison proved in step_001.
2. At L000150, an arbitrary orientation gives a maximum expected out-degree at least the density, not necessarily equal to it. Inequality (A) proves the sufficient corrected assertion.
3. The source requires exactly $k$ distinct groups, but the displayed incident-coordinate groups coincide when $k=2$. Retaining one of the source's padded zero coordinates distinguishes the groups without changing their relevant graphs.
4. Under the literal source wording allowing positive $n$, the pair $(n,k)=(1,2)$ is infeasible: two distinct coordinate groups must include the empty set, whose optimum is zero. The minimal endpoint correction is $n\ge2$, already the frozen task's range. The padded-coordinate adjustment then covers every remaining $k=2$ case. All $k\ge3$ cases and both numerical conclusions are unchanged.
