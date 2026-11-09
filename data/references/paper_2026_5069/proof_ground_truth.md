# Reference Proof

## Obligations and background

We verify: (1) identification, finite moments and nonsingular J; (2) the foldwise nuisance remainder and its aggregation; (3) empirical-root existence and consistency; (4) the root-n rate and asymptotic linearity; (5) the same properties for each fixed unified-family member; (6) the covariance gap and precise strictness condition; and (7) named-member inclusion and feasible known-propensity transfer.

The independent background results used are the weak law for i.i.d. integrable finite-dimensional random vectors, the multivariate CLT for i.i.d. centered vectors with finite second moment, and Slutsky's theorem. The CLT permits singular covariance. Uniform convergence below is derived from finite nets and uniform continuity, rather than assumed from a named empirical-process result.

Write P for population expectation. All constants below are finite, independent of n and the training sample, and may depend on the fixed dimensions, compact feature set, a chosen compact parameter ball, κ, the conditional-covariance bound, and, in the uniform-labeling regime, the fixed ρ.

## 1. Identification and moments

Let L(β)=E[b(Xβ)−YᵀXβ] and H(X,β)=Xᵀ∇²b(Xβ)X. For each compact parameter ball D contained in B, the image {xβ:x∈X̄,β∈D} is a compact subset of Θ. On this image b, ∇b and ∇²b are bounded, and the least eigenvalue of ∇²b has a positive minimum m_D. Consequently differentiation under the expectation is justified, and

∇L(β)=E[Xᵀ(∇b(Xβ)−Y)],

∇²L(β)=E[H(X,β)]⪰m_D E[XᵀX]≻0 for β∈D.

The same argument at every point of B proves strict convexity of L. Thus the assumed interior minimizer β* is unique, ∇L(β*)=0, and J=∇²L(β*) is finite and positive definite.

Define

S=Xᵀ(∇b(Xβ*)−Y),

ζ=Xᵀ(∇b(Xβ*)−g*),   π=Xᵀ(g*−Y).

Then S=ζ+π and E[π|X,Z]=0. Conditional Jensen gives E||g*||²≤E||Y||²<∞. Bounded X and the compact-domain gradient bound imply that S, ζ and π have finite second moments. MAR gives E[wπ/e*|X,Z]=0, hence the oracle score ψ*(β*)=Ψ(Ξ;e*,g*;β*)=ζ+wπ/e* is centered. Its second moment is finite because e*≥κ.

## 2. Cross-fitted nuisance remainder

Condition separately for each fold k on the partition, the observed training data outside I_k, and any independent training randomization. The validation observations are then independent, with the original population law, and the functions ê^(k),ĝ^(k) are fixed. Put Δe=ê^(k)−e* and Δg=ĝ^(k)−g*.

The event E_k={||Δe||∞≤κ/2} is training-measurable and has probability tending to one. On E_k, ê^(k)≥κ/2 almost surely. An exact expansion, valid for every β, is

Ψ(Ξ;ê^(k),ĝ^(k);β)−Ψ(Ξ;e*,g*;β)=A+B+C,

A=(w/e*−1)XᵀΔg,

B=−wΔe Xᵀ(g*−Y)/(e*ê^(k)),

C=−wΔe XᵀΔg/(e*ê^(k)).

Conditional on training, A and B are centered. For A use E[w|X,Z]=e*. For B use MAR and E[g*−Y|X,Z]=0. On E_k their conditional second moments satisfy

E[||A||²|training]≤C₁||Δg||₂²,

E[||B||²|training]≤C₂||Δe||₂².

For the second bound, condition on (X,Z), use w≤1 and 1/(e*ê^(k))≤2/κ², and use

E[||Xᵀ(g*−Y)||²|X,Z]
 =tr(XᵀCov(Y|X,Z)X)≤σ²||X||_F².

Also, by Cauchy–Schwarz,

E[||C|| |training]≤C₃||Δe||₂||Δg||₂.

Let n_k=|I_k| and P_{I_k} denote its empirical mean. Conditional Chebyshev bounds for √n P_{I_k}A and √n P_{I_k}B are bounded by constants times (n/n_k)||Δg||₂² and (n/n_k)||Δe||₂², respectively. These converge to zero in probability because n/n_k is bounded and both fitted functions are consistent. Conditional Markov gives a bound proportional to

√n||Δe||₂||Δg||₂
 =O_p(α_n² n^{1/2−r_e−r_g})=o_p(1)

for √n P_{I_k}C. Truncate each conditional probability bound at one before taking its expectation; bounded convergence in probability then removes the conditioning. The exceptional event E_k^c has vanishing probability.

Since K is fixed,

R_n=(1/n)∑_k∑_{i∈I_k}[Ψ(Ξ_i;ê^(k),ĝ^(k);β)−ψ*(Ξ_i;β)]
 =o_p(n^−1/2).

This vector does not depend on β. Independence between different fold remainders is not required.

## 3. A local convex argument

We give the localization and root-existence argument used for both estimator families. Consider a twice differentiable convex empirical criterion F_n on B, with gradient G_n and Hessian H_n. Suppose G_n(β*)=O_p(n^−1/2), and on a sufficiently small closed ball D about β*, H_n converges uniformly in probability to H_P(β)=E[H(X,β)].

The population Hessian has a positive lower eigenvalue on D. Thus for some c>0, with probability tending to one, H_n(β)⪰cI throughout D. For every unit u and every small fixed radius r with β*+ru∈D,

uᵀG_n(β*+ru)≥−||G_n(β*)||+cr,

F_n(β*+ru)−F_n(β*)≥−r||G_n(β*)||+cr²/2.

Uniformly on the sphere of radius r, the first bound is positive and the second is at least cr²/4 with probability tending to one. The continuous criterion attains its minimum on the closed ball. A boundary point cannot minimize it because its derivative toward the center is negative. Hence an interior score root exists, and convexity makes it a global minimizer on B.

If β lies outside this ball, the segment from β* to β stays in B. Convexity implies that its criterion increment is at least the positive sphere increment, and its outward radial derivative is at least the corresponding sphere derivative. Therefore either an o_p(1) criterion-excess condition or an o_p(1) score-residual condition forces an estimator into the ball with probability tending to one. Taking every sufficiently small fixed radius proves consistency. This also explains why no global uniform strong convexity or compactness of B is needed.

To obtain the requisite uniform Hessian convergence, note that H(x,β) is bounded and uniformly continuous in β, uniformly for x∈X̄ and β∈D. For any ε>0, a finite parameter net makes the oscillation between a point and its net representative at most ε. The weak law applies to each matrix entry at finitely many net points. The supremum deviation is therefore at most the maximum net-point deviation plus 2ε. Letting ε decrease proves uniform convergence. The same proof applies to a bounded random multiplier a(w), with its bound absorbed into ε.

## 4. GAI consistency, rate and normality

The gradient of Q̂_n is G_n(β)=P_nψ*(β)+R_n. Its Hessian is H_n(β)=P_nH(X,β), the sample average of the observation Hessians. It is convex on B. The oracle CLT and Section 2 imply G_n(β*)=O_p(n^−1/2). Section 3 applies and proves consistency, as well as existence of exact roots with probability tending to one. Thus the public estimator conditions are compatible and do not posit a nonexistent family.

For h_n=β̂−β*, the integrated Taylor formula gives exactly

G_n(β̂)=G_n(β*)+A_n h_n,

A_n=∫₀¹H_n(β*+t h_n)dt.

Consistency, uniform Hessian convergence on D, and continuity of H_P imply A_n→pJ. Its inverse is therefore bounded in probability. Since G_n(β̂)=o_p(n^−1/2) by the estimator contract and G_n(β*)=O_p(n^−1/2), this identity first proves h_n=O_p(n^−1/2). Substituting R_n=o_p(n^−1/2) then gives

√n(β̂−β*)=−J^−1√nP_nψ*(β*)+o_p(1).

The verified oracle centering and finite second moment allow the multivariate CLT, and Slutsky gives the first asserted covariance.

For comparison with an empirical-process proof, the correct equicontinuity expression is √n(P_n−P)[ψ*(β̂)−ψ*(β*)], not the uncentered increment in revision 1. The Hessian argument above avoids assuming that false display and establishes the root-n rate before using an o_p(n^−1/2) linearization remainder. Indeed, after the rate is established, uniform Hessian convergence also directly bounds that centered increment by √n||h_n|| times an o_p(1) Hessian deviation.

## 5. Unified-family consistency and normality

Fix a deterministic λ∈[0,1] and measurable f∈L²(X,Z). Let

a(w)=w(1−λ)/ρ+(1−w)λ/(1−ρ),

c(w)=λ[w/ρ−(1−w)/(1−ρ)].

The corrected criterion is

q(Ξ;β)=a(w)b(Xβ)−(w/ρ)YᵀXβ+c(w)fᵀXβ.

Its gradient is exactly Φ_{λ,f}, and its Hessian is a(w)H(X,β). Since a(w)≥0 it is convex, including λ=0 and λ=1. Independence of w implies E[a(w)|X,Y,Z]=1 and E[c(w)|X,Y,Z]=0. Consequently

E[q(Ξ;β)]=L(β),

E[Φ_{λ,f}(Ξ;β)]=∇L(β),

E[a(w)H(X,β)]=H_P(β).

The score at β* is centered and square-integrable: its weights are bounded for fixed 0<ρ<1, ∇b(Xβ*) and X are bounded, and Y and f are square-integrable. Thus its empirical mean is O_p(n^−1/2). The weighted finite-net argument and Section 3 give high-probability root existence and consistency for β̂_{λ,f}. The integrated empirical Taylor argument of Section 4 then proves

√n(β̂_{λ,f}−β*)=−J^−1√nP_nΦ_{λ,f}(β*)+o_p(1).

The CLT gives covariance Σ(λ,f)=J^−1Ω(λ,f)J^−1. This is pointwise in each fixed (λ,f), not uniform asymptotic normality over the entire function class.

## 6. Covariance decomposition and strictness

At β*, let h=λXᵀ(∇b(Xβ*)−f). Then

Φ_{λ,f}=(w/ρ)(S−h)+((1−w)/(1−ρ))h.

The two blocks cannot be simultaneously nonzero as functions of w. Binary w and its independence therefore give

Ω(λ,f)=ρ^−1E[(S−h)(S−h)ᵀ]+(1−ρ)^−1E[hhᵀ].

Put δ=h−(1−ρ)S. Substitution of S−h=ρS−δ and h=(1−ρ)S+δ cancels the mixed terms and gives

Ω(λ,f)=E[SSᵀ]+[ρ(1−ρ)]^−1E[δδᵀ].

With the public residual r_{λ,f}, δ=Xᵀr_{λ,f}−(1−ρ)π. Because Xᵀr_{λ,f} is measurable with respect to (X,Z), and E[π|X,Z]=0, both cross moments are zero. All products are integrable by their second moments. Hence

E[δδᵀ]=E[(Xᵀr_{λ,f})(Xᵀr_{λ,f})ᵀ]+(1−ρ)²E[ππᵀ].

The GAI choice (1−ρ,g*) makes r zero, and its score equals Ψ(Ξ;ρ,g*;β) for every β by substitution. Its Ω is E[ζζᵀ]+ρ^−1E[ππᵀ]. Subtracting its covariance gives the displayed public gap.

For any v, its scalar quadratic gap equals

[ρ(1−ρ)]^−1E[(vᵀJ^−1Xᵀr_{λ,f})²].

It is nonnegative and is positive exactly when the scalar residual is nonzero with positive probability. The covariance gap vanishes as a matrix exactly when Xᵀr_{λ,f}=0 almost surely. A nonzero vector residual alone need not make the matrix positive definite. The minimum covariance is unique, but there can be multiple pairs attaining it.

## 7. Named members and feasible GAI

The stipulated L² condition on Z^P puts PPI and PPI++ inside the same admissible class. At λ=0 the prediction drops out, giving the primary-only score wXᵀ(∇b−Y)/ρ. The other named members follow by their definitions. The function tr Σ(λ,Z^P) is a finite continuous quadratic in λ, since the score is affine in λ and has finite second moment. It attains a minimum on [0,1], so the population λ_* is defined even in degenerate cases with multiple minimizers. Dominance holds for every such choice.

For feasible GAI under known ρ, take ê^(k)≡ρ. The nuisance difference in Section 2 reduces to (w/ρ−1)XᵀΔg. Conditional centering and its second-moment bound show that its aggregated remainder is o_p(n^−1/2) under only foldwise ||Δg||₂=o_p(1). No product rate is used. Sections 3–4 apply unchanged. Both feasible and oracle GAI have the same asymptotic linear representation, so their difference is o_p(n^−1/2) and their covariance is Σ_GAI. All obligations are closed.
