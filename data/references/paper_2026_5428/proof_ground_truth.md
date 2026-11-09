# Reference Proof

## Contract and Proof Obligations

The claim is a deterministic, one-sided regret upper bound for the exact learner in the public task. Predictions and losses both belong to [0,1]^K; consequently |e_t(i)|≤1. Comparators and the consecutive partition are arbitrary and need not be known to the learner. There are no probabilistic or independence assumptions. Write B=log(KMT), q_t(h)=Σ_i x'_t(i,h), and α=KMδ=T^{-3}. All logarithms in the proof are natural.

The obligations are: establish that the learner is defined throughout the horizon; justify the optimistic mirror inequality with possibly infeasible positive centers; derive the active-layer interval bound including its large-update and floor terms; telescope the layer masses and bound the signed penalties from above; select a valid conservative grid rate with short-horizon cases covered; and prove the benign bound with uniform treatment of the remainder. Each obligation is derived below. No paper-specific theorem or specialized external method is used as an unexplained black box.

## 1. Feasibility, Initialization, and Short Horizons

Whenever A_t is nonempty, Ω_t is nonempty: put δ on every coordinate and put the remaining mass 1-α on one active coordinate. It is compact and convex, and every coordinate is positive. The objective functions are continuous and strictly convex on this set, so their minimizers exist and are unique. Their centers need only be positive, not members of Ω_t. The active mass is

1-K(M-|A_t|)δ≥1-α>0,

so p_t is defined and belongs to Δ_K.

For T≥4, the first layer satisfies 32γ_1=4/T≤1. Its penalty increment is always zero because |e_t(i)|≤1. Starting from H_1(1)=0, induction therefore keeps this layer active and makes every round well defined.

For T=2,3, argue inductively instead. At each already defined round,

Σ_h d_t(h)≤Σ_{i,h}x_t(i,h)|e_t(i)|≤1,

hence Σ_h H_t(h)≤t-1. Here M is respectively 2 or 4, and t-1<M throughout the horizon. If all layers were inactive, every H_t(h) would exceed 1 and their sum would exceed M, a contradiction. Thus these horizons are also well defined. Their total regret is at most T≤3log T. This proves both claimed upper bounds for T=2,3, with the second understood conditionally on its premise. No conservative grid point below 1/32 is required for these cases.

We also need the correct bound on initialization. It is not generally true that x'_1(i,h)≥δ. Direct summation gives

min_{i,h} x'_1(i,h)=3/[K(4^M-1)]>3/(4KT^4)≥(KMT)^{-4}.

The last inequality uses K≥1 and M≥2. For a≥2, every x'_a is the output of a constrained update and has every coordinate at least δ≥(KMT)^{-4}. Consequently, for every 1≤a≤T+1,

0<x'_a(i,h)≤1,  log(1/x'_a(i,h))≤4B.                 (1)

This is the logarithmic estimate needed below; the initialization itself must not be altered.

## 2. The Standard Mirror Inequality, Derived

Let C be a nonempty compact convex set of positive vectors, z a positive center, x a minimizer of ⟨m,w⟩+D_Ψ(w,z) over C, and y a minimizer of ⟨L,w⟩+D_Ψ(w,z) over C. The generator is differentiable on the positive orthant. First-order optimality and the Bregman three-point identity give, for u∈C,

⟨L,y-u⟩≤D_Ψ(u,z)-D_Ψ(u,y)-D_Ψ(y,z),

⟨m,x-y⟩≤D_Ψ(y,z)-D_Ψ(y,x)-D_Ψ(x,z).

Adding these inequalities and separating L-m yields

⟨L,x-u⟩≤⟨L-m,x-y⟩+D_Ψ(u,z)-D_Ψ(u,y)
                 -D_Ψ(y,x)-D_Ψ(x,z).               (2)

The derivation does not require z∈C. In our application C=Ω_t, z=x'_t, x=x_t, y=x'_{t+1}, m=tilde-m_t, and L=tilde-ℓ_t+a_t. Section 1 verifies every domain, differentiability, existence, and positivity hypothesis, including after a change of active set.

## 3. An Active-Layer Interval Inequality

Fix I=[a,b], u∈Δ_K, and a layer j active throughout I. Let n=|I| and E=max_{1≤t≤T}||e_t||_∞. Define the fixed expanded comparator

ū(i,h)=δ+(1-α)u(i)1{h=j}.

Its mass is one and it belongs to Ω_t for every t∈I. This assertion is needed only on I, not on the entire horizon.

Let β_t=K(M-|A_t|)δ be the inactive mass, and let μ_t=K^{-1}Σ_iℓ_t(i). The full expanded prediction satisfies the exact identity

⟨tilde-ℓ_t,x_t⟩=(1-β_t)⟨ℓ_t,p_t⟩+β_t μ_t.

The expanded comparator loss is (1-α)⟨ℓ_t,u⟩+αμ_t. Since all these losses lie in [0,1],

|⟨ℓ_t,p_t-u⟩-⟨tilde-ℓ_t,x_t-ū⟩|≤β_t+α≤2/T³.   (3)

In particular, normalization does not give exact equality with the replicated loss when inactive layers are present.

Apply (2), subtract ⟨a_t,x_t-ū⟩, and discard the nonpositive term -D_Ψ(x_t,x'_t). With v_t=tilde-ℓ_t-tilde-m_t+a_t, this gives

⟨tilde-ℓ_t,x_t-ū⟩≤D_Ψ(ū,x'_t)-D_Ψ(ū,x'_{t+1})+F_t,

where

F_t=⟨v_t,x_t-x'_{t+1}⟩-D_Ψ(x'_{t+1},x_t)-⟨a_t,x_t-ū⟩.

### 3.1. Potential Difference

For positive z and nonnegative y, using 0log0=0 when necessary,

D_Ψ(y,z)=Σ_{i,h}[y(i,h)log(y(i,h)/z(i,h))-y(i,h)+z(i,h)]/γ_h.

The comparator is fixed on I, so the potential differences telescope exactly to

Σ_{i,h} ū(i,h)log(x'_{b+1}(i,h)/x'_a(i,h))/γ_h
 +Σ_h(q_a(h)-q_{b+1}(h))/γ_h.

By (1), every logarithmic ratio is at most 4B. Also

Σ_h1/γ_h=16TΣ_{h=1}^M2^{-h}<16T.

The logarithmic part is therefore at most

4B/γ_j+4BKδΣ_h1/γ_h
≤4B/γ_j+32B/T².                                    (4)

There is one layer-mass boundary term, not one copy per round.

### 3.2. Small and Large Updates

For a coordinate with weight x>0, rate γ, and effective loss difference v, direct maximization over w≥0 gives

sup_{w≥0}{v(x-w)-[wlog(w/x)-w+x]/γ}
=x[γv-1+exp(-γv)]/γ,                               (5)

with maximizer w=xexp(-γv). Relaxing the feasible set to the nonnegative orthant makes (5) an upper bound on the corresponding stability term.

Write r=e_t(i), so v=r+32γr². If 32γ|r|≤1, then |v|≤2|r| and |γv|≤1/16. Taylor's integral remainder gives

exp(-z)-1+z=z²∫_0^1(1-s)exp(-sz)ds≤z²

for |z|≤1/16. Consequently (5) is at most 4γxr².

If 32γ|r|>1, then v≥(32γ|r|-1)|r|>0. Thus exp(-γv)≤1, and (5) is at most

xv=32γxr²+xr.

Combining the cases coordinatewise yields the valid common bound

32γxr²+1{32γ|r|>1}xr.

The common coefficient must be 32, not 4. Summing and subtracting the correction gives

F_t≤⟨a_t,ū⟩+Σ_h d_t(h).

Since Σ_hγ_h<2γ_M<T/4,

⟨a_t,ū⟩
≤32γ_jΣ_i u(i)e_t(i)²+32KδΣ_hγ_h||e_t||_∞²
≤32γ_jΣ_i u(i)e_t(i)²+8||e_t||_∞²/T².             (6)

This also shows precisely where the floor residual enters: it is the correction evaluated on the smoothed comparator, not an exception to the exponential estimate.

Combining (3), (4), and (6), we obtain

Σ_{t=a}^b⟨ℓ_t,p_t-u⟩
≤4B/γ_j+32γ_jΣ_{t=a}^bΣ_i u(i)e_t(i)²
 +Σ_h(q_a(h)-q_{b+1}(h))/γ_h
 +Σ_{t=a}^bΣ_h d_t(h)+E_I,                         (7)

where the nonnegative remainder can be taken as

E_I=32B/T²+8|I|E²/T²+2|I|/T³.                     (8)

This is the repaired interval-length-dependent remainder. For arbitrary K it must not be described as uniformly O(1/T), because B can be arbitrarily large.

## 4. Global Bookkeeping

Apply (7) on each consecutive interval with any layer active throughout that interval. Consecutiveness gives

Σ_sΣ_h(q_{a_s}(h)-q_{b_s+1}(h))/γ_h
=Σ_h(q_1(h)-q_{T+1}(h))/γ_h
≤Σ_hq_1(h)/γ_h.

Initialization gives q_1(h)=γ_h²/Σ_kγ_k², hence

Σ_hq_1(h)/γ_h=(Σ_hγ_h)/(Σ_hγ_h²)
≤2/γ_M≤32/T.                                      (9)

For a fixed layer h, let τ(h) be its last active round. Such a round exists because every layer is active at round 1. At that round H_{τ(h)}(h)≤1 and d_{τ(h)}(h)≤1. On each subsequent round, all K coordinates on that layer equal δ, so its upward increment is at most Kδ. Therefore

H_{T+1}(h)≤2+TKδ=2+1/(MT²).

This reasoning permits negative increments and reactivation before the last active round. It is an upper bound, not an assertion that |H_{T+1}(h)| is bounded. Consequently

Σ_{t=1}^TΣ_h d_t(h)=Σ_hH_{T+1}(h)≤2M+1/T²
≤C log T.                                         (10)

Since Σ_s|I_s|=T and E≤1, the remainders satisfy

Σ_s E_{I_s}≤32SB/T²+8/T+2/T².                     (11)

Thus for any intervalwise active rates, the total regret is at most

Σ_s(4B/γ_{j_s}+32γ_{j_s}Q_s)
 +C log T+C SB/T²+C/T.                            (12)

The two regimes below absorb (11) explicitly rather than assuming a growth restriction on K.

## 5. Worst-Case Rate Selection

The cases T=2,3 were settled in Section 1. Assume T≥4. For each interval set

r_s=min{1/32,sqrt(B/(8Q_s))},

with the second expression interpreted as +∞ for Q_s=0. We have Q_s≤|I_s|≤T. Moreover γ_1=1/(8T)≤1/32, sqrt(B/(8T))≥γ_1, and γ_M≥T/16>1/32. Hence the geometric grid contains a rate satisfying

γ_{j_s}≤r_s<2γ_{j_s}.

Because γ_{j_s}≤1/32, its penalty increment is zero at every round; it remains active over the entire horizon.

If r_s=sqrt(B/(8Q_s)), reciprocal-linear balancing gives

4B/γ_{j_s}+32γ_{j_s}Q_s≤C sqrt(BQ_s).

If r_s=1/32, then Q_s≤128B and γ_{j_s}≥1/64, giving instead

4B/γ_{j_s}+32γ_{j_s}Q_s≤C B.

Therefore in all cases

4B/γ_{j_s}+32γ_{j_s}Q_s≤C(B+sqrt(BQ_s)).           (13)

In (12), SB/T²≤SB, log T≤B≤SB, and 1/T is also absorbed. Thus

R≤C(SB+Σ_s sqrt(BQ_s)).                            (14)

Finally M≤T² for T≥2, so

log(KT)≤B≤3log(KT).

Substitution in (14) proves the first public bound, even without additional suppressed log log T factors.

## 6. Benign Active-Rate Selection

Let c_->0 and c_+<∞ be the fixed absolute comparison constants in the premise. Thus each stipulated active rate satisfies

c_-sqrt(B/Q_s)≤γ_{j_s}≤c_+sqrt(B/Q_s).

Since all grid rates are finite, the extended-real convention makes this premise impossible when any Q_s=0. On instances satisfying it, every Q_s is positive and

4B/γ_{j_s}+32γ_{j_s}Q_s
≤(4/c_-+32c_+)sqrt(BQ_s).                          (15)

The remaining logarithmic floor term in (12) is also absorbed uniformly in K. Indeed γ_{j_s}≤γ_M<T/8 and the lower comparison inequality imply

sqrt(BQ_s)≥c_- B/γ_{j_s}≥8c_- B/T.

Consequently

SB/T²≤[1/(8c_-T)]Σ_s sqrt(BQ_s).                  (16)

Combining (12), (15), and (16), and absorbing 1/T into log T, yields

R≤C_{c_-,c_+}(log T+Σ_s sqrt(BQ_s)).

Using B≤3log(KT) proves the second public bound. The constant depends only on the fixed absolute comparison constants, not on any instance parameter. This argument retains the shared global penalty while removing the per-interval logarithmic term.

## Completion and Source Repairs

All obligations listed at the start are closed. The standard mirror inequality was derived from first-order optimality; the distinctive large-update estimate, normalization error, initialization logarithms, signed-penalty control, both rate regimes, and all boundary cases were established explicitly. The proof retains the prior consecutive-interval and remainder repairs and additionally corrects the source's common-center notation, repeated boundary summation, normalization identities, initialization-floor assertion, combined coefficient, inactive Kδ contribution, and short-horizon rate-selection oversight. None changes the public algorithm or its two source-faithful upper-bound targets. No unresolved private proof dependency remains.
