# Problem

## Setup

For each of two systems \(m\in\{A,B\}\), let \(Y_m\in\{0,1\}\) be its true binary outcome and let \(\widetilde Y_m\in\{0,1\}\) be a binary evaluation label. Define
\[
\theta_m=\Pr(Y_m=1),\qquad
q_{1,m}=\Pr(\widetilde Y_m=1\mid Y_m=1),\qquad
q_{0,m}=\Pr(\widetilde Y_m=0\mid Y_m=0).
\]
When a conditioning event \(Y_m=r\) has probability zero, \(q_{r,m}\) denotes a specified fixed value in \([0,1]\) for that part of the conditional label distribution; the calibration-consistency assumption below refers to that same value. On positive-probability conditioning events, these are ordinary conditional probabilities. Write
\[
J_m=q_{0,m}+q_{1,m}-1,
\qquad
p_m=\Pr(\widetilde Y_m=1)=\theta_mJ_m+1-q_{0,m}.
\]

Suppose a test sample for A supplies its evaluation-label sample proportion \(\widehat p_A\), and separate calibration samples for A and B supply conditional sample proportions \(\widehat q_{0,m},\widehat q_{1,m}\). An empirical conditional proportion is assigned the value \(0\) when its calibration stratum is empty. Assume that, for each model, the fractions of its calibration sample in the two true-label strata converge in probability to strictly positive constants. As the A test-sample size and both calibration-sample sizes tend to infinity, assume
\[
\widehat p_A\xrightarrow{p}p_A,
\qquad
\widehat q_{r,m}\xrightarrow{p}q_{r,m}\quad(r\in\{0,1\},\ m\in\{A,B\}).
\]
Assume \(J_A\ne0\) and \(J_B\ne0\). On outcomes where the respective denominator is nonzero, define
\[
\widehat\theta_A^{\rm own}
=\frac{\widehat p_A+\widehat q_{0,A}-1}
{\widehat q_{0,A}+\widehat q_{1,A}-1},
\qquad
\widehat\theta_A^{\rm shared}
=\frac{\widehat p_A+\widehat q_{0,B}-1}
{\widehat q_{0,B}+\widehat q_{1,B}-1}.
\]
Set each estimator to \(0\) when its respective denominator is zero. Finally, write
\[
\Delta q_r=q_{r,A}-q_{r,B}\quad(r\in\{0,1\}),
\qquad
\Delta J=J_A-J_B.
\]

## Task

Prove that \(\widehat\theta_A^{\rm own}\xrightarrow{p}\theta_A\) and that the asymptotic bias incurred by using B's calibration for A, understood as the following limiting error in probability, is
\[
\widehat\theta_A^{\rm shared}-\theta_A
\xrightarrow{p}
\frac{\theta_A\Delta J-\Delta q_0}{J_B}
=
\frac{\theta_A\Delta q_1-(1-\theta_A)\Delta q_0}{J_B}.
\]
Conclude from this identity that calibration mismatch is scaled by the reciprocal of the shared calibration quality index \(J_B\).
