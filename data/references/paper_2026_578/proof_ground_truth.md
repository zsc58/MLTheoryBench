# Reference Proof

## Proof Structure

For one timeline score, prove unbiasedness by conditioning each eligible token on its preceding prefix. The terminating draw is included, so eligibility is determined before that draw. Then compare the variance of the SCOPE sample mean with the Bernoulli sample mean algebraically. Finally construct a finite token process whose outcome probability tends to zero while SCOPE has strictly larger variance.

## Standard Background

For an integrable random variable W and a sigma-field G, the tower identity gives E[E[W|G]]=E[W]. A bounded G-measurable factor H can be taken outside conditional expectation: E[HW|G]=H E[W|G]. For a sequence of nonnegative random variables W_t, monotone convergence gives E[Σ_t W_t]=Σ_t E[W_t]. Below the conditional-expectation arguments involve bounded indicators, and all summands in the expectation interchanges are nonnegative. Thus these results apply without assuming an integrable timeline length.

## Complete Proof

Let one timeline be denoted by Z, let \(\mathcal F_t=\sigma(Z_1,\ldots,Z_t)\), and put
\[
Y=\mathbf 1\{\tau_\omega<\tau_E\},\qquad
K=\min(\tau_\omega,\tau_E),\qquad
U=\sum_{t=1}^{K}r_t.
\]
Post-termination padding makes every coordinate well-defined. Conditional probabilities on null prefixes may be assigned arbitrarily without changing any almost-sure statement or expectation.

For each positive integer t, write \(H_t=\mathbf 1\{K\ge t\}\). Since \(\tau_E\) is a stopping time and \(\tau_\omega\) is the first occurrence time,
\[
\{K\ge t\}=\{\tau_E>t-1\}\cap\{\tau_\omega>t-1\}\in\mathcal F_{t-1}.
\]
The stopping convention and \(\tau_E\ne\tau_\omega\) imply
\[
Y=\sum_{t\ge1}H_t\mathbf 1\{Z_t=\omega\}.
\]
Indeed, if the outcome occurs before termination, exactly its first occurrence contributes; if termination precedes the outcome, no term contributes. Inclusion of the terminating draw introduces no outcome indicator because the endpoint and first-outcome indices cannot coincide.

The summands are nonnegative, and \(H_t\) is bounded and \(\mathcal F_{t-1}\)-measurable. Consequently,
\[
\begin{aligned}
\mathbb E[Y]
&=\sum_{t\ge1}\mathbb E[H_t\mathbf 1\{Z_t=\omega\}]\\
&=\sum_{t\ge1}\mathbb E[H_t\mathbb E[\mathbf 1\{Z_t=\omega\}\mid\mathcal F_{t-1}]]\\
&=\sum_{t\ge1}\mathbb E[H_t r_t]
=\mathbb E[U].
\end{aligned}
\]
Thus \(\mathbb E[U]=\mu\), which also establishes integrability. Linearity yields \(\mathbb E[\widehat\mu_{\rm SCOPE}]=\mu\).

For n iid timelines, the pairs \((U_i,Y_i)\) are iid, and \(Y_i\) is Bernoulli with mean \(\mu\). Finite second moments and independence give zero covariance between distinct timeline scores, so
\[
\operatorname{Var}(\widehat\mu_{\rm SCOPE})
=\frac{1}{n^2}\sum_{i=1}^n\operatorname{Var}(U_i)
=\frac{\operatorname{Var}(U_1)}n,
\qquad
\operatorname{Var}(\widehat\mu_{\rm MC})=\frac{\mu(1-\mu)}n.
\]
Using \(\mathbb E[U_1]=\mu\),
\[
\operatorname{Var}(\widehat\mu_{\rm SCOPE})-\operatorname{Var}(\widehat\mu_{\rm MC})
=\frac{\mathbb E[U_1^2]-\mu^2-\mu(1-\mu)}n
=\frac{\mathbb E[U_1(U_1-1)]}{n}.
\]
Since n is positive, strict variance improvement holds exactly when \(\mathbb E[U_1(U_1-1)]<0\). These calculations also cover \(\mu=0\) and \(\mu=1\); no division by either prevalence or its complement occurs.

To disprove any positive prevalence-only guarantee, fix \(q\in(0,1)\) and set \(a=1-q\). Use the vocabulary \(\{A,B,H,T\}\), with outcome token \(\omega=H\). First emit A with probability a and terminate, or emit B with probability q. After B, emit fair independent H/T tokens, terminating immediately after an H or after three further tokens if they are all T. The possible paths and their probabilities are
\[
A\ (a),\quad BH\ (q/2),\quad BTH\ (q/4),\quad BTTH\ (q/8),\quad BTTT\ (q/8).
\]
On A set \(\tau_E=1\); on BTTT set \(\tau_E=4\); on the three outcome paths set \(\tau_E=\tau_H+1\), as required. This is a finite sequential stopping rule, and \(\tau_E\ne\tau_H\) on every path. Pad after completion as in the public setup. Then \(K\) takes the values \(1,2,3,4,4\) on the five listed paths.

The first-position outcome probability is zero. At each subsequent generated H/T position it is 1/2. Therefore the scores are respectively
\[
0,\quad \tfrac12,\quad 1,\quad \tfrac32,\quad \tfrac32,
\]
and
\[
\mu=\frac78q,\qquad
\mathbb E[U^2]
=q\left(\frac18+\frac14+\frac{9}{32}+\frac{9}{32}\right)
=\frac{15}{16}q.
\]
All second moments are finite. For every n,
\[
\operatorname{Var}(\widehat\mu_{\rm SCOPE})-\operatorname{Var}(\widehat\mu_{\rm MC})
=\frac{1}{n}\left(\frac{15}{16}-\frac78\right)q
=\frac{q}{16n}>0.
\]
Given any \(M>0\), choose \(0<q<\min\{1,8M/7\}\). This gives \(0<\mu<M\) while the variance disadvantage is strict, for every n. Hence no positive prevalence threshold guarantees universal strict SCOPE variance improvement.

## Obligation Closure

The proof explicitly establishes eligibility measurability, the outcome-indicator decomposition, unbiasedness, sample-mean variance scaling, the exact comparison, and a source-grounded finite counterexample for every positive threshold. All hypotheses of the standard expectation identities are checked. There are no unresolved proof obligations.
