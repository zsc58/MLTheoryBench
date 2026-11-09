# Reference Proof

## Proof Structure and Obligations

The theorem-critical obligations are:

1. Establish that release conditioning is well-defined, handle the endpoint q=1 without conditioning on an impossible exclusion event, and derive the Bayes mixture identity for 0<q<1.
2. Couple the remaining sampled records in the inclusion and exclusion experiments and apply the threshold sensitivity assumption before averaging.
3. Establish the shifted Gaussian survival-ratio bound over the entire clipped threshold domain, with the stated noise scale.
4. Convert the acceptance-probability comparison into both required bounds on the inflation ratio and conclude uniformly over histories.

The four steps below close these obligations. The Gaussian fact is derived explicitly rather than left as an unaudited dependency.

## Complete Proof

### Step 1: Well-defined conditioning, the endpoint, and Bayes' rule

Fix a record z from the sampled dataset and an arbitrary prior history. All probabilities and expectations below are taken in the round's prescribed conditional experiment at that history; we suppress the history in notation. Poisson sampling means independent Bernoulli inclusion of the records with probability q. The batch evaluation is the pre-selection-noise function for this history.

Write A for release and define
\[
Q_{\sigma_v}(u)=1-\Phi_{\sigma_v}(u),\qquad
R=\frac{Q_{\sigma_v}(C_{\max}-s)}{Q_{\sigma_v}(C_{\max})}.
\]
Since \(\sigma_v>0\), the Gaussian survival function is positive at every finite real argument. Because it is decreasing and \(s>0\), R is finite and \(R\ge1\). Independence of the selection noise gives
\[
\Pr(A)=\mathbb E[Q_{\sigma_v}(X(B))]
\ge Q_{\sigma_v}(C_{\max})>0.
\]
Thus the conditional inclusion probability is well-defined, including when the sampled batch is empty, since the public setup defines the metric on every possible batch.

If q=1, the record is always included, so
\[
q_{\mathrm{cond}}(z)=1,\qquad \rho=1
=\min\{R,1/q\}.
\]
The effective-rate bound also holds with equality at this endpoint. No probability conditional on exclusion is used.

For the remainder suppose \(0<q<1\). Both inclusion and exclusion have positive probability, so define
\[
p_1=\Pr(A\mid z\in B),\qquad
p_0=\Pr(A\mid z\notin B).
\]
The same threshold bound gives \(p_0,p_1\ge Q_{\sigma_v}(C_{\max})>0\). By total probability and Bayes' rule,
\[
\Pr(A)=q p_1+(1-q)p_0,
\qquad
q_{\mathrm{cond}}(z)=\frac{q p_1}{q p_1+(1-q)p_0},
\]
and hence
\[
\rho=\frac{p_1}{q p_1+(1-q)p_0}.
\]

### Step 2: Coupling and the sensitivity comparison

Let S denote the Poisson-sampled subset of all records other than z. Independence of the inclusion indicators means that S has the same distribution conditional on either inclusion or exclusion of z. Thus the two batches can be represented as S and \(S\cup\{z\}\), with the prior history held fixed.

For a realization of S, put
\[
x_0=X(S),\qquad x_1=X(S\cup\{z\}).
\]
The assumptions imply
\[
x_0\in[-C_{\max},C_{\max}],\qquad x_1\ge x_0-s.
\]
Conditional on the batch, the independent Gaussian noise gives the exact acceptance probability \(Q_{\sigma_v}(X(B))\). Consequently,
\[
p_0=\mathbb E[Q_{\sigma_v}(x_0)],
\qquad
p_1=\mathbb E[Q_{\sigma_v}(x_1)]
\le\mathbb E[Q_{\sigma_v}(x_0-s)].
\]
The argument \(x_0-s\) need not itself lie in the clipped interval: it is used only in a valid upper bound for acceptance, and the Gaussian survival function is defined on all of \(\mathbb R\).

### Step 3: Gaussian survival-ratio monotonicity

Define the Gaussian density and hazard by
\[
\phi_{\sigma_v}(x)=\frac{1}{\sqrt{2\pi}\sigma_v}
\exp\!\left(-\frac{x^2}{2\sigma_v^2}\right),
\qquad
h(x)=\frac{\phi_{\sigma_v}(x)}{Q_{\sigma_v}(x)}.
\]
Using \(Q_{\sigma_v}'=-\phi_{\sigma_v}\) and
\(\phi_{\sigma_v}'(x)=-(x/\sigma_v^2)\phi_{\sigma_v}(x)\), differentiation yields
\[
h'(x)=h(x)\left(h(x)-\frac{x}{\sigma_v^2}\right).
\]
For \(x\le0\), the expression in parentheses is positive because \(h(x)>0\). For \(x>0\), integration of the density derivative gives
\[
\phi_{\sigma_v}(x)
=\int_x^\infty\frac{u}{\sigma_v^2}\phi_{\sigma_v}(u)\,du
>\frac{x}{\sigma_v^2}\int_x^\infty\phi_{\sigma_v}(u)\,du
=\frac{x}{\sigma_v^2}Q_{\sigma_v}(x).
\]
Therefore \(h(x)>x/\sigma_v^2\) also for \(x>0\), so h is increasing on all of \(\mathbb R\).

For
\[
r(x)=\frac{Q_{\sigma_v}(x-s)}{Q_{\sigma_v}(x)},
\]
we obtain
\[
\frac{d}{dx}\log r(x)=h(x)-h(x-s)\ge0.
\]
It follows that
\[
\sup_{x\in[-C_{\max},C_{\max}]}r(x)
=r(C_{\max})=R.
\]
In particular, the pointwise inequality
\(Q_{\sigma_v}(x_0-s)\le RQ_{\sigma_v}(x_0)\), together with Step 2, gives
\[
p_1\le\mathbb E[Q_{\sigma_v}(x_0-s)]
\le R\mathbb E[Q_{\sigma_v}(x_0)]
=Rp_0.
\]
This averages a pointwise inequality; it does not identify a mixture acceptance probability with a single Gaussian tail.

### Step 4: Inflation, probability cap, and uniformity

If \(p_1\ge p_0\), then
\[
q p_1+(1-q)p_0\ge p_0,
\qquad
\rho\le\frac{p_1}{p_0}\le R.
\]
If \(p_1<p_0\), then
\[
q p_1+(1-q)p_0\ge p_1,
\qquad
\rho\le1\le R.
\]
Independently, the conditional probability bound \(q_{\mathrm{cond}}(z)\le1\) and q>0 imply \(\rho\le1/q\). Combining the bounds, including the already treated endpoint q=1, proves
\[
\rho(z\mid\mathcal F_{t-1})\le
\min\left\{
\frac{1-\Phi_{\sigma_v}(C_{\max}-s)}{1-\Phi_{\sigma_v}(C_{\max})},
\frac1q
\right\}.
\]
Finally, by definition,
\[
q_{\mathrm{cond}}(z\mid\mathcal F_{t-1})
=q\,\rho(z\mid\mathcal F_{t-1})
\le q\min\left\{
\frac{1-\Phi_{\sigma_v}(C_{\max}-s)}{1-\Phi_{\sigma_v}(C_{\max})},
\frac1q
\right\}.
\]
Every estimate uses the same q, s, \(C_{\max}\), and \(\sigma_v\), independently of the chosen history and record. The proof also covers \(C_{\max}=0\); it never divides by \(C_{\max}\), s, or the public coefficient \(\Delta\). Thus zero or negative \(\Delta\) introduces no additional condition because sensitivity is imposed directly on X.
