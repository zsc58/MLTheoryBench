# Problem

## Setup

Let X be a measurable space with a measurable cost d:X x X -> [0,+infinity] satisfying d(x,x)=0. Let Theta be a parameter set and let L:X x Theta -> R satisfy that x -> L(x;theta) is measurable for every theta in Theta. Fix theta in Theta and a finite empirical sample x_1,...,x_N, where N>=1, with strictly positive weights mu_i satisfying sum_i mu_i=1. Write P_N=sum_i mu_i delta_{x_i} and Rhat(theta)=sum_i mu_i L(x_i;theta).

For probability laws Q on X, let Pi(Q,P_N) be the set of probability measures on the product measurable space X x X whose first marginal is Q and whose second marginal is P_N. For 1<=p<infinity define

W_p(Q,P_N)=inf_{pi in Pi(Q,P_N)} (integral d(y,x)^p dpi(y,x))^(1/p).

Define

W_infinity(Q,P_N)=inf_{pi in Pi(Q,P_N)} ess sup_{(y,x)~pi} d(y,x).

For a real-valued measurable function g, write g^+=max(g,0) and g^-=max(-g,0). The extended expectation integral g dQ is defined when at least one of integral g^+ dQ and integral g^- dQ is finite. For every finite epsilon>0 and 1<=p<=infinity, define

R_p(epsilon;theta)=sup{integral L(y;theta) dQ(y) : Q is a probability law on X, W_p(Q,P_N)<=epsilon, and integral L(y;theta) dQ(y) is defined as an extended expectation}.

For finite t>=0 define the individual and maximal loss-growth rates

Delta_i(t)=sup{L(y;theta)-L(x_i;theta) : d(y,x_i)<=t},

Delta_*(t)=max_i Delta_i(t).

For a function f:[0,infinity) -> [0,+infinity], let S_f be its least star-shaped majorant with respect to the origin and C_f its least concave majorant. Majorants have domain [0,infinity), may take the value +infinity, and dominate f at every argument. A nonnegative majorant h is star-shaped if h(lambda t)>=lambda h(t) for all finite t>=0 and 0<=lambda<=1. It is concave if h(lambda s+(1-lambda)t)>=lambda h(s)+(1-lambda)h(t) for all finite s,t>=0 and 0<=lambda<=1. Each least majorant is pointwise minimal among majorants of its respective shape. In these definitions use the extended-arithmetic convention 0 times infinity=0; infinity is an allowed function value, not an argument of f, S_f, or C_f.

For 1<=p<infinity set

f_i^p(u)=Delta_i(u^(1/p)),   f_*^p(u)=Delta_*(u^(1/p)),   0<=u<infinity,

lb_p(epsilon)=sum_i mu_i S_{f_i^p}(epsilon^p),

cc_p(epsilon)=C_{f_*^p}(epsilon^p).

For p=infinity set

lb_infinity(epsilon)=sum_i mu_i Delta_i(epsilon),

cc_infinity(epsilon)=sum_i mu_i lim_{t down epsilon} Delta_i(t),

where the limits are from strictly larger finite radii and exist in [0,+infinity].

## Task

Prove the following integrated theorem for every theta and every finite epsilon>0.

1. For every 1<=p<=infinity,

R_p(epsilon;theta)-Rhat(theta)>=lb_p(epsilon)

and

R_p(epsilon;theta)-Rhat(theta)<=cc_p(epsilon).

2. If 1<=p<=p2<=infinity, then

R_p(epsilon;theta)>=R_{p2}(epsilon;theta),

lb_1(epsilon)>=lb_p(epsilon)>=lb_{p2}(epsilon)>=lb_infinity(epsilon),

and

cc_1(epsilon)>=cc_p(epsilon)>=cc_{p2}(epsilon)>=cc_infinity(epsilon),

where endpoint quantities are interpreted as defined above.

3. For every finite p in [1,infinity), exactly one of the following alternatives holds: either lb_p(epsilon)=cc_p(epsilon)=R_p(epsilon;theta)-Rhat(theta)=+infinity for every finite epsilon>0, or all three quantities are finite for every finite epsilon>0.
