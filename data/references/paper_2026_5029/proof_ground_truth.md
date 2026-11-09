# Reference Proof

## Proof Structure and Obligations

1. Establish that completeness, continuity, and the support condition make every truthful class marginal positive. Show that the truthful risk is finite, every candidate risk in the declared domain is a well-defined extended real number, and the excess-risk expansion involves no indeterminate subtraction.
2. Establish the expectation-form log-sum inequality with a correct finite-equality characterization. Handle zero means and positive numerator mass on a zero-denominator set before introducing the auxiliary measure. State and verify the precise Jensen result used.
3. Apply the inequality coordinatewise. Nonnegative gaps imply risk minimization; equality of risks forces finite equality in every coordinate. Continuity on the support upgrades the resulting almost-sure identities to pointwise identities.
4. Use completeness and simplex normalization to force every proportionality constant to equal one, and verify the converse.

The normalization is the exact population expectation, not an empirical or mini-batch average. The conditional-feature-density assumption is retained from the source's standing setup; the argument below uses the explicitly assumed posterior continuity and does not require a further density calculation.

## Complete Proof

Write \(q_k(x)=q(k|x)\), \(p_k(x)=p(k|x)\), and
\[
\pi_k=\mathbb E q_k(Z),\qquad s_k=\mathbb E p_k(Z),
\]
where expectations without a subscript are under \(P_X\).

### 1. Normalization, finiteness, and the excess-risk identity

Completeness implies that no \(q_k\) is identically zero: otherwise the coefficient vector supported on coordinate \(k\) would violate completeness. Thus there is an \(x\in X\) with \(q_k(x)>0\). Continuity gives a relatively open neighborhood on which \(q_k\) is bounded below by a positive number, and the support assumption gives that neighborhood positive probability. Hence \(\pi_k>0\) for every \(k\). In particular, the truthful kernel belongs to the declared score domain.

Use \(0\log 0=0\), and interpret a term with zero label weight as zero. Since \(-t\log t\) is bounded on \([0,1]\),
\[
R(q;q)=-\sum_{k=1}^K\mathbb E[q_k\log q_k]
       +\sum_{k=1}^K\pi_k\log\pi_k
\]
is finite.

For an admissible candidate, every \(s_k>0\). Because \(p_k\le1\), the score satisfies \(S(p,x,k)\ge\log s_k\). Equivalently,
\[
R(p;q)=\sum_{k=1}^K\mathbb E[-q_k\log p_k]
       +\sum_{k=1}^K\pi_k\log s_k,
\]
where the first sum has nonnegative terms and the second sum is finite. Thus \(R(p;q)\in\mathbb R\cup\{+\infty\}\), and the risk is not an undefined difference of infinities.

Subtracting the finite truthful risk yields
\[
R(p;q)-R(q;q)
=\sum_{k=1}^K\left\{
\mathbb E\!\left[q_k\log\frac{q_k}{p_k}\right]
-\pi_k\log\frac{\pi_k}{s_k}
\right\}.\tag{1}
\]
Here \(q_k\log(q_k/p_k)=0\) when \(q_k=0\), including when \(p_k=0\), and it is \(+\infty\) when \(q_k>0=p_k\). Each expectation is bounded below because
\[
q_k\log(q_k/p_k)=q_k\log q_k-q_k\log p_k,
\]
with a bounded first term and a nonnegative second term. Every subtracted marginal term in (1) is finite. Consequently (1) is valid also when the candidate risk is infinite.

### 2. Log-sum inequality and its exact equality cases

Let \(g,h\) be bounded measurable nonnegative functions. Put \(a=\mathbb E g\), \(b=\mathbb E h\), and interpret \(g\log(g/h)\) as zero on \(\{g=0\}\) and as \(+\infty\) on \(\{g>0,h=0\}\). The analogous conventions apply to \(a\log(a/b)\). Then
\[
\mathbb E\!\left[g\log\frac gh\right]\ge a\log\frac ab.\tag{2}
\]
Finite equality in (2) holds if and only if \(g=c h\) almost surely for some finite \(c\ge0\). There is one additional extended-real equality case: if \(b=0<a\), both sides are \(+\infty\), without a proportionality conclusion.

First, the expectation on the left is well defined. On \(\{h>0\}\), set \(t=g/h\). The elementary bound \(t\log t\ge-1/e\) gives \(g\log(g/h)\ge-h/e\), so its negative part is integrable.

If \(a=0\), then \(g=0\) almost surely and both sides are zero; proportionality holds with \(c=0\). If \(b=0<a\), then \(h=0\) almost surely and both sides are \(+\infty\). This proves the inequality in the degenerate cases and separates infinite equality from finite equality.

Now assume \(a,b>0\). If
\[
P_X\{h=0,g>0\}>0,
\]
the left side is \(+\infty\), whereas the right side is finite, so the inequality is strict. Otherwise \(g=0\) almost surely on \(\{h=0\}\). Define
\[
\frac{dQ}{dP_X}=\frac hb,
\qquad
T=\begin{cases}g/h,&h>0,\\0,&h=0.\end{cases}
\]
Then \(Q\) is a probability measure and
\[
\mathbb E_QT=\frac ab<\infty,
\qquad
\mathbb E_Q[T\log T]=\frac1b\mathbb E\!\left[g\log\frac gh\right].
\]
The support-zero reduction is necessary for both identities.

The standard Jensen result used here is the following precise statement: for a probability measure \(Q\), a measurable \(T\ge0\) with finite mean, and \(\phi(t)=t\log t\), \(\phi(0)=0\), one has
\[
\mathbb E_Q\phi(T)\ge\phi(\mathbb E_QT),
\]
allowing an infinite left side; equality holds exactly when \(T\) is constant almost surely. Its application requires no integrability of the positive part of \(\phi(T)\), because \(\phi\) is bounded below. For completeness, when the mean is \(m>0\), the elementary supporting-tangent inequality
\[
\phi(t)\ge\phi(m)+(1+\log m)(t-m),\qquad t\ge0,
\]
is strict unless \(t=m\). Integrating proves the inequality, and the nonnegative tangent gap has zero integral exactly when \(T=m\) almost surely. When the mean is zero, nonnegativity gives \(T=0\) almost surely. This also proves the stated equality characterization, including the endpoint zero.

Applying this result with \(m=a/b\) and multiplying by \(b\) proves (2). In the present positive-mean case, finite equality is equivalent to \(T=a/b\), \(Q\)-almost surely. Since \(h/b>0\) on \(\{h>0\}\), this gives \(g=(a/b)h\), \(P_X\)-almost surely on that set. The earlier reduction gives the same identity on \(\{h=0\}\). Conversely, \(g=c h\) almost surely with finite \(c\ge0\) gives finite equality directly.

If \(g,h\) are continuous on \(X=\operatorname{supp}(P_X)\), an almost-sure identity \(g=c h\) holds everywhere on \(X\). Indeed, a nonzero value of the continuous difference would persist on a relatively open neighborhood of a support point, which has positive probability, contradicting the almost-sure identity.

### 3. Risk minimization and pointwise proportionality

Apply (2) with \(g=q_k\) and \(h=p_k\). These functions are bounded and nonnegative, and their means satisfy \(\pi_k,s_k>0\). Thus every coordinate gap in (1) is nonnegative, proving
\[
R(p;q)\ge R(q;q).
\]

If the risks are equal, their common value is finite by the finiteness of \(R(q;q)\). Hence the finite sum of nonnegative coordinate gaps in (1) equals zero, and every coordinate gap is zero. The finite-equality characterization and continuity on the support give constants \(c_k\ge0\) such that
\[
q_k(x)=c_k p_k(x)\qquad\text{for every }x\in X.\tag{3}
\]
No conclusion is being drawn from an equality of two infinite quantities.

### 4. Completeness and uniqueness

Each \(c_k\) is positive. If \(c_k=0\), (3) makes \(q_k\) identically zero, contradicting completeness. Therefore \(p_k=q_k/c_k\). Since both kernels are simplex-valued,
\[
0=\sum_{k=1}^K(p_k(x)-q_k(x))
 =\sum_{k=1}^K\left(\frac1{c_k}-1\right)q_k(x)
 \qquad\text{for every }x\in X.
\]
Completeness forces every coefficient \(1/c_k-1\) to vanish, so \(c_k=1\) and \(p_k=q_k\) everywhere. Conversely, \(p=q\) plainly gives equal risks. This proves the claimed strict properness. The argument also covers \(K=1\); no multi-class-only assumption or positive pointwise probability assumption is needed.

## Source Repair and Closure

The auxiliary lemma's source statement at L000428 is repaired only by distinguishing finite equality from the degenerate equality \(+\infty=+\infty\) explicitly identified at L000431. The theorem uses the lemma with strictly positive means, where its original proportionality mechanism remains valid. The score-domain clarification prevents undefined \(0/0\) normalizations rather than assigning them an invented extended value. All four proof obligations listed above are explicitly closed; there is no unresolved private ground-truth dependency.
