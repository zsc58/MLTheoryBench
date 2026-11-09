# Problem

## Setup

Let G=(V,E) be an unknown finite directed acyclic graph with |V|=n, underlying a causally sufficient structural causal model. For each vertex, one fixed hard intervention is available: it replaces that vertex's mechanism by an exogenous mechanism and removes its dependence on its parents. An intervention on S subseteq V simultaneously applies these fixed replacements at the vertices in S and leaves every other mechanism unchanged. The replacement at a vertex is the same regardless of which other vertices are intervened on. Write P^S for the resulting interventional distribution and P^emptyset=P. Exact equality of the relevant one-vertex marginals may be queried.

For disjoint S,T subseteq V, define

Delta(S | T) = {v in V : the marginal law of v under P^(S union T) differs from its marginal law under P^T},

and abbreviate Delta(S)=Delta(S | emptyset).

For a DAG F, write Pa_F(y) for the set of vertices with an edge into y. Descendants are vertices reachable by directed paths of positive length; a vertex is not its own descendant. The transitive closure of F has an edge x->y exactly when F has a directed path of positive length from x to y.

For T subseteq V, let G-T be the graph obtained by deleting the vertices in T and all their incident edges. In a DAG F, call c a uniquely reachable child of a if a->c is an edge of F and is the unique directed path from a to c in F. Thus c is a uniquely reachable child of a given T when it has this property in G-T.

Assume the following two properties.

1. **Intervention locality.** For all disjoint S,T,

   Delta(S | T) is contained in S together with the descendants of S in G-T.

2. **Unique-child detectability.** For all disjoint S,T, every uniquely reachable child in G-T of every a in S belongs to Delta(S | T).

Consider the following procedure. If n<=1, return the graph (V,emptyset) without querying any intervention distributions. Otherwise perform these two stages.

1. Form a graph H on V by adding x->y for every distinct x,y such that y is in Delta({x}). Let H* be the transitive closure of H.
2. Initialize K=H*. Traverse the vertices y in a topological order of H*. For every currently present edge x->y, let

   B = Pa_K(y) minus {x}.

   Delete x->y if y is not in Delta({x} | B). Return the final graph K.

## Task

Prove that the procedure returns exactly the true DAG G. Also prove that it requires O(n^2) hard interventions and that every intervention used involves at most n-1 vertices.
