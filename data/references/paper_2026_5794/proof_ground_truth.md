# Reference Proof

## Proof Structure

Conditioning on the clock and the endpoint gives a Gaussian affine transformation. The deterministic clock is then immediate. For the stable clock, express the area functional as a Stieltjes integral, compute its Laplace transform from independent increments, and substitute it into the Gaussian characteristic function. For the inverse-gamma clock, integrate the conditional Gaussian density against the inverse-gamma density to obtain the multivariate Student-t density. The stated radial tail orders follow from the standard tail laws for isotropic symmetric stable and Student-t distributions.

## Complete Proof

Fix a dimension d, an endpoint x_1 in R^d, and t<1. Write alpha_t=t and beta_t=1-t. Conditional on a realized clock T, let

X_0 | T ~ N(0, 2 A(T) I_d),  A(T)=integral from 0 to 1 of T_s ds,

and set X_t=t x_1+(1-t)X_0. The clock is independent of the Gaussian variable and of the endpoint. Since an affine image of a Gaussian vector is Gaussian,

X_t | (T, X_1=x_1) ~ N(t x_1, 2(1-t)^2 A(T) I_d).                                      (1)

For the deterministic clock T_s=s, A(T)=1/2. Thus (1) gives

X_t | (T, X_1=x_1) ~ N(t x_1,(1-t)^2 I_d).

Now let T be a stable subordinator of index rho=alpha/2 in (0,1), with Laplace transform

E[exp(-s T_t)] = exp(-((rho+1)/2)t s^rho),   s>=0.

Because T_0=0 and T is increasing, integration by parts for its Stieltjes measure gives

A(T)=integral_0^1 T_s ds = integral_[0,1] (1-s) dT_s.

Approximating the deterministic integrand by step functions and using independent increments, or equivalently the Laplace functional of a subordinator, yields, for lambda>=0,

E[exp(-lambda A(T))]
 = exp(- integral_0^1 ((rho+1)/2) [lambda(1-s)]^rho ds)
 = exp(-lambda^rho/2),

since the integral of (1-s)^rho over [0,1] is 1/(rho+1). From (1), conditional on x_1 and T the characteristic function is

exp(i t <xi,x_1> - (1-t)^2 A(T) ||xi||^2).

Averaging over T and applying the preceding Laplace transform with lambda=(1-t)^2||xi||^2 gives

E[exp(i<xi,X_t>) | X_1=x_1]
 = exp(i t <xi,x_1> - (1-t)^alpha ||xi||^alpha/2).                    (2)

This is the characteristic function of a shifted isotropic symmetric alpha-stable law, with location t x_1 and scale parameter 1-t under the convention in (2). Its standard radial tail asymptotic gives

P(||X_t-tx_1||>r | X_1=x_1)=Theta(r^{-alpha})

as r tends to infinity.

Finally let T_s=s V_nu, where V_nu has the inverse-gamma density

f(v)=((nu/2)^(nu/2)/Gamma(nu/2)) v^{-nu/2-1} exp(-nu/(2v)),   v>0,

for nu>0. Then A(T)=V_nu/2, so (1), with y=x-tx_1 and beta=1-t, has conditional density

(2 pi beta^2 v)^(-d/2) exp(-||y||^2/(2 beta^2 v))

given V_nu=v. Integrating against f(v) and using the gamma integral gives

f_{X_t|X_1=x_1}(x)
 = Gamma((nu+d)/2) /
   (Gamma(nu/2) (nu pi)^(d/2) beta^d)
   [1+ ||x-tx_1||^2/(nu beta^2)]^(-(nu+d)/2).

This is the d-dimensional Student-t density with nu degrees of freedom, location t x_1, and scale matrix beta^2 I_d. Its standard radial tail asymptotic is

P(||X_t-tx_1||>r | X_1=x_1)=Theta(r^{-nu}),

as r tends to infinity. These calculations prove all three cases of the integrated claim.
