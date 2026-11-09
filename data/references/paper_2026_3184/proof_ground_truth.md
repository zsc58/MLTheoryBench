# Reference Proof

## Audited background

We use the following standard graphical facts, with their hypotheses stated here.

1. Nonadjacent vertices of a DAG can be separated by the parents of one endpoint: choose an endpoint for which the other is a non-descendant.
2. Two DAGs are Markov equivalent exactly when they have the same skeleton and unshielded colliders. For a true unshielded triple X-Z-Y and any separating set Q for its endpoints, Z is a collider exactly when Z is not in Q.
3. Starting with an exact skeleton and its unshielded colliders, consistent orientation knowledge and exhaustive application of the four Meek rules produce the associated MPDAG.
4. For an ancestral vertex set S, d-separation among vertices of S conditional on subsets of S agrees in D and D[S]. Consequently a distribution faithful to D has a marginal faithful to D[S].
5. In a CPDAG, a vertex is an ancestor of another in some represented DAG exactly when there is a possibly directed path between them.
6. For a DAG, d-separation of disjoint endpoint sets by Q is equivalent to separation after deleting Q from the moral graph of the induced DAG on all ancestors of the endpoints and Q. Moralization joins parents of each common child and then drops directions.

These are standard independent graphical results. The prior algorithm-specific SNAP guarantees are provenance context, not assumed proof steps.

## 1. Skeleton preservation and separators

Every initial pair is adjacent. Every subsequent edge deletion, including a collider-subroutine deletion, is certified by an oracle independence with a conditioning set excluding both endpoints. A true adjacency is d-connected by its one-edge path under every such conditioning set. Faithfulness therefore prevents its deletion. Restriction to retained vertices preserves this statement. At every stage the current skeleton contains the true skeleton induced on its current vertices.

Every missing edge between current vertices has a stored valid separator. Known gaps are not deleted merely because they are known. Previously stored separators remain valid even if some of their vertices have subsequently been pruned: the procedure's stored-separator queries are still queries about the original distribution.

## 2. Collider arrowheads

Consider a collider operation adding arrowheads at Z in X *-> Z <-* Y, and write Q for the stored separator of X,Y. The operation ensures

X independent of Y given Q; Z not in Q; X dependent on Z given Q; Y dependent on Z given Q.

At order zero Q is empty. Every surviving unknown pair or known gap has been tested marginally, while a skipped known adjacency is a true adjacency and hence marginally dependent. Thus both dependence witnesses hold at order zero. At later orders they are tested explicitly. Saved triples are removed when one of their incident edges is deleted, and their stored endpoint separators remain valid.

We show that Z cannot be an ancestor of X in any DAG D' in the full observational equivalence class of D. All four relations above hold as d-separation or d-connection statements in D'. Suppose Z were an ancestor of X. Let H be the ancestor set in D' of {X,Y} union Q; then Z belongs to H. The dependence of X,Z given Q gives an X-to-Z connection avoiding Q in the moral graph on An_D'({X,Z} union Q). This moral graph is a subgraph of the moral graph on H. Similarly, the dependence of Y,Z given Q gives a Y-to-Z connection avoiding Q in the latter graph. Since Z is not in Q, these connections join X to Y after Q is deleted. The moral-graph criterion contradicts their separation. Interchanging X,Y proves the other endpoint assertion.

Let C be the full observational CPDAG. Its possible-ancestry characterization shows that C has no possibly directed path from Z to either endpoint. G has the same skeleton as C and only adds orientations, so it cannot acquire a possibly directed, and hence cannot acquire a b-possibly causal, path absent in C. This proves the collider ancestry assertion.

In particular, whenever X-Z is a true adjacency, every DAG in the observational class must orient it X->Z. Thus a collider operation puts no arrowhead on the departure endpoint of any true edge that can be traversed in a possibly directed path of G. Background orientations also agree with G. Temporary spurious edges may be bidirected; this does not affect the true-edge assertion. No finite-order Meek step is used.

## 3. Inductive pruning invariant

Let S be the vertex set present immediately before an iteration. Inductively assume T is contained in S and bPossAn_G(S) is contained in S. Initially S=V, so both assertions hold.

Skeleton preservation and Section 2 imply that every possibly directed path of G whose vertices lie in S can be traversed in the same direction in the temporary graph used for pruning.

Let R be the new retained set. Every target belongs to R by its length-zero path. Suppose Y belongs to R and X belongs to bPossAn_G(Y). Choose a b-possibly causal path from X to Y in G. Every suffix of this path is b-possibly causal to Y, so every vertex of the path belongs to bPossAn_G(S), hence to S. The path is possibly directed and is therefore preserved in the temporary graph. Append the possibly directed path from Y to a target witnessing Y in R. The result is a traversable walk; erasing repeated-vertex segments gives a possibly directed path from X to that target. Hence X belongs to R.

This proves bPossAn_G(R) is contained in R and completes the induction, including all intermediate iterations. In particular, the finite-order conclusion holds for every requested k.

## 4. Exact full-order skeleton and colliders

Assume |V| is at least two and let S be the set retained after the last iteration of the full-order run. By Section 3 it is closed under b-possible ancestry. In particular it contains every true parent of each of its vertices, since a true parent edge is either directed toward its child or undirected in G and is a one-edge b-possibly causal path. These parents also belonged to every earlier retained set containing that child.

Suppose distinct X,Y in S are nonadjacent in D but still adjacent in the final learned skeleton. Choose an endpoint, say X, whose true parent set P separates it from Y. Because X,Y are nonadjacent, P excludes them and |P| is at most |V|-2. Every vertex of P survives throughout the run. True adjacency preservation keeps P adjacent to X, and consistent background knowledge cannot classify a true parent as a child of X or as nonadjacent to X. Thus P is an available candidate set at order |P|. If the pair has no background information, the ordinary pass tests it; if it is a known gap, the gap pass tests it from the appropriate endpoint. It cannot be a known adjacency because the knowledge is consistent. If the pair was already deleted there is nothing to prove; otherwise the search finds a separator no later than this test. This contradicts its final adjacency. Together with Section 1, the final skeleton is exactly that of D[S].

For any unshielded triple X-Z-Y of this exact skeleton, its valid stored endpoint separator contains Z if the triple is a noncollider, since otherwise its two-edge path would be active. If the triple is a collider, the separator cannot contain Z, since conditioning on Z would activate that same path. Its two incident true edges are dependent under every allowed separator. Therefore the final collider operation orients every true unshielded collider and no noncollider. At order zero this is the PC test; at positive orders the two RFCI dependence checks necessarily pass on true incident edges. Orientations are freshly constructed from the current skeleton, so no earlier spurious-edge orientation is carried into this step. The subsequent background orientations are consistent.

## 5. Restriction to the larger closed retained set

We establish the needed induced-MPDAG fact rather than assuming a prior algorithmic result.

For any b-possibly ancestral set S, an edge crossing from an outside vertex W to an inside vertex Z must be Z->W in G. An undirected edge or W->Z would make W a one-edge b-possible ancestor of Z. Consequently all boundary edges point out of S in every DAG represented by G, and S is ancestral in D. The distribution restricted to S is therefore faithful to D[S].

Restrict any full DAG represented by G to S. The resulting DAG has the skeleton and unshielded colliders of D[S] and satisfies the restricted knowledge B[S]. Conversely, take any DAG E on S with this skeleton and these unshielded colliders that satisfies B[S]. Join E to the part of D outside S and retain D's boundary edges. All boundary edges point out of S, so this graph is acyclic. Its unshielded colliders inside S are unchanged; those outside S are unchanged because their incident boundary and exterior edges retain D's orientations. There are no incoming boundary edges at an inside vertex. Thus the joined graph has D's skeleton and unshielded colliders, and it satisfies all of B. It belongs to the full represented class.

The possible orientations of every edge inside S therefore coincide in the full restricted class and the internal class defined by D[S], B[S]. Their MPDAGs agree. By Section 4 and Meek completeness, applying the full-order Meek step yields exactly G[S].

## 6. Final restriction and MPDAG status

Put A=bPossAn_G(T). Since S contains T and is closed under b-possible ancestry, A is contained in S. Moreover, each vertex on a b-possibly causal path to a target is itself in A, by taking a suffix. All such paths and all edges between their vertices are therefore unchanged in G[S]. Conversely, a b-possibly causal path in G[S] is one in G, because the subgraph is induced and cannot hide a backward chord between its path vertices. The final pruning selects exactly A and returns G[A].

It remains to prove that G[A] is an MPDAG. Do not assert that A is b-possibly ancestral: this can fail. Instead let H=G[A] and use D[A] as a consistent DAG extension. Every unshielded collider of D[A] is also an unshielded collider of D, so its two arrowheads occur in H. Each Meek rule has a local premise consisting solely of specified edges and nonedges among its participating vertices. Any applicable rule in H would also be applicable in G. Since G is closed, H is closed as well. Starting from the skeleton and unshielded colliders of D[A], use all directed edges inherited in H as consistent orientation constraints. The intermediate graph is contained in H, and Meek closure cannot leave H; after those constraints are imposed it is H itself. Meek completeness therefore shows that H is an MPDAG.

This last statement retains inherited orientations. It does not claim that arbitrary final pruning permits reconstruction using only B restricted to A; the stronger reconstruction statement in Section 5 required the larger closed set S.

For T empty, the first pruning retains nothing and both targets are the empty graph or empty-set assertions. For an empty or singleton input, the full-order boundary convention returns the edge-free graph on T, which is precisely G[bPossAn_G(T)]. The requested finite-order range is empty when |V|<2. These cases complete the proof.
