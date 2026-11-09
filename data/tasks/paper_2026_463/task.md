# Problem

## Setup

Let S be a nonempty finite alphabet, and let D and K be positive integers. Let p_1 be a probability distribution on S^D. For each coordinate d, let ρ_d be a probability distribution on S, and put p_0(x)=∏_{d=1}^D ρ_d(x^d). Neither the coordinate distributions nor p_1 are required to have full support.

Let κ:[0,1]→[0,1] be continuous and nondecreasing, with κ_0=0 and κ_1=1. Fix δ∈(0,1), put H=1-δ, and assume κ_t<1 on [0,H]. Assume κ is differentiable there and that α_t=κ̇_t/(1-κ_t) is continuous. Fix a deterministic partition 0=t_0<⋯<t_K=H and write I_k=[t_{k-1},t_k] and τ_k=t_k-t_{k-1}.

For t∈[0,H], define

c_t(x|u)=∏_{d=1}^D [(1-κ_t)ρ_d(x^d)+κ_t 1{x^d=u^d}],

p_t(x)=∑_{u∈S^D}p_1(u)c_t(x|u).

For p_t(x)>0, define the coordinate posterior

r_t^d(a|x)=p_{1|t}^d(a|x)= [∑_{u∈S^D:u^d=a}p_1(u)c_t(x|u)]/p_t(x).

Thus the posterior is defined by the experiment that draws u from p_1 and then draws x from c_t(·|u). At states with p_t(x)=0, fix versions of r_t^d(·|x) that are probability distributions on S. Assume the selected versions are differentiable in time and satisfy

L_k^p=sup_{t∈I_k, d∈{1,…,D}, x∈S^D, a∈S\{x^d}} |∂_t r_t^d(a|x)|<∞.

Derivatives at interval endpoints are interpreted one-sidedly. If |S|=1, set L_k^p=0.

For x∈S^D, let x^{d→a} be x with coordinate d replaced by a. Define the oracle generator by

Q_t(x,x^{d→a})=α_t r_t^d(a|x),  a≠x^d.

All other off-diagonal entries are zero, and each diagonal entry is minus the sum of its row's off-diagonal entries. Let X be the continuous-time Markov chain with this generator and initial distribution p_0.

Define

M_k=sup_{t∈I_k} α_t<∞,

and assume max_k τ_k D M_k≤log 2.

## The Two Samplers

The following rule is restarted on every interval I_k. For a sampler path Y, let T_k be its first actual jump after t_{k-1} within that interval, with T_k=∞ if there is no such jump. When T_k<∞, write y_k=Y_{T_k} for its post-jump state. At time s, set x=Y_{s-}.

The oracle location-corrected sampler uses the predictable off-diagonal rates

Q_s^{LC}(x,x^{d→a};Y)=α_s r_{t_{k-1}}^d(a|x),  if s≤T_k,

Q_s^{LC}(x,x^{d→a};Y)=α_s 1{x^d=y_k^d} r_{T_k}^d(a|y_k),  if s>T_k,

for a≠x^d. Other off-diagonal rates vanish, and diagonals make row sums zero. In particular, the schedule factor remains evaluated at s in both stages.

Let θ denote estimator randomness. Conditional on θ, let estimated posterior vectors r̂_{t,θ}^d(·|x) be probability distributions on S, jointly measurable in their arguments. The estimated sampler uses the same rule, with every r replaced by r̂_θ and with its first-jump time and anchor determined by its own path. Assume these rates are predictable. Denote its conditional terminal distribution by p̂_{H,θ}^{LC}.

Both samplers start from p_0. Their initialization and fresh sampling randomness are independent of θ. The oracle path law P^{LC} therefore does not depend on θ. Write Q̂_{s,θ}^{LC} for the estimated rate as a functional of a canonical path; in comparisons of rates, both rate functionals are evaluated on that same path history.

For a,b≥0, define

D_F(a||b)=a log(a/b)-a+b,

with D_F(0||b)=b, D_F(0||0)=0, and D_F(a||0)=∞ when a>0. For each θ, let

K(θ)=E_{P^{LC}}[∫_0^H ∑_{z∈S^D:z≠Y_{s-}} D_F(Q_s^{LC}(Y_{s-},z;Y)||Q̂_{s,θ}^{LC}(Y_{s-},z;Y)) ds].

Let ε_Est^{LC}∈[0,∞) and assume

E_θ K(θ)=2(ε_Est^{LC})^2<∞.

Total variation on S^D is TV(μ,ν)=(1/2)∑_{x∈S^D}|μ(x)-ν(x)|. All logarithms are natural, and a∨b means max{a,b}.

## Task

Prove the following explicit logarithmic form of the location-corrected error bound:

E_θ[TV(p_H,p̂_{H,θ}^{LC})]
≤ [2|S| ∑_{k:M_k>0} (D^3 τ_k^3 M_k^3 ∨ D τ_k^2 M_k L_k^p) {2+log((τ_k D M_k)^(-2))}]^(1/2) + ε_Est^{LC}.

Intervals with M_k=0 contribute zero, and an empty sum is zero. For M_k>0, the nonlogarithmic summand is equivalently D^3 τ_k^3 M_k^3 {1∨L_k^p/(τ_k D^2 M_k^2)}; hence this is the square-root cubic-step/rate guarantee with its logarithmic factor stated explicitly.
