# Reference Proof

## Status and Scope

This is a complete proof of the public worst-case lower bound. It uses the source's conditioning-subset count, clique ordering, and single-edge deletion construction, specialized to a complete clique with isolated remaining vertices. This specialization is sufficient because the public target asks for a hard input of each parameter value, not a lower bound on every fixed input.

The three findings against the previous reference were correct. The required version of U1 is proved in Sections 1 and 3; the required version of U2 is proved for arbitrary set-valued queries in Section 4; and U3 is proved constructively in Section 8. No general clique-extension theorem, specialized edge-deletion lemma, or general faithful-distribution existence theorem is assumed.

The source's stronger arbitrary-input argument is not certified here. Its general clique-extension assertion and general external edge-deletion implication are unnecessary for the unchanged public worst-case target.

## Proof Structure

Choose a complete clique of size s and isolate all remaining vertices. Count the conditioning intersections within that clique and select one absent from a short transcript. Order the clique around that intersection and delete one edge. Direct path analysis shows that the deleted-edge alternative can disagree only at the missing conditioning intersection. Section 8 constructs faithful Markov distributions for both graphs. Adaptive indistinguishability then proves the lower bound, including for exact randomized procedures.

## Theorem-Critical Obligations

- Oracle semantics and the competing-input class: specified by the public setup; the algorithm must be correct over all DAGs on V.
- Existence of a distinguished graph with parameter exactly s: proved in Section 1, with faithful realization in Section 8.
- Subset counting and selection of an unused intersection: proved in Section 2.
- U1 for the required hard family: every prescribed clique order yields a representative of the same MEC, proved in Sections 1 and 3.
- Valid deleted-edge alternative with a distinct essential graph: proved in Section 3.
- U2 for the required hard family and every allowed query: proved in Section 4.
- U3, admissible distributions for the distinguished and alternative graphs: proved in Section 8 by an explicit construction.
- Adaptive and exact-randomized indistinguishability: proved in Sections 5 and 6.
- Zero-bound cases and exponential interpretation: proved in Sections 1 and 7.

## Complete Proof

### 1. Oracle Model, Boundary Cases, and Distinguished Graph

If V is empty, its unique DAG and the distribution on the empty tuple give the asserted zero lower bound. If p≥1 and s=1, take the edgeless DAG and independent standard normal variables. Every disjoint-set CI holds, exactly as every such d-separation holds in the edgeless graph. Its essential graph has maximum clique size one, and the required lower bound is again zero.

Now fix 2≤s≤p. Choose a subset S⊆V of size s. Let G have every edge between distinct vertices of S, oriented according to a total order, and no edges incident to V\S.

For any pairwise disjoint A,B,C, if both A∩S and B∩S are nonempty, some pair of their vertices is joined by an edge. That length-one path is active regardless of C. If either intersection is empty, every vertex on that side is isolated, so no path connects the two sides. Thus the d-separation answers of G depend only on whether both endpoint sets meet S, not on its chosen total order.

Consequently, every total ordering of the complete clique gives a DAG in the same MEC. For each clique edge, orders realizing either orientation exist. Hence E(G) consists of an undirected complete graph on S and isolated vertices outside S, and s(G)=s. Section 8 supplies a distribution P_0 that is Markov and faithful to G. Fix one such distribution and use its exact CI oracle as the distinguished input.

### 2. Counting and Selecting an Unused Intersection

First consider a deterministic procedure and suppose it halts on this oracle after q<2^s-s-1 tests, whose conditioning sets are C_1,...,C_q.

The family

{W⊆S : |W|≤s-2}

has cardinality

sum_{k=0}^{s-2} binom(s,k)=2^s-binom(s,s-1)-binom(s,s)=2^s-s-1.

Each query records only one intersection C_i∩S. Repetitions and intersections outside this family cannot increase the number of its members recorded. Therefore some W⊆S with |W|≤s-2 satisfies C_i∩S≠W for every performed test.

Since |S\W|≥2, choose distinct u,v∈S\W. Order the clique vertices as u, then all vertices of W, then v, then all remaining vertices. Put

R=S\(W∪{u,v}).

### 3. Representative and Deleted-Edge Alternative

Let F contain all clique edges oriented forward in this prescribed order, and keep V\S isolated. Section 1 proves directly that F∈[G]; there are no constraints involving outside vertices to extend. This closes the required version of U1 without assuming the general clique-extension assertion.

Delete u→v from F to obtain H. It is still a DAG, since deleting an edge cannot create a directed cycle. Its skeleton differs from that of G. An essential graph shares its represented DAG's skeleton, so E(H)≠E(G).

Within the clique, the construction also gives the source's parent/child identities

pa_F(v)∩S={u}∪W,

ch_F(u)∩S=S\{u},

and therefore

(pa_F(v)∩ch_F(u))∩S=W=(pa_F(v)\{u})∩S.

These identities are verified algebra, not a substitute for proving the disagreement implication. That implication is proved directly next. Section 8 supplies a faithful Markov distribution for H, closing its admissibility obligation.

### 4. Direct Proof of Query Agreement

First analyze the only nonadjacent pair within S in H, namely u and v. Let C⊆V\{u,v}.

If some w∈W is not in C, the path u→w→v is active given C. Thus u and v are d-connected.

If some r∈R belongs to C, the path u→r←v is active given C because its collider r is conditioned on. Again u and v are d-connected.

It remains to consider C∩S=W. Any path between u and v lies entirely in S, since every outside vertex is isolated. If such a path visits R, choose the vertex on the path that is latest in the prescribed total order. It belongs to R, both neighboring path vertices precede it, and therefore it is a collider. All its descendants also belong to R, while C contains no vertex of R. This collider blocks the path.

If the path does not visit R, every internal vertex belongs to W. There is at least one internal vertex because u-v was deleted. The last internal vertex w is followed by the edge w→v, so w is a non-collider on the path. Since w∈W⊆C, the path is blocked. These cases exhaust all possible paths. Hence

u is d-separated from v by C in H if and only if C∩S=W.

Now consider an arbitrary allowed query (A,B,C), including set-valued or empty endpoint sets. If one endpoint set contains no vertex of S, both graphs give d-separation because that side consists of isolated vertices. If both endpoint sets meet S, G and F give d-connection by a direct edge. For H to give d-separation, every pair crossing A∩S and B∩S must lack an edge. The only missing pair in S is {u,v}, so necessarily A∩S={u}, B∩S={v}, or the reverse. In that case all other endpoints are isolated, and the preceding analysis applies.

Therefore a query answer can differ between G and H only if C∩S=W. This proves the required version of U2 for every allowed query without invoking the general external lemma. Since none of the performed queries has that intersection, their graphical answers agree.

### 5. Adaptive Indistinguishability

Use P_0 for G and a faithful Markov distribution P_H for H from Section 8. Faithfulness and Markovness make their CI answers equal to the graphical answers just analyzed.

At the first query, the deterministic procedure has the same input V. If its transcripts agree through query i-1, it chooses the same ith query. Section 4 gives the same answer to that query. Induction therefore gives the same complete transcript, stopping decision, and output after q tests.

Because E(H)≠E(G), the common output cannot be correct on both admissible inputs. The algorithm must be correct on H even if s(H) differs from s. Thus a universally correct deterministic algorithm cannot halt on the distinguished input before 2^s-s-1 tests.

The same construction proves the public transcript formulation for a short-query procedure whether or not that procedure is correct: its transcript on the distinguished input is compatible with the two distinct admissible MECs.

### 6. Exact Randomized Procedures

Fix an arbitrary enumeration of S to make the choices of u, v, and the orders within W and R deterministic for each W. There are finitely many W and therefore finitely many alternatives H_W. Fix one faithful Markov distribution for each H_W using Section 8, as well as P_0, before considering any random seed of the algorithm.

For an exact randomized algorithm, termination and correctness hold with probability one on each of these finitely many inputs. Intersect these finitely many probability-one events. The intersection still has probability one. Fix a seed in it; the resulting deterministic procedure is correct and terminates on every member of the fixed family simultaneously.

If it uses fewer than 2^s-s-1 tests on P_0, Sections 2–5 select a W and produce a contradictory common output on P_0 and P_{H_W}. Selection of W may depend on the transcript, but the alternative belongs to the already fixed finite family, on all of which this seed is correct. Hence such a short transcript is impossible for a seed in the probability-one event.

In particular, the worst-case query cost, including internal randomness, on the distinguished input is at least the claimed bound. No bounded-error or expected-query lower bound is needed.

### 7. Exponential Interpretation

For integers s≥3, s+1≤2^{s-1}. This holds at s=3, and the induction step follows from s+2≤2(s+1). Consequently,

2^{s-1}≤2^s-s-1≤2^s.

Thus the exact lower bound is exponential as s tends to infinity. The zero values at s=0 and s=1 were handled separately.

### 8. Elementary Faithful Realizations of the Hard Family

We now close U3 and the existence assertion used in Section 1. This construction applies separately to any complete ordered clique graph F with isolated remaining vertices and to any corresponding graph H obtained by deleting u→v in the order u,W,v,R. It uses no general faithful-realization theorem.

Let D denote either graph. Choose independent standard normal variables ε_j, one for each vertex, and a real coefficient β_ij for each allowed arrow i→j of D. In topological order define

Z_j=sum_{i→j in D} β_ij Z_i+ε_j.

Vertices outside S have no incident edges and hence Z_j=ε_j. If B has entry β_ij in row j, column i, then B is strictly triangular in this order and

Z=Lε, where L=(I-B)^{-1}=I+B+...+B^{p-1}.

Thus the covariance matrix Σ=LL^T is positive definite for every coefficient choice, and all its entries are polynomials in the coefficients. The transformation from Z to ε is triangular with determinant one, so the joint density is

(2π)^{-p/2} exp(-1/2 sum_j (z_j-sum_{i→j in D} β_ij z_i)^2).

It factorizes into the conditional normal densities prescribed by D. We next verify its exact graphical independences for a suitable coefficient choice, rather than assuming that a factorizing distribution is faithful.

For distinct i,j and C⊆V\{i,j}, completing the square in this positive Gaussian density gives the conditional covariance

κ_{ij|C}=Σ_ij-Σ_iC Σ_CC^{-1} Σ_Cj.

It does not depend on the value conditioned on. In particular, if it is nonzero, conditional independence is impossible. For nonempty C its numerator after multiplication by the positive number det(Σ_CC) is the polynomial

N_{ij,C}=Σ_ij det(Σ_CC)-Σ_iC adj(Σ_CC) Σ_Cj.

For C empty, set N_{ij,∅}=Σ_ij. The conditional covariance formula follows by subtracting the linear conditional mean Σ_{TC}Σ_CC^{-1}Z_C from a Gaussian subvector Z_T; completing the square yields covariance Σ_TT-Σ_TCΣ_CC^{-1}Σ_CT. Positive definiteness verifies every inverse and conditional density used here.

For every graphically d-connected pair and conditioning set in our family, the corresponding polynomial N_{ij,C} is not identically zero. This is checked with the following explicit coefficient assignments, used only as polynomial witnesses:

1. If i and j are adjacent, set the coefficient of their arrow to 1 and every other coefficient to 0. Their variables are an independent standard noise and its sum with a second independent standard noise. Every variable in C is independent of this pair, so κ_{ij|C}=1.

2. For the missing pair u,v in H, if some w∈W is absent from C, retain only the coefficients on u→w and w→v, setting both to 1. Then Z_u=ε_u, Z_w=ε_u+ε_w, and Z_v=ε_u+ε_w+ε_v. All conditioned variables are independent of this triple, so κ_{uv|C}=1.

3. For the missing pair u,v in H, if C contains some r∈R, retain only the coefficients on u→r and v→r, setting both to 1. Then Z_u and Z_v are independent standard normals and Z_r=Z_u+Z_v+ε_r. All other conditioned variables are independent of these three. The displayed conditional covariance formula gives κ_{uv|C}=0-1·(1/3)·1=-1/3.

Section 4 shows that cases 2 and 3 cover every conditioning set that d-connects the missing pair. Every other d-connected pair lies in S and is adjacent, so case 1 covers it. Zero coefficients in these auxiliary witnesses are allowed: the witnesses need not themselves be faithful; they establish only that particular polynomials are nonzero polynomials.

There are finitely many pairs and conditioning sets. The product of their nonzero numerator polynomials is a nonzero polynomial. For completeness, a product of nonzero real polynomials is nonzero by its leading monomials, and a nonzero real polynomial has a point where it is nonzero: induct on the number of variables, choose values making a nonzero coefficient polynomial nonzero, and then avoid the finitely many roots of the resulting nonzero univariate polynomial. Choose one coefficient vector at which this finite product is nonzero. At that vector, every graphically d-connected pair is conditionally dependent for every relevant C.

It remains to verify the graphically required independences. Outside S, the variables are mutually independent noises independent of the entire clique vector. They remain independent of other unconditioned variables when any disjoint coordinates are conditioned on. For F, these are all its graphical independences, as shown in Section 1.

For H, the only additional separated pair inside S is u,v given a C with C∩S=W. The equation for v is

Z_v=sum_{w∈W} β_wv Z_w+ε_v.

Since u and W precede v, ε_v is independent of (Z_u,Z_W). Conditional on Z_W, the remaining randomness in Z_v is therefore independent of Z_u. Conditioning additionally on isolated outside variables does not change this. Thus the required conditional independence holds for every coefficient vector.

Finally, the set-valued graphical separations were classified in Section 4: either one endpoint set consists only of isolated vertices, or their clique parts are the singletons u and v separated by W. The established product independence and the last conditional independence give the corresponding vector CIs. Conversely, a graphically active path between endpoint sets has some d-connected endpoint pair, whose conditional covariance is nonzero at the chosen vector. Vector conditional independence would imply conditional independence of that pair, a contradiction.

The chosen Gaussian distribution therefore has exactly the d-separation relations of D and also the displayed factorizing density. It is Markov and faithful. This proves the existence of P_0 and every required P_{H_W}, completing all obligations for the public theorem.

## Relation to the General Source Argument

The general clique-order extension and the general external edge-deletion implication remain unproved in the supplied source reconstruction. They are not used as premises in this proof: their required special cases have been explicitly derived. The source-level records may therefore retain an incomplete general-proof assessment without implying any remaining gap in this complete proof of the frozen public worst-case target.
