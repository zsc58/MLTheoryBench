# Problem

## Setup

Fix an integer `K>=3`. Let `{nu_theta : theta in Theta}` be a known regular one-parameter natural exponential family of probability laws on `R`, where `Theta` is a nonempty open interval. More explicitly, for a nonempty open natural-parameter interval `I`, a base probability law `Q` on `R`, and a function `A in C^2(I)` with `0<A''(eta)<infinity`, let the natural-parameter laws `P_eta` satisfy

`d P_eta / d Q (x) = exp(eta x-A(eta))`.

The mean map is `theta=A'(eta)`, its image is `Theta`, and `nu_theta=P_{eta(theta)}`, where `eta(theta)` is the inverse mean map. Write

`D(theta,theta') = KL(nu_theta || nu_theta')`.

An instance is an unknown vector `mu=(mu_1,...,mu_K) in Theta^K` having a unique best arm `b(mu)=argmax_k mu_k`; the set of such instances is `Theta_u^K`.

On instance `mu`, each arm `k` has a sequence of independent observations with law `nu_{mu_k}`, and all these sequences are mutually independent. Pulling an arm reveals its next unused observation. A budget-`T` algorithm chooses each arm measurably from the preceding chosen arms and observed rewards, together with any auxiliary randomization independent of the reward sequences. After exactly `T` pulls it recommends an arm `hat b_T` measurably from the observed history and that randomization. Its decision rules and randomization law may depend on `T` and the known family, but not on the unknown instance `mu`. Its error probability is

`p_{mu,T}=P_mu(hat b_T != b(mu))`.

An algorithm family `mathcal A=(mathcal A_T)_{T>=1}` is consistent if `p_{mu,T}->0` for every `mu in Theta_u^K`.

Let

`Delta_K={w in [0,1]^K : sum_k w_k=1}`,

and let `Delta_K^o` be the subset with every coordinate strictly positive. For `mu in Theta_u^K`, define

`Alt(mu)={lambda in Theta^K : lambda_j>=lambda_b for some j!=b}`, where `b=b(mu)`,

`G(mu,w)=inf_{lambda in Alt(mu)} sum_{k=1}^K w_k D(lambda_k,mu_k)`,

`G_so(mu)=sup_{w in Delta_K^o} G(mu,w)`, and `H_so(mu)=1/G_so(mu)`.

For each fixed `w in Delta_K^o`, a static-proportion family uses deterministic sample counts `n_k(T)` satisfying `sum_k n_k(T)=T` and `n_k(T)/T->w_k`, and recommends an arm with largest empirical mean, using a fixed rule to resolve ties. At the finitely many budgets before every arm has been sampled, its recommendation may be arbitrary. Assume that these static-proportion families satisfy

`lim_{T->infinity} T^{-1} log(1/p_{mu,T})=G(mu,w)`

for every `mu in Theta_u^K`.

For a finite positive function `H:Theta_u^K -> (0,infinity)`, set

`h_{mu,T}(mathcal A_T)=T/log(1/p_{mu,T})`,

with values `0` when `p_{mu,T}=0` and `+infinity` when `p_{mu,T}=1`, and define

`rho_H(mathcal A,mu)=limsup_{T->infinity} h_{mu,T}(mathcal A_T)/H(mu)`.

Such a function `H` is called a complexity for a class `C` of algorithm families if

`inf_{mathcal A in C} inf_{mu in Theta_u^K} rho_H(mathcal A,mu)>=1`

and some `mathcal A* in C` satisfies

`sup_{mu in Theta_u^K} rho_H(mathcal A*,mu)<=1`.

Assume the following information inequality. For every `H:Theta_u^K -> (0,infinity)`, every baseline `mu in Theta_u^K`, every nonempty `S subset Alt(mu) intersect Theta_u^K`, and every consistent family `mathcal A`,

`[sup_{lambda in S} rho_H(mathcal A,lambda)]^{-1} <= sup_{w in Delta_K} inf_{lambda in S} H(lambda) sum_{k=1}^K w_k D(mu_k,lambda_k)`.

Reciprocals of extended nonnegative quantities use the conventions `1/0=+infinity` and `1/(+infinity)=0`.

## Task

Prove the integrated theorem

`inf_{mathcal A consistent} sup_{mu in Theta_u^K} rho_Hso(mathcal A,mu) >= C_K`,

where

`C_K = 1 + sum_{j=3}^K (1+sqrt(j-1))^{-2}`.

Deduce that no consistent algorithm family uniformly attains the static-oracle benchmark, meaning that none satisfies `sup_mu rho_Hso(mathcal A,mu)<=1`, and that no complexity exists for any algorithm class containing all interior static-proportion families.
