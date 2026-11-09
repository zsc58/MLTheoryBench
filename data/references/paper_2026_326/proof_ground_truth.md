# Reference Proof

## Proof Structure

The RKHS unit ball is symmetric, so zero deviation makes the expectation functional vanish on the whole vector RKHS. Gradient tests yield the generator identity and stationarity. Compactly supported vector tests then force the probability current to vanish. Generator symmetry gives reversibility. Conversely, stationarity and reversibility force the current to vanish; a cutoff argument extends the resulting identity to every RKHS test field. This proof does not require an L² score or an assumed decay condition on ∇ρ.

## Complete Proof

Put F(g)=∫(𝒯g)ρ dx. Bounded kernel derivatives give bounded values and first derivatives for every g∈ℋᵈ, with bounds proportional to ‖g‖_{ℋᵈ}. Since b and a are bounded and ρ is a probability density, F is a finite linear functional.

Suppose Δ(ρ)=0. Symmetry of the unit ball implies F(g)=F(−g)=0 for its members; scaling gives F(g)=0 for every g∈ℋᵈ. For u∈C_c^∞(ℝᵈ), each component of ∇u belongs to ℋ, and symmetry of a gives 𝒯(∇u)=2ℒu. Thus ∫ℒu dρ=0 for every such u. The standard generator-core stationarity criterion applies here: for the nonexplosive diffusion with the stated bounded C¹ coefficients and pointwise positive-definite a, C_c^∞ is a generator core, and a probability measure annihilating ℒ on that core is invariant. Hence ρ is stationary.

Define Jᵢ=ρbᵢ−(1/2)∑ⱼ∂ⱼ(ρaᵢⱼ). This is a continuous vector field. Every g∈C_c^∞(ℝᵈ,ℝᵈ) lies in ℋᵈ. Ordinary compact-support integration by parts therefore gives F(g)=2∫J·g dx=0. The fundamental lemma for test functions yields J=0 as a distribution and, by continuity, pointwise.

Here is the detailed-balance step with its hypotheses explicit. For compactly supported smooth f and h, integration by parts gives

∫fℒh dρ=−(1/2)∫ρ(∇f)ᵀa∇h dx+∫fJ·∇h dx.

When J=0, ℒ is symmetric on C_c^∞ in L²(ρ). Stationarity makes (Pₜ) a strongly continuous contraction semigroup on L²(ρ). The stated generator core extends symmetry to its generator; a symmetric generator of a contraction semigroup is self-adjoint by its resolvent, so Pₜ is self-adjoint. This is reversibility. Equivalently, this is the standard zero-current/detailed-balance criterion for a nonexplosive stationary diffusion with the stated core and coefficient regularity.

Conversely, assume ρ is stationary and the diffusion is reversible with respect to ρ. Stationarity gives ∫ℒh dρ=∫J·∇h dx=0 for all h∈C_c^∞, hence div J=0 distributionally. Reversibility makes ℒ symmetric on this core. The displayed integration-by-parts identity then implies ∫fJ·∇h=∫hJ·∇f for compactly supported smooth f,h. Since div J=0, integration by parts also makes these two integrals negatives of one another. Thus ∫fJ·∇h=0. To test component Jᵢ against an arbitrary compactly supported smooth φ, take f=φ and h=xᵢχ, where χ∈C_c^∞ equals one near supp φ. It follows that ∫φJᵢ=0. Hence J=0.

Finally, no boundary assumption on ρ is needed to extend the zero-current identity to ℋᵈ. Choose smooth compactly supported cutoffs χ_R equal to one on the radius-R ball, bounded by one, and satisfying ‖∇χ_R‖∞≤C/R. Compact-support integration by parts and J=0 give F(χ_Rg)=0 for any g∈ℋᵈ; χ_Rg need not itself belong to ℋᵈ. Expanding 𝒯(χ_Rg), the extra integral is bounded by C′‖g‖∞/R because a is bounded and ∫ρ=1. Dominated convergence applies to the remaining integral because g, ∇g, a, and b are bounded. Therefore F(g)=0 for every g∈ℋᵈ. Its unit-ball supremum is zero, and Δ(ρ)=0.

The inherited stationary density p and bounded skew field c specify the source’s class of diffusions. The argument does not need to identify p with ρ or invoke an L² adjoint formula for c∇logρ+div c.
