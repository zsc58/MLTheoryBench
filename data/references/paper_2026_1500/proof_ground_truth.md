# Reference Proof

## Proof Structure

Expand the corrupted risk into a positive multiple of the clean risk plus a multiple of the total loss over all one-hot labels. Bound the range of that total loss uniformly using power-sum bounds on a probability vector. Compare the noisy-risk minimizer with the clean minimizer, then rearrange and simplify.

## Complete Proof

Fix an admissible pair $(\beta,\lambda)$ and abbreviate $A=A_{\beta,\lambda}$ and $B=B_{\beta,\lambda}$. For $p=p(x;\theta)$, write
\[
\ell_j(p)=\ell_{\beta,\lambda}(e_j,p).
\]
Conditionally on $(X,Y)$, uniform corruption gives
\[
\mathbb E[\ell_{\tilde Y}(p)\mid X,Y]
=(1-\eta)\ell_Y(p)+\frac{\eta}{J-1}\sum_{j\ne Y}\ell_j(p).
\]
Averaging over $Y\mid X$ and writing $p_j^*(X)=\Pr(Y=j\mid X)$ yields
\[
R^{(\eta)}(\theta)=\left(1-\frac{J\eta}{J-1}\right)R(\theta)+\frac{\eta}{J-1}T(\theta),
\]
where
\[
T(\theta)=\mathbb E_X\sum_{j=1}^J\ell_{\beta,\lambda}(e_j,p(X;\theta)).
\]
For any probability vector $p$, direct summation of the loss gives
\[
\sum_{j=1}^J\ell_{\beta,\lambda}(e_j,p)
=\frac{J}{A}\sum_{k=1}^Jp_k^{1+\beta}
-\frac{1+\beta}{AB}\sum_{k=1}^Jp_k^B
+\frac{J^2}{B}.
\]
For every $q>0$, a probability vector satisfies
\[
\min(1,J^{1-q})\le\sum_k p_k^q\le\max(1,J^{1-q}).
\]
Using $q=1+\beta$ and $q=B$, and remembering that the coefficient of the $B$-power sum is negative, we obtain pointwise, hence also after expectation,
\[
L_-\le T(\theta)\le L_+,
\]
with
\[
L_- = \frac{J^{1-\beta}}{A}-\frac{(1+\beta)\max(1,J^{1-B})}{AB}+\frac{J^2}{B},
\]
\[
L_+ = \frac{J}{A}-\frac{(1+\beta)\min(1,J^{1-B})}{AB}+\frac{J^2}{B}.
\]
Consequently,
\[
T(\theta_1)-T(\theta_2)\le L_+-L_-
=\frac1A\left[J-J^{1-\beta}+\frac{(1+\beta)|1-J^{1-B}|}{B}\right]
\]
for all parameters $\theta_1,\theta_2$.

Let $\theta^\eta$ minimize $R^{(\eta)}$ and let $\theta^*$ minimize $R$. Optimality of $\theta^\eta$ gives
\[
R^{(\eta)}(\theta^\eta)\le R^{(\eta)}(\theta^*).
\]
Substituting the decomposition and rearranging,
\[
\left(1-\frac{J\eta}{J-1}\right)\bigl(R(\theta^\eta)-R(\theta^*)\bigr)
\le \frac{\eta}{J-1}\bigl(T(\theta^*)-T(\theta^\eta)\bigr).
\]
Because $0\le\eta<1-1/J$, the coefficient on the left is positive. Since $\theta^*$ is a clean-risk minimizer, the clean excess risk is nonnegative. Applying the uniform range bound and dividing by the positive coefficient gives
\[
0\le R(\theta^\eta)-R(\theta^*)
\le \frac{\eta}{J-1-J\eta}\,\frac1A
\left[J-J^{1-\beta}+\frac{(1+\beta)|1-J^{1-B}|}{B}\right],
\]
which is the claimed bound.
