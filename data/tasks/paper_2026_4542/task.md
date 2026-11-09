# Problem

## Setup

Let $X,Y,Z$ be finite discrete variables with one joint distribution $P(x,y,z)$. All marginals and conditionals below are induced by this same distribution, and statements are restricted to contexts of positive mass where the displayed conditionals are defined. Fix $\alpha>0$.

Let $V$ be an event-based value function: it is invariant under permutations of the variables in an information event (in particular, $V(x,y)=V(y,x)$ and $V(x,y,z)=V(z,y,x)$). Fully resolved values are terminal data and partially resolved values are continuation values.

For each $(y,z)$, let $r_z(x\mid y)$ be a reward and consider distributions $q(\cdot\mid y)$ absolutely continuous with respect to $P(\cdot\mid y)$:
\[
J_z(q)=\sum_x q(x\mid y)\left[r_z(x\mid y)-\frac1\alpha\log\frac{q(x\mid y)}{P(x\mid y)}+V(x,y,z)\right].
\]
Assume its unique maximizer is the ambient posterior $P(x\mid y,z)$ and its maximum is the continuation value $V(y,z)$. Assume the same posterior-identification condition holds for the reversed update over $q(\cdot\mid y)$ on $Z$, with reward $r_x(z\mid y)$, signal $V(z,y,x)$, posterior $P(z\mid y,x)$, and maximum $V(y,x)$, using the same permutation-invariant value function.

For positive-mass contexts define conditional pointwise mutual information by
\[
i(x;z\mid y)=\log\frac{P(x,z\mid y)}{P(x\mid y)P(z\mid y)}=\log\frac{P(x\mid y,z)}{P(x\mid y)}.
\]

## Task

Prove the following integrated theorem. For every point where the relevant conditionals are defined,
\[
\alpha\bigl[r_z(x\mid y)+V(x,y,z)-V(y,z)\bigr]=i(x;z\mid y).
\]
Moreover, the posterior and this identity are invariant under the context-baseline gauge
\[
r_z(x\mid y)\mapsto r_z(x\mid y)+c(y,z),\qquad V(y,z)\mapsto V(y,z)+c(y,z)
\]
for arbitrary $c(y,z)$, so absolute rewards and the reward/value split are not identified. Finally, the two update directions obey
\[
r_z(x\mid y)-V(y,z)=r_x(z\mid y)-V(x,y).
\]
