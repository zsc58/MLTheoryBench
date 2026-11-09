# Reference Proof

## Obligations

The proof must establish: (1) well-defined objectives, active sets, and objective subgradients; (2) the occupancy and performance-difference identities; (3) dominance for every active-gradient convex combination under each uniqueness alternative; (4) bounded subgradients and weak convexity; (5) the correctly scaled proximal objective-gap estimate; and (6) the stated rate for the specified projected-subgradient schedule. Each obligation is discharged below.

## 1. Objectives and subgradients

Write f=J_{\mathcal U}, q=1-\gamma, and \(\mu_{\min}=\min_s\mu(s)\). All vector norms and projections are Euclidean. The inverse \((I-\gamma P_\pi)^{-1}\) exists for every policy. Its dependence on the model and policy is continuous. Compactness therefore gives continuity of f, existence of an optimal policy, and nonempty compact active sets. Also \(0\le f\le M:=1/q\).

The same Bellman inverse defines a smooth fixed-model objective on a common neighborhood of \(\Pi\). Indeed, \(\|P_\pi\|_\infty=1\) on \(\Pi\), and a sufficiently small neighborhood keeps \(\gamma\|P_x\|_\infty<1\) uniformly over models. All relevant inverse derivatives are jointly continuous there.

Define the normalized state occupancy
\[
d_P^\pi(s)=q\sum_{h=0}^{\infty}\gamma^h\Pr_P^\pi(s_h=s),\qquad s_0\sim\mu.
\]
It is a probability vector, and \(d_P^\pi(s)\ge q\mu(s)>0\). Consequently, for any two policies and any kernel,
\[
\frac{d_P^\rho(s)}{d_P^\pi(s)}\le\frac1{q\mu(s)}\le D:=\frac1{q\mu_{\min}}.
\]

Differentiating \((I-\gamma P_\pi)V_u^\pi=c_\pi\) in coordinate \(\pi(a\mid s)\) gives
\[
\nabla J_u(\pi)(s,a)=\mu^\top(I-\gamma P_\pi)^{-1}e_s\,Q_u^\pi(s,a)
=\frac{d_P^\pi(s)}q Q_u^\pi(s,a).
\]
The compact smooth-max subdifferential formula therefore gives
\[
\partial f(\pi)=\operatorname{conv}\{\nabla J_u(\pi):u\in\mathcal U^\pi\}.
\]
For completeness, this smooth-max formula follows locally by adding a sufficiently large common quadratic to all indexed smooth functions, applying the convex maximum subdifferential formula, and subtracting the quadratic gradient. Compactness and the joint continuity verified above give the required active-set compactness and gradient continuity. The same argument shows local weak convexity and equality of the Clarke and Frechet subdifferentials. No normal cone is included in this objective subdifferential.

Every member of this convex hull is a finite convex combination of active gradients, including when the active model set is infinite. Thus fix any
\[
g=\sum_{i=1}^k\alpha_i\nabla J_{u_i}(\pi),\qquad \alpha_i\ge0,\quad\sum_i\alpha_i=1,\quad u_i=(c_i,P_i)\in\mathcal U^\pi.
\]

## 2. Performance difference and robust comparison

Let \(A_u^\pi(s,a)=V_u^\pi(s)-Q_u^\pi(s,a)\). Bellman's equation gives \(\sum_a\pi(a\mid s)A_u^\pi(s,a)=0\). Moreover,
\[
(I-\gamma P_\rho)(V_u^\pi-V_u^\rho)(s)
=\sum_a\rho(a\mid s)A_u^\pi(s,a).
\]
Multiplying by \(\mu^\top(I-\gamma P_\rho)^{-1}\) proves
\[
J_u(\pi)-J_u(\rho)=\frac1q\sum_s d_P^\rho(s)\sum_a\rho(a\mid s)A_u^\pi(s,a).
\]
For every active model, \(f(\pi)-f(\pi^*)\le J_u(\pi)-J_u(\pi^*)\). Hence, writing \(\Delta_\pi=f(\pi)-f(\pi^*)\),
\[
\Delta_\pi\le\frac1q\sum_i\alpha_i\sum_s d_{P_i}^{\pi^*}(s)\sum_a\pi^*(a\mid s)A_{u_i}^\pi(s,a). \tag{1}
\]
It is essential to retain the convex combination representing the arbitrary subgradient g; choosing a single active model would not prove dominance for all g.

## 3. Both uniqueness branches

### Common transition kernel

Suppose \(P^\pi=\{P\}\). Put \(B(s,a)=\sum_i\alpha_i A_{u_i}^\pi(s,a)\) and \(b(s)=\max_a B(s,a)\). Because the \(\pi\)-average of B is zero, \(b(s)\ge0\). Equation (1) and the occupancy ratio bound imply
\[
\Delta_\pi\le\frac1q\sum_s d_P^{\pi^*}(s)b(s)
\le\frac Dq\sum_s d_P^\pi(s)b(s).
\]
Set \(\overline Q(s,a)=\sum_i\alpha_iQ_{u_i}^\pi(s,a)\). Then
\[
B(s,a)=\sum_b\pi(b\mid s)\overline Q(s,b)-\overline Q(s,a),
\quad g(s,a)=\frac{d_P^\pi(s)}q\overline Q(s,a).
\]
Independent simplex maximization at each state yields
\[
\frac1q\sum_s d_P^\pi(s)b(s)=\max_{\rho\in\Pi}\langle\pi-\rho,g\rangle.
\]
Thus \(\Delta_\pi\le D\max_\rho\langle\pi-\rho,g\rangle\).

### Common action-value function

Suppose \(Q^\pi=\{Q\}\). All active advantages equal
\[
A(s,a)=\sum_b\pi(b\mid s)Q(s,b)-Q(s,a).
\]
Let \(b(s)=\max_a A(s,a)\ge0\). Equation (1) gives
\[
\Delta_\pi\le\frac1q\sum_s\sum_i\alpha_i d_{P_i}^{\pi^*}(s)b(s)
\le\frac Dq\sum_s\sum_i\alpha_i d_{P_i}^\pi(s)b(s).
\]
Since
\[
g(s,a)=\frac1q\left(\sum_i\alpha_i d_{P_i}^\pi(s)\right)Q(s,a),
\]
the last expression is \(D\max_{\rho\in\Pi}\langle\pi-\rho,g\rangle\).

In either branch the inequality holds for every g in the objective subdifferential. Taking its minimum gives
\[
f(\pi)-f(\pi^*)\le D G(\pi).
\]
The minimum exists because the active-gradient convex hull is compact and the maximized linear pairing is continuous in g. This proof also covers a single available action, when every policy gap is zero.

## 4. Lipschitzness and weak convexity

Since \(0\le Q_u^\pi\le1/q\) and \(\sum_s d_P^\pi(s)=1\),
\[
\|\nabla J_u(\pi)\|^2\le\frac{|A|}{q^4}\sum_s d_P^\pi(s)^2\le\frac{|A|}{q^4}.
\]
Therefore every objective subgradient satisfies \(\|g\|\le L:=\sqrt{|A|}/q^2\). Integrating fixed-model gradients along policy segments and taking maxima also gives \(|f(x)-f(y)|\le L\|x-y\|\) on \(\Pi\).

The standard fixed-model smoothness result used here has the following precise statement: for finite state and action spaces, costs in [0,1], discount \(\gamma<1\), an initial probability distribution, and direct policy parameters,
\[
\|\nabla J_u(x)-\nabla J_u(y)\|\le\ell\|x-y\|,
\qquad x,y\in\Pi,\quad \ell=\frac{2\gamma|A|}{q^3}.
\]
These hypotheses all hold in the present task. This is the audited standard-independent result theory_020, stated at source L000296-L000299. Its segment lower bound, averaged over active gradients, implies
\[
f(y)\ge f(x)+\langle g,y-x\rangle-\frac\ell2\|y-x\|^2,
\qquad g\in\partial f(x),\quad x,y\in\Pi. \tag{2}
\]
In particular f is \(\ell\)-weakly convex on \(\Pi\).

## 5. Correctly scaled Moreau domination

Define \(\bar f=f+\delta_\Pi\), where the indicator is zero on \(\Pi\) and infinity elsewhere, and
\[
E(x)=\min_{y\in\Pi}\{f(y)+\ell\|x-y\|^2\}.
\]
The minimized function is \(\ell\)-strongly convex in y, so it has a unique minimizer \(y_x\). The usual differentiable-minimum calculation, justified by uniqueness and compactness, gives
\[
v(x):=\nabla E(x)=2\ell(x-y_x).
\]
Proximal optimality supplies \(g_x\in\partial f(y_x)\) with \(v(x)-g_x\in N_\Pi(y_x)\). This follows either by convexifying f before applying the convex sum rule or directly from the locally Lipschitz objective and the convex constraint. Here \(N_\Pi(y)=\{n:\langle n,\rho-y\rangle\le0\text{ for all }\rho\in\Pi\}\). Consequently
\[
\langle g_x,y_x-\rho\rangle\le\langle v(x),y_x-\rho\rangle.
\]
Apply dominance at \(y_x\), not at x, and use \(\operatorname{diam}(\Pi)\le2\sqrt{|S|}\):
\[
f(y_x)-f(\pi^*)\le2D\sqrt{|S|}\,\|v(x)\|.
\]
For \(x\in\Pi\), Lipschitzness gives
\[
f(x)-f(y_x)\le L\|x-y_x\|=\frac{L}{2\ell}\|v(x)\|.
\]
Adding proves
\[
f(x)-f(\pi^*)\le D'\|\nabla E(x)\|,
\qquad D'=2D\sqrt{|S|}+\frac{\sqrt{|A|}}{2\ell q^2}. \tag{3}
\]
The reciprocal factor follows from the definition of E; replacing it by \(2\ell L\) is not valid uniformly over positive discounts.

## 6. PSD stationarity and objective convergence

We derive the needed stationarity result rather than relying on the inconsistent schedule in the source appendix. Set \(x=\pi_t\), \(y=y_x\), \(g=g_t\), and \(x^+=\operatorname{Proj}_\Pi(x-\eta g)\). Strong convexity of the proximal objective gives
\[
f(x)-f(y)\ge\frac{3\ell}{2}\|x-y\|^2.
\]
Together with (2), this implies
\[
\langle g,x-y\rangle\ge\ell\|x-y\|^2.
\]
Projection nonexpansiveness and the feasible comparison point y yield
\[
\begin{aligned}
E(x^+)&\le f(y)+\ell\|x^+-y\|^2\\
&\le E(x)-2\ell\eta\langle g,x-y\rangle+\ell\eta^2\|g\|^2\\
&\le E(x)-\frac\eta2\|\nabla E(x)\|^2+\ell\eta^2L^2.
\end{aligned}
\]
Sum over \(t=0,\ldots,T-1\). Since \(0\le E\) and \(E(\pi_0)\le f(\pi_0)\le M\),
\[
\min_{0\le t<T}\|\nabla E(\pi_t)\|^2
\le\frac{2M}{\eta T}+2\ell\eta L^2.
\]
For the prescribed \(\eta=1/\sqrt T\), this is at most
\[
\frac{4M+2\ell L^2}{\sqrt T}
=\frac1{\sqrt T}\left(\frac4{1-\gamma}+\frac{4\gamma|A|^2}{(1-\gamma)^7}\right).
\]
Combine its square root with (3) at an iterate minimizing the envelope-gradient norm. This proves the stated bound with the corrected D' and C.

For any \(\varepsilon>0\), taking an integer \(T\ge\max\{1,\lceil(C/\varepsilon)^4\rceil\}\) ensures an \(\varepsilon\)-optimal iterate among \(\pi_0,\ldots,\pi_{T-1}\). Selecting an iterate of minimum robust objective proves the claimed update complexity. The conclusion is an update count with exact subgradients; it makes no extra assertion about the computational cost of a worst-case-model oracle.

## Source corrections used

The main-text step size 1/sqrt(T) is retained. The earlier artifact's normalized step size is retracted. The appendix schedule mismatch is repaired by the explicit descent calculation above. The Moreau coefficient is corrected from 2ell L to L/(2ell), and dominance is applied at the proximal point. The smooth Danskin proof's indexing set is consistently Y. No unresolved theorem-critical proof obligation remains.
