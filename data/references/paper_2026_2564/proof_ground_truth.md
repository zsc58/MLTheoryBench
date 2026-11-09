# Reference Proof

## Proof Structure

1. Establish the unique entropic optimizer's normalized continuous Schrödinger potentials and Gibbs factorization on the compact supports.
2. Transfer uniform density through the injective feature map and remove the additive gauge by centering, obtaining centered approximants to the normalized target potential.
3. Use sup-norm stability of the soft transform to show semidual values converge to the entropic optimum.
4. Apply the Gibbs-plan gap identity and Pinsker's inequality to obtain reverse KL and total-variation convergence; total variation implies weak convergence.

## Complete Proof

Let
\[
Z_h(x)=\int_{K_\nu}\exp\!\big((h(y)-c(x,y))/\epsilon\big)\,d\nu(y),\qquad
(Th)(x)=-\epsilon\log Z_h(x),
\]
and, for bounded continuous \(h\), let
\[
J(h)=\int h\,d\nu+\int Th\,d\mu.
\]
The supports are nonempty and compact, so \(c\) is bounded and uniformly continuous on \(K_\mu\times K_\nu\). We invoke the standard bounded-cost entropic OT duality result: for probability marginals and a bounded measurable cost, the entropy-regularized coupling problem at \(\epsilon>0\) has a unique minimizer; its dual is attained by potentials satisfying the soft-transform equations almost surely, and the minimizer has density \(\exp((f(x)+g(y)-c(x,y))/\epsilon)\) relative to the product of its marginals. Its dual value equals the primal value. The stated assumptions hold here because \(\mu,\nu\) are probabilities, \(\epsilon>0\), and \(c\) is bounded on their supports. Thus there are potentials \((f^\star,g^\star)\) and a unique optimizer \(\pi^\star\) with
\[
\frac{d\pi^\star}{d(\mu\otimes\nu)}(x,y)=
\exp\!\left(\frac{f^\star(x)+g^\star(y)-c(x,y)}{\epsilon}\right).
\]

Choose pointwise representatives via the soft-transform equations. To check their regularity, for any two target points \(y,y'\), comparison inside the transform defining \(g^\star\) gives
\[
|g^\star(y)-g^\star(y')|
\leq \sup_{x\in K_\mu}|c(x,y)-c(x,y')|.
\]
Consequently \(g^\star\) is uniformly continuous on \(K_\nu\). It is finite there: the target soft-transform normalizer at one point is finite and positive by the dual equations, and bounded differences in \(c\) compare that normalizer with those at every other target point. Compactness then makes \(g^\star\) bounded. The analogous argument applies to \(f^\star\). The transform equations therefore hold for bounded continuous representatives on the supports. Adjust their additive gauge so that \(\int g^\star d\nu=0\); then \(f^\star=Tg^\star\). Normalization of the Gibbs density gives
\(J(g^\star)=\int f^\star d\mu+\int g^\star d\nu=\mathrm{OT}_\epsilon(\mu,\nu)\).

Since \(\phi:K_\nu\to\mathbb R^n\) is continuous and injective, compactness makes it a homeomorphism onto the compact image \(\phi(K_\nu)\). For any \(q\in C(K_\nu)\), the function \(q\circ\phi^{-1}\) is continuous on that image. The image is closed in \(\mathbb R^n\), so the continuous function extends to \(\mathbb R^n\) by the standard continuous-extension theorem for closed subsets of a normal space. The assumed density of \(\mathcal F\) then uniformly approximates the extension on \(\phi(K_\nu)\). Hence \(\phi^*\mathcal F\) is uniformly dense in \(C(K_\nu)\). Choose \(u_m=a_m\circ\phi\) with \(\|u_m-g^\star\|_\infty\to0\), and center them:
\[
 g_m=u_m-\int u_m\,d\nu\in\mathcal C_\nu(\phi^*\mathcal F).
\]
As \(\int g^\star d\nu=0\), \(\|g_m-g^\star\|_\infty\le 2\|u_m-g^\star\|_\infty\to0\).

For any bounded \(h,k\), pointwise comparison of the integrands gives
\(e^{-\|h-k\|_\infty/\epsilon}Z_k\le Z_h\le e^{\|h-k\|_\infty/\epsilon}Z_k\), hence
\[
\|Th-Tk\|_{\infty,K_\mu}\le \|h-k\|_{\infty,K_\nu}.
\]
Therefore \(Tg_m\to Tg^\star=f^\star\) uniformly, and
\[
|J(g_m)-J(g^\star)|
\le \|g_m-g^\star\|_\infty+\|Tg_m-Tg^\star\|_\infty\to0.
\]
Thus the semidual gaps \(\Delta_m=\mathrm{OT}_\epsilon-J(g_m)\) tend to zero.

For each \(m\), define
\[
\frac{d\pi_m}{d(\mu\otimes\nu)}(x,y)=
\exp\!\left(\frac{Tg_m(x)+g_m(y)-c(x,y)}{\epsilon}\right).
\]
The definition of \(T\) implies that integrating this density in \(y\) gives 1 for every \(x\), so \(\pi_m\) is a probability with first marginal \(\mu\). Comparing the two positive Gibbs densities and integrating their log ratio with respect to \(\pi^\star\), using its marginals \(\mu,\nu\) and \(f^\star=Tg^\star\), yields
\[
\epsilon\,\mathrm{KL}(\pi^\star\Vert\pi_m)
=J(g^\star)-J(g_m)=\Delta_m.
\]
Thus \(\mathrm{KL}(\pi^\star\Vert\pi_m)\to0\). With probabilistic total variation \(\|P-Q\|_{\mathrm{TV}}=\sup_A|P(A)-Q(A)|\), Pinsker's inequality gives
\[
\|\pi_m-\pi^\star\|_{\mathrm{TV}}
\le \sqrt{\mathrm{KL}(\pi^\star\Vert\pi_m)/2}
=\sqrt{\Delta_m/(2\epsilon)}\to0.
\]
Finally, total-variation convergence implies convergence against every bounded continuous test function on \(K_\mu\times K_\nu\), hence \(\pi_m\Rightarrow\pi^\star\).
