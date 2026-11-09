# Problem

## Setup

Consider the deterministic scalar system x_{t+1}=a*x_t+b*u_t, with q,r>0, gamma in (0,1), b nonzero, and |a|<=1-delta_0 for some delta_0>0. The initial law rho has a positive, finite scale sigma_rho^2 satisfying E_rho[x_0^2*1_{x_0>=0}]=E_rho[x_0^2*1_{x_0<0}]=sigma_rho^2/2. For a deterministic feedback law mu, set J_rho(mu)=E_rho[sum_{t>=0} gamma^t*(q*x_t^2+r*u_t^2)], with u_t=mu(x_t). Call mu stabilizing when every closed-loop trajectory converges to zero. Let mu*(x)=K*x be the unique optimal scalar discounted-LQR controller and P* its value coefficient, so its value from x is P*x^2.

For width m>=2, use the bias-free one-hidden-layer ReLU controller mu_theta(x)=sum_{j=1}^m v_j*[w_j*x]_+, where [z]_+=max(z,0). Define K_1(theta)=sum_{w_j>=0}v_j*w_j and K_2(theta)=sum_{w_j<0}v_j*w_j. Thus mu_theta(x)=K_1*x for x>=0 and K_2*x for x<0. Write ||mu-mu*||_2^2=(K_1-K*)^2+(K_2-K*)^2. For the gradient update below, use the ReLU derivative convention [z]_+'=0 at z=0; in particular a neuron with w_j=0 has zero selected derivatives with respect to both of its weights.

Choose 0<delta<delta_0, set delta_bar=delta/2, and define K_delta={(K_1,K_2): |a+b*K_i|<=1-delta for i=1,2}; K_{delta_bar} is defined analogously. Let Phi be the standard normal cdf. Fix 0<s<S<infinity, V>0, beta>0, iota>0, and epsilon in (0,1). Set alpha=beta^(-2), tau=s*sqrt(beta), W=S*sqrt(beta), c=(1-epsilon)*(Phi(S)-Phi(s))*(2*Phi(V*beta)-1), and lambda_*=c*tau^2/4. Let K_max=(|a|+1-delta_bar)/|b|, phi_max=q+r*K_max^2, P_max=phi_max/[1-gamma*(1-delta_bar)^2], and Delta_max=sigma_rho^2*P_max-J_rho(mu*).

Take positive constants L_mu, alpha_mu, C_grad, G_max. Define B=2*sqrt(C_grad*Delta_max)/(lambda_* *alpha_mu), R_c=sqrt(W^2+V^2), R_*^2=(1+epsilon)*(alpha+beta), and G_*=exp(2B)*R_*^2. For B satisfying exp(B)*B<1, set tau_w=[exp(B)*B/sqrt(1-exp(2B)*B^2)]*V. Let Z and U be independent standard normal variables. Choose deterministic M_w,M_v>0 satisfying M_w>E[(beta*Z^2+alpha*U^2)*1_{|sqrt(beta)*Z|<=tau_w}] and M_v>E[(beta*Z^2+alpha*U^2)*1_{|sqrt(alpha)*U|>V}]. Set Xi_*=exp(2B)*(M_w+M_v), L_*=(3/2)*G_*+2*sqrt(2)*Xi_*, and C_*=(1/2)*G_* *G_max+(L_mu/2)*L_*^2. All constants and thresholds are fixed before m is chosen.

With eta_m=iota/m, the benign width regime means that all of the following hold: eta_m*G_max<=1; eta_m*lambda_* *alpha_mu<=1; exp(B)*B<1; exp(B)*B*R_c<=tau/2; 2*sqrt(2)*Xi_*<=lambda_*/4; eta_m*C_*<=lambda_*/4; and |b|*L_* *B<=delta/2. The cutoff tau_w and its threshold condition are evaluated only when exp(B)*B<1.

## Task

Prove that there exist positive L_mu, alpha_mu, C_grad, G_max, C_0, deterministic thresholds M_w,M_v as specified above, and m_0, depending only on the stated system, initial law, margin, and fixed initialization parameters, with L_mu chosen from the gain-space smoothness bound, such that if iota<1/L_mu, then for every m>=m_0 in the benign width regime the following holds. Initialize weights independently with w_{j,0} distributed N(0,beta/m) and v_{j,0} distributed N(0,beta^(-2)/m), and use theta_{k+1}=theta_k-eta_m*grad_theta J_rho(theta_k) with the stated ReLU derivative convention. With probability at least 1-exp(-C_0*m), every iterate is stabilizing and (K_1(theta_k),K_2(theta_k)) belongs to K_{delta_bar}; for all k>=0,

J_rho(mu_{theta_k})-J_rho(mu*) <= rho_m^k*[J_rho(mu_{theta_0})-J_rho(mu*)],

where rho_m=1-eta_m*alpha_mu*(1-epsilon)*(Phi(S)-Phi(s))*(2*Phi(V*beta)-1)*s^2*beta/4. Moreover, for every k>=0,

||mu_{theta_k}-mu*||_2^2 <= [J_rho(mu_{theta_0})-J_rho(mu*)]*rho_m^k / [(r+gamma*b^2*P*)*(sigma_rho^2/2)].
