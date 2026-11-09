# Problem

## Setup

Let K≥1 and T≥2 be integers, let [K]={1,…,K}, and let Δ_K be the probability simplex in R^K. Over rounds t=1,…,T, a learner first receives a prediction vector m_t∈[0,1]^K, chooses p_t∈Δ_K, then observes ℓ_t∈[0,1]^K and incurs ⟨ℓ_t,p_t⟩. Write e_t=ℓ_t-m_t.

Consider the following safeguarded multi-rate mirror learner. Set

M=⌈log₂(T²)⌉,  δ=1/(KMT³),  γ_j=2^j/(16T),  j=1,…,M,

and define

Ψ(x)=Σ_{i=1}^KΣ_{j=1}^M x(i,j)log(x(i,j))/γ_j,

with its Bregman divergence D_Ψ. Initialize

x'_1(i,j)=γ_j²/(KΣ_{h=1}^Mγ_h²),  H_1(j)=0.

At round t, let

A_t={j∈{1,…,M}:H_t(j)≤1}

and let Ω_t be the subset of the KM-dimensional probability simplex consisting of vectors x satisfying x(i,j)≥δ for j∈A_t and x(i,j)=δ for j∉A_t. Define replicated vectors tilde-m_t,tilde-ℓ_t∈R^{K×M} by

tilde-m_t(i,j)=m_t(i),  tilde-ℓ_t(i,j)=ℓ_t(i).

Compute

x_t∈argmin_{x∈Ω_t}{⟨tilde-m_t,x⟩+D_Ψ(x,x'_t)}.

Predict with the normalized active-layer marginal

p_t(i)= [Σ_{j∈A_t}x_t(i,j)]/[Σ_{k=1}^KΣ_{j∈A_t}x_t(k,j)].

After observing ℓ_t, set

a_t(i,j)=32γ_j e_t(i)²

and compute

x'_{t+1}∈argmin_{x∈Ω_t}{⟨tilde-ℓ_t+a_t,x⟩+D_Ψ(x,x'_t)}.

Finally define

d_t(j)=Σ_{i=1}^K 1{32γ_j|e_t(i)|>1}x_t(i,j)e_t(i),

and update H_{t+1}(j)=H_t(j)+d_t(j).

Let {I_1,…,I_S} be a partition of {1,…,T} into consecutive intervals, choose u_s∈Δ_K for each interval, and set

Q_s=Σ_{t∈I_s}Σ_{i=1}^K u_s(i)e_t(i)².

All constants in O(·) and Θ(·) below are absolute and uniform in K,T,S, the vectors, the partition, and the comparators. The two comparison constants in the Θ premise are fixed uniformly over all intervals; the implicit constant in its conclusion may depend on those fixed comparison constants. The displayed O-bounds may suppress factors depending only on log log T. When Q_s=0, interpret sqrt(log(KMT)/Q_s)=+∞. Each expression R≤O(F) below denotes a one-sided upper bound R≤CF with the stated constant convention, not an absolute-value bound on R.

## Task

Prove the following integrated switching-regret guarantee:

1. For every sequence of prediction and loss vectors, every consecutive-interval partition, and every choice of comparators,

Σ_{s=1}^SΣ_{t∈I_s}⟨ℓ_t,p_t-u_s⟩
≤O(Slog(KT)+Σ_{s=1}^S√(log(KT)Q_s)).

2. Moreover, suppose that for every s there is a layer j_s such that

γ_{j_s}=Θ(√(log(KMT)/Q_s))

and j_s∈A_t for every t∈I_s. Then

Σ_{s=1}^SΣ_{t∈I_s}⟨ℓ_t,p_t-u_s⟩
≤O(log T+Σ_{s=1}^S√(log(KT)Q_s)).
