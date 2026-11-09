# Problem

## Setup

Let d,T be positive integers, let 0<r<=R, and let G,L>0. Write B_2={x in R^d: ||x||_2<=1}. Let X be compact and convex with r B_2 subseteq X subseteq R B_2.

Fix a sequence of differentiable losses ell_1,...,ell_T, independently of the algorithm's random samples. For every x,y in X and every t, assume

|ell_t(x)-ell_t(y)|<=G||x-y||_2,

||nabla ell_t(x)-nabla ell_t(y)||_2<=L||x-y||_2.

The losses are either all linear, all convex, or all lambda-strongly convex for a known lambda>0. In the last case, strong convexity means

ell_t(y)>=ell_t(x)+<nabla ell_t(x),y-x>+(lambda/2)||y-x||_2^2

for every x,y in X.

The learner observes only the two queried function values at each round. Define

delta=min{r/2,1/(2d^2LTR)},  xi=delta/r,  K=(1-xi)X,

and let Pi_K denote Euclidean projection onto K.

## Algorithm

Initialize hat w_1=0 and Vbar_0=0. At the start of round t, let m_t in R^d store, in each coordinate i, the value v_s from the most recent previous round s<t with i_s=i, or zero if that coordinate has not occurred. Thus m_1=0, and m_t uses only previous observations.

Choose the step size

eta_t=R/sqrt(d^2+Vbar_{t-1})

in the linear or convex case, and

eta_t=1/(lambda t)

in the strongly convex case. Set

w_t=Pi_K(hat w_t-eta_t m_t).

Independently of the previous samples, draw i_t uniformly from {1,...,d}, where e_i denotes the i-th standard basis vector. Query

x_t^+=w_t+delta e_{i_t},  x_t^-=w_t-delta e_{i_t},

and set

v_t=[ell_t(x_t^+)-ell_t(x_t^-)]/(2delta).

Let a_t be the most recent s<t with i_s=i_t, or zero if there is no such round, and use v_0=0. Define

g_t=m_t+d(v_t-v_{a_t})e_{i_t}.

Update

hat w_{t+1}=Pi_K(hat w_t-eta_t g_t),

Vbar_t=Vbar_{t-1}+||g_t-m_t||_2^2,

and replace coordinate i_t of the historical buffer by v_t, leaving its other coordinates unchanged.

## Performance quantities

For any tuple (z_1,...,z_T) in X^T, define

mu(z_1,...,z_T)=(1/T)sum_{t=1}^T nabla ell_t(z_t).

Define the deterministic gradient-variance quantity

W_T=sup_{(z_1,...,z_T) in X^T} sum_{t=1}^T ||nabla ell_t(z_t)-mu(z_1,...,z_T)||_2^2.

Define regret using the average of the two queried losses:

Reg_T=sum_{t=1}^T [ell_t(x_t^+)+ell_t(x_t^-)]/2-min_{x in X}sum_{t=1}^T ell_t(x).

Expectation is over the independent coordinate samples.

## Task

Prove that the algorithm satisfies

- E[Reg_T]=O(sqrt(dW_T)+d) for linear losses;
- E[Reg_T]=O(d sqrt(W_T+d)) for convex losses;
- E[Reg_T]=O((d/lambda)log(2+dW_T)) for lambda-strongly convex losses.

The implicit constants may depend on r,R,G,L, but not on d,T,W_T or lambda. The logarithm is natural. The last rate is equivalently O((d/lambda)(1+log(1+dW_T))).
