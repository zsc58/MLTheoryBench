# Problem

## Setup

Let d be a positive integer, let the feature space be R^d with its Euclidean norm and Borel sigma-algebra, and let the label set C be finite and nonempty. Let (Y_i,C_i)_{i=1}^n be independent copies of a pair (Y,C), and write P_Y for the marginal distribution of Y.

Fix a version of the conditional distribution of C given Y, defined on R^d, and write p_c(y)=P(C=c | Y=y) for its probability of class c. Assume that, for a known finite constant L>=0, every p_c satisfies

|p_c(y)-p_c(y')| <= L ||y-y'||   for all y,y' in R^d.

Fix constants 0<c_k<infinity and 0<lambda<infinity and a Borel-measurable function K:[0,infinity)->[0,c_k] such that K(r)=0 for r>1. These choices are deterministic, not selected using the training sample. Define

K_lambda(y,y') = c_k^{-1} K(||y-y'||/lambda),

kappa_n(y) = sum_{i=1}^n K_lambda(y,Y_i).

Whenever kappa_n(y)>0, define

hat p_c(y) = [sum_{i=1}^n K_lambda(y,Y_i) 1_{C_i=c}]/kappa_n(y).

A real random variable X is called sigma-sub-Gaussian here if

E[exp(tX)] <= exp(sigma^2 t^2/2)   for every t in R.

Let 0<=sigma<infinity be a fixed common scale such that, for every class c and P_Y-almost every x, the centered variable p_c(x)-B with B distributed as Bernoulli(p_c(x)) is sigma-sub-Gaussian.

For 0<delta<1 and kappa_n(y)>0, define

alpha_n(y,delta) = sqrt(kappa_n(y) log(delta^{-1} sqrt(1+kappa_n(y))))   if kappa_n(y)>1,

alpha_n(y,delta) = sqrt(log(sqrt(2)/delta))   if 0<kappa_n(y)<=1,

where log denotes the natural logarithm.

## Task

For every fixed integer n>=1, query y in R^d, class c in C, and confidence parameter 0<delta<1, prove that there is an event E of probability at least 1-delta under the joint distribution of the training sample such that, for every sample in E with kappa_n(y)>0,

|p_c(y)-hat p_c(y)| <= L lambda + 2 sigma alpha_n(y,delta)/kappa_n(y).
