# Problem

## Setup

Fix an integer d≥1. Let ρ∈C¹(ℝᵈ) be a probability density with full support. Consider a nonexplosive autonomous Itô diffusion

dXₜ=b(Xₜ)dt+σ(Xₜ)dBₜ,    a(x):=σ(x)σ(x)ᵀ,

with generator

ℒf(x)=b(x)·∇f(x)+(1/2)∑ᵢ,ⱼ aᵢⱼ(x)∂ᵢⱼf(x).

Assume σ is continuous, b∈C_b¹(ℝᵈ,ℝᵈ), a∈C_b¹(ℝᵈ,ℝᵈˣᵈ), and a(x) is positive definite for every x. Here C_b¹ means that the function and its continuous first derivatives are bounded.

Assume also that the diffusion has a stationary C¹ probability density p with full support and that there is a skew-symmetric c∈C_b¹(ℝᵈ,ℝᵈˣᵈ) satisfying, for every i and x,

2p(x)bᵢ(x)=∑ⱼ ∂ⱼ[p(x)(aⱼᵢ(x)+cⱼᵢ(x))].

For a continuously differentiable vector field g:ℝᵈ→ℝᵈ, define

(𝒯g)(x):=2b(x)·g(x)+∑ᵢ,ⱼ aᵢⱼ(x)∂ⱼgᵢ(x).

Let k be a bounded scalar positive-definite kernel whose mixed derivatives through order two in each argument are bounded and continuous. Let ℋ be its scalar RKHS, let ℋᵈ be the vector RKHS for K(x,y)=k(x,y)I_d, and suppose C_c^∞(ℝᵈ)⊆ℋ. Write ℋ₁ᵈ={g∈ℋᵈ:‖g‖_{ℋᵈ}≤1}, and define

Δ(ρ):=(sup_{g∈ℋ₁ᵈ} 𝔼_{X∼ρ}[(𝒯g)(X)])².

The density ρ is called stationary if X₀∼ρ implies Xₜ∼ρ for every t≥0. The diffusion is reversible with respect to ρ if its Markov semigroup (Pₜ)ₜ₍ₜ≥₀₎ satisfies

∫fPₜg dρ=∫gPₜf dρ

for all bounded suitable f,g and every t≥0.

## Task

Prove the equivalence

Δ(ρ)=0  ⇔  ρ is stationary and the diffusion is reversible with respect to ρ.
