# Reference Proof

## Proof Structure and Obligations

The proof must establish: (1) normalization of the reward-weighted law and its condition marginal; (2) the marginal change-of-measure identity under the common forward kernel; (3) its expression as a source posterior expectation; (4) the score decomposition and removal of the condition-only normalizer; and (5) identification of every population minimizer up to the objective measure's null sets. All five obligations are derived below.

The source's weighted-denoising calculation is also reconstructed in a separate auxiliary section with its precise hypotheses. The public theorem does not assume those hypotheses, and its proof does not invoke an unverified global denoising-loss equivalence.

## Complete Proof

### Step 1: Normalize the target and transfer the marginal law

For almost every relevant condition, set
\[
w(z,c)=\frac{\exp(R(z,c)/\tau)}{A(c)}.
\]
This is a positive finite function on the source support. It is a version of the density ratio \(Q/P\); there is no need to divide by a zero source density. By the definition of \(A\),
\[
\int Q(z,c)\,dz
=\frac{P(c)}{A(c)}\int P(z\mid c)\exp(R(z,c)/\tau)\,dz
=P(c).
\]
Consequently \(Q\) is a probability density, its condition marginal equals that of \(P\), and
\[
Q(z\mid c)=w(z,c)P(z\mid c).
\]
Applying the common forward kernel therefore gives
\[
Q_t(x\mid c)=\int K_t(x\mid z)w(z,c)P(z\mid c)\,dz.
\]
This is the required target-to-source change of measure at the marginal level. All integrands in this step are nonnegative, so no signed integral interchange or subtraction of infinite quantities is involved.

### Step 2: Identify the posterior density ratio

At a point where the source posterior is defined, put
\[
D(x,c,t)=\mathbb E_{P(z\mid x,c,t)}[w(z,c)].
\]
Substituting the normalized posterior formula yields
\[
\begin{aligned}
P_t(x\mid c)D(x,c,t)
&=\int P(z\mid c)K_t(x\mid z)w(z,c)\,dz\\
&=Q_t(x\mid c).
\end{aligned}
\]
In particular,
\[
D(x,c,t)=\frac{Q_t(x\mid c)}{P_t(x\mid c)}.
\]
The positive finite weight \(w\) also implies equivalence of the source and target joint laws on their supports. Applying their common kernel preserves equivalence of the noised joint laws. Thus the use of a source posterior causes no missing target-positive support case. The explicit public regularity assumptions ensure that all logarithms and gradients used below are defined on a set of full objective measure.

### Step 3: Differentiate the marginal identity

On that full-measure set, the previous identity gives
\[
\log Q_t(x\mid c)=\log P_t(x\mid c)+\log D(x,c,t).
\]
Ordinary differentiation in \(x\), with \(c,t\) fixed, yields
\[
\nabla_x\log Q_t(x\mid c)
=\nabla_x\log P_t(x\mid c)+\nabla_x\log D(x,c,t).
\]
This differentiates an identity between the marginal and posterior-expectation functions. It does not exchange a gradient with an integral and does not require differentiability of the forward-kernel density.

### Step 4: Substitute the reward ratio

Because \(A(c)\) does not depend on \(z\) or \(x\),
\[
D(x,c,t)=\frac{1}{A(c)}\,
\mathbb E_{P(z\mid x,c,t)}\!\left[\exp(R(z,c)/\tau)\right].
\]
The derivative of \(\log A(c)\) with respect to \(x\) is zero. Hence
\[
\nabla_x\log Q_t(x\mid c)
=\nabla_x\log P_t(x\mid c)
+\nabla_x\log\mathbb E_{P(z\mid x,c,t)}\!\left[\exp(R(z,c)/\tau)\right].
\]
No differentiability of the reward in \(z\) or \(c\) is needed.

### Step 5: Identify every optimizer

Let \(s_Q(x,c,t)\) be the finite jointly measurable version of \(\nabla_x\log Q_t(x\mid c)\), extended arbitrarily on its exceptional set. The optimization domain contains \(s_Q\), and \(L(s_Q)=0\). Since \(L\) is nonnegative, its minimum is zero and every minimizer \(u^*\) satisfies
\[
\int\mu(dt)\,Q_t(dx,dc)\,\lambda(t)
\|u^*(x,c,t)-s_Q(x,c,t)\|^2=0.
\]
A nonnegative measurable function with zero integral vanishes almost everywhere. Since \(0<\lambda(t)<\infty\), this proves \(u^*=s_Q\) for \(\mu(dt)Q_t(dx,dc)\)-almost every triple. Combining this with Step 4 proves the claimed formula.

This argument does not require integrability of \(\|s_Q\|^2\) by itself: the admissible field \(s_Q\) has exactly zero error. It makes no assertion at exceptional times, at zero-probability conditions, or outside the support of the objective measure. A reward depending only on the condition gives \(Q=P\) and zero guidance, as the same formulas show.

## Auxiliary Audit of the Source's Denoising Route

This section preserves the weighted-posterior calculation appearing in the source while stating exactly when its global loss interpretation is justified. Its additional hypotheses are not assumptions of the public task and are not needed in Steps 1-5.

Suppose additionally that the forward densities are differentiable in \(x\), that their scores
\[
g_t(x,z)=\nabla_x\log K_t(x\mid z)
\]
have measurable versions on the positive-density support, and that differentiation under the defining marginal integrals is valid for both source and target:
\[
\nabla_x\int K_t(x\mid z)B(z\mid c)\,dz
=\int\nabla_xK_t(x\mid z)B(z\mid c)\,dz,
\qquad B\in\{P,Q\}.
\]
Suppose also that
\[
\int\mu(dt)\lambda(t)
\mathbb E_{Q(dz,dc)K_t(dx\mid z)}\|g_t(x,z)\|^2<\infty.
\]
These explicit hypotheses are sufficient for the following standard conditional denoising identity.

Normalizing the target posterior and using the target differentiation identity gives
\[
\mathbb E_{Q(z\mid x,c,t)}[g_t(x,z)]
=\frac{\int Q(z\mid c)\nabla_xK_t(x\mid z)\,dz}{Q_t(x\mid c)}
=s_Q(x,c,t).
\]
At zeros of a differentiable nonnegative kernel density, its gradient is zero, so the kernel-score representation is used only where needed. Conditional square expansion now gives
\[
\mathbb E_{Q(z\mid x,c,t)}\|u-g_t\|^2
=\|u-s_Q\|^2+
\mathbb E_{Q(z\mid x,c,t)}\|g_t-s_Q\|^2,
\]
because the conditional cross term is zero. Integrating this nonnegative conditional identity yields
\[
\widetilde L(u)=L(u)+C,
\quad
C=\int\mu(dt)\lambda(t)
\mathbb E_{Q(dz,dc)K_t(dx\mid z)}\|g_t-s_Q\|^2<\infty.
\]
The assumed kernel-score second moment and conditional square expansion imply finiteness of \(C\). Changing measure using \(Q=wP\) and the common kernel gives exactly
\[
\widetilde L(u)=\int\mu(dt)\lambda(t)
\mathbb E_{P(dz,dc)K_t(dx\mid z)}
\left[w(z,c)\|u(x,c,t)-g_t(x,z)\|^2\right].
\]
Thus, under these auxiliary hypotheses, the two global objectives have the same minimizers.

Furthermore, Bayes normalization gives
\[
Q(z\mid x,c,t)=\frac{w(z,c)}{D(x,c,t)}P(z\mid x,c,t).
\]
Consequently the conditional mean, equivalently the pointwise minimizer of the weighted quadratic, is
\[
s_Q(x,c,t)=
\frac{\mathbb E_{P(z\mid x,c,t)}[w(z,c)g_t(x,z)]}
{\mathbb E_{P(z\mid x,c,t)}[w(z,c)]}.
\]
Writing \(s_P=\nabla_x\log P_t(x\mid c)\), differentiation of \(D=Q_t/P_t\) with the assumed marginal derivative formulas yields
\[
\nabla_xD
=\mathbb E_{P(z\mid x,c,t)}[w(z,c)g_t(x,z)]-D s_P.
\]
This is the same posterior differentiation calculation obtained from
\(\nabla_x\log P(z\mid x,c,t)=g_t-s_P\) when differentiation of the posterior expectation is justified. Dividing by \(D\) recovers the score decomposition in Step 3.

Without a finite score-independent residual, one cannot infer equality of global argmin sets merely by writing that two losses differ by a constant: the denoising loss can be infinite for every field. Nor does marginal differentiability alone imply differentiability or a valid differentiation-under-the-integral formula for the kernel. Steps 1-5 avoid both problems and close the public theorem without these additional hypotheses.

## Dependency and Source Notes

The conditional denoising identity indexed by theory_013 is proved explicitly in the auxiliary section rather than imported with unchecked hypotheses. The framework indexed by theory_014 supplies historical context; no unexpanded specialized result from it is required for the proof. The elementary change-of-measure and Bayes calculations underlying theory_011 and theory_012 are derived explicitly above.

The normalization used throughout is the conditional partition function defined at source L000121-L000124. The incidental expression at L000510 instead integrates a joint density and differs by the condition marginal. It is not used to redefine the reward-weighted law; the density-ratio lemma itself does not require that expression, and a positive condition-only factor cannot affect an \(x\)-score. The existing notational source repairs for theory_006 and theory_012 remain unchanged.

There are no unresolved theorem-critical proof obligations.
