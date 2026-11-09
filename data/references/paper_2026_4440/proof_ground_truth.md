# Reference Proof

## Proof Structure

1. Compute the componentwise Student-t score and its uniform pointwise bound.
2. Derive score centering and the exact score variance, and factor the covariance through the deterministic network Jacobian.
3. Establish invertibility and use an SVD and scalar inequality to bound the regularized natural-gradient operator.
4. Combine the operator and score bounds and simplify the constants.

## Complete Proof

Fix any input x, parameter vector w, and observation y. Write f=f_w(x) and let J=J_w(x) be the m-by-p Jacobian. All expectations below use the stated model distribution at this fixed x,w, with nu,s held fixed.

For component i, put r_i=y_i-f_i. Differentiating the log likelihood gives

z_i=partial_{f_i} log p_w(y|x)=(nu+1)r_i/(nu s^2+r_i^2).

The sign is positive for the log-likelihood location score with residual y_i-f_i. Since

nu s^2+r_i^2 >= 2s sqrt(nu)|r_i|,

we obtain

|z_i| <= (nu+1)/(2s sqrt(nu)),

including r_i=0. Consequently,

||z||_2 <= sqrt(m)(nu+1)/(2s sqrt(nu)).

This also proves that every component of the random score has finite first and second moments, even when the observation itself has no finite mean or variance.

We next derive the score covariance. Under the model, each residual R_i=Y_i-f_i has a symmetric density, and its score is an odd bounded function. Thus E[z_i(Y)]=0.

For the second moment, put U=R_i/(s sqrt(nu)) and a=(nu+1)/2>1/2. The density of U is proportional to (1+u^2)^(-a). Define

I_0=integral_R (1+u^2)^(-a) du,

I_1=integral_R (1+u^2)^(-a-1) du,

K=integral_R u^2(1+u^2)^(-a-2) du.

All three integrals are finite: their tail orders are respectively |u|^(-nu-1), |u|^(-nu-3), and |u|^(-nu-3), and the integrands are bounded on compact intervals. Also I_0>0.

Integrate the derivative of u(1+u^2)^(-a) over the real line. Its boundary values vanish because u(1+u^2)^(-a) tends to zero in absolute value like |u|^(-nu). This gives

0=I_0-2a integral_R u^2(1+u^2)^(-a-1) du
 =I_0-2a(I_0-I_1).

Hence

I_1/I_0=(2a-1)/(2a)=nu/(nu+1).

Similarly, the boundary values of u(1+u^2)^(-a-1) vanish, and integrating its derivative gives

0=I_1-2(a+1)K.

Therefore

K/I_0=nu/((nu+1)(nu+3)).

Since the normalized density of U is I_0^(-1)(1+u^2)^(-a) and

z_i(Y)=(nu+1)/(s sqrt(nu)) * U/(1+U^2),

we conclude

E[z_i(Y)^2]=(nu+1)^2/(nu s^2) * K/I_0
            =(nu+1)/((nu+3)s^2)=:kappa.

The product likelihood makes the residual components independent. Their scores, being functions of the individual residuals, are also independent and centered. Thus

Cov(z(Y)|x)=kappa I_m.

At fixed x,w, J is deterministic, so

F_w(x)=Cov(J^T z(Y)|x)=J^T Cov(z(Y)|x)J=kappa J^T J.

Because kappa>0 and tau>0, for every nonzero v in R^p,

v^T(kappa J^T J+tau I_p)v=kappa||Jv||_2^2+tau||v||_2^2>0.

Hence the regularized matrix is invertible, with no rank assumption on J. The regularized natural-gradient score is

tilde g=(kappa J^T J+tau I_p)^(-1)J^T z(y).

Take a full singular-value decomposition J=U Sigma V^T, where U and V are orthogonal and Sigma is rectangular diagonal with nonnegative singular values. Then

(kappa J^T J+tau I_p)^(-1)J^T
 =V(kappa Sigma^T Sigma+tau I_p)^(-1)Sigma^T U^T.

Its singular values are sigma/(kappa sigma^2+tau), for the singular values sigma of J, together with any additional zero singular values. For every sigma>=0,

kappa sigma^2+tau >= 2sigma sqrt(kappa tau),

and consequently

sigma/(kappa sigma^2+tau) <= 1/(2sqrt(kappa tau)).

At sigma=0 the ratio is zero. This covers rank-deficient J and J=0 as well. Orthogonal matrices preserve Euclidean norms, so

||(kappa J^T J+tau I_p)^(-1)J^T||_op <= 1/(2sqrt(kappa tau)).

Combining with the pointwise score bound yields

||tilde g||_2 <= [1/(2sqrt(kappa tau))] [sqrt(m)(nu+1)/(2s sqrt(nu))]
              =sqrt(m)(nu+1)/(4s sqrt(nu kappa tau)).

Substitution of kappa=(nu+1)/((nu+3)s^2), using s>0, gives

||tilde g||_2 <= (1/4)sqrt(((nu+1)(nu+3)m)/(tau nu)).

The argument holds at every fixed x,w,y and the right-hand side does not depend on any of them. This proves the claimed uniform bound.

## Source Repair and Obligation Audit

The deterministic-Jacobian covariance justification replaces the source's incorrect conditional-independence explanation. The positive score sign corrects the source's local sign error; it agrees with differentiation of the likelihood and the subsequent scale discussion. Both repairs leave the covariance and norm argument unchanged.

All theorem-critical obligations are closed above: score differentiation and boundedness; centering and variance; covariance factorization; regularized invertibility; spectral control including zero singular values; and exact constant simplification and uniformity. No specialized external theorem or unproved Student-t moment identity is needed.
