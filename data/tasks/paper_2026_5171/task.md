# Problem

## Setup

Let S be a finite training set and Q a finite test set. For parameters w, let U_S(w) and U_Q(w) be the vectors of model outputs on these sets, and assume F(w,z), hence these output maps, is C^2 in w. Define J_S(w)=D_w U_S(w), J_Q(w)=D_w U_Q(w), K_SS(w)=J_S(w)J_S(w)^T, and K_QS(w)=J_Q(w)J_S(w)^T.

Consider gradient flow for the training quadratic loss Phi_S(U_S)=1/2 (U_S-y)^T B (U_S-y), where B is constant, symmetric, and positive definite. Along a realized trajectory w(t), t in [s,T] with s<T, let g(t)=B(U_S(w(t))-y) and assume w'(t)=-J_S(t)^T g(t), g'(t)=-B K_SS(t)g(t), where time arguments mean evaluation at w(t). Let P(t) solve P'(t)=-B K_SS(t)P(t), P(s)=I. Define

G = int_s^T K_QS(t)P(t) dt,
D = int_s^T K_SS(t)P(t) dt,
A_circ = G D^dagger.

Assume all displayed integrals exist, and let M^dagger denote the Moore-Penrose pseudoinverse.

## Task

Prove the following integrated theorem for every finite realized window [s,T]:

U_Q(T)-U_Q(s) = A_circ (U_S(T)-U_S(s)).

No assumption of small or vanishing kernel drift, and no asymptotic limit, may be used or required.
