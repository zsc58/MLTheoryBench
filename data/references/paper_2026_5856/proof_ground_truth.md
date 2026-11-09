# Reference Proof

## Theorem-critical obligations

The proof must close the following obligations: (1) well-defined operators and ridge normal equations; (2) the well-specified population approximation bound; (3) Hilbert-valued concentration for bounded state observables under the stated total variation convention; (4) conditional moment concentration for transition residuals; (5) a common high-probability event controlling both empirical quantities; (6) the conditional ridge perturbation estimate and its threshold; and (7) the exact constants, final probability, and regularization specialization. All seven are closed below. Only the two explicitly stated, standard independent Hilbert-martingale inequalities are used as external concentration results.

## 1. Operators and approximation error

All expectations below use the law of the given chain with its arbitrary initial distribution. Jensen's inequality and the second-moment assumption give |f_star(x)|<=R for every x. Invariance also gives int x^2 pi(dx)<=R^2. Bounded measurable features into a separable Hilbert space imply that Phi f_star and Phi tensor Phi are Bochner integrable, the latter in the separable Hilbert space of Hilbert-Schmidt operators. The empirical quantities are measurable and finite almost surely; no moment assumption on X_0 is required, since the response variables are X_1,...,X_T and features are bounded.

Use the notation of the task and write
\[
\Sigma_\lambda=\Sigma+\lambda I,\qquad
\widehat\Sigma_\lambda=\widehat\Sigma+\lambda I,\qquad
w_\lambda=\Sigma_\lambda^{-1}h,\qquad
f_\lambda(x)=\langle w_\lambda,\Phi(x)\rangle.
\]
Both covariance operators are bounded, positive, and self-adjoint, so their regularized inverses exist for every lambda>0. The normal equations are
\[
\Sigma_\lambda w_\lambda=h,\qquad
\widehat\Sigma_\lambda\widehat w_\lambda=\widehat h.
\]
For any v,w in H,
\[
\mathcal E(\langle v,\Phi\rangle,\langle w,\Phi\rangle)
=\langle v-w,\Sigma(v-w)\rangle
=\|\Sigma^{1/2}(v-w)\|^2.
\]
Well specification gives h=Sigma w_star. Thus
\[
w_\lambda=\Sigma_\lambda^{-1}\Sigma w_\star,
\qquad \|w_\lambda\|\le\|w_\star\|,
\qquad w_\lambda-w_\star=-\lambda\Sigma_\lambda^{-1}w_\star.
\]
Spectral calculus, using s/(s+lambda)^2<=1/lambda for s>=0, yields
\[
\mathcal E(f_\lambda,f_\star)
=\lambda^2\|\Sigma^{1/2}\Sigma_\lambda^{-1}w_\star\|^2
\le\lambda\|w_\star\|^2.\tag{1}
\]
These arguments allow singular Sigma, zero features, zero w_star, and nonunique well-specified representations.

## 2. Standard independent martingale inequalities

The source quotes the following two Hilbert-valued inequalities from Pinelis. They concern arbitrary martingale differences, not Markov-chain learning or the paper-specific estimator.

Let d_j, j=1,...,T, be differences in a real separable Hilbert space, adapted to a filtration G_0,...,G_T, with E[d_j|G_{j-1}]=0.

* If ||d_j||<=b_j almost surely for deterministic b_j>=0 and B^2=sum_j b_j^2>0, then
\[
\mathbb P\left\{\left\|\sum_{j=1}^T d_j\right\|\ge r\right\}
\le2\exp\left(-\frac{r^2}{2B^2}\right),\qquad r>0.
\]
If B=0, all differences vanish almost surely.
* If, for deterministic v,L>0 and every integer m>=2,
\[
\mathbb E[\|d_j\|^m\mid G_{j-1}]
\le\frac{m!}{2}v^2L^{m-2},
\]
then, for eta in (0,1), with probability at least 1-eta,
\[
\left\|\frac1T\sum_{j=1}^T d_j\right\|
\le v\sqrt{\frac{2\log(2/\eta)}T}
 +\frac{L\log(2/\eta)}T.
\]

The bounded-increment statement is quoted in the source at L001400-L001403; the moment statement is at L001413-L001417. Their applications, including filtrations and hypotheses, are verified next.

## 3. Derivation of bounded-state concentration

Let K be a real separable Hilbert space and u:R->K be bounded and measurable with pi u=0. Write ||u||_infinity=sup_x ||u(x)||. The total variation convention in the task and Hilbert-space duality imply, for every integer k>=0,
\[
\|P^ku(x)\|
=\left\|\int u\,d(P^k(x,\cdot)-\pi)\right\|
\le C\rho^k\|u\|_\infty.
\]
Indeed, test this integral against each unit vector in K and apply the scalar bounded-function dual norm. Therefore
\[
g=\sum_{k=0}^\infty P^ku
\]
converges uniformly to a bounded measurable function, with
\[
G:=\|g\|_\infty\le\frac{C\|u\|_\infty}{1-\rho}.
\]
The Markov operator is a contraction in the supremum norm. Telescoping finite sums and passing to the uniform limit give g-Pg=u.

Let F_t=sigma(X_0,...,X_t). For j=1,...,T, put
\[
d_j=g(X_j)-Pg(X_{j-1}).
\]
These variables are F_j-measurable, satisfy E[d_j|F_{j-1}]=0 by the Markov property, and obey ||d_j||<=2G. Direct telescoping gives
\[
\sum_{t=0}^{T-1}u(X_t)
=\sum_{j=1}^T d_j+g(X_0)-g(X_T).
\]
The endpoint norm is at most 2G. Applying the bounded-increment inequality with b_j=2G, and treating G=0 directly, gives with probability at least 1-eta,
\[
\left\|\frac1T\sum_{t=0}^{T-1}u(X_t)\right\|
\le\frac{2C\|u\|_\infty}{1-\rho}
\left(\sqrt{\frac{2\log(2/\eta)}T}+\frac1T\right).\tag{2}
\]
This establishes the needed Markov concentration result rather than assuming it. It is valid for every initial law.

## 4. Explicit trajectory deviations

Fix delta in (0,1), and put
\[
q=\log(6/\delta),\qquad s=\sqrt{2q/T},\qquad b=1/T.
\]
For t=0,...,T-1, define
\[
r_{t+1}=\Phi(X_t)(X_{t+1}-f_\star(X_t)).
\]
It is F_{t+1}-measurable, and the Markov property gives
\[
\mathbb E[r_{t+1}\mid F_t]=0,
\qquad
\mathbb E[\|r_{t+1}\|^m\mid F_t]
\le\frac{m!}{2}(\kappa\sigma)^2(\kappa M)^{m-2}.
\]
Thus the moment inequality, with v=kappa sigma, L=kappa M and eta=delta/3, gives
\[
\left\|\frac1T\sum_{t=0}^{T-1}r_{t+1}\right\|
\le\kappa\sigma s+\frac{\kappa Mq}{T}
\le\kappa\sigma s+\frac{2\kappa Mq}{T} \tag{3}
\]
with failure probability at most delta/3. The final enlargement matches the source's constants.

The observable
\[
u_h(x)=\Phi(x)f_\star(x)-h
\]
is pi-centered and has supremum norm at most 2 kappa R. Applying (2) with eta=delta/3 gives
\[
\left\|\frac1T\sum_{t=0}^{T-1}u_h(X_t)\right\|
\le\frac{4C\kappa R}{1-\rho}(s+b) \tag{4}
\]
with failure probability at most delta/3.

In the real separable Hilbert space of Hilbert-Schmidt operators, define
\[
u_\Sigma(x)=\Phi(x)\otimes\Phi(x)-\Sigma.
\]
The rank-one map is measurable, ||Phi(x) tensor Phi(x)||_HS=||Phi(x)||^2<=kappa^2, and ||Sigma||_HS<=kappa^2. Hence pi u_Sigma=0 and ||u_Sigma||_infinity<=2 kappa^2. A further application of (2) gives
\[
\|\widehat\Sigma-\Sigma\|_{\rm op}
\le\|\widehat\Sigma-\Sigma\|_{\rm HS}
\le\frac{4C\kappa^2}{1-\rho}(s+b) \tag{5}
\]
with failure probability at most delta/3.

The three events have a common intersection of probability at least 1-delta; independence is not needed. On this intersection, the identity
\[
\widehat h-h
=\frac1T\sum_{t=0}^{T-1}r_{t+1}
 +\frac1T\sum_{t=0}^{T-1}u_h(X_t)
\]
gives
\[
\|\widehat h-h\|
\le\frac{4C\kappa R}{1-\rho}(s+b)
 +\frac{2\kappa Mq}{T}+\kappa\sigma s.\tag{6}
\]

## 5. Conditional ridge perturbation and constants

Work on that common event and fix lambda>=Lambda_{T,delta}. By (5),
\[
\|\widehat\Sigma-\Sigma\|_{\rm op}\le\lambda/2.
\]
Set A=(hatSigma-Sigma)Sigma_lambda^{-1}. Then ||A||<=1/2 and
\[
\widehat\Sigma_\lambda=(I+A)\Sigma_\lambda,
\qquad
\widehat\Sigma_\lambda^{-1}=\Sigma_\lambda^{-1}(I+A)^{-1}.
\]
The Neumann series bounds ||(I+A)^{-1}|| by 2. Spectral calculus gives the sharper scalar bound
\[
\|\Sigma^{1/2}\Sigma_\lambda^{-1}\|
\le\sup_{z\ge0}\frac{\sqrt z}{z+\lambda}
=\frac1{2\sqrt\lambda}.
\]
Consequently
\[
\|\Sigma^{1/2}\widehat\Sigma_\lambda^{-1}\|\le\lambda^{-1/2}.
\]
Subtracting the normal equations gives
\[
\widehat w_\lambda-w_\lambda
=\widehat\Sigma_\lambda^{-1}
\big[(\widehat h-h)+(\Sigma-\widehat\Sigma)w_\lambda\big].
\]
Together with ||w_lambda||<=||w_star||, this proves, under the verified covariance condition,
\[
\sqrt{\mathcal E(\widehat f_\lambda,f_\lambda)}
\le\lambda^{-1/2}
\big(\|\widehat h-h\|+
\|\widehat\Sigma-\Sigma\|_{\rm op}\|w_\star\|\big).
\]
Put
\[
K=\frac{4C\kappa(R+\kappa\|w_\star\|)}{1-\rho}.
\]
Equations (5)-(6) yield
\[
\sqrt{\mathcal E(\widehat f_\lambda,f_\lambda)}
\le\lambda^{-1/2}\left[K(s+b)+\frac{2\kappa Mq}{T}+\kappa\sigma s\right].
\]
Using (a+c+d)^2<=3(a^2+c^2+d^2) and (s+b)^2<=2(s^2+b^2), we obtain
\[
\begin{aligned}
\mathcal E(\widehat f_\lambda,f_\lambda)
&\le\frac{6K^2}{\lambda}(s^2+b^2)
 +\frac{12\kappa^2M^2q^2}{\lambda T^2}
 +\frac{3\kappa^2\sigma^2s^2}{\lambda}\\
&=\frac{C^2D_4}{(1-\rho)^2}
 \left(\frac{2q}{\lambda T}+\frac1{\lambda T^2}\right)
 +\frac{D_2q^2}{\lambda T^2}
 +\frac{D_3q}{\lambda T}.\tag{7}
\end{aligned}
\]
Here 6K^2=C^2D4/(1-rho)^2, D2=12 kappa^2 M^2, and D3=6 kappa^2 sigma^2, exactly as required.

## 6. Final bound and specialization

The squared triangle inequality gives
\[
\mathcal E(\widehat f_\lambda,f_\star)
\le2\mathcal E(\widehat f_\lambda,f_\lambda)
 +2\mathcal E(f_\lambda,f_\star).
\]
Combining (1) and (7) proves the target inequality on an event of probability at least 1-delta. The public assertion is for each fixed lambda; no simultaneous-in-T assertion is needed.

For fixed delta, choose a positive gamma independent of T that satisfies the prescribed threshold for all positive integer T. Such a choice exists, since it suffices that
\[
\gamma\ge\frac{8C\kappa^2}{1-\rho}\left(\sqrt{2q}+1\right).
\]
Substituting lambda_T=gamma T^{-1/2} gives
\[
\begin{aligned}
\mathcal E(\widehat f_{\lambda_T},f_\star)
\le{}&\frac{2C^2D_4}{(1-\rho)^2}
 \left(\frac{2q}{\gamma\sqrt T}+\frac1{\gamma T^{3/2}}\right)
 +\frac{2D_2q^2}{\gamma T^{3/2}}\\
&+\frac{2D_3q}{\gamma\sqrt T}
 +\frac{2\gamma\|w_\star\|^2}{\sqrt T}.
\end{aligned}
\]
For each T this holds with probability at least 1-delta. With delta, gamma, and the model constants fixed, it is O(T^{-1/2}); the logarithmic factors and both T^{-3/2} contributions remain explicit. No unresolved proof obligation remains.
