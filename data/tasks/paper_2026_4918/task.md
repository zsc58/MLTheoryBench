# Problem

## Setup

Consider a K-armed bandit with K>=3 and a distinguished optimal arm y*. Let z in R^K be logits and let pi=softmax(z), so pi(a)>0 and sum_a pi(a)=1. Define the score phi_pi(a)=grad_z log pi(a)=e_a-pi, the objective J(z)=pi(y*), and the unit true-gradient direction u=phi_pi(y*)/||phi_pi(y*)|| with orthogonal projector Pi_perp=I-u u^T.

The reward is r=I{a=y*}, and use the constant baseline b=1/2. Thus U(y*)=1/2 and U(a)=-1/2 for a != y*. Samples are drawn from the contaminated law mu=(1-rho)pi+rho nu, where rho in [0,1] and nu is any distribution on the arms.

For eta>0 define ell(a)=-log pi(a), the sigmoid sigma(x)=1/(1+exp(-x)), and the learner-relative gate
w(a)=sigma(U(a)ell(a)/eta).
Define plain and gated sample-gradient vectors
G_plain(a)=U(a)phi_pi(a),   G_gate(a)=w(a)U(a)phi_pi(a),
and failure-only perpendicular second moments
V^A_perp,fail=E_{a~mu}[||Pi_perp G_A(a)||^2 I{a != y*}],  A in {plain,gate}.
Finally define
M_{nu,eta}^perp(pi)=sum_{a != y*} nu(a) pi(a)^(1/eta)||Pi_perp phi_pi(a)||^2
and S_nu^perp(pi)=sum_{a != y*} nu(a)||Pi_perp phi_pi(a)||^2.

## Task

Prove that

V^plain_perp,fail=(1/4) sum_{a != y*} mu(a)||Pi_perp phi_pi(a)||^2,

V^gate_perp,fail<=(1/4) sum_{a != y*} mu(a)pi(a)^(1/eta)||Pi_perp phi_pi(a)||^2.

Moreover, in any near-optimal regime with pi(y*)=1-delta, delta tending to zero, and q=max_{a != y*}pi(a)<=delta, show
M_{nu,eta}^perp(pi)<=4 q^(1/eta) tending to zero. Hence the rho-weighted contamination contribution in the gated bound is at most (rho/4)M_{nu,eta}^perp(pi) and vanishes for fixed rho and eta. In contrast, if S_nu^perp(pi)>=gamma for some constant gamma>0 throughout the regime, show that the plain contamination contribution equals (rho/4)S_nu^perp(pi)>=rho gamma/4 (for rho>0), so it remains bounded away from zero.
