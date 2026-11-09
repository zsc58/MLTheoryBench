# Problem

## Setup

Let p be a positive integer and K an index set. Let F: R^p → R and f_k: R^p → R, k ∈ K, be functions. Fix a point x* and a closed Euclidean ball B with x* in its interior. Assume F is C³ and every f_k is C² on an open neighborhood of B. Write A(x)=∇²F(x) and s(x)=λ_max(A(x)). Assume the largest eigenvalue is simple on that neighborhood, and let v(x) be a corresponding unit eigenvector.

Full-batch gradient descent with baseline step size h>0 has update x_{n+1}=x_n−h∇F(x_n). Consider a fork at the active boundary s(x*)=2/h. One branch, E, retains the baseline step size; the other, X, uses ρh, where 0<ρ<1. The comparison uses the common baseline-scaled clock u=h(n−n*), not a separately rescaled clock for each branch.

The assertions below concern the stipulated local slow-time description of these branches. They do not assert a discrete-to-continuous approximation theorem for arbitrary gradient-descent iterates.

Define, at the fork,

a=−⟨∇F(x*),∇s(x*)⟩,   b=∥∇s(x*)∥².

Assume a>0 and b>0, and define the oscillation scale d=√(2a/b). The symbol p denotes the parameter-space dimension; d denotes only this oscillation scale.

Assume the following conditions on a window 0≤u≤U, where U>0.

**A1. Local regularity.** The smoothness and simple-eigenvalue assumptions above hold. All slow-curve and phase locations specified below belong to B.

**A2. Assumed slow descriptions.** There are C¹ slow curves x_E,x_X:[0,U]→B with x_E(0)=x_X(0)=x*. The curve x_E lies on the regular part of M={x:s(x)=2/h} and follows Euclidean projected negative-gradient dynamics for F in the clock u. Here projected negative-gradient dynamics means that, at each point, its velocity is the tangent vector to M nearest in Euclidean distance to the negative Euclidean gradient of F. The curve x_X is ordinary negative-gradient dynamics with its algorithmic clock slowed by the factor ρ: if y satisfies y′(t)=−∇F(y(t)) and y(0)=x*, then x_X(u)=y(ρu). These are the assumed local descriptions, not conclusions to be proved about the discrete iterates.

**A3. Top-direction stable exit.** The exit satisfies ρh s(x*)<2. This condition concerns the top eigendirection and does not impose positivity of every Hessian eigenvalue.

**A4. Short-window Taylor condition.** For each j∈{E,X} and each map G in the collection {∇F,A}∪{∇f_k:k∈K}, there is a finite constant M_{G,j}, independent of u, such that

G(x_j(u))=G(x*)+DG(x*)[x_j(u)−x*]+R_{G,j}(u),

with ∥R_{G,j}(u)∥≤M_{G,j}u². Here DG is the derivative of the indicated vector- or matrix-valued map, and the norm is its Euclidean or operator norm. No Taylor condition on ∇s is additionally assumed.

**A5. Phase observations and averaging.** At a fixed slow time u, let x_j⁺(u),x_j⁻(u) be the two phase locations used for branch j's cycle average, and put e_j⁺(u)=x_j⁺(u)−x_j(u) and e_j⁻(u)=x_j⁻(u)−x_j(u). There are finite constants M_j, independent of u, for which

∥e_j⁺(u)∥≤M_j d,   ∥e_j⁻(u)∥≤M_j d,

and

∥(e_j⁺(u)+e_j⁻(u))/2∥≤M_j d².

These conditions specify the amplitude control and cancellation of the leading alternating phase in the local description. A branch with no fast phase may have both phase displacements zero. Define the equal-weight cycle average and the exit-minus-baseline difference by

bar f_{k,j}(u)=[f_k(x_j⁺(u))+f_k(x_j⁻(u))]/2,

bar Δf_k(u)=bar f_{k,X}(u)−bar f_{k,E}(u).

Finally, define the fork scores

r_k=⟨∇f_k(x*),∇F(x*)⟩,   q_k=⟨∇f_k(x*),∇s(x*)⟩.

## Task

Prove that, for every k and all sufficiently small u≥0 in the specified window,

bar Δf_k(u)=[(1−ρ)r_k+(a/b)q_k]u+O_k(u²)+O_k(d²).

More explicitly, there is a sufficiently small U₀∈(0,U] such that, for each k, finite constants C_k,D_k satisfy

|bar Δf_k(u)−[(1−ρ)r_k+(a/b)q_k]u|≤C_k u²+D_k d²

for 0≤u≤U₀. Constants may depend on the fixed local data, subset, local smoothness bounds, phase bounds, and chosen window, but not on u. No uniformity over different forks or an amplitude-indexed family is asserted. The two displayed linear contributions are respectively the learning-rate slowdown contribution and the sharpness-selector contribution.
