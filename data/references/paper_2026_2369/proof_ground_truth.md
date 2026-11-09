# Reference Proof

Write Delta L=L_{M_theta}-L_{M_obs} and use column gradients.

For a smooth scalar f and h, the score-based form gives

<L_M f,h>_p = integral [(M s+div M) dot grad f + D_M:Hess f] h p.

Since (div M)_i p + M_ij (grad log p)_j p = partial_j(M_ij p), integration by parts gives

<L_M f,h>_p = - integral M_ij (partial_i f)(partial_j h)p
                 + integral (D_M,ij-M_ij)(partial_i partial_j f)h p.

The last term vanishes because D_M-M is antisymmetric while Hess f is symmetric. Therefore

<L_M f,h>_p = -<(grad f)^T M grad h>_p. (1)

This calculation applies componentwise and uses exactly the stated smoothness and boundary assumptions.

For the observed correlation,

C_obs,alpha beta(t)=<K_t^obs phi_alpha,v_beta>_p.

Differentiating the semigroup and applying (1) gives

d C_obs,alpha beta(t)/dt
 = <L_{M_obs}K_t^obs phi_alpha,v_beta>_p
 = -<(grad K_t^obs phi_alpha)^T M_obs grad v_beta>_p. (2)

The transition-kernel representation is

K_t^obs phi_alpha(x_0)=integral phi_alpha(x_t)p_t^obs(x_t|x_0)dx_t.

The positivity, differentiability, and stated differentiation-under-the-integral assumptions imply

grad K_t^obs phi_alpha(x_0)
 = E[phi_alpha(X_t^obs)s_{t|0}(X_t|X_0)|X_0=x_0]. (3)

Substitution of (3) into (2), followed by averaging over the stationary pair, proves

d C_obs,alpha beta(t)/dt=A_{alpha beta,t}[M_obs].

For any smooth matrix field H, define L_H by the same displayed generator formula, without requiring H itself to be a mobility of a Markov diffusion. Applying (1) algebraically to H and subtracting the observed identity yields

A_{alpha beta,t}[H]-d C_obs,alpha beta(t)/dt
 = <(L_H-L_{M_obs})K_t^obs phi_alpha,v_beta>_p.

Taking H=M_theta proves

R_theta,alpha beta(t)=<Delta L K_t^obs phi_alpha,v_beta>_p.

If all fitted residuals vanish, then A_{alpha beta,t}[M_theta-M_obs]=0 for every selected alpha,beta,t, so the admissible difference belongs to N_A. This is a projected generator statement, not pointwise mobility identification.

For the quantitative estimate, define r_j=(mathsf R_theta,j1,...,mathsf R_theta,jq)^T. If f is any L2(p) function, the coefficient vector of P_V f in the basis v_1,...,v_q is G_V^{-1}(<f,v_1>_p,...,<f,v_q>_p)^T. Hence

||P_V f||_2^2 = b^T G_V^{-1}b <= lambda_V^{-1}||b||_2^2.

Applying this to f=Delta L u_j and summing over j gives

(sum_j ||P_V Delta L u_j||_2^2)^{1/2}
 <= lambda_V^{-1/2}||mathsf R_theta||_F
 <= lambda_V^{-1/2}epsilon. (4)

For each s in [0,T], choose a coefficient representation of P_U K_s^obs phi_alpha whose norm approaches the infimum in the definition of A_{U,alpha}(T). By (4),

||P_V Delta L P_U K_s^obs phi_alpha||_2
 <= A_{U,alpha}(T)lambda_V^{-1/2}epsilon. (5)

By the definition of zeta and the decomposition

Delta L K_s^obs phi_alpha
 = P_V Delta L P_U K_s^obs phi_alpha
   +(Delta L-P_V Delta L P_U)K_s^obs phi_alpha,

(5) implies, uniformly for 0<=s<=T,

||Delta L K_s^obs phi_alpha||_2
 <= A_{U,alpha}(T)lambda_V^{-1/2}epsilon+zeta_{U,V,alpha}^theta(T). (6)

For the semigroup comparison, fix t in [0,T] and define

Psi_t(s)=K_{t-s}^theta K_s^obs phi_alpha, 0<=s<=t.

The explicit common-core and cross-generator assumptions in the task imply that Psi_t is absolutely continuous in L2(p) and, for almost every s,

d Psi_t(s)/ds
 = -K_{t-s}^theta L_{M_theta}K_s^obs phi_alpha
   +K_{t-s}^theta L_{M_obs}K_s^obs phi_alpha
 = -K_{t-s}^theta Delta L K_s^obs phi_alpha.

Since Psi_t(0)=K_t^theta phi_alpha and Psi_t(t)=K_t^obs phi_alpha, integration gives

K_t^theta phi_alpha-K_t^obs phi_alpha
 = integral_0^t K_{t-s}^theta Delta L K_s^obs phi_alpha ds. (7)

Thus the Duhamel step is not an unverified invocation: its domain, absolute continuity, generator actions, and integrability are exactly the explicit hypotheses of the task.

Because K_t^theta is a Markov semigroup preserving p, Jensen's inequality and invariance imply L2(p)-contractivity:

||K_t^theta f||_2 <= ||f||_2. (8)

Combining (6), (7), and (8), for 0<=t<=T,

||K_t^theta phi_alpha-K_t^obs phi_alpha||_2
 <= t[A_{U,alpha}(T)lambda_V^{-1/2}epsilon+zeta_{U,V,alpha}^theta(T)].

Finally,

C_theta,alpha beta(t)-C_obs,alpha beta(t)
 = <K_t^theta phi_alpha-K_t^obs phi_alpha,v_beta>_p,

so Cauchy-Schwarz proves the stated bound.
