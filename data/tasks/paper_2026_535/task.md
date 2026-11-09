# Problem

## Population setting

Let X and Y be measurable spaces, let rho be a probability measure on X, and let pi_ref(dy|x) be a fixed probability kernel on Y. Let r:X times Y -> [0,r_max] be measurable, where 0<r_max<infinity. Assume that, for rho-almost every x, the distribution of r(x,Y) under Y~pi_ref(.|x) has a density with respect to Lebesgue measure.

Let P be the set of probability kernels pi such that pi(.|x) is absolutely continuous with respect to pi_ref(.|x) for rho-almost every x. Kernels that agree outside a rho-null set of contexts are identified. All kernels, density versions, random sample maps, and residuals used below are assumed jointly measurable.

Fix a nonnegative, nondecreasing function f:[0,1]->R with integral_0^1 f(u)du=1. Suppose |f(u)-f(v)|<=L_f|u-v| for a finite L_f>=0. Define

C_pi(x,s)=integral 1{r(x,y)<=s} pi(dy|x),  0<=s<=r_max,

T[pi](dy|x)=f(C_pi(x,r(x,y)))pi(dy|x),

R[pi]=integral_X integral_Y r(x,y)T[pi](dy|x)rho(dx).

For probability kernels nu and pi, define

KL(nu|pi)=integral_X KL(nu(.|x)|pi(.|x))rho(dx),

with the usual value +infinity when absolute continuity or finite relative entropy fails. Fix beta>0 and define the extended-valued loss

L[pi]=-R[pi]+beta KL(pi|pi_ref).

For a measurable function h and two policies, write

<h,nu-pi>=integral_X integral_Y h(x,y)(nu-pi)(dy|x)rho(dx)

whenever this pairing is defined. A functional derivative is a representative of directional variation under this pairing and is defined up to addition of a function of x. For a real measurable h, define its conditional span seminorm by

||h||_sp,x=(ess sup_y h(x,y)-ess inf_y h(x,y))/2,

where both essential extrema are with respect to pi_ref(.|x).

## Empirical estimator and updates

Let M and T be positive integers. Choose a fixed initial policy pi_0 and a constant L>0 with L>=L_f r_max, and set eta=1/L.

At each iteration t=0,...,T-1, the current policy pi_t is determined before the new samples are drawn. At each context x, draw M responses Y_{t,1}(x),...,Y_{t,M}(x) whose conditional joint distribution given the preceding history is pi_t(.|x) to the M-th product power. No independence between different contexts is required. Define

Chat_t(x,s)=M^(-1) sum_{j=1}^M 1{r(x,Y_{t,j}(x))<=s},

ghat_t(x,y)=integral_{r(x,y)}^{r_max} f(Chat_t(x,s))ds.

This formula defines the empirical loss-gradient estimator. In particular, it does not require the empirical reward distribution to have a density. Let

e_t=ghat_t-d(-R)[pi_t].

The definition is independent of the choice of population derivative representative when measured by the span seminorm.

Write p_t(x,y)=dpi_t(.|x)/dpi_ref(.|x)(y). Suppose the iterates have strictly positive finite densities p_t almost everywhere with respect to rho(dx)pi_ref(dy|x), and that the inexact update satisfies, up to addition of a function of x,

ghat_t(x,y)+L log(p_{t+1}(x,y)/p_t(x,y))+beta log p_{t+1}(x,y)=r_t(x,y).

The update and residual may depend on the current samples and on optimization randomness. Suppose that, for finite epsilon,delta>=0 and rho-almost every x,

E[||e_t||_sp,x^2 | pi_t]<=epsilon,

E[||r_t||_sp,x^2 | pi_t]<=delta.

Here conditioning on pi_t means conditioning on the current policy kernel. Let pi_* denote the minimizer whose existence and uniqueness are to be proved. For the convergence claim, assume almost surely that KL(pi_t|pi_ref) and KL(pi_*|pi_t) are finite for 0<=t<=T, and KL(pi_{t+1}|pi_t) is finite for 0<=t<T.

## Task

Prove the following claims.

1. T[pi] is a probability kernel for every pi in P. The reward functional R is concave and KL-relative smooth with constant L_f r_max: for pi,nu in P,

   R[nu]<=R[pi]+<dR[pi],nu-pi>,

   R[nu]>=R[pi]+<dR[pi],nu-pi>-L_f r_max KL(nu|pi).

   Establish the functional derivative needed in these statements. Also prove that L[pi] has a unique minimizer pi_* in its finite-KL domain. When L_f r_max>0 one may choose L=L_f r_max; when it is zero, retain any positive L.

2. For the empirical estimator specified above and rho-almost every context x,

   E[||e_t||_sp,x^2 | pi_t]<=L_f^2 r_max^2/M.

3. Set q=(L+beta/2)/L. After generating the iterates, independently draw an index hat t in {1,...,T} with

   P(hat t=k)=q^k/(sum_{j=1}^T q^j).

   Prove

   E[L[pi_hat t]-L[pi_*]]
   <= ((beta/2)KL(pi_*|pi_0))/(q^T-1)+2(epsilon+delta)/beta.

   The expectation includes the samples, optimization randomness, and final index draw; R and KL already include the average over rho. In particular, substituting epsilon=L_f^2 r_max^2/M gives the dimension-independent floor

   2 L_f^2 r_max^2/(beta M)+2 delta/beta.

   Thus the sampling contribution is O(1/M), and the entire floor is O(1/M) if delta=0 or delta=O(1/M).
