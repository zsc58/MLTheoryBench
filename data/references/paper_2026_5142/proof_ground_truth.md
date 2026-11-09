# Reference Proof

## Contract and proof obligations

The experiment is deterministic exact Euclidean gradient flow for a finite softmax policy with orthonormal features. Both trajectories start at the same finite parameter vector. Rewards and epsilon remain fixed in the final small-initial-probability comparison. The probability guarantee begins at the numerical upper bound U_epsilon, not at the first ground-truth-reward hitting time along the proxy trajectory.

The critical obligations are: correct gradient and probability dynamics; quantitative attraction through two reward thresholds; concentration at the second threshold; escape-time integration with its denominator restriction; the proxy hitting-time and probability guarantees; and uniform control of the proxy coefficient as the initial optimal probability decreases. All are derived below. No specialized external theorem is assumed. The scalar comparisons used below follow by direct integration.

## step_001: Gradient identities and well-definedness

For either reward r, write p_y=pi_theta(y), V=V_r(theta), A_y=r(y)-V, and bar_phi=sum_y p_y phi(y). Differentiating the finite softmax sum gives
\[
\nabla p_y=p_y(\phi(y)-\bar\phi),\qquad
\nabla V=\sum_y p_yA_y\phi(y).
\]
For orthonormal features, their norms are one, and therefore
\[
\|\nabla V\|\le\sum_y p_y|A_y|
\le\left(\sum_y p_yA_y^2\right)^{1/2}\le1.
\]
The last inequality follows from Var_p(r)<=E_p[r^2]<=1. Thus V is 1-Lipschitz, by integrating its gradient along line segments. The vector field is smooth and bounded, so its unique local solutions extend to every finite nonnegative time. In particular, parameters remain finite and all output probabilities remain strictly positive. Along its own gradient flow,
\[
\frac{d}{dt}V(\theta_t)=\|\nabla V(\theta_t)\|^2\ge0.
\]

## step_002: Logit and probability dynamics

Let f_y(theta)=<phi(y),theta>. In general,
\[
\dot f_y=\sum_z p_zA_z\langle\phi(y),\phi(z)\rangle.
\]
Separating the term z=y gives the self/cross decomposition; under orthonormality it reduces to dot f_y=p_y A_y. Differentiating the softmax with respect to time then gives
\[
\dot p_y=p_y\left(\dot f_y-\sum_zp_z\dot f_z\right)
=p_y\left(p_yA_y-\sum_zp_z^2A_z\right).
\]
The factors p_y and p_z^2 inside the parentheses are essential.

## step_003: Quantitative attraction under the ground-truth reward

Use the private abbreviations
\[
a=r_G(y_{\mathrm{star}}),\quad g=r_G(y_{\mathrm{med}}),\quad c=r_G(y_{\mathrm{bad}}),\quad
d=\Delta_1,\quad e=\Delta_2,\quad H=d+e=a-c.
\]
Thus 0<g<a<=1, -1<=c<=0, 0<d<1, e>=g>0, and H<=2. On the ground-truth trajectory write
\[
q=p_{y_{\mathrm{star}}},\quad m=p_{y_{\mathrm{med}}},\quad b=\sum_{z\in Y_{\mathrm{bad}}}p_z,\quad K=\sum_{z\in Y_{\mathrm{bad}}}p_z^2,
\]
with initial values q_0,m_0,b_0. Define
\[
\gamma=(q_0/M)^{14/13},\qquad h=\sqrt\gamma,\qquad x(t)=g-V_{r_G}(\theta_t^G),\qquad A_0=a-V_{r_G}(\theta_0).
\]
The initialization assumptions give
\[
0<\gamma<\min\{0.01,(21/(1100H))^{7/3},e^2\},
\]
\[
q_0=M\gamma^{13/14}\le\gamma^{13/14},\qquad
q_0\le\frac{g^{2/7}}{20H}\gamma^{13/14},\qquad
\max\{2h/e,0.05g\}\le b_0\le0.1g.
\]
Consequently m_0=1-q_0-b_0>0.8. Since all bad rewards equal c,
\[
V_{r_G}=g+dq-eb,\qquad x=eb-dq,
\]
so
\[
x(0)\ge2h-dq_0>h,\qquad x(0)\le eb_0\le0.1e<\tfrac12 e m_0^2.
\]
Also d<A_0=d+x(0)<=H. The advantages are
\[
A_{\mathrm{star}}=d+x,\qquad A_{\mathrm{med}}=x,\qquad A_{\mathrm{bad}}=x-e.
\]
Here x is nonincreasing, and x<e at every finite time because V_{r_G}>c.

If t_epsilon is infinite, the desired lower bound is immediate. For the rest of this part assume it is finite. By continuity there are finite first times s and tau at which x=h and x=gamma, respectively, and
\[
0<s<\tau<t_\varepsilon.
\]
The probability equations give
\[
\dot b=(x-e)K(1-b)-b\{q^2(d+x)+m^2x\}<0\quad\text{whenever }x>0,
\]
\[
\frac{\dot q}{q}=q(1-q)(d+x)-m^2x+(e-x)K,
\]
\[
\frac{\dot m}{m}=m(1-m)x-q^2(d+x)+(e-x)K.
\]
In particular, whenever x>0 and dot q<0, the identity dot m=-dot q-dot b gives dot m>0.

### Monotonicity up to s

Suppose there were a first time v in [0,s] with dot q(v)>=0. Before v, q decreases and m increases; hence at v, q<=q_0 and m>=m_0. Also x>=h. Since gamma<=0.01 implies 2 gamma^(3/7)<0.3, we have dq<=0.3x and therefore
\[
b=(x+dq)/e\le1.3x/e.
\]
Using x<=x(0)<=e m_0^2/2 yields
\[
e b^2\le\frac{1.69x^2}{e}\le\frac{1.69}{2}m_0^2x<\frac78m_0^2x.
\]
Since K<=b^2 and d+x<=A_0,
\[
\frac{\dot q(v)}{q(v)}\le q_0A_0-\frac18m_0^2h<0.
\]
The last strict inequality follows from
\[
q_0A_0\le\frac{g^{2/7}}{20}\gamma^{13/14}
\le\frac1{20}h\gamma^{3/7}<\frac{0.8^2}{8}h\le\frac18m_0^2h.
\]
This contradicts the definition of v, including the possibility v=0. Thus dot q<0 and dot m>0 on [0,s]. In particular, q<=q_0, m>=m_0, and b<=b_0<=0.1 there.

### Quantitative derivative bounds on [0,s]

We now prove
\[
\dot q\le-0.3qm^2x,\qquad
0<\dot m\le2.1m^2(1-m)x.
\]
First note that e-x=em+Hq and eb=x+dq>=h. Using the equation for q and K<=b^2,
\[
\frac{\dot q}{q}+0.3m^2x
\le eb(-0.7m^2+bm)+q_0(0.7m^2d+Hb^2+d+x).
\]
Because b<=0.5m, the first term is at most -0.2ebm^2. The bracket in the second term is at most 2H. Furthermore,
\[
\gamma^{3/7}<\frac{21}{1100H}\le\frac{m_0^2}{10H},\qquad
q_0\le\frac{h m_0^2}{10H}.
\]
Thus 2Hq_0<=0.2hm_0^2<=0.2ebm^2, proving the bound on dot q.

For m, the negative optimal-output term can be discarded, giving
\[
\dot m\le m(1-m)\{mx+(e-x)b\}.
\]
To bound the last term, calculate
\[
1.1mx-(e-x)b=0.1emb-q(1.1md+Hb).
\]
Here b<=0.4m, so 1.1md+Hb<=1.5mH. Also
\[
q\le q_0\le h\gamma^{3/7}\le\frac{h}{50H},
\]
because 21/1100<1/50. It follows that q(1.1md+Hb)<=0.03mh<=0.1emb. Hence (e-x)b<=1.1mx, proving the asserted bound on dot m.

### Small optimal probability at s

The preceding inequalities imply
\[
\frac{\dot q}{q}\le-\frac{\dot m}{7(1-m)}
=\frac17\frac{d}{dt}\log(1-m).
\]
All denominators are positive. Integrating gives
\[
q(s)\le q_0\left(\frac{1-m(s)}{1-m_0}\right)^{1/7}.
\]
At s, the reward equality and c<=0, a<=1 give
\[
g-h=gm(s)+aq(s)+cb(s)\le gm(s)+q_0,
\]
so 1-m(s)<=(h+q_0)/g<=1.3h/g. Since 1-m_0>=b_0>=0.05g,
\[
q(s)\le Q:=q_0\left(\frac{26h}{g^2}\right)^{1/7}
\le\frac{26^{1/7}}{20H}\gamma
<\frac{m_0^2\gamma}{8A_0}.
\]
For the strict comparison, 26^(1/7)/20<0.08, m_0^2>=0.64, and A_0<=H. The same estimate gives dQ<0.3gamma.

### Monotonicity from s to tau and endpoint concentration

If v in [s,tau] were the first subsequent time with dot q(v)>=0, then q(v)<=q(s)<=Q, m(v)>=m_0, and x(v)>=gamma. Thus dq(v)<0.3x(v). Exactly as above,
\[
b(v)\le1.3x(v)/e,\qquad e b(v)^2<\frac78m_0^2x(v),
\]
and therefore
\[
\frac{\dot q(v)}{q(v)}\le q(s)A_0-\frac18m_0^2\gamma<0,
\]
a contradiction. Hence q decreases and m increases throughout [0,tau], and
\[
q(\tau)\le\frac{m_0^2\gamma}{8A_0}\le\frac{\gamma}{8d}.
\]
At tau, V_{r_G}=g-gamma. Therefore, putting u_tau=1-m(tau),
\[
g u_\tau=\gamma+a q(\tau)+c b(\tau)
\le\gamma+q(\tau),
\]
which yields the required endpoint estimate
\[
u_\tau\le\frac{(1+8d)\gamma}{8dg}.
\]
This concentration estimate is asserted at tau, not throughout [0,tau].

## step_004: Escape-time lower bound

For any parameter vector, the three advantage expressions and the triangle inequality give
\[
\|\nabla V_{r_G}\|
\le2\{q(1-q)d+b(1-b)e\}
\le2H(q+b)=2H(1-m).
\]
For example, the first inequality follows by bounding |A_med|=|eb-dq| by eb+dq and collecting the coefficients of d and e in q A_star+m|A_med|+b|A_bad|.

Let u(t)=1-m(t)>0 on the ground-truth trajectory, now for t>=tau. Orthonormality gives, for every y,
\[
\|\phi(y)-\bar\phi\|^2=(1-p_y)^2+\sum_{z\ne y}p_z^2\le2.
\]
Summing the probability gradients over y different from y_med therefore shows
\[
\dot u\le\sqrt2 u\|\nabla V_{r_G}\|\le k u^2,\qquad k=2\sqrt2 H.
\]
Since u is positive and continuously differentiable, direct integration of (1/u)' >= -k gives
\[
u(t)\le\frac{u_\tau}{1-ku_\tau(t-\tau)}
\quad\text{when }ku_\tau(t-\tau)<1.
\]
For such t, the gradient bound yields
\[
\begin{aligned}
\|\theta_t^G-\theta_\tau^G\|
&\le2H\int_\tau^t u(v)\,dv\\
&\le2H\int_0^{t-\tau}\frac{u_\tau}{1-ku_\tau v}\,dv\\
&=\frac1{\sqrt2}\log\frac1{1-ku_\tau(t-\tau)}.
\end{aligned}
\]
The second transition is an inequality, correcting the equality sign at source L002765. The restriction on the denominator is retained throughout.

At a finite t_epsilon, continuity gives
\[
V_{r_G}(\theta_{t_\varepsilon}^G)-V_{r_G}(\theta_\tau^G)
=d-\varepsilon+\gamma\ge d-\varepsilon.
\]
If ku_tau(t_epsilon-tau)>=1, then immediately
\[
t_\varepsilon-\tau\ge\frac1{ku_\tau}\ge\frac{1-e^{-\sqrt2(d-\varepsilon)}}{ku_\tau}.
\]
Otherwise the 1-Lipschitz property from step_001 and the logarithmic displacement bound imply the same final inequality by exponentiation. Consequently, in both cases,
\[
\begin{aligned}
t_\varepsilon
&\ge\frac{1-e^{-\sqrt2(d-\varepsilon)}}{2\sqrt2 H u_\tau}\\
&\ge\frac{2\sqrt2 dg(1-e^{-\sqrt2(d-\varepsilon)})}{H(1+8d)\gamma}\\
&=\frac{2\sqrt2 M^{14/13}dg(1-e^{-\sqrt2(d-\varepsilon)})}{H(1+8d)}q_0^{-14/13}.
\end{aligned}
\]
This is the stated lower bound. The infinite-hitting-time case was already covered.

## step_005: Proxy upper bound, probability guarantee, and separation

For the remainder, probabilities refer to the proxy trajectory. All nonoptimal outputs have proxy reward c, while the optimal reward is a. Therefore
\[
V_{r_P}=a-H(1-q),\qquad A_{\mathrm{star}}^P=H(1-q),\qquad A_y^P=-Hq\quad(y\ne y_{\mathrm{star}}).
\]
In particular,
\[
A_0^P:=r_P(y_{\mathrm{star}})-V_{r_P}(\theta_0)=H(1-q_0)>0.
\]
The correct probability equation gives
\[
\dot q=Hq^2\left((1-q)^2+\sum_{y\ne y_{\mathrm{star}}}p_y^2\right)>0.
\]

Define privately
\[
\sigma=\inf\{t\ge0:V_{r_P}(\theta_t^P)\ge a-\varepsilon\},\qquad
\rho=1-\frac{\varepsilon}{a+1}\in(0,1).
\]
Because r_P<=r_G pointwise, t_epsilon^{no-med}<=sigma whenever sigma is finite. Initially V_{r_P}(theta_0)<=V_{r_G}(theta_0)<g<a-epsilon. Moreover,
\[
V_{r_P}(\theta_t^P)\ge(a+1)q(t)-1,
\]
so q>=rho implies V_{r_P}>=a-epsilon. Hence q_0<rho and q(t)<rho for t<sigma.

For t<sigma, A_star^P(t)>epsilon and A_0^P<=a+1, so
\[
A_{\mathrm{star}}^P(t)\ge(1-\rho)A_0^P.
\]
Discarding the nonnegative contributions of nonoptimal outputs in the equation for dot q then gives
\[
\dot q\ge q^2(1-q)A_{\mathrm{star}}^P(t)
\ge c_0 q^2,\qquad
c_0=(1-\rho)^2 A_0^P=\frac{\varepsilon^2 A_0^P}{(a+1)^2}>0.
\]
For t<sigma, integration yields
\[
\frac1{q(t)}\le\frac1{q_0}-c_0t.
\]
Set
\[
S=\frac1{c_0}\left(\frac1{q_0}-\frac1\rho\right)>0.
\]
If sigma>S, the reciprocal inequality at S implies q(S)>=rho, contradicting the definition of sigma. Thus
\[
t_\varepsilon^{\mathrm{no\text{-}med}}\le\sigma\le S<\frac1{c_0q_0}=U_\varepsilon.
\]
This also proves finiteness rather than assuming convergence of the proxy trajectory.

Along the proxy flow, V_{r_P} is nondecreasing. Hence, for every t>=U_epsilon>=sigma,
\[
H(1-q(t))=a-V_{r_P}(\theta_t^P)\le\varepsilon,
\]
which proves the stated probability guarantee. The argument does not replace sigma or U_epsilon by the possibly earlier ground-truth hitting time.

Finally, fix Y, phi, r_G, and epsilon. The lower-bound constant C is strictly positive and independent of theta_0. For q_0<=1/2,
\[
A_0^P=H(1-q_0)\ge H/2,
\qquad
U_\varepsilon\le K_0q_0^{-1},\quad K_0=\frac{2(a+1)^2}{\varepsilon^2H}.
\]
Therefore, with the stated extended-real convention if necessary,
\[
t_\varepsilon-t_\varepsilon^{\mathrm{no\text{-}med}}
\ge Cq_0^{-14/13}-K_0q_0^{-1}
=q_0^{-14/13}(C-K_0q_0^{1/13})\longrightarrow+\infty.
\]
The bound is uniform over the other admissible initial probabilities. Admissible arbitrarily small q_0 exist: choose b_0=0.075g, distribute it positively among the bad outputs, and set m_0=1-q_0-b_0. All initialization inequalities hold for sufficiently small positive q_0. Any such positive probability vector is realized by theta_0=sum_y log(p_y) phi(y), using orthonormality. This completes every claimed conclusion.
