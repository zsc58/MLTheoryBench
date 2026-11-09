# Reference Proof

## Proof Structure

1. Verify that the mixture is a bounded probability density and that both overlap integrals are finite.
2. Compute the squared-density integral by expanding into pairwise Gaussian products and evaluating them by reflection and convolution.
3. Express the overlap difference as an integral against the density difference, then apply Hölder and Pinsker inequalities with the common Gaussian peak bound.
4. Handle infinite KL and every nonnegative penalty weight, including zero.
5. Derive covariance-collapse and class-mean-separation consequences from the exact formula.

## Complete Proof

Write $\phi_c(z)=\mathcal N(z;\mu_c,\Sigma)$ and $p_\theta(z)=\sum_c\pi_c\phi_c(z)$. Positive definiteness of $\Sigma$ makes every component a strictly positive probability density. Thus $p_\theta$ is also a strictly positive probability density.

Set
\[
M=(2\pi)^{-d/2}(\det\Sigma)^{-1/2}.
\]
The Gaussian density formula gives
\[
\phi_c(z)=M\exp\!\left[-\frac12(z-\mu_c)^\top\Sigma^{-1}(z-\mu_c)\right]\leq M.
\]
The maximum is attained at $z=\mu_c$. Since the weights sum to one,
\[
\|p_\theta\|_\infty\leq M.
\]
Consequently,
\[
0\leq C(p_\theta)\leq M\int p_\theta=M,
\qquad
0\leq O(p,p_\theta)\leq M\int p=M.
\]
In particular, subtracting these integrals is legitimate even when the KL divergence is infinite.

The finite mixture expansion gives
\[
C(p_\theta)=\int p_\theta(z)^2\,dz
=\sum_{i,j}\pi_i\pi_j\int\phi_i(z)\phi_j(z)\,dz.
\]
For fixed $i,j$, define the reflected density
\[
\widetilde\phi_j(u)=\phi_j(-u)=\mathcal N(u;-\mu_j,\Sigma).
\]
Then, by the definition of convolution,
\[
\int\phi_i(z)\phi_j(z)\,dz=(\phi_i*\widetilde\phi_j)(0).
\]
The standard Gaussian convolution identity states that, for positive-definite covariance matrices $S_1,S_2$,
\[
\mathcal N(\cdot;m_1,S_1)*\mathcal N(\cdot;m_2,S_2)
=\mathcal N(\cdot;m_1+m_2,S_1+S_2).
\]
Here both covariances equal the positive-definite matrix $\Sigma$, so the identity applies and gives
\[
\int\phi_i\phi_j
=\mathcal N(0;\mu_i-\mu_j,2\Sigma)
=\mathcal N(\mu_i-\mu_j;0,2\Sigma).
\]
The final equality follows directly from the symmetric Gaussian quadratic form. Hence
\[
C(p_\theta)=\sum_{i,j=1}^C\pi_i\pi_j\,\mathcal N(\mu_i-\mu_j;0,2\Sigma).
\]
Using $\det(2\Sigma)=2^d\det\Sigma$ and $(2\Sigma)^{-1}=\tfrac12\Sigma^{-1}$ yields
\[
C(p_\theta)=\frac{1}{(4\pi)^{d/2}\sqrt{\det\Sigma}}
\sum_{i,j=1}^C\pi_i\pi_j
\exp\!\left[-\frac14(\mu_i-\mu_j)^\top\Sigma^{-1}(\mu_i-\mu_j)\right].
\]

Next suppose $\mathrm{KL}(p\|p_\theta)<\infty$. Because $p$ and $p_\theta$ are probability densities, $p-p_\theta\in L^1$ with norm at most two. Together with the established boundedness of $p_\theta$, this verifies the hypotheses for the $L^1$/$L^\infty$ form of Hölder's inequality. Therefore
\[
\begin{aligned}
|O(p,p_\theta)-C(p_\theta)|
&=\left|\int(p-p_\theta)p_\theta\right|\\
&\leq\|p-p_\theta\|_1\,\|p_\theta\|_\infty.
\end{aligned}
\]
For probability densities $r,s$, with total variation defined by $\operatorname{TV}(r,s)=\tfrac12\|r-s\|_1$, Pinsker's inequality for natural-logarithm KL is
\[
\operatorname{TV}(r,s)\leq\sqrt{\tfrac12\mathrm{KL}(r\|s)}.
\]
Our densities meet these hypotheses, and $p_\theta>0$ ensures absolute continuity of the probability measure with density $p$ with respect to the one with density $p_\theta$. Applying Pinsker gives
\[
|O(p,p_\theta)-C(p_\theta)|
\leq\|p_\theta\|_\infty\sqrt{2\,\mathrm{KL}(p\|p_\theta)}
\leq M\sqrt{2\,\mathrm{KL}(p\|p_\theta)}.
\]
If the KL divergence is infinite, the right-hand side is infinite and the left-hand side is finite by the initial bounds, so the same inequality holds in the extended-real sense.

For $\lambda>0$, multiplication gives
\[
|\lambda O(p,p_\theta)-\lambda C(p_\theta)|
\leq\lambda(2\pi)^{-d/2}(\det\Sigma)^{-1/2}
\sqrt{2\,\mathrm{KL}(p\|p_\theta)}.
\]
For $\lambda=0$, the left side is zero, and the right side is zero under the stated convention, including when KL is infinite. Thus the weighted inequality holds for every $\lambda\geq0$.

Finally, keep $d,C$ fixed. The unweighted comparison coefficient $M$ diverges as $\det\Sigma\downarrow0$. This does not assert that its product with a varying KL factor must diverge.

The total diagonal contribution to the information potential is
\[
(4\pi)^{-d/2}(\det\Sigma)^{-1/2}\sum_i\pi_i^2.
\]
All other contributions are nonnegative, and
\[
1=\left(\sum_i\pi_i\right)^2\leq C\sum_i\pi_i^2.
\]
Thus the diagonal sum, and hence the intrinsic overlap, diverges as the determinant tends to zero. In particular, this holds with the weights fixed as requested and does not depend on the behavior of the means.

For fixed $\Sigma$ and weights, the contribution associated with $i\ne j$ has the form
\[
a_{ij}\exp(-s_{ij}/4),\qquad
a_{ij}=\pi_i\pi_j(4\pi)^{-d/2}(\det\Sigma)^{-1/2}>0,
\quad
s_{ij}=\|\mu_i-\mu_j\|_{\Sigma^{-1}}^2.
\]
Its derivative with respect to $s_{ij}$ is $-a_{ij}\exp(-s_{ij}/4)/4<0$. This proves the pairwise separation claim. When $C=1$, there are no off-diagonal terms and this part is vacuous. These conclusions concern the intrinsic overlap and its comparison bound; they do not by themselves prove an optimization guarantee for the data-distribution penalty. In particular, a zero penalty weight produces no penalization.
