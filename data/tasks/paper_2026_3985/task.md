# Problem

## Setup

Fix an integer d≥1. Let P₂(Rᵈ) denote the Borel probability measures on Rᵈ with finite second moment, and let W₂ denote their usual 2-Wasserstein distance. Let p_data∈P₂(Rᵈ) have a strictly positive smooth Lebesgue density ρ_data and a square-integrable score under p_data, meaning

∫_{Rᵈ} ||∇log ρ_data(x)||² ρ_data(x) dx < ∞.

Let γ=N(0,I_d), and assume that the density ratio f_data=dp_data/dγ belongs to L²(γ). Fix α∈(0,1) and t₀>0. For t≥0 and μ∈P₂(Rᵈ), define the OU sampling operator by

U_tμ = Law(e^(−t/2)X + √(1−e^(−t))Z),

where X∼μ and Z∼γ are independent. Starting from p̂⁰=p_data, define, for every integer i≥0, the error-free recursion

q_i=αp_data+(1−α)p̂ⁱ,    p̂ⁱ⁺¹=U_t₀(q_i).

Write N₀={0,1,2,…}. Let {H_n}_{n∈N₀ᵈ} be an orthonormal multivariate Hermite basis of L²(γ), with total degree |n|=n₁+⋯+n_d, and write

c_n=⟨f_data,H_n⟩_{L²(γ)},    ⟨f,g⟩_{L²(γ)}=∫fg dγ.

## Task

Prove that the recursion has a unique fixed point p_∞*∈P₂(Rᵈ), that

p_∞* = α∑_{k=0}^∞(1−α)^k U_{(k+1)t₀}(p_data),

and that, for every integer N≥0, the iterates satisfy

W₂(p̂ᴺ,p_∞*) ≤ [√(1−α)e^(−t₀/2)]ᴺ W₂(p_data,p_∞*).

Moreover, prove that p_∞* is absolutely continuous with respect to γ, that its density ratio f_∞*=dp_∞*/dγ belongs to L²(γ), and that

f_∞* = ∑_{n∈N₀ᵈ} m_n c_n H_n

with convergence in L²(γ), where

m_n = αe^(−|n|t₀/2) / [1−(1−α)e^(−|n|t₀/2)].

Conclude that the multiplier m_n is nonincreasing with total Hermite degree |n|, so higher-degree modes are more strongly attenuated.
