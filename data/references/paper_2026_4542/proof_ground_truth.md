# Reference Proof

## Proof Structure

Use the KL variational (free-energy) identity to obtain the unique exponential-tilt optimizer and its log-normalizer. Posterior identification then gives the conditional log-ratio, which is conditional PMI. A context-only gauge shift leaves the optimizer unchanged. Applying the same argument to the reversed update and using permutation invariance of the shared value and symmetry of conditional PMI yields the commutativity constraint.

## Complete Proof

For fixed positive-mass $(y,z)$, write
\[
s_z(x\mid y)=r_z(x\mid y)+V(x,y,z).
\]
The KL variational identity gives the unique optimizer
\[
q_z^*(x\mid y)=\frac{P(x\mid y)e^{\alpha s_z(x\mid y)}}{\sum_{\tilde x}P(\tilde x\mid y)e^{\alpha s_z(\tilde x\mid y)}},
\]
and the maximum
\[
V(y,z)=\frac1\alpha\log\sum_{\tilde x}P(\tilde x\mid y)e^{\alpha s_z(\tilde x\mid y)}.
\]
By posterior identification, $q_z^*(x\mid y)=P(x\mid y,z)$. Taking the ratio to $P(x\mid y)$ and substituting the log-normalizer gives
\[
\log\frac{P(x\mid y,z)}{P(x\mid y)}
=\alpha\bigl[r_z(x\mid y)+V(x,y,z)-V(y,z)\bigr].
\]
By the definition of conditional PMI, the left side is $i(x;z\mid y)$, proving
\[
\alpha\bigl[r_z(x\mid y)+V(x,y,z)-V(y,z)\bigr]=i(x;z\mid y)
\]
for every point with the relevant conditional probabilities defined.

Now let $c(y,z)$ be arbitrary and replace
\[
r_z'(x\mid y)=r_z(x\mid y)+c(y,z),\qquad V'(y,z)=V(y,z)+c(y,z),
\]
leaving $V(x,y,z)$ unchanged. Every exponent in the tilt is shifted by the same constant $\alpha c(y,z)$, so numerator and denominator scale equally; hence $q_z^*=P(x\mid y,z)$ is unchanged. The displayed posterior identity is also unchanged. Thus only within-context relative incentives are identified, and the reward/value decomposition has a context-baseline gauge freedom.

For the reversed update, optimize over $q(z\mid y)$ with signal $r_x(z\mid y)+V(z,y,x)$ relative to $P(z\mid y)$, and impose optimizer $P(z\mid y,x)$. The same calculation yields
\[
\alpha\bigl[r_x(z\mid y)+V(z,y,x)-V(y,x)\bigr]=i(z;x\mid y).
\]
The shared event-based value is permutation invariant, so $V(z,y,x)=V(x,y,z)$ and $V(y,x)=V(x,y)$; conditional PMI is symmetric, so $i(z;x\mid y)=i(x;z\mid y)$. Equating this equation with the forward identity and cancelling the common $V(x,y,z)$ term gives
\[
r_z(x\mid y)-V(y,z)=r_x(z\mid y)-V(x,y),
\]
which is the required commutativity constraint.
