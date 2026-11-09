# Problem

## Setup

Let A, L, C, and X be standard Borel spaces, and let ν be a σ-finite measure on C. For a measurable map f, let T_f denote pushforward: (T_fλ)(E)=λ(f^{-1}(E)). For a Markov kernel u, write uλ for the measure defined by (uλ)(E)=∫u(E|z)λ(dz).

Fix a Markov kernel b:L→C, a class 𝒬 of Markov kernels q:A→L, and a class 𝒦 of Markov kernels k:C→X. The model class is
\[
\mathcal M=\mathcal Q\times\{b\}\times\mathcal K.
\]
For m=(q,b,k)∈𝓜, write μ=bq, μ_a=μ(·|a), and
\[
P^m(\cdot\mid a)=k\mu_a.
\]
Thus the induced concept-kernel class is {bq:q∈𝒬}.

Let A_obs⊆A_test⊆A be measurable sets, and fix a_0∈A_obs. Two models m,m'∈𝓜 are observed-feature-equivalent when P^m(·|a)=P^{m'}(·|a) for every a∈A_obs.

A transition in Aut_ν(C) is a bimeasurable bijection between two measurable ν-conull subsets of C that preserves ν-null sets in both directions. Transitions are identified when they agree ν-almost everywhere. Pushforward by such a transition, or its inverse, is defined for ν-dominated measures by restriction to the corresponding conull domain.

Assume the following factorization condition on 𝒦. There exist a standard Borel space Z, a collection 𝒢 of bimeasurable embeddings g:C→Z, and a shared Markov kernel h:Z→X such that:

- For every k∈𝒦 there is a g∈𝒢 satisfying
\[
k\lambda=h(T_g\lambda)
\quad\text{for every probability law }\lambda\ll\nu.
\]
- The map ξ↦hξ is injective on
\[
\mathcal S=\{T_g\lambda:g\in\mathcal G,\ \lambda\text{ a probability law on }C,\ \lambda\ll\nu\}.
\]

Here a bimeasurable embedding is an injective measurable map with measurable image and measurable inverse on its image.

Assume also that, for every induced kernel μ=bq and every a∈A, the probability law μ_a has a ν-density p_a satisfying 0<p_a(c)<∞ for ν-almost every c. Define the attribute potential
\[
V_\mu(a,a_0;c)=\log p_a(c)-\log p_{a_0}(c),
\]
understood ν-almost everywhere.

## Task

Prove the following integrated theorem. For any observed-feature-equivalent models m=(q,b,k) and m'=(q',b,k') in 𝓜, with μ=bq and μ'=bq', there exists t∈Aut_ν(C) such that
\[
k'\lambda=k(T_t\lambda)
\quad\text{for every probability law }\lambda\ll\nu,
\qquad
\mu_a=T_t\mu'_a\quad\text{for every }a\in A_{\mathrm{obs}}.
\]
For this t,
\[
P^m(\cdot\mid a)=P^{m'}(\cdot\mid a)
\quad\text{for every }a\in A_{\mathrm{test}}
\]
if and only if
\[
V_{\mu'}(a,a_0;c)=V_\mu(a,a_0;t(c))
\quad\text{for every }a\in A_{\mathrm{test}},\ \nu\text{-almost every }c.
\]

Moreover, suppose there is a fixed map ψ:A→R^d into a finite-dimensional real vector space such that, for every induced kernel μ, there is a measurable map H_μ:C×C→R^d satisfying
\[
V_\mu(a,a_0;c)-V_\mu(a,a_0;c_0)
=\langle\psi(a)-\psi(a_0),H_\mu(c,c_0)\rangle
\]
for every a∈A_test and ν⊗ν-almost every (c,c_0). If ψ(A_test) is contained in the affine hull of ψ(A_obs), then, for the same t, the displayed potential identities hold for every a∈A_test, and consequently feature equivalence extrapolates from A_obs to A_test.
