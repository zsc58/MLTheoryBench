# Problem

## Setup

Let K be a positive finite integer and let X be a nonempty measurable subset of [0,1]^p. For each arm a in {1,...,K}, independently draw a latent joint context-reward law pi_a from a prior Pi_a. Write Pi=product_a Pi_a. These laws have the same fixed context marginal. Define the finite latent conditional mean

f_0(x,a)=integral y pi_a(dy|x).

Contexts X_t are independent exogenous draws from that marginal, independent of the latent laws and the algorithms' randomization. At round t, a policy observes X_t, selects A_t using only its previous observations, X_t, and its own randomization, and observes a reward from pi_{A_t}(.|X_t). The reward model is

R_t=f_0(X_t,A_t)+xi_t,

where the observation noises are independent, mean zero, and bounded in absolute value by a finite constant B. Conditional reward observations are generated according to the latent arm laws. Let H_{t,a} be the ordered context-reward pairs previously observed from arm a, and write H_t=(H_{t,1},...,H_{t,K}). Each arm's posterior uses only its own observed pairs.

Fix measurable versions of the conditional laws used below. An admissible history collection H=(H_1,...,H_K) is a finite collection of arm-specific context-reward histories compatible with this observation model, including empty histories, on which these versions are specified. All histories reached by the policies are in their domains.

Let a^*(x) be an arm maximizing f_0(x,a), and define

Regret_T=sum_{t=1}^T [f_0(X_t,a^*(X_t))-f_0(X_t,A_t)].

Expectations of regret are over the latent laws, contexts, rewards, and algorithmic randomization.

Exact posterior sampling draws a fresh vector from the posterior law of (f_0(x,1),...,f_0(x,K)) conditional on H, independently of the actual latent laws given the observed information, and chooses a maximizing coordinate. Denote that posterior vector law by S_t^Pi(.|x,H), and its induced action law by P_t^Pi(.|x,H). Use the smallest-index maximizer as the tie-breaking rule throughout.

An approximate Gaussian sampler instead draws independent coordinates with laws

G_{t,a}^{approx}(.|x,H)=N(mu_{t,a}^{approx}(x,H), V_{t,a}^{approx}(x,H)/s_a),

and applies the same maximizing rule. Its action law is Q_t(.|x,H). For comparison, let the Gaussian approximation based on the exact model have coordinate laws

G_{t,a}^Pi(.|x,H)=N(mu_{t,a}^Pi(x,H), V_{t,a}^Pi(x,H)/s_a).

Write G_t^{approx}=product_a G_{t,a}^{approx} and G_t^Pi=product_a G_{t,a}^Pi. The means are finite real-valued measurable parameter functions, and the variances and scales satisfy

0<V_{t,a}^{approx}(x,H)<infinity,   0<V_{t,a}^Pi(x,H)<infinity,   0<s_a<infinity.

These parameters use only the indicated observed information. The notation s_a may suppress dependence on t and the observed history H_a; the same scale is used for arm a in both Gaussian laws. The Gaussian draws use fresh randomization conditionally independent of the latent laws given the observed information. The parameter functions are specified on the admissible domains, including histories reached by the sampler.

For probability laws M,N on the same measurable space, define TV(M,N)=sup_E |M(E)-N(E)|. Put

epsilon_t=sup_{x,H} TV(Q_t(.|x,H),P_t^Pi(.|x,H)),

rho_t=sup_{x,H} TV(G_t^Pi(.|x,H),S_t^Pi(.|x,H)),

Delta_{t,a}(x,H)=mu_{t,a}^{approx}(x,H)-mu_{t,a}^Pi(x,H),

r_{t,a}(x,H)=V_{t,a}^{approx}(x,H)/V_{t,a}^Pi(x,H).

Assume that there is a finite constant B_R>=0 such that, for every finite admissible arm-specific history collection H,

sup_{x in X, a,a' in {1,...,K}} E_Pi[|f_0(x,a)-f_0(x,a')| | H] <= 2B_R.

## Task

Prove that, for every positive integer horizon T,

E[Regret_T^{approx}] <= E[Regret_T^{Pi-TS}] + 2B_R sum_{t=1}^T (T-t+1)epsilon_t,

and, simultaneously, for every t,

epsilon_t <= rho_t + (1/2) sup_{x,H} sqrt(sum_{a=1}^K [r_{t,a} + s_a Delta_{t,a}^2/V_{t,a}^Pi - 1 - log r_{t,a}]).

Here Regret_T^{Pi-TS} is the regret of exact posterior sampling and Regret_T^{approx} is the regret of the approximate Gaussian sampler, each in the specified Bayesian experiment. The suprema range over contexts and all finite admissible arm-specific history collections on which the displayed quantities are defined, and all terms inside a supremum are evaluated at the same x,H.
