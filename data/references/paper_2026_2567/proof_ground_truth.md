# Reference Proof

## Contract and Obligations

The context space is finite, the support and parameter set are nonempty, and the same fixed probability kernel K is used for every parameter. The two requested bounds are unconditional. Support identifiability is needed only for the optional zero-cost specialization below.

The theorem-critical obligations are: (1) contraction of a fixed probability kernel in TV; (2) the support comparison yielding the factor 2; (3) the signed-residual triangle inequality at each perturbation output; (4) the base-uncertainty bound at radius rho, including rho=0; and (5) taking the comparison infimum pointwise, followed by mixing and the outer suprema. All are derived below, without an external theorem dependency.

## Elementary TV Facts

Write Q_theta=tilde P_theta. All context integrals are finite sums.

For probability measures mu,nu on Z, let r(u)=mu(u)-nu(u). Since sum_u r(u)=0, the sum of its positive entries and the negative of the sum of its negative entries both equal TV(mu,nu). For any output event A, 0<=P_theta(A|u)<=1, so

|sum_u P_theta(A|u)r(u)|<=TV(mu,nu).

Taking the supremum over A proves

TV(sum_u P_theta(.|u)mu(u),sum_u P_theta(.|u)nu(u))<=TV(mu,nu).

For finite signed measures H of total mass zero, set ||H||_0=sup_A |H(A)|. This is precisely the TV convention used in the task when applied to the difference of two equal-mass measures. Testing each event proves both the triangle inequality and

||sum_u k(u)H_u||_0<=sum_u k(u)||H_u||_0

for nonnegative weights k summing to one. In particular, mixtures of pairs of probability laws obey the corresponding convexity inequality.

## First Bound

Fix z with d(z,S)<=delta and parameters theta,theta' whose perturbed models agree on S. Since S is finite and nonempty, there is s in S minimizing TV(K(.|z),K(.|s)). Its value is at most eta_K(delta).

The triangle inequality, Q_theta(.|s)=Q_theta'(.|s), and the contraction just proved give

TV(Q_theta(.|z),Q_theta'(.|z))
<=TV(Q_theta(.|z),Q_theta(.|s))+TV(Q_theta'(.|s),Q_theta'(.|z))
<=2 TV(K(.|z),K(.|s))
<=2 eta_K(delta).

Taking the supremum over z and admissible parameter pairs proves the first claim. This argument tests arbitrary measurable events; a supremum over individual output atoms alone would not establish TV control.

## Decomposition Bound

Fix z and an admissible perturbed pair theta,theta' as above. Let u have K({u}|z)>0. For any comparison parameters a,b whose base models agree on S, define

H_u=P_theta(.|u)-P_theta'(.|u),

B_u=P_a(.|u)-P_b(.|u),

D_u=[P_theta(.|u)-P_a(.|u)]-[P_theta'(.|u)-P_b(.|u)].

These signed measures have total mass zero, and H_u=B_u+D_u. The elementary triangle inequality therefore yields

TV(P_theta(.|u),P_theta'(.|u))
<=TV(P_a(.|u),P_b(.|u))
+TV(P_theta(.|u)-P_a(.|u),P_theta'(.|u)-P_b(.|u)).

By the definition of rho_K(delta), d(u,S)<=rho_K(delta). Since a,b agree on S, the first term is at most U_{P,S}(rho_K(delta)). This remains valid when rho_K(delta)=0, because uncertainty is defined for all nonnegative radii.

Take the infimum over a,b at this fixed u, and write the resulting residual as

e(z,u,theta,theta')=inf_{a,b: P_a=P_b on S} TV(P_theta(.|u)-P_a(.|u),P_theta'(.|u)-P_b(.|u)).

The comparison set is nonempty: any diagonal pair a=b is admissible. Since the preceding inequality holds for every such pair,

TV(P_theta(.|u),P_theta'(.|u))<=U_{P,S}(rho_K(delta))+e(z,u,theta,theta').

No attainment of this infimum is required. The definition of the source-faithful cost gives e(z,u,theta,theta')<=E_{K,P,delta} for every currently fixed admissible tuple. Consequently, mixture convexity gives

TV(Q_theta(.|z),Q_theta'(.|z))
<=sum_u K({u}|z) TV(P_theta(.|u),P_theta'(.|u))
<=U_{P,S}(rho_K(delta))+E_{K,P,delta}.

Only positive-mass u contribute. Taking the supremum over z and the admissible perturbed pairs proves the second claim. Importantly, the comparison pair may depend on u; no infimum is moved outside the output supremum or the mixture.

## Optional Zero-Cost Specialization

If support identifiability additionally holds, every admissible perturbed pair theta,theta' has corresponding base models agreeing on S. For every output u, choose a=theta and b=theta' in the comparison infimum. Both signed arguments then vanish, so the nonnegative residual infimum is zero. Taking the outer suprema gives E_{K,P,delta}=0, and the second bound specializes to U_{tilde P,S}(delta)<=U_{P,S}(rho_K(delta)). This is not an additional public target and is not required for full credit.

## Definition Closure and Attached Support Results

All optimization sets in the public definitions are nonempty: support contexts supply nearby contexts, probability kernels have nonempty positive-mass support, and diagonal parameter pairs supply support-agreeing pairs. Finite Z and nonempty S make rho finite. Probability TV is at most one; each signed residual is bounded by two by the triangle inequality. Thus no infinite-value or empty-set arithmetic is needed.

For the attached basic uncertainty properties, distance zero is exactly membership in S, so U(0)=0. Nested radius sets prove monotonicity. The finite set of context-to-support distances has a gap immediately to the right of any radius, proving right continuity. Monotonicity and the bound U<=1 give the limit as the radius tends to infinity.

For the attached hierarchical representation, the identity context kernel together with the original conditional probability kernel represents every original model. Conversely, a finite mixture of conditional probability laws is itself a conditional probability law. The selected proof already uses this mixture representation directly and does not rely on a specialized representation theorem.
