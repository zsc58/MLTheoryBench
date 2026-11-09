# Reference Proof

## Proof Structure and Obligations

1. Verify the population measurement relation and the own-calibration population correction, including the interpretation of null population strata.
2. Check that the empirical quantities and corrected estimators are defined everywhere, and that exceptional sample events do not affect their probability limits.
3. Obtain joint convergence from the finitely many stated consistency assumptions and apply continuous mapping at nonzero population denominators.
4. Subtract the shared-calibration population limit from the target with the correct sign, preserving the distinct A and B parameters.
5. Rewrite the mismatch numerator and interpret the reciprocal factor without asserting expectation convergence or unavoidable nonzero bias.

## Complete Proof

For system A, partitioning by its true binary outcome gives
\[
p_A=\theta_A q_{1,A}+(1-\theta_A)(1-q_{0,A})
    =\theta_AJ_A+1-q_{0,A}.
\]
If a true-label class has probability zero, its term in this partition is zero. Thus the identity also holds at boundary accuracies under the specified conditional-law convention. No division by \(\theta_A\) or \(1-\theta_A\) is used.

The prescribed value on an empty calibration stratum makes every empirical conditional proportion a random variable. To verify that such exceptional samples have vanishing probability, let \(S_{r,m}\) denote the fraction of model \(m\)'s calibration sample in stratum \(r\), and let its strictly positive probability limit be \(s_{r,m}\). Then
\[
\Pr(S_{r,m}=0)
\leq \Pr\bigl(|S_{r,m}-s_{r,m}|\geq s_{r,m}/2\bigr)
\longrightarrow 0.
\]
Consequently a fixed convention on empty strata does not affect an otherwise established probability limit. The consistency of the conditional proportions is explicitly assumed in the task; it is not inferred from stratum positivity alone.

Set
\[
\widehat J_m=\widehat q_{0,m}+\widehat q_{1,m}-1.
\]
The assumed convergences imply \(\widehat J_m\xrightarrow{p}J_m\). Since \(J_m\ne0\),
\[
\Pr(\widehat J_m=0)
\leq\Pr\bigl(|\widehat J_m-J_m|\geq |J_m|/2\bigr)
\longrightarrow0.
\]
Thus the assigned estimator values on zero-denominator events do not change the limits. This argument does not assert that the empirical denominators are nonzero for every sample, nor does it condition on their being nonzero.

Here is the standard probability result used for the plug-in step: if a finite-dimensional random vector \(X_n\) converges in probability to a constant \(x\), and a measurable map \(f\) is continuous at \(x\), then \(f(X_n)\) converges in probability to \(f(x)\). Componentwise convergence in probability to constants implies this vector convergence: for every \(\varepsilon>0\), the probability that the maximum componentwise error exceeds \(\varepsilon\) is at most the sum of the corresponding componentwise probabilities.

Apply this fact to
\[
\widehat X=(\widehat p_A,\widehat q_{0,A},\widehat q_{1,A},
\widehat q_{0,B},\widehat q_{1,B})
\xrightarrow{p}
(p_A,q_{0,A},q_{1,A},q_{0,B},q_{1,B}).
\]
No independence between these components is needed. Define the ratio map to have value zero when its denominator is zero, as in the task. This map is measurable and is continuous at each population argument used here because the corresponding \(J_m\) is nonzero. All continuous-mapping hypotheses are therefore satisfied, and
\[
\widehat\theta_A^{\rm own}\xrightarrow{p}
\frac{p_A+q_{0,A}-1}{J_A}
=\frac{\theta_AJ_A}{J_A}=\theta_A,
\]
while
\[
\widehat\theta_A^{\rm shared}\xrightarrow{p}
\frac{p_A+q_{0,B}-1}{J_B}.
\]
The own-calibration convergence also shows that the difference between the shared and own estimators has the same limit as the shared estimator's error relative to \(\theta_A\).

Subtracting \(\theta_A\) from the shared-calibration population limit gives
\[
\begin{aligned}
\frac{p_A+q_{0,B}-1}{J_B}-\theta_A
&=\frac{\theta_AJ_A+1-q_{0,A}+q_{0,B}-1}{J_B}-\theta_A\\
&=\frac{\theta_AJ_A-(q_{0,A}-q_{0,B})-\theta_AJ_B}{J_B}\\
&=\frac{\theta_A\Delta J-\Delta q_0}{J_B}.
\end{aligned}
\]
Since
\[
\Delta J=(q_{0,A}-q_{0,B})+(q_{1,A}-q_{1,B})
=\Delta q_0+\Delta q_1,
\]
this equals
\[
\frac{\theta_A\Delta q_1-(1-\theta_A)\Delta q_0}{J_B}.
\]
This proves both displayed forms of the asserted limiting error.

The exact signed factor multiplying the mismatch numerator is \(1/J_B\); its magnitude is \(1/|J_B|\). Thus a small nonzero absolute value of the shared index produces a large reciprocal factor. This does not imply that every nonzero mismatch produces nonzero bias, because the numerator can cancel. It also does not establish monotonicity of bias across arbitrary changes in all parameters. Negative nonzero indices are permitted. The result is pointwise for fixed population parameters, not a uniform statement over indices approaching zero. Finally, the claimed asymptotic bias is the specified probability limit, not a limit of expectations; no uniform-integrability assertion is required or made.
