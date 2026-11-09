# Reference Proof

## Proof Structure

Restrict the perfect dependency matrix to variables on which the parents differ. Use its separating threshold to distinguish edges of the induced interaction graph from non-edges. Maintain the invariant that current clusters lie within connected components until each component has become a cluster. A path crossing two current clusters supplies an above-threshold linkage whenever a component remains split, whereas every cross-component linkage is below threshold. Finite progress and retention of all created clusters finish the proof.

## Complete Proof

Let
\[
I=\{g\in[n]:x^{(1)}_g\ne x^{(2)}_g\},\qquad H=G[I].
\]
The component masks, called PX masks in the source, are exactly the connected components of \(H\). If \(I=\varnothing\), there are no component masks and the claim is vacuous. Assume henceforth that \(I\ne\varnothing\).

Restrict \(D^*\) to \(I\times I\), writing \(D_I(g,h)=D^*(g,h)\). By perfectness, a real number \(\theta\) satisfies
\[
D_I(g,h)>\theta\quad\text{for each edge }\{g,h\}\text{ of }H,
\]
and
\[
D_I(g,h)<\theta\quad\text{for each distinct nonadjacent pair }g,h\text{ in }H.
\]
For distinct current clusters \(A,B\), the algorithm uses
\[
L(A,B)=\max_{g\in A,\,h\in B}D_I(g,h).
\]
The clusters are nonempty and finite, so the maximum exists. Symmetry of \(D_I\) makes this a strength for an unordered cluster pair. The prescribed update assigns exactly the same formula after each merge.

Current clusters form a partition of \(I\): this holds initially for singletons and is preserved by replacing two clusters with their union. Initially, each current cluster is also contained in a connected component of \(H\).

Suppose this latter property holds and some component \(C\) is not yet a single current cluster. Choose vertices of \(C\) in different current clusters and a path between them in \(H\). At some consecutive pair along that path, the vertices belong to different current clusters \(A,B\). That pair is an edge, hence
\[
L(A,B)>\theta.
\]
Conversely, if two current clusters lie in different components of \(H\), every cross pair is a non-edge. Their finite maximum linkage is therefore strictly below \(\theta\).

It follows that whenever any component remains split, a maximizing cluster pair has linkage above \(\theta\) and cannot lie in different components. Merging that pair preserves the property that every current cluster is contained in a component. This conclusion holds for every choice among maximizing pairs.

Each merge reduces the number of current clusters by one. Thus the algorithm must reach a stage at which every component is a single current cluster: it cannot stop while a component is split, since then at least two current clusters remain and an above-threshold merge is available. At this stage the current clusters are exactly the components of \(H\). The stage can be the initial stage, if all components are singletons, or the final stage, if \(H\) is connected. No actual below-threshold merge is needed for the argument.

Every cluster appearing at this stage is either an initial singleton or a union created by a merge. The algorithm retains all such nodes, even if subsequent merges join different components. Consequently, its returned linkage tree contains every component mask.

## Source Contract and Local Repairs

The source defines perfectness by requiring every edge entry to exceed every non-edge entry. For finite index sets this is equivalent to the strict real-threshold formulation in the task. If both classes are nonempty, choose a threshold strictly between the maximum non-edge entry and the minimum edge entry. If there are no edges, choose \(\theta=2\); if there are no non-edges but there is an edge, choose \(\theta=-1\). If there are no distinct pairs, either choice works. Diagonal entries are unused.

The matrix is supplied as a well-defined symmetric matrix. The theorem does not require proving that a particular sampling procedure produces it. The normalized-information background, the separate fitness-preservation properties of PX, and the downstream noise experiments are not invoked.

Two local source corrections are explicit. The restricted matrix uses \(D^*\), correcting the isolated \(D^{\bar *}\) symbol. Also, the source's assertion that no directly nonadjacent vertices are clustered together is replaced by the component-refinement invariant proved above. A connected component need not be a clique. The corrected assertion preserves the source's path-connectivity argument and final theorem.

## Proof-Obligation Closure

1. The restriction and mask identification follow directly from the definitions.
2. Threshold separation is an explicit hypothesis; its equivalence to source perfectness is established above, including empty edge classes.
3. The current-cluster partition and component-refinement properties are established initially and preserved by the stated merge argument.
4. A split component supplies a crossing edge; cross-component pairs contain only non-edges; maximality forces a within-component merge.
5. Strict decrease of the finite cluster count supplies the required stage without assuming a threshold crossing occurs.
6. Retention of every singleton and merged node proves the target, including empty and singleton cases.

No theorem-critical proof obligation remains unresolved.
