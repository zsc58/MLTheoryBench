# Problem

## Setup

Let $n$ be a positive integer and write $[n]=\{1,\ldots,n\}$. Let $Q_n$ be the graph on $\{0,1\}^n$ with edges between vectors differing in exactly one coordinate. An instance is an induced subgraph $G$ of $Q_n$, possibly with an empty vertex set. An orientation assigns a direction to every edge; $\operatorname{outdeg}_{H,\phi}(v)$ counts edges of a subgraph $H$ directed out of $v$ by the restriction of $\phi$. A randomized orientation $\Phi$ is a probability distribution on the finite set of deterministic orientations of $G$.

For a coordinate set $S\subseteq[n]$, let $G^S$ be the spanning subgraph containing exactly those edges whose differing coordinate lies in $S$. For any finite graph $H$ with at least one vertex, define
\[
\rho(H)=\max_{\varnothing\ne W\subseteq V(H)}\frac{|E(H[W])|}{|W|},
\]
where $H[W]$ is the subgraph induced by $W$. Set $\rho(H)=0$ when $V(H)=\varnothing$. Define
\[
\operatorname{opt}_S(G)=\min_{\phi\text{ a deterministic orientation of }G}\max_{v\in V(G)}\operatorname{outdeg}_{G^S,\phi}(v),
\]
with the maximum over an empty vertex set interpreted as zero.

For a family $\mathcal S\subseteq 2^{[n]}$, put
\[
\mathcal S_+(G)=\{S\in\mathcal S:E(G^S)\ne\varnothing\}.
\]
When $\mathcal S_+(G)\ne\varnothing$, define the multi-group price by
\[
\operatorname{price}(G,\mathcal S)
=\min_{\Phi\text{ a randomized orientation of }G}
\max_{S\in\mathcal S_+(G)}
\frac{\displaystyle\max_{v\in V(G)}\mathbb E_\Phi[\operatorname{outdeg}_{G^S,\Phi}(v)]}{\operatorname{opt}_S(G)}.
\]
No price is asserted when $\mathcal S_+(G)=\varnothing$.

## Task

Prove the following integrated theorem.

1. (**Lower construction.**) For every pair of integers $n,k\ge2$ with $\binom{k}{2}\le n$, there are an induced subgraph $G\subseteq Q_n$ and $k$ pairwise distinct coordinate groups $S_1,\ldots,S_k\subseteq[n]$ such that $\operatorname{opt}_{S_i}(G)=1$ for every $i$, while every randomized orientation $\Phi$ of $G$ has some index $i$ and vertex $v$ with
\[
\mathbb E_\Phi[\operatorname{outdeg}_{G^{S_i},\Phi}(v)]\ge\frac{k-1}{2}.
\]
Consequently, the worst-case multi-group price over induced subgraphs of $Q_n$ and families of exactly $k$ coordinate groups is at least $(k-1)/2$.

2. (**Universal upper bound.**) For every induced $G\subseteq Q_n$ and every family $\mathcal S\subseteq 2^{[n]}\setminus\{\varnothing\}$, there is one deterministic orientation $\phi$ such that, simultaneously for all $S\in\mathcal S$ and all $v\in V(G)$,
\[
\operatorname{outdeg}_{G^S,\phi}(v)\le2\sqrt n\,\rho(G^S).
\]
Hence, whenever $\mathcal S_+(G)\ne\varnothing$, the multi-group price is at most $2\sqrt n$.
