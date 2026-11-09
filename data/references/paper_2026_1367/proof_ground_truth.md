# Reference Proof

## Proof Structure

First make the density domain explicit: strict positivity of all isotropic error variances makes both induced Gaussian covariance matrices positive definite. Then reduce equality of centered Gaussian laws to equality of covariance matrices. The smallest-eigenvalue argument identifies each isotropic error variance. Equality of the cross-block covariance yields the unique coupled invertible coordinate transformation of the two joint-loading matrices and shows that the joint rank equals the rank of the cross-block covariance. Equality of the diagonal blocks then gives exactly the positive-semidefinite residual Gram-matrix conditions. Conversely, those conditions make all covariance blocks equal.

## Complete Proof

Assume throughout that \(\sigma_k^2>0\) and \(\sigma_k^{*2}>0\) for \(k=1,2\), as required by the density formulation. Define
\[
S_k=W_{Jk}W_{Jk}^{\mathsf T}+W_{Ik}W_{Ik}^{\mathsf T},
\qquad
C_k=S_k+\sigma_k^2I_{p_k},
\]
and let the joint covariance be
\[
C=\begin{pmatrix}C_1&W_{J1}W_{J2}^{\mathsf T}\\
W_{J2}W_{J1}^{\mathsf T}&C_2\end{pmatrix}.
\]
The starred parameterization has the analogous matrices \(S_k^*,C_k^*,C^*\). Since the error covariance is positive definite and the signal covariance is positive semidefinite, both \(C\) and \(C^*\) are positive definite. Both induced laws are centered Gaussian laws, so equality of their Lebesgue densities is equivalent to \(C=C^*\).

Assume first that \(C=C^*\). Since \(S_k\succeq0\) and
\[
\operatorname{rank}(S_k)\leq\operatorname{rank}([W_{Jk},W_{Ik}])<p_k,
\]
\(S_k\) has a zero eigenvalue. Hence the smallest eigenvalue of \(C_k=S_k+\sigma_k^2I\) is \(\sigma_k^2\). The same argument applies to the starred block, so equality of diagonal blocks gives \(\sigma_k^{*2}=\sigma_k^2\) for \(k=1,2\).

Equality of the off-diagonal blocks gives
\[
W_{J1}W_{J2}^{\mathsf T}=W_{J1}^*W_{J2}^{*\mathsf T}.
\]
Because both joint-loading matrices in each block have full column rank, this cross-covariance has rank \(r_J\), its column space is the column space of \(W_{J1}\) and \(W_{J1}^*\), and its row space is the row space of \(W_{J2}^{\mathsf T}\) and \((W_{J2}^*)^{\mathsf T}\). Therefore there are invertible \(r_J\times r_J\) matrices \(T_1,T_2\) with
\[
W_{J1}^*=W_{J1}T_1,\qquad W_{J2}^*=W_{J2}T_2.
\]
Substitution into the cross-covariance and cancellation using full column rank imply
\[
T_1T_2^{\mathsf T}=I,
\]
so \(T_2=(T_1^{-1})^{\mathsf T}\). The same rank calculation shows that the joint rank is the rank of the observable cross-block covariance, namely \(r_J\), and is therefore identifiable.

Using the already identified noise variances and equality of the diagonal blocks, for each \(k\),
\[
W_{Ik}^*W_{Ik}^{*\mathsf T}
 =W_{Ik}W_{Ik}^{\mathsf T}
  +W_{Jk}W_{Jk}^{\mathsf T}
  -W_{Jk}^*W_{Jk}^{*\mathsf T}.
\]
Thus, with \(T_2=(T_1^{-1})^{\mathsf T}\),
\[
W_{I1}^*W_{I1}^{*\mathsf T}
 =W_{I1}W_{I1}^{\mathsf T}+W_{J1}(I-T_1T_1^{\mathsf T})W_{J1}^{\mathsf T},
\]
\[
W_{I2}^*W_{I2}^{*\mathsf T}
 =W_{I2}W_{I2}^{\mathsf T}+W_{J2}(I-T_2T_2^{\mathsf T})W_{J2}^{\mathsf T}.
\]
The left sides are Gram matrices, so both right sides are positive semidefinite. This proves necessity.

Conversely, suppose the two positive noise variances are equal, the joint loadings satisfy the displayed relations for an invertible \(T_1\) with \(T_2=(T_1^{-1})^{\mathsf T}\), and the two individual Gram equalities hold. Direct substitution shows \(C_1=C_1^*\) and \(C_2=C_2^*\); moreover
\[
W_{J1}^*W_{J2}^{*\mathsf T}
=W_{J1}T_1T_2^{\mathsf T}W_{J2}^{\mathsf T}
=W_{J1}W_{J2}^{\mathsf T}.
\]
Therefore \(C=C^*\). Since both covariance matrices are positive definite, the centered Gaussian densities coincide. The equivalence follows, including identifiable isotropic error variances and joint rank, together with the possible nonuniqueness of the split between joint and individual covariance components under admissible nonorthogonal transformations.
