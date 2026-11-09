# Reference Proof

## Proof Structure

1. Zero MMD with the characteristic Gaussian kernel implies equality of the transported independent coupling and the Bayesian joint coupling.
2. Test this joint-measure equality with products of bounded continuous functions of state and observation, then disintegrate with respect to the observation marginal.
3. Use a countable measure-determining class of state tests to identify the conditional push-forward measure for almost every observation.

## Audited Background Facts

The Gaussian characteristic property used here is the following standard independent result: for a Gaussian kernel with finite positive bandwidth on a finite-dimensional Euclidean space, zero kernel MMD between two Borel probability measures implies equality of those measures. No moment or absolute-continuity hypothesis is needed. The public task explicitly assumes characteristicness, and both measures to which it is applied below are Borel probability measures on the specified joint Euclidean space.

The bounded-continuous identification result states that Borel probability measures on a Euclidean space are equal if their integrals agree for every bounded continuous function. It also implies that a finite signed Borel measure integrating every bounded continuous function to zero is zero: the constant test gives equal total masses of its positive and negative parts, and, when that mass is positive, normalization reduces the assertion to probability-measure identification. If the mass is zero, both parts are zero.

## Complete Proof

Let $P=\pi_x\otimes\pi_y$. The measurable push-forward $T\#P$ and the given joint law $Q$ are Borel probability measures on $X\times Y$. A Gaussian kernel is bounded, and the reproducing inequality bounds every RKHS unit-ball function by $\sqrt{k(z,z)}$, so the MMD integrals are finite. By assumption,
\[
\operatorname{MMD}_k(T\#P,Q)=0.
\]
The characteristic property therefore gives
\[
T\#P=Q. \tag{1}
\]

Fix bounded continuous functions $f$ on the state space and $h$ on the observation space. Since $T(x,y)=(T_x(x,y),y)$, applying (1) to the product test function $(u,v)\mapsto f(u)h(v)$ yields
\[
\int h(y)f(T_x(x,y))\,\pi_x(dx)\pi_y(dy)
=\int h(y)\left[\int f(u)\,\pi_{x\mid y}(du\mid y)\right]\pi_y(dy).
\]
Define
\[
a_f(y)=\int f(T_x(x,y))\,\pi_x(dx),\qquad
b_f(y)=\int f(u)\,\pi_{x\mid y}(du\mid y).
\]
Joint measurability of $T_x$, measurability of the posterior kernel, and boundedness of $f$ imply that these are bounded measurable functions. Boundedness also justifies the preceding iterated integrals. The identity says
\[
\int h(y)(a_f(y)-b_f(y))\,\pi_y(dy)=0
\]
for every bounded continuous $h$. The finite signed Borel measure with density $a_f-b_f$ with respect to $\pi_y$ is consequently zero by the audited identification fact. Hence
\[
a_f(y)=b_f(y)
\quad\text{for }\pi_y\text{-almost every }y.
\]
Here the observation is held fixed in the prior integral defining $a_f(y)$; it is not averaged over $\pi_y$.

For completeness, construct a countable measure-determining family explicitly. If $d_x\geq1$, let $R=\prod_{i=1}^{d_x}(r_i,s_i)$ range over bounded open rectangles with rational endpoints $r_i<s_i$, and for each positive integer $n$ set
\[
f_{R,n}(u)=\prod_{i=1}^{d_x}\min\{1,n(u_i-r_i)_+,n(s_i-u_i)_+\},
\qquad t_+=\max\{t,0\}.
\]
These are bounded continuous functions, and $f_{R,n}\uparrow\mathbf 1_R$ as $n\to\infty$. The family $\mathcal F=\{f_{R,n}\}$ is countable. If $d_x=0$, take $\mathcal F=\{1\}$; the state space then has only one probability measure.

For each $f\in\mathcal F$, the equality $a_f=b_f$ holds on a measurable full-measure set. Intersect these countably many sets to obtain $Y_0$ with $\pi_y(Y_0)=1$. For every $y\in Y_0$ and $f\in\mathcal F$,
\[
\int f\,d\bigl(T_x(\cdot,y)\#\pi_x\bigr)
=\int f\,d\pi_{x\mid y}(\cdot\mid y).
\]
Each section $T_x(\cdot,y)$ is measurable, so its push-forward is a Borel probability measure. For $d_x\geq1$, monotone convergence gives equality of these two measures on every rational open rectangle. Such rectangles, together with the empty set and $X$, form a generating pi-system for the Borel sigma-algebra. Uniqueness of finite measures on a generating pi-system therefore gives equality on every Borel set. For $d_x=0$, equality is automatic.

Thus
\[
T_x(\cdot,y)\#\pi_x=\pi_{x\mid y}(\cdot\mid y)
\quad\text{for every }y\in Y_0,
\]
which is the required conclusion for $\pi_y$-almost every observation.

## Source Repair Notes

The proof uses the Gaussian kernel's characteristic property, not uniform density of its RKHS in all of $C_b$ on the noncompact joint domain. It also retains the observation as a fixed parameter in the prior integral, correcting the source's dropped conditioning. The countable determining family makes the common full-measure set explicit. These are local repairs; no substantive hypothesis or conclusion is changed.
