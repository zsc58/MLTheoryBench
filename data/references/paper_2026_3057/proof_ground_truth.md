# Reference Proof

The argument is pathwise for any realized solution satisfying the stated assumptions.

First set A(x) = J_h(x) J_h(x)^T and r = h(x) + s. If s_i = 0, then

    dot{s}_i = c ReLU(-h_i(x) - lambda_i/c) >= 0.

The usual first-exit argument therefore gives s_t >= 0 componentwise for all t in [0,1).

By the compactness part of (B3) and continuity of h, there are finite constants H and S such that ||h(x_t)|| <= H and ||s_t|| <= S. By (B1), if b(x,t) = J_h(x)v(x,t), then ||b(x_t,t)|| <= L B. By (B2), ||A(x_t)||_2 <= a_max.

Set tau = -log(1-t) and eta = (1-t)lambda = exp(-tau)lambda. Then d t/d tau = exp(-tau). The dual equation gives

    eta' = r - eta.

Differentiating r = h(x) + s and using the three original equations gives

    r' = -A(x) eta + exp(-tau)[b(x,t) - c A(x) r + c(u-s)],

where u = ReLU(-h(x) - lambda/c). Let q = -h(x) - lambda/c and let E be the diagonal projector whose i-th diagonal entry is 1 when q_i > 0 and 0 otherwise. On an active component,

    u_i = -h_i - lambda_i/c = -r_i + s_i - exp(tau) eta_i/c,

while on an inactive component u_i = 0. Consequently, for almost every tau,

    r' = -(A(x) + E) eta + exp(-tau) F_E,
    eta' = r - eta,

where

    F_E = b(x,t) - c(A(x) + E)r - c(I_k-E)s.

At a switching value q_i = 0, either choice of the corresponding diagonal entry gives the same value of the right-hand side, so the equations and the estimates below extend across switches.

Write Delta(x) = A(x) - A_* and z = (r,eta). With

    M_E = [[0, -(A_*+E)], [I_k, -I_k]],

we have

    z' = M_E z + (-Delta(x) eta + exp(-tau) F_E, 0).

The public task defines

    P = [[I_k, -I_k/2], [-I_k/2, A_*+I_k/2]]

and

    D_E = [[-I_k, I_k-E], [I_k-E, E-A_*-I_k]].

The Schur complement of the upper-left block of P is A_* + I_k/4, so P is positive definite. Direct block multiplication gives

    M_E^T P + P M_E = D_E.

The upper-left block of D_E is -I_k. Its Schur complement is

    (E-A_*-I_k) + (I_k-E)^2 = -A_*,

because E is a diagonal 0-1 projector. Thus D_E is negative definite for every E. Since the set of such E is finite, the public definition

    kappa_0 = (1/2) min_E lambda_min(-D_E)

is positive, and

    z^T P M_E z <= -kappa_0 ||z||^2.

Let V(z) = (1/2) z^T P z. Its r-gradient is

    grad_r V = r - eta/2,

and therefore

    ||grad_r V|| <= (sqrt(5)/2) ||z||.

The forcing is uniformly bounded. Indeed, ||E||_2 <= 1 and

    ||F_E|| <= L B + c(a_max+1)(H+S) + c S =: C_F.

Differentiating V along the switched system and separating the frozen part gives

    V' = z^T P M_E z - (grad_r V)^T Delta(x) eta
         + exp(-tau)(grad_r V)^T F_E.

The variation term satisfies

    |(grad_r V)^T Delta(x) eta|
      <= (sqrt(5)/2) ||Delta(x)||_2 ||z||^2
      <= rho ||z||^2.

The forcing term is bounded by

    exp(-tau) (sqrt(5)/2) C_F ||z|| = exp(-tau) K ||z||,

where K = (sqrt(5)/2) C_F. Hence, using rho < kappa_0,

    V' <= -(kappa_0-rho)||z||^2 + exp(-tau) K ||z||.

Let

    c_1 = lambda_min(P)/2,
    c_2 = lambda_max(P)/2.

Then c_1 ||z||^2 <= V <= c_2 ||z||^2. Set y = sqrt(V). Where y > 0,

    y' = V'/(2y)
       <= -(kappa_0-rho)y/(2c_2) + K exp(-tau)/(2 sqrt(c_1)).

The same inequality holds in the upper-right-derivative sense when y = 0. Since the public definition gives Lambda = lambda_max(P) = 2c_2, this is

    y' <= -alpha y + gamma exp(-tau),

where

    alpha = (kappa_0-rho)/Lambda > 0,
    gamma = K/(2 sqrt(c_1)).

An integrating-factor comparison gives

    y(tau) <= y(0) exp(-alpha tau)
       + gamma integral from 0 to tau of
         exp(-alpha(tau-u)) exp(-u) du.

Moreover, lambda_max(P) >= 1, while lambda_min(-D_E) <= 1 by testing -D_E on vectors of the form (q,0). Thus kappa_0 <= 1/2 and alpha <= 1/2. The convolution term is therefore O(exp(-alpha tau)), including the possible equal-exponent case, and

    y(tau) = O(exp(-alpha tau)).

Norm equivalence now gives

    ||r|| + ||eta|| = O(exp(-alpha tau)).

Since exp(-tau) = 1-t and eta = (1-t)lambda,

    ||r_t|| = O((1-t)^alpha),
    (1-t)||lambda_t|| = ||eta_t|| = O((1-t)^alpha).

Finally, s_t >= 0 implies ReLU(h(x_t)) <= ReLU(h(x_t)+s_t) componentwise. Since ReLU is componentwise nonexpansive,

    ||ReLU(h(x_t))|| <= ||r_t||.

Therefore ||ReLU(h(x_t))|| tends to zero and has the stated O((1-t)^alpha) rate, while the rescaled dual variable has the other stated rate.
