# Reference Proof

## Proof Structure

For each order-statistic index, identify marginal coverage with the mean of the realized-coverage random variable. Compare this mean with the beta reference mean using the Wasserstein-1 mean bound and Wasserstein monotonicity. For lower-tail probabilities, couple the beta variable to the realized-coverage law by monotone transport, split according to whether transport displacement exceeds a tolerance, and control the exceptional event by Markov's inequality. The almost-sure displacement hypothesis removes the exceptional event.

## Complete Proof

Fix k and write D=D_{n,k}, nu=nu_{n,k}, and let B have law beta_{n,k}. By the tower property,
\[
\operatorname{Cov}(k)=\Pr(\widetilde T\le T_{(k)})=\mathbb E D=\int_0^1u\,\nu(du).
\]
The beta law is the law of the kth order statistic of n iid Uniform(0,1) variables, so its standard order-statistic moment is \(\mathbb EB=k/(n+1)\). Since u is 1-Lipschitz on [0,1], the Wasserstein-1 mean inequality gives
\[
\left|\operatorname{Cov}(k)-\frac{k}{n+1}\right|\le W_1(\nu,\beta_{n,k}).
\]
For p>=1, Wasserstein monotonicity gives \(W_1(\nu,\beta_{n,k})\le W_p(\nu,\beta_{n,k})\le\rho\).

Let \(T=F_\nu^{-1}\circ F_\beta\), with generalized inverses. Monotone one-dimensional transport gives \(T(B)\sim\nu\) and
\[
\mathbb E|T(B)-B|^p=W_p^p(\nu,\beta_{n,k})\le\rho^p.
\]
On \(\{|T(B)-B|\le\varepsilon\}\), the implication \(T(B)\le t\Rightarrow B\le t+\varepsilon\) holds. Therefore
\[
\Pr(D\le t)=\Pr(T(B)\le t)\le F_{\beta_{n,k}}(t+\varepsilon)+\Pr(|T(B)-B|>\varepsilon).
\]
Markov's inequality bounds the last probability by \((\rho/\varepsilon)^p\), proving the stated tail estimate. If \(|T(B)-B|\le\rho\) almost surely, the implication holds everywhere with epsilon=rho, giving \(\Pr(D\le t)\le F_{\beta_{n,k}}(t+\rho)\).

Finally, for \(k_\gamma=\lceil(n+1)\gamma\rceil\le n\), \(0\le k_\gamma/(n+1)-\gamma<1/(n+1)\). The triangle inequality and the coverage bound imply \(|\operatorname{Cov}(k_\gamma)-\gamma|\le\rho+1/(n+1)\).
