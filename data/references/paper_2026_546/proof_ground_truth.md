# Reference Proof

## Contract and proof obligations

The upper bound uses the fixed centered embedding and the fourth-moment assumption for every empirical sample size. The lower bound uses only the population fourth moment of each specified, uncentered embedding; its covariance parameter is centered and its estimators observe only the sample array. The two moment requirements must not be conflated.

The obligations are: (1) well-defined means, embeddings and covariance operators; (2) the inter-measure Hilbert-Schmidt fluctuation bound; (3) the within-measure replacement bound; (4) admissible Gaussian alternatives; (5) a bound for the full observation-law KL divergence uniform in m; (6) covariance separation in each actual Hilbert space; and (7) a measurable testing reduction with an explicit positive constant. All seven are closed below.

## 1. Definition closure and integrability

A measurable Hilbert-valued random variable with finite fourth moment has a finite Bochner mean and finite second moment. Its centered covariance is well defined. For any orthonormal basis (e_j), Parseval gives
\[
\|u\otimes v\|_{HS}^2
=\sum_j|\langle u,e_j\rangle|^2\|v\|^2
=\|u\|^2\|v\|^2.
\]
Thus the covariance has finite Hilbert-Schmidt norm. It is positive and trace class, with trace equal to the centered second moment. These are the rank-one and trace facts needed from the operator background; no infinite-dimensional eigenvalue-ordering result is needed.

The map A is defined on measures with finite first moment. For B, the standard optimal-map result used by the source says that an absolutely continuous probability measure with finite second moment admits a unique almost-everywhere squared-cost optimal map to any probability measure with finite second moment. Here the reference is the fixed Gaussian gamma_d, which has a density and finite second moment. Also, if T pushes gamma_d to nu, then the integral of ||T||^2 is the second moment of nu, so T-Id belongs to the stated vector-valued L^2 space. The standing measurability requirement for the embeddings is retained in the task.

For C, a projected quantile has squared L^2 norm equal to the second moment of the projected distribution. Integration over the sphere is finite for nu in M_2, since |theta^T x| <= ||x||. The endpoint values are immaterial. These facts close the embedding domains without imposing compact support or regularity assumptions from the separate sampling-rate results.

## 2. Upper bound: intermediate covariance

Write Z_i=barPhi_P(mu_i)=Phi(mu_i), Zhat_i=barPhi_P(hat mu_i), and
\[
\Sigma^n=\frac1n\sum_{i=1}^n Z_i\otimes Z_i.
\]
Then E Z_i=0, Sigma_P=E[Z_i\otimes Z_i], and
\[
E\|\widehat\Sigma-\Sigma_P\|_{HS}
\le E\|\Sigma^n-\Sigma_P\|_{HS}
   +E\|\widehat\Sigma-\Sigma^n\|_{HS}.
\]
All expectations below include conditional sampling where applicable.

The independent centered Hilbert-Schmidt random operators Z_i\otimes Z_i-Sigma_P have vanishing cross inner-product expectations. Consequently,
\[
E\|\Sigma^n-\Sigma_P\|_{HS}^2
=\frac1n E\|Z\otimes Z-\Sigma_P\|_{HS}^2
=\frac1n\big(E\|Z\|^4-\|\Sigma_P\|_{HS}^2\big)
\le R/n.
\]
Taking square roots bounds the first term by R^{1/2}n^{-1/2}.

For the second term, bilinearity gives
\[
Z\otimes Z-\widehat Z\otimes\widehat Z
=(Z-\widehat Z)\otimes Z+\widehat Z\otimes(Z-\widehat Z).
\]
The rank-one norm formula, the triangle inequality and Cauchy-Schwarz therefore imply
\[
E\|\widehat\Sigma-\Sigma^n\|_{HS}
\le (E\|Z-\widehat Z\|^2)^{1/2}
\left((E\|Z\|^2)^{1/2}+(E\|\widehat Z\|^2)^{1/2}\right)
\le2R^{1/4}r_m(\Phi).
\]
Centering by the same fixed vector does not change Phi(mu)-Phi(hat mu). Adding the two bounds proves the first assertion. The proof works also when the covariance or sampling error vanishes; it divides by neither quantity.

## 3. Lower bound: alternatives and class membership

Put delta=n^{-1/2}, tau_0=1 and tau_1=1+delta. For k=0,1, define a random measure
\[
\mu=N(b,I_d),\qquad b\sim N(0,\tau_k I_d),
\]
and let P_k denote its law. Each observed group has its own independent latent b_i. Conditional observations are
\[
X_{ij}=b_i+\varepsilon_{ij},
\]
where all noises are independent N(0,I_d), independent also of the latent means. This is exactly the stipulated observation experiment, not an experiment in which b_i or mu_i are observed. Both alternatives belong to every relevant embedding domain.

For G with independent standard normal coordinates,
\[
E\|G\|^2=d,\qquad
E\|G\|^4=\sum_j EG_j^4+2\sum_{j<\ell}EG_j^2EG_\ell^2
=3d+d(d-1)=d(d+2).
\]
Hence E||b||^4=tau_k^2 d(d+2).

For A, Phi_A(mu)=b. For B, Phi_B(mu) is the constant function x mapsto b: the translation x mapsto x+b transports gamma_d to N(b,I_d) and is optimal, since every such map has cost at least ||b||^2 by Jensen and translation attains that cost. Constant vector functions have their Euclidean norm in L^2(gamma_d;R^d). Therefore, for both A and B,
\[
E\|\Phi(\mu)\|^4=\tau_k^2d(d+2)
\le4d(d+2)\le R,
\]
because n>=1 implies tau_k<=2.

For C, put q(t)=sqrt(2) erf^{-1}(2t-1), a standard-normal quantile. Thus integral q(t) dt=0 and integral q(t)^2 dt=1. Sphere symmetry gives
\[
\int\theta_j\theta_\ell\,d\sigma_{d-1}(\theta)
=\delta_{j\ell}/d:
\]
off-diagonal integrals vanish by reflection, diagonal integrals are equal by permutation symmetry, and their sum is one. These statements also hold on the two-point sphere when d=1. It follows that
\[
\|\Phi_C(N(b,I_d))\|^2=\|b\|^2/d+1,
\]
and therefore
\[
E\|\Phi_C(\mu)\|^4
=(1+2/d)\tau_k^2+2\tau_k+1
\le3\cdot4+4+1=17\le R.
\]
This calculation concerns the uncentered map, as required by the minimax class. Its population mean is q; that deterministic function disappears when forming the covariance. The alternatives' population feature means are identical under the two hypotheses: zero for A and B, and q for C. No such mean is supplied to an estimator.

The population-only class membership is all that is required here. One must not additionally demand the empirical fourth-moment bound of the upper theorem at the same numerical R.

## 4. KL divergence for the complete observed data

Let Q_k denote the law of the full array under P_k. Stacking one group produces a Gaussian vector with mean zero and covariance
\[
K_k=(I_m+\tau_k\mathbf1_m\mathbf1_m^T)\otimes I_d.
\]
Indeed the stacked vector is 1_m\otimes b_i plus independent standard Gaussian noise. Different groups are independent, so Q_k is the n-fold product of N(0,K_k).

The matrices K_k are positive definite. Along the group-mean direction, their eigenvalues are 1+m tau_k, each repeated d times; on its orthogonal complement they are one. The standard zero-mean Gaussian KL identity, whose hypothesis is positive definiteness, is
\[
\mathrm{KL}(N(0,K_1)\|N(0,K_0))
=\tfrac12\big(\operatorname{tr}(K_0^{-1}K_1)-dm
-\log\det(K_0^{-1}K_1)\big).
\]
Set x=m delta/(1+m). Only the d group-mean eigenvalues contribute, and additivity of KL for independent products gives
\[
\mathrm{KL}(Q_1\|Q_0)
=\frac{nd}{2}\big(x-\log(1+x)\big).
\]
For x>=0,
\[
x-\log(1+x)=\int_0^x\frac{t}{1+t}\,dt\le x^2/2.
\]
Since x<=delta and n delta^2=1,
\[
\mathrm{KL}(Q_1\|Q_0)\le d/4.
\]
This is a bound for the marginal observed-data experiment, uniform over every positive integer m, not a conditional KL calculation with the latent means held observed.

## 5. Exact covariance separations

For A, the standard coordinate vectors form an orthonormal basis and the centered feature is b. Consequently,
\[
\Sigma_k=\tau_k I_d,\qquad
\|\Sigma_1-\Sigma_0\|_{HS}=\sqrt d\,\delta.
\]

For B, let f_j(x)=e_j. These constant vector functions are orthonormal in L^2(gamma_d;R^d). Since the centered feature equals sum_j b_j f_j and the b_j have independent mean-zero coordinates,
\[
\Sigma_k=\tau_k\sum_{j=1}^d f_j\otimes f_j.
\]
The rank-one projections are orthonormal as Hilbert-Schmidt operators, yielding the same separation sqrt(d) delta.

For C, let f_j(theta,t)=sqrt(d) theta_j. The sphere calculation above makes these functions orthonormal. After subtracting the population mean q, the feature is
\[
\theta^Tb=\frac1{\sqrt d}\sum_{j=1}^d b_j f_j.
\]
Thus
\[
\Sigma_k=\frac{\tau_k}{d}\sum_{j=1}^d f_j\otimes f_j,
\qquad
\|\Sigma_1-\Sigma_0\|_{HS}=\delta/\sqrt d.
\]
These are direct calculations, not appeals to an unreconstructed Gaussian-spectrum proposition.

## 6. Testing reduction and explicit constants

Let Delta=||Sigma_1-Sigma_0||_{HS}>0. Given any measurable estimator T, define a test psi selecting the nearer of Sigma_0 and Sigma_1, with a fixed rule for ties. It is measurable. If psi is wrong under k, the triangle inequality implies ||T-Sigma_k||_{HS}>=Delta/2. Hence
\[
\max_k E_{Q_k}\|T-\Sigma_k\|_{HS}
\ge\frac{\Delta}{2}\max_k Q_k(\psi\ne k).
\]
The standard two-distribution testing inequality used in the source states that if KL(Q_1||Q_0)<=alpha<infinity, every test satisfies
\[
\max_k Q_k(\psi\ne k)\ge e^{-\alpha}/4.
\]
Its hypotheses hold here: Q_0 and Q_1 are probability measures on the same observed-data space with positive Gaussian densities, and the preceding calculation gives finite KL at most d/4. Therefore,
\[
\max_k E_{Q_k}\|T-\Sigma_k\|_{HS}
\ge\Delta e^{-d/4}/8.
\]
Both P_k lie in the appropriate class. Taking the supremum over that class and then the infimum over estimators proves the claim with
\[
C_{\Phi_A,d}=C_{\Phi_B,d}=\frac{\sqrt d}{8}e^{-d/4},
\qquad
C_{\Phi_C,d}=\frac{1}{8\sqrt d}e^{-d/4}.
\]
They are strictly positive for every positive integer d and independent of n, m and R. The membership calculations include the threshold values of R and the boundary n=m=d=1. No dense-sampling inequality is an assumption of this finite-sample lower bound.

## Source-local repairs used

In the source's two A/B moment-bound displays, replace the erroneous baseline s^(1) in s^(1)+epsilon and s^(1)+1 by s. The correct bound is (s^(k))^2<=(s+epsilon)^2<=(s+1)^2, exactly the expression controlled by the stated admissible interval. The source's missing spherical coordinate in the Gaussian SW proposition is f_j(theta,t)=sqrt(d) theta_j, as explicitly given in its proof. Its scalar normal quantile formula is understood with N(a,sigma^2) and a+sigma q(t), before substituting the projected mean and variance. These recorded local corrections introduce neither a new construction nor a stronger hypothesis.
