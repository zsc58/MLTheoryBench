# Problem

## Setup

Let n and m be positive integers. Consider the discrete-time bilinear system

x_{t+1}=A x_t+sum_{i=1}^m u_t[i] B_i x_t+w_t=Theta_* z_t+w_t,  t>=0,

where x_t in R^n, u_t in R^m, A,B_i in R^{n by n},

z_t=[x_t^T,(u_t tensor x_t)^T]^T,

and Theta_*=[A B_1 ... B_m] is unknown. Here tensor denotes the Kronecker product. Let w_max>0 and

W={w in R^n:||w||_infty<=w_max}.

For a positive integer T, observe D_T={(z_t,x_{t+1})}_{t=0}^{T-1} and define

S_T=intersection_{t=0}^{T-1}{Theta in R^{n by (n+nm)}:x_{t+1}-Theta z_t belongs to W}.

For a nonempty set S of such matrices, define

diam(S)=sup_{Theta,Theta' in S}||Theta-Theta'||_F,

where ||.||_F is the Frobenius norm, with diam(S)=infinity if S is unbounded.

Assume the following.

1. The inputs u_t are i.i.d., centered, satisfy ||u_t||_infty<=u_max almost surely for a finite u_max>0, and have covariance sigma_u^2 I_m with sigma_u>0. The input sequence is independent of the initial state and the entire disturbance sequence.
2. The disturbances w_t are i.i.d., centered, supported on W, and satisfy Cov(w_t) succeq sigma_w^2 I_n for sigma_w>0. For every v in R^n with ||v||_2=1, v^T w_t has a centered symmetric log-concave density.
3. The initial state satisfies E||x_0||_2^2<infinity. The pair (x_0,w_0) is independent of the future disturbance sequence (w_t)_{t>=1}; x_0 and w_0 themselves need not be independent.
4. There are c_w>0 and epsilon_0 in (0,w_max] such that, for every coordinate j, sign b in {+1,-1}, and 0<e<=epsilon_0,

P(b w_t[j]>=w_max-e)>=c_w e.

Define

TildeA=A tensor A+sigma_u^2 sum_{i=1}^m B_i tensor B_i,

and assume rho(TildeA)<=1, where rho denotes spectral radius.

## Task

Prove that there exist an integer r in {0,...,n^2} and a constant 0<C_z<infinity, depending only on the fixed model parameters and E||x_0||_2^2 and not on T, eta, or epsilon, for which the following holds.

Define

k_z=(sigma_w/2)(sqrt(min{1,sigma_u^2})/2),

p_z=3 min{1,sigma_u^2}/[128(1+m u_max^2)],

d_z=n+nm,  d_gamma=n^2+n^2m.

For every eta in (0,1), every epsilon in (0,16 sqrt(n) epsilon_0/(k_z p_z)], and every positive integer T, set

epsilon_z=min{k_z^2 p_z^2 eta/(192 C_z T^{r+1}),1/4},

epsilon_gamma=min{k_z p_z sqrt(eta)/(16 sqrt(6 n C_z T^{r+1})),1/4},

L_z=1+log(1632T/eta)+5d_z log(d_z/epsilon_z),

L_gamma=1+log(1632/eta)+5d_gamma log(d_gamma/epsilon_gamma),

where log is the natural logarithm. If

T >= [256 sqrt(n)/(k_z p_z^3 c_w epsilon)] L_z L_gamma,

then

P(diam(S_T)>epsilon)<=eta.

Thus, with probability at least 1-eta, the feasible-set diameter is at most epsilon. Explain why the displayed implicit sample condition gives a tilde-O(1/epsilon) sample rate for fixed model parameters and fixed eta, where tilde-O suppresses powers of log(1/epsilon), with dimension and model dependence specified by the displayed formula.
