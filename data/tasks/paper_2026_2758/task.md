# Problem

## Parameters, data, and probability

Let T be a nonnegative integer and let L,H,N,B,d,k be positive integers. Put t_r=r/L and K={x in R^d: ||x||<=R_0}, where R_0>0. Vector norms are Euclidean and matrix norms are Frobenius unless indicated otherwise. Fix beta>0, lambda>0, epsilon>0, 0<beta_1<=beta_2<1, and deterministic learning rates 0<eta_j<lambda^{-1} for 1<=j<=T.

A head parameter is theta=(theta_Q,theta_K,theta_V,theta_O), with each block in R^{k x d}. Choose one of the following two optimizer maps R:

- Coordinatewise normalization: R(g)=g.
- Blockwise normalization: R(g)=(||g_Q||_F 1,||g_K||_F 1,||g_V||_F 1,||g_O||_F 1), where 1 is the k x d all-ones matrix.

Let pi be a probability law supported on {theta: ||R(theta)||_infinity<=lambda^{-1}}, where the infinity norm is the maximum absolute entry. Initialize theta_{r,0}^h independently with law pi for all 0<=r<L and 1<=h<=H.

Let Xi be any probability law on K^N. For each training step tau=0,...,T-1, draw B independent input vectors bold y_{b,tau} from Xi, independently across training steps and independently of all initial heads. No independence is assumed between the N tokens within an input vector. Write P^0 for the training-data law and P^1 for the head-initialization law, and use their completed product probability space. E^1 denotes expectation over P^1 with the training data fixed.

Let ell:P_2(R^d)->[0,infinity) be Lions differentiable. Assume its derivative has a jointly continuous representative such that, for each R>0, there are specified finite constants Lambda_ell(R),K_ell(R) satisfying

||partial_mu ell(mu)(x)-partial_mu ell(mu')(x')||
<=Lambda_ell(R)(||x-x'||+W_2(mu,mu')),

||partial_mu ell(mu)(x)||<=K_ell(R)

for x,x' in the radius-R closed ball and mu,mu' supported there. Here P_2 is the space of Borel probability laws with finite second moment. For measures on a Euclidean or matrix space, W_2 is the infimum, over couplings, of the square root of the expected squared Euclidean or Frobenius distance.

## Attention and adjoint fields

For compactly supported token and parameter laws mu and nu, define

gamma(z,mu)=(integral u exp(z.u) mu(du))/(integral exp(z.u) mu(du)),

Gamma(x,mu,nu)=integral theta_O^T theta_V gamma(beta theta_K^T theta_Q x,mu) nu(dtheta),

mathcal H(x,mu,nu,a)=a^T Gamma(x,mu,nu),

mathcal K(x,rho,nu,a)=nabla_x mathcal H(x,rho_x,nu,a)
+integral partial_mu mathcal H(y,rho_x,nu,p)(x) rho(dy,dp),

where rho is a compactly supported law on pairs (x,a) in R^d x R^d and rho_x is its first marginal. The symbols partial_mu and partial_nu denote Lions derivatives in the respective measure arguments; the latter takes values in the parameter matrix space with its Frobenius inner product. For the attention fields on compact supports, these derivatives are understood locally: take a smooth bounded cutoff of token or parameter arguments that agrees with the identity on a neighborhood of the supports and evaluation points, and differentiate the resulting lifting. The derivative values used here do not depend on this cutoff.

## Discrete model

For each training step tau and each deterministic input vector bold y=(y^1,...,y^N) in K^N, define x_{0,tau}^{i,bold y}=y^i and, for 0<=r<L,

bar nu_{r/L,tau}=H^{-1}sum_{h=1}^H delta_{theta_{r,tau}^h},
m_{r,tau}^{N,bold y}=N^{-1}sum_{i=1}^N delta_{x_{r,tau}^{i,bold y}},

x_{r+1,tau}^{i,bold y}=x_{r,tau}^{i,bold y}
+L^{-1}Gamma(x_{r,tau}^{i,bold y},m_{r,tau}^{N,bold y},bar nu_{r/L,tau}).

The discrete adjoints are defined backward by

a_{L,tau}^{i,bold y}=partial_mu ell(m_{L,tau}^{N,bold y})(x_{L,tau}^{i,bold y}),
rho_{r,tau}^{D,N,bold y}=N^{-1}sum_i delta_{(x_{r,tau}^{i,bold y},a_{r+1,tau}^{i,bold y})},

a_{r,tau}^{i,bold y}=a_{r+1,tau}^{i,bold y}
+L^{-1}mathcal K(x_{r,tau}^{i,bold y},rho_{r,tau}^{D,N,bold y},bar nu_{r/L,tau},a_{r+1,tau}^{i,bold y}).

Define the piecewise-constant extensions by

bar X_{t,tau}^{i,L,bold y}=x_{floor(Lt),tau}^{i,bold y} for 0<=t<1,
bar X_{1,tau}^{i,L,bold y}=x_{L,tau}^{i,bold y},

bar a_{t,tau}^{i,L,bold y}=a_{ceil(Lt),tau}^{i,bold y} for 0<t<=1,
bar a_{0,tau}^{i,L,bold y}=a_{0,tau}^{i,bold y}.

## Continuous model

The continuous parameter law is initialized by nu_{t,0}=pi for every t in [0,1]. For each tau and bold y in K^N, define

mu_{t,tau}^{N,bold y}=N^{-1}sum_i delta_{X_{t,tau}^{i,bold y}},
rho_{t,tau}^{N,bold y}=N^{-1}sum_i delta_{(X_{t,tau}^{i,bold y},a_{t,tau}^{i,bold y})},

dX_{t,tau}^{i,bold y}/dt=Gamma(X_{t,tau}^{i,bold y},mu_{t,tau}^{N,bold y},nu_{t,tau}),
X_{0,tau}^{i,bold y}=y^i,

da_{t,tau}^{i,bold y}/dt=-mathcal K(X_{t,tau}^{i,bold y},rho_{t,tau}^{N,bold y},nu_{t,tau},a_{t,tau}^{i,bold y}),
a_{1,tau}^{i,bold y}=partial_mu ell(mu_{1,tau}^{N,bold y})(X_{1,tau}^{i,bold y}).

## Training and coupled parameter measures

For either optimizer choice, a parameter trajectory with gradient sequence g_j starts with m_0=v_0=0 and follows, componentwise where appropriate,

m_j=beta_1 m_{j-1}+(1-beta_1)g_j,
v_j=beta_2 v_{j-1}+(1-beta_2)R(g_j) odot R(g_j),
mhat_j=m_j/(1-beta_1^j),
vhat_j=v_j/(1-beta_2^j),

theta_j=(1-eta_j lambda)theta_{j-1}-eta_j mhat_j/(sqrt(vhat_j)+epsilon).

Here odot, square roots, and division are entrywise. Different head trajectories have their own moment accumulators.

At training step tau, superscript b means evaluation on the same sampled vector bold y_{b,tau} in both models. Define the rescaled batch gradient maps

g^D_{r,tau+1}(theta)=(BN)^{-1}sum_{b=1}^B sum_{i=1}^N
partial_nu mathcal H(x_{r,tau}^{i,b},m_{r,tau}^{N,b},bar nu_{r/L,tau},a_{r+1,tau}^{i,b})(theta),

g^C_{t,tau+1}(theta)=(BN)^{-1}sum_{b=1}^B sum_{i=1}^N
partial_nu mathcal H(X_{t,tau}^{i,b},mu_{t,tau}^{N,b},nu_{t,tau},a_{t,tau}^{i,b})(theta).

The actual discrete head theta_{r,tau}^h is updated by the displayed optimizer using g_{tau+1}=g^D_{r,tau+1}(theta_{r,tau}^h). These are the batch loss gradients multiplied by LH.

For fixed t and initial parameter theta, let Phi_{t,0}(theta)=theta. Define Phi_{t,j}(theta) by the same optimizer, with its own zero initial moments and gradients g^C_{t,j}(Phi_{t,j-1}(theta)). Inductively set

nu_{t,tau}=(Phi_{t,tau})_# pi.

Thus the continuous model, its batch gradients, and its parameter laws are constructed in training-step order. They use only the training data and pi, not the sampled finite array of initial heads. The notation F_#pi denotes the pushforward law of F(theta) for theta with law pi.

Finally define, using the very same initial heads as the discrete model,

hat nu_{r/L,tau}=H^{-1}sum_{h=1}^H delta_{Phi_{r/L,tau}(theta_{r,0}^h)}.

In particular, these coupled heads use continuous-model gradients, not gradients computed from their own finite empirical system.

## Task

Prove that the constructions are well defined and that there are constants C_1,C_2 such that, for every integer 0<=tau<=T, P^0-almost surely,

E^1[max_{0<=r<L} W_2^2(hat nu_{r/L,tau},bar nu_{r/L,tau})]
<=C_1(L^{-2}+L^{-2/3}H^{-1}),

E^1[sup_{t in [0,1]} sup_{bold y in K^N} max_{1<=i<=N}
(||bar X_{t,tau}^{i,L,bold y}-X_{t,tau}^{i,bold y}||^2
+||bar a_{t,tau}^{i,L,bold y}-a_{t,tau}^{i,bold y}||^2)]
<=C_2(L^{-2}+L^{-2/3}H^{-1}).

The constants may depend only on T,beta,beta_1,beta_2,epsilon,lambda,R_0, the specified functions Lambda_ell and K_ell, and, for coordinatewise normalization, d and k. They are independent of L,H,N,B, the sampled training data, and the laws Xi and pi subject to the stated support conditions. Under blockwise normalization they can also be chosen independent of d and k, with the listed scalar bounds held fixed.

Conclude that the corresponding L2 errors are O(L^{-1}+L^{-1/3}H^{-1/2}).
