# Reference Proof

## Proof Structure

1. Verify the affine diffusion and path-entropy hypotheses, and reduce the posterior KL to the covariance drift cost plus the observation constant by discarding explicitly nonnegative terms.
2. Compute the actual drift coefficients of both gauges in covariance eigen-coordinates, treating repeated eigenvalues separately.
3. Establish the common scalar lower bound and apply the occupation-time/control-cost dichotomy.
4. Bound the stationary observation density uniformly in the rotation speed.

## Complete Proof

Put \(A=-\alpha I_2+\omega J\), and write \(q_0=N(m(0),S(0))\). All marginal parameter paths are \(C^1\) on \([0,T]\). Compactness and positive definiteness imply that \(S\), \(S^{-1}\), and \(\dot S\) are bounded. The principal square root \(L\) is \(C^1\): differentiating \(L^2=S\) determines \(\dot L\) through the invertible linear map \(H\mapsto LH+HL\). In the symmetric gauge, the map \(H\mapsto HS+SH\) is likewise invertible on symmetric matrices. Its eigenbasis denominators are \(\lambda_i+\lambda_j>0\). Consequently both gauges give continuous bounded \(B\), and their drifts have bounded time-dependent affine coefficients. Their unit diffusion is uniformly elliptic and their initial laws are nondegenerate Gaussian.

The square-root gauge has the required covariance evolution because
\[
BS+SB^{\mathsf T}+I_2
=\dot L L+L\dot L=\dot S.
\]
The symmetric gauge satisfies the same equation by definition. The affine diffusion initialized with \(q_0\) therefore has the prescribed mean and covariance, by uniqueness of the linear moment equations.

### 1. Entropy and observation reduction

The standard Girsanov result used here, specialized to this setting, is the following: two diffusions on a finite time interval with common identity diffusion, bounded deterministic affine drift coefficients, and nondegenerate Gaussian initial laws are equivalent, and
\[
\operatorname{KL}(Q\|P)
=\operatorname{KL}(q_0\|p_0)
+\frac12\mathbb E_Q\int_0^T\|b_Q(X_t,t)-AX_t\|^2\,dt.
\]
Here is why its integrability conditions hold in this application. With a shared initial law, stop the Girsanov exponential when the state exits a ball. The stopped drift difference is bounded, so the stopped exponential is a martingale. Under the tilted stopped law the drift is the candidate affine drift before exit and the prior affine drift afterward. Their common linear-growth bound and the finite initial second moment give a uniform bound on \(\mathbb E\sup_{t\le T}\|X_t\|^2\) by the usual Itô, martingale, and Gronwall estimates. The tilted exit probabilities tend to zero, which establishes the unstopped change of measure. The reverse change is identical. Changing the initial Gaussian density supplies the initial-density ratio. Under \(Q\), the drift difference has finite integrated second moment, so the stochastic integral in the log density is square-integrable and has mean zero. This proves the displayed entropy formula with all its hypotheses verified; no global Novikov assumption is being inferred merely from differentiability.

Let \(\ell_y(X)\) be the product of the observation densities. Since \(\sigma>0\), it is strictly positive and bounded, and \(0<p(y)=\mathbb E_P\ell_y(X)<\infty\). Bayes' formula gives
\[
\operatorname{KL}(Q\|Q^*)
=\operatorname{KL}(Q\|P)-\mathbb E_Q\log\ell_y(X)+\log p(y).
\]
Every term is finite here: Gaussian initial KL is finite, the affine drift cost is finite, and the observation penalties have finite Gaussian second moments.

Writing \(X_t=m(t)+(X_t-m(t))\) and taking expectations eliminates the drift cross term. The observation expansion is
\[
\mathbb E_Q\|y_n-X_{t_n}\|^2
=\|y_n-m(t_n)\|^2+\operatorname{tr}S(t_n).
\]
It follows that
\[
\operatorname{KL}(Q\|Q^*)
=C_{\rm OU}+\mathcal M+\mathcal C,
\qquad
\mathcal C=\frac12\int_0^T
\operatorname{tr}\big((B-A)S(B-A)^{\mathsf T}\big)\,dt,
\]
where
\[
\mathcal M=
\operatorname{KL}(q_0\|p_0)
+\frac12\int_0^T\|\dot m-Am\|^2\,dt
+\frac1{2\sigma^2}\sum_{n=1}^N
\left(\|y_n-m(t_n)\|^2+\operatorname{tr}S(t_n)\right)
\ge0.
\]
Thus it suffices to lower-bound \(\mathcal C\). In particular, no assertion about attainment at the posterior mean is needed.

### 2. Covariance eigen-coordinates

Let \(0<\lambda_1(t)\le\lambda_2(t)\) be the ordered eigenvalues of \(S(t)\). The variational characterization of the extreme eigenvalues gives
\[
|\lambda_i(t)-\lambda_i(s)|\le\|S(t)-S(s)\|_{\rm op}.
\]
Since \(S\) is \(C^1\), the eigenvalues are Lipschitz, hence absolutely continuous and differentiable almost everywhere.

On each component of the open set \(D=\{\lambda_1<\lambda_2\}\), choose a \(C^1\) oriented orthonormal eigenbasis \(U(t)\). Such a local choice follows, for example, from the \(C^1\) rank-one projector \((S-\lambda_2 I)/(\lambda_1-\lambda_2)\); choices can be continued along the interval. Write
\[
S=U\Lambda U^{\mathsf T},\qquad
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2),\qquad
\Omega=U^{\mathsf T}\dot U=wJ.
\]
Then
\[
U^{\mathsf T}\dot S U=\dot\Lambda+\Omega\Lambda-\Lambda\Omega,
\qquad U^{\mathsf T}AU=A.
\]
Set \(\widetilde B=U^{\mathsf T}BU\) and \(\Delta=\widetilde B-A\).

For the symmetric gauge, the covariance equation gives
\[
\widetilde B_{ii}=\frac{\dot\lambda_i-1}{2\lambda_i},
\qquad
\widetilde B_{ij}=\frac{\Omega_{ij}(\lambda_j-\lambda_i)}{\lambda_i+\lambda_j}\quad(i\ne j).
\]
For the principal-square-root gauge, differentiating \(L=U\Lambda^{1/2}U^{\mathsf T}\) gives
\[
\widetilde B
=\Omega+\frac12\dot\Lambda\Lambda^{-1}
-\Lambda^{1/2}\Omega\Lambda^{-1/2}
-\frac12\Lambda^{-1}.
\]
Therefore
\[
\widetilde B_{ii}=\frac{\dot\lambda_i-1}{2\lambda_i},
\qquad
\widetilde B_{ij}=\Omega_{ij}\left(1-\sqrt{\lambda_i/\lambda_j}\right)\quad(i\ne j).
\]

For both gauges,
\[
\operatorname{tr}(\Delta\Lambda\Delta^{\mathsf T})
=\lambda_1\Delta_{11}^2+\lambda_2\Delta_{22}^2
+\lambda_1\Delta_{21}^2+\lambda_2\Delta_{12}^2.
\]
Write \(\Delta_{12}=aw+\omega\) and \(\Delta_{21}=bw-\omega\). Completing the scalar square shows that the off-diagonal contribution is at least
\[
\omega^2\left(\lambda_1+\lambda_2-
\frac{(\lambda_2a-\lambda_1b)^2}{\lambda_1b^2+\lambda_2a^2}\right)
=\frac{\omega^2\lambda_1\lambda_2(a+b)^2}{\lambda_1b^2+\lambda_2a^2}.
\]
The denominator is positive on \(D\) for both gauges.

For the symmetric gauge,
\[
a=b=-\frac{\lambda_2-\lambda_1}{\lambda_1+\lambda_2},
\]
so this lower bound equals
\[
\frac{4\omega^2\lambda_1\lambda_2}{\lambda_1+\lambda_2}
\ge2\omega^2\lambda_1.
\]
For the square-root gauge put \(r=\sqrt{\lambda_1/\lambda_2}<1\). Then \(a=r-1\), \(b=1-r^{-1}\), and
\[
\lambda_1b^2+\lambda_2a^2=2\lambda_2(r-1)^2,
\qquad
(a+b)^2=\frac{(r^2-1)^2}{r^2}.
\]
The lower bound is consequently
\[
\frac{\omega^2}{2}(\sqrt{\lambda_1}+\sqrt{\lambda_2})^2
\ge2\omega^2\lambda_1.
\]
Define, almost everywhere,
\[
u=\dot\lambda_1-1+2\alpha\lambda_1.
\]
The first diagonal contribution is \(\lambda_1\Delta_{11}^2=u^2/(4\lambda_1)\). Dropping the other diagonal square proves on \(D\)
\[
\frac12\operatorname{tr}\big((B-A)S(B-A)^{\mathsf T}\big)
\ge\frac{u^2}{8\lambda_1}+\omega^2\lambda_1.
\]

For completeness, let \(H=\{\lambda_1=\lambda_2\}\). On this set \(S=\lambda I_2\), with \(\lambda=\lambda_1\). An absolutely continuous scalar function has derivative zero almost everywhere on its zero set: at every differentiability point that is an accumulation point of that set, difference quotients along its zeros give zero; isolated points are countable. Apply this entrywise to \(S-\lambda I_2\). It follows that \(\dot S=\dot\lambda I_2\) almost everywhere on \(H\). Both gauges then yield
\[
B=\frac{\dot\lambda-1}{2\lambda}I_2.
\]
Consequently their half-trace cost is
\[
\frac{u^2}{4\lambda}+\omega^2\lambda,
\]
which is at least the same common lower bound. This handles repeated eigenvalues without dividing by an eigenvalue gap or assuming a global differentiable eigenbasis.

Combining the two sets gives
\[
\mathcal C\ge I:=\int_0^T\left(\frac{u(t)^2}{8\lambda_1(t)}+\omega^2\lambda_1(t)\right)dt.
\]

### 3. Occupation-time dichotomy

Set
\[
\delta=\frac1{4\omega},\qquad
E_\delta=\{t:\lambda_1(t)\ge\delta\},\qquad
F_\delta=[0,T]\setminus E_\delta,\qquad
 a_0=1-\frac1{2c_0}>0.
\]
Here \(\omega\ge c_0\alpha>0\), so the threshold is well-defined.

If \(|E_\delta|\ge T/2\), then
\[
I\ge\int_{E_\delta}\omega^2\lambda_1(t)\,dt
\ge\frac{T\omega}{8}.
\]
Otherwise \(|F_\delta|>T/2\). On \(F_\delta\),
\[
2\alpha\lambda_1\le\frac{\alpha}{2\omega}\le\frac1{2c_0},
\qquad \dot\lambda_1=1-2\alpha\lambda_1+u\ge a_0+u
\]
almost everywhere. Decompose the relatively open set \(F_\delta\) into its countably many interval components. For an interior component \((a,b)\), continuity gives \(\lambda_1(a)=\lambda_1(b)=\delta\), so integration yields
\[
-\int_a^b u\,dt\ge a_0(b-a).
\]
A component meeting an endpoint of \([0,T]\) has endpoint covariance eigenvalues in \([0,\delta]\), so its endpoint difference has absolute value at most \(\delta\). There are at most two such components, including the possibility that a single component meets both endpoints. Summing therefore gives
\[
-\int_{F_\delta}u\,dt\ge a_0|F_\delta|-2\delta.
\]
The countable sum is justified by absolute integrability of \(u\), which follows from Lipschitz continuity of \(\lambda_1\). This also covers an empty high set or a low set equal to the entire interval.

AM–GM gives, pointwise almost everywhere,
\[
\frac{u^2}{8\lambda_1}+\omega^2\lambda_1
\ge\frac{\omega}{\sqrt2}|u|.
\]
Hence in the low-set case
\[
I\ge\frac{\omega}{\sqrt2}\int_{F_\delta}|u|\,dt
\ge\frac{\omega}{\sqrt2}(a_0|F_\delta|-2\delta)
\ge\frac{1-1/(2c_0)}{2\sqrt2}T\omega-\frac1{2\sqrt2}.
\]
Combining the alternatives and restoring \(C_{\rm OU}\) proves
\[
\operatorname{KL}(Q\|Q^*)
\ge\min\left\{\frac18,\frac{1-1/(2c_0)}{2\sqrt2}\right\}T\omega
-\frac1{2\sqrt2}+C_{\rm OU}
\]
for both gauge families.

### 4. Uniform stationary observation constant

Assume \(p_0=N(0,(2\alpha)^{-1}I_2)\). The affine solution and \(e^{At}=e^{-\alpha t}e^{\omega tJ}\) give stationary marginal covariance \((2\alpha)^{-1}I_2\), and
\[
\operatorname{Cov}(X_{t_i},X_{t_j})
=\frac1{2\alpha}e^{-\alpha|t_i-t_j|}e^{\omega(t_i-t_j)J}.
\]
Thus the stacked observations \(y_{1:N}\in\mathbb R^{2N}\) have centered Gaussian law with covariance \(\Sigma_\omega\) whose blocks are
\[
(\Sigma_\omega)_{ij}
=\frac1{2\alpha}e^{-\alpha|t_i-t_j|}e^{\omega(t_i-t_j)J}
+\mathbf1_{i=j}\sigma^2I_2.
\]
Its latent contribution is positive semidefinite, so \(\Sigma_\omega\succeq\sigma^2I_{2N}\). For a block vector \(z=(z_1,\ldots,z_N)\), orthogonality of the rotations gives
\[
z^{\mathsf T}\Sigma_\omega z
\le\sigma^2\sum_i\|z_i\|^2
+\frac1{2\alpha}\left(\sum_i\|z_i\|\right)^2
\le\left(\sigma^2+\frac N{2\alpha}\right)\sum_i\|z_i\|^2.
\]
Put \(M=\sigma^2+N/(2\alpha)\). These estimates imply
\[
\det\Sigma_\omega\le M^{2N},\qquad
 y_{1:N}^{\mathsf T}\Sigma_\omega^{-1}y_{1:N}
\le\frac{\|y_{1:N}\|^2}{\sigma^2}.
\]
The Gaussian density formula consequently yields
\[
C_{\rm OU}
\ge N\log\sigma^2-N\log M
-\frac{\|y_{1:N}\|^2}{2\sigma^2},
\]
which is independent of \(\omega\) for the fixed quantities specified in the task.

## Source-Audit Notes

The source's general observation model is reduced to the public one by the fixed transformation \(Y\mapsto C^{-1}(Y-d)\). Since \(\det C=1\), this leaves the observation density normalization unchanged and does not transform the latent state or the gauges.

Three source-local corrections are used: the square-root conjugation at L000826 is \(\Lambda^{1/2}\Omega\Lambda^{-1/2}\); the subtractive term in the completed-square minimum at L000839 has factor \(\omega^2\); and the coefficient in the isotropic covariance equation at L000859 is \(A_q=B\), not \(K\). All three corrections are fixed by adjacent source equations and leave the theorem unchanged.

All theorem-critical proof obligations are closed. No specialized nonstandard external dependency is needed.
