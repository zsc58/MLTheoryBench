# Reference Proof

## Proof Structure

1. Establish the bounded smoothness supplied by the explicit attention map on compact parameter and input sets. Differentiate the logits using fixed feature-coordinate tests in the weak equation, and derive energy dissipation without assuming a measure-space chain rule.
2. Prove the two-sided stationary characterization, including the support formulation, without requiring strict positivity of the learning rate.
3. Derive continuity of the dissipation and a quantitative continuity estimate for the trajectory. Construct accumulated-time dynamics even when the learning rate vanishes, prove vanishing dissipation by an elementary integrability argument, and identify all omega-limit points as stationary.
4. Establish the nonempty compact connected omega-limit set and deduce full convergence under the stated total-disconnectedness hypothesis.

## Complete Proof

### 1. Regularity, first variation, and energy dissipation

Choose a closed parameter ball containing $H$. After removing masked entries, each attention row is a finite softmax over a nonempty set, since the diagonal entry is unmasked. Its denominator is positive. The attention formula consists of polynomial operations and smooth finite softmax operations, with a fixed matrix $W_{\rm out}$. Consequently its parameter derivatives are continuous, and compactness of the parameter ball and $H_x^L$ gives finite constants $B_m$ such that
\[
\sup_{X\in H_x^L,\,l,\,\theta\text{ in the ball}}
\|D_\theta^m\psi_l(X;\theta)\|\le B_m,\qquad m=0,1,2,3.
\]
Here $D^0\psi=\psi$, vector norms are Euclidean, and derivative norms are operator norms. This establishes the source's uniform smoothness assumption from the stated concrete model and compact support; no additional public regularity assumption is needed. In particular, the derivative bounds also hold along every line segment joining points of $H$.

Write
\[
J_l(X;\theta)=D_\theta\psi_l(X;\theta),\qquad
r_l^\rho(X)=\operatorname{softmax}(z_l^\rho(X))-Y_l(X),\qquad
g(\theta,\rho)=\nabla_\theta\Phi(\theta;\rho).
\]
The probability vector and one-hot label both have Euclidean norm at most one, so $\|r_l^\rho(X)\|\le2$. Differentiation under the expectation is justified by the uniform derivative bounds and gives
\[
g(\theta,\rho)=\mathbb E_X\left[\frac1L\sum_lJ_l(X;\theta)^\top r_l^\rho(X)\right],
\qquad \|g(\theta,\rho)\|\le G:=2B_1.
\]
Likewise, differentiation along $(1-\varepsilon)\rho+\varepsilon\nu$ gives
\[
\left.\frac d{d\varepsilon}\mathcal E((1-\varepsilon)\rho+\varepsilon\nu)\right|_{\varepsilon=0+}
=\int_H\Phi(\theta;\rho)(\nu-\rho)(d\theta).
\]
All logits have norm at most $B_0$. For one-hot $y$, cross-entropy satisfies
\[
0\le\ell(y,z)\le\log c+2B_0\quad\text{when }\|z\|\le B_0.
\]
Thus every risk in the argument is a finite real number.

For a fixed input $X$, token index $l$, and feature coordinate, use that coordinate of $\psi_l(X;\cdot)$ as a fixed $C^1$ test function in the integrated weak equation. This gives an absolutely continuous logit curve with
\[
\frac d{dt}z_l^{\rho_t}(X)
=-2\zeta(t)\int_H J_l(X;\theta)g(\theta,\rho_t)\,\rho_t(d\theta)
\]
for almost every $t$. Its derivative is bounded in norm by $2\zeta(t)B_1G$, uniformly in $X,l$. The ordinary finite-dimensional chain rule for $\ell$ and this domination justify the chain rule under $\mathbb E_X$. Fubini's theorem is applicable because all integrands are bounded on every finite time interval. Therefore
\[
\begin{aligned}
\frac d{dt}\mathcal E(\rho_t)
&=\mathbb E_X\left[\frac1L\sum_l\left\langle r_l^{\rho_t}(X),\frac d{dt}z_l^{\rho_t}(X)\right\rangle\right]\\
&=-2\zeta(t)\int_H\left\langle
\mathbb E_X\left[\frac1L\sum_lJ_l(X;\theta)^\top r_l^{\rho_t}(X)\right],g(\theta,\rho_t)\right\rangle\rho_t(d\theta)\\
&=-2\zeta(t)\mathcal I(\rho_t).
\end{aligned}
\]
Initially this is an almost-everywhere identity, with the integrated identity
\[
\mathcal E(\rho_b)-\mathcal E(\rho_a)
=-\int_a^b2\zeta(t)\mathcal I(\rho_t)\,dt
\tag{A}
\]
for every finite interval. The dissipation continuity proved below also makes the differential identity valid at every positive time, with a right derivative at zero.

Since $\zeta\ge0$ and $\mathcal I\ge0$, the risk is non-increasing. Its lower bound zero and finite initial value give a finite limit $\mathcal E_\infty\ge0$.

### 2. Stationary measures

If $\bar\rho$ is stationary, apply (A) to its constant trajectory. Since $\int_0^\infty\zeta(t)\,dt=\infty$, there is a finite $T$ for which $\int_0^T\zeta(t)\,dt>0$. Thus
\[
0=-2\mathcal I(\bar\rho)\int_0^T\zeta(t)\,dt,
\]
so $\mathcal I(\bar\rho)=0$. A nonnegative squared norm has zero integral exactly when $g(\theta,\bar\rho)=0$ for $\bar\rho$-almost every $\theta$.

Conversely, if this almost-sure vanishing holds, the right-hand side of the integrated weak equation for the constant curve is zero for every test function and every interval. Hence the constant curve is a weak solution.

The function $\theta\mapsto g(\theta,\bar\rho)$ is continuous by the uniform feature derivative bounds and dominated convergence. If it did not vanish at some point of $\operatorname{supp}\bar\rho$, continuity would give a neighborhood on which its norm is bounded below by a positive number, and that neighborhood has positive $\bar\rho$ mass. This contradicts almost-sure vanishing. The converse follows because a Borel probability measure on Euclidean space gives full mass to its support. This proves both stationary formulations, including measures supported on the boundary of $H$; the equation uses ambient gradients, not projected or reflected gradients.

### 3. Dissipation continuity and vanishing dissipation

First derive the continuity that was only asserted in the original reference proof. For $p=\operatorname{softmax}(z)$,
\[
D\operatorname{softmax}(z)=\operatorname{diag}(p)-pp^\top.
\]
For a vector $u$, the associated quadratic form is the variance of the values $u_j$ under probabilities $p_j$. Centering at the midpoint of their minimum and maximum shows that this variance is at most $(\max_j u_j-\min_j u_j)^2/4\le\|u\|^2/2$. Hence softmax is $1/2$-Lipschitz.

The feature derivative bounds give
\[
\|\psi_l(X;\theta)-\psi_l(X;\eta)\|\le B_1\|\theta-\eta\|,
\qquad
\|J_l(X;\theta)-J_l(X;\eta)\|\le B_2\|\theta-\eta\|.
\]
Integrating the first inequality against any coupling and taking the infimum yields
\[
\|z_l^\rho(X)-z_l^\nu(X)\|\le B_1W_1(\rho,\nu).
\]
Consequently
\[
\|g(\theta,\rho)-g(\eta,\nu)\|
\le2B_2\|\theta-\eta\|+\tfrac12B_1^2W_1(\rho,\nu).
\tag{B}
\]
For any coupling of $\rho,\nu$, represent the difference of the two dissipation integrals on that coupling. Using $\|g\|\le G$, the difference-of-squares inequality, (B), and then the infimum over couplings gives
\[
|\mathcal I(\rho)-\mathcal I(\nu)|
\le C_IW_1(\rho,\nu),\qquad
C_I=2G\left(2B_2+\tfrac12B_1^2\right).
\tag{C}
\]
Thus dissipation is Lipschitz on $\mathcal P(H)$, not an assumed continuous quantity.

The standard independent Wasserstein fact used next is Kantorovich--Rubinstein duality: for Borel probability measures with finite first moments on Euclidean space,
\[
W_1(\rho,\nu)=\sup_{\operatorname{Lip}(f)\le1}\left|\int f\,d(\rho-\nu)\right|.
\]
All its hypotheses hold here because the measures have common compact support. Smooth convolution approximations of a globally $1$-Lipschitz function remain $1$-Lipschitz and converge uniformly on $H$. Thus bounds established for smooth $1$-Lipschitz tests extend to every test in this dual formula.

For such a smooth test, the weak equation and $\|g\|\le G$ give, for $0\le u\le t$,
\[
\left|\int f\,d(\rho_t-\rho_u)\right|
\le2G\int_u^t\zeta(r)\,dr.
\]
Define $s(t)=2\int_0^t\zeta(r)\,dr$. Duality therefore yields
\[
W_1(\rho_t,\rho_u)\le G\bigl(s(t)-s(u)\bigr).
\tag{D}
\]
The function $s$ is continuous, nondecreasing, and unbounded, and maps $[0,\infty)$ onto $[0,\infty)$. It need not be strictly increasing. If $s(t)=s(u)$, (D) gives $\rho_t=\rho_u$. Hence
\[
\widetilde\rho_s=\rho_t\quad\text{for any }t\text{ with }s(t)=s
\]
is well defined. Again by (D), this curve is $G$-Lipschitz in $W_1$. By (C), the function $h(s)=\mathcal I(\widetilde\rho_s)$ is nonnegative and Lipschitz, hence uniformly continuous.

Let $F(s)=\int_0^s h(v)\,dv$. Since $h$ is continuous, the ordinary chain rule gives
\[
\frac d{dt}F(s(t))=2\zeta(t)h(s(t))
\]
even at times when $\zeta(t)=0$. Applying (A) and the surjectivity of $s$ gives
\[
\mathcal E(\widetilde\rho_s)=\mathcal E(\rho_0)-\int_0^s h(v)\,dv.
\]
As $t\to\infty$, also $s(t)\to\infty$. It follows that
\[
\int_0^\infty h(v)\,dv=\mathcal E(\rho_0)-\mathcal E_\infty<\infty.
\]
To prove $h(s)\to0$ without leaving a named-lemma obligation, suppose instead that $h(s_n)\ge\varepsilon>0$ for some $s_n\to\infty$. Uniform continuity gives a common positive interval length on which $h$ remains at least $\varepsilon/2$ after each $s_n$. Choose a subsequence so these intervals are disjoint. Their integrals then have an infinite sum, contradicting integrability. Therefore $h(s)\to0$, and hence $\mathcal I(\rho_t)=h(s(t))\to0$.

If $t_n\to\infty$ and $\rho_{t_n}\to\bar\rho$ in $W_1$, (C) implies $\mathcal I(\bar\rho)=0$. The stationary characterization proves $\bar\rho\in\mathsf{Stat}$.

### 4. Omega-limit geometry and full convergence

Let $\mathcal K$ be the compact $W_1$ closure of the trajectory. For each positive integer $n$, set
\[
C_n=\overline{\{\rho_t:t\ge n\}}^{\,W_1}.
\]
These are nonempty nested compact subsets of $\mathcal K$. Moreover,
\[
\Omega=\bigcap_{n\ge1}C_n.
\]
Indeed, an omega-limit point lies in every tail closure. Conversely, if a point belongs to every $C_n$, choose $t_n\ge n$ with distance less than $1/n$ from that point. This is the required sequence in the definition of $\Omega$. Compactness and nesting show the intersection is nonempty: a subsequential limit of any choices $\nu_n\in C_n$ belongs to every $C_m$. The intersection is also compact.

Each tail image is connected because $[n,\infty)$ is connected and the trajectory is $W_1$-continuous. Its closure $C_n$ is connected as well. For completeness, their nested intersection is connected: otherwise write $\Omega=A\cup B$ as two disjoint nonempty compact sets and choose disjoint open neighborhoods $U,V$ of $A,B$. Some $C_n$ must be contained in $U\cup V$; if not, points in $C_n\setminus(U\cup V)$ would have a subsequential limit in $\Omega\setminus(U\cup V)$ by compactness and nesting. But that $C_n$ contains both $A$ and $B$, so containment in the disjoint union would disconnect $C_n$, a contradiction. Thus $\Omega$ is connected. Step 3 already proved $\Omega\subseteq\mathsf{Stat}$.

If $\Omega\cap\mathsf{Stat}$ is totally disconnected, then $\Omega$, being nonempty and connected and contained in this intersection, is a singleton, say $\{\rho_\infty\}$. To obtain convergence of the entire trajectory, suppose that some $\varepsilon>0$ and $t_n\to\infty$ satisfy $W_1(\rho_{t_n},\rho_\infty)\ge\varepsilon$. Precompactness provides a convergent subsequence whose limit belongs to $\Omega$, hence equals $\rho_\infty$, a contradiction. Therefore $W_1(\rho_t,\rho_\infty)\to0$, with $\rho_\infty$ stationary.

All arguments allow $c=1$, a zero fixed output projection, vanishing derivative bounds, arbitrary compact supports, and learning-rate zero intervals. No positive lower bound on the learning rate, support interior condition, or existence of an ordinary inverse time map has been used.
