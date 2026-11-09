# Reference Proof

## Proof Structure

Handle graphs with at most one vertex without experiments. For larger graphs, show that the graph obtained from singleton-intervention changes has exactly the same reachability relation as the true DAG. Then prove that, throughout the deletion stage, the current graph lies between the true DAG and its transitive closure. Under this invariant, the conditional query retains every true edge and removes every non-edge. Finally count both distributions needed for each conditional comparison and bound all intervention cardinalities.

## Intervention Semantics

Each vertex has one fixed available replacement mechanism. Consequently, the replacements on B are identical in P^B and P^(B union {x}); the comparison does not change the intervention on B when x is added. This is the fixed-conditioning semantics required by the source.

The conditional locality assumption is also the hard-intervention consequence used in the source. To see this, compare the two structural recursions with the same exogenous inputs. Vertices in B use the same parent-independent replacement mechanisms in both systems. Outside B, the only newly replaced mechanism is at x. In a topological recursion, a difference can therefore propagate from x only along a directed path avoiding B. More generally, for disjoint S,T, changes can occur only in S and its descendants in G-T. This explains the source fidelity of the public conditional-locality formulation; the proof below uses it as the stated assumption.

## Complete Proof

If n<=1, a DAG on V has no edges. The procedure returns this graph without queries. Exact recovery and the intervention-count bound hold, and the cardinality assertion is vacuous because there are no interventions, including when n=0. Henceforth suppose n>=2.

Let H be the graph formed in the first stage and let H* be its transitive closure.

By locality with T empty, if y is in Delta({x}) and y!=x, then y is a descendant of x in G. Therefore every edge of H belongs to TC(G), and hence H* is a subgraph of TC(G). In particular, H and H* are acyclic, so the topological order requested by the procedure exists.

For the reverse inclusion, fix a topological ordering r of G. We prove by strong induction on r(y)-r(x) that every true edge x->y of G is represented by a directed x-to-y path in H. If the direct edge is the unique directed path from x to y, then y is a uniquely reachable child of x. Unique-child detectability with S={x} and T empty gives y in Delta({x}), so x->y is an edge of H.

Otherwise there is another directed path

x=z_0 -> z_1 -> ... -> z_m=y,

with m>=2. Every edge z_{i-1}->z_i on this path has a strictly smaller topological-index difference than x->y. By induction, each is represented by a path in H. Concatenating these paths gives an x-to-y path in H. The concatenation cannot repeat a vertex because H is acyclic. The induction starts because an edge with topological-index difference one cannot have an alternative directed path.

Thus every edge of G belongs to H*. Since H* is transitive, TC(G) is a subgraph of H*. Consequently,

H* = TC(G).

Now consider the deletion stage. Initially K=H*=TC(G), so

G is a subgraph of K, and K is a subgraph of TC(G).

We show that processing an edge preserves this invariant and makes the correct decision. Suppose the current candidate is x->y and set

B = Pa_K(y) minus {x}.

Neither x nor y belongs to B, because x was excluded and K has no self-edges.

First suppose x->y is a true edge. Because G is a subgraph of K, B contains every true parent of y other than x. Every alternative directed path from x to y has a final edge p->y with p a true parent of y distinct from x. Indeed, a longer path ending with x->y would repeat x, which is impossible in a DAG. Hence p is in B. Deleting B destroys every alternative x-to-y path, while the direct edge x->y remains. Thus y is a uniquely reachable child of x in G-B. Unique-child detectability gives

y in Delta({x} | B),

so the procedure retains every true edge.

Next suppose x->y is not a true edge. Every directed x-to-y path in G ends with p->y for some true parent p of y. Because x is not itself a parent of y, every such p differs from x. The invariant G subseteq K implies p is in Pa_K(y), and hence p is in B. Thus G-B has no directed path from x to y. Since y!=x, conditional locality implies

y not in Delta({x} | B).

The procedure therefore deletes every candidate that is not a true edge.

Deleting a non-edge preserves G subseteq K; retaining a true edge does not change K. No operation adds an edge, so K remains a subgraph of TC(G). The invariant therefore holds after every query, independently of the order used among candidate parents.

Only the edge currently being tested can be deleted at a step. Thus every original candidate edge is tested once when its head is processed, unless it has already been tested and deleted. At termination every true edge remains and every other edge of TC(G) has been removed. The returned graph is exactly G.

There are at most n singleton interventions in the first stage. An acyclic graph has at most one directed edge for each unordered pair, so H* has at most n(n-1)/2 edges. The second stage makes at most that many conditional comparisons. Each comparison uses at most the two distributions P^B and P^(B union {x}). Even without reusing any previously obtained intervention distributions, the number of hard interventions is therefore at most

n + 2[n(n-1)/2] = n^2.

The observational distribution P^emptyset is not a hard intervention. Counting it additionally as a distribution request would not change the asymptotic bound.

Because neither x nor y belongs to B, |B|<=n-2 and |B union {x}|<=n-1. The first-stage singleton interventions also have size at most n-1 because n>=2. Together with the query-free n<=1 case, this proves every claimed intervention bound.

## Source Audit Notes

The source's reverse-topological proof has a local direction-word error: downstream vertices occur before, not after, the current source in reverse topological order. Its replacement-child recursion terminates by strict decrease in ordinary topological position. The topological-gap induction above supplies a complete equivalent derivation.

The literal source algorithm unnecessarily queries its singleton at n=1. The explicit query-free return for n<=1 is the local boundary repair needed for the advertised n-1 bound. Counting both distributions in each conditional comparison also corrects the source's one-intervention-per-edge accounting without changing its O(n^2) conclusion. These repairs are recorded in provenance. No theorem-critical proof obligation remains unresolved.
