# Problem

## Setup

Fix K independent of dimension d. Let Z be uniform on {1,...,K}. Conditional on Z=r, X_0 is N(mu_r, sigma_0^2 I_d), where sigma_0^2>0 is fixed and there are constants 0<c_mu<=C_mu and 0<c_delta<=C_delta such that c_mu d <= ||mu_r||_2^2 <= C_mu d and c_delta d <= ||mu_r-mu_s||_2^2 <= C_delta d for every r != s. Evolve X_t by the VP Ornstein-Uhlenbeck diffusion

dX_t=-X_t dt+sqrt(2)dW_t,

so X_t|X_0 is N(e^{-t}X_0,(1-e^{-2t})I_d). Write p_r(x,t)=p(X_t=x|Z=r), p_t(x)=K^{-1}sum_r p_r(x,t), posterior responsibilities gamma_r(x,t)=p(Z=r|X_t=x), and class-conditional entropy

H(t)=H(Z|X_t)=-integral p_t(x) sum_r gamma_r(x,t) log gamma_r(x,t) dx.

Define the class scores s_r(x,t)=gradient_x log p_r(x,t), and

m_r(t)=e^{-t}mu_r,  v(t)=e^{-2t}sigma_0^2+1-e^{-2t},  lambda_rs(t)=||m_r(t)-m_s(t)||_2^2/v(t).

## Task

Prove the following integrated theorem. First, the exact entropy-production identity holds:

(d/dt)H(t)=(1/(2K))sum_{r,s} E[gamma_s(X_t,t)||s_r(X_t,t)-s_s(X_t,t)||_2^2 | Z=r].

Equivalently, in the present Gaussian mixture,

(d/dt)H(t)=(1/(2Kv(t)))sum_r E[sum_{s != r} gamma_s(X_t,t)lambda_rs(t) | Z=r].

Set t_*(d)=1/2 log d. Moreover, entropy production vanishes along every sequence with t-t_*(d) -> -infinity and along every sequence with t-t_*(d) -> +infinity; the only regime in which it can remain non-negligible is t=t_*(d)+O(1) (equivalently lambda_rs(t)=Theta(1)).
