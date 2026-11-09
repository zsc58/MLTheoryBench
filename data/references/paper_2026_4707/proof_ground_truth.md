# Reference Proof

## Proof Structure

Rewrite the conditional error terms using the positive class probabilities and calibration. Identify the three pointwise action costs and construct a measurable minimizing policy to establish attainment and the value formula. Compare the affine costs in both positive-weight regimes, including coincident thresholds, and then handle zero weights using constant policies. Boundary actions must minimize the cost even when the score distribution has atoms.

## Complete Proof

### 1. Calibration reduction

Put \(a=\lambda_1/\alpha_0\) and \(b=\lambda_2/\alpha_1\). These are finite nonnegative real numbers. Calibration gives
\[
\mathbb E[\mathbf 1\{Y=0\}\mid S]=1-S,
\qquad
\mathbb E[\mathbf 1\{Y=1\}\mid S]=S.
\]
For an admissible policy, the action indicators are measurable functions of \(S\). Therefore
\[
\begin{aligned}
\lambda_1\Pr(\pi(S)=\mathsf A\mid Y=0)
&=a\,\mathbb E[\mathbf 1\{\pi(S)=\mathsf A\}\mathbf 1\{Y=0\}]\\
&=a\,\mathbb E[\mathbf 1\{\pi(S)=\mathsf A\}(1-S)],
\end{aligned}
\]
and similarly
\[
\lambda_2\Pr(\pi(S)=\mathsf R\mid Y=1)
=b\,\mathbb E[\mathbf 1\{\pi(S)=\mathsf R\}S].
\]
Define
\[
c_{\mathsf V}(s)=1,\qquad
c_{\mathsf A}(s)=a(1-s),\qquad
c_{\mathsf R}(s)=bs.
\]
Then
\[
J(\pi)=\mathbb E[c_{\pi(S)}(S)].
\]
All these costs are measurable and bounded, so the expectations are finite.

### 2. Measurable minimization and the value

Let
\[
m(s)=\min\{1,a(1-s),bs\}.
\]
Every admissible policy satisfies \(c_{\pi(s)}(s)\ge m(s)\), and hence \(J(\pi)\ge\mathbb E[m(S)]\).

To attain this bound, fix an ordering of the three actions and at each score choose the first action attaining \(m(s)\). Each selection region is a finite combination of comparisons of continuous functions, so this selector is Borel measurable. It is therefore an admissible deterministic policy and has cost \(m(s)\) at every score. Consequently,
\[
\inf_\pi J(\pi)=\min_\pi J(\pi)
=\mathbb E\!\left[\min\{1,a(1-S),bS\}\right].
\]
This proves attainment without interchanging an infimum and expectation without justification. A fixed tie rule is sufficient; an unrestricted selection from ties need not be measurable.

### 3. Threshold policies for positive weights

Assume \(a,b>0\), and define
\[
L=\frac1b,\qquad H=1-\frac1a.
\]
The verification cost is no larger than rejection exactly when \(s\ge L\), and no larger than acceptance exactly when \(s\le H\).

First suppose \(L\le H\). Since \(L>0\) and \(H<1\), this condition implies
\[
0<L\le H<1.
\]
No endpoint clipping is necessary. For \(s<L\),
\[
bs<1<a(1-s),
\]
so rejection is optimal. For \(L\le s\le H\), both other costs are at least one, so verification is optimal. For \(s>H\),
\[
a(1-s)<1<bs,
\]
so acceptance is optimal. Choose \(t_{\rm low}=L\) and \(t_{\rm high}=H\).

If \(L<H\), rejection and verification tie at \(L\), and acceptance and verification tie at \(H\); either minimizing action may be chosen at the corresponding boundary. If \(L=H\), all three costs equal one at the common threshold, so any of the three boundary actions is optimal. These choices remain valid even when the score distribution has atoms at the boundaries.

Now suppose \(L>H\). Multiplying the inequality \(1/b>1-1/a\) by \(ab>0\) gives \(a+b>ab\). Set
\[
c=\frac{a}{a+b}\in(0,1),\qquad
k=\frac{ab}{a+b}<1.
\]
The acceptance and rejection costs agree at \(c\), both equaling \(k\). If \(s\le c\), then
\[
bs\le a(1-s),\qquad bs\le bc=k<1.
\]
Thus rejection is minimizing on that side. If \(s\ge c\), then
\[
a(1-s)\le bs,\qquad a(1-s)\le a(1-c)=k<1.
\]
Thus acceptance is minimizing on that side. Choose \(t_{\rm low}=t_{\rm high}=c\), reject below \(c\), accept above \(c\), and choose either rejection or acceptance at \(c\). Verification is strictly more costly there and must not be selected at the common threshold. This policy has an empty verification region and is pointwise optimal.

### 4. Zero weights and endpoint thresholds

If \(a=0\), acceptance has cost zero everywhere. Choose the constant acceptance policy and \(t_{\rm low}=t_{\rm high}=0\), with acceptance also at the boundary score zero. This covers \(a=b=0\).

If \(a>0\) and \(b=0\), rejection has cost zero everywhere. Choose the constant rejection policy and \(t_{\rm low}=t_{\rm high}=1\), with rejection also at the boundary score one.

These are admissible measurable threshold policies under the stated boundary convention. Together with the positive-weight cases, they establish the threshold assertion for every permitted pair of weights. Every constructed policy attains the value proved in Section 2.

## Source Alignment and Obligation Closure

The conditional-probability reduction is derived from the population setup and calibration, as in source L000283-L000310. The affine comparisons use L000313-L000320. The complementary positive-weight case is supplied by the elementary comparison above, preserving the previously recorded repair. The endpoint convention reconciles the literal closed-interval display at L000098 with the source's constant policies at L000313 and its boundary tie-breaking at L000320. Positive class probabilities, already made explicit in the task, follow the convention at L000285.

The proof explicitly closes normalization, calibration conditioning, measurable attainment, both positive-weight regimes, coincident thresholds, zero weights, and boundary atoms. It uses no sequential algorithm, concentration theorem, or unresolved external dependency.
