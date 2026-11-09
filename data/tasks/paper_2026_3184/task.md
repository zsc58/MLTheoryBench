# Problem

## Setup and graph notation

Let V be a finite set of observed variables. Let p be Markov and faithful to a causal DAG D on V, with no latent confounding or selection bias. Thus an oracle query X independent of Y given S returns true exactly when S d-separates X and Y in D; queries always have distinct endpoints outside S.

A CPDAG represents a DAG Markov-equivalence class: it has the common skeleton, and an edge is directed exactly when all represented DAGs agree on its direction. Background knowledge B consists of pairwise assertions of adjacency, oriented adjacency X->Y, or a gap between two vertices. Adjacencies and gaps are symmetric assertions. Assume all assertions are consistent with D. Let G be the MPDAG obtained from the CPDAG of D by imposing B's orientation assertions and applying Meek closure. An MPDAG is a maximally oriented partially directed acyclic graph representing a Markov-equivalence class restricted by consistent orientation knowledge.

Write H[S] for the induced subgraph on S and Adj_H(X) for the vertices adjacent to X in H. A path has distinct vertices; length-zero paths are allowed. A path from X=V_0 to Y=V_m is **possibly directed** if the edge V_i V_{i+1} has no arrowhead at V_i for every i. Temporary graphs in the procedure below may have bidirected edges; their arrowheads count in this test. A path is **b-possibly causal** if there is no directed edge V_j->V_i in the graph for any i<j, including edges between nonconsecutive path vertices. Write bPossAn_H(S) for the vertices with a b-possibly causal path in H to some vertex of S, including S itself. This notation will be used for graphs having only directed and undirected edges.

An unshielded triple (X,Z,Y) consists of distinct vertices with edges XZ and ZY but no edge XY; Z is its middle vertex. Adding an arrowhead at Z preserves the mark at the other endpoint of the edge, so two collider operations may temporarily produce a bidirected edge.

## Meek closure

Meek closure repeatedly applies the following rules until none applies. Vertices within a rule are distinct, a dash denotes an undirected edge, and each conclusion orients X-Y as X->Y:

1. Z->X-Y and Z,Y nonadjacent.
2. X->Z->Y and X-Y.
3. U->Y<-Z, U-X-Z, X-Y, and U,Z nonadjacent.
4. X-Y, X-U, U->Z, X-Z, Z->Y, and U,Y nonadjacent.

## Skeleton searches

The procedure maintains an undirected skeleton U on its current vertex set and a shared map Q assigning a separating set to an unordered pair whenever one is found. For a current vertex X define

P_U(X) = Adj_U(X) minus {W : B asserts X->W or a gap between X and W}.

At conditioning order i, perform these two passes in the stated order:

- **Ordinary pass.** For ordered adjacent pairs (X,Y) about which B contains no assertion, test all i-element subsets of P_U(X) minus {Y} until a separator is found or the candidates are exhausted. On finding X independent of Y given S, delete XY, store Q({X,Y})=S, and stop testing that ordered pair.
- **Known-gap pass.** For known-gap pairs whose endpoints are current vertices, perform the same i-element subset search from both endpoint orderings. On finding a separator, delete the edge if present and store the separator. If no separator has been found, do not delete an edge merely because B declares a gap.

Known adjacencies and known orientations are skipped by these skeleton passes. Current adjacency sets are used during the searches. Loops may use any fixed ordering, stopping a pair's search after a separator is found. Separator entries persist between calls and iterations, including entries containing vertices later pruned. Such entries, when subsequently used in an oracle query, still refer to variables in the original set V. No separator entry is inferred from background knowledge alone.

## Collider operations

Both operations start from the input skeleton with no arrowheads inherited from an earlier iteration.

**Vstruct-0.** For every unshielded triple (X,Z,Y), if Z is not in Q({X,Y}), add arrowheads at Z on both incident edges.

**Vstruct-R.** Maintain a worklist M of the skeleton's unshielded triples and an initially empty set L of verified triples. While M is nonempty, remove a triple (X,Z,Y) from M and process it as follows:

- If Z belongs to Q({X,Y}), do nothing further with this triple.
- Otherwise, set S=Q({X,Y}) and test X independent of Z given S and Y independent of Z given S. If both tests return dependence, add (X,Z,Y) to L.
- If at least one returns independence, for each endpoint W in {X,Y} for which W is independent of Z given S, reduce a copy of S by repeatedly removing one element whenever independence still holds, until no single removal preserves independence. Store the resulting separator for {W,Z} and delete WZ from U. Remove from M and L every triple that uses WZ as an incident edge. Add to M all newly unshielded triples whose endpoints are W,Z and whose middle vertex is a remaining common neighbor.

When M is empty, form a fresh undirected copy of the resulting U and, for every (X,Z,Y) in L, add arrowheads at Z on XZ and YZ. Return this graph, its skeleton, and the updated separator map. Worklists contain each unshielded triple at most once, up to interchange of its endpoints. Choices of triples and removable separator elements may use any fixed ordering.

## Targeted-BK procedure

Fix a target set T subseteq V and an integer k>=0. Initialize the current vertex set as V, U as the complete undirected graph on V, and Q as empty. At each order i=0,...,k:

1. Restrict U to the currently retained vertices and run the two skeleton passes at order i.
2. Apply Vstruct-0 if i=0 and Vstruct-R otherwise. In the latter case retain its updated skeleton and separator map.
3. Apply B's orientation assertions on current edges of the temporary graph.
4. Retain exactly the current vertices having a possibly directed path in that graph to a vertex of T.

Only the skeleton, separator map, and retained vertex set are carried to the next order; temporary orientations are reconstructed as specified above. Meek closure is not applied in this loop. Let Vhat_k be the retained set after order k, let Uhat_k be the skeleton restricted to Vhat_k, and let Hhat_k be the last temporary oriented graph restricted to Vhat_k.

For |V|>=2, the **full-order output** is obtained by running this procedure with k=|V|-2, applying Meek closure to Hhat_k, and then taking the induced subgraph on vertices having a b-possibly causal path to T in that graph. For |V|<2, define the full-order output to be the edge-free graph on T. Empty target sets and empty induced graphs are allowed.

## Task

Under the assumptions above, prove the following integrated claim for every permitted ordering of the procedure's searches and worklists:

1. For every k=0,1,...,|V|-2, the finite-order output satisfies

   T subseteq Vhat_k and bPossAn_G(Vhat_k) subseteq Vhat_k.

2. The full-order output is exactly

   G[bPossAn_G(T)],

   and this output is an MPDAG.
