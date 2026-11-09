# Reference Proof

## Proof Obligations

1. Verify the pushforward density, positivity, normalization, and continuity in time of the resulting probability measures.
2. Differentiate the density-Jacobian identity and explicitly derive the Jacobian-to-divergence relation.
3. Derive the Fokker-Planck equation by cancellation of the score and diffusion terms.
4. Verify the hypotheses of the standard forward-equation/SDE correspondence and identify the marginals on each specified nonexplosive interval.

## Standard Background Used

**Jacobi's formula (theory_014).** If A_t is a differentiable curve of invertible square matrices, then

`d/dt det A_t = det A_t tr(A_t^{-1} partial_t A_t)`.

The same formula holds with the determinant replaced by its absolute value. Indeed, the continuous nonzero determinant has constant sign locally.

**Forward-equation correspondence (theory_012).** The relevant standard form is as follows. On a compact time interval [a,T], let beta(t,y) be measurable in time and C^1 in space. Suppose that, for each compact spatial set K, `sup_{y in K} (|beta(t,y)|+|D_y beta(t,y)|)` has an integrable upper bound in time. Let s be a measurable scalar function with `integral_a^T s(t)^2 dt < infinity`. A nonnegative classical probability-density solution p of

`partial_t p = -div(beta p)+(s^2/2)Delta p`

with initial density p_a agrees with the marginals of any nonexplosive solution of `dY_t=beta(t,Y_t)dt+s(t)dW_t` having that initial law.

The applicable standard forward-equation fact is minimality of the killed transition evolution: on a bounded domain D, its evolution from `1_D p_a` is dominated within D by any nonnegative classical forward-equation solution p with that initial density on D. This is the positivity/comparison form of forward-backward duality, including the degenerate case s=0. Increasing bounded domains to the whole space proves the stated correspondence: the nonexplosive SDE marginal is dominated by `p_t(y)dy`, and both measures have total mass one. This form avoids assuming global integrability of `|beta|` against p or asserting an unconditional equivalence between SDE uniqueness and all formulations of Fokker-Planck uniqueness.

## Complete Proof

Fix z and abbreviate the public conditional maps by F_t. All arguments are on positive-time intervals. Derivatives at t=1 are left derivatives.

### 1. Density and Probability Measures

For every Borel set A, change of variables through the diffeomorphism F_t gives

`nu_t(A) = integral_{F_t^{-1}(A)} pi(x) dx = integral_A pi(F_t^{-1}(y)) |det D_xF_t(F_t^{-1}(y))|^{-1} dy`.

Thus the displayed pi_t is the pushforward density. It is positive, and its integral is one. For every bounded continuous function f,

`integral f(y) nu_t(dy) = integral f(F_t(x)) nu(dx)`.

Continuity of F_t in t and dominated convergence show that t maps to nu_t is narrowly continuous. No moment assumption is needed.

### 2. Continuity Equation

Set `A_t(x)=D_xF_t(x)` and `J_t(x)=|det A_t(x)|`. The density formula gives

`pi_t(F_t(x)) J_t(x)=pi(x)`.

The definition of u_t gives

`partial_t F_t(x)=u_t(F_t(x))`.

The public regularity of u_t and D_yu_t makes the right-hand side continuously differentiable in x. Differentiating the integral identity for F_t on a compact positive-time interval therefore justifies commutation of the mixed derivatives and yields

`partial_t A_t(x)=D_x(partial_t F_t)(x)=(D_yu_t)(F_t(x)) A_t(x)`.

The matrices A_t(x) are invertible. Jacobi's formula and cyclicity of trace now give

`partial_t J_t(x) = J_t(x) tr(A_t(x)^{-1}(D_yu_t)(F_t(x))A_t(x)) = J_t(x) (div u_t)(F_t(x))`.

Here the divergence is in the argument of u_t, followed by evaluation at F_t(x); it is not divergence in x of the composite vector field.

Differentiate the density-Jacobian identity at fixed x:

`[(partial_t pi_t)(F_t(x)) + grad pi_t(F_t(x)) dot partial_t F_t(x)]J_t(x) + pi_t(F_t(x)) partial_t J_t(x)=0`.

Substitute the two derivative formulas, divide by the positive J_t(x), and use surjectivity of F_t. This gives

`partial_t pi_t + grad pi_t dot u_t + pi_t div u_t=0`,

hence

`partial_t pi_t + div(pi_t u_t)=0`.

For source auditing, the absolute value does not repair an actual orientation error here: continuity and nonvanishing of `det A_t(x)`, together with `A_1(x)=I`, imply `det A_t(x)>0` for every positive t. Keeping the absolute value matches the density definition directly.

### 3. Fokker-Planck Equation

Positivity and spatial differentiability imply

`pi_t grad log pi_t=grad pi_t`.

Because sigma_t is independent of the spatial variable,

`-div(pi_t b_t)+(sigma_t^2/2)Delta pi_t = -div(pi_t u_t)-(sigma_t^2/2)div(grad pi_t)+(sigma_t^2/2)Delta pi_t = -div(pi_t u_t) = partial_t pi_t`.

This calculation is pointwise, including times at which sigma_t=0. No time derivative of sigma is taken.

### 4. SDE Marginals

Fix `0<t_0<T<=1` and a nonexplosive weak solution on [t_0,T] with initial density pi_{t_0}. The case T=t_0 is immediate.

We check the forward-equation correspondence rather than assuming it from a blanket equivalence assertion. On every compact cylinder `[t_0,T] x K`, positivity and continuity of pi_t give a positive lower bound for pi_t. The public spatial regularity therefore bounds both `grad log pi_t` and its spatial derivative on that cylinder. The same cylinder bounds u_t and D_yu_t. Consequently, for a finite constant C_K,

`sup_{y in K} (|b_t(y)|+|D_yb_t(y)|) <= C_K(1+sigma_t^2)`.

The right side is integrable in t. The drift is measurable in time and C^1 in space, and sigma is square-integrable on [t_0,T]. Thus the local coefficient hypotheses of theory_012 are satisfied. The candidate pi_t is a nonnegative classical solution of the forward equation, has the required initial density, has mass one at every time, and defines a narrowly continuous probability path.

More explicitly, let D_R be increasing balls covering R^d, and let tau_R be the exit time from D_R, with tau_R=t_0 when the initial point is outside D_R. Killed-evolution minimality gives

`P(X_t in A, tau_R>t) <= integral_A pi_t(y) dy`

for Borel A contained in D_R. Nonexplosion and continuity of sample paths imply that, as R increases, the left side converges to `P(X_t in A)` for each bounded Borel A. Hence the SDE marginal is dominated by `pi_t(y)dy`. Both measures have total mass one, so equality follows. Exhaustion extends the equality to all Borel sets.

Therefore X_t has density pi_t for every t in [t_0,T]. The assumed uniqueness in law makes this the unique SDE evolution. The argument includes zero noise and requires neither initialization at t=0 nor an assertion about an explosive or killed process being a probability-preserving evolution.

All four proof obligations are closed.
