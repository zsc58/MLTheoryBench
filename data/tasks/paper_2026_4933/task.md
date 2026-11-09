# Problem

## Setup

Let V be a finite vertex set, with p=|V|. A directed acyclic graph (DAG) on V is a directed graph with no directed cycle. Its skeleton is obtained by forgetting all arrowheads.

For pairwise disjoint sets A,B,C⊆V, define d-separation as follows. An internal vertex on a path is a collider when both path edges incident to it point toward it. A path is active given C when every internal non-collider lies outside C and every internal collider either belongs to C or has a descendant in C. Here a descendant is a vertex reachable by a directed path. The sets A and B are d-separated by C if there is no active path between a vertex of A and a vertex of B.

Two DAGs are Markov equivalent when they have the same d-separation relations. The essential graph E(G) of a DAG G has the same skeleton as G. An edge is directed in E(G) exactly when its orientation is the same in every DAG Markov equivalent to G; otherwise it is undirected. An undirected clique in E(G) is a set of vertices with an undirected edge between every two distinct members. Write s(G) for its maximum size. Singletons count as cliques, and s(G)=0 when V is empty.

Associate a random variable with each vertex. The unknown joint distribution P is Markov and faithful to an unknown DAG G on V: for every pairwise disjoint A,B,C⊆V, the random vectors indexed by A and B are conditionally independent given the vector indexed by C if and only if G d-separates A and B given C. A conditional-independence (CI) oracle returns this exact Boolean answer. Empty endpoint sets are allowed and give the vacuous independence answer.

A constraint-based discovery procedure receives V and accesses the unknown distribution only through this oracle. Each query consists of one triple (A,B,C), and counts as one test, including when A or B contains several vertices. Queries and the final output may depend on previous queries and answers. Internal randomness, if used, is independent of the unknown instance. An exact algorithm must terminate and output E(G) for every admissible DAG and distribution; for a randomized algorithm this correctness requirement holds with probability one for each instance. The query bound below is a worst-case bound, not a bounded-error or expected-query assertion.

The algorithm must be correct over all DAGs on V. In particular, s(G) is a parameter used to describe its complexity, not a promised restriction supplied to the algorithm; competing inputs are not required to have the same clique size.

## Task

For each integer s with 1≤s≤p, prove that every exact constraint-based discovery algorithm has an admissible input G on V with s(G)=s on which its worst-case number of CI tests is at least

2^s-s-1.

For randomized algorithms, worst-case query cost also ranges over their internal randomness. When V is empty, use s=0, for which the asserted lower bound is zero. The bound is also zero for s=1. Explain why the bound is 2^{Omega(s)} as s tends to infinity.

Equivalently, any procedure attempting to identify the essential graph using fewer than 2^s-s-1 tests on every input of parameter s must have a transcript compatible with two distinct Markov-equivalence classes on V, at least one having parameter s. Each class must be compatible with a Markov and faithful distribution. The alternative class need not have parameter s.
