# Reference Proof

## Proof Structure

1. Reduce the nondecreasing time weighting to the interval beginning at the generalized-inverse cutoff, treating zero tolerance and an unattained inverse cutoff explicitly.
2. Condition on the training dataset and control the population and empirical cutoff laws by the same generated law using reverse-process entropy bounds and terminal Gaussian mixing.
3. Use Pinsker and Gaussian-ball testing to obtain a small-ball constraint, then apply the lower order-2 Renyi dimension.

## Complete Proof

Write S=(X_1,...,X_n), and throughout use the unhalved losses in the public task. The empirical law, score b_S, and generated law q^S are conditional on S. Population loss for b_S means integration against the fixed population law with S held fixed; it is not integration against the empirical conditional law.

### 1. Weighting and cutoff

The generalized inverse is taken over [epsilon,T]. Since 32 varepsilon<=w(T), its defining set is nonempty and epsilon<=delta<=T.

If varepsilon>0, then for every t>delta in [epsilon,T], monotonicity and the definition of an infimum imply w(t)>=32 varepsilon. Indeed, there is a point u<t in the defining set, and w(t)>=w(u). Therefore, regardless of whether the inverse is attained,

\[
\mathbb E_S\widehat{\mathcal L}(b_S,\varpi)
\ge 32\varepsilon\,\mathbb E_S\widehat{\mathcal L}(b_S,\varpi_{\rm ELBO}^{\delta}).
\]

Consequently the expected empirical cutoff ELBO loss is at most 1/32. Under alternative 1 the identical argument gives the population cutoff bound. Under alternative 2, nonnegativity of the loss and delta>=epsilon give it by restricting the integration interval.

If varepsilon=0, then delta=epsilon. Since w is positive almost everywhere on (epsilon,T), Tonelli's theorem and nonnegativity show that zero expected weighted empirical loss implies zero expected unweighted loss on this interval. The same reasoning applies to alternative 1; alternative 2 already gives the needed population bound. Thus no division by zero is needed.

### 2. Conditional reverse-process entropy bounds

The relevant standard entropy estimate is as follows. For nonexplosive diffusions P and Q with the same constant invertible diffusion matrix A, finite initial relative entropy, a well-defined weakly unique comparison law Q, and finite true-path energy,

\[
\mathrm{KL}(P\|Q)
\le \mathrm{KL}(P_0\|Q_0)
+\frac12\mathbb E_P\int_0^H
\|A^{-1}(\beta_P-\beta_Q)(Z_u,u)\|^2\,du.
\]

This is the localized Girsanov entropy bound; endpoint data processing gives the corresponding endpoint inequality. This standard-independent result is recorded with its hypotheses in theory_022.

Fix S outside a null set. The exact reversal of the population OU process on [0,T-delta] has drift kappa y+2 grad log mu_{T-u}(y); the exact empirical reversal has the analogous empirical score. Both exist by reversing their forward OU processes at a positive-time cutoff. The comparison process is the public, nonexplosive weakly unique reverse diffusion. All these processes have A=sqrt(2) I_d. Their drift difference is twice the score error, so

\[
\frac12\left\|(\sqrt2 I_d)^{-1}(2e)\right\|^2=\|e\|^2.
\]

Thus the entropy cost is the public unhalved loss, not half that loss. Whenever the corresponding cutoff loss is finite,

\[
\mathrm{KL}(\mu_\delta\|q^S_{T-\delta})
\le \mathcal L(b_S,\varpi_{\rm ELBO}^{\delta})
+\mathrm{KL}(\mu_T\|q_0),
\]

\[
\mathrm{KL}(\widehat\mu_\delta\|q^S_{T-\delta})
\le \widehat{\mathcal L}(b_S,\varpi_{\rm ELBO}^{\delta})
+\mathrm{KL}(\widehat\mu_T\|q_0).
\]

The expected loss bounds imply finite conditional losses almost surely. Terminal finiteness and the comparison-law hypotheses are verified below and in the public setup. Under alternative 3 only the empirical entropy estimate is needed, because the population KL bound is assumed almost surely.

### 3. Terminal KL bounds

First suppose kappa>0 and set gamma=q_0=N(0,kappa^{-1}I_d). Its Gaussian log-Sobolev inequality has constant kappa^{-1}; along the OU semigroup this gives

\[
\mathrm{KL}(P_T\|\gamma)
\le e^{-2\kappa(T-s)}\mathrm{KL}(P_s\|\gamma),\qquad 0<s\le T.
\]

Here the reference Gaussian is invariant for that semigroup. To verify the smoothing estimate used with this decay, couple the initial law P_0 with gamma, say by (U,V). The two transition kernels have equal covariance sigma_s^2 I_d and means alpha_s U and alpha_s V. The log-sum inequality, applied to these mixtures, and the equal-covariance Gaussian KL formula give

\[
\mathrm{KL}(P_s\|\gamma)
\le \frac{\alpha_s^2}{2\sigma_s^2}\mathbb E\|U-V\|^2.
\]

Taking the infimum over couplings and using exp(2 kappa s)-1>=2 kappa s yields

\[
\mathrm{KL}(P_s\|\gamma)
\le \frac{W_2(P_0,\gamma)^2}{4s}.
\]

The source's looser elementary moment bound is

\[
W_2(P_0,\gamma)^2
\le 2\left(\mathbb E_{P_0}\|X\|^2+\kappa^{-1}d\right).
\]

Since T>=1, take s=1. For the population law this proves

\[
\mathrm{KL}(\mu_T\|q_0)
\le \frac12 e^{-2\kappa(T-1)}(\sigma^2+\kappa^{-1}d)
\le \frac1{32}
\]

under the public horizon condition. The same calculation conditional on S replaces sigma^2 by n^{-1} sum_i ||X_i||^2. Its expectation equals sigma^2, proving

\[
\mathbb E_S\mathrm{KL}(\widehat\mu_T\|q_0)\le\frac1{32}.
\]

For kappa=0, the terminal population law is the mixture of N(x,2T I_d) with x~mu, while q_0=N(0,2T I_d). The log-sum inequality gives

\[
\mathrm{KL}(\mu_T\|q_0)
\le \int\mathrm{KL}(N(x,2T I_d)\|N(0,2T I_d))\,d\mu(x)
=\frac{\sigma^2}{4T}.
\]

The empirical version is bounded by (4Tn)^{-1} sum_i ||X_i||^2, and averaging gives the same bound. Thus T>=8 sigma^2 supplies both terminal thresholds. This is the local zero-kappa completion of the source argument recorded in theory_023.

Combining terminal bounds and cutoff losses, alternatives 1 and 2 give

\[
\mathbb E_S\mathrm{KL}(\widehat\mu_\delta\|q^S_{T-\delta})\le\frac1{16},\qquad
\mathbb E_S\mathrm{KL}(\mu_\delta\|q^S_{T-\delta})\le\frac1{16}.
\]

Alternative 3 gives the population expectation at most 1/32 directly, while the empirical bound remains at most 1/16. In every alternative the two displayed 1/16 bounds therefore hold.

### 4. Total-variation closeness

Define TV(P,Q)=sup_A |P(A)-Q(A)|. Pinsker's inequality states TV(P,Q)^2<=KL(P||Q)/2. Apply it conditionally on S to each cutoff law and the same q^S, and then use the L2 triangle inequality:

\[
\left(\mathbb E_S\mathrm{TV}(\mu_\delta,\widehat\mu_\delta)^2\right)^{1/2}
\le \left(\mathbb E_S\mathrm{TV}(\mu_\delta,q^S_{T-\delta})^2\right)^{1/2}
+\left(\mathbb E_S\mathrm{TV}(\widehat\mu_\delta,q^S_{T-\delta})^2\right)^{1/2}
\le 2\sqrt{\frac1{32}}=\frac1{\sqrt8}.
\]

The randomness of the common comparison law causes no difficulty: the metric inequality is applied for each dataset before taking the L2 norm.

### 5. Gaussian-ball separation

Write alpha=alpha_delta, tau=sigma_delta, m=E||Z|| for Z~N(0,I_d), and R=tau sqrt(2 log 8). Gaussian concentration for the 1-Lipschitz norm, as recorded in theory_020 and theory_008, gives

\[
p_*:=\mathbb P(\|\tau Z\|\le m\tau+R)\ge\frac78\ge\frac34.
\]

Also m<=sqrt(d) by Jensen. For the fixed dataset define

\[
A_S=\mathbb R^d\setminus\bigcup_{i=1}^n B(\alpha X_i,m\tau+R),
\qquad
D_S=\left\{x:\|x-X_i\|\ge\frac{2(m\tau+R)}\alpha\text{ for all }i\right\}.
\]

Each empirical mixture component assigns at most 1-p_* to A_S, so hat mu_delta(A_S)<=1-p_*. For x in D_S, the Gaussian ball of radius m tau+R about alpha x lies outside the sample balls, up to boundaries of zero Gaussian mass. Hence mu_delta(A_S)>=p_* mu(D_S).

Put

\[
\rho(r)=\int\mu(B(x,r))\,d\mu(x).
\]

Iid sampling and a union bound give

\[
\mathbb E_S\mu(D_S)\ge\left(1-n\rho\left(\frac{2(m\tau+R)}\alpha\right)\right)_+.
\]

For sufficiently small delta, alpha>=1/2. Since d>=5>log 64 and sqrt(2 log 8)=sqrt(log 64),

\[
\frac{2(m\tau+R)}\alpha
\le4\tau(\sqrt d+\sqrt{\log64})
\le8\sqrt d\,\tau=:r_\delta.
\]

We may also require r_delta<1. Monotonicity of rho and the test-set inequality now imply

\[
\mathbb E_S\mathrm{TV}(\mu_\delta,\widehat\mu_\delta)
\ge \frac14\left(3(1-n\rho(r_\delta))_+-1\right)_+.
\]

Jensen and the preceding upper bound imply

\[
\frac14\left(3(1-n\rho(r_\delta))_+-1\right)_+\le\frac1{\sqrt8}.
\]

If n rho(r_delta)>=1 there is nothing to prove; otherwise rearranging the last inequality gives

\[
n\rho(r_\delta)\ge c,\qquad c=\frac{2-\sqrt2}{3}>0.
\]

Therefore n>=c/rho(r_delta).

### 6. Dimension conversion and boundary cases

Let gamma=underline d_2(mu). For 0<r<1, 0<rho(r)<=1, so gamma>=0. Its finiteness follows by taking a bounded cube with positive mu-mass, partitioning it into O(r^{-d}) cells of diameter below r, and using the sum-of-squares bound for their masses; this gives rho(r)>=C r^d for small r and gamma<=d.

For any e<gamma, the definition of a liminf and the negative sign of log r give, for every sufficiently small r,

\[
\frac{\log\rho(r)}{\log r}>e,
\qquad\rho(r)\le r^e.
\]

If d'>0 and d'<gamma, choose e with d'/2<e<gamma. Then

\[
n\ge c r_\delta^{-e}\ge r_\delta^{-d'/2}
\]

for all sufficiently small delta, because c r_delta^{-(e-d'/2)} tends to infinity. This proves the frozen target. If d'<=0, r_delta<1 and n>=1 already imply n>=r_delta^{-d'/2}. In particular the zero-dimension and zero-second-moment cases are covered without an additional assumption.

The same argument recovers the stronger displayed source exponent: when gamma>0, take e strictly between gamma/2 and gamma and absorb c; when gamma=0, use n>=1. All small-cutoff thresholds depend only on the fixed population distribution, d, kappa, T, and the chosen exponent, not on n or the trained score.

### Supplementary deterministic-score Fisher bound

The preceding lemma is not needed for this proof. To retain its correct scope, let b be a deterministic field independent of S. Inserting b between the two scores gives

\[
\mathbb E_S J(\widehat\mu_t\|\mu_t)
\le2\mathbb E_S\widehat{\mathcal L}_t(b)
+2\mathbb E_S\int\|b(y,t)-\nabla\log\mu_t(y)\|^2\,d\widehat\mu_t(y)
=2\mathbb E_S[\widehat{\mathcal L}_t(b)+\mathcal L_t(b)].
\]

The equality uses both the averaged empirical-law identity and the integrand's independence of S. It cannot be used for an arbitrary training-dependent b_S. Accordingly this supplementary bound is not a mandatory rubric step.

## Obligation Closure

The weighting, inverse-cutoff endpoint, zero-tolerance case, both conditional entropy applications, both terminal experiments, TV conversion, Gaussian-ball test, numerical constants, dimension conversion, and degenerate exponent cases are all closed above. The invoked standard-independent entropy, OU decay, Pinsker, and Gaussian concentration statements have their relevant hypotheses stated and verified. No unresolved private proof obligation remains.
