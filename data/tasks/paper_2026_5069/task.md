# Problem

## Population setup

Let p,d be fixed positive integers. Let X∈R^{p×d} have support contained in a compact set X̄, let Y∈R^p, let Z take values in a measurable auxiliary space, and let w∈{0,1}. The latent observations Ξ_i=(X_i,Y_i,w_i,Z_i), i=1,…,n, are i.i.d. from the population defining the target. X_i,w_i,Z_i are observed for every unit; Y_i is observed only when w_i=1. A term multiplied by w_i and involving Y_i is evaluated as zero when w_i=0.

Assume:

- B⊂R^d and Θ⊂R^p are open and convex, and xβ∈Θ for every x∈X̄ and β∈B.
- b:Θ→R is twice continuously differentiable, with ∇²b(θ) positive definite for every θ∈Θ.
- w is conditionally independent of Y given (X,Z). Write e*(X,Z)=E[w|X,Z] and g*(X,Z)=E[Y|X,Z], using measurable versions, and assume e*≥κ>0 almost surely for a fixed κ.
- E[XᵀX] is positive definite, E||Y||²<∞, and ||Cov(Y|X,Z)||≤σ² almost surely for a finite constant σ². Vector norms are Euclidean and matrix norms are operator norms unless specified otherwise.
- An interior population minimizer exists:

  β*∈argmin_{β∈B} E[b(Xβ)−YᵀXβ].

  Its first-order condition is E[Xᵀ(∇b(Xβ*)−Y)]=0.

Define

Ψ(Ξ;e,g;β)=Xᵀ[∇b(Xβ)−g(X,Z)+(w/e(X,Z))(g(X,Z)−Y)],

J=E[Xᵀ∇²b(Xβ*)X].

All parameters, the population law, κ, σ², and the dimensions are fixed as n tends to infinity.

## Cross-fitted estimator

Fix an integer K≥2, independent of n. Partition the indices into K folds I_1,…,I_K of sizes differing by at most one, using randomization independent of the observations. For each fold k, fit measurable functions ê^(k)(x,z)>0 and ĝ^(k)(x,z)∈R^p using only observed data outside I_k. Outcome-regression fitting uses the available labels outside I_k. Any model selection or preprocessing used to fit these functions is also confined to that training sample; additional training randomization is independent of the observations. For i∈I_k, set ê_i=ê^(k)(X_i,Z_i) and ĝ_i=ĝ^(k)(X_i,Z_i).

Let

Q̂_n(β)=n^−1∑_i{b(X_iβ)−[ĝ_i−(w_i/ê_i)(ĝ_i−Y_i)]ᵀX_iβ},

Ĝ_n(β)=n^−1∑_k∑_{i∈I_k}Ψ(Ξ_i;ê^(k),ĝ^(k);β).

Let β̂ be a measurable B-valued estimator satisfying

Q̂_n(β̂)≤inf_{β∈B}Q̂_n(β)+o_p(1),

||Ĝ_n(β̂)||=o_p(n^−1/2).

Estimator conditions of this kind are understood on events whose probability tends to one, with an arbitrary fixed value in B used on exceptional events.

For a measurable function h of (X,Z), define ||h||₂=(E||h(X,Z)||²)^{1/2}, and let ||h||∞ be its essential supremum norm under the law of (X,Z). For a fitted random function these norms integrate over a fresh population draw with the training sample held fixed.

For conclusion 1 assume that, for every fold k,

||ĝ^(k)−g*||₂=O_p(α_n n^{−r_g}),

||ê^(k)−e*||₂=O_p(α_n n^{−r_e}),

||ê^(k)−e*||∞=o_p(1),

where α_n>0 is deterministic with α_n↓0, r_g,r_e≥0 are fixed, and r_g+r_e≥1/2.

## Unified family under uniform labeling

For conclusion 2 retain the population setup and instead assume w is independent of (X,Y,Z), with known fixed P(w=1)=ρ∈(0,1). For each fixed λ∈[0,1] and fixed measurable function f(X,Z)∈R^p satisfying E||f(X,Z)||²<∞, define

Φ_{λ,f}(Ξ;β)
 = (w/ρ)Xᵀ[(∇b(Xβ)−Y)−λ(∇b(Xβ)−f(X,Z))]
   +((1−w)/(1−ρ))λXᵀ(∇b(Xβ)−f(X,Z)),

q_{λ,f}(Ξ;β)
 = [w(1−λ)/ρ+(1−w)λ/(1−ρ)]b(Xβ)
   −(w/ρ)YᵀXβ
   +λ[w/ρ−(1−w)/(1−ρ)]f(X,Z)ᵀXβ.

For any observation function h, write P_nh=n^−1∑_i h(Ξ_i). Let β̂_{λ,f} be a measurable B-valued estimator satisfying

P_nq_{λ,f}(β̂_{λ,f})≤inf_{β∈B}P_nq_{λ,f}(β)+o_p(1),

||P_nΦ_{λ,f}(β̂_{λ,f})||=o_p(n^−1/2),

with the same exceptional-event convention as above. The functions f and the scalar λ are fixed population choices, not arbitrary functions of the inference sample.

Define

Ω(λ,f)=E[Φ_{λ,f}(Ξ;β*)Φ_{λ,f}(Ξ;β*)ᵀ],

Σ(λ,f)=J^−1Ω(λ,f)J^−1.

Let Z^P∈R^p be a designated measurable prediction component of Z satisfying E||Z^P||²<∞; the other components of Z remain unrestricted. The primary-only, PPI and PPI++ members are respectively (0,·), (1,Z^P) and (λ_*,Z^P), where λ_* is any fixed population minimizer of λ↦tr Σ(λ,Z^P) over [0,1]. The oracle GAI member is (1−ρ,g*).

For feasible GAI in this regime use the same fixed-fold estimator definition, set ê^(k)≡ρ, and assume only ||ĝ^(k)−g*||₂=o_p(1) for every fold. The quantitative nuisance-rate assumptions for conclusion 1 are not required in this known-propensity regime.

## Task

Prove that:

1. Under the assumptions for conclusion 1, β̂ converges in probability to β* and

   √n(β̂−β*)⇒N(0,Σ_GAI),

   Σ_GAI=J^−1E[Ψ(Ξ;e*,g*;β*)Ψ(Ξ;e*,g*;β*)ᵀ]J^−1.

2. Under uniform labeling, for every fixed admissible (λ,f), β̂_{λ,f} is consistent for the same β* and

   √n(β̂_{λ,f}−β*)⇒N(0,Σ(λ,f)).

   Writing

   r_{λ,f}(X,Z)=λ(∇b(Xβ*)−f(X,Z))−(1−ρ)(∇b(Xβ*)−g*(X,Z)),

   prove

   Σ(λ,f)−Σ_GAI
   =[ρ(1−ρ)]^−1J^−1E[(Xᵀr_{λ,f})(Xᵀr_{λ,f})ᵀ]J^−1⪰0.

   Thus the GAI choice weakly dominates primary-only, PPI and PPI++. In a direction v≠0, the covariance improvement is strict exactly when P(vᵀJ^−1Xᵀr_{λ,f}≠0)>0. The feasible cross-fitted GAI estimator under the known-propensity assumptions has the same limiting covariance as the oracle GAI member.

The normal limits may have singular covariance.
