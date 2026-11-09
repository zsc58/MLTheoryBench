# Problem

## Setup

Let d and m be positive integers, let [d] = {1,...,d}, and let bar F: R^d -> R^d be any map. For each coordinate block below, use a fixed norm ||.||_c. Let D_1,...,D_m be a partition of [d], meaning the blocks are pairwise disjoint and their union is [d].

A strict decomposition operator T^hard: R^d -> R^d (with respect to this partition) is specified by maps G_i: R^{|D_i|} -> R^{|D_i|} such that
(T^hard(x))_{D_i} = G_i(x_{D_i}) for every x and every i.

For i and u in R^{|D_i|}, define the blockwise variation of the true map by
Delta_i(u) = sup { ||(bar F(x))_{D_i} - (bar F(x'))_{D_i}||_c : x_{D_i}=x'_{D_i}=u }.

An overlapping-read decomposition consists of sets D_i subseteq S_i subseteq [d], where the disjoint owned blocks D_i partition [d], and the sets S_i are read sets. It is compatible with bar F if equality of two states on S_i implies equality of their bar F outputs on D_i; equivalently, there are local maps T_i: R^{|S_i|} -> R^{|D_i|} satisfying T_i(x_{S_i}) = (bar F(x))_{D_i} for every x.

For a compatible overlapping-read decomposition, define the lifted operator tilde T_i: R^d -> R^d by
(tilde T_i(x))_{D_i} = T_i(x_{S_i}), and (tilde T_i(x))_j = x_j for j not in D_i.

## Task

Prove the following integrated theorem.

1. For every block i and every u in R^{|D_i|},

sup_{x:x_{D_i}=u} ||(T^hard(x)-bar F(x))_{D_i}||_c >= Delta_i(u)/2.

2. For every compatible overlapping-read decomposition, with lifts defined above,

(1/m) sum_{i=1}^m tilde T_i(x) = (1-1/m)x + (1/m)bar F(x) for all x in R^d,

and therefore x is a fixed point of the averaged lifted operator if and only if x=bar F(x).
