# Problem

## Setup

Let `G=(V,E)` be a finite undirected unweighted graph, with neighborhood `N(u)` for each vertex. Fix a nonempty initial active set `S_0 subseteq V`, an integer threshold `kappa>=1`, and an integer horizon `ell>=1`. A threshold cascade produces nested sets
`S_0 subseteq S_1 subseteq ... subseteq S_ell subseteq V`.
For every time `t=1,...,ell` and every vertex `w in S_t \ S_{t-1}`, it satisfies
`|N(w) intersect S_{t-1}| >= kappa`.
The cascade may stop before time `ell` if no eligible vertex remains. For an activated vertex define `T(w)=min{t in {0,...,ell}:w in S_t}`, and let `H=G[S_ell]` be the induced activated subgraph. Let `R_eff^H(S_0,w)` denote effective resistance between `w` and the terminal obtained by contracting all vertices of `S_0` (unit edge resistances).

## Task

Prove that for every `u in S_ell \ S_0`, the graph `H` contains `kappa` pairwise edge-disjoint paths joining `u` to `S_0`, each of length at most `T(u)`, and consequently
`R_eff^H(S_0,u) <= T(u)/kappa <= ell/kappa`.
