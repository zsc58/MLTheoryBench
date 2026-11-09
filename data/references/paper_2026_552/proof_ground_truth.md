# Reference Proof

## Contract and source corrections

The upper-bound branch uses the bounded-objective and finite-box setting at source L000085-L000101 and L000124-L000129, including attainment for every instance and parameter. General finite closed boxes have the same domain-predicate count as the displayed source cubes; alternatively, they are affine images of cubes, including zero-slope coordinates for singleton intervals. The converse explicitly uses all of R^p and R^d and real-valued losses at L000140 and L000366, so the boundedness assumptions of the upper-bound branch do not carry over.

Pseudo-dimension means binary threshold shattering, as used in L000142 and L000368-L000369, not the literal ternary-cardinality test in L000043. Complexity parameters are upper budgets: degree budgets can be padded to at least 1, and predicate budgets can be padded to avoid a zero logarithm. In the actual upper-bound application the predicate budget is already at least 3.

The main-text extractor coefficient 5 at L000150 is replaced by 1/2, as explicitly given in L000388 and L000400. Stabilization uses closed value bounds, as in L000430. Appendix B's products are indexed by the number of blocks K, not the number of polynomials M, and its generic degree parameter is Delta. The quantified dimension in the training-loss formula is d, and piecewise sign patterns are ternary.

## Audited standard independent inputs

**Quantifier elimination.** The one-block specialization of the result stated at L000075-L000082 is the following. A polynomial first-order formula with p free real variables, one quantified block of d real variables, at most M distinct atomic polynomials, and degrees at most D, where M>=2 and D>=1, admits an equivalent quantifier-free formula with I distinct atomic polynomials of degree at most D_QE satisfying
\[
I\le M^{d+1}D^{c_1pd},\qquad D_{QE}\le D^{c_2d}
\]
for absolute constants c_1,c_2. Boolean combinations and all the stated polynomial comparison relations are permitted. The constants are absolute here because the number of blocks is one.

**Goldberg-Jerrum threshold bound.** The result stated at L000292-L000294, with its harmless small-budget normalization made explicit, says that a p-parameter real-valued class has pseudo-dimension at most
\[
C_0p\log(2D\Lambda)
\]
if, for each fixed instance and real threshold, its threshold indicator can be decided by an arithmetic-and-sign algorithm of degree at most D>=1 and predicate complexity at most Lambda>=1. Degree bounds all rational intermediate expressions in the real parameter input; predicate complexity counts distinct rational expressions tested. Restricting the parameter domain cannot increase pseudo-dimension. The instance and threshold are fixed constants of the algorithm, not additional free parameter inputs.

These are the only external proof inputs. The interpolation and stabilization arguments below are derived explicitly.

## step_001: Definitions and parameter cases

Let L={ell_alpha:alpha in A}. Attainment and the real-valued objective ensure that every ell_alpha(x) is a finite real number. Boundary signs include zero, while shattering uses the binary indicator of a comparison with a fixed threshold. The cases of an empty instance domain, singleton boxes, no boundary polynomials, and constant value polynomials are included. Constant polynomials use degree budget 1, so no logarithm of zero occurs. No sampling distribution, expectation, or ERM assumption is needed for these combinatorial claims.

## step_002: Threshold encoding and exact complexity accounting

Fix an instance x and a threshold t. For each realized sign pattern sigma, let P_{x,sigma}(alpha,theta) be its value polynomial, and let h_{x,j} be the boundary polynomials. Define the polynomial Boolean formula
\[
B_{x,t}(\alpha,\theta)=
\bigvee_{\sigma\in\Sigma_x}
\left[
\left(\bigwedge_j \operatorname{sign}(h_{x,j}(\alpha,\theta))=\sigma_j\right)
\land(P_{x,\sigma}(\alpha,\theta)-t\ge0)
\right].
\]
Every sign condition is an ordinary polynomial comparison with zero. On A times Theta this formula is equivalent to f_x(alpha,theta)>=t. Its polynomial expressions are defined everywhere even if f itself is specified only on A times Theta.

Write the box Theta as the product of intervals [a_m,b_m]. Membership in Theta is expressed by the 2d affine comparisons theta_m-a_m>=0 and b_m-theta_m>=0. Thus, for alpha in A,
\[
\ell_\alpha(x)\ge t
\quad\Longleftrightarrow\quad
(\forall\theta\in\mathbb R^d)
[\neg(\theta\in\Theta)\lor B_{x,t}(\alpha,\theta)].
\]
Indeed, an attained minimum is at least t exactly when every feasible objective value is at least t. The guard avoids evaluating an undefined objective outside its domain.

The formula has p free variables and exactly one d-dimensional quantified block. Repeated occurrences of boundary polynomials in different Boolean clauses do not create additional distinct polynomials. There are at most
\[
M=M_f+T_f+2d
\]
distinct atomic polynomials, all of degree at most D=Delta_f. The degree bound applies to both boundary and value polynomials, and D>=1 also covers the box constraints. Since T_f>=1 and d>=1, M>=3. Both bounds are uniform in x and t; subtracting the fixed threshold does not change degree.

## step_003: Quantifier elimination and sign computation

Apply the audited one-block quantifier-elimination result. It gives
\[
\log I\le(d+1)\log M+c_1pd\log D,
\qquad
\log D_{QE}\le c_2d\log D.
\]
In particular, the degree-dependent term belongs in log I; it cannot be omitted or replaced merely by enlarging the bound on D_QE.

For fixed x,t, evaluate each resulting polynomial by forming its monomials and adding them. Every intermediate polynomial has degree at most D_QE. Testing a polynomial and its negative determines its negative, zero, or positive sign, so all required comparison relations can be decided using at most 2I distinct nonconstant tests, with at most a constant number of additional constant tests for Boolean bookkeeping. The Boolean formula can then be evaluated. Consequently this is a GJ algorithm of degree at most D_QE and predicate complexity at most 2I+2. This verifies the hypotheses of the audited GJ result, without requiring any algebraic dependence on x or t.

## step_004: Upper-bound conclusion

The preceding bounds give
\[
\operatorname{Pdim}(L)
\le O\!\left(p+p(d+1)\log M+(p^2+p)d\log D\right).
\]
Because p,d>=1, M=M_f+T_f+2d, and M_f+T_f+d>=2, the additive p term and the replacements d+1<=2d and p^2+p<=2p^2 are absorbed. Also M<=2(M_f+T_f+d). Therefore
\[
\operatorname{Pdim}(L)
=O\!\left(pd\log(M_f+T_f+d)+p^2d\log\Delta_f\right).
\]
For D=1 the degree logarithm vanishes, but the first term remains positive and the derivation is still valid. All constants are absolute. Neither q, H, nor the box endpoints enter the complexity bounds.

## step_005: Explicit lower-bound construction and stabilization

### Construction and total degree

For a sufficiently large real Delta, set
\[
K=\lfloor\Delta/2\rfloor,\qquad B=\lfloor\log_2K\rfloor,\qquad N=pdB.
\]
We can take a universal degree threshold ensuring K>=2. Let G={0,...,K-1}^d. Use the instance domain
\[
X=\{0,1\}^p\times\{0,1\}^d\times\{0,1\}^B.
\]
For j=1,...,p, i=1,...,d, b=1,...,B, designate the distinct instance x^{(j,i,b)}=(e_j,e_i,e_b), where the vectors have the corresponding dimensions.

For r in {0,...,K-1}, let beta_{r,b} be the b-th binary digit of r, counting from the least significant digit. Define
\[
E_b(s)=\sum_{r=0}^{K-1}\beta_{r,b}
\prod_{\substack{0\le k<K\\k\ne r}}\frac{s-k}{r-k}.
\]
All denominators are nonzero constants. At an integer r in the grid, the corresponding interpolation factor is one and all other factors vanish, so E_b(r)=beta_{r,b}. Its degree is at most K-1.

Set
\[
P(\theta)=\sum_{m=1}^d\prod_{k=0}^{K-1}(\theta_m-k)^2
\]
and, for x=(u,v,w), define
\[
f_x(\alpha,\theta)=CP(\theta)
+\left(\sum_{n=1}^pu_n\alpha_n-\sum_{m=1}^d\theta_mK^{m-1}\right)^2
+\frac12\sum_{m=1}^d\sum_{b=1}^Bv_mw_bE_b(\theta_m).
\]
A single finite coefficient C>=1 will be chosen below. For fixed x this is a polynomial jointly in alpha and theta of degree at most max{2K,2,K-1}=2K<=Delta. Coefficient magnitude does not affect degree.

### Attainment for every instance and parameter

P is nonnegative and vanishes exactly on G. It is coercive: if R=||theta||_infinity is sufficiently large, one coordinate has absolute value R and every factor of its product has absolute value at least R/2, giving P(theta)>=(R/2)^{2K}. For fixed x and alpha, the other terms have degree in theta at most max{2,K-1}<2K. Thus CP plus these terms tends to positive infinity as ||theta|| tends to infinity for every C>0. Continuity and coercivity imply that f_x(alpha,.) has a finite attained minimum for every x and every alpha, not just for the parameters used to shatter the designated instances.

For completeness, the coercive minimum principle used here follows by taking any point of a nonempty closed domain, choosing a sufficiently large ball outside which the function exceeds its value at that point, and minimizing on the resulting nonempty compact intersection. Continuity gives an attained minimum there, which is global. This also proves the source's internal coercivity lemma in the form used below.

### Encoding every labeling and computing the grid minimum

Given any y in {0,1}^{p times d times B}, set
\[
D_{j,i}=\sum_{b=1}^B y_{j,i,b}2^{b-1},
\qquad
\alpha_{y,j}=\sum_{i=1}^d D_{j,i}K^{i-1}.
\]
Because 2^B<=K, each D_{j,i} belongs to {0,...,K-1}. Fix a designated instance x^{(j,i,b)}, and write
\[
\theta^*=(D_{j,1},\ldots,D_{j,d}),
\qquad
\psi(\theta)=\left(\sum_{m=1}^d\theta_mK^{m-1}-\alpha_{y,j}\right)^2
+\tfrac12E_b(\theta_i).
\]
At theta*, both penalties vanish and psi(theta*)=y_{j,i,b}/2. At every different grid point v, uniqueness of base-K representation makes the selector difference a nonzero integer. Its square is at least one, while the extractor is nonnegative on the grid. Hence
\[
\psi(v)\ge1\quad(v\in G\setminus\{\theta^*\}),
\qquad
\min_{v\in G} f_{x^{(j,i,b)}}(\alpha_y,v)=y_{j,i,b}/2.
\]
The selected grid point is unique and is separated from every other grid point by at least 1/2 in objective value.

### One penalty coefficient works for all labelings

For fixed p,d,K there are finitely many choices of (y,j,i,b), hence finitely many polynomials psi. Put Q=[-1/2,K]^d and choose
\[
L=\max\left\{1,\max_{y,j,i,b}\sup_{\theta\in Q}\|\nabla\psi(\theta)\|_2\right\}<\infty,
\qquad
\delta=\min\{1/4,1/(10L)\}>0.
\]
Each psi is L-Lipschitz on the convex box Q. Define
\[
R_\delta=\mathbb R^d\setminus\bigcup_{v\in G}B(v,\delta).
\]
This set is closed and unbounded, and contains no zero of P. The coercive minimum principle gives
\[
\mu=\min_{\theta\in R_\delta}P(\theta)>0.
\]
The strict positivity follows from attainment and the fact that the entire zero set G was removed.

For each of the finitely many psi, P+psi is coercive by the same growth calculation used above. Therefore there is one finite T>0 such that P(theta)+psi(theta)>=1 for every such psi whenever ||theta||_infinity>=T. On the compact cube [-T,T]^d, choose a common M_0>=0 with psi(theta)>=-M_0 for every such psi. Now fix one coefficient
\[
C>1+\frac{M_0+1/2}{\mu}.
\]
This C is independent of y,j,i,b. It may depend on p,d,K, which is permitted and has no effect on the polynomial degree or the universal lower-bound constant.

Consider any continuous global minimizer for a fixed (y,j,i,b). Its value is at most psi(theta*)<=1/2. It cannot lie in R_delta. Indeed, outside the cube of radius T,
\[
CP+\psi\ge P+\psi\ge1,
\]
and inside that cube but in R_delta,
\[
CP+\psi\ge C\mu-M_0>1/2.
\]
It also cannot lie within distance delta of a wrong grid point v: that ball lies in Q and
\[
CP(\theta)+\psi(\theta)\ge\psi(\theta)
\ge\psi(v)-L\delta\ge1-1/10>1/2.
\]
Consequently every continuous minimizer lies within distance delta of theta*. Nonnegativity of P and Lipschitz continuity then give
\[
\frac{y_{j,i,b}}2-\frac1{10}
\le \ell_{\alpha_y}(x^{(j,i,b)})
\le\frac{y_{j,i,b}}2.
\]
The upper inequality is obtained by evaluating the objective at theta*. Equality at an endpoint is harmless; strict improvement over the grid value is neither required nor asserted.

### Shattering and universal rate

Take every threshold to be 1/4. When y_{j,i,b}=0, the loss is at most zero; when y_{j,i,b}=1, it is at least 2/5. Thus all N labels are realized with strict threshold separation. The designated instances are shattered, so Pdim>=pdB. Finally, for all sufficiently large Delta, floor(log_2 floor(Delta/2)) is at least a universal positive multiple of log Delta. This proves the asserted lower bound with a universal degree threshold and a universal constant, simultaneously for all positive p,d.

## Obligation closure

Definition closure and binary shattering are explicit. Threshold equivalence, polynomial counts, and degrees are derived. Both external complexity theorems are stated in the exact forms used and their hypotheses are verified. The lower construction, interpolation property, degree bound, attainment on the entire parameter domain, discrete separation, uniform finite coefficient selection, continuous value bounds, and final asymptotic shattering count are all proved above. No unresolved private proof obligation remains.
