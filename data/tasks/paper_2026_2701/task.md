# Problem

## Setup

Fix sigma>0 and tau>=0. Let X_t in R^d solve the stationary isotropic diffusion
\[
dX_t=-\frac12X_t\,dt+sigma\,dW_t,
\]
where W_t is standard d-dimensional Brownian motion, so X_t has marginal law N(0,sigma^2 I_d). For j=1,...,N, take independent trajectory pairs (X_0^{(j)},X_tau^{(j)}). Thus E[X_tau^{(j)}X_0^{(j)T}]=alpha sigma^2 I_d with alpha=exp(-tau/2). Define
\[
\widehat C_{tau}=\frac1{2N}\sum_{j=1}^N\left(X_0^{(j)}X_{tau}^{(j)T}+X_{tau}^{(j)}X_0^{(j)T}\right).
\]
Let d,N->infinity with d/N->gamma in (0,infinity), keeping sigma and tau fixed, and write
\[
c_+=\frac{sigma^2(1+alpha)}2,\qquad c_- =\frac{sigma^2(1-alpha)}2.
\]
The empirical spectral distribution of a d-by-d real symmetric matrix is the probability measure assigning mass 1/d to each eigenvalue, counted with multiplicity.

Use the mean-one Marchenko-Pastur convention
\[
MP_{gamma}=\max(0,1-1/gamma)\,\delta_0+
\frac{\sqrt{(b-x)(x-a)}}{2\pi gamma x}\,\mathbf 1_{(a,b)}(x)\,dx,
\qquad a=(1-\sqrt{gamma})^2,\quad b=(1+\sqrt{gamma})^2.
\]
For a probability law nu, r nu denotes its pushforward under x->rx. The symbol boxplus denotes free additive convolution, the law of the sum of freely independent self-adjoint variables with the specified laws. For a probability law mu, use
\[
G_mu(z)=\int (z-x)^{-1}\,d\mu(x),\qquad \operatorname{Im}z>0.
\]

## Task

For tau>0, prove that the empirical spectral distribution of \(\widehat C_{tau}\) converges weakly almost surely to
\[
mu_{tau}=c_+\,MP_{gamma}\boxplus\bigl(-c_-\,MP_{gamma}\bigr).
\]
Show that its only possible atom is at zero, of mass max(0,1-2/gamma), and that the remaining measure is absolutely continuous. Denote its density, of total mass min(1,2/gamma), by rho_tau.

Show that the Stieltjes transform is the analytic branch G on the upper half-plane satisfying Im G(z)<0 and zG(z)->1 as z tends to infinity, of
\[
z c_+c_-gamma^2G^3+\bigl[c_+c_-gamma(2-gamma)-z(c_--c_+)gamma\bigr]G^2+\bigl[(c_--c_+)(gamma-1)-z\bigr]G+1=0.
\]
Recover the density almost everywhere through
\[
rho_tau(x)=-\frac1\pi\lim_{eta\downarrow0}\operatorname{Im}G(x+i eta).
\]
Characterize the boundaries of the support of the absolutely continuous part using the real roots of the quartic discriminant of this cubic, selecting the actual boundary roots according to the physical branch G. The isolated zero atom, when present, is not included in this continuous-support boundary assertion. Show that the upper edge lambda_+(tau) is the largest real continuous-support boundary root.

Finally, verify separately that at tau=0 the limiting law is sigma^2 MP_gamma with zero atom max(0,1-1/gamma). After taking the proportional limit, verify the weak limit of mu_tau as tau->infinity at fixed sigma and gamma, and the corresponding limit of lambda_+(tau), deriving a closed-form expression for its upper edge valid for every gamma>0.
