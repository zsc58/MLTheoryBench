# Reference Proof

## Scope and approximation convention

The input, network, layer, and output class are fixed. All expectations and variances in the task concern the Gaussian sensitivity randomness, not an additional average over random inputs. The Gaussian sensitivity laws are explicit modeling assumptions; they are not being deduced merely from finite covariance or a variance-decay rate.

The smooth-moment formulas and the sigmoid–probit relation are adopted approximation prescriptions, as in the source. An approximation sign here does not assert equality, asymptotic equivalence, or a quantified error bound. In particular, the exact limit to prove is the limit of the displayed approximate ratio expression. We distinguish the exact moments of A_alpha from their numerical approximations throughout.

## Proof Structure

1. Derive the Bernoulli and normalized-binomial laws for the hard scores.
2. Identify the smooth score as logit-normal and apply the adopted moment prescriptions.
3. Verify mean matching at alpha-star, including the zero-signal case.
4. Make the approximation in the variance prefactor explicit, substitute alpha-star, and compute the limit of the resulting ratio expression.

## Complete Proof

Let mu be real, sigma>0, s>=2 and n>=1 be integers, and N=sn. The full-budget and batch sensitivities have the laws specified in the task.

### 1. Hard-score distributions and moments

For any positive sample count j with Z_j distributed as N(mu,sigma^2/j), standardization and symmetry of the standard normal give

\[
\Pr(Z_j>0)=1-\Phi(-\sqrt j\,\mu/\sigma)=\Phi(\sqrt j\,\mu/\sigma)=:p_j.
\]

Thus I_N is Bernoulli(p_N). Since I_N^2=I_N,

\[
\mathbb E I_N=p_N,\qquad \operatorname{Var}(I_N)=p_N-p_N^2=p_N(1-p_N).
\]

Set B_b=1{Z_{n,b}>0}. The B_b are independent Bernoulli(p_n), since each is a measurable function of one of the independent batch sensitivities. For k=0,...,s, independence gives

\[
\Pr\left(\sum_{b=1}^sB_b=k\right)=\binom{s}{k}p_n^k(1-p_n)^{s-k}.
\]

Consequently s M_s is Binomial(s,p_n), and

\[
\mathbb E M_s=p_n,\qquad
\operatorname{Var}(M_s)=\frac1{s^2}\sum_{b=1}^s\operatorname{Var}(B_b)
=\frac{p_n(1-p_n)}s.
\]

This direct variance expansion does not require a no-atom-at-zero condition on the Bernoulli indicators. Since mu is finite and sigma>0, 0<p_n<1, so the variance used as the ratio denominator is strictly positive.

### 2. Smooth-score distribution and moment prescriptions

The sigmoid maps the real line into (0,1), and

\[
\log\frac{A_\alpha}{1-A_\alpha}=\alpha Z_N
\sim\mathcal N(\alpha\mu,\alpha^2\sigma^2/N).
\]

Thus A_alpha is exactly logit-normal under the stipulated Gaussian model. All its moments exist because it is bounded.

The adopted prescription for a Gaussian X with mean a and variance b>0 is

\[
\mathbb E g(\alpha X)\approx
m(a,b,\alpha):=g\!\left(\frac{\alpha a}{\sqrt{1+\tau_1\alpha^2b}}\right),
\]

with approximate second moment

\[
m(a,b,\alpha)^2+m(a,b,\alpha)[1-m(a,b,\alpha)]
\left[1-(1+\tau_2\alpha^2b)^{-1/2}\right].
\]

Subtracting the square of the adopted mean gives its variance prescription. Substitute a=mu and b=sigma^2/N, which is positive, and define the numerical approximations

\[
m_\alpha=g\!\left(\frac{\alpha\mu}{\sqrt{1+\tau_1\alpha^2\sigma^2/N}}\right),
\qquad
\widetilde v_\alpha=m_\alpha(1-m_\alpha)
\left[1-(1+\tau_2\alpha^2\sigma^2/N)^{-1/2}\right].
\]

Then the adopted rules say E A_alpha approximately equals m_alpha and Var(A_alpha) approximately equals tilde v_alpha. These are applications of the specified prescriptions, not proofs of their numerical accuracy. The other adopted rule is g(t) approximately Phi(sqrt(tau_1)t).

### 3. Mean matching and the zero-signal case

Applying the sigmoid–probit rule to m_alpha gives

\[
m_\alpha\approx
\Phi\!\left(\frac{\sqrt{\tau_1}\alpha\mu}
{\sqrt{1+\tau_1\alpha^2\sigma^2/N}}\right).
\]

For mu != 0, equality of the arguments of this expression and p_n is equivalent to

\[
\frac{\alpha}{\sqrt{1+\tau_1\alpha^2\sigma^2/N}}
=\frac{\sqrt n}{\sigma\sqrt{\tau_1}}.
\]

Both sides are positive. Squaring and rearranging gives

\[
\alpha^2\left(1-\frac nN\right)=\frac{n}{\tau_1\sigma^2}.
\]

Since N=sn and s>1, its positive solution is

\[
\alpha_\star=\frac1\sigma\sqrt{\frac{n}{\tau_1(1-1/s)}}.
\]

Substitution verifies the argument equality and hence the claimed approximate matching.

If mu=0, the argument equation is 0=0 for every alpha>0, so it cannot identify a unique parameter. Nevertheless alpha-star is positive and well-defined and is a valid matching choice. In fact Z_N has the same law as -Z_N and g(t)+g(-t)=1, so E A_alpha=1/2 for every alpha>0. Also p_n=Phi(0)=1/2 and m_alpha=g(0)=1/2. This closes the zero-signal case without dividing by mu.

### 4. Approximate ratio and its limit

Before the additional mean-matching replacement, the ratio of the variance prescription to the exact Multi-TCAV variance is exactly

\[
\frac{\widetilde v_{\alpha_\star}}{\operatorname{Var}(M_s)}
=s\frac{m_{\alpha_\star}(1-m_{\alpha_\star})}{p_n(1-p_n)}
\left[1-(1+\tau_2\alpha_\star^2\sigma^2/N)^{-1/2}\right].
\]

The source's comparison replaces m_{alpha-star} by its approximately matched value p_n in this prefactor. This is a second approximation, not an exact cancellation or a claim of uniformly small relative error. Under that prescription, the ratio becomes

\[
s\left[1-(1+\tau_2\alpha_\star^2\sigma^2/N)^{-1/2}\right].
\]

Now

\[
\frac{\tau_2\alpha_\star^2\sigma^2}{N}
=\frac{\tau_2}{\tau_1(s-1)},
\]

so the resulting approximate ratio expression is

\[
r(s)=s\left[1-\left(1+\frac{\tau_2/\tau_1}{s-1}\right)^{-1/2}\right].
\]

Let u=tau_2/tau_1>0. Rationalization gives the exact identity

\[
r(s)=\frac{su/(s-1)}
{\sqrt{1+u/(s-1)}\,[\sqrt{1+u/(s-1)}+1]}.
\]

Therefore, as the integer s tends to infinity,

\[
r(s)\longrightarrow\frac u2=\frac{\tau_2}{2\tau_1}\approx0.4558.
\]

One may hold n, mu, and sigma fixed and let N=sn grow. This is not an infinite-batch limit at a fixed finite total budget. The limiting expression means that the approximation predicts retention of about 45.6% of the Multi-TCAV variance, equivalently a reduction of about 54.4%. In particular the expression is within 45–55% for sufficiently large s. No convergence of the exact variance ratio follows merely from the adopted approximations.

## Private source-support closure

The upstream CAV records motivate the Gaussian variance scaling but are not additional public hypotheses. Their selected claims can be checked directly. For independent class samples with finite covariances, the empirical class means have means mu_ell and covariances Sigma_ell/n_ell. Hence their difference has mean mu_2-mu_1 and covariance Sigma_1/n_1+Sigma_2/n_2. The global-centroid formula yields w_fast=[n_1/(n_1+n_2)]w_pat, proving the corresponding scaled moments. The simultaneous sign reversal in an outer product is harmless; the redundant off-diagonal sum at L002988 must instead be removed.

Taking traces gives the stipulated total CAV variance. With deterministic concept data, Sigma_2=0 and the result is Tr(Sigma_1)/n_1. With n_ell=c_ell N, fixed positive c_ell, and fixed finite covariance traces, it is [Tr(Sigma_1)/c_1+Tr(Sigma_2)/c_2]/N. The reciprocal at L001195 is corrected accordingly. For a fixed gradient z, the sensitivity variance is z^T Cov(w)z, bounded by ||z||^2 Tr(Cov(w)); this motivates, but does not establish, the separate Gaussian modeling assumption.

The other recorded source-local corrections are: the negative-signal cdf limit is zero; the normalized independent indicator sum is binomial; Bernoulli variance is p(1-p); batch indices must be consistent; and the recovery-of-standard-TCAV parenthesis at L001801 concerns the formal s-to-1 limit, not the large-s limit used above. None changes the frozen target.

## Obligation audit

All obligations for the stated task are closed: the exact hard laws and moments are derived; the logit-normal identification is derived; the specified approximation prescriptions are applied with their domains verified; the matching parameter is checked for nonzero and zero signal; the extra approximate prefactor replacement is disclosed; and the limit of the resulting expression is proved exactly. The source's citations are not treated as proofs of a quantitative approximation-accuracy theorem. Such a theorem is not part of the public task.
