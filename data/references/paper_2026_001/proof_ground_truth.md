# Reference Proof

## Proof Structure

Fix the training data, feature map, and test distribution. Verify that the ridge inverses and risk quantities are well defined. Use linearity of ridge fitting in its response matrix to obtain the affine coefficient and field identities. Expand squared risk along that affine path and complete the square when D(lambda)>0. Finally differentiate the ridge coefficients and justify the risk derivative using a finite moment expansion, yielding the derivative formula, exact gain, and sign rule.

## Complete Proof

Write z=phi(T,X_T). By assumption z is measurable and E||z||^2 and E||u||^2 are finite. For any fixed coefficient matrix W,

E||W^T z||^2 <= ||W||_F^2 E||z||^2 < infinity.

Thus all fields in the statement have square-integrable predictions once their finite coefficient matrices are defined. Their residuals and differences are square integrable, and their cross inner products are integrable by Cauchy–Schwarz.

Let Sigma=Phi^T Phi/N and b=Phi^T U/N. For every nonzero a in R^m,

a^T(Sigma+lambda I_m)a = ||Phi a||^2/N + lambda ||a||^2 > 0.

Hence Q_lambda=(Sigma+lambda I_m)^(-1) exists for every lambda>0, including when Phi is rank deficient. Abbreviate Q=Q_lambda. The teacher coefficient is W_lambda=Qb, and

W_pd,lambda = Q Phi^T(Phi W_lambda)/N = Q Sigma W_lambda.

Linearity in the response matrix gives

W_sd,lambda,xi = Q Phi^T[(1-xi)U+xi U_hat_lambda]/N
= (1-xi)W_lambda + xi W_pd,lambda.

Since v_W(t,x)=W^T phi(t,x) is linear in W, it follows pointwise that

v_sd,lambda,xi(t,x) = (1-xi)v_lambda(t,x) + xi v_pd,lambda(t,x).

For the independent test triple, set r_T=u-v_lambda(T,X_T) and r_P=u-v_pd,lambda(T,X_T). The student residual is

r_sd=(1-xi)r_T+xi r_P.

Suppressing lambda in R, R_pd, C, and D, expansion and expectation give

R_sd(lambda,xi)=(1-xi)^2 R+xi^2 R_pd+2xi(1-xi)C.

Also,

D=E||r_T-r_P||^2=R+R_pd-2C.

Consequently, for every real xi, including when D=0,

R_sd(lambda,xi)=R-2xi(R-C)+xi^2 D.

If D>0, completing the square yields

R_sd(lambda,xi)=R-(R-C)^2/D+D[xi-(R-C)/D]^2.

The final term is nonnegative and vanishes at exactly one real xi. Hence the unique unconstrained minimizer is xi_star=(R-C)/D, and the minimum risk is R-(R-C)^2/D.

For the derivative argument, the feature map, training data, and test law remain fixed. The coefficient path is smooth on lambda>0 because its defining matrix is invertible there. Differentiating (Sigma+lambda I_m)W_lambda=b gives

partial_lambda W_lambda=-Q_lambda W_lambda.

Since Q_lambda Sigma=I_m-lambda Q_lambda,

W_lambda-W_pd,lambda=(I_m-Q_lambda Sigma)W_lambda
=lambda Q_lambda W_lambda=-lambda partial_lambda W_lambda.

Therefore

v_pd,lambda(t,x)-v_lambda(t,x)=lambda partial_lambda v_lambda(t,x).

To justify differentiation of risk, define the finite matrices H=E[zz^T] and M=E[zu^T], and the finite scalar c=E||u||^2. Each entry is finite: products of feature coordinates are integrable by Cauchy–Schwarz, and E|z_j u_k| <= (E z_j^2)^(1/2)(E u_k^2)^(1/2). Expanding the squared norm as a finite sum gives, for every W,

E||u-W^T z||^2=c-2 tr(W^T M)+tr(W^T H W).

Here tr denotes the trace, and H is symmetric. Apply this identity to W_lambda and differentiate the finite polynomial in its entries. With W_lambda'=partial_lambda W_lambda,

R'(lambda)=-2 tr((W_lambda')^T M)+2 tr((W_lambda')^T H W_lambda)
=-2 E< u-W_lambda^T z, (W_lambda')^T z >.

This proves the risk derivative formula without assuming that scalar differentiability alone permits exchange of a derivative and an expectation. In fact, the explicit moment assumptions make R differentiable throughout lambda>0.

Using r_P=r_T-(v_pd,lambda-v_lambda), we obtain

R-C=E<r_T,v_pd,lambda(T,X_T)-v_lambda(T,X_T)>
=lambda E<r_T,partial_lambda v_lambda(T,X_T)>
=-(lambda/2)R'(lambda).

When D>0, substitution into the previously established optimum and minimum gives

xi_star(lambda)=-lambda R'(lambda)/(2D(lambda))

and

R_sd(lambda,xi_star)=R(lambda)-lambda^2(R'(lambda))^2/(4D(lambda)).

Since lambda>0 and D(lambda)>0, a nonzero R'(lambda) makes the risk reduction strictly positive and gives sign(xi_star(lambda))=-sign(R'(lambda)).

For completeness, the excluded optimization case D=0 presents no inconsistency. The two predictions then agree almost surely, so r_T=r_P almost surely, C=R, and the student risk equals R for every xi. The derivative relation also gives R'(lambda)=0 at that parameter. No unique optimizer or quotient formula is asserted in this case.

All theorem-critical obligations are closed by the displayed finite-dimensional calculations and integrability estimates. No external paper-specific result is used.
