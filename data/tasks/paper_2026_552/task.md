# Problem

Let p and d be positive integers. All polynomial degrees below are total degrees in the displayed polynomial variables.

## Definitions

A function h on a domain D contained in a Euclidean space is piecewise polynomial with complexity at most (M,T,Delta) if there are at most M real boundary polynomials and at most T realized sign patterns of those polynomials on D, with one real value polynomial assigned to each realized sign pattern. At every point of D, h equals the value polynomial assigned to its sign pattern. Both the boundary polynomials and the value polynomials have degree at most Delta. Signs take the values -1, 0, and 1, so this definition also specifies the function on the boundaries. The budgets satisfy M >= 0, T >= 1, and Delta >= 1 and are integers; constant polynomials may be described using degree budget 1.

For a class F of real-valued functions on X, its pseudo-dimension is the supremum of the nonnegative integers N for which there are distinct instances x_1,...,x_N and thresholds t_1,...,t_N such that, for every y in {0,1}^N, some h in F satisfies
\[
\mathbf 1\{h(x_i)\ge t_i\}=y_i\qquad(i=1,\ldots,N).
\]
The thresholds are fixed before the labeling y is chosen. The pseudo-dimension is infinite if these integers are unbounded.

## Task

Prove the following two assertions.

1. **Upper bound.** Let X be a subset of R^q for a positive integer q. Let A be a nonempty bounded closed box in R^p and Theta a nonempty bounded closed box in R^d, where a box is a Cartesian product of closed intervals with finite endpoints; singleton intervals are allowed. Let H > 0 and
\[
f:X\times A\times\Theta\longrightarrow[-H,H].
\]
For each x, write f_x(alpha,theta)=f(x,alpha,theta). Assume that f_x is piecewise polynomial on A times Theta with complexity at most (M_f,T_f,Delta_f), with the same budgets for every x. Assume also that
\[
\operatorname*{argmin}_{\theta\in\Theta} f(x,\alpha,\theta)\ne\varnothing
\qquad\text{for every }(x,\alpha)\in X\times A.
\]
Define
\[
\ell_\alpha(x)=\min_{\theta\in\Theta}f(x,\alpha,\theta).
\]
Then
\[
\operatorname{Pdim}\bigl(\{x\mapsto\ell_\alpha(x):\alpha\in A\}\bigr)
=O\!\left(pd\log(M_f+T_f+d)+p^2d\log\Delta_f\right).
\]
The implied constant is absolute and is independent of q, H, the box endpoints, and the objective family.

2. **Converse.** In this assertion the domains are A=R^p and Theta=R^d, and no uniform boundedness assumption is imposed on the objective or the minimized loss. There are universal constants c>0 and Delta_0 such that, for every p,d>=1 and every real degree budget Delta>=Delta_0, there exist an instance domain X contained in R^q for some positive integer q and a family of real polynomials f_x on R^p times R^d, each of total degree at most Delta, such that the minimum
\[
\ell_\alpha(x)=\min_{\theta\in\mathbb R^d}f_x(\alpha,\theta)
\]
is finite and attained for every x and alpha, and
\[
\operatorname{Pdim}\bigl(\{x\mapsto\ell_\alpha(x):\alpha\in\mathbb R^p\}\bigr)
\ge c\,pd\log\Delta.
\]

Any fixed logarithm base greater than one may be used; changing it changes only the universal constants.
