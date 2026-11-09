# Problem

## Setup

Let `X` be a type in `[0,1]` with probability law `P`. Fix a cutoff `tau` with `0<tau<1`, and let `L:[0,1]->R` be integrable and satisfy

- `L(x)<0` for `x<tau`;
- `L(x)>0` for `x>=tau`.

Assume `P(X<tau)>0`, `P(X>tau)>0`, and `P(X=tau)=0`.

Let `c>0` and `b>0`. An admissible gate is a nondecreasing upper-semicontinuous function `g:[0,1]->[0,1]`. After observing its type `x`, an agent chooses a report in

`BR_g(x) = argmax_{y in [0,1]} {-c(y-x)^2 + b g(y)}`.

For each gate, let `y_g(x)` be a measurable best-response selection and define the principal's value by

`W(g) = E[g(y_g(X)) L(X)]`.

The first-best screening value is

`W_FB = E[max{L(X),0}]`.

Call a gate affine if `g(y)=a+s y` on `[0,1]` for constants `a,s` compatible with admissibility.

Assume the unsaturated condition

`b/c <= (1-tau)^2`.

## Task

Prove the following integrated theorem.

No affine admissible gate attains `W_FB`. In contrast, with

`t = tau + sqrt(b/c)`,  `g*(y)=1{y>=t}`,

the gate `g*` is admissible and, under any measurable best-response selection,

`g*(y_{g*}(X)) = 1{X>=tau}`

almost surely. Consequently, `g*` attains `W_FB`. Moreover, every type `x` with `tau<x<t` strictly inflates its report under `g*`, meaning `y_{g*}(x)>x`. Conclude that an optimal admissible gate exists and that every optimal gate is non-affine.
