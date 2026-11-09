# Problem

## Setup

Let N≥2 and T≥1 be integers, and let B>0. There are N experts. On round j, the learner chooses a probability vector p_j using the losses revealed on earlier rounds. Nature then reveals a vector ℓ_j∈R^N satisfying

max_{i,k}|ℓ_{j,i}−ℓ_{j,k}|≤B.

The learner incurs loss ⟨p_j,ℓ_j⟩. Define cumulative regrets and their nonnegative parts by

x_{0,i}=0,  Δx_{j,i}=⟨p_j,ℓ_j⟩−ℓ_{j,i},  x_{j,i}=x_{j−1,i}+Δx_{j,i},  y_{j,i}=max{x_{j,i},0}.

For z∈R and t>0, define

φ(z,t)=t^(−1/2) exp(z²/(2t)),    Φ(y,t)=∑_{i=1}^N φ(y_i,t).

Set

t_0=max{512 e² B² log N,1}.

On each round j, let

p_{j,i}=φ_x(y_{j−1,i},t_{j−1}) / ∑_{k=1}^N φ_x(y_{j−1,k},t_{j−1})

when the denominator is positive; otherwise let p_j be uniform. Also define

q_{j,i}=φ_xx(y_{j−1,i},t_{j−1}) / ∑_{k=1}^N φ_xx(y_{j−1,k},t_{j−1}).

After updating x_j and y_j, choose the unique Δt_j≥0 satisfying

Φ(y_j,t_{j−1}+Δt_j)=Φ(y_{j−1},t_{j−1}),

and set t_j=t_{j−1}+Δt_j. Define

V_T=∑_{j=1}^T ∑_{i=1}^N q_{j,i}(Δx_{j,i})².

Write x_{T,(1)}≥⋯≥x_{T,(N)} for the cumulative regrets in decreasing order. For 0<ε≤1, define

Regret_ε(T)=x_{T,(⌈Nε⌉)}.

All logarithms are natural.

## Task

Prove that the update is well-defined and that, for every allowed loss sequence and every 0<ε≤1,

Regret_ε(T)≤sqrt((t_0+2V_T)[log((t_0+2V_T)/t_0)+2 log(1/ε)]).
