# Reference Proof

## Obligations and source contract

The proof must establish: (i) the centered initialization law and concentration of the final-layer gradient Gram matrix; (ii) the engineered target's conditional Gaussian law and the joint limiting independence needed for the initialization error; (iii) the finite-time dynamical reduction with initialization-dependent target labels; and (iv) the converged covariance and posterior interpretation.

Stationary empirical NTK convergence along training is a public premise inherited from the source's lazy NTK regime. It is not inferred here from NTK scaling or initialization-kernel convergence alone. The generic recursive NTK theorem is not used. The previously repaired kernel-regression sign and conditional-characteristic-function independence argument are retained.

## 1. Initialization and the final-layer contribution

Fix a finite input list S of length q. Use r as an index for the collection of hidden widths. Let V_{r,j}^ell be the q-vector of preactivations of neuron j in layer ell, evaluated on S. Conditional on all parameters through layer ell-1, the vectors V_{r,j}^ell are independent centered Gaussian vectors with a common covariance C_r^ell. The first-layer covariance is deterministic:

\[
C^1=\sigma_b^2\mathbf 1\mathbf 1^{\mathsf T}
 +\frac{\sigma_w^2}{d}SS^{\mathsf T},
\]

where S in this display is the matrix with the input vectors as rows. For ell greater than one,

\[
C_r^\ell=\sigma_b^2\mathbf 1\mathbf 1^{\mathsf T}
 +\frac{\sigma_w^2}{r_{\ell-1}}
 \sum_{j=1}^{r_{\ell-1}}
 \phi(V_{r,j}^{\ell-1})\phi(V_{r,j}^{\ell-1})^{\mathsf T}.
\]

Activation is applied componentwise. Define

\[
F(C)=\sigma_b^2\mathbf 1\mathbf 1^{\mathsf T}
 +\sigma_w^2\mathbb E[\phi(V)\phi(V)^{\mathsf T}],
 \qquad V\sim\mathcal N(0,C).
\]

We claim that C_r^ell converges in probability to deterministic C^ell, recursively given by C^ell=F(C^{ell-1}). To justify the induction, condition on the parameters through layer ell-2. The summands in C_r^ell are then independent and identically distributed. Since phi is Lipschitz, |phi(v)| is bounded by a constant times 1+|v|. Gaussian fourth moments therefore bound the conditional variance of each matrix entry of a summand uniformly when C_r^{ell-1} ranges over a compact set. Conditional Chebyshev's inequality bounds the corresponding empirical-average variance by a constant divided by r_{ell-1}. Tightness of C_r^{ell-1} removes the compact-set restriction. Consequently,

\[
C_r^\ell-F(C_r^{\ell-1})\xrightarrow{p}0.
\]

The map F is continuous on positive-semidefinite matrices, including singular ones: couple V=C^{1/2}\xi with a fixed standard Gaussian vector xi, use continuity of the matrix square root, and dominate the integrands by a constant times 1+||xi||^2 on bounded sets of covariance matrices. This completes the induction. Fixed depth and divergence of every hidden width suffice for this conditional argument; no width-ratio restriction is used.

Let U_r=u_r(S;vartheta_0). Conditional on the hidden-layer parameters, U_r is centered Gaussian with covariance C_r^L. Define D_r to be the Gram matrix of gradients with respect to all final-layer weights and the final-layer bias. Direct differentiation of the publicly specified readout gives

\[
D_r=\sigma_b^2\mathbf 1\mathbf 1^{\mathsf T}
 +\frac{\sigma_w^2}{r_{L-1}}
 \sum_j v^{L-1}_j(S)v^{L-1}_j(S)^{\mathsf T}
 =C_r^L.
\]

For L=1, this identity reads D_r=C^1 and there is no limiting hidden layer. Write D=C^L. The preceding induction and conditional Gaussian characteristic functions give

\[
D_r\xrightarrow{p}D,
\qquad
U_r\Rightarrow\mathcal N(0,D).
\]

The latter assertion follows because E exp(i a^T U_r)=E exp(-a^T D_r a/2), whose bounded integrand converges in probability to exp(-a^T D a/2). A bounded random variable converging in probability to a constant converges to it in L^1. We use the finite-dimensional continuity theorem: pointwise convergence of characteristic functions to a characteristic function continuous at zero implies convergence in distribution. Here the limiting function is explicitly Gaussian.

## 2. Engineered target and joint limit

Let J_r be the q-by-p Jacobian of u_r(S;vartheta_0), with one input evaluation per row and one parameter per column. Let J_r^{pre} retain only columns belonging to layers before L, and define

\[
Q_r=J_r^{pre}(J_r^{pre})^{\mathsf T}.
\]

The parameter-block decomposition is an exact finite-width identity:

\[
K_{r,0}(S,S)=D_r+Q_r.
\]

The public NTK premise at time zero and the first part of the proof imply

\[
Q_r\xrightarrow{p}Q:=\Theta_{SS}-D.
\]

In particular Q is positive semidefinite, as a limit of Gram matrices. Conditional on the full predictor initialization vartheta_0, the target vector G_r=tilde g_r(S) is centered Gaussian with covariance Q_r: it equals J_r^{pre} psi_0^{pre}, and psi_0^{pre} is independent standard Gaussian. This proves the target's Gaussian limit by the same characteristic-function argument.

Separate Gaussian limits or zero cross-covariance would not alone prove independence. For arbitrary a,b in R^q, compute instead

\[
\begin{aligned}
\mathbb E e^{i a^{\mathsf T}U_r+i b^{\mathsf T}G_r}
 &=\mathbb E\left[e^{i a^{\mathsf T}U_r}
                 e^{-b^{\mathsf T}Q_r b/2}\right].
\end{aligned}
\]

The second factor converges in L^1 to the constant exp(-b^T Q b/2), while the first has absolute value one. Thus the displayed expectation converges to

\[
\exp(-a^{\mathsf T}Da/2)\exp(-b^{\mathsf T}Qb/2).
\]

This is the characteristic function of a jointly Gaussian pair with independent components. It follows that h_r(S):=U_r-G_r converges to a centered Gaussian vector h(S) with covariance

\[
D+Q=\Theta_{SS}.
\]

This argument applies to every finite list, in particular the concatenated list of training and test inputs, including repetitions. It also establishes tightness of h_r(X), which is needed for the dynamical argument. Finite-width independence between predictor and target is neither asserted nor required.

## 3. Training dynamics and order of limits

Write R_r(t)=u_r(X;vartheta_t)-tilde g_r(X)=epsilon_{r,t}(X). Because the target remains fixed, the exact chain-rule equations are, almost everywhere in time,

\[
\dot R_r(t)=-K_{r,t}(X,X)R_r(t),
\qquad
\frac{d}{dt}\epsilon_{r,t}(Z)=-K_{r,t}(Z,X)R_r(t).
\]

Every empirical training Gram matrix is positive semidefinite. Hence

\[
\frac{d}{dt}\|R_r(t)\|^2
 =-2R_r(t)^{\mathsf T}K_{r,t}(X,X)R_r(t)\leq0,
\]

so ||R_r(t)||<=||R_r(0)||. Let B=Theta_XX. Its symmetry and positive semidefiniteness follow from empirical Gram convergence; invertibility makes it positive definite. Fix T<infinity and put

\[
\delta_{r,AB}=\sup_{0\leq s\leq T}
 \|K_{r,s}(A,B)-\Theta_{AB}\|_{\mathrm{op}}.
\]

The public stationary-regime assumption says delta_{r,AB}->0 in probability. Variation of constants gives

\[
R_r(t)-e^{-tB}R_r(0)
 =\int_0^t e^{-(t-s)B}
    (B-K_{r,s}(X,X))R_r(s)\,ds.
\]

Since ||exp(-sB)||<=1,

\[
\sup_{t\leq T}\|R_r(t)-e^{-tB}R_r(0)\|
 \leq T\delta_{r,XX}\|R_r(0)\|\xrightarrow{p}0.
\]

The last implication uses tightness of R_r(0)=h_r(X), not independence of target labels and predictor initialization.

Integrating the test equation and using the same estimate yields, uniformly on [0,T],

\[
\epsilon_{r,t}(Z)
 =h_r(Z)-\Theta_{ZX}B^{-1}(I-e^{-tB})h_r(X)+o_p(1).
\]

For completeness, the norm of the error in replacing its integral is at most

\[
T\delta_{r,ZX}\|R_r(0)\|
 +\|\Theta_{ZX}\|T^2\delta_{r,XX}\|R_r(0)\|,
\]

which tends to zero in probability. Applying the joint initialization limit proves, at each fixed t,

\[
\epsilon_{r,t}(Z)\Rightarrow
 h(Z)-\Theta_{ZX}B^{-1}(I-e^{-tB})h(X).
\]

Now, and only now, let t tend to infinity. Positive definiteness of B implies exp(-tB)->0, so the limiting converged error is

\[
\epsilon_\infty(Z)=h(Z)-A_Zh(X),
\qquad A_Z=\Theta_{ZX}\Theta_{XX}^{-1}.
\]

This establishes the specified width-first, then time limit. No convergence of finite-width infinite-time predictors or interchange of limits is used.

## 4. Covariance and posterior law

The preceding expression is a deterministic linear map of the centered jointly Gaussian initialization-error vector. Therefore it is centered Gaussian with covariance

\[
\begin{aligned}
\operatorname{Cov}(\epsilon_\infty(Z))
 &=\Theta_{ZZ}-A_Z\Theta_{XZ}-\Theta_{ZX}A_Z^{\mathsf T}
   +A_Z\Theta_{XX}A_Z^{\mathsf T}\\
 &=\Theta_{ZZ}-\Theta_{ZX}\Theta_{XX}^{-1}\Theta_{XZ}.
\end{aligned}
\]

To identify the posterior, let F be a zero-mean GP with kernel Theta. The residual W=F(Z)-A_Z F(X) is jointly Gaussian with F(X) and has zero cross-covariance with it. They are consequently independent. Conditioning F(X)=Y thus gives F(Z) the law of A_ZY+W. Subtracting its deterministic mean A_ZY gives exactly the error law just calculated.

Singular test or posterior covariance matrices cause no difficulty: all characteristic-function arguments and Gaussian linear maps allow degenerate Gaussian laws. The formula also covers overlapping training and test points. If the training list is empty, training does nothing and the conclusion is the already-proved law h(Z)~N(0,Theta_ZZ), with the zero-dimensional matrix convention. An empty test list is vacuous. For L=1 the target is zero and the preceding argument holds exactly without a hidden-width limit. Zero scaling parameters are allowed whenever the stated training-kernel invertibility and well-definedness conditions hold.

All theorem-critical obligations are closed. No conclusion is drawn here about proving stationary NTK training from weaker architecture-only hypotheses, and no unproved full recursive NTK formula is used.
