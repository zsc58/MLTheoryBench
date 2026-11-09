# Problem

## Setup

Fix `d≥1` and an original time interval `[0,T_0]`. Let `g∈C^1([0,T_0])` satisfy `g(t)≥g_min>0`, and let `f` be regular enough that the induced drift below is `C^2` in `x` and `C^1` in `τ`. Define
`τ(t)=∫_0^t g(s)^2/2 ds`, let `T=τ(T_0)`, and let `t(τ)` be its inverse on `[0,T]`. Set
`b(x,τ)=f(x,t(τ))/(g(t(τ))^2/2)`. Assume `u:R^d×(0,T)→(0,∞)` is `C^{2,1}` and satisfies
`∂_τu-Δu=-∇·(b u)`.

For `(x_0,τ_0)∈R^d×(0,T)` and `r>0`, define
`Φ(z,σ)=(4πσ)^{-d/2} exp(-|z|^2/(4σ))` for `σ>0`,
`E_1={(z,σ):σ>0, Φ(z,σ)≥1}`, and
`ψ_0(z,σ)=log Φ(z,σ)` on `E_1`. Assume the backward heat-ball
`{(x_0+rz,τ_0-r^2σ):(z,σ)∈E_1}` is contained in `R^d×(0,T)`.
For any smooth `F`, write
`M_r[F]=(1/4)∫_{E_1}F(x_0+rz,τ_0-r^2σ)|z|^2/σ^2 dz dσ`.

Set `v=log u`, `w=u log u`, and `s=∇_x log u`.

## Task

Prove that, for every admissible `(x_0,τ_0,r)`,

`u(x_0,τ_0)=M_r[u]+d∫_{E_1}ψ_0(z,σ)∫_0^r ρ[-∇·(b u)](x_0+ρz,τ_0-ρ^2σ)dρ dz dσ`,

`v(x_0,τ_0)=M_r[v]+d∫_{E_1}ψ_0(z,σ)∫_0^r ρ[|∇v|^2-b·∇v-div b](x_0+ρz,τ_0-ρ^2σ)dρ dz dσ`,

and

`w(x_0,τ_0)=M_r[w]+d∫_{E_1}ψ_0(z,σ)∫_0^r ρ[-∇·(b w)-u|∇v|^2-u div b](x_0+ρz,τ_0-ρ^2σ)dρ dz dσ`.

Moreover, prove the score identity

`s(x_0,τ_0)= (1/4)∫_{E_1}s(x_0+rz,τ_0-r^2σ)|z|^2/σ^2 dz dσ`
`+d∫_{E_1}ψ_0(z,σ)∫_0^r ρ ∇[|∇v|^2-b·∇v-div b](x_0+ρz,τ_0-ρ^2σ)dρ dz dσ`.

Here all gradients and divergences in source terms are taken with respect to the spatial variable.
