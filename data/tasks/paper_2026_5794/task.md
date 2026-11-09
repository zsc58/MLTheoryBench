# Problem

## Setup

Fix d>=1. Let T be a random element of the space of cadlag nondecreasing paths T:[0,1]->R_+ with T_0=0, independent of all Gaussian and endpoint randomness. Define the clock area

A(T)=integral_0^1 T_s ds,

and, conditional on T, let X_0 be centered Gaussian with covariance 2 A(T) I_d. For a fixed endpoint x_1 in R^d and t in [0,1), use the straight-line affine interpolation

X_t=t x_1+(1-t)X_0.

(Thus the conditional covariance is the area-clock covariance scaled by (1-t)^2.) A radial tail statement Theta(r^{-q}) is understood as r tending to infinity, with constants allowed to depend on d and the other fixed parameters.

## Task

Prove the following integrated claim for every t<1 and every endpoint x_1.

1. If T_s=s deterministically, then X_t is Gaussian with law N(t x_1,(1-t)^2 I_d).
2. Let alpha in (0,2), set rho=alpha/2, and let T be a stable subordinator satisfying
   E[exp(-s T_u)]=exp(-((rho+1)/2)u s^rho) for u in [0,1] and s>=0. Then X_t has a shifted isotropic symmetric alpha-stable law with location t x_1 and characteristic function
   exp(i t <xi,x_1>-(1-t)^alpha ||xi||^alpha/2),
   and P(||X_t-t x_1||>r)=Theta(r^{-alpha}).
3. Let nu>0 and let V_nu have the inverse-gamma density
   ((nu/2)^(nu/2)/Gamma(nu/2)) v^(-nu/2-1) exp(-nu/(2v)) on v>0. If T_s=s V_nu, then X_t has density
   Gamma((nu+d)/2)/(Gamma(nu/2)(nu pi)^((d)/2)(1-t)^d)
   times [1+||x-t x_1||^2/(nu(1-t)^2)]^(-(nu+d)/2),
   i.e. the d-dimensional Student-t law with nu degrees of freedom, location t x_1, and scale matrix (1-t)^2 I_d, and P(||X_t-t x_1||>r)=Theta(r^{-nu}).
