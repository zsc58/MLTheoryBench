# Reference Proof

## Proof Structure

1. Differentiate the conditional entropy using the Ornstein-Uhlenbeck Fokker-Planck equation and reduce the result to the difference between conditional and mixture Fisher-score energies.
2. Apply the mixture-score identity and the finite weighted-variance identity to obtain the exact pairwise entropy-production formula.
3. Compute the Gaussian scores and posterior log-odds, reducing each pairwise contribution to a factor involving the control parameter lambda_rs.
4. Analyze VP scaling: lambda_rs is comparable to d exp(-2t), and Gaussian concentration suppresses posterior competition when lambda is large, while the score-gap factor suppresses production when lambda is small. Hence only the logarithmic critical window can contribute.

## Complete Proof

Let p_r(x,t)=p_t(x|Z=r), p_t(x)=K^{-1} sum_r p_r(x,t), and s_r=gradient_x log p_r, s=gradient_x log p_t. The VP process has Fokker-Planck equation

partial_t q = div(x q) + (g_t^2/2) Delta q,

with g_t^2=2, and the stated Gaussian kernel. For any smooth density q with sufficient decay, integration by parts gives

(d/dt)h(q_t) = (drift term common to all components) + (g_t^2/2) I(q_t),

where I(q)=integral q ||gradient log q||^2. The common drift term cancels in h(X_t|Z)-h(X_t), so, using H(Z|X_t)=H(Z)-h(X_t)+h(X_t|Z),

(d/dt)H(Z|X_t) = (g_t^2/2)[K^{-1} sum_r I(p_r)-I(p_t)].

Since s=sum_r gamma_r s_r, where gamma_r=p_r/(sum_u p_u), the pointwise weighted-variance identity yields

sum_r gamma_r ||s_r||^2-||s||^2 = (1/2) sum_{r,s} gamma_r gamma_s ||s_r-s_s||^2.

Multiplying by p_t and using p_t gamma_r=K^{-1}p_r gives the exact identity

(d/dt)H(Z|X_t) = (g_t^2/4K) sum_{r,s} E[gamma_s(X_t,t)||s_r(X_t,t)-s_s(X_t,t)||^2 | Z=r].

(The diagonal terms are zero.)

Now p_r is N(m_r(t),v(t)I_d), with m_r=e^{-t}mu_r and v=e^{-2t}sigma_0^2+1-e^{-2t}. Thus

s_r(x,t)=-(x-m_r)/v,

so s_r-s_s=(m_r-m_s)/v is deterministic and

||s_r-s_s||^2=lambda_rs/v,  lambda_rs=||m_r-m_s||^2/v.

For equal priors, define Lambda_rs=log(p_r(X_t,t)/p_s(X_t,t)). Under Z=r, write X_t=m_r+sqrt(v)epsilon with epsilon standard Gaussian. Direct expansion of the two Gaussian log densities gives

Lambda_rs = lambda_rs/2 + sqrt(lambda_rs) xi_rs,

where xi_rs is standard normal (correlations between different s are immaterial). Also

gamma_s = exp(-Lambda_rs)/(1+sum_{u != r} exp(-Lambda_ru)).

Substitution therefore gives

(d/dt)H(Z|X_t) = (g_t^2/(4Kv)) sum_r E[sum_{s != r} gamma_s(X_t,t)lambda_rs(t) | Z=r].

For VP, v(t)=1+e^{-2t}(sigma_0^2-1) is bounded above and below by positive constants. The assumptions on pairwise mean separations imply constants c,C>0, independent of d and r != s, such that

c d e^{-2t} <= lambda_rs(t) <= C d e^{-2t}.

Consequently the scale at which all pairwise parameters are order one is t_s(d)=1/2 log d+O(1).

If lambda=lambda_rs tends to infinity, split according to A={Lambda_rs >= lambda/4}. On A, gamma_s <= exp(-lambda/4). Since Lambda_rs is N(lambda/2,lambda), Gaussian tail bounds give P(A^c)<=exp(-c_1 lambda). Therefore

E[lambda gamma_s] <= lambda exp(-lambda/4)+lambda exp(-c_1 lambda) -> 0.

With fixed K and the uniform comparability above, the whole finite sum tends to zero whenever t-t_s(d)->-infinity (equivalently lambda_rs->infinity; in particular for t/t_s(d)->u<1).

If lambda_rs tends to zero, simply gamma_s<=1 gives E[lambda_rs gamma_s]<=lambda_rs->0. Hence the entropy-production derivative tends to zero whenever t-t_s(d)->+infinity (in particular for t/t_s(d)->u>1).

When t=t_s(d)+O(1), lambda_rs=Theta(1), v=Theta(1), and neither suppression argument applies; this is the only regime in which the exact entropy-production expression can remain non-negligible. Thus entropy production is concentrated in an O(1) window around the logarithmic speciation scale t_s(d)=1/2 log d+O(1), as claimed.
