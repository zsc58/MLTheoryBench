# Reference Proof

## Proof Structure

Use the balance identity to normalize two classifier-weighted densities. Apply nonnegativity of KL divergence and Jensen's inequality to obtain the two complementary expected-ratio bounds, explicitly checking integrability in the finite-expectation cases. Finally substitute the Bayes density-ratio classifier into the balance identity to show that the exact classifier is feasible, including when it takes boundary values.

## Standard Facts and Analytic Justification

The standard-independent facts used are:

- For probability densities a and c, with c positive almost everywhere under the distribution with density a, the KL divergence D_KL(a||c)=integral a log(a/c) is nonnegative whenever this integral is finite. More generally it is a well-defined nonnegative extended quantity.
- If Z is an integrable real random variable and exp(Z) is integrable, Jensen's inequality gives exp(E[Z]) <= E[exp(Z)].

Here is the routine integrability check used below. For probability densities a and c with c>0 almost everywhere under the distribution with density a, put R=a/c on that distribution's support. R is positive and finite almost surely. If E_a[R]=+infinity, the desired bound E_a[R]>=1 is immediate. If E_a[R]<infinity, then log^+(R)<=R, so the positive part of log R is integrable. On the set c>a>0, writing t=c/a>1 gives
\[
 a\log(c/a)=c\frac{\log t}{t}\le \frac{c}{e},
\]
since the maximum of (log t)/t for t>=1 is 1/e. Consequently
\[
 \mathbb E_a[(\log R)^-]
 =\int_{c>a>0}a\log(c/a)\le \frac1e\int c=\frac1e.
\]
Thus log R is integrable in the finite-ratio-expectation case, and both standard facts apply with all hypotheses verified. No extra moment or finiteness assumption is imposed on the classifier.

## Complete Proof

Let mu be the common dominating measure. Choose finite-valued density versions p and q, and let h be a balanced measurable [0,1]-valued classifier satisfying 0<h<1 wherever p+q>0. Balance gives
\[
 \int ph\,d\mu=\int q(1-h)\,d\mu,
\]
so
\[
 \int(p+q)h\,d\mu=1.
\]
Define
\[
 f=(p+q)h.
\]
This is a nonnegative measurable probability density. Let F be its probability distribution. Under P, p>0 almost surely, and hence f>0 almost surely. On this set,
\[
 \frac{p}{f}=\frac{b}{h}.
\]
If E_P[b/h]=+infinity, the first inequality holds immediately. Otherwise the analytic justification above, with a=p and c=f, proves that log(b/h) is integrable. Nonnegativity of KL divergence therefore gives
\[
 0\le D_{\mathrm{KL}}(P\|F)
 =\int p\log\frac{p}{f}\,d\mu
 =\mathbb E_P\left[\log\frac{b}{h}\right].
\]
Jensen's inequality for the exponential function now gives
\[
 \mathbb E_P\left[\frac{b}{h}\right]
 =\mathbb E_P\left[\exp\left(\log\frac{b}{h}\right)\right]
 \ge \exp\left(\mathbb E_P\left[\log\frac{b}{h}\right]\right)
 \ge 1.
\]

Since integral(p+q) dmu=2 and integral(p+q)h dmu=1, the complementary weighting
\[
 g=(p+q)(1-h)
\]
is also a nonnegative measurable probability density. Let G be its probability distribution. Under Q, q>0 almost surely, so g>0 almost surely. Moreover,
\[
 \frac{q}{g}=\frac{1-b}{1-h}
\]
Q-almost surely. If E_Q[(1-b)/(1-h)]=+infinity, the second inequality is immediate. Otherwise the analytic justification above, with a=q and c=g, proves log integrability. Nonnegativity of KL divergence gives
\[
 0\le D_{\mathrm{KL}}(Q\|G)
 =\int q\log\frac{q}{g}\,d\mu
 =\mathbb E_Q\left[\log\frac{1-b}{1-h}\right].
\]
Applying Jensen with the verified integrability yields
\[
 \mathbb E_Q\left[\frac{1-b}{1-h}\right]
 \ge \exp\left(\mathbb E_Q\left[\log\frac{1-b}{1-h}\right]\right)
 \ge 1.
\]

For the Bayes classifier itself, b=p/(p+q) where p+q>0, with any measurable [0,1]-valued extension elsewhere. The identity (p+q)b=p holds also where p+q=0, because both sides are zero. Thus
\[
 \mathbb E_P[b]+\mathbb E_Q[b]
 =\int(p+q)b\,d\mu
 =\int p\,d\mu=1.
\]
Equivalently, E_P[b]=E_Q[1-b], so b is balanced under the full [0,1]-valued definition. No strict-interiority assumption on b is needed for this step. Therefore restricting the [0,1]-valued classifier class to balanced classifiers retains the exact Bayes density-ratio solution, while every balanced classifier satisfying the ratio-domain condition obeys both complementary expected-ratio inequalities.

## Obligation Closure

Both weighted-density normalizations, both positivity conditions, both finite/infinite expectation cases, the log-integrability checks, the hypotheses of KL nonnegativity and Jensen, Bayes feasibility at boundary values, and the exact-solution retention conclusion have been explicitly verified. There are no unresolved reference-proof obligations.
