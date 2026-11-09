# Reference Proof

## Proof Structure and Audited Background

The proof closes six obligations: kernel regularity and well-defined iterates; a one-step MMD inequality; a bandwidth-convolution comparison with a noise moment bound; terminal-lengthscale descent; a contractive recursion with vanishing normalized error; and convergence of that recursion. The primary proof retains the source's convolution architecture. A final private scoring note verifies an alternative using the source's lengthscale-continuity estimate.

The following standard-independent harmonic-analysis facts, recorded under theory_017 and explicitly invoked in the supplied source, are used with the statements given here.

1. With Fourier convention \(\widehat\psi(\omega)=\int e^{-i\omega^\top z}\psi(z)\,dz\), the Gaussian profile \(\psi_u(z)=e^{-\|z\|^2/(2u^2)}\) has transform
\[
S_u(\omega)=(2\pi)^{d/2}u^d e^{-u^2\|\omega\|^2/2}.
\]
For the normalized Matérn profile in the task, with fixed \(s>0\), its transform is
\[
S_u(\omega)=c_{s,d}u^d\left(1+\frac{u^2\|\omega\|^2}{2s}\right)^{-(s+d/2)},
\]
where \(c_{s,d}>0\) is independent of \(u\). Both profiles and their transforms are integrable. Fourier inversion applies, and convolution of an integrable function with a finite measure multiplies their Fourier transforms. Fourier transforms determine integrable functions up to equality almost everywhere and determine finite measures uniquely. These are the transform formulas and convolution facts used at source L000729-L000743.

2. A smooth function \(q\) on \((0,\infty)\) is completely monotone when \((-1)^nq^{(n)}\ge0\) for every integer \(n\ge0\). Products of completely monotone functions are completely monotone. A nonnegative smooth function \(h\) whose derivative is completely monotone is a Bernstein function; for such \(h\), \(e^{-h}\) is completely monotone. If a completely monotone \(q\) extends continuously to zero with \(q(0)=1\), then \(\omega\mapsto q(\|\omega\|^2)\) is positive definite on \(\mathbb R^d\). Every continuous positive-definite function equal to one at zero is the characteristic function of a probability measure. These are the standard Bernstein, Schoenberg, and Bochner facts stated and applied at source L000747-L000756.

Their kernel and parameter hypotheses hold here: the family and Matérn smoothness are fixed, every lengthscale is positive, and \(s>1\). The additional positivity and continuity hypotheses needed for the spectral ratio are verified below. No paper-specific descent or convolution lemma is accepted without deriving its required conclusion.

Write
\[
a_t=\operatorname{MMD}_r^2(P_t,Q),\qquad
g_{u,t}=\nabla f_{u,P_t,Q},\qquad
\Delta_t=r_t^2-r^2\ge0,\qquad A_t=(r_t/r)^d.
\]
Constants denoted by \(K\) may be enlarged between displays and may depend on the fixed kernel profile, dimension, and Matérn smoothness, but not on time, the probability measures, or the lengthscales except through displayed factors.

## 1. Kernel Bounds and Well-Definedness

Here are explicit regularity bounds supporting the estimates used in the source. By scaling, \(S_u(\omega)=u^dS_1(u\omega)\). Define
\[
M_j=(2\pi)^{-d}\int_{\mathbb R^d}\|\omega\|^jS_1(\omega)\,d\omega.
\]
For the Gaussian, all these moments are finite. For the Matérn spectrum, the radial tail for this integral has order \(R^{j-2s-1}\); consequently \(M_1,M_2<\infty\) when \(s>1\). There is no singularity at zero. Fourier inversion and dominated differentiation therefore give a twice continuously differentiable profile and
\[
\sup_z\|\nabla\psi_u(z)\|\le M_1u^{-1},\qquad
\sup_z\|\nabla^2\psi_u(z)\|_{\mathrm{op}}\le M_2u^{-2}.
\]
These bounds include the origin and apply to derivatives in either kernel argument.

For completeness, lengthscale continuity follows by differentiating the spectrum with respect to \(a=u^2\). Put \(p=s+d/2\) in the Matérn case. Then
\[
\partial_a S_{\sqrt a}(\omega)
=\frac{S_{\sqrt a}(\omega)}{a}
\left[\frac d2-p\frac{a\|\omega\|^2}{2s+a\|\omega\|^2}\right].
\]
The bracket is bounded in absolute value by \(d/2+p\). Thus the integral of \(\|\omega\|\,|\partial_aS_{\sqrt a}(\omega)|\), divided by \((2\pi)^d\), is at most a constant times \(a^{-3/2}\). For the Gaussian, the corresponding bracket is \(d/2-a\|\omega\|^2/2\); scaling bounds the same integral by \((dM_1+M_3)a^{-3/2}/2\), where \(M_3<\infty\) is used only for the Gaussian. Integrating in \(a\) and using Fourier inversion yields
\[
\sup_z\|\nabla\psi_{u'}(z)-\nabla\psi_u(z)\|
\le K\frac{u'^2-u^2}{u^3},\qquad u'\ge u>0.
\]
This is the gradient part of the source's kernel-profile continuity bound; it requires no stronger Matérn smoothness than \(s>1\).

Integrating against \(P-Q\), whose total variation is at most two, now gives, uniformly over probability measures,
\[
\|\nabla f_{u,P,Q}\|_\infty\le K/u,\qquad
\operatorname{Lip}(\nabla f_{u,P,Q})\le K/u^2,
\]
\[
\|\nabla f_{u',P,Q}-\nabla f_{u,P,Q}\|_\infty
\le K\frac{u'^2-u^2}{u^3}. \tag{1}
\]
All differentiations under these finite signed-measure integrals are justified by the uniform derivative bounds.

The continuous kernel feature map has norm \(\|k_u(x,\cdot)\|_{\mathcal H_u}=1\) and separable range, so its probability-measure integrals exist. In particular, \(0\le a_t\le4\). The update map is continuous and differs from the identity by a bounded vector field. If \(X\sim P_t\), then
\[
\mathbb E\|X-\gamma_tg_{r_t,t}(X)\|^2
\le2\mathbb E\|X\|^2+2\gamma_t^2K^2/r_t^2<\infty.
\]
Induction proves that every iterate is well defined and belongs to \(\mathcal P_2(\mathbb R^d)\).

## 2. A General One-Step Inequality

Let \(P\in\mathcal P_2(\mathbb R^d)\), let \(G\) be a measurable square-integrable vector field, let \(\gamma>0\), and put \(P^+=(\mathrm{Id}-\gamma G)_\#P\). For \(0\le v\le1\), set \(X_v=X-v\gamma G(X)\) with \(X\sim P\), and let \(P_v\) be its law. Independent copies of \(X\), and independent variables with law \(Q\), give the usual kernel-expectation expression for squared MMD. Its derivative is
\[
\frac{d}{dv}\operatorname{MMD}_u^2(P_v,Q)
=-2\gamma\,\mathbb E[\nabla f_{u,P_v,Q}(X_v)^\top G(X)].
\]
The bounded kernel gradients and \(\mathbb E\|G(X)\|<\infty\) justify differentiation under expectation.

Let \(H=M_2\) be a kernel Hessian-bound constant. The spatial Lipschitz bound is \(2H/u^2\). Coupling the changing measure by \(Y_v=Y-v\gamma G(Y)\), where \(Y\) has law \(P\), gives, for every \(x\),
\[
\|\nabla f_{u,P_v,Q}(x)-\nabla f_{u,P,Q}(x)\|
\le Hv\gamma u^{-2}\mathbb E\|G(Y)\|.
\]
Consequently,
\[
\|\nabla f_{u,P_v,Q}(X_v)-\nabla f_{u,P,Q}(X)\|
\le Hv\gamma u^{-2}\bigl(2\|G(X)\|+\mathbb E\|G(X)\|\bigr).
\]
Multiplying by \(\|G(X)\|\), taking expectations, and using Cauchy-Schwarz bounds the resulting expectation by \(3Hv\gamma u^{-2}\|G\|_{L_2^d(P)}^2\). Integrating the derivative from zero to one therefore proves
\[
\operatorname{MMD}_u^2(P^+,Q)-\operatorname{MMD}_u^2(P,Q)
\le-2\gamma\langle\nabla f_{u,P,Q},G\rangle_{L_2(P)}
+K\gamma^2u^{-2}\|G\|_{L_2^d(P)}^2. \tag{2}
\]
This argument does not require a density for \(P\), invertibility of the update, or pointwise boundedness of an arbitrary \(G\).

## 3. Bandwidth Convolution and Noise Moments

We derive, for \(u'\ge u>0\), a symmetric centered probability law \(\nu_{u,u'}\) such that
\[
\mathbb E[k_u(x+U,y)]=(u/u')^d k_{u'}(x,y),\qquad
\mathbb E\|U\|\le D_{d,s}\sqrt{u'^2-u^2}. \tag{3}
\]
When \(u'=u\), take \(U=0\). Suppose henceforth that \(u'>u\).

For the Gaussian, the required Fourier multiplier is
\[
(u/u')^d\frac{S_{u'}(\omega)}{S_u(\omega)}
=\exp\left(-\frac{(u'^2-u^2)\|\omega\|^2}{2}\right).
\]
This is the characteristic function of \(U\sim N(0,(u'^2-u^2)I_d)\). Its second moment is \(d(u'^2-u^2)\).

For the Matérn, put \(p=s+d/2\), \(\alpha=u^2/(2s)\), and \(\beta=u'^2/(2s)\). The required multiplier is \(g(\|\omega\|^2)\), where
\[
g(z)=\left(\frac{1+\alpha z}{1+\beta z}\right)^p,
\qquad
h(z)=-\log g(z)=p[\log(1+\beta z)-\log(1+\alpha z)].
\]
In particular, \(h(0)=0\), \(h\ge0\), and
\[
h'(z)=-\frac{d}{dz}\log g(z)
=\frac{p(\beta-\alpha)}{(1+\alpha z)(1+\beta z)}. \tag{4}
\]
For any \(b>0\),
\[
(-1)^n\frac{d^n}{dz^n}(1+bz)^{-1}
=n!b^n(1+bz)^{-n-1}\ge0.
\]
Thus both reciprocal factors in (4) are completely monotone, and their product is completely monotone; this also follows directly from Leibniz's rule. Since \(p(\beta-\alpha)>0\), the derivative \(h'\) is completely monotone. The stated Bernstein result applies to the nonnegative function \(h\), so \(g=e^{-h}\) is completely monotone. It is continuous at zero and \(g(0)=1\). Schoenberg and Bochner therefore supply a probability law with characteristic function
\[
\chi(\omega)=g(\|\omega\|^2).
\]
The characteristic function is even, so uniqueness implies that this law is symmetric.

The second moment can be justified without assuming in advance that differentiating the characteristic function under its defining integral is permissible. For a coordinate vector \(e_j\) and a nonzero real \(h_0\),
\[
\mathbb E\left[\frac{2(1-\cos(h_0U_j))}{h_0^2}\right]
=\frac{2(1-\chi(h_0e_j))}{h_0^2}
\longrightarrow-2g'(0)=\frac{p(u'^2-u^2)}s.
\]
Fatou's lemma first proves that \(\mathbb E U_j^2\) is finite and bounded by this limit. Since \(2(1-\cos(h_0U_j))/h_0^2\le U_j^2\), dominated convergence then gives equality. Summing over coordinates yields
\[
\mathbb E\|U\|^2=\frac{dp}{s}(u'^2-u^2).
\]
Symmetry and finite first moment imply centering. Cauchy-Schwarz proves (3)'s moment bound, with \(D_{d,s}=\sqrt{dp/s}\) for Matérn and \(D_d=\sqrt d\) for Gaussian.

For either law, symmetry and the convolution theorem give
\[
\mathcal F\bigl[\mathbb E\psi_u(\cdot+U)\bigr](\omega)
=S_u(\omega)\chi(\omega)=(u/u')^dS_{u'}(\omega).
\]
The function on the left is integrable because \(\nu_{u,u'}\) is a probability measure and \(\psi_u\) is integrable. Fourier uniqueness gives the desired identity almost everywhere, and continuity gives it everywhere. This proves the kernel identity in (3). No density of the noise law is required.

Finally, bounded kernel gradients justify differentiating this identity and integrating it against \(P_t-Q\). Thus
\[
\mathbb E[g_{u,t}(x+U)]=(u/u')^d g_{u',t}(x). \tag{5}
\]

## 4. Terminal-Lengthscale Descent

Use (5) with \(u=r\) and \(u'=r_t\). Boundedness permits exchanging the integrals. By (1) and (3),
\[
\begin{aligned}
\langle g_{r,t},g_{r_t,t}\rangle_{L_2(P_t)}
&=A_t\mathbb E_U\int g_{r,t}(x)^\top g_{r,t}(x+U)\,dP_t(x)\\
&\ge A_t\|g_{r,t}\|_{L_2^d(P_t)}^2
-A_t\|g_{r,t}\|_\infty\operatorname{Lip}(g_{r,t})\mathbb E\|U\|\\
&\ge A_t\|g_{r,t}\|_{L_2^d(P_t)}^2
-KA_t\frac{\sqrt{\Delta_t}}{r^3}.
\end{aligned} \tag{6}
\]
Also, adding and subtracting the terminal-scale gradient and using (1),
\[
r^{-2}\|g_{r_t,t}\|_{L_2^d(P_t)}^2
\le K\left(\frac1{r^4}+\frac{\Delta_t^2}{r^8}\right). \tag{7}
\]
Apply (2) at lengthscale \(r\) with \(G=g_{r_t,t}\). Equations (6)-(7) imply
\[
a_{t+1}-a_t
\le-2\gamma_tA_t\|g_{r,t}\|_{L_2^d(P_t)}^2
+K\gamma_tA_t\frac{\sqrt{\Delta_t}}{r^3}
+K\gamma_t^2\left(\frac1{r^4}+\frac{\Delta_t^2}{r^8}\right). \tag{8}
\]
If \(r_t=r\), the zero-noise choice makes all these arguments valid, with zero bandwidth mismatch. Equivalently, that case follows directly from (2).

## 5. Contractive Recursion

The assumed gradient dominance turns (8) into
\[
a_{t+1}\le(1-2C\gamma_t)a_t+\gamma_t\eta_t, \tag{9}
\]
where
\[
\eta_t=KA_t\frac{\sqrt{\Delta_t}}{r^3}
+K\gamma_t\left(\frac1{r^4}+\frac{\Delta_t^2}{r^8}\right)\ge0.
\]
The positive terminal lengthscale and the schedule assumptions imply \(A_t\to1\), \(\Delta_t\to0\), and \(\gamma_t\to0\), hence \(\eta_t\to0\). Moreover, \(0<2C\gamma_t<1\). No rate relating the two schedules and no summability of their error terms are needed.

## 6. Convergence

Iterating (9), with an empty product interpreted as one, gives
\[
a_T\le a_0\prod_{k=0}^{T-1}(1-2C\gamma_k)
+\sum_{j=0}^{T-1}\gamma_j\eta_j
\prod_{k=j+1}^{T-1}(1-2C\gamma_k). \tag{10}
\]
The initial term tends to zero because
\[
\prod_{k=0}^{T-1}(1-2C\gamma_k)
\le\exp\left(-2C\sum_{k=0}^{T-1}\gamma_k\right)\longrightarrow0.
\]
Given \(\varepsilon>0\), choose \(N\) so that \(0\le\eta_j\le\varepsilon\) for \(j\ge N\). Each of the finitely many terms with \(j<N\) in (10) tends to zero, since the remaining step-size sum diverges. For the tail, the exact identity
\[
\sum_{j=N}^{T-1}2C\gamma_j
\prod_{k=j+1}^{T-1}(1-2C\gamma_k)
=1-\prod_{k=N}^{T-1}(1-2C\gamma_k)\le1
\]
shows that its contribution is at most \(\varepsilon/(2C)\). Therefore \(\limsup_Ta_T\le\varepsilon/(2C)\). Since \(a_T\ge0\) and \(\varepsilon\) is arbitrary,
\[
\operatorname{MMD}_r^2(P_T,Q)=a_T\longrightarrow0.
\]

## Private Alternative-Route Check for Scoring

A convolution construction is not logically required by the public target. Indeed, (1) alone gives
\[
\langle g_{r,t},g_{r_t,t}\rangle_{L_2(P_t)}
\ge\|g_{r,t}\|_{L_2^d(P_t)}^2-K\Delta_t/r^4.
\]
Since \(1\le A_t\le A_0\), gradient dominance implies \(\|g_{r,t}\|_{L_2^d(P_t)}^2\ge Ca_t/A_0\). Also \(\|g_{r_t,t}\|_\infty\le K/r\). The same one-step inequality therefore gives
\[
a_{t+1}\le(1-c\gamma_t)a_t+\gamma_t\widetilde\eta_t,
\qquad c=2C/A_0>0,
\]
with \(\widetilde\eta_t\le K\Delta_t/r^4+K\gamma_t/r^4\to0\) and \(0<c\gamma_t<1\). The preceding product-and-tail argument applies with \(c\) in place of \(2C\). This alternative uses exactly the public assumptions and the source's continuity estimate, so a complete proof along this route merits full credit.

All theorem-critical obligations are closed. There is no unresolved private reference-proof dependency.
