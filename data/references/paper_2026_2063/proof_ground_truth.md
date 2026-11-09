# Reference Proof

## Audited dependencies and obligations

The obligations are: (1) conditional-mean and second-order remainder identities for the four links; (2) unrestricted population minimization and the truth excess-risk identity; (3) a well-defined zero mixed nuisance/target derivative; (4) compact-domain regularity; (5) a conditional evaluation-fold learning bound; and (6) the probability and nuisance-error bookkeeping for the average of the two fits. All are closed below. The only independent statistical result used is stated explicitly next. We do not treat the source's bare invocation of an external orthogonal-learning theorem as a complete statement of that theorem.

### Standard independent localized deviation theorem

Let (X_i,W_i), i=1,...,m, be independent copies of (X,W), with |W|<=B. Let F be a deterministic measurable class of functions bounded by M>=1, and let f_* belong to F. Define

H={a(f-f_*)/(2M): f in F, 0<=a<=1},

R_m(s)=E sup_{h in H, ||h||_2<=s}|m^{-1} sum_i epsilon_i h(X_i)|,

where the epsilon_i are independent uniform signs, independent of the observations, and the supremum is measurable. For any deterministic r>=m^{-1/2} satisfying R_m(r)<=r^2, and every epsilon in (0,1), with probability at least 1-epsilon, simultaneously for all f in F,

|(P_m-P)[(W-f(X))^2-(W-f_*(X))^2]|
<= (1/4)||f-f_*||_2^2 + C(B,M)[r^2+log(1/epsilon)/m].

Here P_m is the empirical average and P is expectation. The comparator need not equal E[W|X], and F need not be convex. This is the standard quadratic-offset version of the localized bounded-class empirical-process inequality. Its applicable structure is bounded squared-loss differences, Lipschitz dependence on f, variance bounded by a constant times ||f-f_*||_2^2, and the displayed localized Rademacher fixed-point inequality. The star-shaped class permits enlargement of the radius by a constant depending on B and M, so the numerical constant in the fixed-point inequality is immaterial to the conclusion. The floor m^{-1/2} absorbs fixed additive confidence constants. This general independent result, rather than a target-specific oracle inequality, is the external dependency used below.

## 1. Conditional means and remainder

Fix one of the four maps and write psi for it. Suppress X in nuisance evaluations. Set q=(q_1,q_0), p=(p_1,p_0), Delta=p-q, a_1=partial_1 psi, and a_0=partial_2 psi. Conditional expectation gives

E[T(Y-q_1)/pi|X]=(e/pi)Delta_1,

E[(1-T)(Y-q_0)/(1-pi)|X]=((1-e)/(1-pi))Delta_0.

Consequently,

m_eta=psi(q)+a_1(q)(e/pi)Delta_1+a_0(q)((1-e)/(1-pi))Delta_0.

Use Taylor's theorem in its integral form:

psi(p)=psi(q)+a_1(q)Delta_1+a_0(q)Delta_0
+integral_0^1 (1-t) Delta^T H_psi(q+t Delta)Delta dt.

The integral form avoids any measurable-selection issue for a mean-value intermediate point. Therefore

R_eta=a_1(q)((e-pi)/pi)Delta_1
+a_0(q)((pi-e)/(1-pi))Delta_0
-integral_0^1 (1-t) Delta^T H_psi(q+t Delta)Delta dt,

and m_eta=theta+R_eta.

All four specified maps are smooth on (0,1)^2. Their gradients and Hessians are bounded on [c_0,1-c_0]^2, and the whole segment q+t Delta lies in that square. Inverse propensity denominators are bounded by c_0^{-1}. Hence

|R_eta|<=C(c_0,psi)(|e-pi|(|Delta_1|+|Delta_0|)+|Delta|_2^2).

This is the required cross-product plus quadratic structure, uniformly over admissible nuisances. In particular R_eta=0 when both outcome regressions are correct, with no requirement that pi=e. At the true nuisance, m_eta_0=theta. Correct propensity alone does not generally eliminate the quadratic term; no such property is claimed or needed.

Writing d_eta=eta-eta_0 and using elementary product bounds also gives

|R_eta(X)|<=C|d_eta(X)|_2^2,

so

||R_eta||_2<=C(E_X|d_eta(X)|_2^4)^{1/2}=C||eta-eta_0||_G^2.                 (A)

For an estimated nuisance trained on an independent fold, these identities hold conditional on that training information, with a fresh observation or an evaluation-fold observation.

## 2. Population risk and orthogonality

The pseudo-outcomes are uniformly bounded under the probability boundary, so their conditional means and variances exist. For f in L2(P_X), conditional variance decomposition yields

L(f,eta)=E[Var(phi(Z;eta)|X)]+||f-m_eta||_2^2.

Thus m_eta is the minimizer over L2(P_X), unique up to P_X-null sets. It is also the minimizer among all measurable functions, allowing infinite risks. It need not belong to F for misspecified eta. At eta_0, m_eta_0=theta, so

L(f,eta_0)-L(theta,eta_0)=||f-theta||_2^2.

For h in L2(P_X),

D_f L(f,eta)[h]=-2E[(phi(Z;eta)-f(X))h(X)].

At f=theta and eta=eta_0 this is zero. For a bounded measurable nuisance direction k, the path eta_0+s k stays in a compact subset of (0,1)^3 for sufficiently small |s|. The remainder bound gives

|R_{eta_0+s k}(X)|<=Cs^2|k(X)|_2^2.

Consequently,

|D_f L(theta,eta_0+s k)[h]-D_f L(theta,eta_0)[h]|
<=Cs^2 ||h||_2 ||k||_G^2.

Dividing by s and taking the limit proves

D_eta D_f L(theta,eta_0)[h,k]=0.

This argument also justifies passage through expectation. Equivalently one can differentiate the explicit smooth pseudo-outcome and use domination. The mixed derivative extends continuously to k in L4(P_X;R^3); bounded directions are dense there, and the extension is identically zero. Thus the derivative convention in the task is satisfied without asserting that every unbounded L4 direction generates a two-sided probability-valued linear path.

## 3. Regularity for all four targets

For each target, phi(Z;eta) is smooth in the three nuisance coordinates on (0,1)^3. This follows from the actual rational and logarithmic formulas, not merely from a bound on the first two derivatives of psi. Since T and Y have only four possible pairs and the nuisance cube is compact, there are finite constants B_phi and K_phi, depending only on c_0 and the map, such that

|phi(Z;eta)|<=B_phi,

||H_eta phi(Z;eta)||_op<=K_phi.

In particular the higher derivatives of psi that arise on differentiating its gradient are also bounded. For f_1,f_2 in F,

|(phi-f_1)^2-(phi-f_2)^2|
<=2(B_phi+M)|f_1-f_2|.

The target Hessian is exactly

D_f^2 L(f,eta)[h,h]=2||h||_2^2,

which establishes both the target smoothness and strong convexity used in the source. Finally,

|D_eta^2 D_f L(theta,bar eta)[h,k,k]|
<=2K_phi E[|h(X)||k(X)|_2^2]
<=2K_phi ||h||_2 ||k||_G^2.

This verifies the higher mixed-derivative estimate for each of the four maps. All constants are uniform over the admissible nuisance cube.

## 4. Evaluation-fold bound

Fix a fold j and condition on its nuisance-training observations and any training randomness. The nuisance eta_hat^(j) is now fixed. The observations indexed by I_j remain independent copies of Z, and W_i=phi(Z_i;eta_hat^(j)) are bounded by the deterministic B_phi. F and theta are deterministic, theta belongs to F, and all required suprema and ERMs are measurable by the task's typing assumptions. The localized class and its radius concern only F, theta, and P_X, and are unaffected by this conditioning.

Apply the stated independent deviation theorem with m=m_j, f_*=theta, and r=r_n. With conditional probability at least 1-epsilon, the deviation bound holds for every f in F. Put f=theta_hat^(j) and d=f-theta. By exact empirical risk minimization,

P_{I_j}[(phi-f)^2-(phi-theta)^2]<=0.

Therefore

L(f,eta_hat^(j))-L(theta,eta_hat^(j))
<= (1/4)||d||_2^2+A_j,

where A_j=C[r_n^2+log(1/epsilon)/m_j]. Conditional on the training information, the left side equals

||d||_2^2-2E_X[d(X)R_{eta_hat^(j)}(X)].

Using 2ab<=(1/4)a^2+4b^2 gives

(1/2)||d||_2^2<=A_j+4||R_{eta_hat^(j)}||_2^2.

By (A),

||theta_hat^(j)-theta||_2^2
<=2A_j+C||eta_hat^(j)-eta_0||_G^4.                 (B)

The conditional failure probability is bounded by epsilon for every realized training fit. Integrating gives the same unconditional failure bound. No event controlling the first-stage error is needed: that error remains a random quantity on the right side.

## 5. Cross-fitting, confidence, and constants

Use epsilon=delta/2 in the two applications of (B). Their good events intersect with probability at least 1-delta, without any independence claim about the two fitted estimators. Since theta_hat=(theta_hat^(1)+theta_hat^(2))/2,

||theta_hat-theta||_2^2
<= (1/2)sum_{j=1}^2 ||theta_hat^(j)-theta||_2^2.

The average need not belong to F; the last inequality holds nonetheless. The nuisance terms average to the defined E_n^4. For n>=2, each m_j>=n/3. Also r_n^2>=1/m_j for both folds, so the additive log 2 contribution is absorbed by a constant times r_n^2. Thus

||theta_hat-theta||_2^2
<=C_1[r_n^2+log(1/delta)/n]+C_2 E_n^4
=C_1[delta_n^2/M^2+log(1/delta)/n]+C_2 E_n^4.

The expectation in the norm is over an independent test covariate with the fitted functions held fixed. Constants depend only on c_0, M, and the chosen map, not on n, delta, or the nuisance-fitting algorithms.

If all four targets are fitted on the same sample, use epsilon=delta/8 for the eight target/fold applications. A union bound gives the four conclusions on a common event of probability at least 1-delta. The fixed log 8 contribution is again absorbed by the radius floor; constants can be enlarged by a fixed numerical factor. This completes all obligations.
