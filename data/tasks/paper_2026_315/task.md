# Problem

## Setup

Let d,n be positive integers, β,L,σ>0, and 1≤p≤∞. On 𝒳=[0,1]^d observe i.i.d. pairs (X_i,Y_i), where Y_i=f*(X_i)+ξ_i. The design law P_X has density satisfying 0<μ_under≤dP_X/dx≤μ_over<∞ on 𝒳. The ξ_i are i.i.d. N(0,σ²) and independent of the design variables. An estimator is a jointly measurable function of its argument and the training sample. In risks, X denotes a fresh draw from P_X independent of that sample; expectations include both the sample and this draw.

Put k=⌈β⌉−1, the largest nonnegative integer strictly smaller than β. Using multi-indices α and the Euclidean norm, define 𝓗(β,L) by

max_{|α|≤k} sup_{x∈𝒳}|D^αf(x)| + max_{|α|=k} sup_{x,z∈𝒳, x≠z} |D^αf(x)−D^αf(z)|/‖x−z‖₂^(β−k) ≤ L.

For s≥0, B_p(x,s)={z:‖z−x‖_p≤s}. Fix an attack-radius bound R<∞ and allow 0≤r≤R, possibly depending on n. Define

R_r(f̂,f*)=E sup_{x′∈𝒳∩B_p(X,r)}[f̂(x′)−f*(X)]².

For a deterministic δ=δ_n≥0, let 𝓘(δ) consist of the jointly measurable estimators satisfying max_{1≤i≤n}|f̂(X_i)−Y_i|≤δ almost surely for every f*∈𝓗(β,L). Put

S_p(x,s)={i:X_i∈𝒳∩B_p(x,s)},   M_δ(x,s)=max_{i∈S_p(x,s)}(|ξ_i|−δ)_+²,

with an empty maximum equal to zero. Suprema and expectations are understood on the completed probability spaces.

Assume a jointly measurable base estimator f̃ is available: there are fixed s₀,C₀>0, independent of n, such that for every f*∈𝓗(β,L), x∈𝒳 and 0≤s≤s₀,

E sup_{z∈𝒳∩B_p(x,s)}[f̃(z)−f*(z)]² ≤ C₀{s^(2β)+n^(−2β/(2β+d))}.

The expectation here is over the training sample, with x fixed.

## Task

Prove, uniformly over 0≤r≤R and δ≥0, that

inf_{f̂∈𝓘(δ)} sup_{f*∈𝓗(β,L)} R_r(f̂,f*) ≍ r^(2(1∧β))+n^(−2β/(2β+d))+∫_𝒳 E M_δ(x,r) dx.

The comparison constants are independent of n,r and δ and may depend on the fixed model parameters, R, and the fixed constants in the base-estimator hypothesis. Moreover, for every deterministic sequence 0<τ_n↓0 satisfying

τ_n ≲ n^(−max{β/((2β+d)(1∧β)), (4β+d)/(d(2β+d))}),

construct a measurable δ-interpolating modification of f̃ supported within the τ_n-neighborhoods of the observations whose risk has the displayed order. Constants for this construction may also depend on the fixed constant in the bound on τ_n.
