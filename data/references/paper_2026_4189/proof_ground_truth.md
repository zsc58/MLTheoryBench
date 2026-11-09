# Reference Proof

## Proof Structure

Show that a zero conditional leakage score forces zero averaged conditional mutual information in every model. Convert this to conditional independence, combine it with the factorized prior and shared marginal model, apply Bayes' rule, and integrate the resulting invariant posterior against the fixed predictive kernel. Finally verify the product-measure null sets in the parity statement.

## Complete Proof

Fix the policy throughout and assume $F_c(\pi_d)=0$. For each model $m$, write
\[
e_m(t)=I_m(D;\phi\mid\theta=t,\pi_d)\geq 0,
\]
where this is mutual information under the conditional joint law at the fixed value $t$. The score definition gives
\[
\max_{m\in\mathbb M}\int e_m(t)p(t)\,dt=0.
\]
Every integral is nonnegative, so every model has $\int e_m(t)p(t)\,dt=0$. A nonnegative measurable function with integral zero vanishes almost everywhere. Thus $e_m(t)=0$ for $p(\theta)$-almost every $t$, separately for every model $m$. Equivalently, the conventional, already-averaged conditional mutual information satisfies
\[
I_m(D;\phi\mid\theta,\pi_d)=0.
\]
There is no need for a common exceptional set across models.

The standard zero-CMI characterization states that, for random variables with the relevant regular conditional laws, $I(X;Y\mid T)=0$ if and only if the conditional joint law of $(X,Y)$ given $T=t$ is the product of its conditional marginals for almost every $t$. The task supplies these conditional laws, and the preceding paragraph verifies the zero-information hypothesis. Hence $D$ and $\phi$ are conditionally independent given $\theta$ in each model.

The prior factorization gives $p_m(\phi\mid\theta)=p_m(\phi)$ almost surely, and the shared marginal assumption gives the conditional dataset law $p(D\mid\theta,\pi_d)$ in every model. Conditional independence therefore yields the joint-law factorization
\[
p_m(\theta,\phi,D\mid\pi_d)
=p(\theta)p_m(\phi)p(D\mid\theta,\pi_d).
\]
This equality is an equality of measures, or of densities almost everywhere with respect to their dominating product measure. Integrating out $\theta$ gives
\[
p_m(\phi,D\mid\pi_d)=p_m(\phi)p(D\mid\pi_d),
\qquad
p(D\mid\pi_d)=\int p(D\mid\theta,\pi_d)p(\theta)\,d\theta.
\]
In particular, $p_m(D\mid\pi_d)=p(D\mid\pi_d)$, and $D$ and $\phi$ are marginally independent.

For $p(D\mid\pi_d)$-almost every $D$, its marginal density is positive and finite. Bayes' rule and the preceding factorization give
\[
\begin{aligned}
p_m(\theta\mid D,\phi,\pi_d)
&=\frac{p(D\mid\theta,\pi_d)p(\theta)}{p(D\mid\pi_d)}\\
&=p(\theta\mid D,\pi_d).
\end{aligned}
\]
The equality holds as equality of posterior probability measures for $p_m(\phi)p(D\mid\pi_d)$-almost every $(\phi,D)$. Indeed, the exceptional conditioning set is null under the joint law of $(\phi,D)$, which has just been identified with that product law. Null datasets do not require any prescribed posterior values.

Integrating the fixed nonnegative measurable predictive density against these equal posterior measures gives, for every $z$,
\[
\begin{aligned}
p_m(z\mid\phi,D,\pi_d)
&=\int p(z\mid\theta)p_m(\theta\mid D,\phi,\pi_d)\,d\theta\\
&=\int p(z\mid\theta)p(\theta\mid D,\pi_d)\,d\theta.
\end{aligned}
\]
The right-hand side is independent of $\phi$. Equality of the posterior measures makes this true for all $z$ outside the same exceptional set of conditioning pairs; no intersection over uncountably many $z$ is needed.

For a fixed model let $N_m$ be that exceptional set of $(\phi,D)$ pairs. Each of the sets $\{(\phi_1,\phi_2,D):(\phi_i,D)\in N_m\}$, for $i=1,2$, has zero measure under $p_m(\phi_1)p_m(\phi_2)p(D\mid\pi_d)$, by integrating out the other sensitive coordinate. Outside their union, both predictions equal the same integral above. Since $p_m(D\mid\pi_d)=p(D\mid\pi_d)$, this is precisely the required demographic parity for $p_m(\phi_1)p_m(\phi_2)p_m(D\mid\pi_d)$-almost every triple, in every model.

## Obligation Closure

1. Zero leakage in every model: derived from nonnegativity and the zero maximum.
2. Conditional independence: obtained from the standard zero-CMI characterization, with its statement and hypotheses verified above.
3. Posterior invariance: derived from the source's primitive model assumptions, integration, and Bayes' rule, including identification of the conditioning product law.
4. Predictive parity: derived by integration against equal posterior measures and an explicit two-set null-measure argument.

No specialized or unresolved external proof dependency remains.
