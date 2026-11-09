# Reference Proof

## Proof Structure

Keep only edges whose endpoints have different activation times in an auxiliary directed graph, orienting them from earlier to later activation. Add a capacitated source network. A minimum-time argument gives a cut lower bound of `kappa`, and integral max-flow/min-cut yields paths whose portions inside the activated graph are pairwise edge-disjoint. Their lengths are bounded by the target's activation time. Sending equal flow along these paths and applying Thomson's principle gives the effective-resistance bound.

## Audited Standard Background

1. **Max-flow/min-cut and integrality (theory_021).** In a finite directed network with distinct source and sink and nonnegative integer capacities, the maximum flow value equals the minimum capacity of a source-to-sink cut, and a maximum flow can be chosen integral. Cut capacity is the sum of capacities of arcs directed from the source side to the sink side. The application below has capacities `1` and `kappa`, so these hypotheses hold. The relevant source invocation is L001181-L001188.
2. **Thomson's principle (theory_022).** In a finite electrical network with unit edge resistances and connected distinct terminals `a,b`, effective resistance equals the minimum of `sum_e f(e)^2` over unit flows with net outflow `1` at `a`, net inflow `1` at `b`, and zero net outflow at every other vertex. The sum counts each undirected electrical edge once, using any fixed orientation to represent its signed current. Distinct parallel edges are counted separately. Unused components can carry zero current. For resistance to a nonempty set, identify that set to one terminal, retaining distinct parallel edges; loops may be ignored. The source states the set-to-vertex characterization and applies it at L001192-L001197. The paths constructed below verify connectivity, and the flow verifies all conservation requirements.

## Complete Proof

If `S_ell \ S_0` is empty, both universally quantified conclusions are vacuous. Otherwise fix `u in S_ell \ S_0` and write `t=T(u)`, so `1<=t<=ell`. For every `x in S_ell`, its activation time is an integer in `{0,...,ell}`, and `T(x)=0` exactly when `x in S_0`.

### Step 1: Auxiliary Directed Graph and Network

Let `H=G[S_ell]`. Construct an auxiliary directed graph `D` on `S_ell` as follows. For each edge `{a,b}` of `H` with `T(a)<T(b)`, include the arc `a->b`; use the reverse direction when `T(b)<T(a)`. If `T(a)=T(b)`, include no corresponding arc. This omission applies in particular to edges inside `S_0`, and also to edges between vertices activated simultaneously. It changes only the auxiliary graph, not `H`.

Every arc of `D` strictly increases activation time, so `D` is acyclic. Add a new source `r`, an arc `r->z` of capacity `kappa` for each `z in S_0`, and capacity one on every arc of `D`. The augmented network is finite and acyclic, has distinct source `r` and sink `u`, and has nonnegative integer capacities.

### Step 2: Cut Bound, Path Extraction, and Lengths

Consider any `r-u` cut, and let `U` be the graph vertices on its sink side. Thus `u in U`. If `U` contains a vertex `z in S_0`, then the arc `r->z` crosses the cut and already contributes capacity `kappa`.

Otherwise `U` is disjoint from `S_0`. Choose `x in U` minimizing `T(x)`. Then `T(x)>=1`. The activation condition gives at least `kappa` distinct neighbors of `x` in `S_{T(x)-1}`. Every such neighbor `y` satisfies `T(y)<T(x)` and therefore lies outside `U`, by the minimality of `T(x)`. Its edge to `x` is represented by an arc `y->x` crossing the cut, with capacity one. Hence this cut also has capacity at least `kappa`.

All cuts consequently have capacity at least `kappa`. By the stated max-flow/min-cut and integrality result, there is an integral maximum flow of value `F>=kappa`.

For completeness, its needed path decomposition is elementary here. While the remaining flow value is positive, start with a positive-flow arc leaving `r` and follow positive-flow arcs. At every reached vertex other than `u`, conservation supplies an outgoing positive-flow arc. Acyclicity prevents repetition, and finiteness forces the walk to reach `u`. Subtract one unit along this path; integrality preserves nonnegativity and conservation, and the flow value decreases by one. Repeating this procedure extracts at least `kappa` unit-flow `r-u` paths.

The auxiliary arcs `r->z` may occur in more than one extracted path because their capacities are `kappa`. In contrast, every arc of `D` has capacity one and can occur in at most one extracted path. Delete the initial source arc from each of any `kappa` extracted paths. The resulting directed paths `P_1,...,P_kappa` start in `S_0`, end at `u`, and are pairwise arc-disjoint inside `D`. Since each arc of `D` comes from a distinct undirected edge of `H`, these are pairwise edge-disjoint paths in `H`.

Along each `P_i`, activation times are strictly increasing integers, starting at zero and ending at `t`. Each edge increases the time by at least one, so `length(P_i)<=t`. Moreover, no path can meet `S_0` after its starting vertex, since all vertices of `S_0` have time zero. Reversing the paths gives the required paths joining `u` to `S_0`.

### Step 3: Unit Flow and Energy

Contract `S_0` to one terminal `s`, retaining distinct parallel edges with their unit resistances. Each `P_i` meets `S_0` only at its initial endpoint, so after contraction it is a path between `s` and `u` with the same length. No two distinct used edges are identified as electrical edges by this contraction. Thus the paths remain edge-disjoint, even if they share vertices or their edges become parallel.

Orient each path from `u` toward `s` and send `1/kappa` units of current along it. Put zero current on all unused edges. Each individual path conserves current at its internal vertices; summing the path flows preserves conservation even at shared vertices. The net outflow at `u` is `kappa*(1/kappa)=1`, and the net inflow at `s` is one. This is therefore a unit flow between connected distinct terminals.

Edge-disjointness makes the magnitude of the current on every used edge exactly `1/kappa`. Its energy is consequently
`sum_e f(e)^2 = (1/kappa^2)*sum_{i=1}^kappa length(P_i) <= (1/kappa^2)*kappa*t = t/kappa`.

### Step 4: Effective Resistance and Horizon

Thomson's principle applies to this finite unit-resistance network and the verified unit flow. It gives
`R_eff^H(S_0,u) <= t/kappa = T(u)/kappa`.
Since `T(u)<=ell` and `kappa>0`,
`R_eff^H(S_0,u) <= T(u)/kappa <= ell/kappa`.
The target `u` was arbitrary, so both conclusions hold for every required vertex. The argument uses only the threshold condition on each newly activated vertex, not a selection distribution, a single-activation rule, or connectedness of the initial set. Repeated active sets and early stopping require no additional case.

## Source and Obligation Closure

Step 1 follows the construction at L001170-L001172. Step 2 supplies the entire cut and path argument at L001173-L001190, including the distinction between shared auxiliary source arcs and disjoint graph arcs. Step 3 gives the conservation and energy argument at L001192-L001195; the activation-time paths already meet the initial set only at their endpoints, so no trimming is needed in this application. Step 4 is the application at L001199-L001202. Every theorem-critical obligation is derived above or follows from the stated standard-independent results with verified hypotheses. No unresolved private proof obligation remains.
