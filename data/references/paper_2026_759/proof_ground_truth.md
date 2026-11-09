# Reference Proof

## Proof Structure

Fix a time and realized prefix. Reduce conditional-variance minimization to second-moment minimization, prove that the conditional mean is proposal-invariant, solve the constrained optimization including zero-probability tokens, and identify the normalized alpha-power proposal and its temperature form.

## Complete Proof

Fix t and h=(x,y_{<t}), and write p(v)=p_theta(v|h). Let S={v:p(v)>0}; let q be support-compatible, so q(v)>0 on S. Define Z=sum_u p(u)^alpha and omega(v)=p(v)^alpha/q(v) on S, with omega(v)=0 outside S. Then
E_q[omega]=sum_{v in S} q(v)p(v)^alpha/q(v)=Z,
so the conditional mean does not depend on q. Therefore minimizing conditional variance is equivalent to minimizing M(q)=E_q[omega^2]=sum_{v in S} p(v)^(2alpha)/q(v).

Let r=sum_{v in S}q(v). Writing q(v)=r q_tilde(v) on S gives M(q)=r^{-1}M(q_tilde), where q_tilde is a probability distribution on S. Hence an optimizer has r=1 and assigns no mass outside S. On the simplex over S, the Lagrangian
L(q,lambda)=sum_{v in S} p(v)^(2alpha)/q(v)+lambda(sum_{v in S}q(v)-1)
has stationarity condition -p(v)^(2alpha)/q(v)^2+lambda=0. Thus q(v)=p(v)^alpha/sqrt(lambda), and normalization gives sqrt(lambda)=Z. Hence q*(v)=p(v)^alpha/Z. Strict convexity on the positive simplex, together with the r=1 argument, gives uniqueness.

For q*, omega(v)=Z for every v in S, so its conditional variance is zero, which is the global minimum. If p(v)=softmax(ell)(v), then q*(v)=exp(alpha ell(v))/sum_u exp(alpha ell(u))=softmax(ell/tau)(v) with tau=1/alpha. Thus the optimizer is realized by temperature sampling at temperature 1/alpha.
