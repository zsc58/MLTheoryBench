# Problem

## Setup

Let G=(V,E) be a finite directed graph with n=|V|. Fix an integer t with 1<=t<=n. Write u reaches v if there is a directed path from u to v, allowing a path of length zero; in particular, every vertex reaches itself. The underlying undirected graph is obtained by forgetting edge orientations.

A tree decomposition of an undirected graph is a tree T with bags (V_x)_{x in V(T)} such that every vertex occurs in some bag, the endpoints of every edge occur together in a bag, and the bags containing any fixed vertex induce a connected subtree. Its width is max_x |V_x|-1, and the treewidth tw(G) is the minimum width over all decompositions of the underlying undirected graph.

A d-dimensional reachability embedding consists of maps a,b:V->R^d satisfying <a_u,b_v> > 0 exactly when u reaches v.

Use standard asymptotic notation with universal constants.

## Task

Prove the following integrated theorem. There is a universal constant C such that every directed graph on n vertices whose underlying undirected graph has treewidth at most t admits a reachability embedding of dimension at most C t log(n+1). Conversely, for integers 2<=t<=n/2, there exists an n-vertex directed acyclic graph whose underlying undirected graph has treewidth at most t and for which every reachability embedding has dimension at least c t/log(n/t), for a universal constant c>0.
