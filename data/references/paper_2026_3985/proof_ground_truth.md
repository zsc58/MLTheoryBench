# Reference Proof

## Proof Structure and Audited Background

Let T(μ)=U_t₀(αp_data+(1−α)μ). Establish that T maps P₂(Rᵈ) into itself and is a strict W₂ contraction. Apply the fixed-point theorem on the full complete Wasserstein space. Identify the fixed point through a Neumann expansion on finite signed measures, verifying that operator's norm independently of the Wasserstein contraction. Control second moments and use probability-valued approximants when discussing W₂ convergence. Finally identify the Gaussian density action, establish convergence of the geometric density series in L²(γ), and calculate its Hermite coefficients.

The standard independent results used are the following:

- The space of all Borel probability measures on Rᵈ with finite second moment is complete under W₂. This is the Wasserstein background stated in the source at L000397–L000400, indexed by theory_002.
- A self-map of a nonempty complete metric space with Lipschitz constant κ<1 has a unique fixed point, and its iterates satisfy distance(Tᴺx,x*)≤κᴺ distance(x,x*). This is theory_022.
- If A is a bounded linear operator on a Banach space and ||A||<1, then (I−A)⁻¹=∑_{k≥0}Aᵏ in operator norm. This is theory_008.
- An orthonormal multivariate Hermite family is a complete orthonormal basis of L²(γ), and for the Gaussian OU function operator P_t, P_tH_n=e^(−|n|t/2)H_n. These are the classical facts indexed by theory_018, with the normalization convention in theory_024 and the recorded repair to theory_011. Their hypotheses here are precisely the standard Gaussian reference, this OU scaling, and functions in L²(γ).

The reverse-time diffusion theorem is not needed as a proof obligation: the public problem directly defines the ideal OU recursion. All paper-specific steps used below are derived, rather than assumed from the selected conclusions.

## Complete Proof

### step_001: Self-mapping and contraction

Put r=1−α and κ=√r exp(−t₀/2). Then 0<r<1 and κ<1. For a probability measure μ, write M₂(μ)=∫||x||² μ(dx). The defining independent Gaussian representation gives

M₂(U_tμ)=e^(−t)M₂(μ)+d(1−e^(−t)).

Thus U_t maps P₂ into P₂, and the mixture defining T also belongs to P₂. In particular, T is a self-map of P₂.

For μ,ν∈P₂, couple the common αp_data components identically and the remaining components by any coupling of μ and ν. Taking the infimum of its quadratic cost gives

W₂²(αp_data+rμ, αp_data+rν)≤rW₂²(μ,ν).

For a coupling (X,Y) of μ,ν, use a common independent Z∼γ in their OU representations. Their difference after time t is e^(−t/2)(X−Y). Taking the infimum over couplings yields

W₂(U_tμ,U_tν)≤e^(−t/2)W₂(μ,ν).

Combining these inequalities,

W₂(Tμ,Tν)≤κW₂(μ,ν).

### step_002: Existence and uniqueness

The full space P₂(Rᵈ) is nonempty and complete, and step_001 verifies every hypothesis of the fixed-point theorem. Consequently T has a unique fixed point p_∞*∈P₂.

This application uses the full Wasserstein space, not a possibly nonclosed subclass of absolutely continuous measures. Since t₀>0, U_t₀ applied to any probability measure has a Lebesgue density: a Lebesgue-null set has zero probability under every nondegenerate Gaussian kernel, hence also under their mixture. Therefore the fixed point is absolutely continuous as well. This agrees with the source's density convention.

### step_003: The geometric mixture and its convergence

The Gaussian kernel defines U_t on finite signed Borel measures by integration. It is linear in the input measure. Composing two independent Gaussian transitions gives mean factor e^(−(s+t)/2) and noise covariance

[e^(−t)(1−e^(−s))+1−e^(−t)]I_d=(1−e^(−(s+t)))I_d.

Hence U_tU_s=U_{t+s}.

The fixed-point equation is

p_∞*=αU_t₀p_data+rU_t₀p_∞*.

Its finite iteration gives, for every integer j≥1,

p_∞*=S_j+rʲU_{jt₀}p_∞*,

where S_j=α∑_{k=0}^{j−1}rᵏU_{(k+1)t₀}p_data.

Here S_j has mass 1−rʲ; it is not itself an element of P₂. To justify the linear Neumann argument, use the Banach space of finite signed Borel measures with total-variation norm. A Markov kernel satisfies |U_tν|≤U_t|ν| and preserves the mass of nonnegative measures, so

||U_tν||_TV≤||ν||_TV.

It follows that ||rU_t₀||≤r<1. Thus the audited linear Neumann theorem applies on this specified Banach space. Equivalently, the remainder in the finite expansion has total-variation norm rʲ and tends to zero. We obtain equality of measures

p_∞*=α∑_{k=0}^∞rᵏU_{(k+1)t₀}(p_data).

The weights are nonnegative and sum to one. Moreover, with C_data=max(M₂(p_data),d), the moment identity gives M₂(U_t p_data)≤C_data for all t≥0. Tonelli's theorem therefore shows that the infinite mixture is a probability measure with second moment at most C_data.

For an explicit W₂ interpretation, let B_j=S_j+rʲγ, which is a probability measure in P₂. Couple the common S_j components identically in B_j and p_∞*, and couple their remaining probability components independently. If C_*=max(M₂(p_∞*),d), then

W₂²(B_j,p_∞*)≤rʲW₂²(γ,U_{jt₀}p_∞*)≤2rʲ(d+C_*)→0.

Thus the representation is compatible with convergence in P₂ using probability-valued approximants; it does not apply W₂ to subprobability partial sums.

### step_004: Geometric convergence of the recursion

Since p̂⁰=p_data, p̂ᴺ=Tᴺp_data, and T p_∞*=p_∞*, repeated application of step_001 gives, for every N∈N₀,

W₂(p̂ᴺ,p_∞*)≤κᴺW₂(p_data,p_∞*).

All distances are finite by membership in P₂, and κ<1 gives the requested geometric convergence.

### step_005: Gaussian density action and L² control

Define the function operator

(P_t h)(x)=E[h(e^(−t/2)x+√(1−e^(−t))Z)],  Z∼γ.

If X and Z are independent standard Gaussians, then Y=e^(−t/2)X+√(1−e^(−t))Z is standard Gaussian. The joint Gaussian law of (X,Y) has covariance blocks I_d,I_d and cross-covariance e^(−t/2)I_d, so it is invariant under exchanging X and Y. Consequently P_t is self-adjoint with respect to γ. Also Jensen's inequality and invariance give

||P_t h||²₂≤∫P_t(|h|²)dγ=||h||²₂.

These identities extend from bounded functions to L² functions by truncation and this contraction bound.

For μ=fγ with f∈L²(γ) and any bounded measurable φ, kernel duality and self-adjointness give

∫φ d(U_tμ)=∫(P_tφ)f dγ=∫φ(P_tf)dγ.

Hence d(U_tμ)/dγ=P_tf, with P_tf∈L²(γ).

### step_006: Hermite expansion and OU eigenvalues

The public Hermite family is orthonormal. The L² assumption on f_data and the audited Hermite basis theorem therefore give

f_data=∑_n c_nH_n in L²(γ),  ∑_n|c_n|²=||f_data||²₂.

For λ_n=exp(−|n|t₀/2), the audited OU eigenvalue relation gives

P_{(k+1)t₀}H_n=λ_n^(k+1)H_n.

Since P_t is bounded on L², it acts on the convergent Hermite expansion by continuity. Thus

P_{(k+1)t₀}f_data=∑_n c_nλ_n^(k+1)H_n in L²(γ).

### step_007: Identification and coefficients of the limiting density

By step_005,

∑_{k=0}^∞||αrᵏP_{(k+1)t₀}f_data||₂≤α∑_{k=0}^∞rᵏ||f_data||₂=||f_data||₂.

The geometric density series consequently converges in L² to a function g. Because γ is a probability measure, L² convergence implies L¹ convergence. Its finite sums are exactly the densities of S_j, so the L¹ limit and the measure identity in step_003 imply p_∞*=gγ. In particular, f_∞*=g∈L²(γ).

The functional h↦⟨h,H_n⟩ is continuous on L². Taking it through the geometric series yields

⟨f_∞*,H_n⟩=α∑_{k=0}^∞rᵏc_nλ_n^(k+1)=c_n αλ_n/(1−rλ_n),

since 0<λ_n≤1 and r<1. This argument justifies the spectral calculation without assuming an unjustified interchange of two infinite series.

Set m_n=αλ_n/(1−rλ_n). Completeness of the orthonormal Hermite basis now gives

f_∞*=∑_n m_nc_nH_n in L²(γ),

with precisely the multiplier stated in the problem.

### step_008: Monotonicity, including degree zero

For 0<λ≤1, the denominator 1−rλ is positive and

d/dλ [αλ/(1−rλ)]=α/(1−rλ)²>0.

As total degree increases, λ_n=exp(−|n|t₀/2) strictly decreases because t₀>0. Thus m_n is nonincreasing with total degree, and strictly decreases between distinct degrees. At degree zero, λ_0=1 and m_0=α/(1−r)=1. For positive degree, 0<m_n<1. This proves the stated mode-dependent attenuation and covers the constant mode. If p_data=γ, only the constant mode is present and the fixed point is γ, consistently with every conclusion.

## Audit Closure

All theorem-critical obligations are closed by the displayed derivations or by the explicitly stated standard independent results with verified hypotheses. The source-local corrections concern the operator typing and elementary calculations in theory_004, the Neumann application in theory_009, and the already recorded Hermite normalization in theory_011. No specialized nonstandard dependency remains unresolved.
