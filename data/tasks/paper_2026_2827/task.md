# Problem

## Setup

For a nonzero vector $x\in\mathbb R^n$, let $M=\|x\|_\infty$ and define coordinatewise
\[
\alpha=M/127,\qquad x^{(1)}_i=\operatorname{clip}(\operatorname{round}(x_i/\alpha),-128,127),
\]
where `round` is nearest-integer rounding. Set
\[
r=x-\alpha x^{(1)},\qquad \beta=\alpha/254,\qquad x^{(2)}_i=\operatorname{clip}(\operatorname{round}(r_i/\beta),-128,127).
\]

Now let $x_b\in\mathbb R^{32}$ be a nonzero 32-element block, $M_b=\|x_b\|_\infty$, and
\[
\alpha=2^{\lceil\log_2(M_b/1.859375)\rceil},\qquad \beta=\alpha/16.
\]
The MXFP4 block uses one shared E8M0 exponent-only (power-of-two) scale. Let
\[
S=\{0\}\cup\{\pm0.25,\pm0.5,\pm0.75,\pm1,\pm1.25,\pm1.5,\pm1.75\}.
\]
For $t\in\mathbb R$, let $Q_4(t)$ be nearest-element rounding to $S$ after clipping magnitudes to at most $1.75$. Define $q_{1,i}=Q_4(x_{b,i}/\alpha)$, $r=x_b-\alpha q_1$, and $q_{2,i}=Q_4(r_i/\beta)$.

## Task

Prove the following integrated theorem:

1. The INT8 two-pass reconstruction satisfies
\[
\left\|x-(\alpha x^{(1)}+\beta x^{(2)})\right\|_\infty\le M/64516.
\]
2. Every nonzero 32-element MXFP4 block satisfying the Setup has reconstruction error
\[
\left\|x_b-(\alpha q_1+\beta q_2)\right\|_\infty\le\alpha/64.
\]
