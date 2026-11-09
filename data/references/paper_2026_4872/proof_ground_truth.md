# Reference Proof

## Ambient Contract and Obligations

The task concerns population KL objectives for overlapping, strictly positive Gaussian densities on R^d. The covariance is shared and fixed, target means are distinct, and alpha lies in (0,1). Forward weight optimization includes beta=0 and beta=1, whereas logit dynamics and reverse-KL parameter derivatives use interior beta. Learner means are unrestricted. In particular, m_n=mu_o is allowed. There is no empirical sampling experiment or finite-batch assertion. The disjoint-support illustration is not an assumption of this chain.

The theorem-critical obligations are:

1. **step_001:** Finite forward loss, endpoint continuity, strict positivity away from zero, and strict increase on the entire closed weight interval.
2. **step_002:** The logit responsibility identity and global, strictly decreasing forward-KL flow converging to zero old weight.
3. **step_003:** The responsibility leakage bound, including its exact weight prefactor and Gaussian exponent.
4. **step_004:** Valid reverse-KL differentiation, the two parameter-gradient formulas, and stationarity and global minimality at target matching.
5. **step_005:** Valid old-mean differentiation and Gaussian integration by parts, the exact responsibility decomposition, both explicit leakage estimates, the operator-norm bound, and its correctly qualified separation interpretation.

All five obligations are derived below. The Gaussian Stein identity indexed by theory_022 is standard independent background; its relevant statement and application hypotheses are also checked explicitly.

## step_001: Forward-KL Positivity and Monotonicity

Write \(A=\Sigma^{-1}\), \(D=\|\mu_o-\mu_n\|_A>0\), and \(X(x)=p_o(x)/p_n(x)\). Then
\[
L_F(\beta)=\mathbb E_{p_n}\big[-\log(1-\beta+\beta X)\big],\qquad \mathbb E_{p_n}X=1.
\]
The logarithm of X is
\[
\log X(x)=(\mu_o-\mu_n)^\top A\left(x-\frac{\mu_o+\mu_n}{2}\right).
\]
Under p_n this is a nonconstant Gaussian random variable of mean \(-D^2/2\) and variance \(D^2\). Completing the square in its exponential integral gives \(\mathbb E_{p_n}X^t=\exp((t^2-t)D^2/2)\) for every real t. In particular, all moments needed below are finite.

For every beta in [0,1], the number \(1-\beta+\beta X\) lies between 1 and X. Therefore
\[
|\log(1-\beta+\beta X)|\le|\log X|.
\]
This integrable envelope proves finiteness and continuity of L_F on [0,1], including both endpoints. Strict Jensen gives \(L_F(0)=0\) and \(L_F(\beta)>0\) for every beta>0, since X is nonconstant. Hence zero is the unique minimizer.

Differentiation gives
\[
L_F'(\beta)=\mathbb E_{p_n}\frac{1-X}{1-\beta+\beta X},\qquad
L_F''(\beta)=\mathbb E_{p_n}\frac{(1-X)^2}{(1-\beta+\beta X)^2}>0
\]
for 0<beta<1. On compact interior weight intervals the derivative integrands have bounded envelopes. Near beta=0, they are bounded by constant multiples of \(1+X\) and \((1+X)^2\), respectively. Thus the right derivative at zero is \(L_F'(0)=\mathbb E(1-X)=0\), and \(L_F'(\beta)>0\) throughout (0,1). Continuity at the endpoints extends strict increase to [0,1]. For example, comparison with any intermediate interior weight makes the comparison with beta=1 strict.

## step_002: Responsibility Identity and Global Flow

For beta=sigma(phi), direct differentiation yields
\[
\partial_\phi\log q_\beta
=\frac{\beta(1-\beta)(p_o-p_n)}{q_\beta}
=\frac{\beta p_o}{q_\beta}-\beta=r_o-\beta.
\]
Consequently, defining \(F(\phi)=\partial_\phi L_F(\sigma(\phi))\),
\[
F(\phi)=\beta-\mathbb E_{p_n}r_o
=\beta(1-\beta)L_F'(\beta)>0.
\]
The expectation differentiation is valid because the log-density derivative is bounded. The responsibility is a smooth sigmoid of phi plus log X; its phi derivative is \(r_o(1-r_o)\), bounded by 1/4. Hence F is continuous and locally smooth. Since both beta and r_o lie in (0,1), positivity also gives \(0<F(\phi)<1\).

For a finite initial value phi_0, define, for a<=phi_0,
\[
T(a)=\int_a^{\phi_0}\frac{du}{F(u)}.
\]
This is continuous and strictly decreasing as a increases, with T(phi_0)=0 and \(T(a)\ge\phi_0-a\to\infty\) as a tends to minus infinity. Its inverse defines a solution phi(t) for every t>=0, and differentiation of T(phi(t))=t gives \(\dot\phi=-F(\phi)\). Any solution with that initial condition satisfies the same integral relation, so this solution is unique. It decreases strictly and tends to minus infinity; therefore beta(t)=sigma(phi(t)) decreases strictly to zero. This also explicitly rules out finite-time escape.

## step_003: Leakage and Gaussian Overlap

For positive densities f,g and 0<w<1, put \(h=wf+(1-w)g\) and \(r_f=wf/h\). Define the Bhattacharyya coefficient by
\[
\operatorname{BC}(f,g)=\int\sqrt{fg}\,dx.
\]
The arithmetic-geometric mean inequality gives
\[
h\ge2\sqrt{w(1-w)fg}.
\]
It follows directly that
\[
\mathbb E_g r_f
=\int\frac{wfg}{h}\,dx
\le\frac12\sqrt{\frac{w}{1-w}}\operatorname{BC}(f,g),
\]
and
\[
\mathbb E_f(1-r_f)
=\int\frac{(1-w)fg}{h}\,dx
\le\frac12\sqrt{\frac{1-w}{w}}\operatorname{BC}(f,g).
\]
Thus the internal support result is proved rather than merely invoked.

For Gaussian densities with means a,b and common covariance Sigma, expansion of the quadratic forms gives
\[
\sqrt{\varphi_\Sigma(x;a)\varphi_\Sigma(x;b)}
=\varphi_\Sigma\left(x;\frac{a+b}{2}\right)
\exp\left(-\frac{\|a-b\|_A^2}{8}\right).
\]
Integration proves \(\operatorname{BC}=\exp(-\|a-b\|_A^2/8)\). Taking f=p_o, g=p_n and w=beta proves the requested forward responsibility estimate.

## step_004: Reverse-KL Gradients and Matching

We first justify the analytic operations throughout the full learner parameter domain. On a compact neighborhood of any interior weight and finite pair of learner means, weights are bounded away from zero and one and means remain bounded. Writing a Gaussian density as
\[
C_\Sigma e^{-x^\top Ax/2}e^{x^\top Aa-a^\top Aa/2}
\]
shows that the common quadratic factor cancels in log(q/p_alpha). The remaining logarithms of finite sums of exponentials of affine functions satisfy
\[
|\log(q/p_\alpha)|\le C(1+\|x\|)
\]
uniformly on that parameter neighborhood. Gaussian densities and their first parameter derivatives are bounded there by polynomial multiples of \(e^{-c\|x\|^2}\), for finite C and c>0. These facts provide integrable envelopes for the loss integrand and its first parameter derivatives. They justify differentiation and continuity of the resulting derivatives by dominated convergence. No global restriction on the learner means is imposed by this local argument.

For any of the learner parameters theta, normalization gives
\[
\partial_\theta L_R
=\int(\partial_\theta q)\big(\log(q/p_\alpha)+1\big)\,dx
=\int(\partial_\theta q)\log(q/p_\alpha)\,dx,
\]
because \(\int\partial_\theta q=\partial_\theta1=0\). Now
\[
\partial_\beta q=q_o-q_n,\qquad
\nabla_{m_n}q=(1-\beta)q_nA(x-m_n).
\]
Substitution proves the two required gradient formulas, including when the old learner mean is arbitrary.

At (beta,m_o,m_n)=(alpha,mu_o,mu_n), q=p_alpha pointwise, so the logarithmic factor and both displayed gradients vanish, and L_R=0. Nonnegativity follows, for example, from Jensen applied to \(-\log(p_\alpha/q)\) under q, whose density-ratio expectation is one. Thus the matching point is a global minimizer over the full stated learner domain. This asserts neither uniqueness of the full parameter minimizer nor global convergence of reverse-KL gradient flow.

## step_005: Old-Mean Decomposition and Drift Control

Differentiate with respect to m_o in the full family and then evaluate at m_o=mu_o. The normalization identity just proved yields
\[
\nabla_{m_o}L_R(\beta,\mu_o,m_n)
=\beta\,\mathbb E_{p_o}\left[A(Y-\mu_o)g(Y)\right],
\qquad g(x)=\log\frac{q_{\beta,\mu_o,m_n}(x)}{p_\alpha(x)}.
\]
The relevant Gaussian Stein identity is
\[
\mathbb E[A(Y-\mu_o)g(Y)]=\mathbb E[\nabla g(Y)]
\]
for a continuously differentiable g with the requisite integrability, when Y has density p_o. Here g is smooth and has at most linear growth by the preceding Gaussian calculation. Direct spatial differentiation of a mixture gives
\[
\nabla_x\log q=-A\big[x-r_o\mu_o-(1-r_o)m_n\big],
\qquad
\nabla_x\log p_\alpha=-A\big[x-s_o\mu_o-(1-s_o)\mu_n\big].
\]
Their difference is bounded in x, since all responsibilities lie in [0,1] and all means in this calculation are fixed. Thus \(\mathbb E_{p_o}\|\nabla g\|<\infty\), and \(\mathbb E_{p_o}\|A(Y-\mu_o)g(Y)\|<\infty\) follows from Gaussian second moments. These verify the identity's hypotheses. Equivalently, the identity follows here by integrating \(\nabla(p_og)\): \(\nabla p_o=-A(x-\mu_o)p_o\), and its boundary term vanishes because a Gaussian tail dominates the linear growth of g and the surface-area factor. This supplies a direct derivation for the application.

Subtracting the two mixture scores yields
\[
\nabla g(x)=A\big[(1-r_o(x))(m_n-\mu_o)-(1-s_o(x))(\mu_n-\mu_o)\big].
\]
Stein's identity and expectation under p_o therefore give
\[
\nabla_{m_o}L_R(\beta,\mu_o,m_n)
=\beta A\big[\varepsilon_q(m_n-\mu_o)-\varepsilon_p(\mu_n-\mu_o)\big].
\]
The Euclidean triangle inequality and definition of the induced operator norm give
\[
\|\nabla_{m_o}L_R\|
\le\beta\|A\|_{op}\big[\varepsilon_q\|m_n-\mu_o\|+\varepsilon_p\|\mu_n-\mu_o\|\big].
\]

Apply the second leakage inequality from step_003 first with f=p_o, g=N(m_n,Sigma), w=beta, and then with f=p_o, g=p_n, w=alpha. The Gaussian overlap calculation gives explicitly
\[
\varepsilon_q\le\frac12\sqrt{\frac{1-\beta}{\beta}}
 e^{-\|m_n-\mu_o\|_A^2/8},\qquad
\varepsilon_p\le\frac12\sqrt{\frac{1-\alpha}{\alpha}}
 e^{-\|\mu_n-\mu_o\|_A^2/8}.
\]
These inequalities hold for all admissible means and interior weights, even when a right-hand side exceeds one. No lower bound on either separation was used.

For completeness, let \(D_q=\|m_n-\mu_o\|_A\) and \(D_p=\|\mu_n-\mu_o\|_A\). Since \(\|v\|\le\sqrt{\lambda_{\max}(\Sigma)}\|v\|_A\), the drift upper bound is at most
\[
\frac{\beta\|A\|_{op}\sqrt{\lambda_{\max}(\Sigma)}}2
\left[\sqrt{\frac{1-\beta}{\beta}}D_qe^{-D_q^2/8}
+\sqrt{\frac{1-\alpha}{\alpha}}D_pe^{-D_p^2/8}\right].
\]
With d,Sigma,alpha,beta fixed, this tends to zero when D_q and D_p both tend to infinity. The leakage estimates are exponential in their respective squared separations, with the displayed weight dependence; they are not uniform over weights approaching zero. If m_n=mu_o, then r_o=beta and epsilon_q=1-beta, and its contribution to the exact gradient vanishes because m_n-mu_o=0. This permissible degenerate learner case requires no exclusion. All theorem-critical obligations are closed.
