# Reference Proof

## Contract and normalization

Write R=||theta_star||_2, Z=||theta^(0)||_2, and B=B_Phi. The empirical loss is Lhat(theta)=(theta-theta_star)^T A(theta-theta_star)/2; the population loss has no factor 1/2. Initialization is independent of the sampled data. All hyperparameters are fixed before sampling. We prove a high-probability event on which the conclusions hold whenever the explicitly stated sample-dependent hypotheses hold; we do not condition the sampling law on those hypotheses.

Choose the universal constant c<=1/16. Choose the universal C sufficiently large for the concentration and uniform-convergence estimates below. These choices are independent of all problem parameters.

## 1. Ridge optimality and linear dynamics

Since lambda>0, the Hessian A+lambda I is positive definite. Thus F_lambda has a unique minimizer theta_lambda, characterized by

(A+lambda I)theta_lambda=A theta_star.

Comparing objective values gives

Lhat(theta_lambda)+(lambda/2)||theta_lambda||_2^2 <= F_lambda(theta_star)=(lambda/2)R^2.

Consequently ||theta_lambda||_2<=R and Lhat(theta_lambda)<=lambda R^2/2. The comparison is an inequality, not an equality.

Put e_t=theta^(t)-theta_lambda. The update gives exactly

e_(t+1)=[I-eta(A+lambda I)]e_t.

Fix any sampled data satisfying the sample-dependent hypotheses. Let P be the orthogonal projection onto the row space of Phi. The smallest positive eigenvalue alpha exists, B>0, and q=1-eta(alpha+lambda) belongs to (0,1). Every row-space eigenvalue of I-eta(A+lambda I) lies in (0,q], so

||P e_t||_2<=q^t||e_0||_2.

This spectral calculation is the transferable part of the zero-teacher argument; its zero-teacher loss bound cannot itself be applied to the present residual.

## 2. Initialization event and training threshold

The audited Gaussian concentration statement is: for w~N(0,sigma^2 I_d), sigma>0, and u in (0,1),

P(| ||w||_2^2-d sigma^2 |>=u d sigma^2)<=2 exp(-d u^2/8).

Apply it with d=m, sigma=nu, and u=1/2. Except with probability at most 2 exp(-m/32)<=delta/3,

Z^2>=m nu^2/2>=R^2.

The last two inequalities follow from the width assumptions once C>=32 and C>=2. Denote this event by E_init. On it, ||e_0||_2<=Z+R<=2Z.

The normal equations imply A(theta_lambda-theta_star)=-lambda theta_lambda. Expanding the empirical loss, rather than discarding its cross term, gives

Lhat(theta^(t))=Lhat(theta_lambda)+(1/2)e_t^T A e_t-lambda<e_t,theta_lambda>.

Also theta_lambda lies in the row space: applying the kernel projection to its normal equation gives lambda(I-P)theta_lambda=0. Since lambda_max(A)<=tr(A)=B, it follows that

Lhat(theta^(t)) <= Lhat(theta_lambda)+(B/2)||P e_t||_2^2+lambda||P e_t||_2 R

<=2B q^(2t)Z^2+2lambda q^t ZR+(lambda/2)R^2.

For every nonnegative integer t>=T_train, the logarithm with base q in (0,1) gives

q^t Z<=sqrt(epsilon/(6B)).

This implication also holds if T_train is negative. Therefore

Lhat(theta^(t)) <= epsilon/3+(2c/sqrt(6))epsilon+(c/2)epsilon < epsilon,

using both terms in the stated upper bound on lambda and c<=1/16. This proves the required weak inequality simultaneously for all the specified training times.

## 3. Null-space concentration and the delayed interval

Condition on the sampled data. Let P_perp=I-P and k=dim ker(Phi)=m-rank(Phi)>=m-n. In an orthonormal basis of this kernel, P_perp theta^(0) has k independent N(0,nu^2) coordinates, because initialization is independent of the data and isotropic. The same Gaussian inequality gives

P(||P_perp theta^(0)||_2^2<k nu^2/2 | data)<=2 exp(-k/32)<=2 exp(-(m-n)/32)<=delta/3.

Let E_kernel be the complementary event. Its unconditional failure probability is also at most delta/3. No full-row-rank assumption is needed.

Projecting the GD update onto the kernel gives, with s=1-eta lambda in (0,1),

P_perp theta^(t)=s^t P_perp theta^(0).

On E_kernel, for every t>=0,

||theta^(t)-theta_star||_2 >= s^t sqrt((m-n)nu^2/2)-R.

A lower bound of this form may be squared only when its right side is nonnegative; globally one must first take its positive part. For t<=T_delay, the definition of the logarithm gives directly

s^t sqrt((m-n)nu^2/2)-R>=sqrt(gamma/mu)>0.

Since L(theta)=(theta-theta_star)^T Sigma(theta-theta_star)>=mu||theta-theta_star||_2^2, the delayed population-loss claim follows simultaneously for all its specified times. Moreover, C>=8 and the two width terms R^2/nu^2 and gamma/(mu nu^2) ensure sqrt((m-n)nu^2/2)>=R+sqrt(gamma/mu), so T_delay>=0. The proof does not assert any ordering between T_train and T_delay beyond what their formulas imply.

## 4. Convergence

Bounded features imply 0<=lambda_max(A)<=b^2. Every eigenvalue of I-eta(A+lambda I) has absolute value less than one under the stated positive step-size assumptions; indeed on the samples under consideration it lies in (0,1-eta lambda]. Hence the centered recursion implies e_t->0 and theta^(t)->theta_lambda. This directly establishes parameter convergence and does not rely on an unproved convergence assertion for general smooth convex objectives.

## 5. Uniform convergence on the fixed predictor ball

For a sample S and a function class H, define its empirical Rademacher complexity by

Rad_S(H)=E_sigma[sup_(h in H) (1/n) sum_i sigma_i h(x_i)],

where the sigma_i are independent uniform signs. For H_R={x-><theta,phi(x)>:||theta||_2<=R}, Cauchy-Schwarz, Jensen, and E[sigma_i sigma_j]=0 for i!=j give

Rad_S(H_R) <= (R/n) E_sigma||sum_i sigma_i phi(x_i)||_2

<= (R/n) sqrt(sum_i||phi(x_i)||_2^2)

=R sqrt(B/n)<=Rb/sqrt(n).

The radius R and the feature map are fixed independently of S. For all functions in H_R and all labels generated by the fixed teacher, predictions and labels have absolute value at most bR. Thus the squared loss is bounded by M=4b^2R^2. On the prediction interval [-bR,bR], it is ell=4bR-Lipschitz in its first argument, since

|(a-y)^2-(a'-y)^2|=|a-a'||a+a'-2y|<=4bR|a-a'|.

We use the following audited standard-independent result from theory_016. For a fixed measurable class H, independent identically distributed examples, a loss bounded in absolute value by M, and confidence parameter rho in (0,1), with probability at least 1-rho, simultaneously for h in H,

P loss_h <= P_n loss_h+2 Rad_S(loss o H)+4M sqrt(2 log(4/rho)/n).

The contraction part of the same result gives Rad_S(loss o H)<=K_0 ell Rad_S(H) for a universal constant K_0 when the loss is ell-Lipschitz on the prediction domain. It applies to the restricted bounded prediction domain here; subtracting any label-dependent constant from the loss does not change its Rademacher complexity because the signs have mean zero. The finite-dimensional parameter ball is separable, and the losses are continuous in the parameter, so suprema can be taken over a countable dense subset and are measurable.

Take rho=delta/3. Applying these statements to H_R yields an event E_gen with failure probability at most delta/3 on which, for every ||theta||_2<=R,

L(theta)<=2Lhat(theta)+8K_0 b^2R^2/sqrt(n)+16b^2R^2 sqrt(2 log(12/delta)/n).

Since log(12/delta)<=2 log(6/delta) and log(6/delta)>=log 6, a sufficiently large universal C in the sample-size assumption makes the last two terms sum to at most epsilon. All hypotheses of the external inequality have now been checked. In particular, its uniformity allows its application to the data-dependent ridge minimizer because ||theta_lambda||_2<=R. Therefore

L(theta_lambda)<=2Lhat(theta_lambda)+epsilon.

## 6. Eventual loss and joint probability

On E_gen, ridge optimality and c<=1/16 provide strict slack:

L(theta_lambda)<=lambda R^2+epsilon<=17epsilon/16<3epsilon.

The population loss is a continuous quadratic form, with finite Sigma and ||Sigma||_op<=b^2. Parameter convergence therefore implies L(theta^(t))->L(theta_lambda), and the strict slack proves L(theta^(t))<=3epsilon for all sufficiently large nonnegative integers t. Convergence to a limit merely bounded by 3epsilon would not alone establish this assertion.

The events E_init, E_kernel, and E_gen have failure probabilities at most delta/3 each. Their intersection has probability at least 1-delta without any independence requirement between these events. The Gaussian initialization is nonzero almost surely. On this intersection, all conclusions hold whenever the sample-dependent hypotheses hold. This is the public probability statement.

## Obligation audit

The ridge minimizer and centered recursion, empirical-loss expansion and quantitative training threshold, kernel dimension and conditional Gaussian concentration, delayed interval and sign check, parameter convergence, bounded-class uniform convergence, strict eventual-loss slack, and joint probability bound are all established above. The only external ingredients are the explicitly stated standard-independent Gaussian concentration and bounded-loss Rademacher/contraction inequalities, with their hypotheses verified. No private proof obligation remains unresolved.
