# Problem

## Setup

Let C be a closed convex subset of R^n with nonempty interior, and choose an anchor 0 in Int(C). For u in R^n define

alpha(u) = sup { a in [0,1] : a u belongs to C },   q(u)=alpha(u)u,

with q(0)=0. Let r:[0,infinity)->[0,1) be C1, strictly increasing, satisfy r'(s)>0 for s>0, r(0)>0, and lim_{s->infinity} r(s)=1. Define

p(u)=r(||u||^2)q(u).

## Task

Prove that p is a homeomorphism from R^n onto Int(C). Moreover, p is differentiable almost everywhere, and at every point where its Jacobian exists that Jacobian is invertible.
