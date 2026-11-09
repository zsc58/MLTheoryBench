# Reference Proof

## Proof obligations

We establish: (1) valid candidate generation and distinctness; (2) sound structural bounds and the precise, conservative interpretation of the completion intervals; (3) safe deletion with M distinct replacements for an actual outside clustering; (4) preservation through all bottom-up pruning decisions; and (5) the root cardinality and ranking conclusion, including ties and empty feasible families. All obligations are proved below. No external theorem is needed.

## 1. Candidate generation

Let Z(C) be the finite set of flat clusterings of the subtree rooted at C. Every member is either {C}, or, when C is internal and not selected, the union of one member of Z(D) for each child D. Child subtrees are disjoint, so restriction to the children uniquely recovers the chosen tuple. Thus distinct tuples produce distinct clusterings, and none of these unions equals {C}. Scores and cardinalities add across children.

Write G(C) for the candidates actually generated from retained child sets, together with {C}. Every member of G(C), and hence of R(C), is a valid subtree clustering. Inductively, a generated candidate also respects all prior retention requirements within its subtree wherever it does not select an ancestor of the previously processed node.

## 2. Structural bounds and actual completions

An outside clustering for C consists of a flat clustering in every sibling subtree encountered on the path from C to the root. Such an outside clustering can be joined to any member of Z(C), and every full-tree clustering with no selected strict ancestor of C has this form.

Each of these sibling subtrees contributes at least one selected node. Selecting its root attains this minimum. Summing over the path gives LB(root)=0 and LB(C)=LB(parent(C))+nu(C). Every selected node covers at least one leaf, and selected nodes cover disjoint leaf sets, so the maximum outside count is the number of leaves outside C. Selecting those leaves attains UB(C)=leaf_no(root)-leaf_no(C). These arguments also establish 0<=LB(C)<=UB(C).

Fix an actual outside clustering w and put t=|w|. Then LB(C)<=t<=UB(C), and for any z in Z(C),

z union w is feasible if and only if k_min<=|z|+t<=k_max, if and only if t belongs to I_C(z).

In particular, an empty interval rules out every actual feasible completion. Nonemptiness is equivalent to the two inequalities |z|+LB(C)<=k_max and |z|+UB(C)>=k_min. However, nonemptiness need not imply actual extendability: not every integer between LB and UB must be attainable.

For example, let the root have a leaf child A and a child B with three leaf children. Outside A the available counts are 1 and 3. With k_min=k_max=3, the candidate {A} has I_A({A})={2}, but no feasible completion. This corrects the source's overstated sufficiency assertion without changing the pruning algorithm. Our proof never constructs an outside clustering merely from interval membership.

## 3. A finite elimination invariant

Let F be the set of all feasible full-tree clusterings. Conceptually maintain a surviving family H, initially F, while executing the prescribed bottom-up algorithm. Say a full clustering is active at C if it selects no strict ancestor of C. Its restriction to C's subtree is then a member of Z(C). A clustering selecting a strict ancestor of C is unaffected by processing C.

At each processed node, delete from H the active full clusterings whose local restriction is discarded. A previously processed node imposes the requirement that an active restriction there belong to that node's retained set.

Before C is processed, every surviving full clustering active at C has its restriction in G(C). Indeed, either it selects C, giving {C}, or it selects no C and is active at each child. Since the children have already been processed, their restrictions are retained. This also explains why pruning through generated candidates accounts for every survivor that needs a decision at C.

For each real threshold a, define

N_H(a)=|{x in H : q(x)>=a}|.

We show that every deletion preserves min(M,N_H(a)) for every a. Consider a generated local candidate z that is discarded.

If I_C(z) is empty, there is no surviving feasible full clustering using z, by Section 2, so no deletion occurs.

Otherwise, for every t in I_C(z) there are M distinct already retained candidates y_1,...,y_M at C with t in I_C(y_j) and q(y_j)>=q(z). The numerical comparison is non-strict, including when candidates tie.

Take a survivor x=z union w that is being deleted. Its outside count t=|w| belongs to I_C(z). The full clusterings

x_j=y_j union w, for j=1,...,M,

are feasible by Section 2 and satisfy q(x_j)>=q(x). They are distinct because their restrictions to C are distinct; they also differ from x. They satisfy all previously processed requirements outside C because w is unchanged. Inside C, they satisfy those requirements because each y_j is a generated candidate assembled from retained child candidates, or selects C and thereby makes descendant requirements inactive. Finally, they are not removed by the present pruning at C because each y_j is retained.

Thus, immediately before and after deleting x, these M alternative survivors remain. If q(x)<a, its deletion does not change N_H(a). If q(x)>=a, at least M alternatives still have score at least a, so the truncated count min(M,N_H(a)) again does not change. Apply this argument one full clustering at a time to all deletions associated with z and then to all discarded candidates at C.

The tree and all candidate families are finite, so the invariant composes through all nodes. Later deletions need not preserve the particular alternatives just exhibited; each later deletion separately preserves the same truncated counts. This supplies the multiplicity argument that a single non-decreasing replacement would not establish.

Consequently, after all processing, the final surviving family H_final satisfies

min(M,N_H_final(a))=min(M,N_F(a)) for every real a.

## 4. Identification at the root

At the root C_0, LB(C_0)=UB(C_0)=0. A generated candidate is feasible exactly when its interval is {0}; otherwise its interval is empty. The scan therefore retains exactly the first M feasible generated candidates, or all of them if fewer exist. In particular, |R(C_0)|<=M.

After root processing, H_final=R(C_0). Every surviving full clustering must be retained at the root. Conversely, every retained root candidate is feasible and was generated from retained child candidates, so it satisfies all earlier retention requirements and belongs to H_final.

If F is empty, validity of the retained root candidates immediately gives R(C_0)=empty. Otherwise choose a real threshold below all scores in the finite family F. The invariant and |R(C_0)|<=M imply

|R(C_0)|=min(M,|F|).

For every threshold a, it further gives

N_R(C_0)(a)=min(M,N_F(a)).

If |F|<M, the inclusion R(C_0) subseteq F and equality of cardinalities imply R(C_0)=F. If |F|>=M and an omitted clustering x had score strictly greater than a returned clustering y, use a=q(x). At most M-1 returned clusterings meet this threshold. Since x is an additional feasible clustering meeting it, the displayed threshold equality is impossible. Hence every returned clustering has score at least that of every omitted clustering.

Ordering the returned distinct clusterings by nonincreasing score gives a top-M list. Equal-score alternatives may be chosen arbitrarily; no particular global tie order or strict improvement from tie-breaking is asserted.

## Source-local and boundary clarifications

The completion intervals are conservative numerical tests, not exact sets of attainable outside counts. Retained intervals can cover a particular count more than M times, because a candidate may be retained for a different count. Neither exact attainability nor exact per-count retention is used.

The mathematical procedure applies pruning at every node, including leaves. The source pseudocode's leaf `continue` must be removed so that initialized leaf candidates reach the common pruning stage; otherwise a root consisting of an infeasible singleton is incorrectly returned. The public procedure already includes the correct all-node treatment.

The proof uses no binary-branching, balanced-tree, nonnegative-score, positive-k_min, or existence-of-a-feasible-solution assumption. It covers one-node trees, unary nodes, arbitrary finite branching, all allowed integer count bounds, and every M>=1.
