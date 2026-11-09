# Reference Proof

Write J_F and J_P for the transpose Jacobians of F and Psi, and put r=F-Psi. Set a=bar L_f, b=bar L_nabla f, u=bar L_Psi, v=bar L_nabla Psi, H=L_nabla g, T=L_nabla^2 g, and L=L_g. Conditional Jensen gives the derivative identity and random Lipschitz modulus for F. Differentiating under expectation gives

nabla G=E[J_F nabla g(F)],
nabla_beta Q=E[J_F r], and nabla_theta Q=-E[J_P r].

Fix lambda>max{H,2Mu^2H}, and let A=lambda/M-2u^2H>0. The lower smoothness inequality for g gives g(F)-g(Psi)-nabla g(Psi)^T r >= -H||r||^2/2. Thus Delta^lambda>=0 and W^lambda>=G>=G^min.

At a point (beta,theta), set h=nabla G, B=E[J_F(nabla g(F)-nabla g(Psi))], D=E[J_F r], and t=E[J_P r]. The conditional mean direction is Gamma=(-h+B,gamma t). Direct differentiation gives nabla_beta W=h+B+lambda D and nabla_theta W=-E[J_P nabla^2 g(Psi)r]-lambda t. Since E||r||^2=2Q, Cauchy-Schwarz and the derivative envelopes give ||B||<=aH sqrt(2Q), ||D||<=a sqrt(2Q), and ||E[J_P nabla^2 g(Psi)r]||<=uH sqrt(2Q). Also ||t||<=u sqrt(2Q), while (A4) gives ||t||^2>=Q/M. Consequently

<nabla_theta W,gamma t> <= -gamma A Q.

For the beta component, expand <h+B+lambda D,-h+B>=-||h||^2+||B||^2-lambda<D,h>+lambda<D,B>. Because lambda>=H, its upper bound is

-||h||^2+lambda a||h||sqrt(2Q)+4lambda a^2 H Q.

Young's inequality with epsilon=1 therefore yields

<nabla W,Gamma> <= -(gamma A-4lambda a^2 H-lambda^2 a^2)Q-||h||^2/2.

Choose gamma_min=(1+4lambda a^2 H+lambda^2 a^2)/A, c_1=1, and c_2=1/2. For every gamma>gamma_min the last display is at most -V. The chosen c_1,c_2 work uniformly over that entire range of gamma.

Here is an explicit uniform smoothness bound. Put C=C_f+C_Psi and D_0=H+lambda. Comparing the beta gradients at (beta,theta) and (beta',theta') gives respective coefficients

K_bb=b(3L+lambda C)+(2H+lambda)a^2, and K_bt=(H+lambda)au

on ||beta-beta'|| and ||theta-theta'||. Comparing the theta gradients gives

K_tb=D_0ua, and K_tt=vD_0C+Tu^2C+D_0u^2.

To verify these bounds, split each difference into a change of Jacobian and a change of its remaining factor. Use the L_nabla f and L_nabla Psi envelopes for the former, and |F(beta)-F(beta')|<=E[L_f|X]||beta-beta'|| and |Psi(theta)-Psi(theta')|<=L_Psi(X)||theta-theta'|| for the latter. For the Hessian change use its T-Lipschitz bound and E[L_Psi^2||r||]<=u^2 C, by Cauchy-Schwarz and the fourth moment of L_Psi. These estimates also justify the differentiated expectations. Thus L_W=1+sqrt(K_bb^2+K_bt^2+K_tb^2+K_tt^2) is a global Lipschitz constant for nabla W.

Let tilde d^k be the stacked sample direction and d^k=E[tilde d^k|F_k]=Gamma(z^k). Set e^k=tilde d^k-d^k. Independence of the fresh pair gives E[e^k|F_k]=0. The inequality ||f-Psi||^4<=8(||f||^4+||Psi||^4), followed by Cauchy-Schwarz, gives the parameter-uniform bound

E[||tilde d^k||^2|F_k] <= B_0 := L^2 a^2+gamma^2 u^2 sqrt(8(C_f^4+C_Psi^4)).

Conditional Jensen and the variance identity give ||d^k||^2<=B_0 and E[||e^k||^2|F_k]<=B_0. Take C_d^2=sigma^2=1+B_0. These constants can depend on the fixed gamma, but not on k, N, or alpha.

The smoothness inequality, conditioned on F_k, now gives

E[W(z^{k+1})|F_k] <= W(z^k)+tau_k<nabla W(z^k),d^k>+(L_W tau_k^2/2)(C_d^2+sigma^2)
<=W(z^k)-tau_k V(z^k)+(L_W tau_k^2/2)(C_d^2+sigma^2).

The zero conditional mean of e^k eliminates both its linear term and its cross term with d^k. Take total expectations and sum for k=0,...,N-1 with tau_k=alpha/sqrt(N). Since W(z^N)>=G^min, division by alpha sqrt(N) gives

(1/N)sum_{k=0}^{N-1} E[V(z^k)] <= { (L_W/2)(C_d^2+sigma^2)alpha^2+W(z^0)-G^min }/(alpha sqrt(N)).

Independence and uniformity of S identify the left side with E[V(z^S)]. The numerator is independent of N for fixed alpha and gamma, proving the stated rate.
