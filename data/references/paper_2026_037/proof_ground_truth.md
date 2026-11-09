# Reference Proof

## Proof Structure

For a Gaussian initial law, both ratio estimators depend on the reference bank through the same self-normalized weighted mean. The weights are well-defined and the weighted mean has a finite second moment. Centering at the estimators' own reference-bank expectations therefore gives two opposite linear transforms of one fluctuation. Their inner product is a negative quadratic form. The blend result then follows by minimizing a scalar quadratic.

## Complete Proof

Write a = exp(-t) and v = 1 - exp(-2t), so a > 0 and v > 0. Each Gaussian transition density w_i = q_t(y|X_i) is strictly positive and finite. Since N >= 1, their sum is strictly positive, and the normalized weights are measurable, positive, and sum to one.

Define

m_hat = sum_i tilde_w_i X_i.

The squared Euclidean norm is convex, so pointwise

||m_hat||^2 <= sum_i tilde_w_i ||X_i||^2 <= sum_i ||X_i||^2.

Consequently,

E||m_hat||^2 <= N (||mu||^2 + tr(Sigma)) < infinity.

In particular, m = E[m_hat] and Delta = m_hat - m are well-defined, and Delta has a finite second moment. All expectations here are over the iid reference bank, with y and t fixed.

Because p_0 is N(mu,Sigma), its score is

s_0(x) = -Sigma^{-1}(x-mu).

Using the definition of estimator B and the fact that the normalized weights sum to one,

hat s_B = exp(t) sum_i tilde_w_i s_0(X_i)
        = -exp(t) Sigma^{-1}(m_hat-mu).

Similarly, estimator A satisfies

hat s_A = -v^{-1} sum_i tilde_w_i (y-a X_i)
        = -v^{-1}(y-a m_hat).

These are fixed affine transforms of m_hat, so both estimators have finite second moments. Their expectations are

E[hat s_B] = -exp(t) Sigma^{-1}(m-mu),

E[hat s_A] = -v^{-1}(y-a m).

Thus their centered errors satisfy

e_B = -exp(t) Sigma^{-1} Delta,

e_A = (a/v) Delta.

Their second moments are finite, and their inner product is integrable, for example by 2|<e_A,e_B>| <= ||e_A||^2 + ||e_B||^2. Consequently,

<e_A,e_B> = -(a exp(t)/v) Delta^T Sigma^{-1} Delta
           = -v^{-1} Delta^T Sigma^{-1} Delta.

Since Sigma is symmetric positive definite, so is Sigma^{-1}. Taking expectations gives

rho = -v^{-1} E[Delta^T Sigma^{-1} Delta] <= 0.

A nonnegative integrable random variable has expectation zero exactly when it vanishes almost surely. Positive definiteness therefore shows that rho = 0 exactly when Delta = 0 almost surely, equivalently when m_hat is almost surely constant. Otherwise rho < 0. This proves the requested strictness conclusion as well as nonpositive alignment.

Now write

sigma_A^2 = E||e_A||^2,    sigma_B^2 = E||e_B||^2.

For every deterministic real lambda, expansion of the squared norm gives

J(lambda) = lambda^2 sigma_A^2 + (1-lambda)^2 sigma_B^2
             + 2 lambda(1-lambda) rho.

In particular,

D = sigma_A^2 + sigma_B^2 - 2 rho = E||e_A-e_B||^2 >= 0.

Under the stated assumption D > 0, completing the square yields

J(lambda) = D [lambda - (sigma_B^2-rho)/D]^2
             + sigma_B^2 - (sigma_B^2-rho)^2/D.

The positive coefficient D proves that the unique minimizer over R is

lambda* = (sigma_B^2-rho)/D.

The constant term simplifies to

J(lambda*) = [sigma_B^2 D - (sigma_B^2-rho)^2]/D
           = (sigma_A^2 sigma_B^2-rho^2)/D.

Finally, if rho < 0, both sigma_A^2-rho and sigma_B^2-rho are positive. Since

D = (sigma_A^2-rho) + (sigma_B^2-rho),

D > 0, the numerator of lambda* is positive and strictly smaller than D. Hence 0 < lambda* < 1.

No uniqueness is claimed when D = 0. In this Gaussian setting, nonpositive rho and nonnegative variances imply that D = 0 forces sigma_A^2 = sigma_B^2 = rho = 0, in which case J is identically zero. The argument also applies without change when N = 1. No limit in N or t, and no finite-sample unbiasedness assumption, is used.
