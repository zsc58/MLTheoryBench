# Problem

## Setup

Fix eta>0. For a twice continuously differentiable scalar loss L, let m be a center variable and Sigma>=0 an extent variable. Set delta=sqrt(Sigma), define G_+=L'(m+delta), G_-=L'(m-delta), H_+=L''(m+delta), and H_-=L''(m-delta), and consider

dm/dt = -(eta/2)(G_+ + G_-) -(eta^2/8)(H_+ + H_-)(G_+ + G_-),

dSigma/dt = (eta^2/4)(G_+^2+G_-^2)-2 Sigma.

For the quadratic loss below, its sharpness is the scalar Hessian value S.

## Task

Prove the following integrated theorem.

1. For L_q(w)=S w^2/2 with S>0 and initial state m(0)=0, Sigma(0)>0, the extent satisfies
   Sigma(t)=Sigma(0) exp((eta^2 S^2/2-2)t).
   Deduce that the zero-extent state is attracting when S<2/eta, unstable when S>2/eta, and at the neutral transition when S=2/eta, for the extent dynamics on the symmetric branch m=0.

2. For L_4(w)=S w^2/2+Q w^4/4 with S>0, consider the symmetric branch m=0. In the stabilizing regime S>2/eta and Q<0, prove that the induced one-dimensional extent dynamics on this branch have a finite positive equilibrium
   Sigma_* = -(S-2/eta)/Q,
   and that this extent equilibrium is locally asymptotically stable to extent perturbations within the branch. Also show that the zero-extent state is linearly unstable in the extent direction above the threshold S=2/eta.
