# Reference Proof

## Contract and repairs

The playing weights p are proportional to the first spatial derivative at the projected cumulative regrets. The weights q in V_T are proportional to the second spatial derivative at the same pre-round state. They are not interchangeable. The potential φ(z,t)=t^(−1/2)exp(z²/(2t)) is smooth for every real z and positive t. Projection is applied to cumulative regret, not to time and not recursively to an already projected regret vector.

The source-local repairs used below are explicit: the quantile uses the ceiling rank required by the counting argument; zero time increments are allowed; the linear time term in the Taylor expansion has coefficient −1/2; the mixed space-time Hessian term is retained; and the invariant and final summation use their correct normalizations. No stronger loss assumption or larger initialization is introduced.

## 1. Well-defined updates and the potential invariant

Fix one round. Write x for the raw cumulative regret, y=[x]_+, t for the current time, and r_i=⟨p,ℓ⟩−ℓ_i for the actual regret increment. The loss-range assumption gives |r_i|≤B. Since p is a probability vector, ∑_i p_i r_i=0. Consequently

∑_i φ_x(y_i,t) r_i=0,

including the case in which every first derivative vanishes.

For fixed t, the function H_t(z)=φ([z]_+,t) is convex and continuously differentiable, with derivative H_t'(z)=φ_x([z]_+,t). Therefore the supporting-hyperplane inequality gives

∑_i H_t(x_i+r_i)≥∑_i H_t(x_i)+∑_i H_t'(x_i)r_i=Φ(y,t).

For fixed finite coordinates, the total potential is continuous and strictly decreasing in positive time and tends to zero as time tends to infinity. The current potential is positive. Thus there is a unique finite δ≥0 such that

Φ([x+r]_+,t+δ)=Φ(y,t).

The value δ can be zero; in particular it is zero on a round with identical expert losses. The q denominator is strictly positive because φ_xx(z,t)=(1/t+z²/t²)φ(z,t)>0. Hence both distributions and the entire update are well-defined.

Inductively,

Φ(y_j,t_j)=N/sqrt(t_0),    t_j≥t_0.

This is an invariant of the actual projected algorithm.

## 2. A valid smooth comparison and the corrected Taylor identity

Define an auxiliary increment d coordinatewise by

- d_i=r_i if x_i>0;
- d_i=[x_i+r_i]_+ if x_i≤0.

Then [y+d]_+=[x+r]_+, |d_i|≤|r_i|, and ∑_i φ_x(y_i,t)d_i=0. The last equality holds because φ_x(0,t)=0 on every coordinate where d differs from r.

Let F(z,u)=∑_i φ(z_i,u), defined on R^N×(0,∞), without clipping its argument. Convexity in z and the cancellation show F(y+d,t)≥F(y,t). Strict decrease in time and the zero limit therefore give a unique smooth comparison increment s≥0 such that

F(y+d,t+s)=F(y,t).

Since φ([z]_+,u)≤φ(z,u), the actual equalizer satisfies δ≤s. This comparison does not incorrectly identify [x+r]_+ with [y+r]_+.

At the base point (y,t), set

F=F(y,t),  S=∑_i φ_xx(y_i,t),  U=∑_i φ_xxx(y_i,t)d_i,

m=∑_i q_i d_i²,  a=U/S,

D=(∑_i φ_xxxx(y_i,t))/(4S)−S/(4F).

Here q_i=φ_xx(y_i,t)/S, and m≤∑_i q_i r_i². Put f=log F. The smooth potential satisfies φ_t=−φ_xx/2 and φ_tt=φ_xxxx/4. For a trial time increment v≥0 and h=(d,v), Taylor's theorem gives a point on the corresponding segment such that

f(y+d,t+v)−f(y,t)=−Sv/(2F)+(1/2)∇²f(midpoint)[h,h].

At the base point the exact Hessian identity is

(F/S)∇²f(y,t)[h,h]=m−v a+v²D.

Indeed, ∇²F[h,h]=∑_i φ_xx d_i²−v∑_i φ_xxx d_i+(v²/4)∑_i φ_xxxx, while ∇F·h=−Sv/2. The term −v a must not be discarded: cancellation of ∑_i φ_x d_i at one point does not imply cancellation of its time derivative with d held fixed.

Consequently, if the segment Hessian is at most C times the base Hessian in quadratic-form order, then

(2F/S)[f(y+d,t+v)−f(y,t)]≤−v+C(m+v|a|+v²D).                 (A)

At the smooth equalizer v=s this gives

s≤C(m+s|a|+s²D).                                         (B)

## 3. Derivative and discretization estimates

Direct differentiation gives

φ_xx=(1/t+z²/t²)φ,

φ_xxx=(3z/t²+z³/t³)φ,

φ_xxxx=(3/t²+6z²/t³+z⁴/t⁴)φ.

Suppose max_i y_i²/t≤K. Since

|φ_xxx/φ_xx|=(|y_i|/t)(y_i²/t+3)/(y_i²/t+1)≤3 sqrt(K/t),

Cauchy-Schwarz under q gives

|a|≤3 sqrt(K/t)∑_i q_i|d_i|≤3 sqrt(K/t)sqrt(m)≤3B sqrt(K/t).                 (C)

To bound D, let w_i=φ(y_i,t)/F, let u_i=1+y_i²/t, and let μ=E_w[u]. Then 1≤u_i≤1+K, μ≥1, and

D=(1/(4t))[Var_w(u)/μ+4−2/μ].

For completeness, if a random variable Z lies in [a,b], the pointwise inequality (Z−a)(b−Z)≥0 implies Var(Z)≤(b−E Z)(E Z−a). Applying this with a=1 and b=1+K gives Var_w(u)/μ≤K. Therefore

0≤D≤(K+4)/(4t).                                         (D)

All moments here are finite sums, so the bounded-variable inequality's hypotheses are satisfied.

## 4. Local Hessian control for the smooth log-potential

Consider any segment (z(λ),u(λ)) with positive time, let t_* be its minimum time, and set

K_seg=sup_{0≤λ≤1} max_i z_i(λ)²/u(λ).

We prove the Hessian sandwich with

A_x=8 sqrt(K_seg∨1)/sqrt(t_*),   A_t=16(K_seg∨1)/t_*.

At a point on the segment write g_i=log φ(z_i,u)=−(1/2)log u+z_i²/(2u), and let w_i=exp(g_i)/∑_k exp(g_k). For fixed directions v and h, define

A_i=Dg_i[v], B_i=D²g_i[v,v], C_i=D²g_i[v,h], H_i=Dg_i[h], T_i=D³g_i[v,v,h].

The quotient rule gives D_h w_i=w_i(H_i−E_w H). More generally, D_h E_w Z=E_w[D_h Z]+Cov_w(Z,H). Applying this rule successively gives

D²f[v,v]=E_w B+Var_w A,

D³f[v,v,h]=E_w T+Cov_w(B,H)+2Cov_w(A,C)+Cov_w((A−E_w A)²,H).                 (E)

These identities are derived here, rather than invoked as an unproved specialized result.

For a direction v=(v_1,…,v_N,v_t), put α_i=v_i−(z_i/u)v_t and β=v_t/u. For h put η_i=h_i−(z_i/u)h_t and θ=h_t/u. Differentiation gives

A_i=(z_i/u)α_i+(1/2)(z_i²/u−1)β,

B_i=α_i²/u+β²/2,

C_i=α_iη_i/u+βθ/2,

T_i=−2α_iβη_i/u−(α_i²/u)θ−β²θ.

In particular B_i≥0, |α_i|≤sqrt(u B_i), and |β|≤sqrt(2B_i). Also

|η_i|≤||h_x||_∞+sqrt(K_seg/t_*)|h_t|,

|H_i|≤sqrt(K_seg/t_*)||h_x||_∞+((K_seg+1/2)/t_*)|h_t|.

It follows term by term that

|E_w T|≤[2sqrt(2)||h_x||_∞/sqrt(t_*)+(3+2sqrt(2K_seg))|h_t|/t_*] E_w B.

For any nonnegative X and bounded Y, |Cov(X,Y)|≤2||Y||_∞ E X, because Cov(X,Y)=E[X(Y−EY)]. This bounds the second and fourth terms of (E). Finally,

|C_i|≤sqrt(B_i)[||h_x||_∞/sqrt(t_*)+(sqrt(K_seg)+1/sqrt(2))|h_t|/t_*].

Cauchy-Schwarz and 2sqrt(ab)≤a+b therefore bound 2|Cov(A,C)| by the bracket in this display times E_w B+Var_w A.

Adding these four bounds yields

|D³f[v,v,h]|≤[A_x||h_x||_∞+A_t|h_t|] D²f[v,v].

For example, before relaxing constants the spatial coefficient is at most (2sqrt(2)+1+4sqrt(K_seg))/sqrt(t_*), and the time coefficient is at most [5+1/sqrt(2)+(2sqrt(2)+1)sqrt(K_seg)+4K_seg]/t_*. They are respectively bounded by A_x and A_t.

For a fixed vector v, differentiate Q(λ)=v^T∇²f(z(λ),u(λ))v. With h equal to the segment displacement, the preceding inequality gives |Q'(λ)|≤Λ Q(λ), where Λ=A_x||h_x||_∞+A_t|h_t|. Integrating the two differential inequalities, without dividing by Q, gives

exp(−Λ)∇²f(start)≼∇²f(point)≼exp(Λ)∇²f(start).             (F)

This also covers zero quadratic forms. The argument applies to the smooth extension, not to the clipped function at its nonsmooth second derivative.

## 5. Crude comparison bound and the burn-in invariant

First suppose max_i y_i²/t≤K, put κ=max{K,1}, and assume t≥256e²B²κ. We show that the trial increment v=2eB² makes the smooth potential nonincreasing.

Along this trial segment, t_*=t and K_seg≤2K+2B²/t≤3κ. Hence (F) applies with

Λ≤8B sqrt(3κ/t)+48κv/t≤sqrt(3)/(2e)+3/(8e)<1.

Furthermore, m≤B² and, by (C)-(D),

v|a|≤(3/8)B²,   v²D≤(5/256)B².

Thus

m+v|a|+v²D≤(357/256)B²<2B².

Substitution into (A), with C=exp(Λ)≤e, proves f(y+d,t+v)≤f(y,t). Monotonicity in time gives

s≤2eB²,   δ≤2eB².                                       (G)

This is a trial-increment argument and is not circular.

Now return to actual iterates. The invariant from Section 1 implies

y_i²/t≤log(t/t_0)+2log N=:K(t).

Since N≥2, K(t)≥2log N>1. The prescribed initialization satisfies

t_0≥256e²B²K(t_0).

The function t−256e²B²K(t) is nonnegative at t_0 and has derivative 1−256e²B²/t≥0 for t≥t_0. Therefore

t≥256e²B²K(t)                                           (H)

at every actual iterate. In particular, (G) applies to every smooth comparison update.

The log-coordinate bound applies to projected coordinates at actual iterates, not to the squared negative raw regrets.

## 6. Refined second-moment bound, including the mixed term

Fix an actual base point and its smooth equalizer s. Both smooth endpoints have potential N/sqrt(t_0). The function φ is jointly convex on R×(0,∞): its log has quadratic form α²/u+β²/2≥0, and exponentiation preserves convexity. Thus F is jointly convex and is at most N/sqrt(t_0) throughout the comparison segment.

Using (G), its segment parameter consequently satisfies

K_seg≤K(t)+log(1+s/t)≤K(t)+log 2≤2K(t).

Here t≥t_0≥2eB². Combining this estimate with (H) gives

Λ≤8B sqrt(2K(t)/t)+32K(t)s/t

  ≤sqrt(2)/(2e)+1/(4e)=:α.

In particular α<0.414. At the base point, (C), (D), (G), and (H) also give

|a|≤3/(16e),   sD≤5/(512e).

Applying (B) with C=exp(Λ) yields

[exp(−Λ)−|a|−sD]s≤m.

The bracket is strictly greater than 1/2. Indeed, exp(−α)≥1−α implies

exp(−Λ)−|a|−sD

≥1−[(2sqrt(2)+1)/4+3/16+5/512]/e>1/2.

The last strict inequality follows already from sqrt(2)<3/2 and e>5/2. Therefore

δ≤s≤2m≤2∑_i q_i r_i².                                  (I)

The omitted mixed derivative in the source is thus controlled explicitly using the existing constant slack. No cancellation beyond the algorithm's actual first-order cancellation is assumed.

Summing (I) over rounds gives

t_T=t_0+∑_{j=1}^T Δt_j≤t_0+2V_T.

## 7. Quantile conversion and boundary cases

Let k=ceil(Nε) and r=x_{T,(k)}. If r≤0, the desired inequality is immediate. Otherwise at least k≥Nε coordinates have positive regret at least r. The invariant gives

N/sqrt(t_0)=Φ(y_T,t_T)≥Nε t_T^(−1/2)exp(r²/(2t_T)).

Taking logarithms yields

r²≤t_T[log(t_T/t_0)+2log(1/ε)].

For u≥t_0 and 0<ε≤1, the function u[log(u/t_0)+2log(1/ε)] is nonnegative and increasing, since its derivative is log(u/t_0)+1+2log(1/ε)≥1. Substituting t_T≤t_0+2V_T proves the required bound.

The ceiling rank is defined for all 0<ε≤1, including ε<1/N and ε=1. Zero increments cause no difficulty. If V_T=0, strict positivity of every q_{j,i} forces every actual regret increment to vanish; consequently t_T=t_0 and all cumulative regrets are zero.

## Obligation ledger

All obligations are closed: the two distributions and their timing; existence, uniqueness, and nonnegativity of the actual equalizer; the correct cumulative-regret projection comparison; the corrected Taylor and mixed-Hessian formula; explicit discretization and cross-term bounds; the local Hessian sandwich with its constants; a noncircular crude estimate; the invariant and initialization conditions; the refined factor-2 increment estimate; and the quantile conversion with all endpoints. The only named independent inequality used, the bounded-variable variance inequality, is stated and proved above. There is no unresolved specialized dependency.
