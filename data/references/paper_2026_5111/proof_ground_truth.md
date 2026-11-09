# Reference Proof

## Proof Structure

Establish the exact one-step loss identity from a stationary first argument of an auxiliary two-point functional, telescope it to obtain the weighted curvature balance, and then localize each triangular Hessian average to an interior point of its step segment. Rayleigh's principle transfers the resulting statements to the largest Hessian eigenvalue.

## Complete Proof

For brevity write \(s=s_k\). Introduce the auxiliary function
\[
B_\eta(a,b)=L(a)+L(b)-\frac{1}{2\eta}\|a-b\|^2.
\]
The update rule gives
\[
\nabla_a B_\eta(x_k,x_{k+1})
=\nabla L(x_k)-\frac{x_k-x_{k+1}}{\eta}=0.
\]
Consider \(\phi(t)=B_\eta(x_k+t s,x_{k+1})\). Thus \(\phi'(0)=0\), while
\[
\phi''(t)=s^\top\nabla^2L(x_k+t s)s-\frac{\|s\|^2}{\eta}.
\]
The integral Taylor formula yields
\[
\phi(1)-\phi(0)=\int_0^1(1-t)\phi''(t)\,dt
=\frac12s^\top\widetilde H_k s-\frac{\|s\|^2}{2\eta}.
\]
On the other hand, evaluating the endpoints directly gives
\[
\phi(1)-\phi(0)=L(x_{k+1})-L(x_k)+\frac{\|s\|^2}{2\eta}.
\]
Equating these displays proves, for every nonzero step,
\[
L(x_{k+1})-L(x_k)
=-\frac{\|s_k\|^2}{\eta}+\frac12s_k^\top\widetilde H_k s_k
=-\frac{\|s_k\|^2}{2\eta}(2-\eta\rho_k).
\]
For a zero step, its contribution is zero. Summing from \(k=0\) to \(K-1\) therefore gives
\[
\sum_{\substack{k<K\\s_k\ne0}}\|s_k\|^2(2/\eta-\rho_k)
=2\bigl(L(x_0)-L(x_K)\bigr). \tag{1}
\]
If \(E_K>0\), division by \(E_K\) gives the asserted weighted-average identity. Since \(L(x_K)\ge L_{\inf}\), this identity implies
\[
\frac{\sum_{k<K,\ s_k\ne0}\|s_k\|^2\rho_k}{E_K}
\ge \frac2\eta-\frac{2(L(x_0)-L_{\inf})}{E_K}.
\]
A weighted average is at most the corresponding maximum, proving the effective-curvature maximum bound.

Now fix a nonzero step and define
\[
q_k(t)=u_k^\top\nabla^2L(x_k+t s_k)u_k.
\]
This is continuous on \([0,1]\), and
\[
\rho_k=\int_0^1 2(1-t)q_k(t)\,dt.
\]
Because the weight \(2(1-t)\) is nonnegative, has integral one, and is positive on \((0,1)\), the weighted mean-value theorem supplies \(\theta_k\in(0,1)\) such that
\[
\rho_k=q_k(\theta_k)
=u_k^\top\nabla^2L(x_k+\theta_k s_k)u_k. \tag{2}
\]
For every symmetric matrix \(H\) and unit vector \(u\), \(u^\top H u\le\lambda_{\max}(H)\). Applying this to (2) gives
\[
\lambda_{\max}(\nabla^2L(x_k+\theta_k s_k))\ge\rho_k.
\]
Termwise substitution in (1) proves
\[
\sum_{\substack{k<K\\s_k\ne0}}\|s_k\|^2\left[\frac2\eta-
\lambda_{\max}(\nabla^2L(x_k+\theta_k s_k))\right]
\le2(L(x_0)-L(x_K)).
\]
Likewise, the maximum of these eigenvalues is at least the maximum of the \(\rho_k\)'s, which proves the claimed eigenvalue lower bound.

Finally, suppose \(L(x_k)\) is bounded above along the trajectory and \(E_K\to\infty\). Together with the lower bound, this makes \(|L(x_0)-L(x_K)|\) uniformly bounded. The weighted-average identity following from (1) then shows that its correction term \(2(L(x_0)-L(x_K))/E_K\) tends to zero. Hence the weighted average of \(\rho_k\) converges to \(2/\eta\), as required.
