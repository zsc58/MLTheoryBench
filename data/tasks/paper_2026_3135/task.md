# Problem

## Setup

Let (S,mathcal S) be a measurable state space, let d>=1 be an integer, and let the action space be R^d with its Borel sigma-algebra and Euclidean norm ||.||. Consider a discounted infinite-horizon Markov decision process with discount gamma in [0,1), a bounded measurable reward r:S x R^d -> R that is continuous in the action variable, and a measurable probability transition kernel P(.|x,a) on S.

A stationary Markov policy pi is a measurable probability kernel from S to R^d. Starting with X_0 distributed according to a probability law rho, generate U_h conditionally according to pi(.|X_h) and X_(h+1) conditionally according to P(.|X_h,U_h). Define

V^pi(rho)=E_rho^pi[sum_(h=0)^infinity gamma^h r(X_h,U_h)],

V^pi(x)=V^pi(delta_x),    V*(x)=sup_pi V^pi(x),    V*(rho)=integral_S V*(x)rho(dx).

When gamma=0, only the h=0 reward is retained. Assume V* is measurable and that there is a measurable optimal deterministic selector g*:S -> R^d such that V^(delta_g*)(x)=V*(x) at every state and

g*(x) in A*(x):=argmax_(a in R^d) Q*(x,a),

where Q*(x,a)=r(x,a)+gamma integral_S V*(y)P(dy|x,a).

Fix a probability law mu_0 on R^d with m_2(mu_0):=integral_R^d ||a||^2 mu_0(da)<infinity. Fix constants 0<kappa<=Lambda<infinity. For horizon T>0, a diffusion policy is a measurable terminal-law kernel

pi_(f,sigma,T)(.|x)=Law(A_T^x)

of the state-conditioned equation

dA_t^x=f(t,A_t^x,x)dt+sigma(t,A_t^x,x)dB_t,    A_0^x distributed according to mu_0.

Here f:[0,T] x R^d x S -> R^d and sigma:[0,T] x R^d x S -> R^(d x d) are measurable deterministic functions. The solution is adapted to a filtration with respect to which B is a d-dimensional Brownian motion, and A_0^x is independent of B. For the general admissible policy class, the equation has a unique weak solution at every state. The same law mu_0 is used for every state, budget, horizon, and admissible policy. All volatilities satisfy

kappa I_d <= sigma(t,a,x)sigma(t,a,x)^T <= Lambda I_d

in the positive-semidefinite matrix order, with the same kappa and Lambda independently of the budget, horizon, coefficients, and state.

A drift has budget K if K>=1,

||f(t,a,x)-f(t,a',x)|| <= K||a-a'||

for all t,x,a,a', and integral_0^T ||f(t,0,x)||dt<infinity for every x.

Assume the following local action-continuity condition. For every x, there are R_x>0 and finite nonnegative nondecreasing functions omega_(r,x),omega_(P,x) on [0,R_x], each tending to zero at zero, such that whenever ||a-g*(x)||<=R_x,

|r(x,a)-r(x,g*(x))| <= omega_(r,x)(||a-g*(x)||),

TV(P(.|x,a),P(.|x,g*(x))) <= omega_(P,x)(||a-g*(x)||).

Here TV(mu,nu)=sup_(E in mathcal S)|mu(E)-nu(E)|.

## Task

Prove both assertions.

1. For every fixed T>0, define, for every K>=1,

c_K(x)=g*(x)/(1-exp(-KT)),    f_K(t,a,x)=K(c_K(x)-a).

Suppose that for every K>=1 and every state x this mean-reverting equation admits a weak solution initialized independently of Brownian motion with law mu_0, and that its terminal laws define a measurable policy pi_K. The volatility may depend on K but must satisfy the fixed covariance bounds above. Prove that, for every initial state probability law rho,

lim_(K->infinity) |V^(pi_K)(rho)-V*(rho)|=0.

2. For this assertion additionally suppose mu_0 is absolutely continuous with respect to Lebesgue measure. Fix an integer M>=1 and R>0. Suppose every A*(x) is finite with 1<=|A*(x)|<=M, and there is lambda_(M,R)>0, independent of x, such that for all x,a,

V*(x)-Q*(x,a) >= lambda_(M,R)(dist(a,A*(x))^2 wedge R^2).

For a nonempty set Z, dist(a,Z)=inf_(z in Z)||a-z||, and u wedge v=min(u,v). Prove that there exist c_(M,R)>0 and K_0<infinity depending only on M,R,d,kappa,Lambda,mu_0 such that, for every K>=K_0, every T>0, every admissible diffusion policy pi_(f,sigma,T) with drift budget K, and every initial state probability law rho,

V*(rho)-V^(pi_(f,sigma,T))(rho) >= c_(M,R)lambda_(M,R)/K.

In particular, the constants are independent of target locations and separations, gamma, rho, the admissible coefficients, and T.
