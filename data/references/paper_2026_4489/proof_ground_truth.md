# Reference Proof

## Proof Structure

1. Establish the estimator's mean and variance under the fresh fixed-arm experiment.
2. Reduce variance minimization to the bounded mean-constrained objective J(pi)=E[g/pi].
3. Construct a budget-feasible clipped square-root rule, including endpoint budgets, zero residuals, and saturation.
4. Prove global optimality by an integrated pointwise inequality or pointwise saturation.
5. Construct bounded heterogeneous instances with an arbitrarily large uniform-audit variance ratio.

## Complete Proof

Write a=pi_min, R=Y-F, and
\[
Z_\pi=F+\frac{A}{\pi(X,F)}R.
\]
All relevant expectations are finite: |R|<=1 and pi>=a>0 imply |Z_pi|<=1+1/a. The independent fresh pulls and fresh audit randomization make the summands independent and identically distributed. Thus n Var(theta-hat_n)=Var(Z_pi)=V(pi).

### 1. Conditional moments and the variance objective

Let m(X,F)=E[R|X,F]. Ignorability and the specified propensity give
\[
E[AR/\pi\mid X,F]=m,
\qquad
E[(AR/\pi)^2\mid X,F]=g/\pi.
\]
In particular,
\[
\operatorname{Var}(AR/\pi\mid X,F)=g/\pi-m^2.
\]
It is important not to replace m^2 by g: Y need not be determined by (X,F).

Conditioning instead on (X,F,Y), the only remaining randomness is the audit coin, so
\[
E[Z_\pi\mid X,F,Y]=Y,
\qquad
\operatorname{Var}(Z_\pi\mid X,F,Y)
=(Y-F)^2(1/\pi-1).
\]
Taking expectations and using total variance yields
\[
E[Z_\pi]=\theta,
\qquad
V(\pi)=\operatorname{Var}(Y)+E[g(1/\pi-1)].
\]
Consequently the publicly defined audit-induced component satisfies
\[
B(\pi)=V(\pi)-\operatorname{Var}(Y)=E[g(1/\pi-1)]\geq0.
\]
Minimizing V is equivalent to minimizing
\[
J(\pi)=E[g/\pi],
\qquad a\leq\pi\leq1,\quad E\pi=\rho.
\]
These expectations are finite because 0<=g<=1 almost surely and a>0.

### 2. Endpoint and zero-residual cases

If rho=a, nonnegativity of pi-a and E(pi-a)=0 force pi=a almost surely. This is optimal and is represented on g>0 by c=0. If rho=1, the same argument applied to 1-pi forces pi=1 almost surely; c=infinity represents this on g>0. These cases include a=1.

If g=0 almost surely, J is identically zero, so every feasible policy is optimal. The constant policy rho is feasible, and the positive-g formula is vacuous.

It remains to consider a<rho<1 and r=P(g>0)>0. Put s=P(g=0)=1-r and
\[
b=r+as.
\]
This is the mean propensity obtained by fully auditing g>0 while using the lower bound on g=0.

### 3. Budgets below positive-stratum saturation

Suppose rho<b. For finite c>=0 define
\[
p_c=\max\{a,\min\{1,c\sqrt g\}\},
\qquad H(c)=E[p_c].
\]
Here p_c=a on g=0. The clipping function is 1-Lipschitz, and sqrt(g)<=1, so
\[
|H(c)-H(d)|\leq |c-d|.
\]
Thus H is continuous. It is nondecreasing, H(0)=a, and H(c) tends to b as c tends to infinity. For the last assertion, p_c tends pointwise to 1 on g>0 and remains a on g=0; bounded convergence applies because 0<=p_c<=1 on a probability space. The bounded-convergence fact used here is that uniformly bounded random variables converging almost surely have convergent expectations.

Because a<rho<b, a finite positive c with H(c)=rho exists by continuity. No uniqueness of c is needed. Set lambda=c^(-2)>0. For each fixed g>=0, the function
\[
p\longmapsto g/p+\lambda p,\qquad p\in[a,1],
\]
has its minimum at p_c. Indeed, for g>0 its derivative is -g/p^2+lambda and its second derivative is 2g/p^3>0, giving the clipped square-root minimum. For g=0 it is increasing and is minimized at a.

For any other feasible policy pi, integrate the pointwise minimum inequality:
\[
J(p_c)+\lambda E[p_c]
\leq J(\pi)+\lambda E[\pi].
\]
The expectations of both policies equal rho, so J(p_c)<=J(pi). This proves global optimality in this case.

### 4. Saturated budgets and the zero-residual stratum

Suppose rho>=b. Set pi*=1 on g>0. If s>0, choose the constant value
\[
\eta=\frac{\rho-r}{s}
\]
on g=0. Since rho>=r+as and rho<=r+s=1, this value belongs to [a,1], and the resulting policy has mean rho. If s=0, then b=1, so this case can only be the already handled rho=1 endpoint.

For every feasible pi, g/pi>=g pointwise. The constructed pi* attains equality because it is one wherever g>0. Therefore J(pi*)=E[g] is globally minimal. This policy is represented by c=infinity on g>0. The same argument includes rho=b, even if no finite c attains that mean.

On g=0 the objective contribution is zero. Any measurable replacement of the zero-stratum values within [a,1] that preserves their required total budget leaves feasibility and optimality unchanged. In the nonsaturated case the construction uses the lower bound there; arbitrary spending on zero residuals before saturation is not justified by the Lagrange argument.

Together the cases prove existence of the asserted optimizer for every permitted budget. They do not assert that every feasible choice of c and zero-stratum spending is optimal, or that the normalizing constant is unique.

### 5. An admissible arbitrarily large uniform-audit gap

Fix any 0<a<rho<1. Choose
\[
0<q<\frac{\rho-a}{1-a},
\qquad
p=\frac{\rho-q}{1-q}.
\]
These inequalities imply a<p<1 and q+(1-q)p=rho.

Let the context have two values, with a region H of probability q. Set Y=1 everywhere and define
\[
F=0\quad\text{on }H,
\qquad
F=1-\sqrt\varepsilon\quad\text{on }H^c,
\]
where 0<epsilon<p^2. These outcomes lie in [0,1]. They produce g=1 on H and g=epsilon on H^c, so g is heterogeneous. All pulls are fresh copies of this law, and audits use independent Bernoulli coins with the designated propensities.

For c=p/sqrt(epsilon), the clipped square-root rule equals one on H, because c>1, and equals p on H^c. It satisfies both propensity bounds and the exact mean budget. The pointwise argument above proves it is an optimizer.

Its audit-induced component is
\[
B(\pi^*)=(1-q)\varepsilon(1/p-1)>0.
\]
Uniform auditing has
\[
B(\rho)=(1/\rho-1)\bigl[q+(1-q)\varepsilon\bigr].
\]
As epsilon decreases to zero, the numerator tends to the strictly positive value q(1/rho-1), while the denominator tends to zero through positive values. Hence B(rho)/B(pi*) tends to infinity. For every L>0, a sufficiently small epsilon gives the claimed strict inequality. Since Y is constant in this construction, Var(Y)=0, so the same example also has an unbounded ratio of total estimator variances. In particular, uniform auditing need not be optimal.

At rho=a or rho=1 the unique feasible policy is uniform, as already shown; no arbitrary-gap assertion is made at these endpoints.

## Proof-Obligation Closure

All obligations are closed by the displayed calculations, elementary one-variable minimization, continuity, bounded convergence with its hypotheses checked, and the explicit bounded construction. No paper-specific prior theorem or specialized external result is required. There are no unresolved ground-truth proof obligations.
