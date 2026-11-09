# Problem

## Setup

Let M and N be smooth (C^∞), compact, d-dimensional Riemannian manifolds with fixed Riemannian metrics. Write μ_M and μ_N for their Riemannian volume measures. Fix an integer m>2d+1.

Define
\[
\mathcal P^1_+(M)=\left\{\rho\in C^1(M,\mathbb R):\rho(x)>0\text{ for every }x\in M,\quad\int_M\rho\,d\mu_M=1\right\}.
\]
Equip this space with the subspace C^1 topology and its m-fold product with the product topology. A subset of a topological space is generic if it is open and dense.

A C^1 map Y:M→R^k is an embedding if it is injective, its differential is injective at every point, and it is a homeomorphism onto its image.

Let Diff^1(M,N) denote the bijective C^1 maps M→N whose inverses are C^1, and let 𝔛^1(M) denote the C^1 vector fields on M. For a measurable map f:M→N and ρ∈P^1_+(M), write f_#ρ for the pushforward of the probability measure ρ dμ_M; thus
\[
(f_\#\rho)(B)=\int_{f^{-1}(B)}\rho\,d\mu_M
\]
for every Borel set B⊆N. For a C^1 diffeomorphism, its density relative to μ_N is given by the change-of-variables formula. For a C^1 vector field v, div(ρv) denotes the Riemannian divergence on M.

## Task

Prove that there exists a generic set D⊆P^1_+(M)^m such that every ρ=(ρ_1,...,ρ_m)∈D has both properties:

1. For all f,g∈Diff^1(M,N), if f_#ρ_j=g_#ρ_j as measures for every j=1,...,m, then f=g.
2. For all v,w∈𝔛^1(M), if div(ρ_j v)=div(ρ_j w) pointwise on M for every j=1,...,m, then v=w.
