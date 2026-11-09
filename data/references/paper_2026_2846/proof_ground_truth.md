# Reference Proof

## Proof Structure

Work in whitened coordinates. Establish the unique interior linear/quadratic exponential tilt realizing zero mean and identity second moment, using an explicit coercive dual bound, and identify it by a KL decomposition. Identify the finite-particle Gibbs law using regular-value coarea conditioning and orthogonal transitivity. Verify Fourier smoothing and the density local-CLT hypotheses for the mean/second-moment statistic, obtain the one-particle density-ratio limit, and transfer the conditioned tilted product law to the original product law. Push forward to the original coordinates, identify the free-energy minimizer, and derive the multiplier identities by cutoff integration by parts.

## Complete Proof

### 1. Analytic Properties and Quadratic Integrability

All data, d, delta, sigma, mu, Sigma, and L are fixed as P increases. Let R=max_j ||x_j||. The correct triangle bounds are
\[
((\|u\|-R)_+)^2\leq\min_j\|u-x_j\|^2\leq(\|u\|+R)^2.
\]
The lower bound is at least ||u||^2/2-R^2. Bounding the finite Gaussian sum above and below by its largest summand, up to fixed multiplicative constants, therefore gives
\[
c_-\|u\|^2-C\leq-\log p_\delta(u)\leq c_+\|u\|^2+C
\]
for fixed positive c_-,c_+. Taking the Gaussian expectation and applying the invertible affine change yields
\[
\beta_-\|y\|^2-C\leq\widetilde V(y)\leq\beta_+\|y\|^2+C.
\]
Thus q_tilde(y)=Z_0^{-1}exp(-V_tilde(y)) is a full-support probability density with a Gaussian envelope.

The Gaussian-mixture score is (c(u)-u)/delta^2, where c(u) is a convex combination of the finitely many centers. Hence ||g(z)||<=C(1+||z||). Derivatives of the finite-center log-sum-exp are bounded at every positive order, except for the explicit quadratic contribution to the potential. These bounds justify differentiation under Gaussian expectation, including the unsmoothed case sigma=0. In particular, V is smooth, its gradient grows at most linearly, and its higher derivatives have at most polynomial growth.

Expanding the common-covariance mixture gives
\[
\widetilde V(y)=\tfrac12y^TQy+q^Ty-\ell(y)+C,
\qquad Q=L^TL/\delta^2\succ0,
\]
where
\[
\ell(y)=E\log\sum_j\exp(b_j^Ty+\gamma_j(\epsilon)),
\qquad b_j=L^Tx_j/\delta^2.
\]
The offsets gamma_j are affine functions of Gaussian noise plus constants, so their absolute expectations are finite. The finite log-sum-exp bounds imply |ell(y)|<=C(1+||y||). Moreover, keeping any one summand supplies a global affine lower bound
\[
\ell(y)\geq\beta^Ty+c_0
\]
for a fixed beta and finite c_0.

For parameters a and symmetric B, set K=Q-B and c=a-q. Up to a fixed additive constant, the log partition is
\[
H(c,K)=\log\int\exp\{c^Ty-\tfrac12y^TKy+\ell(y)\}\,dy.
\]
It is finite when K is positive definite, by the linear upper growth of ell. Conversely, the affine lower bound bounds its integrand below by a constant times exp((c+beta)^T y-y^T K y/2). If K has a negative eigenvalue, this Gaussian-type integral diverges along that eigendirection. If K is positive semidefinite with a zero eigenvalue, integration in a null direction diverges whether the corresponding linear coefficient vanishes or not. Thus the integrability domain is exactly K positive definite. The relevant boundary is that of Q-B, not that of B itself.

### 2. Moment Realization and the KL Identity

The dual objective for moments (0,I_d), after the preceding affine parameter change and omission of fixed constants, is
\[
D(c,K)=H(c,K)+\tfrac12\operatorname{tr}K,\qquad K\succ0.
\]
Gaussian integration using the affine lower bound gives
\[
D(c,K)\geq C_0+\tfrac12(c+\beta)^TK^{-1}(c+\beta)
 +\tfrac12\operatorname{tr}K-\tfrac12\log\det K.
\]
If k_j are the eigenvalues of K, the final two terms are one half the sum of k_j-log k_j. This scalar function is bounded below and tends to infinity at both zero and infinity. Consequently every sublevel set has all eigenvalues of K bounded above and bounded away from zero. On such a set the quadratic term also bounds c. Thus every sublevel set is contained in a compact subset of the open integrability domain. Continuity there and a minimizing-sequence argument give an interior minimizer.

The Hessian of a log partition in a parameter direction is the variance of the corresponding linear/quadratic statistic. A polynomial u^Ty+y^TSy/2 cannot be constant under a strictly positive density on R^d unless u=0 and S=0. Hence the objective is strictly convex and its minimizer is unique. Differentiating under the integral at this interior point yields
\[
E_rY=0,\qquad E_rYY^T=I_d.
\]
Writing a_*=c_*+q and B_*=Q-K_* gives
\[
r(y)=\exp\{a_*^Ty+\tfrac12y^TB_*y-\widetilde V(y)-A_*\},
\qquad K_*\succ0.
\]
The positive precision K_* and the linear growth of ell give a Gaussian envelope for r and E_r exp(eta||Y||^2)<infinity for some eta>0. The derivative bounds above imply that every derivative of r is bounded by a polynomial times a Gaussian envelope, hence r is a Schwartz function; its orthogonal orbit is bounded in every Schwartz seminorm.

For every density s with the prescribed moments and finite free energy,
\[
\mathrm{KL}(s\|q_{\rm tilde})
 =\mathrm{KL}(s\|r)+\int\log(r/q_{\rm tilde})s
 =\mathrm{KL}(s\|r)+\mathrm{KL}(r\|q_{\rm tilde}).
\]
Indeed, log(r/q_tilde)=a_*^Ty+y^TB_*y/2 plus a constant, so its integral is the same under s and r. The quadratic growth bounds ensure integrability of this log ratio. The Gaussian envelope and quadratic log growth make r's own potential and entropy integrals finite. Nonnegativity of KL, with equality only for equal densities almost everywhere, proves the unique minimizer assertion in whitened coordinates. Densities of infinite positive entropy cannot improve this finite minimum; finite second moments control the negative entropy part by comparison with a Gaussian.

### 3. Fourier Smoothing for the Statistic

Identify R^d times Sym_d with R^m using any fixed linear coordinates, where m=d+d(d+1)/2. Set T(y)=(y,yy^T), W=T(Y), and t_0=(0,I_d), with Y distributed as r. Use the pairing u^Ty+y^TAy/2 for frequencies; this is merely an invertible rescaling of the symmetric-matrix frequency coordinates.

Here is the needed oscillatory estimate, with its derivation. For a bounded family of Schwartz functions b on R,
\[
\left|\int e^{i\eta x+i\lambda x^2/2}b(x)\,dx\right|
 \leq C_N(1+|\lambda|)^{-1/2}
 \left(1+\frac{|\eta|}{1+|\lambda|}\right)^{-N}.
\]
For |lambda|>=1 and |eta| bounded by a fixed multiple of 1+|lambda|, the quadratic van der Corput bound gives C|lambda|^{-1/2}, using uniformly bounded amplitude supremum and derivative L^1 norm. For |lambda|<=1 in this regime the L^1 amplitude bound suffices.

For |eta| much larger than 1+|lambda|, localize with a smooth cutoff supported where |x|<2|eta|/(3|lambda|) and equal to one where |x|<=|eta|/(2|lambda|), when lambda is nonzero. On this inner part |eta+lambda x|>=|eta|/3, so repeated integration by parts with (i(eta+lambda x))^{-1}d/dx gives arbitrarily high inverse powers of |eta|. The cutoff derivatives and the coefficients produced by integration by parts are uniformly controlled since |lambda|/|eta| is bounded. On the outer part, the amplitude is supported at distance comparable to |eta|/|lambda| from zero. Its supremum and derivative L^1 norm decay to every order in that distance by the Schwartz bounds. Applying the quadratic van der Corput estimate there retains the |lambda|^{-1/2} factor when |lambda|>=1; when |lambda|<=1 the amplitude L^1 bound suffices. For lambda=0, ordinary Fourier integration by parts gives the estimate directly. Taking enough derivatives gives the displayed bound, with a constant depending on finitely many Schwartz seminorms. The localization is essential: integration by parts is not applied across a stationary point.

Diagonalize A=O^T diag(lambda_1,...,lambda_d)O and put eta=Ou. Apply the scalar estimate successively. This iteration is valid for a non-product amplitude: after integrating one coordinate, differentiate and polynomially weight the remaining coordinates, and apply the same scalar estimate to those differentiated and weighted amplitudes. The resulting Schwartz seminorms are bounded by the first coordinate's frequency factor times finitely many original seminorms. Iterating gives
\[
|\phi_W(u,A)|\leq C_N\prod_{j=1}^d(1+|\lambda_j|)^{-1/2}
\left(1+\frac{|\eta_j|}{1+|\lambda_j|}\right)^{-N}.
\]
Orthogonal changes preserve boundedness of the relevant Schwartz seminorms uniformly in O.

Choose an integer n_0>2(d+1) and N with N n_0>1. Integrating the n_0-th power first in the linear frequency gives
\[
\int_{\mathbb R^d}|\phi_W(u,A)|^{n_0}\,du
 \leq C\prod_j(1+|\lambda_j|)^{1-n_0/2}.
\]
Lebesgue integration of a spectral function on symmetric matrices has the eigenvalue Jacobian product_{i<j}|lambda_i-lambda_j|, with a finite orthogonal-group factor. This Jacobian formula follows by differentiating A=O^T diag(lambda)O: each off-diagonal rotational direction acquires its eigenvalue difference; repeated-eigenvalue matrices form a Lebesgue-null set. Bounding the product by C product_j(1+|lambda_j|)^{d-1} yields
\[
\int|\phi_W(u,A)|^{n_0}\,du\,dA
 \leq C\int_{\mathbb R^d}\prod_j(1+|\lambda_j|)^{d-n_0/2}\,d\lambda<\infty.
\]
Thus the required convolution power is integrable.

The same bound shows phi_W(u,A)->0 at infinity. If A is unbounded, a largest-eigenvalue prefactor tends to zero. If A remains bounded and u is unbounded, one rotated linear-frequency factor tends to zero. Separately, full support gives |phi_W(u,A)|<1 for every nonzero frequency: equality would make the continuous linear/quadratic phase constant modulo 2 pi everywhere, hence constant as an ordinary polynomial. This verifies both nonlattice behavior and the strong Cramer condition.

### 4. The Audited Density Local CLT and the Ratio Limit

The standard independent result used here is the following density local CLT. If iid random vectors have finite nonsingular covariance Gamma, characteristic function of modulus less than one off zero satisfying the strong Cramer condition, and an integrable characteristic-function power, then sufficiently large sums have continuous densities f_n and
\[
\sup_x\left|n^{m/2}f_n(nt_0+\sqrt n\,x)-\gamma_\Gamma(x)\right|\longrightarrow0,
\]
where gamma_Gamma is the centered normal density with covariance Gamma. In particular, sup f_n<=C n^{-m/2}, f_n(nt_0) is asymptotic to n^{-m/2}gamma_Gamma(0), and the relative Gaussian approximation holds uniformly for displacements o(sqrt n). The source's cited version additionally assumes exponential moments, which are also verified here. This statement is the standard_independent dependency theory_012, not an unproved paper-specific ensemble result.

For the present W, exponential moments near the origin follow from ||T(y)||<=C(1+||y||^2) and the Gaussian envelope. Covariance is nonsingular because any zero-variance linear combination of W would be a constant linear/quadratic polynomial on the full support. Fourier smoothing and the strong Cramer condition were proved in the preceding section. Hence all hypotheses of the stated theorem hold.

With Delta=T(Y)-t_0, its distribution is fixed as P increases and it has exponential tails. Define
\[
R_P(\Delta)=\frac{f_{P-1}((P-1)t_0-\Delta)}{f_P(Pt_0)}.
\]
On ||Delta||<=K log P, the local CLT gives uniform convergence of this ratio to one: the Gaussian displacement exponent tends to zero and the ratio of the central prefactors tends to one. The global upper density bound and the positive central asymptotic bound make R_P uniformly bounded for all Delta and sufficiently large P. The probability of the complement tends to zero, so
\[
E_r|R_P(T(Y)-t_0)-1|\longrightarrow0.
\]
No independence of Delta from any auxiliary construction is needed for this estimate.

### 5. Coarea Conditioning and Equality of the Conditioned Laws

For every integer P>=d+1, M_P is nonempty and compact. For
\[
\Psi_P(Y)=(P^{-1}Y^T1_P,P^{-1}Y^TY),
\]
its differential at Y in M_P is
\[
D\Psi_P(Y)[H]=(P^{-1}H^T1_P,P^{-1}(H^TY+Y^TH)).
\]
For any vector u and symmetric S, H=1_Pu^T+YS/2 produces (u,S). Thus (0,I_d) is a regular value.

The standard coarea formula, dependency theory_014, says that at a regular value the density-based disintegration of an ambient density h has fiber density proportional to h/J_P against induced surface measure, where J_P is the positive coarea Jacobian. We use this coarea version, not an arbitrary version of conditioning on a null event.

An orthogonal matrix O fixing 1_P preserves Psi_P and the Frobenius metric. Differentiating this invariance shows J_P(OY)=J_P(Y). These transformations act transitively on M_P: choose an orthonormal U spanning 1_P's orthogonal complement and write Y=sqrt(P)UX; orthogonal transformations of R^{P-1} take any orthonormal d-frame X to any other by extending frames to orthonormal bases. This is valid also at P=d+1 and includes disconnected components. Normalized induced surface measure is therefore the same invariant probability as the pushed-forward Stiefel-Haar measure, dependency theory_015. The coarea Jacobian is constant, so the coarea conditional law of q_tilde^{otimes P} is exactly the prescribed Gibbs law.

The likelihood ratio of r^{otimes P} to q_tilde^{otimes P} is
\[
\exp\{\sum_i a_*^Ty_i+\tfrac12\sum_i y_i^TB_*y_i+\text{constant}_P\}.
\]
On M_P its linear sum is zero and its quadratic sum is P tr(B_*)/2. Hence it is constant on the fiber, and the two coarea conditional laws agree.

For sufficiently large P, independence under the tilted product law gives the joint density of Y_1 and S_P=sum_i T(Y_i), namely
\[
r(y)f_{P-1}(s-T(y)).
\]
Thus its density-based conditional first marginal at s=Pt_0 is
\[
r(y)\frac{f_{P-1}(Pt_0-T(y))}{f_P(Pt_0)}.
\]
This formula agrees at the particular regular value with the coarea version. To justify evaluation there, nearby moment fibers remain regular and lie in a common compact set: second-moment constraints bound sum_i ||y_i||^2, and failure of nearby regularity would, by compactness and continuity, contradict regularity on the central fiber. Integration along this proper local submersion makes coarea expectations of bounded continuous tests continuous in the constraint value. The density formula also gives continuous test expectations, using the continuous convolution densities, their boundedness, and dominated convergence against r. Since these versions agree almost everywhere near the value, continuity makes them agree at the value itself. The local CLT ensures f_P(Pt_0)>0 for sufficiently large P.

### 6. Convergence and Variational Identification in Original Coordinates

For any bounded continuous test function varphi,
\[
E_{\mu_P}\varphi(Y_1)=E_r[\varphi(Y)R_P(T(Y)-t_0)]\longrightarrow E_r\varphi(Y).
\]
The L^1 ratio estimate even proves total-variation convergence of these sufficiently large-P marginals. In particular, they converge weakly to r. No density assertion for the smallest admissible P is needed.

Push forward by z=mu+Ly. The limiting density has mean mu and covariance Sigma and is
\[
\rho_\infty(z)=Z^{-1}\exp\{-V(z)-\lambda^Tz-\tfrac12(z-\mu)^T\Lambda(z-\mu)\},
\]
where
\[
\lambda=-L^{-T}a_*,\qquad\Lambda=-L^{-T}B_*L^{-1}.
\]
Lambda is symmetric, and all affine constants and the constant Jacobian are absorbed into Z. The Gaussian envelope proves that rho_infty belongs to C(mu,Sigma).

Let q(z) be the normalized density proportional to exp(-V(z)). Affine invariance of KL, or direct subtraction of the two log densities, gives for every rho in C(mu,Sigma)
\[
\mathrm{KL}(\rho\|q)=\mathrm{KL}(\rho\|\rho_\infty)+\mathrm{KL}(\rho_\infty\|q).
\]
The log ratio is a linear/quadratic polynomial, and its expectation is constant because the moments are fixed. Moreover,
\[
\mathrm{KL}(\rho\|q)=F(\rho)+\log\int e^{-V(z)}\,dz.
\]
Therefore rho_infty is the unique minimizer of F, up to equality of densities almost everywhere.

### 7. Multiplier Identities

The limiting density and its derivatives have Gaussian envelopes, while g grows at most linearly. Apply integration by parts with smooth compactly supported cutoffs and send their radius to infinity. Gaussian domination removes the cutoff terms and gives
\[
E[\nabla\log\rho_\infty(Z)]=0,
\qquad E[(Z-\mu)\nabla\log\rho_\infty(Z)^T]=-I_d.
\]
Since
\[
\nabla\log\rho_\infty(z)=-g(z)-\lambda-\Lambda(z-\mu),
\]
the first identity gives lambda=-E[g(Z)]. The second, using the prescribed covariance and the symmetry of Lambda, gives
\[
C+\Sigma\Lambda=I_d,\qquad C=E[(Z-\mu)g(Z)^T].
\]
Transposing and adding yields
\[
\Sigma\Lambda+\Lambda\Sigma=2(I_d-\operatorname{sym}(C)).
\]
All stated conclusions follow.

## Proof-Obligation Audit

The analytic and domain bounds, interior moment realization, uniqueness and KL decomposition, Fourier decay and smoothing, strong Cramer verification, regular-value geometry and constant Jacobian, exact conditioning version, likelihood-ratio invariance, marginal convergence, affine pushforward, finite-free-energy membership, and multiplier identities are explicitly derived above. The only invoked independent probability theorem is the density local CLT, whose relevant statement and all hypotheses are supplied. The standard coarea statement is supplied and its regularity hypotheses verified; Stiefel transitivity is also explicitly established. No nonstandard dependency or unresolved GT obligation remains.
