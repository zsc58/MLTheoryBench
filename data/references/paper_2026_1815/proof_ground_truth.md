# Reference Proof

## Proof obligations

The proof must establish: (1) identification and the conditional-expectation identities with adequate integrability; (2) the Gaussian hyperbola calculation under the correct law; (3) deconfounding in both models; (4) the two distinct normalized overlap formulas; (5) nondecrease and smooth strictness, including analytic justifications; (6) strictness for the two nonsmooth links and all endpoints; and (7) minimization over the specified unit-vector family. All seven obligations are closed below.

## 1. Identification, integrability, and change of measure

Write \(\pi=\Pr(T=1)\), \(r(X)=dP_X^1/dP_X^0(X)\), and \(M=m_0(X)\). Conditional Jensen gives \(M\in L^2(P^0)\). For a measurable representation \(V=\psi(X)\), define \(r_V=\mathbb E_0[r\mid V]\). For every bounded measurable function \(b\),
\[
\mathbb E_0[b(V)r_V]=\mathbb E_0[b(V)r]=\mathbb E_1[b(V)].
\]
Thus \(P_V^1\ll P_V^0\) and \(r_V=dP_V^1/dP_V^0(V)\). Moreover \(\|r_V\|_{L^2(P^0)}\le\|r\|_{L^2(P^0)}\). This proves directly the portion of the inherited external proposition needed here; no unproved external dependency is used.

Also \(m_0(V)=\mathbb E_0[M\mid V]\in L^2(P^0)\). Cauchy–Schwarz therefore makes both \(\mathbb E_1|M|\) and \(\mathbb E_1|m_0(V)|\) finite. To check identification of the actual potential-outcome target, set \(a(X)=\mathbb E_0[|Y|\mid X]\). Conditional Jensen gives \(a\in L^2(P^0)\). Consistency, unconfoundedness, and one-sided overlap yield
\[
\mathbb E_1|Y(0)|=\mathbb E_0[r(X)a(X)]<\infty,
\qquad \mathbb E_1[Y(0)]=\mathbb E_1[M].
\]
The treated potential outcome equals observed \(Y\) under \(P^1\) and is integrable. Consequently \(\tau=\mathbb E_1[Y]-\mathbb E_1[M]\).

Changing measure and centering conditionally gives
\[
\begin{aligned}
\tau_V-\tau
&=\mathbb E_0[r(M-\mathbb E_0[M\mid V])]\\
&=\mathbb E_0[(r-r_V)(M-\mathbb E_0[M\mid V])]\\
&=\mathbb E_0[\operatorname{Cov}_0(M,r\mid V)].
\end{aligned}
\]
Every product is integrable by the preceding L2 bounds.

## 2. Gaussian geometry

Use \(R=P^0\) in model A and \(R=P\) in model B. In either case \(X\sim_R N(0,I_d)\). Put \(A=\alpha^\top X\), \(B=\beta^\top X\), \(V=\gamma^\top X\), \(p=\alpha^\top\gamma\), and \(q=\beta^\top\gamma\). The Gaussian residuals \(A-pV\) and \(B-qV\) are jointly Gaussian and independent of \(V\), with covariance \(\rho-pq\). Hence
\[
\operatorname{Cov}_R(A,B\mid V)=\rho-pq.
\]
Zero covariance gives conditional independence, including when a residual is identically zero.

The vectors \(u_+,u_-\) are orthonormal. With \(a=\sqrt{(1+\rho)/2}\) and \(b=\sqrt{(1-\rho)/2}\),
\[
p=aw_1+bw_2,\qquad q=aw_1-bw_2,
\qquad pq=\frac{(1+\rho)w_1^2-(1-\rho)w_2^2}{2}.
\]
Thus the displayed constraint is exactly \(pq=\rho\), and its unit vectors have \(A\perp_R B\mid V\).

## 3. Deconfounding in the two models

In A, let \(c=\mathbb E[h(Z)]\in(0,\infty)\). Then \(M=m(A)\) and \(r=h(B)/c\). Conditional independence under \(P^0\) makes their conditional covariance zero. The bias formula proves \(\tau_V=\tau\). The normalizer \(1/c\) must be retained in the covariance formula.

In B, use population conditional independence. The preceding bounds imply \(M\in L^1(P)\), since \(P\) is the mixture of \(P^0\) and \(P^1\). Put \(s(V)=\mathbb E_P[h(B)\mid V]=\Pr(T=1\mid V)\) and \(\mu(V)=\mathbb E_P[M\mid V]\). Since \(h(B)<1\) almost surely, \(s(V)<1\) almost surely. Conditional independence gives
\[
\mathbb E_P[M(1-h(B))\mid V]=\mu(V)(1-s(V)),
\quad
\mathbb E_P[Mh(B)\mid V]=\mu(V)s(V).
\]
Conditioning on treatment therefore gives
\[
m_0(V)=\mathbb E_0[M\mid V]
=\frac{\mathbb E_P[M(1-h(B))\mid V]}{1-s(V)}=\mu(V).
\]
Finally,
\[
\mathbb E_1[m_0(V)]
=\pi^{-1}\mathbb E_P[s(V)\mu(V)]
=\pi^{-1}\mathbb E_P[h(B)M]
=\mathbb E_1[M].
\]
The products in these population calculations are integrable because \(M\in L^1(P)\) and \(h,s\in[0,1]\). This proves deconfounding without incorrectly treating \(P^0\) as Gaussian in B.

## 4. Exact overlap formulas

For independent standard normal variables \(Z,Z'\), set
\[
S_u(x)=\mathbb E[h(ux+\sqrt{1-u^2}Z')],\qquad -1\le u\le1.
\]
Gaussian conditioning under the appropriate law gives:

- In A, \(r_V=S_q(V)/c\) and \(V\sim_{P^0}N(0,1)\), so
\[
\mathcal O(V)=G(q),\qquad G(u)=\mathbb E[S_u(Z)^2]/c^2.
\]
- In B, \(V\sim_PN(0,1)\), \(s(V)=S_q(V)\), and Bayes' rule gives
\[
\frac{dP_V^0}{dP_V}(V)=\frac{1-s(V)}{1-\pi},\qquad
r_V=\frac{1-\pi}{\pi}\frac{s(V)}{1-s(V)}.
\]
Thus
\[
\mathcal O(V)=G(q),\qquad
G(u)=\frac{1-\pi}{\pi^2}\mathbb E\!\left[\frac{S_u(Z)^2}{1-S_u(Z)}\right].
\]
In B, \(\pi=\mathbb E[h(Z)]\in(0,1)\).

Write \(G(u)=\mathbb E[F(S_u(Z))]\), where \(F(t)=t^2/c^2\) in A and \(F(t)=k t^2/(1-t)\), \(k=(1-\pi)/\pi^2>0\), in B. The latter is used only on \([0,1)\). Both are convex, with
\[
F_A''=2/c^2,\qquad F_B''(t)=2k/(1-t)^3>0.
\]
Since \(S_{-u}(x)=S_u(-x)\), \(G\) is even. Jensen also gives, for every \(u\in[0,1]\),
\[
G(u)\le \mathbb E[F(h(Z))]=G(1).
\]
The right side is finite: in A this follows from the standing density-ratio L2 assumption, and in B it follows from that assumption and the displayed Bayes formula. The link-class bounds give the same finiteness directly.

## 5. Smooth monotonicity and analytic justification

For \(0\le u<1\), put
\[
A_j(u,x)=\mathbb E[h^{(j)}(ux+\sqrt{1-u^2}Z')].
\]
The bounds below apply to every derivative available in the relevant class. The elementary Gaussian integral obtained by completing the square is
\[
\mathbb E[e^{a(\mu+\sigma Z')^2}]
=(1-2a\sigma^2)^{-1/2}
\exp\!\left(\frac{a\mu^2}{1-2a\sigma^2}\right),
\quad 2a\sigma^2<1.
\]
It implies
\[
|A_j(u,x)|\le\sqrt2 C e^{\lambda x^2}.
\]
The same bound applies to \(j=0\) in B because \(0\le h<1<C e^{\lambda x^2}\). On each \(0\le u\le u_0<1\), completing the square also gives
\[
\mathbb E[|Z'|e^{\lambda(ux+\sqrt{1-u^2}Z')^2}]
\le\sqrt2(3+16\lambda^2x^2)e^{\lambda x^2}.
\]
For pointwise differentiation inside the inner integral one may use \((ux+\sqrt{1-u^2}z')^2\le x^2+z'^2\), together with \(\lambda<1/2\), as a uniform integrable envelope on compact parameter intervals. Therefore
\[
\partial_u S_u(x)=xA_1(u,x)-uA_2(u,x),\qquad
\partial_x S_u(x)=uA_1(u,x),\qquad
\partial_x A_1(u,x)=uA_2(u,x).
\]
The first identity follows initially by differentiating and then integrating \(Z'h'(ux+\sqrt{1-u^2}Z')\) by parts against the Gaussian density.

In B, the lower bound on \(1-h\) gives
\[
\frac1{1-S_u(x)}
\le C\sqrt{1+2\lambda'(1-u^2)}
\exp\!\left(\frac{\lambda'u^2x^2}{1+2\lambda'(1-u^2)}\right)
\le\frac{2C}{\sqrt3}e^{\lambda'x^2}.
\]
Consequently \(|F_B'(S_u(x))|\) is bounded by a constant times \(e^{2\lambda'x^2}\), and \(F_B''(S_u(x))\) by a constant times \(e^{3\lambda'x^2}\). In A the corresponding bounds are a constant times \(e^{\lambda x^2}\) and a constant.

These estimates dominate the derivative of \(F(S_u(x))\) by a polynomial times \(e^{2\lambda x^2}+e^{(\lambda+2\lambda')x^2}\). The integrands after integration by parts are bounded by constants times
\[
e^{2\lambda x^2}+e^{(\lambda+2\lambda')x^2}+e^{(2\lambda+3\lambda')x^2}.
\]
All exponents are strictly below \(1/2\), since \(2\lambda<1/2\) and \(2\lambda+3\lambda'<1/2\). Multiplication by the Gaussian density also makes the boundary term \(A_1(u,x)F'(S_u(x))\varphi(x)\) vanish at both infinities. Thus dominated differentiation and integration by parts are justified. Mere K-times differentiability is sufficient: the derivative bounds make the lower derivatives locally Lipschitz where needed, and Gaussian convolution supplies the displayed derivatives.

Now
\[
G'(u)=\mathbb E[(ZA_1(u,Z)-uA_2(u,Z))F'(S_u(Z))].
\]
Integration by parts in \(Z\), using
\[
\partial_x[A_1(u,x)F'(S_u(x))]
=uA_2(u,x)F'(S_u(x))+uA_1(u,x)^2F''(S_u(x)),
\]
cancels the terms containing \(A_2\), leaving
\[
G'(u)=u\,\mathbb E[A_1(u,Z)^2F''(S_u(Z))]\ge0.
\]
The same envelopes give continuity at zero. This proves nondecrease on \([0,1)\); the Jensen bound from Section 4 extends it to \([0,1]\).

## 6. Smooth strictness

Let \(a=\mathbb E[h^{(K)}(Z)]\ne0\), and define
\[
J_j(u)=\mathbb E[A_j(u,Z)^2],\qquad 0\le j\le K.
\]
The preceding calculation with the quadratic function, applied to \(h^{(j)}\), is valid for \(j\le K-1\), since it uses derivatives only through \(j+2\le K+1\). It gives
\[
J_j'(u)=2uJ_{j+1}(u),\qquad 0\le j\le K-1.
\]
All these functions are continuous at zero. No differentiability of \(J_K\) is needed. Jensen and the standard normal distribution of \(uZ+\sqrt{1-u^2}Z'\) give
\[
J_K(u)\ge\big(\mathbb E[h^{(K)}(Z)]\big)^2=a^2.
\]
Integrating the recursions, and using \(J_j(0)\ge0\), gives
\[
J_1(u)\ge\frac{a^2u^{2K-2}}{(K-1)!}>0\qquad(0<u<1).
\]
In A, \(G'(u)=2uJ_1(u)/c^2>0\). In B, \(F_B''\ge2k\), so \(G'(u)\ge2kuJ_1(u)>0\). Hence \(G\) is strictly increasing on \([0,1)\). For any \(u<1\), choosing \(u<v<1\) gives \(G(u)<G(v)\le G(1)\), so strictness also includes the endpoint 1.

## 7. Nonsmooth strict regimes

Only A is at issue here. Write \(\varphi\) and \(\Phi\) for the standard normal density and distribution function, and \(s=\sqrt{1-u^2}\).

For the threshold link, \(c=\Phi(z_0)>0\), and for \(0<u<1\),
\[
S_u(x)=\Phi\!\left(\frac{z_0-ux}{s}\right),\qquad
\partial_xS_u(x)=-\frac{u}{s}\varphi\!\left(\frac{z_0-ux}{s}\right)\ne0.
\]
For the ReLU link, direct integration of a truncated Gaussian gives \(c=\varphi(0)>0\) and
\[
S_u(x)=s\varphi(ux/s)+ux\Phi(ux/s),\qquad
\partial_xS_u(x)=u\Phi(ux/s)>0.
\]
Differentiating either explicit expression verifies
\[
\partial_uS_u(x)=\frac{x\partial_xS_u(x)-\partial_{xx}S_u(x)}{u}.
\]
For example, in the threshold case set \(b=(z_0-ux)/s\). Then \(\partial_u b=-x/s+ub/s^2\) and \(\partial_{xx}S_u=-u^2b\varphi(b)/s^2\), which give the identity. In the ReLU case \(\partial_uS_u=x\Phi(ux/s)-(u/s)\varphi(ux/s)\) and \(\partial_{xx}S_u=(u^2/s)\varphi(ux/s)\), giving the same identity.

On each compact subinterval of \((0,1)\), these formulas and their required derivatives are bounded by polynomials in \(|x|\), so differentiation and Gaussian integration by parts are justified. As \(G(u)=\mathbb E[S_u(Z)^2]/c^2\),
\[
\begin{aligned}
G'(u)
&=\frac{2}{uc^2}\mathbb E[S_u(Z)(Z\partial_xS_u(Z)-\partial_{xx}S_u(Z))]\\
&=\frac{2}{uc^2}\mathbb E[(\partial_xS_u(Z))^2]>0.
\end{aligned}
\]
For the last equality, integrate \(Z S_u\partial_xS_u\) by parts; its derivative is \((\partial_xS_u)^2+S_u\partial_{xx}S_u\), and the boundary terms vanish.

At zero, \(S_u(x)\to c\). Dominated convergence applies because the threshold smoothing is bounded by 1 and the ReLU smoothing is bounded by \(|x|+\mathbb E|Z'|\). Hence \(G\) is continuous at zero. Its derivative is positive on \((0,1)\), so it is strictly increasing on \([0,1)\). The finite Jensen endpoint bound again gives strictness through 1. This closes both nonsmooth cases without invoking an external Gaussian integral formula.

## 8. Optimizer geometry and conclusion

For every admissible unit vector, Section 2 gives \(pq=\rho\), where \(|p|\le1\). If \(\rho\ne0\),
\[
|q|=|\rho|/|p|\ge|\rho|.
\]
Equality requires \(|p|=1\), which for unit vectors is equivalent to \(\gamma=\alpha\) or \(\gamma=-\alpha\). Both are admissible and attain \(|q|=|\rho|\).

If \(\rho=0\), the minimum of \(|q|\) is zero, attained by \(\gamma=\alpha\), for example. Because \(\alpha,\beta\) are then orthonormal, the condition \(q=0\) says exactly that the projection of \(\gamma\) onto their span is \(t\alpha\), with \(|t|\le1\). Conversely every such unit vector satisfies the constraint and attains zero. This statement concerns actual unit vectors; in dimension two no nonzero orthogonal component is available, so only feasible members of the stated set occur.

Since \(\mathcal O(V)=G(|q|)\), nondecrease makes all these vectors global minimizers within the displayed family. Strict increase makes them the only minimizers in each strict regime. Constant links can make \(G\) constant, so no exact optimizer characterization is claimed in the non-strict regime.
