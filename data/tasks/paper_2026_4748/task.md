# Problem

## Statistical setup

Let X and Y be measurable context and outcome spaces. Let Z be a nonempty compact convex subset of R^d with diameter at most D, where 0<=D<infinity. Equip Z and all finite-dimensional real vector and matrix spaces with their Borel sigma-algebras, and use product sigma-algebras on products. Let s:Y->Z be measurable. For every p in Z, a supplied measure oracle returns a probability measure mu_p on Y such that

\[
\mathbb E_{\tilde y\sim\mu_p}s(\tilde y)=p.
\]

Assume p->mu_p is a probability kernel, so that these measures may be used with random forecasts.

Let H be a real vector-valued RKHS of measurable functions h:X x Z->R^d. Its feature operator Phi(x,p):R^d->H satisfies

\[
h(x,p)^\top u=\langle h,\Phi(x,p)u\rangle_H,
\qquad \|\Phi(x,p)\|_{\mathrm{op}}^2\le G
\]

for all x,p,u, where 0<=G<infinity. Write Gamma(a,b)=Phi(a)^*Phi(b) for its matrix-valued kernel. For h in H define

\[
f_h(x,p,y)=h(x,p)^\top s(y).
\]

At round t, Nature supplies x_t, and the procedure, having observed x_t and all previous rounds but not y_t, chooses a finitely supported probability distribution Q_t on Z. Nature's current outcome y_t may depend on the previous history, x_t, and Q_t, but is fixed without access to the fresh draw p_t from Q_t. The procedure draws p_t and outputs mu_t=mu_{p_t}; y_t is then revealed. All history-dependent choices are measurable. This includes every fixed adversarial sequence and every nonanticipating adaptive choice described here.

For a fixed h, define

\[
\operatorname{OIGap}_T(f_h)=
\left|\sum_{t=1}^T\mathbb E\left[
 f_h(x_t,p_t,y_t)-
 \mathbb E_{\tilde y\sim\mu_t}f_h(x_t,p_t,\tilde y)
\right]\right|.
\]

The outer expectation includes the procedure's forecast randomness and the resulting random history; it is not an expectation of an absolute value or a supremum. Define the unit-ball average error by

\[
A_T=\frac1T\sup_{\|h\|_H\le1}\operatorname{OIGap}_T(f_h).
\]

## Computational model

Use an oracle-arithmetic model. Kernel-matrix evaluations cost poly(d) operations. If an explicit finite feature representation is supplied, it is a matrix Psi(x,p) in R^{r x d}, for an integer r>=1, satisfying

\[
\Gamma(a,b)=\Psi(a)^\top\Psi(b).
\]

In this representation, evaluating the supplied feature matrix and multiplying it by a vector are charged O(poly(d)r) operations. If no finite representation is supplied, set r=infinity. This is the evaluation-cost convention for the stated bounds, not a claim that every program computing a feature map has linear cost in its dimension.

The numerical evaluation interfaces are measurable: Gamma:(X x Z)^2->R^{d x d} is jointly measurable in both input pairs, and Psi:X x Z->R^{r x d} is jointly measurable when a finite representation is supplied.

The affine hull A of Z is supplied in Euclidean coordinates. If its dimension is positive, known c in Z and radii 0<rho<=R satisfy

\[
B_A(c,\rho)\subseteq Z\subseteq B_A(c,R),
\]

where B_A denotes a ball in A. If the affine dimension is zero, its single point is supplied. Separation and linear-optimization oracles for Z are available in these coordinates. A separation query either certifies membership or supplies a separating hyperplane; a linear-optimization query maximizes a supplied linear functional over Z. Each geometric oracle has a fixed Borel-measurable response rule as a function of its Euclidean query inputs, including any requested positive accuracy; this includes its rule for choosing among multiple valid responses. Their numerical implementations have cost polynomial in d and logarithmic in the inverse requested positive accuracy and in the geometric condition R/rho. Oracle-arithmetic bounds use these costs. The notation tilde-O suppresses logarithmic factors in the horizon, inverse statistical accuracy, and this geometric condition.

Evaluating s(y_t) and obtaining mu_{p_t} count as separate supplied-oracle calls. Their actual implementation costs are added to the arithmetic bounds below; no complexity assumption on an arbitrary encoding of X or Y is implicit.

## Task

Prove that there is an online procedure such that, for every admissible Nature strategy, every T>=1, and every h in H,

\[
\operatorname{OIGap}_T(f_h)
\le \|h\|_H\sqrt{2D^2GT}.
\]

Consequently, for any class with sup_h ||h||_H<=B<infinity, prove that its supremum expected gap is at most B sqrt(2D^2GT), and hence is o(T).

Prove also that the procedure can be implemented, in the computational model above, with O(T) statistic and measure-oracle calls and total arithmetic time

\[
\widetilde O\!\left(\operatorname{poly}(d,D,G)\,
T\min\{r,T\}\right).
\]

In particular, show that for 0<epsilon<=1 it can achieve A_T<=epsilon with total arithmetic time

\[
\widetilde O\!\left(
\operatorname{poly}(d,D,G)
\min\{r,\epsilon^{-2}\}\epsilon^{-2}
\right),
\]

which is at most tilde-O(poly(d,D,G)epsilon^{-4}). Here epsilon is average statistical error, not the numerical tolerance of an individual oracle call. The total horizon dependence is nearly linear when a fixed finite feature representation is used; the kernel-only bound may be nearly quadratic. Include the cases D=0 and G=0.
