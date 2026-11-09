# Reference Proof

## Proof Structure

Specialize the state equations to one dimension, first for the quadratic loss and then for the symmetric quartic loss. In both cases, symmetry makes the center m=0 invariant. The extent equation is then obtained by evaluating the endpoint gradients. Its equilibria and their local stability follow from factorization and the derivative of the scalar vector field.

## Complete Proof

Write m for the center, Sigma >= 0 for the extent, and delta=sqrt(Sigma). Let
G_+=L'(m+delta), G_-=L'(m-delta), and H_+=L''(m+delta), H_-=L''(m-delta). The one-dimensional state equations are

dm/dt = -(eta/2)(G_+ + G_-) -(eta^2/8)(H_+ + H_-)(G_+ + G_-),

dSigma/dt = (eta^2/4)(G_+^2+G_-^2)-2 Sigma.

For L_q(w)=S w^2/2 and m=0, delta=sqrt(Sigma), so G_+=S delta and G_-=-S delta, while H_+=H_-=S. Hence G_++G_-=0, proving dm/dt=0 and therefore invariance of m=0. Moreover,

dSigma/dt=(eta^2/4)(2 S^2 Sigma)-2 Sigma=(eta^2 S^2/2-2)Sigma.

Setting beta=eta^2 S^2/4-1 gives Sigma(t)=Sigma(0) exp(2 beta t). Thus the zero-extent equilibrium is attracting for S<2/eta, unstable for S>2/eta, and is the neutral transition case at S=2/eta. Since the one-dimensional quadratic sharpness is S, this is exactly the threshold 2/eta.

Now let L_4(w)=S w^2/2+Q w^4/4. At m=0,
G_+=S delta+Q delta^3=delta(S+Q Sigma),
G_-=-delta(S+Q Sigma),
and H_++H_- is finite but is multiplied by G_++G_-=0. Therefore m=0 is invariant, and

dSigma/dt=(eta^2/2) Sigma (S+Q Sigma)^2-2 Sigma
       =(eta^2 S^2/2-2)Sigma+eta^2 S Q Sigma^2+(eta^2 Q^2/2)Sigma^3.

If Q=0 this reduces to the quadratic equation. Assume Q != 0. Factoring the equilibrium condition gives Sigma=0 or S+Q Sigma=2/eta or S+Q Sigma=-2/eta. Thus

Sigma_- = -(S-2/eta)/Q,   Sigma_+ = -(S+2/eta)/Q.

Only roots in the physical domain Sigma>=0 are admissible. Let f denote the scalar right-hand side. At zero,
f'(0)=eta^2 S^2/2-2,
so zero is linearly attracting below the threshold and unstable above it (with zero linear derivative at equality). At a nonzero root, the factor (eta^2/2)(S+Q Sigma)^2-2 vanishes, so
f'(Sigma)=Sigma eta^2 Q(S+Q Sigma).
Consequently,
f'(Sigma_-)=2 eta(2/eta-S),
f'(Sigma_+)=2 eta(2/eta+S)>0.
Therefore every physically present Sigma_+ is unstable. Sigma_- is stable exactly when S>2/eta; in that regime Sigma_->0 exactly when Q<0. Hence a stabilizing quartic coefficient Q<0 produces a stable finite positive extent above the threshold, whereas the zero-extent state has already become unstable. This is the claimed finite-amplitude self-stabilization.
