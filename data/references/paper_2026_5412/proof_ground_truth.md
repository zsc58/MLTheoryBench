# Reference Proof

## Proof Structure

First identify each label probability with a coordinate mean of the random probability vector. Compute that mean conditional on the latent component using the Dirichlet mean formula, average over the categorical component, and then reorganize the result into a common normalized-base term and a coordinate-weighted gating term.

## Complete Proof

Fix the input \(x\), and suppress its dependence in the notation. By the conditional categorical model,
\[
\Pr(Y=r\mid P,x)=P_r.
\]
The tower property therefore gives
\[
q_r=\Pr(Y=r\mid x)=\mathbb E[P_r\mid x].
\]

Let \(Z=\sum_{i=1}^K a_i\). Conditional on \(H=j\), the Dirichlet parameter vector is \(a+s_j e_j\), whose total concentration is \(Z+s_j\). Hence the Dirichlet coordinate-mean identity yields
\[
\mathbb E[P_r\mid H=j,x]
 =\frac{a_r+s_j\mathbf 1\{r=j\}}{Z+s_j}.
\]
Averaging over \(H\sim\operatorname{Cat}(w)\),
\[
\begin{aligned}
q_r
&=\sum_{j=1}^K w_j
  \frac{a_r+s_j\mathbf 1\{r=j\}}{Z+s_j}\\
&=a_r\sum_{j=1}^K\frac{w_j}{Z+s_j}
  +\frac{s_r w_r}{Z+s_r}.
\end{aligned}
\]
Define
\[
\kappa=\sum_{j=1}^K\frac{w_j}{Z+s_j}.
\]
The scalar coefficient from the problem satisfies \(c=Z\kappa\). Since \(u_r=a_r/Z\) and \(d_r=s_r/(Z+s_r)\), the preceding identity becomes
\[
q_r
 = (Z\kappa)\frac{a_r}{Z}
   +\frac{s_r}{Z+s_r}w_r
 =c\,u_r+d_r g_r,
\]
because \(g_r=w_r\). This holds for every \(r\), so stacking the coordinate identities proves
\[
q=c\,u+d\odot g.
\]

For completeness, all terms are nonnegative, and the decomposition preserves total mass:
\[
\begin{aligned}
c+\sum_{r=1}^K d_r g_r
&=\sum_{r=1}^K w_r\frac{Z}{Z+s_r}
  +\sum_{r=1}^K w_r\frac{s_r}{Z+s_r}\\
&=\sum_{r=1}^K w_r=1.
\end{aligned}
\]
Thus the displayed vector is indeed the induced label-probability vector.
