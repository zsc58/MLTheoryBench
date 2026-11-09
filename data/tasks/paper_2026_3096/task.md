# Problem

## Setup

Let n,m be positive integers, H=R^n, and Y=R^m. All norms on these spaces are Euclidean. Let mu be a probability measure on H such that

\[
\int_H e^{C_1\|x\|^2}\,\mu(dx)<\infty
\]

for some C_1>0.

For z=(x,y) in R^{n+m}, define

\[
q_f(z)=\frac{f(z)}{1+\|z\|^2},\qquad
\|f\|_w=\|q_f\|_\infty+\sum_{k=1}^{n+m}\|\partial_k q_f\|_\infty.
\]

The weighted C^1 space consists of functions for which q_f is continuously differentiable and this norm is finite. Let F be a convex, closed subset of this normed space, consisting of nonnegative real-valued functions, and let L belong to F. Assume

\[
\sup_{f\in\mathcal F}\|f\|_w<\infty.
\]

Assume there exist constants C_2^-,C_2^+>0 such that, for every eta>0, there exists delta(eta)>0 for which

\[
-C_2^- -\eta\|x\|^2+\delta(\eta)\|y\|^2
\le f(x,y)\le C_2^+(1+\|x\|^2+\|y\|^2)
\]

simultaneously for every f in F and every (x,y) in H times Y. These constants and delta(eta) do not depend on f,x,y.

For f in F, define

\[
Z_f(y)=\int_H e^{-f(x,y)}\,\mu(dx),\qquad
J_f=\int_Y Z_f(v)\,dv,
\]

\[
\mu_f^y(dx)=Z_f(y)^{-1}e^{-f(x,y)}\mu(dx),\qquad
\pi_f(dy)=J_f^{-1}Z_f(y)\,dy,
\]

\[
\lambda_f(dx,dy)=\pi_f(dy)\mu_f^y(dx).
\]

Here dy and dv denote Lebesgue measure on Y. Let the true joint observation law and its observation marginal be

\[
\lambda=\lambda_L,\qquad \pi=\pi_L.
\]

In particular the true conditional law is mu^y=mu_L^y. Define

\[
d_\Phi(f,g)=\int_{H\times Y}
\left|f(x,y)+\log Z_f(y)-g(x,y)-\log Z_g(y)\right|\,\lambda(dx,dy),
\]

\[
\Phi(f)=\int_{H\times Y}f\,d\lambda+\int_Y\log Z_f\,d\pi.
\]

Draw iid outer samples (X_i,Y_i) from lambda. Independently of all outer samples, draw an array of mutually independent inner samples X_{i,j} from mu. Let M:N->N be deterministic, positive integer valued, and satisfy M(N)->infinity. Set

\[
Z_f^M(Y_i)=\frac1M\sum_{j=1}^M e^{-f(X_{i,j},Y_i)},\qquad
\Lambda_N(f)=\frac1N\sum_{i=1}^N\log Z_f^{M(N)}(Y_i),
\]

\[
\Phi_N(f)=\frac1N\sum_{i=1}^N f(X_i,Y_i)+\Lambda_N(f).
\]

Let f_N^* be an F-valued measurable estimator from these samples, where F is equipped with the Borel sigma-field of uniform convergence on compact sets. Suppose there are measurable real random variables r_N such that, almost surely,

\[
\Phi_N(f_N^*)\le\inf_{f\in\mathcal F}\Phi_N(f)+r_N,
\qquad r_N\xrightarrow{P}0.
\]

Probability and convergence in probability are under the joint sampling law of the outer and inner samples.

## Task

Prove that, for every epsilon>0,

\[
\mathbb P\bigl(d_\Phi(f_N^*,L)>\varepsilon\bigr)\longrightarrow0
\qquad(N\to\infty).
\]
