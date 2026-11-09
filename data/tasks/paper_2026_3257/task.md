# Problem

## Setup

Let X and Y be nonempty compact convex subsets of R^{d_x} and R^{d_y}, respectively, with Euclidean projections Pi_X and Pi_Y. All vector norms are Euclidean and matrix norms are the induced operator norms. Let f:X x Y -> R^{d_x} and g:X x Y -> R^{d_y} be measurable mean fields. For every y in Y, assume that f(.,y) has a fixed point x^*(y) in X and satisfies

`||f(x,y)-f(x',y)|| <= mu ||x-x'||` for all x,x' in X,

with a fixed constant 0<=mu<1. This fixed point is unique. Assume that h(y)=g(x^*(y),y) maps Y into Y, is non-expansive on Y, and has a nonempty fixed-point set. Assume also that g is uniformly Lipschitz in its first argument on X, uniformly over y in Y.

The primitive stochastic oracles F and G return observations in R^{d_x} and R^{d_y}. At each call, the query is measurable with respect to the algorithmic history before that call, and the observation uses a fresh sample independent of that history. For every such history sigma-field H and H-measurable query (x,y) in X x Y, assume almost surely

`E[F(x,y)|H]=f(x,y)`, `E[G(x,y)|H]=g(x,y)`,

and, for q=2,4,

`E[||F(x,y)-f(x,y)||^q|H] <= sigma^q`,

`E[||G(x,y)-g(x,y)||^q|H] <= sigma^q`,

where sigma<infinity is fixed. Randomness in oracle calls is understood separately at each occurrence. All algorithmic quantities and initializations are adapted to their stated histories.

For the corrected scheme, additionally suppose f and g extend to an open convex neighborhood U of X x Y, are twice continuously differentiable in x there, and have x-Jacobians jointly continuous in (x,y). Assume fixed finite constants L_1,L_f,L_g^nabla such that, throughout U,

`||nabla_x f(x,y)|| <= mu`, `||nabla_x g(x,y)|| <= L_1`,

and, whenever (x,y),(x',y) belong to U,

`||nabla_x f(x,y)-nabla_x f(x',y)|| <= L_f||x-x'||`,

`||nabla_x g(x,y)-nabla_x g(x',y)|| <= L_g^nabla||x-x'||`.

Define

`A(y)=I-nabla_x f(x^*(y),y)`,

`C(y)=nabla_x g(x^*(y),y)`,

`P^*(y)=C(y)A(y)^(-1)`.

Assume A(y) is uniformly invertible and P^*(y) is uniformly bounded on Y. The corrected scheme has exact access to P^*(y) at each queried y through a separate structured oracle.

Define the mean queries

`H^raw(x,y)=g(x,y)`,

`H^corr(x,y)=g(x,y)+P^*(y)(f(x,y)-x)`.

## Algorithms

Fix an anchor u in Y and an initial outer point Y_0 in Y. For each integer horizon N>=1, fix b in (0,3/4) and set

`beta=N^(-b)`, `lambda=N^(-b/3)`.

These parameters remain constant during the N outer steps m=0,...,N-1. At step m, hold Y_m fixed and choose any X-valued inner initialization X_{m,0} measurable with respect to the history before the inner loop. Run n steps

`X_{m,t+1}=Pi_X[X_{m,t}+eta_t(F(X_{m,t},Y_m)-X_{m,t})]`, `t=0,...,n-1`,

where `eta_t=eta_0/(t+t_0)`, `eta_0>1/(1-mu)`, and the fixed positive t_0 is sufficiently large; in particular eta_t<=1 for all t>=0.

For the raw scheme, set `n=ceil(N^(4b/3))`. After the inner loop, obtain one fresh G observation and set

`H_m=G(X_{m,n},Y_m)`.

For the corrected scheme, set `n=ceil(N^(2b/3))`. After the inner loop, obtain one fresh G observation and one additional fresh F observation, using separate independent samples, and set

`H_m=G(X_{m,n},Y_m)+P^*(Y_m)(F(X_{m,n},Y_m)-X_{m,n})`.

The outer observations are fresh relative to the complete history including the just-completed inner loop. In either scheme, update

`Y_{m+1}=Pi_Y[Y_m+beta(H_m-Y_m+lambda(u-Y_m))]`.

Let T_N be the total number of primitive F and G calls used by these N outer steps, including every inner-loop call and every outer observation. The separate exact structured P^* evaluations are excluded from T_N.

## Task

Prove that, for every fixed b in (0,3/4), both schemes satisfy

`E||h(Y_N)-Y_N||^2 <= C_b N^(-2b/3)`

for all sufficiently large horizons N. The constants and horizon thresholds may depend on b, the fixed problem and oracle parameters, and the fixed inner stepsize parameters, but not on N; the bound should hold uniformly over admissible initializations.

Moreover, prove that `T_N=Theta(N^(1+4b/3))` for the raw scheme and `T_N=Theta(N^(1+2b/3))` for the corrected scheme.

Finally, show that for every fixed epsilon>0, a fixed b<3/4 sufficiently close to 3/4 can be chosen so that, for all sufficiently large horizons, the respective bounds are

`E||h(Y_N)-Y_N||^2 <= C_epsilon T_N^(-1/4+epsilon)` for the raw scheme,

`E||h(Y_N)-Y_N||^2 <= C_epsilon T_N^(-1/3+epsilon)` for the corrected scheme.

Thus the total-sample residual rates approach T_N^(-1/4+o(1)) and T_N^(-1/3+o(1)), respectively, in the fixed-positive-epsilon-loss sense just specified.
