# Reference Proof

## Proof Structure

The theorem-critical obligations are: (i) establish existence and uniqueness of interpolation on the scaled design and its weight invariance, (ii) prove a polynomial-residual projection bound, (iii) obtain the order-n Taylor remainder bound for the SPD resolvent, (iv) control arbitrary nodal perturbations, and (v) combine the bounds. Each obligation is closed below. No general scaling theorem for arbitrary polynomial subspaces or numerical direct-solver error estimate is assumed.

## Complete Proof

Fix all the stated parameters and an arbitrary h in (0,1].

### Scaled interpolation and weights

The map taking a polynomial p(s) to p(s/h) is a bijection of P_n onto itself, with inverse taking p(s) to p(hs). Moreover, p(s/h) evaluated at h sigma_i equals p(sigma_i). Since evaluation on Sigma_ref is invertible, evaluation on Sigma_h is therefore invertible as well. Both exact and arbitrary prescribed nodal data consequently have unique coordinatewise interpolants on Sigma_h.

For each i, the polynomial ell_i(s/h;Sigma_ref) belongs to P_n and has the required cardinal values at the scaled nodes. Uniqueness gives
\[
\ell_i(s;\Sigma_h)=\ell_i(s/h;\Sigma_{\rm ref}).
\]
In particular, define
\[
\lambda_h:=\sum_{i=1}^n|\ell_i(0;\Sigma_h)|.
\]
Then lambda_h=lambda_ref.

For scalar nodal data g, use Pi_h[g] to denote the scalar interpolation value at zero. Its coordinatewise extension is the vector functional in the task. The Lagrange formula and polynomial exactness are
\[
\Pi_h[g]=\sum_{i=1}^n g(h\sigma_i)\ell_i(0;\Sigma_h),
\qquad \Pi_h[p]=p(0)\quad(p\in P_n).
\]
Indeed, the Lagrange sum is a polynomial in P_n with the prescribed nodal values, so uniqueness proves both assertions.

### Projection bound

Write
\[
\|g\|_{\infty,[0,h\sigma_{\max}]}:=\sup_{0\le s\le h\sigma_{\max}}|g(s)|.
\]
For each coordinate f_j and every p in P_n, polynomial exactness and the Lagrange formula imply
\[
\begin{aligned}
|f_j(0)-\Pi_h[f]_j|
&\le |f_j(0)-p(0)|+|\Pi_h[f_j-p]|\\
&\le \|f_j-p\|_{\infty,[0,h\sigma_{\max}]}
+\lambda_h\max_i|f_j(h\sigma_i)-p(h\sigma_i)|\\
&\le (1+\lambda_h)\|f_j-p\|_{\infty,[0,h\sigma_{\max}]}.
\end{aligned}
\]
All nodes and zero lie in this interval. This argument requires no existence theorem for a best approximating polynomial.

### Resolvent remainder and exact-data error

By the spectral theorem for a real symmetric matrix, write
\[
A=Q\operatorname{diag}(\alpha_1,\ldots,\alpha_d)Q^T,
\qquad Q^TQ=I.
\]
Positive definiteness gives alpha_k>=lambda_min(A)>0 for every k. Consequently
\[
f(s)=Q\operatorname{diag}((\alpha_k+s)^{-1})Q^Tb
\]
is smooth on a neighborhood of every compact interval of nonnegative s. Differentiating the scalar diagonal entries n times yields
\[
f^{(n)}(s)=(-1)^n n!(A+sI)^{-(n+1)}b.
\]
Orthogonality of Q shows that the Euclidean operator norm of the power appearing here is
\[
\|(A+sI)^{-(n+1)}\|_{2\to2}
=\max_k(\alpha_k+s)^{-(n+1)}
\le \lambda_{\min}(A)^{-(n+1)}
\quad(s\ge0).
\]
Thus
\[
|f_j^{(n)}(s)|\le\|f^{(n)}(s)\|_2
\le n!\lambda_{\min}(A)^{-(n+1)}\|b\|_2.
\]

Take p to be the degree-(n-1) Taylor polynomial of f_j at zero. Taylor's theorem, applicable because f_j is smooth on the interval, gives
\[
|f_j(s)-p(s)|
\le \frac{s^n}{n!}\sup_{0\le t\le s}|f_j^{(n)}(t)|
\le s^n\lambda_{\min}(A)^{-(n+1)}\|b\|_2
\]
for 0<s<=h sigma_max. At s=0 the residual is zero, so the same bound holds there. It follows that
\[
\|f_j-p\|_{\infty,[0,h\sigma_{\max}]}
\le(h\sigma_{\max})^n\lambda_{\min}(A)^{-(n+1)}\|b\|_2.
\]
Applying the projection bound, taking the maximum over j, and using lambda_h=lambda_ref proves
\[
\|f(0)-\Pi_h[f]\|_\infty
\le(1+\lambda_{\rm ref})\sigma_{\max}^n
\lambda_{\min}(A)^{-(n+1)}\|b\|_2h^n.
\]

### Arbitrary nodal perturbations

The definition on prescribed numerical values gives
\[
\Pi_h[\hat f]_j=\sum_{i=1}^n\hat f_j(h\sigma_i)\ell_i(0;\Sigma_h).
\]
Subtracting the corresponding exact-data formula therefore yields
\[
\begin{aligned}
|\Pi_h[f]_j-\Pi_h[\hat f]_j|
&\le\sum_{i=1}^n|\ell_i(0;\Sigma_h)|
|f_j(h\sigma_i)-\hat f_j(h\sigma_i)|\\
&\le\lambda_{\rm ref}\max_{i,k}|f_k(h\sigma_i)-\hat f_k(h\sigma_i)|.
\end{aligned}
\]
Taking the maximum over j proves
\[
\|\Pi_h[f]-\Pi_h[\hat f]\|_\infty
\le\lambda_{\rm ref}\|f-\hat f\|_{\infty,\Sigma_h}.
\]
No continuity assumption or extension of the numerical data is required.

### Total error and boundary cases

The triangle inequality gives
\[
\|f(0)-\Pi_h[\hat f]\|_\infty
\le\|f(0)-\Pi_h[f]\|_\infty
+\|\Pi_h[f]-\Pi_h[\hat f]\|_\infty.
\]
Substituting the two bounds proves the stated total-error estimate.

If sigma_max=0, nonnegativity and unisolvency force n=1 and Sigma_ref={0}. Exact interpolation then returns f(0), and the zero exact-data bound is valid; the perturbation argument is unchanged. The proof also includes b=0 and h=1. No division by sigma_max, ||b||_2, or the nodal discrepancy occurs. The quantities multiplying h^n depend only on the fixed A, b, n, and reference design, not on h. All five proof obligations are closed.
