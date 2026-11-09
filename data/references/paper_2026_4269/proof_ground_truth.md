# Reference Proof

## Obligations

We prove: (1) integrability and normalization of the weights; (2) the exact forced heat-ball identity, including its boundary terms and small-radius limit; (3) the three source equations; and (4) justified differentiation giving the score identity. No paper-specific result is assumed without derivation.

## 1. Geometry, bounds, and normalization

Write

`a=1/(4π)`, `R(σ)²=−2dσ log(4πσ)`, and `Q(z,σ)=|z|²/(4σ²)`.

Apart from measure-zero endpoints, `E1` consists of `0<σ<a`, `|z|<R(σ)`. Its closure adds the tip `(0,0)` and is compact. The lowest-time point of the physical heat-ball is `(x0,τ0−r²a)`, which belongs to the heat-ball. Admissibility therefore gives `τ0−r²a>0`. All points sampled at radii `0≤ρ≤r`, together with a sufficiently small neighborhood of their spatial translates, lie in a compact subset of the solution domain. Continuous derivatives are bounded there, and positivity of `u` gives a positive lower bound there.

Let `ω_{d−1}` be the surface area of the unit sphere and put `n=d/2`. Spherical integration gives

`∫_{E1}Q = [ω_{d−1}/(4(d+2))](2d)^{(d+2)/2} ∫_0^a σ^{d/2−1}[−log(4πσ)]^{d/2+1} dσ = 1`.

For the last equality substitute `q=4πσ` and use

`∫_0^1 q^{n−1}(−log q)^{n+1}dq=Γ(n+2)/n^{n+2}`,

which follows by `y=−log q`, together with `ω_{d−1}=2π^n/Γ(n)`. Thus `∫_{E1}|z|²/σ²=4`.

Also `0≤ψ0≤(d/2)|log(4πσ)|` on each slice, whose volume is proportional to `σ^{d/2}|log(4πσ)|^{d/2}`. Hence `ψ0` is integrable. The weights and derivatives used below are integrable for every `d≥1`; in particular, their worst temporal powers are bounded by a constant times `σ^{d/2−1}` times a fixed power of `1+|log σ|` near zero.

## 2. The forced identity

Let `F∈C^{2,1}` on a neighborhood of the physical heat-ball and its tip, and set `h=(∂τ−Δ)F`. Define

`G_r(z,σ)=F(x0+rz,τ0−r²σ)` and `M(r)=∫_{E1}QG_r`.

The chain rule gives

`rM'(r)=∫_{E1}Q(z·∇_zG_r+2σ∂σG_r)`.

Differentiation is legitimate locally in `r` by the compact bounds and integrability from Section 1. We now derive its value rather than assume a heat-ball cancellation.

Write `B(σ)={|z|<R(σ)}` and

`H_r(σ)=∫_{|z|=R(σ)}G_r(z,σ)dS`.

Spatial integration by parts, followed by temporal integration over the moving balls, yields

`∫_{E1}Q(z·∇G_r+2σ∂σG_r)`

`=−d∫_{E1}QG_r+∫_0^a [R−2σR']Q(R,σ)H_r(σ)dσ`.

Indeed, `div_z(Qz)=(d+2)Q` and `∂σ(2σQ)=−2Q`. The moving-boundary contribution from the temporal integration is `−2σR'Q(R,σ)H_r`, while the spatial boundary contribution is `RQ(R,σ)H_r`.

Since `R²=−2dσ log(4πσ)`,

`R−2σR'=2dσ/R`,

so the preceding expression equals

`−dM(r)+d∫_0^a [R/(2σ)]H_r(σ)dσ`.  (A)

Next, direct differentiation of `ψ0` gives

`∂σψ0=−d/(2σ)+Q`, `Δ_zψ0=−d/(2σ)`, and `∂νψ0=−R/(2σ)` on the spatial slice boundary.

Integrating `∫ψ0(∂σG_r+Δ_zG_r)` by parts gives

`∫_{E1}ψ0(∂σG_r+Δ_zG_r)`

`=∫_{E1}(−∂σψ0+Δ_zψ0)G_r+∫_0^a [R/(2σ)]H_r(σ)dσ`

`=−M(r)+∫_0^a [R/(2σ)]H_r(σ)dσ`.  (B)

Here the terms containing `ψ0` itself on the lateral boundary vanish, but its normal derivative does not vanish; that term is explicitly retained in (B).

For rigor, perform these integrations first for `ε<σ<a−δ`. The temporal endpoint expressions involving `2σQG_r` and `ψ0G_r` are bounded near `σ=ε` by a constant times `ε^{d/2}(1+|log ε|)^{d/2+1}`, and hence tend to zero. They also tend to zero as `σ↑a`, since the slice radius and auxiliary function shrink to zero. The remaining integrals converge absolutely by the slice estimates in Section 1. Thus (A) and (B) hold on the full heat-ball, including in dimension one.

Comparing them and using

`∂σG_r+Δ_zG_r=−r²h(x0+rz,τ0−r²σ)`

proves

`M'(r)=−dr∫_{E1}ψ0(z,σ)h(x0+rz,τ0−r²σ) dz dσ`.

Consequently,

`M(r)+d∫_{E1}ψ0(z,σ)∫_0^r ρh(x0+ρz,τ0−ρ²σ)dρ dz dσ`

is constant in `r`. The normalized weight and continuity imply `M(r)→F(x0,τ0)` as `r↓0`. The other term tends to zero, bounded in absolute value by

`(d r²/2) sup|h| ∫_{E1}ψ0`.

We have therefore proved

`F(x0,τ0)=M_r[F]+d∫_{E1}ψ0(z,σ)∫_0^r ρh(x0+ρz,τ0−ρ²σ)dρ dz dσ`.  (C)

The argument is local and applies to every admissible radius, without any global boundedness or initial-data restriction.

## 3. Density, logarithm, and entropy density

The given time change has positive derivative `g²/2`, and the task assumes the normalized equation

`(∂τ−Δ)u=−div(bu)=:h_u`.

For `v=log u`, positivity and the chain rule give

`(∂τ−Δ)v=((∂τ−Δ)u)/u+|∇v|²`

`=|∇v|²−b·∇v−div b=:h_v`.

For `w=uv`, the product rule gives

`(∂τ−Δ)w=v h_u+u h_v−2∇u·∇v`.

Using `∇u=u∇v` and `div(buv)=v div(bu)+bu·∇v`, this becomes

`(∂τ−Δ)w=−div(bw)−u|∇v|²−u div b=:h_w`.

All three functions are `C^{2,1}` on the compact neighborhoods in question, and their sources are continuous. Applying (C) to `u`, `v`, and `w` gives exactly the three public identities, with the stated signs, factors, and radial integrations.

## 4. Score differentiation

Apply (C) to `v` and differentiate with respect to the anchor `x0`, keeping the scaled variables `(z,σ)` fixed. The domain `E1`, `Q`, and `ψ0` are independent of `x0`; no moving-domain calculation is needed at this step.

The required spatial source derivative is

`∇h_v=2D²v∇v−(Db)^T∇v−D²v b−∇div b`.

It is continuous under the public assumptions and bounded on the compact neighborhood described in Section 1. So are `∇v` and the derivatives needed for local difference quotients. The integrable dominating weights are `Q` and `ρψ0`, with `0≤ρ≤r`. Dominated convergence therefore gives

`∇v(x0,τ0)=∫_{E1}Q(z,σ)∇v(x0+rz,τ0−r²σ) dz dσ`

`+d∫_{E1}ψ0(z,σ)∫_0^r ρ∇h_v(x0+ρz,τ0−ρ²σ)dρ dz dσ`.

Substituting `s=∇v` and the definition of `h_v` is the asserted score identity. This also explains why no third spatial derivative of `u` is required.

## Source-dependency clarification

The source's standalone classical mean-value statement uses the wrong sign for the positive lag variable. In those coordinates the sampled function satisfies `∂σθ+Δθ=0`; equivalently the physical function `F(x,τ)=θ(x,−τ)` is forward caloric. The normalization used here is unaffected. Both normalization and the more general forced identity have been explicitly proved above, so no unresolved external or paper-specific proof obligation remains.
