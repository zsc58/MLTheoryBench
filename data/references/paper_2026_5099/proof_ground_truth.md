# Reference Proof

## Proof Structure

Establish existence and uniqueness of the minimum-norm solutions and apply finite-dimensional convex duality. For each leave-one-out sample, establish a primal-dual norm-gap sandwich by weak duality. Specialize it to the omitted singleton, choose the auxiliary multiplier that maximizes the resulting quadratic, and bound the hinge violation by the omitted full-sample dual multiplier times the squared feature norm. Sum these inequalities and use the primal-dual multiplier identity.

## Complete Proof

Write I={1,...,n}, and identify subsamples with their index sets. For T contained in I, consider
\[
P_T=\min_{f\in H}\frac12\|f\|^2
\quad\text{subject to }y_j\langle f,u_j\rangle\ge1\quad(j\in T).
\]
Every such problem is feasible because the full-sample separator is feasible on T.

First suppose T is nonempty. Let V_T be the finite-dimensional span of the vectors u_j with j in T. Decomposing f into its component in V_T and its orthogonal component leaves every constraint unchanged when the orthogonal component is removed, and cannot increase the norm. Thus the minimization reduces to V_T. Its feasible set is nonempty and closed. Intersecting it with a closed ball containing any feasible point gives a compact set on which the continuous objective attains its minimum. Strict convexity of the squared norm on the convex feasible set gives uniqueness. Consequently f_T exists and is unique, also as an element of H.

We use the following standard convex duality result: a finite-dimensional convex quadratic minimization problem with affine inequality constraints, a finite attained optimum, and a strictly feasible point has equality of its primal and Lagrange-dual optimal values, an attained dual optimum, and KKT multipliers satisfying stationarity and complementary slackness. Weak duality bounds every feasible dual value by the primal optimum. Here a feasible separator projected onto V_T can be multiplied by 2 to make every constraint strict, so these hypotheses hold.

For nonnegative multipliers alpha_j, the Lagrangian is
\[
\mathcal L_T(f,\alpha)
=\frac12\|f\|^2+\sum_{j\in T}\alpha_j(1-y_j\langle f,u_j\rangle).
\]
Minimizing over f by completing the square gives the dual objective
\[
D_T(\alpha)=\sum_{j\in T}\alpha_j-\frac12\left\|\sum_{j\in T}\alpha_jy_ju_j\right\|^2,
\qquad \alpha_j\ge0.
\]
For an optimal multiplier vector, stationarity and complementary slackness give
\[
f_T=\sum_{j\in T}\alpha_jy_ju_j,
\qquad
\alpha_j(y_j\langle f_T,u_j\rangle-1)=0.
\]
Taking the inner product of the representation with f_T yields
\[
\|f_T\|^2
=\sum_{j\in T}\alpha_jy_j\langle f_T,u_j\rangle
=\sum_{j\in T}\alpha_j.
\]
When T is empty, the unique optimizer is f_T=0, the dual has the single empty multiplier vector, and its objective is zero. All the preceding identities and duality conclusions hold directly with empty sums. This includes the leave-one-out training sample when n=1.

Fix a partition I=I_{\rm in}\mathbin{\dot\cup}I_{\rm out}. Let eta be dual-optimal for I_in and beta dual-optimal for I. Write f_in=f_{I_in} and f_S=f_I, and set
\[
b=\sum_{i\in I_{\rm out}}\beta_i y_i u_i,
\qquad
s=\sum_{i\in I_{\rm out}}\beta_i.
\]
The restriction of beta to I_in is dual-feasible for the in-sample problem. Complementary slackness gives
\[
\langle f_S,b\rangle
=\sum_{i\in I_{\rm out}}\beta_i y_i\langle f_S,u_i\rangle=s.
\]
Its restricted dual value is therefore
\[
\begin{aligned}
D_{I_{\rm in}}(\beta|_{I_{\rm in}})
&=\|f_S\|^2-s-\frac12\|f_S-b\|^2\\
&=\frac12\|f_S\|^2-\frac12\|b\|^2.
\end{aligned}
\]
Weak duality for the in-sample problem implies
\[
\frac12\|b\|^2\ge
\frac12\bigl(\|f_S\|^2-\|f_{\rm in}\|^2\bigr).
\]

Conversely, let gamma be any nonnegative multiplier vector on I_out and put
\[
c=\sum_{i\in I_{\rm out}}\gamma_i y_i u_i.
\]
The combined vector (eta,gamma) is dual-feasible for the full sample. Expanding its dual value and using the in-sample identities gives
\[
\begin{aligned}
\frac12\|f_S\|^2
&\ge\sum_{j\in I_{\rm in}}\eta_j+
\sum_{i\in I_{\rm out}}\gamma_i-\frac12\|f_{\rm in}+c\|^2\\
&=\frac12\|f_{\rm in}\|^2+
\sum_{i\in I_{\rm out}}\gamma_i(1-y_i\langle f_{\rm in},u_i\rangle)
-\frac12\|c\|^2.
\end{aligned}
\]
Combining these inequalities proves the partition sandwich
\[
\frac12\left\|\sum_{i\in I_{\rm out}}\beta_i y_i u_i\right\|^2
\ge\frac12\bigl(\|f_S\|^2-\|f_{\rm in}\|^2\bigr)
\ge\sum_{i\in I_{\rm out}}\gamma_i(1-y_i\langle f_{\rm in},u_i\rangle)
-\frac12\left\|\sum_{i\in I_{\rm out}}\gamma_i y_i u_i\right\|^2.
\]

Now take I_out={i} and I_in=I\setminus{i}. Define
\[
h_i=1-y_i\langle f_{S\setminus i},u_i\rangle,
\qquad a_i=\max\{h_i,0\}.
\]
Feasibility implies u_i is nonzero: otherwise its margin constraint would read 0>=1. The sandwich consequently gives, for every gamma>=0,
\[
\frac12\beta_i^2\|u_i\|^2
\ge\gamma h_i-\frac12\gamma^2\|u_i\|^2.
\]
The nonnegative maximizer of the quadratic on the right is gamma=a_i/\|u_i\|^2. Indeed, if h_i<=0 the maximum is zero at gamma=0; if h_i>0, completing the square gives that maximizer. In both cases the resulting value is a_i^2/(2\|u_i\|^2). Hence
\[
a_i^2\le\beta_i^2\|u_i\|^4.
\]
Since a_i and beta_i are nonnegative,
\[
a_i\le\beta_i\|u_i\|^2\le\beta_iR^2.
\]
Use the same full-sample optimal vector beta for every omitted index. Summing and applying its multiplier identity gives
\[
\frac1n\sum_{i=1}^n a_i
\le\frac{R^2}{n}\sum_{i=1}^n\beta_i
=\frac{R^2\|f_S\|^2}{n}.
\]
This is the required bound, including n=1.
