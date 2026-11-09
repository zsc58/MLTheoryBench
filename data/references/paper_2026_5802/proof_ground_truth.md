# Reference Proof

## Contract and proof obligations

The upper experiment has arbitrary positive integers M,K,R and T=KR. Samples are fresh and independent across clients and time, with each client using its own distribution. All clients start at zero. The same minimizer x* satisfies the radius and optimum-gradient bounds. The upper output averages all pre-update states. Each lower experiment has two clients and uses the final synchronized state; its objectives must be fixed independently of K and eta.

The obligations are: (1) derive the average-iterate recursion; (2) derive and close the consensus/heterogeneity inequalities; (3) verify the prescribed step-size calculation, including the constant 18; (4) construct and analyze the second-order instance uniformly over K and eta; (5) construct and analyze the first-order instance uniformly over K and eta. All are closed below without invoking a specialized external result.

## Preliminary elementary inequality

For a differentiable convex H-smooth function f, with H>0,
\[
f(x)-f(y)-\langle\nabla f(y),x-y\rangle\ge\frac{\|\nabla f(x)-\nabla f(y)\|^2}{2H}.
\]
Indeed, subtract the linear function with gradient \(\nabla f(y)\), obtaining a convex H-smooth function h minimized at y. Smoothness at \(x-H^{-1}\nabla h(x)\) gives \(h(y)\le h(x)-\|\nabla h(x)\|^2/(2H)\). Applying the inequality in both directions and adding proves
\[
\langle\nabla f(x)-\nabla f(y),x-y\rangle\ge H^{-1}\|\nabla f(x)-\nabla f(y)\|^2.
\]
Expanding a squared distance now shows that \(x\mapsto x-\eta\nabla f(x)\) is nonexpansive for \(0\le\eta\le2/H\).

## Step 1: Average-iterate descent

Write
\[
y_t=M^{-1}\sum_m x_t^m,\quad A(t)=\mathbb E\|y_t-x^*\|^2,\quad C(t)=M^{-1}\sum_m\mathbb E\|x_t^m-y_t\|^2,
\]
\[
D(t)=\mathbb E[F(y_t)-F(x^*)],\qquad V(t)=M^{-1}\sum_m\mathbb E\|\nabla F_m(y_t)-\nabla F(y_t)\|^2.
\]
For each sequence let the subscript max denote its maximum over integer times 0 through T. All second moments are finite: the gradients of the client objectives have at most linear growth, the oracle variance is uniformly bounded, and induction over the finite number of updates, together with Jensen's inequality at synchronization, preserves finite second moments.

Condition on the samples before time t. Put \(y=y_t\), \(a_m=\nabla F_m(x_t^m)\), \(a_m^*=\nabla F_m(x^*)\),
\[
d=M^{-1}\sum_m a_m,\quad U=M^{-1}\sum_m\|a_m-a_m^*\|^2,\quad \Xi=M^{-1}\sum_m\|x_t^m-y\|^2.
\]
Since \(M^{-1}\sum_m a_m^*=\nabla F(x^*)=0\), Jensen gives \(\|d\|^2\le U\). Smoothness from \(x_t^m\) to y and the preliminary inequality from \(x_t^m\) to x* give, after subtraction and averaging,
\[
F(y)-F(x^*)\le\langle d,y-x^*\rangle+\frac H2\Xi-\frac{U}{2H}.
\]
The average update, whether or not synchronization occurs, is \(y_{t+1}=y-\eta(d+\bar\epsilon_t)\). Conditional unbiasedness and independence give \(\mathbb E_t\bar\epsilon_t=0\) and \(\mathbb E_t\|\bar\epsilon_t\|^2\le\sigma^2/M\). Thus
\[
\mathbb E_t\|y_{t+1}-x^*\|^2\le\|y-x^*\|^2-2\eta(F(y)-F(x^*))+\eta H\Xi-(\eta/H-\eta^2)U+\eta^2\sigma^2/M.
\]
For \(0<\eta\le1/(2H)\), dropping the nonpositive U term and using nonnegativity of the gap and consensus error yields the weaker convenient recursion
\[
D(t)\le\frac{A(t)-A(t+1)}\eta+\frac{3\eta\sigma^2}{M}+2HC(t).\tag{1}
\]
In particular, since \(A(0)=\|x^*\|^2\le B^2\),
\[
A_{\max}\le B^2+3\eta^2\sigma^2T/M+2\eta HT C_{\max}.\tag{2}
\]

## Step 2: Consensus and self-bounding closure

If K=1, all states are synchronized at every integer time and C(t)=0. Suppose K>=2. At a nonsynchronization time t, empirical variance is no larger than the average squared distance to \(y_{t-1}-\eta\nabla F(y_{t-1})\). Condition on the past, remove the zero-mean noise, and decompose the remaining displacement as
\[
[x_{t-1}^m-\eta\nabla F_m(x_{t-1}^m)]-[y_{t-1}-\eta\nabla F_m(y_{t-1})]
+\eta[\nabla F(y_{t-1})-\nabla F_m(y_{t-1})].
\]
The inequality \(\|u+v\|^2\le K\|u\|^2/(K-1)+K\|v\|^2\), followed by nonexpansiveness, gives
\[
C(t)\le\frac K{K-1}C(t-1)+\eta^2K V(t-1)+\eta^2\sigma^2.
\]
Let \(\delta(t)=K\lfloor t/K\rfloor\). Since \(C(\delta(t))=0\), unrolling fewer than K steps and using \((1+1/(K-1))^{K-1}\le e<3\) proves
\[
C(t)\le3(t-\delta(t))(\eta^2K V_{\max}+\eta^2\sigma^2),
\quad C_{\max}\le3\eta^2K^2 V_{\max}+3\eta^2K\sigma^2.\tag{3}
\]
The same final bound holds for K=1.

Decompose each gradient disagreement at y_t around x*. The two heterogeneity assumptions and \(\nabla F(x^*)=0\) imply
\[
V(t)\le2\tau^2 A(t)+2\zeta_*^2,
\qquad V_{\max}\le2\tau^2 A_{\max}+2\zeta_*^2.\tag{4}
\]
Combining (2)--(4), with T=KR, gives
\[
(1-12\eta^3H\tau^2K^3R)A_{\max}
\le B^2+3\eta^2\sigma^2T/M+12\eta^3HK^3R\zeta_*^2+6\eta^3HK^2R\sigma^2.
\]
The prescribed second step-size restriction makes the coefficient on the left at least 1/2, also when tau=0. Hence
\[
A_{\max}\le2B^2+6\eta^2\sigma^2T/M+24\eta^3HK^3R\zeta_*^2+12\eta^3HK^2R\sigma^2.\tag{5}
\]
Furthermore \(6\eta^2K^2\tau^2\le1/(2\eta HT)\), so (3)--(5) imply
\[
C_{\max}\le\frac{A_{\max}}{2\eta HT}+6\eta^2K^2\zeta_*^2+3\eta^2K\sigma^2
\le\frac{B^2}{\eta HT}+\frac{3\eta\sigma^2}{HM}+18\eta^2K^2\zeta_*^2+9\eta^2K\sigma^2.\tag{6}
\]

## Step 3: Upper bound and boundary cases

First suppose B>0. The prescribed eta is positive and finite. Convexity, telescoping (1), and (6) give
\[
\mathbb E[F(\hat x)-F(x^*)]\le\frac{3B^2}{\eta KR}+\frac{9\eta\sigma^2}{M}+36\eta^2HK^2\zeta_*^2+18\eta^2HK\sigma^2.\tag{7}
\]
The reciprocal of the minimum defining eta is the maximum of the reciprocals, which is at most their sum. Consequently the first term in (7) is at most
\[
6\frac{HB^2}{KR}+3\sqrt[3]{24}\frac{(H\tau^2)^{1/3}B^2}{R^{2/3}}
+3\sqrt3\frac{\sigma B}{\sqrt{MKR}}
+3\sqrt[3]{12}\frac{(H\zeta_*^2B^4)^{1/3}}{R^{2/3}}
+3\sqrt[3]{6}\frac{(H\sigma^2B^4)^{1/3}}{K^{1/3}R^{2/3}}.
\]
The remaining three terms in (7) are bounded, respectively, by
\[
3\sqrt3\frac{\sigma B}{\sqrt{MKR}},\qquad
3\sqrt[3]{12}\frac{(H\zeta_*^2B^4)^{1/3}}{R^{2/3}},\qquad
3\sqrt[3]{6}\frac{(H\sigma^2B^4)^{1/3}}{K^{1/3}R^{2/3}}.
\]
A term with zero noise or heterogeneity is simply zero and needs no division. The five combined coefficients are
\[
6,\quad3\sqrt[3]{24},\quad6\sqrt3,\quad6\sqrt[3]{12},\quad6\sqrt[3]{6},
\]
all less than 18. This proves the required upper bound. This calculation corrects the source's intermediate stochastic coefficient without changing its final result.

If B=0, then x*=0. If sigma>0 or zeta_*>0, the prescribed minimum is eta=0; all states remain zero. If sigma=zeta_*=0, every client gradient and its stochastic error vanish at zero, so again all states remain zero. The upper bound is therefore zero on both sides. This covers B=0 without dividing by eta or B.

## Step 4: Uniform second-order lower construction

Fix H,B,tau,R. If B=0 or tau=0, take both objectives identically zero on R^2. The target lower bound is zero. Otherwise set
\[
\kappa=12R,\quad\alpha=\frac{\kappa-1}{\kappa+1},\quad
p_1=(1,0)^\top,\quad p_2=(\alpha,\sqrt{1-\alpha^2})^\top,
\quad\lambda=\min\{H,\sqrt{3R}\tau\}.
\]
Let \(A_m=\lambda p_mp_m^\top\) and \(A=(A_1+A_2)/2\). Its eigenvalues are
\[
\Lambda_+=\frac{12R\lambda}{12R+1},\qquad\Lambda_-=\frac\lambda{12R+1}.
\]
For orthonormal eigenvectors u_+,u_-, choose
\[
x^*=-\frac B{\sqrt2}(u_++u_-),\qquad F_m(x)=\frac12(x-x^*)^\top A_m(x-x^*).
\]
These objectives are deterministic, convex, and H-smooth, with common minimizer x* of norm B and zeta_*=0. Also
\[
\|A_1-A_2\|=\lambda\sqrt{1-\alpha^2}\le\lambda/\sqrt{3R}\le\tau.
\]
Since \(A_1-A=(A_1-A_2)/2=-(A_2-A)\), the averaged squared gradient-increment disagreement is at most \(\tau^2\|x-y\|^2\). Thus the required second-order condition holds.

For any K>=1 and eta>0, the rank-one identity gives
\[
(I-\eta A_m)^K=I-sA_m,\qquad s=\frac{1-(1-\eta\lambda)^K}{\lambda}.
\]
Consequently synchronized error evolves by \(e_{r+1}=(I-sA)e_r\). Its final objective gap is
\[
\frac{B^2}{4}\left[\Lambda_+(1-s\Lambda_+)^{2R}+\Lambda_-(1-s\Lambda_-)^{2R}\right].\tag{8}
\]
If \(s\ge3/\Lambda_+\), the high-eigenvalue term in (8) is at least \(\lambda B^2/(4R)\). Otherwise,
\[
1-s\Lambda_->1-\frac1{4R}>0.
\]
This also covers negative s. Bernoulli's inequality gives \((1-1/(4R))^R\ge3/4\), so the low-eigenvalue term is at least
\[
\frac{9\lambda B^2}{64(12R+1)}\ge\frac9{832}\frac{\lambda B^2}{R}.
\]
The constant 9/832 replaces the source's incorrect final numerical comparison. Since
\[
\frac{\lambda B^2}{R}=\min\{HB^2/R,\sqrt3\tau B^2/\sqrt R\}\ge\min\{HB^2/R,\tau B^2/\sqrt R\},
\]
the claimed lower bound follows. The objectives depend only on H,B,tau,R, not on K or eta.

## Step 5: Uniform first-order lower construction

### Active-coordinate estimate

Fix L>0 and zeta_*>0. Define
\[
g(s)=\begin{cases}Ls^2/4,&s<0,\\Ls^2/2,&s\ge0,\end{cases}
\qquad G_1(s)=g(s)-\zeta_*s,\quad G_2(s)=g(s)+\zeta_*s.
\]
For K>=2 and \(0<\eta\le1/L\), compare these updates to those for
\[
\widetilde G_1(s)=Ls^2/2-\zeta_*s,\qquad
\widetilde G_2(s)=Ls^2/4+\zeta_*s.
\]
All four update maps are nondecreasing. For client 1 the true map is no larger than the comparison map on s<0 and agrees on s>=0; for client 2 it agrees on s<0 and is no larger on s>=0. Induction over local steps and synchronization therefore gives \(\bar s_{rK}\le\widetilde{\bar s}_{rK}\) from common zero initialization.

Set
\[
a=1-\eta L/2,\quad b=1-\eta L,\quad
A_K=(a^K+b^K)/2,\quad\Delta_K=\frac{\zeta_*}{2L}(1+b^K-2a^K).
\]
Solving the two affine local recurrences and averaging yields
\[
\widetilde{\bar s}_{(r+1)K}=A_K\widetilde{\bar s}_{rK}-\Delta_K,
\qquad\widetilde{\bar s}_{T}=-\Delta_K\sum_{r=0}^{R-1}A_K^r.
\]
Here \(A_K\in[0,1)\). For \(\phi(h)=1+(1-h)^K-2(1-h/2)^K\),
\[
\phi(0)=0,\qquad\phi'(h)=K[(1-h/2)^{K-1}-(1-h)^{K-1}]\ge0
\]
on [0,1], so \(\Delta_K\ge0\) and \(\bar s_T\le\widetilde{\bar s}_T\le0\).

Write \(\theta=K\eta L\). If theta<=1, the second derivative of \(f(h)=(1-h)^K\) on [0,eta L] is at least
\[
K(K-1)(1-1/K)^{K-2}\ge K^2/(2e).
\]
The midpoint strong-convexity inequality gives \(\phi(\eta L)\ge\theta^2/(8e)\). If theta>=1, monotonicity of phi and the preceding estimate at h=1/K give \(\phi(\eta L)\ge1/(8e)\). Thus
\[
\Delta_K\ge\frac{\zeta_*}{16eL}\min\{\theta^2,1\}.\tag{9}
\]
For theta<=1, \(1-A_K\le3\theta/4\le\theta\). The geometric-sum formula and \(1-e^{-u}\ge(1-e^{-1})\min\{u,1\}\) give
\[
\sum_{r=0}^{R-1}A_K^r\ge(1-e^{-1})\min\{R,(1-A_K)^{-1}\}
\ge(1-e^{-1})\min\{R,1/\theta\}.
\]
For theta>=1 the sum is at least one. Combining this with (9) gives, for a universal c_0>0,
\[
|\bar s_T|\ge c_0\frac{\zeta_*}{L}\min\{1,\theta,R\theta^2\}.
\]
As \(g(\bar s_T)=L\bar s_T^2/4\), there is a universal c_1>0 such that
\[
g(\bar s_T)-g(0)\ge c_1\frac{\zeta_*^2}{L}\min\{1,\theta^2,R^2\theta^4\}
=c_1\min\left\{\frac{\zeta_*^2}{L},LK^2\eta^2\zeta_*^2\min\{(RK\eta L)^2,1\}\right\}.\tag{10}
\]
This closes the active-coordinate obligation rather than invoking it as an unexplained prior result.

### Auxiliary coordinates and assembly

Let
\[
Q=\min\left\{HB^2,\frac{\zeta_*^2}{H},\frac{(H\zeta_*^2B^4)^{1/3}}{R^{2/3}}\right\}.
\]
If Q=0, choose both objectives identically zero on R^3. Otherwise B,zeta_*>0. Set exactly as in the source
\[
L=H/2,\qquad\mu=Q/(4B^2),\qquad
q(u)=\frac\mu2(u+B/3)^2,\quad h(v)=\frac H2(v+B/3)^2,
\]
\[
F_m(s,u,v)=G_m(s)+q(u)+h(v).
\]
The average objective is \(g(s)+q(u)+h(v)\), with minimizer \(x^*=(0,-B/3,-B/3)\) and norm \(\sqrt2B/3\le B\). Since \(\mu\le H/4\), the clients are convex and H-smooth. Their gradients at x* are \((\mp\zeta_*,0,0)\). Their gradient differences from the average are these same constant vectors everywhere, which verifies tau=0 directly, including across the curvature change at s=0. No twice differentiability is assumed or needed.

Identical deterministic client objectives on the u and v coordinates keep those coordinates synchronized at every step. Their errors relative to their respective minimizers are
\[
u_t+B/3=(1-\eta\mu)^tB/3,\qquad v_t+B/3=(1-\eta H)^tB/3.
\]
If \(\eta\le1/(2\mu KR)\), Bernoulli's inequality gives \((1-\eta\mu)^{KR}\ge1/2\), hence
\[
q(u_T)\ge\mu B^2/72=Q/288.
\]
If \(\eta>2/H\), then \(|1-\eta H|>1\), and \(h(v_T)\ge HB^2/18\ge Q/18\).

It remains only to consider the interval
\[
\eta_0:=1/(2\mu KR)<\eta\le2/H=1/L.
\]
If that interval is empty there is nothing to prove. Otherwise the right side of (10) is nondecreasing in eta, so it may be evaluated at eta_0. Because \(\mu\le H/4=L/2\),
\[
RK\eta_0L=L/(2\mu)\ge1.
\]
The two entries in the resulting minimum are
\[
\frac{\zeta_*^2}{L}=\frac{2\zeta_*^2}{H}\ge2Q,
\qquad
LK^2\eta_0^2\zeta_*^2=\frac{L\zeta_*^2}{4\mu^2R^2}
=\frac{2H\zeta_*^2B^4}{Q^2R^2}\ge2Q,
\]
where the last inequality uses \(Q^3\le H\zeta_*^2B^4/R^2\). Thus the active-coordinate error is at least \(2c_1Q\) throughout the intermediate interval. The three cases cover every eta>0, including eta=2/H. The objectives depend only on H,B,zeta_*,R, not on K or eta.

Finally choose one universal positive c no larger than the constants obtained in Steps 4 and 5. This proves both lower assertions with the same c. All five proof obligations and all boundary cases are closed.
