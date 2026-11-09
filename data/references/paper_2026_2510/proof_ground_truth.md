# Reference Proof

## Proof Structure

First establish the conditional counting fact and the constant-observation conditioning relation. Then show that interventions recover each hidden tree or bipartite graph, apply counting to the distinct answer strings, and give conditional prefix-free encodings for the upper bounds. Finally encode an arbitrary finite-schema bounded-indegree SCM, derive the binomial estimate, and verify that suitable fixed libraries contain the lower-bound constructions.

## Complete Proof

### step_001: Conditional counting

Fix an auxiliary input w. For every integer k>=0, there are at most 2^k-1 binary programs of length less than k, hence at most that many distinct outputs with K(z|w)<k. For N distinct strings and any real c>=0, put t=log_2 N-c-1. If t<=0, no string has complexity below t. Otherwise the number with K(z|w)<t is at most 2^{ceil(t)}-1<=2^{t+1}=N2^{-c}. Thus at least a 1-2^{-c} fraction satisfies K(z|w)>=log_2 N-c-1. Similarly, taking k=floor(log_2 N) shows that at least one string has complexity at least log_2 N-1. The constants are uniform in w,N,c.

### step_002: Constant-observation conditioning

Ignoring an extra auxiliary input gives K(I|P,n)<=K(I|n)+O(1). Conversely, suppose P is computed from n by a program of uniformly bounded length. A fixed interpreter can run that program and then a program for I given (P,n), so K(I|n)<=K(I|P,n)+O(1). Prefix-free program composition has only constant overhead here because the observation program has bounded length. Consequently, in either displayed family, Delta_{2|1}(M)=DL_2(M) plus or minus O(1), uniformly over the family and n.

### step_003: Tree observations and recovery

In M_T every variable equals the root noise before intervention. Therefore the observation is P*, with probabilities 1/2 at 0^n and 1^n and zero elsewhere. One fixed program outputs its rational probability table given n, establishing DL_1=O(1).

Let D_T(i) contain i and all its descendants. Under do(X_i=0), every coordinate in D_T(i) is deterministically zero by propagation along the tree. If j is outside D_T(i), the root-to-j path avoids i, so its equations are unchanged and X_j still equals the Bernoulli(1/2) root. Hence D_T(i) is exactly the set of coordinates having zero marginal probability equal to 1 in this intervention distribution.

These sets reconstruct the tree. The root is the unique i with D_T(i)=[n]. For a nonroot vertex v, the vertices u!=v with v in D_T(u) are precisely its strict ancestors. Their descendant sets form a strictly nested chain, and the smallest is the set belonging to the parent of v. This recovers every parent and proves that T maps injectively to Int_1(M_T).

### step_004: Tree counting and encoding

For n>=2, rooted labeled trees are in bijection with a root label and a Prüfer sequence of n-2 labels from [n]. For completeness, the sequence is obtained by repeatedly deleting the smallest labeled leaf and recording its neighbor until two vertices remain. To decode a sequence, give each label initial degree one plus its number of occurrences. At each step connect the smallest label of degree one to the next sequence label, remove that leaf, and decrement the neighbor's degree; finally connect the two remaining labels. At each step a degree-one label exists because the remaining occurrence counts have total two less than the number of remaining vertices. The construction stays connected and acyclic: each removed vertex is attached once to a remaining vertex, followed by the final edge. In the resulting tree, the labels absent from the remaining sequence are exactly its leaves, so the same smallest-leaf rule reverses the construction. The two procedures are therefore inverse. The number of rooted trees is n*n^{n-2}=n^{n-1}. For n=1 there is one tree.

By injectivity, there are N=n^{n-1} distinct intervention answers for fixed n. Conditional counting with w=n, followed by step_002, yields a lower bound (n-1)log_2 n-c-O(1) with probability at least 1-2^{-c}. This implies the stated bound with O(log n) remainder, with constants independent of c.

For the upper bound, encode the root and entire Prüfer sequence as one mixed-radix integer in a set of size n^{n-1}, rather than rounding the bit length of each symbol separately. This takes ceil((n-1)log_2 n) bits. Given n, all payloads have the same known length, so they form a conditional prefix-free code; a fixed interpreter adds O(1) bits. It decodes the tree and computes all intervention distributions by evaluating the two root-noise outcomes. This gives the requested DL_2 upper bound. The n=1 model is handled by a fixed program. As usual, the displayed O(log n) bounds are asymptotic; a remainder O(1+log n) also covers the isolated n=1 case.

### step_005: Bipartite observations and recovery

Use the fixed labeling r=1, a_i=i+1, b_j=m+1+j. Without intervention, all A variables equal X_r. Each B equation also equals X_r: the explicit root input forces zero when the root is zero, and every input is one when the root is one, including the empty-neighborhood case. Thus every graph has observation P* and DL_1=O(1).

Under do(X_{a_i}=0), the root remains Bernoulli(1/2), and every other A variable still equals it. If (a_i,b_j) is an edge, the forced zero is an AND input and X_{b_j}=0 deterministically. If it is not an edge, every included A input equals X_r, so X_{b_j}=X_r, also when the neighborhood is empty. The zero marginal is therefore 1 for an edge and 1/2 for a non-edge. These marginals recover every adjacency entry, proving injectivity of G maps to Int_1(M_G). This uses the corrected b_j indexing recorded for theory_011.

### step_006: Bipartite counting and encoding

There are 2^{m^2} graphs, because each of the m^2 potential edges is independently present or absent under the uniform distribution. Injectivity and conditional counting give Delta_{2|1}(M_G)>=m^2-c-O(1) with probability at least 1-2^{-c}, by step_002. This implies the requested O(log n) version. Taking c=m^2/2 gives an Omega(n^2) lower bound except with probability exp(-Omega(n^2)) as m grows.

For the upper bound, the adjacency matrix has exactly m^2 bits. Given n, the decoder knows m and the fixed vertex labeling, and hence knows the payload length. Its fixed-length payload code is prefix-free for each auxiliary n. A fixed interpreter reconstructs the equations and evaluates the two root-noise outcomes under each intervention. Thus DL_2(M_G)<=m^2+O(1), without an additional self-delimiting length charge. For m=0 the family contains only the single root model, and a fixed program suffices.

### step_007: General finite-schema upper bound

Fix Gamma and Pi independently of n,d. Every chosen schema has one fixed algorithm accepting its arity, its parent-input tuple in label order, and a compatible noise value. No additional per-node gate parameter or input-order parameter is present.

For n>=2 and 1<=d<=n-1, put S=sum_{k=0}^d binom(n-1,k). Encode d in ceil(log_2 n) bits. Encode a topological ordering as n labels, costing n ceil(log_2 n) bits. For each node, enumerate all subsets of [n] excluding that node of cardinality at most d and encode the rank of its parent set in ceil(log_2 S) bits. The arity is the cardinality of the decoded set, so it needs no separate code. Finite gate and noise choices cost at most C_{Gamma,Pi} bits per node. Rounding the parent-set ranks contributes less than n additional bits.

For a fixed n, d has a fixed-length field. For each decoded d all remaining fields have fixed lengths, so the valid descriptions form a conditional prefix-free code. A fixed interpreter adds only a library-dependent constant. Invalid descriptions may be rejected. These components give

DL_2(M)<=C_{Gamma,Pi}n+n log_2 S+O(n log n),

where the constants are uniform in d and M. The description of the fixed libraries and interpreter is absorbed into the library-dependent constant.

The decoder can compute the answer exactly. Each local noise has explicitly known finite support and rational weights. Enumerate the Cartesian product of these supports, multiply the independent rational weights, and evaluate the computable equations in topological order. For each hard intervention, replace just the relevant equation by its constant and repeat. Summing weights for each binary outcome yields exact rational joint distributions, which the decoder writes in the fixed canonical encoding. No runtime bound is needed.

To derive the asymptotic estimate, write N=n-1. For 1<=k<=N, integrating log over [1,k] gives k!>=(k/e)^k, so binom(N,k)<=N^k/k!<=(eN/k)^k. The function x log(eN/x) is nondecreasing on 0<x<=N because its derivative is log(N/x)>=0. Consequently, for every 1<=k<=d, binom(N,k)<=(eN/d)^d; the k=0 term satisfies the same bound. Therefore

S<=(d+1)(eN/d)^d.

Taking base-2 logarithms, using log_2(d+1)<=d and N<=n, gives log_2 S=O(d log_2(en/d)) uniformly for 1<=d<=n-1. Finally, ignoring Obs in the auxiliary input gives Delta_{2|1}(M)<=DL_2(M)+O(1). This proves both requested general bounds.

### Order optimality

The witness families lie in suitable fixed finite libraries. Explicitly, use a schema whose zero-arity component returns the local binary noise and whose positive-arity components copy the first parent; add an AND schema that ignores its noise and takes the conjunction of all parent inputs. Use the fixed noise library consisting of Bernoulli(1/2) and the point mass at zero. These are uniformly computable schemas and finite-support rational noises. The tree models use indegree at most one, while the bipartite models use indegree at most m+1, which is Theta(n) for growing m.

For d=1 the general upper bound is O(n log n), and taking c to be a fixed positive fraction of (n-1)log_2 n in the tree probability bound gives matching lower order with probability tending to one. For the bipartite models the dense upper bound is O(n^2), matched by step_006. This is order optimality across the relevant finite-schema classes with suitable witness libraries, not a claim that every arbitrary fixed library admits these constructions.

## Obligation Closure

Conditional counting and conditioning are derived in steps 001-002. Intervention injectivity is derived in steps 003 and 005. Tree cardinality and its encoding are justified by the mutually inverse procedures in step 004. Graph cardinality and its conditional prefix-free encoding are established in step 006. General code framing, exact simulation, the binomial estimate, and the gap reduction are derived in step 007. Fixed-library membership and order matching are verified in the final section. No theorem-critical proof obligation remains unresolved.
