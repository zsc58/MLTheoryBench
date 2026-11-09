# Reference Proof

## Proof Structure and Obligations

The argument is deterministic and holds for every realized admissible loss sequence. It therefore does not require an oblivious adversary or any probabilistic assumption. The hidden coordinates and mirror steps introduced below are analysis objects, not quantities supplied to the learner.

The theorem-critical obligations are:

1. Establish well-defined updates and a comparator, and obtain the hidden linearization with its correct gradient bound.
2. Localize both one-step updates and express them using a common quadratic model.
3. Derive both Taylor-remainder gradient bounds explicitly.
4. Compare the constrained minimizers to obtain an order-eta-squared discrepancy.
5. Derive and telescope the perturbed mirror-step inequality without relying on an unproved specialized external lemma.
6. Choose a positive step size of the required order with constants depending only on the displayed parameters.

All six obligations are proved below.

## 1. Well-Definedness and Hidden Linearization

Write `u=phi^{-1}`, `H_z=nabla^2 Psi(z)`, `z_t=phi(x_t)`, and `g_t=nabla f_t(x_t)`. The compatibility identity makes `J_phi(x)` nonsingular, and differentiation of the local inverse gives

`Du(z_t)=J_phi(x_t)^{-1}`.

Since `c_t=f_t circ u` on `Y`, the chain rule gives a gradient representative

`a_t=Du(z_t)^T g_t=J_phi(x_t)^{-T}g_t`

for `c_t` on `Y`. In particular,

`||a_t||_2<=L M`,

and convexity gives, for every `y in Y`,

`c_t(z_t)-c_t(y)<=<a_t,z_t-y>`.

This supporting inequality also holds on a lower-dimensional domain: differentiate `c_t(z_t+s(y-z_t))` at `s=0` and use convexity of this one-variable restriction. No unique choice of a normal component of the gradient is needed.

Projection onto `X` exists and is unique because `X` is nonempty, compact, and convex. For later use, Euclidean projection is nonexpansive. Indeed, if `p=Pi_X(v)` and `q=Pi_X(w)`, the two minimizing variational inequalities imply

`||p-q||_2^2<=<p-q,v-w>`,

hence `||p-q||_2<=||v-w||_2`. These inequalities follow by differentiating the squared-distance objective along feasible line segments.

The cumulative loss is continuous on compact `X`, so it has a minimizer `x^*`. Each mirror objective used below is continuous and strongly convex on nonempty compact convex `Y`, and consequently has a unique minimizer.

## 2. Localization and the Common Quadratic Model

Fix a round and write `x=x_t`, `z=z_t`, `g=g_t`, and `a=a_t`. Define

`m=argmin_{w in Y}{eta<a,w-z>+D_Psi(w||z)}`

and write `z^+=z_{t+1}`. The center of this mirror step is the actual current point `z_t`; an independent mirror trajectory is not carried across rounds.

Strong convexity gives

`eta<a,w-z>+D_Psi(w||z)>=-eta L M ||w-z||_2+||w-z||_2^2/2`.

This is positive when `||w-z||_2>2 eta L M`, whereas the value at `w=z` is zero. Thus `||m-z||_2<=2 eta L M`.

Since `Pi_X(x)=x`, projection nonexpansiveness and the Lipschitz property of `phi` give

`||z^+-z||_2<=L||x_{t+1}-x_t||_2<=eta L M`.

Both points therefore belong to the nonempty compact convex set

`Y_t={w in Y: ||w-z||_2<=2 eta L M}`.

Put `K=Du(z)` and define

`Phi_t(w)=<a,w-z>+(1/(2eta))(w-z)^T H_z(w-z)`.

Compatibility implies

`H_z=(J_phi(x)J_phi(x)^T)^{-1}=K^T K`.

The quadratic model is `1/eta`-strongly convex on `Y_t`. This conclusion does not require a full-dimensional domain. On the linear space `V=span(Y-Y)`, strong convexity of `Psi` implies `h^T H_z h>=||h||_2^2`. At relative-interior points this follows by differentiating the strong-convexity inequality along short feasible line segments, and at all other points it follows by continuity of the Hessian. All differences of feasible points lie in `V`.

Define the exact mirror remainder by

`eps_M(w)=eta^{-1}[D_Psi(w||z)-(1/2)(w-z)^T H_z(w-z)]`.

Then `m` minimizes `Phi_t+eps_M` on `Y_t`.

The projected-gradient update minimizes

`<g,v-x>+(1/(2eta))||v-x||_2^2`

over `v in X`. Changing variables `w=phi(v)` and using `a=K^T g` and `H_z=K^T K`, its objective is exactly `Phi_t(w)+eps_G(w)`, where

`eps_G(w)=<g,u(w)-u(z)-K(w-z)>`

` +(1/(2eta))[||u(w)-u(z)||_2^2-||K(w-z)||_2^2]`.

Since the global minimizer `z^+` is already in `Y_t`, it also minimizes `Phi_t+eps_G` on `Y_t`. Convexity of this transformed objective is not asserted or needed.

## 3. Remainder-Gradient Estimates

Differentiating the exact definition of `eps_M`, rather than differentiating a third-order integral remainder, gives

`nabla eps_M(w)=eta^{-1}[nabla Psi(w)-nabla Psi(z)-H_z(w-z)]`.

The third-derivative bound implies that the Hessian changes by at most `L` times distance along every segment in `Y`. Integrating the Hessian difference along the segment from `z` to `w` therefore gives

`||nabla eps_M(w)||_2<=(L/(2eta))||w-z||_2^2`.

At `w=m`, localization yields

`||nabla eps_M(m)||_2<=2L^3 M^2 eta`.                         (1)

For the other remainder, put `h=w-z` and

`e(w)=u(w)-u(z)-K h`.

Integration along the segment from `z` to `w`, using the bound on `D^2 u`, gives

`||e(w)||_2<=(L/2)||h||_2^2`,

`J_e(w)=Du(w)-K`, and `||J_e(w)||_op<=L||h||_2`.

The exact remainder can be written as

`eps_G(w)=<g,e(w)>+eta^{-1}[(1/2)||e(w)||_2^2+<K h,e(w)>]`.

Its gradient is consequently

`nabla eps_G(w)=J_e(w)^T g`

` +eta^{-1}[J_e(w)^T e(w)+K^T e(w)+J_e(w)^T K h]`.

At `w=z^+`, the sharper localization bound `||h||_2<=eta L M` implies

`||J_e(z^+)||_op<=eta L^2 M`,

`||e(z^+)||_2<=(eta^2 L^3 M^2)/2`.

Together with `||K||_op<=L` and `||g||_2<=M`, these give

`||nabla eps_G(z^+)||_2`

` <=eta L^2 M^2+(eta^2 L^5 M^3)/2+(eta L^4 M^2)/2+eta L^4 M^2`

` <=L^5(3M^2+M^3 eta)eta`,                                  (2)

where the last inequality uses `L>1`. Combining (1) and (2),

`||nabla eps_G(z^+)-nabla eps_M(m)||_2`

` <=L^5(5M^2+M^3 eta)eta`.                                  (3)

Only the stated derivatives of `u` and `Psi` have been used; no additional smoothness of the losses is required.

## 4. Constrained Minimizer Comparison

For a closed convex set `K_0`, define

`N_{K_0}(p)={v: <v,w-p><=0 for every w in K_0}`.

A differentiable function minimized at `p` over `K_0` satisfies the necessary first-order inequality against every feasible line segment. Therefore the negative gradient belongs to `N_{K_0}(p)`, even when the function itself is not convex.

Apply this fact to the two minimizers over `Y_t`. There exist `v_G in N_{Y_t}(z^+)` and `v_M in N_{Y_t}(m)` such that

`nabla Phi_t(z^+)+nabla eps_G(z^+)+v_G=0`,

`nabla Phi_t(m)+nabla eps_M(m)+v_M=0`.

The normal-cone definition gives `<v_G,m-z^+><=0` and `<v_M,z^+-m><=0`. Subtracting these inequalities shows

`<v_G-v_M,z^+-m>>=0`.

Subtract the two optimality equations and take the inner product with `delta=z^+-m`. Strong convexity of the quadratic model on feasible differences and the preceding normal-cone inequality imply

`eta^{-1}||delta||_2^2`

` <=||nabla eps_G(z^+)-nabla eps_M(m)||_2 ||delta||_2`.

If `delta=0` there is nothing to prove; otherwise divide by its norm and use (3). Thus, in every round,

`||z_{t+1}-m_{t+1}||_2<=C_eta`,

`C_eta=L^5(5M^2+M^3 eta)eta^2`.                              (4)

This establishes the required order-eta-squared discrepancy, uniformly over the initialization and loss sequence, for any fixed bounded range of positive step sizes.

## 5. Direct Perturbed Mirror-Descent Telescoping

Fix any comparator `y in Y`. The first-order inequality for the mirror step centered at `z_t` is

`<eta a_t+nabla Psi(m_{t+1})-nabla Psi(z_t),y-m_{t+1}>>=0`.

Expanding the definition of the Bregman divergence gives the identity

`<nabla Psi(m_{t+1})-nabla Psi(z_t),y-m_{t+1}>`

` =D_Psi(y||z_t)-D_Psi(y||m_{t+1})-D_Psi(m_{t+1}||z_t)`.

Consequently,

`<a_t,z_t-y>`

` <=[D_Psi(y||z_t)-D_Psi(y||m_{t+1})]/eta`

`   +<a_t,z_t-m_{t+1}>-D_Psi(m_{t+1}||z_t)/eta`.

By strong convexity, Cauchy-Schwarz, and the elementary inequality

`ar-r^2/(2eta)<=eta a^2/2`,

which follows by completing a square, the last two terms are at most `eta||a_t||_2^2/2`. Hence

`<a_t,z_t-y><=[D_Psi(y||z_t)-D_Psi(y||m_{t+1})]/eta`

`                 +eta||a_t||_2^2/2`.

The assumed second-argument Lipschitz property and (4) give

`D_Psi(y||z_{t+1})-D_Psi(y||m_{t+1})<=L C_eta`.

Insert `D_Psi(y||z_{t+1})` into the preceding inequality and sum. The Bregman differences telescope, their terminal value is nonnegative, and their initial value is at most `B`. Therefore

`sum_{t=1}^T <a_t,z_t-y>`

` <=B/eta+(L C_eta T)/eta+(eta/2)sum_{t=1}^T||a_t||_2^2`

` <=B/eta+(L C_eta T)/eta+(eta L^2 M^2 T)/2`.                (5)

This explicitly proves the specialized perturbed-mirror-descent bound needed here. The external attribution in theory_005 is not used as a substitute for a derivation. In particular, the last term contains the squared hidden-gradient bound `L^2 M^2`, rather than `L^2` alone.

Taking `y=phi(x^*)` and applying the supporting inequality from Section 1 yields

`Reg_T<=sum_{t=1}^T<a_t,z_t-y>`.

## 6. Positive Step Size and Uniform Constants

For `0<eta<=1`, substitute (4) into (5) and set

`A=L^6(5M^2+M^3)+(L^2 M^2)/2`.

Then

`Reg_T<=B/eta+A eta T`.

Here `A>0` because `M>0`, and `B>0` is the positive bound required in the setup. Define

`k=sqrt(B/A)`,

`T_0=max{1,ceil(B/A)}`.

For every integer `T>=T_0`, the choice `eta=k T^{-1/2}` is positive and at most one. It gives

`Reg_T<=2 sqrt(A B T)`.

Thus `C=2 sqrt(A B)` and `k,T_0` depend only on `L,M,B`, as required. The conclusion is uniform over all admissible loss sequences and initial points. Singleton domains are included: their regret is zero, and the same positive step-size prescription remains well defined because `B` is a positive upper bound, not necessarily the exact divergence diameter.

## Source-Repair Ledger

The previously recorded constant repairs in theory_003 and theory_004 are retained: use the general coupling coefficient in (4), do not absorb arbitrary powers of `M` without justification, and retain the factor two from optimizing `B/eta+A eta T`.

The additional repair to theory_005 replaces the supplied paper's literal gradient-cost term `eta G^2 T/2` by `(eta/2) sum_t ||grad h_t(z_t)||_2^2`, bounded by `eta G^2 G_F^2 T/2`. Its mirror step is centered at the actual iterate, as required by the source's reset coupling. This is a local normalization correction, and Sections 1 and 5 give its complete derivation.
