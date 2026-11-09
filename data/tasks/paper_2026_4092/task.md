# Problem

## Setup

Let T be a finite rooted tree, and work in the noiseless setting. Each node C represents a cluster and has a real locally evaluated quality q(C). Fix an integer M>=1 and integers k_min<=k_max. A flat clustering of the subtree rooted at C is a set z of nodes of that subtree containing exactly one selected node on every root-to-leaf path. Its score is additive: q(z)=sum_{D in z}q(D). A full-tree clustering is feasible when k_min<=|z|<=k_max. Clusterings with different selected node sets are distinct, even when their scores are equal.

For every node C, let leaf_no(C)=1 if C is a leaf and otherwise the sum of the leaf_no values of its children. Let C_0 be the root. Define LB(C_0)=0 and, for a non-root C, let nu(C) be the number of children of parent(C) other than C, and set LB(C)=LB(parent(C))+nu(C). Define UB(C)=leaf_no(C_0)-leaf_no(C).

For a candidate z in the subtree of C, define
ell_C(z)=max{LB(C), k_min-|z|},
u_C(z)=min{UB(C), k_max-|z|},
I_C(z)={t: t is an integer and ell_C(z)<=t<=u_C(z)}.

Define the retained set R(C) recursively bottom-up. Before pruning, form all candidates consisting of (i) the singleton clustering {C}, and (ii) for an internal C, every union of one retained candidate from each child. The score and cardinality of a union are the sums of the child scores and cardinalities. Process these candidates in nonincreasing score order. Retain a candidate z exactly when I_C(z) is nonempty and there exists t in I_C(z) that lies in fewer than M intervals I_C(y) of candidates y already retained at C; otherwise discard it. Ties may be broken arbitrarily but consistently.

## Task

Let F be the set of all feasible full-tree flat clusterings. Prove that R(C_0), ordered by nonincreasing score, is a list of the top M feasible clusterings, or contains all feasible clusterings when fewer than M exist. Precisely, prove that R(C_0) is a subset of F, that |R(C_0)|=min{M,|F|}, and that q(y)>=q(z) for every y in R(C_0) and z in F outside R(C_0). Selection among equal-score alternatives may be arbitrary; no independently prescribed global ordering of tied clusterings is required.
