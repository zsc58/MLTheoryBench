# Reference Proof

## Proof Structure

Express the objective on the finite simplex, establish existence and convexity, characterize every minimizer using KKT conditions, derive the normalization equation, prove existence and uniqueness of its positive root, and verify that the resulting distribution satisfies sufficient conditions for global optimality.

## Complete Proof

### 1. Simplex formulation and existence

Index the realization set by $i=1,\ldots,K$, and put $a=e^\beta>0$. The assumptions $q_i\ge0$ and $\sum_i q_i=1$ imply $K\ge1$ and $q_*:=\max_i q_i>0$.

For $r_i>0$,
\[
\operatorname{softplus}(\beta+\log r_i)=\log(1+a r_i).
\]
The right side is also zero at $r_i=0$, agreeing with the specified continuous extension. Thus
\[
F_\beta(r)=-\sum_{i=1}^K q_i\log(1+a r_i)
\]
on the simplex $\Delta_K=\{r\in\mathbb R^K:r_i\ge0,\ \sum_i r_i=1\}$. This objective is continuous on the nonempty compact simplex, so it attains its minimum.

### 2. Convexity and the applicable KKT theorem

The objective is differentiable on the open convex set $\{r:r_i>-a^{-1}\text{ for all }i\}$, which contains the simplex. Its Hessian is diagonal, with entries
\[
\frac{q_i a^2}{(1+a r_i)^2}\ge0.
\]
It is therefore convex.

We use the standard differentiable convex KKT theorem in the following form: for minimization of a differentiable convex function subject to affine equalities and affine inequalities, a feasible point satisfying all inequalities strictly guarantees that every minimizer admits multipliers satisfying stationarity, dual feasibility, and complementary slackness. Conversely, any feasible point with such multipliers is a global minimizer. Here $r_i=1/K$ satisfies the equality and all inequalities $-r_i<0$, including when $K=1$, so the hypotheses for necessity hold.

### 3. Characterization of every minimizer

For any minimizer, introduce the Lagrangian
\[
F_\beta(r)+\zeta\left(\sum_i r_i-1\right)-\sum_i\nu_i r_i.
\]
KKT gives
\[
-\frac{q_i a}{1+a r_i}+\zeta-\nu_i=0,
\qquad \nu_i\ge0,\qquad \nu_i r_i=0.
\]
Before dividing by $\zeta$, choose $j$ with $q_j>0$. Stationarity gives
\[
\zeta=\frac{q_j a}{1+a r_j}+\nu_j>0.
\]
If $r_i>0$, complementary slackness gives $\nu_i=0$, and hence
\[
r_i=\frac{q_i}{\zeta}-a^{-1}>0.
\]
If $r_i=0$, stationarity gives $\zeta\ge a q_i$, so $q_i/\zeta-a^{-1}\le0$. Therefore every minimizer satisfies
\[
r_i=\left(\frac{q_i}{\zeta}-a^{-1}\right)_+.
\]
This derivation includes $q_i=0$ without dividing by $q_i$ or by $\zeta-\nu_i$.

### 4. Normalization and the cutoff equation

Set $\tau=a^{-1}\zeta>0$. Then
\[
r_i=\frac{a^{-1}}{\tau}(q_i-\tau)_+.
\]
Normalization implies
\[
\tau=a^{-1}\sum_i(q_i-\tau)_+.
\]
Moreover, $\tau<q_*$, since otherwise all displayed masses would be zero.

### 5. Existence and uniqueness of the cutoff

Define
\[
b(t)=\sum_i(q_i-t)_+,
\qquad h_\beta(t)=t-a^{-1}b(t).
\]
Each hinge function is continuous and nonincreasing, so $b$ has these properties. Also $b(0)=1$ and $b(q_*)=0$. Consequently
\[
h_\beta(0)=-a^{-1}<0,
\qquad h_\beta(q_*)=q_*>0.
\]
By the intermediate value theorem, a continuous real function with opposite signs at the endpoints has a zero between them. Applying it here gives a root in $(0,q_*)$.

For $t_2>t_1$,
\[
h_\beta(t_2)-h_\beta(t_1)
=(t_2-t_1)+a^{-1}\bigl(b(t_1)-b(t_2)\bigr)>0.
\]
Thus $h_\beta$ is strictly increasing and the root is unique. This reasoning does not require distinct or strictly positive empirical masses.

### 6. Converse verification and global optimality

Let $\tau$ be that unique root and define
\[
r_i=\frac{a^{-1}}{\tau}(q_i-\tau)_+,
\qquad \zeta=a\tau,
\qquad \nu_i=(\zeta-aq_i)_+.
\]
The root equation gives $\sum_i r_i=1$, and all masses and inequality multipliers are nonnegative.

If $q_i>\tau$, then $r_i>0$, $\nu_i=0$, and
\[
1+a r_i=\frac{q_i}{\tau},
\qquad \frac{q_i a}{1+a r_i}=a\tau=\zeta.
\]
If $q_i\le\tau$, then $r_i=0$ and $\nu_i=\zeta-aq_i\ge0$. In both cases stationarity and complementary slackness hold, including at $q_i=\tau$ and $q_i=0$.

KKT sufficiency proves global optimality. Explicitly, for any feasible $s$, convexity and stationarity give
\[
F_\beta(s)\ge F_\beta(r)+\nabla F_\beta(r)\cdot(s-r)
=F_\beta(r)+\sum_i\nu_i s_i\ge F_\beta(r),
\]
where normalization cancels the $\zeta$ term and complementarity gives $\sum_i\nu_i r_i=0$.

Every minimizer has the formula from Steps 3–4, and the cutoff is unique, so the minimizing distribution is unique and has exactly the required form. Its masses are the normalized positive parts of $q_i-\tau$: one subtracts the cutoff, truncates at zero, and normalizes. This is not, in general, the same as retaining the original $q_i$ on the surviving coordinates and only normalizing them.

## Private Source-Repair Notes

The source quotient $q_i/(\zeta-\nu_i)$ is undefined when both numerator and denominator vanish; Step 3 instead uses undivided stationarity. In the source's sorted-piece proof of continuity, the coefficient in the left-limit expression must be $K-k+1$, not $K-k-1$. Step 5 proves continuity directly from the finite sum of hinge functions. These are local proof repairs, not changes to the theorem. The previously recorded cutoff-theorem notation repair remains in force.
