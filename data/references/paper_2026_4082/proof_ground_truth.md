# Reference Proof

## Proof Structure

The upper bound recursively decomposes the underlying undirected graph into balanced sides and a small separator. The child embeddings share one coordinate block; additional coordinates suppress cross-side false positives and certify paths through the separator. The lower bound counts distinct reachability matrices of bounded-span bipartite DAGs and compares this count with the standard count of low-sign-rank matrices.

Throughout, paths of length zero are allowed. All logarithms in this proof are natural; changing the base changes only universal constants.

## 1. Balanced separators and component grouping

We first justify the separator guarantee used by the source directly from a tree decomposition. Let H have m vertices and a tree decomposition with bags of size at most t+1. We may take its decomposition tree to be finite: choose finitely many bags witnessing vertex and edge coverage and restrict to the finite subtree joining them.

For a decomposition node x with bag V_x, every vertex outside V_x has all its occurrence bags in a unique component of the decomposition tree minus x. Assign that vertex to that component. These groups partition V(H) minus V_x, and no graph edge joins different groups, by the edge-coverage and connected-occurrence properties.

If all these groups have size at most (m-|V_x|)/2, take S=V_x. Otherwise mark the unique neighboring node toward the group of size greater than (m-|V_x|)/2. Each node has at most one marked outgoing edge. Following marked edges in a finite tree either stops at a node with no outgoing mark or produces two adjacent nodes marking toward each other. The first outcome supplies the desired separator bag.

For the second outcome, let the adjacent bags be P and Q and put I=P intersect Q. Removing their tree edge partitions every graph vertex outside I into two sets X and Y, according to which side contains its occurrence bags; let X be on Q's side. There are no graph edges between X and Y. Put p=|P minus I| and q=|Q minus I|. The group at P toward Q is X, and the group at Q toward P is Y. Mutual marking therefore implies

|X| > (|X|+|Y|-p)/2,

|Y| > (|X|+|Y|-q)/2.

If |X|≥|Y|, the second inequality gives |X|-|Y|<q. Delete I and any |X|-|Y| vertices of X. The separator has size at most |I|+q=|Q|≤t+1, and the two remaining sides each have |Y| vertices. Each connected component is contained in one side, hence has at most half the total number of remaining vertices. If |Y|>|X|, use the symmetric argument with P. This proves the separator guarantee, including cases in which no vertices remain.

Now choose such an S and put N=m-|S|. If N=0, take A=B=empty. Otherwise let the component sizes of H-S be x_1,...,x_k, each at most N/2. If some component has size at least N/3, place it alone in A; its size is at most N/2 and the remaining total is at most 2N/3. If every component has size less than N/3, accumulate components until their total first reaches N/3. That total is less than 2N/3, and its complement is at most 2N/3. Thus in all cases

V(H) minus S = A disjoint union B,

|A|,|B|≤2m/3,

and there is no undirected edge between A and B.

Finally, intersecting every bag with A gives a tree decomposition of H[A] of no larger width; the same holds for B. This explicitly verifies the subgraph-monotonicity hypothesis needed for recursion.

## 2. Recursive reachability embedding

Fix t≥1. Let f(m) be the maximum minimum embedding dimension over directed graphs with at most m vertices and underlying treewidth at most t. This quantity is finite: any m by m reachability sign matrix has a factorization in dimension at most m. Set f(0)=0; a singleton graph has a one-dimensional embedding with positive self-score.

For a graph H on m≥2 vertices, use the partition A,B,S above. Recursively embed H[A] and H[B]. Pad the shorter child embedding with zeros so that both have dimension

q≤f(floor(2m/3)).

Place both child embeddings in the SAME q coordinates: use the A vectors on A, the B vectors on B, and zero vectors on S. Denote these vectors by a_u^rec,b_v^rec and their products by R_uv. Within either side, R_uv is positive exactly for reachability inside that induced subgraph. If an endpoint lies in S, R_uv=0. Cross-side products are unrestricted; in particular, they need not vanish.

Since H is finite, the number

C_H=max_{u,v}|R_uv|

is finite. Choose M_1>C_H and M_2>M_1+C_H.

Add two separation coordinates. Give a_u^sep the values (1,0) on A, (0,1) on B, and (0,0) on S. Give b_v^sep the values (0,-M_1) on A, (-M_1,0) on B, and (0,0) on S. Their inner product is -M_1 on opposite-side pairs and zero otherwise.

For each s in S, add one connection coordinate. Give its left value M_2 when u reaches s in H and zero otherwise; give its right value 1 when s reaches v in H and zero otherwise. The sum K_uv of connection products is nonnegative. It vanishes unless some separator vertex certifies reachability from u to v, and it is at least M_2 whenever such a vertex exists. Reflexive reachability permits a separator witness to equal either endpoint.

Concatenate the recursive, separation, and connection blocks. The resulting score is R_uv plus the separation contribution plus K_uv.

If u reaches v through a vertex of S, the score is at least -C_H-M_1+M_2>0. This includes all reachable pairs having an endpoint in S.

If u reaches v but no separator vertex certifies this, a directed path avoids S. Because no edge joins A and B, both endpoints and that path lie in one induced child graph. The recursive score is positive, the separation contribution is zero, and the connection contribution is zero.

If u does not reach v, K_uv=0. For opposite-side pairs, the score is at most C_H-M_1<0. For same-side pairs, the induced child graph also has no such path, so the recursive score is nonpositive and the separation contribution is zero. If either endpoint lies in S, both the recursive and separation contributions vanish, giving score zero. Thus no nonreachable pair has positive score.

This establishes the required equivalence for every ordered pair. The construction uses q+2+|S| coordinates, so

f(m)≤f(floor(2m/3))+t+3.

The recursion reaches m≤1 in O(log(m+1)) levels. Because t≥1, its total dimension is O(t log(m+1)), with a universal constant. Taking m=n proves the upper bound, including n=1 and edgeless graphs under the positive budget t.

## 3. A large family of bounded-treewidth DAGs

Fix integers 2≤t≤n/2. On vertices 1,...,n allow an edge u to v exactly when u is odd, v is even, u<v, and v-u≤t. Every subset of the allowed edges defines a graph in the family.

All edges go from odd vertices to even vertices, and even vertices have no outgoing edges. Thus each graph is a DAG, and every positive-length directed path has length one. Distinct subsets of allowed edges consequently give distinct reachability sign matrices. The diagonal is positive by the fixed reflexive convention and does not affect this injectivity.

For 1≤i≤n, let

X_i={i,i+1,...,min(n,i+t)}.

These bags form a path decomposition of the underlying graph. Every vertex v belongs to X_v. Every allowed edge (u,v) has both endpoints in X_u. The bags containing v have consecutive indices max(1,v-t) through v. Every bag has size at most t+1, so the treewidth is at most t.

To count allowed edges without discarding terminal effects, put r=ceil(t/2). The allowed spans are 2j-1 for 1≤j≤r. For span 2j-1, the odd starting vertices number ceil((n-(2j-1))/2). Hence the number N of allowed edges satisfies

N=sum_{j=1}^r ceil((n-(2j-1))/2)

≥sum_{j=1}^r (n-(2j-1))/2

=r(n-r)/2

≥nt/8.

Here r≥t/2 and r≤n/2; the latter holds even throughout 1≤t<n. Therefore the family contains at least 2^{nt/8} distinct reachability matrices. The larger constant nt/4 asserted in the source is unnecessary and is not generally correct.

## 4. Counting representable matrices and inverting the bound

The audited standard-independent input is the sign-rank counting bound cited in the source: for integers 1≤s≤n/2, the number of n by n strict sign patterns realizable by real matrices of rank at most s is at most

exp(K s n log(n/s))

for a universal constant K. A strict sign pattern uses positive entries for +1 and negative entries for -1. This is sufficient even though reachability embeddings permit zero scores on negative entries.

Indeed, if an embedding has dimension d, its score matrix R=AB^T has rank at most d. Its positive entries form a nonempty finite set because its diagonal is positive. Choose epsilon smaller than their minimum. Then R-epsilon J, where J is the all-ones matrix, is strictly positive at the positive entries of R and strictly negative at all its nonpositive entries. Its rank is at most d+1. Thus the needed reachability patterns admit strict realizations with only a one-rank overhead.

Let D be the maximum, over the finite graph family, of the minimum embedding dimension. The maximum is attained, and D≥1. If D>n/4, then, since t≤n/2 and log(n/t)≥log 2,

D>n/4≥t/2≥(log 2)t/(2 log(n/t)),

which already proves the conclusion with a universal constant.

Otherwise put s=D+1. Since D≥1, we have s≤2D≤n/2. All hypotheses of the counting input are satisfied. Every graph in the family has an embedding in dimension D after padding, and hence a strict realization of rank at most s. It follows that

2^{nt/8}≤exp(K s n log(n/s))≤exp(2K D n log(n/D)).

Consequently

D log(n/D)≥a t,

where a=(log 2)/(16K)>0 is universal.

For completeness, set L=log(n/t), so L≥log 2. Choose a universal constant c>0 sufficiently small that c≤(log 2)/2 and

c[1+1/e+log(1/c)/log 2]<a.

Such a choice exists because c log(1/c) tends to zero as c tends to zero. Put z_0=c t/L. Then z_0≤t/2≤n/4. The function z log(n/z) is increasing on 0<z≤n/4, since its derivative is log(n/z)-1>0. Moreover,

z_0 log(n/z_0)

=c t[1+log L/L+log(1/c)/L]

≤c t[1+1/e+log(1/c)/log 2]

<a t,

using log L/L≤1/e for L>0. Therefore D<z_0 would contradict D log(n/D)≥a t. Hence D≥c t/log(n/t).

A graph attaining D supplies the required n-vertex DAG. Taking the smaller universal constant from the two cases completes the lower bound.

## Obligation Closure

The separator existence and grouping, induced-width inheritance, recursive coordinate construction, all sign cases, and dimension recurrence are derived above. The graph-family count and path decomposition are also derived. The sole external counting input is a standard-independent result explicitly stated above, with its rank range and strict-sign hypotheses verified. The finite-rank perturbation, high-dimension case, and inversion of the counting inequality are explicit. No unresolved private proof obligation remains.
