# Reference Proof

## Proof Structure

The proof first solves the reporting problem for an arbitrary affine gate and uses the resulting strictly positive approval of loss-making types to rule out first-best affine screening. It then analyzes the sharp-threshold gate directly, verifies every type's best response, and shows that its strategically chosen offset makes the reporting cutoff coincide with the principal's value cutoff. Finally, a pointwise welfare bound proves global optimality and implies that every optimal gate is non-affine.

## Complete Proof

Let `d = sqrt(b/c)` and `t = tau + d`. The unsaturated-regime assumption gives `t <= 1`.

### Affine gates cannot attain first best

Consider an admissible affine gate `g(y)=a+s y`, where `s>=0`. Its reporting objective is

`-c(y-x)^2 + b(a+s y)`.

Completing the square, or differentiating the strictly concave objective before imposing the report constraints, shows that its unique maximizer is

`y_g(x)=clip(x+delta,0,1)`, where `delta=bs/(2c)`.

If `s>0`, then `delta>0`, so `y_g(x)>0` for every `x` in `[0,1]`. Since an admissible affine gate has `a>=0`,

`g(y_g(x))=a+s y_g(x)>0`

for every type, including every type below `tau`.

For any gate and response selection,

`W_FB-W(g) = E[(1-g(y_g(X)))L(X) 1{X>=tau}] + E[-g(y_g(X))L(X) 1{X<tau}]`.

Both terms are nonnegative. When `s>0`, the second integrand is strictly positive for every `X<tau`; that event has positive probability. Hence `W(g)<W_FB`.

If `s=0`, the gate is constant, say `g=a`. For `a=0`, it rejects all profitable types, and the first term above is strictly positive because `P(X>tau)>0`. For `a>0`, it gives positive approval to every loss-making type, so the second term is strictly positive; this also covers `a=1`. Thus every constant gate, and consequently every affine gate, has welfare strictly below `W_FB`.

### The offset threshold implements the value cutoff

Define

`g*(y)=1{y>=t}`.

This gate is nondecreasing, takes values in `[0,1]`, and is upper semicontinuous because its value at the jump is the upper value.

Fix a type `x<t`. Among unapproved reports `y<t`, truthful reporting `y=x` uniquely maximizes the quadratic term and yields utility `0`. Among approved reports `y>=t`, the nearest report is `y=t`, yielding

`b-c(t-x)^2`.

Since `t-d=tau`, this approved-report utility is negative for `x<tau`, zero for `x=tau`, and positive for `tau<x<t`. Therefore types below `tau` report truthfully and remain unapproved, while types strictly between `tau` and `t` report `t` and are approved.

For `x>=t`, truthful reporting is approved and yields utility `b`. Every other approved report incurs a strictly positive quadratic loss, while every unapproved report yields at most `0`. Thus `y=x` is the unique best response for these types.

Consequently, except at the indifferent boundary type,

`y_{g*}(x)=x` for `x<tau`,

`y_{g*}(x)=t` for `tau<x<t`, and

`y_{g*}(x)=x` for `x>=t`.

At `x=tau`, both `y=tau` and `y=t` are best responses. This type has probability zero by assumption, so the choice does not affect welfare. Hence

`g*(y_{g*}(X))=1{X>=tau}` almost surely.

In particular, every type in `(tau,t)` inflates its report from `x` to `t`; this strategic inflation is exactly what aligns the induced approval cutoff with `tau`.

### Optimality and non-affinity

For any admissible gate, `0<=g<=1`. Pointwise,

`g(y_g(x))L(x) <= max{L(x),0}`:

when `L(x)>0`, approval is at most one, and when `L(x)<0`, nonnegative approval can only reduce the value relative to zero. Taking expectations gives `W(g)<=W_FB`.

The threshold gate attains equality because it approves exactly the types for which `L` is positive, almost surely. Thus `g*` is optimal and an optimum exists. Since every affine gate was shown to have value strictly below `W_FB`, no affine gate is optimal. Therefore every optimal gate is non-affine. The displayed response characterization also establishes the claimed report inflation under the optimal threshold.
