# Reference Proof

## Proof Structure and Obligations

1. Verify that the signed-measure objective and kernel embeddings are finite, that the kernel mean embedding is differentiable, and that the regularized Gram matrix is positive definite.
2. Solve the unconstrained weight minimization and differentiate its reduced value, explicitly cancelling derivatives of the optimizing weights.
3. Compute the embedding and Gram derivatives and obtain the gradient identity for every configuration, including configurations with zero weights or repeated particles.
4. Establish positive-definite preconditioning and the update identity on the nonzero-weight domain.
5. Prove positive-rescaling invariance and equality of the domains of definition.

All five obligations are derived below. No specialized external result is needed.

## Complete Proof

Write T=mu(R^d). Since 0<k<=1, every double integral defining the objective is absolutely integrable with respect to the relevant total variation measures. In particular, q_{a,Z} has total variation at most sum_i |a_i|, and
\[
c_\mu=\iint k(x,x')\,d\mu(x)d\mu(x')
\]
is finite. For fixed z, putting r=||x-z|| gives
\[
\|x\|k(x,z)\leq \|z\|+r e^{-r^2/(2\sigma^2)}\leq \|z\|+\sigma e^{-1/2}.
\]
Thus m_1 is finite without any unweighted first-moment assumption. Also
\[
\|\nabla_z k(x,z)\|=\sigma^{-2}\|x-z\|k(x,z)\leq \sigma^{-1}e^{-1/2}.
\]
The mean value theorem bounds coordinate difference quotients by this same constant. Because mu is finite, dominated convergence permits differentiation under the integral. Applying dominated convergence to the continuous kernel derivatives also gives continuity of these derivatives. Consequently m_0 is continuously differentiable and
\[
\nabla_{z_i}m_{0,i}=\sigma^{-2}(m_{1,i}-z_i m_{0,i}).
\]
Other rows of m_0 do not depend on z_i.

For completeness, the Gaussian Gram matrix is positive semidefinite even when particles coincide. Set f_z(u)=exp(-||u-z||^2/sigma^2) and b_sigma=int_{R^d} exp(-2||u||^2/sigma^2) du, which is positive and finite. Completing the square gives
\[
\int f_z(u)f_w(u)\,du=b_\sigma k(z,w).
\]
Hence, for every v in R^M,
\[
v^T K v=b_\sigma^{-1}\int\Big(\sum_i v_i f_{z_i}(u)\Big)^2\,du\geq0.
\]
It follows that v^T G_lambda v >= lambda||v||^2, so G_lambda=K+lambda I_M is positive definite and invertible for every configuration.

The objective expands as
\[
\mathcal E_{\mu,\lambda}(a,Z)=\tfrac12c_\mu-a^Tm_0+\tfrac12a^TG_\lambda a.
\]
The coefficient lambda/2 in the public penalty is the normalization already repaired from the source; it agrees with its weight equation and appendix expansion. Completing the square yields
\[
\mathcal E_{\mu,\lambda}(a,Z)=\tfrac12c_\mu-\tfrac12m_0^TG_\lambda^{-1}m_0+\tfrac12(a-a_\lambda)^TG_\lambda(a-a_\lambda),
\qquad a_\lambda=G_\lambda^{-1}m_0.
\]
Thus a_lambda is the unique minimizer and
\[
\mathcal E_{\mu,\lambda}^{\rm red}(Z)=\tfrac12c_\mu-\tfrac12m_0^TG_\lambda^{-1}m_0.
\]
The entries of K are smooth, and the inverse of G_lambda is continuously differentiable: this follows, for example, from its cofactor formula and its everywhere nonzero determinant. Hence a_lambda and the reduced objective are continuously differentiable.

In the following differential calculation abbreviate a=a_lambda(Z). Differentiating the objective at its minimizing weights gives
\[
d\mathcal E_{\mu,\lambda}^{\rm red}=(-m_0+G_\lambda a)^T da-a^Tdm_0+\tfrac12a^T(dG_\lambda)a
=-a^Tdm_0+\tfrac12a^T(dK)a.
\]
Here G_lambda a=m_0 and lambda is fixed. The last quadratic term differentiates K only; it is not the total derivative of a_lambda(Z)^T K(Z) a_lambda(Z).

For a coordinate z_{i,r}, kernel differentiation gives
\[
\frac{\partial K_{j\ell}}{\partial z_{i,r}}
=\sigma^{-2}K_{j\ell}\left[\mathbf1_{j=i}(z_{\ell,r}-z_{j,r})+\mathbf1_{\ell=i}(z_{j,r}-z_{\ell,r})\right].
\]
The diagonal term j=ell=i is zero, as required by k(z_i,z_i)=1. Symmetry therefore yields
\[
\tfrac12a^T\frac{\partial K}{\partial z_{i,r}}a
=\sigma^{-2}a_i\sum_j K_{ij}a_j(z_{j,r}-z_{i,r}).
\]
Let D=diag(a). Combining the Gram contribution with the embedding derivative, row by row, gives
\[
\nabla_{z_i}\mathcal E_{\mu,\lambda}^{\rm red}
=\sigma^{-2}a_i\left[-m_{1,i}+z_i m_{0,i}+(KDZ)_i-z_i(Ka)_i\right].
\]
Since m_0-Ka=lambda a, this equals
\[
\sigma^{-2}a_i\left[(KDZ)_i+\lambda a_i z_i-m_{1,i}\right]
=\sigma^{-2}a_i\left[(G_\lambda DZ)_i-m_{1,i}\right].
\]
Consequently, for every configuration,
\[
\nabla_Z\mathcal E_{\mu,\lambda}^{\rm red}
=\sigma^{-2}D_\lambda(G_\lambda D_\lambda Z-m_1).
\]
No division by a weight has occurred, so this identity includes zero weights and repeated particles.

Now suppose every weight is nonzero. Then D_lambda is invertible and
\[
v^TP_\lambda v=\sigma^{-2}(D_\lambda v)^TG_\lambda(D_\lambda v)>0
\quad\text{for every }v\ne0.
\]
Thus P_lambda is positive definite, even if some weights are negative. The definition of Phi gives
\[
P_\lambda(Z-\Phi_{\mu,\lambda})
=\sigma^{-2}D_\lambda G_\lambda D_\lambda Z-\sigma^{-2}D_\lambda m_1
=\nabla_Z\mathcal E_{\mu,\lambda}^{\rm red}.
\]
Multiplying by P_lambda^{-1} proves, for every eta>0,
\[
Z-\eta P_\lambda^{-1}\nabla_Z\mathcal E_{\mu,\lambda}^{\rm red}
=(1-\eta)Z+\eta\Phi_{\mu,\lambda}(Z).
\]
This is a preconditioned gradient-descent update. The statement makes no claim that every positive step size decreases the objective or preserves the nonzero-weight domain at the next iterate.

Finally, fix C>0, leaving sigma, lambda, and Z unchanged. For mu_C=C mu, linearity gives
\[
m_0^C=Cm_0,\qquad m_1^C=Cm_1,\qquad a_\lambda^C=Ca_\lambda,\qquad D_\lambda^C=CD_\lambda.
\]
A weight is zero after scaling exactly when it was zero before scaling, so the two map domains coincide. On that domain,
\[
\Phi_{\mu_C,\lambda}(Z)
=(CD_\lambda)^{-1}G_\lambda^{-1}(Cm_1)
=D_\lambda^{-1}G_\lambda^{-1}m_1
=\Phi_{\mu,\lambda}(Z).
\]
If mu is the zero measure, the reduced objective and its gradient are zero, all optimal weights are zero, and the map domain is empty. The gradient identity still holds and the domain-qualified claims are vacuous. This completes every stated obligation.
