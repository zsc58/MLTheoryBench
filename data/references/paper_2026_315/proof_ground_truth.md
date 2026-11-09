# Reference Proof

Write a=1∧β, b_n=n^(−2β/(2β+d)), and A_δ(s)=∫_𝒳 E M_δ(x,s)dx. All risk bounds below are uniform in δ≥0. Distinctness of the observed design points holds almost surely; interpolation is asserted on this probability-one event.

## Lower bound

For f*=0, interpolation gives |f̂(X_i)|≥(|ξ_i|−δ)_+. Every X_i∈B_p(x,r) is an allowable attacked point when the fresh input is x. Hence, for every f̂∈𝓘(δ), the density lower bound and Tonelli's theorem give R_r(f̂,0)≥μ_under A_δ(r).

Here is a direct derivation of the remaining unrestricted benchmark, avoiding a paper-specific prior theorem. First, R_r≥R_0. To lower-bound the latter, set m=⌈n^(1/(2β+d))⌉ and h=1/m, and partition the cube into m^d cubes Q_j of side h. Fix a nonzero smooth bump φ supported strictly inside (0,1)^d and, in Q_j with corner u_j, set a_j(z)=εh^β φ((z−u_j)/h), extended by zero. For sufficiently small fixed ε, every f_θ=∑_j θ_j a_j, θ_j∈{0,1}, belongs to 𝓗(β,L): derivatives of order at most k=⌈β⌉−1 and the (β−k)-Hölder seminorm of the kth derivatives are bounded uniformly in h, including across the separated supports.

Let P_θ be the law of the n training pairs under f_θ. If θ and θ^(j) differ only at j, the Gaussian conditional-density calculation gives their Hellinger affinity as

∫√(dP_θ dP_{θ^(j)}) = [∫ exp{−a_j(x)²/(8σ²)}P_X(dx)]^n ≥ 1−n∫a_j²dP_X/(8σ²).

Since nh^(2β+d)≤1 and ∫a_j²dP_X≤Cε²h^(2β+d), choose ε so this affinity exceeds 15/16. Cauchy–Schwarz applied to the square-root densities then bounds the total-variation distance by √(1−(15/16)²)<1/2. Given an arbitrary estimator, decode θ_j by choosing whichever of 0 and a_j is nearer to its restriction to Q_j in L²(P_X). A decoding error forces squared estimation error on Q_j of at least (1/4)∫a_j²dP_X≥cε²h^(2β+d). For each adjacent pair of parameters, the two decoding-error probabilities sum to at least one minus their total-variation distance, hence at least 1/2. Average over all θ and sum over j. This proves sup_{f*∈𝓗}R_0(f̂,f*)≥c m^d h^(2β+d)≥c′b_n for every estimator.

For the attack contribution, suppose r>0 and put t=min{r/2,1/4}. For every x with x_1≤1−t, both x and y=x+te_1 can be attacked at their common midpoint z=x+(t/2)e_1. Pointwise,

[f̂(z)−f(x)]²+[f̂(z)−f(y)]² ≥ [f(x)−f(y)]²/2.

Integrating the two risks over x and over its translate, and using the density lower bound, yields R_r(f̂,f)≥(μ_under/4)∫_{[0,1−t]×[0,1]^(d−1)}[f(x)−f(x+te_1)]²dx. For 0<β≤1 take f(x)=c₀t^β cos(πx_1/t); its 𝓗(β,L) bound is uniform in t, and the last integral is at least c t^(2β). For β>1 take f(x)=c₀x_1, giving c t². Choose c₀ small enough for membership in the class. Because r≤R, t^(2a)≥c_R r^(2a). The claim is trivial for r=0. Thus sup_f R_r(f̂,f)≥c_R r^(2a). Combining this, the estimation bound, and the zero-function penalty by max{u,v,w}≥(u+v+w)/3 proves the asserted minimax lower bound.

## Interpolating construction and upper bound

Let ψ_δ(v)=sgn(v)(|v|−δ)_+. For τ>0, choose measurably a nearest design point X_{i(z)} to z, breaking ties by index. If its distance is at most τ, define

f̂_{δ,τ}(z)=f̃(z)+ψ_δ(Y_{i(z)}−f̃(X_{i(z)}))(1−‖z−X_{i(z)}‖_p/τ)_+;

otherwise set f̂_{δ,τ}(z)=f̃(z). For τ=0, change f̃ only at the distinct X_i, setting f̂_{δ,0}(X_i)=f̃(X_i)+ψ_δ(Y_i−f̃(X_i)). These are jointly measurable and equal f̃ outside the respective unions of τ-balls. At X_i the training residual has magnitude min{|Y_i−f̃(X_i)|,δ}, so both constructions belong to 𝓘(δ).

At any z, the magnitude of the correction is at most max_{i∈S_p(z,τ)}(|Y_i−f̃(X_i)|−δ)_+, with zero for an empty set. Thus, for a fresh input fixed at x, every correction visible within B_p(x,r) is bounded using indices in S_p(x,r+τ). Since

(|Y_i−f̃(X_i)|−δ)_+² ≤ 2(|ξ_i|−δ)_+²+2|f̃(X_i)−f*(X_i)|²,

the base-estimator hypothesis and |f*(z)−f*(x)|≤C‖z−x‖_p^a imply

sup_{f*}R_r(f̂_{δ,τ},f*) ≤ C{(r+τ)^(2a)+b_n+A_δ(r+τ)}

whenever r+τ≤s₀. This also holds, with a constant depending on R and s₀, for larger r+τ and sufficiently small τ: finitely many s₀-balls cover 𝒳, so the hypothesis bounds E sup_{z∈𝒳}|f̃(z)−f*(z)|² by a constant; in this case (r+τ)^(2a) is bounded below by a positive constant. Integrating pointwise bounds against P_X uses its density upper bound.

It remains to justify the radius comparison rather than merely assert it. Let W=(|ξ_1|−δ)_+², let q_x(s)=P_X(B_p(x,s)∩𝒳), and define F_n(q)=E max_{1≤i≤n} B_iW_i for independent Bernoulli(q) indicators B_i and independent copies W_i of W. Independence of the Gaussian errors and design yields E M_δ(x,s)=F_n(q_x(s)). Moreover,

F_n(q)=∫₀^∞[1−(1−q P(W>u))^n]du.

This is increasing and concave in q, with F_n(0)=0, so F_n(q′)≤(q′/q)F_n(q) when q′≥q>0. If r≥τ>0, convexity of the cube and dilation about x give |𝒳∩B_p(x,r+τ)|≤2^d|𝒳∩B_p(x,r)|. Consequently q_x(r+τ)≤2^d(μ_over/μ_under)q_x(r), and A_δ(r+τ)≤C A_δ(r). The same conclusion is immediate when τ=0.

If 0≤r<τ, then r+τ<2τ. Bounding a nonnegative maximum by its sum, applying Tonelli, and using independence gives

A_δ(r+τ)≤∑_{i=1}^n E W_i∫_𝒳1{‖X_i−x‖_p≤2τ}dx ≤ nσ² v_p(2τ)^d,

where v_p is the volume of the unit p-ball. This also covers empty neighborhoods and r=0. Thus in every case A_δ(r+τ)≤C{A_δ(r)+nτ^d}.

For a sequence in the question, τ_n^(2a)≲b_n by its first exponent, and nτ_n^d≲b_n by its second. Also (r+τ_n)^(2a)≤C(r^(2a)+τ_n^(2a)). Substitution proves sup_f R_r(f̂_{δ,τ_n},f)≤C{r^(2a)+b_n+A_δ(r)}, matching the lower bound. The base estimator's existence is an explicit hypothesis; neither this proof nor the minimax lower bound treats a cited paper-specific prior theorem as a closed obligation.
