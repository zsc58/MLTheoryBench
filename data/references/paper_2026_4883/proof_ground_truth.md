# Reference Proof

## Proof Structure

Express the cosine with the equal-weight direction through the positive orthogonal coefficients. Interpolate between the policy-gradient coefficients and the gated coefficients by raising each gate to a power. Differentiate the squared cosine, antisymmetrize the derivative into pairwise terms, and use the temperature condition to show that every unequal-probability pair contributes positively.

## Audited Proof Obligations

1. Establish positivity and nonvanishing of the relevant quantities, and obtain the weighted squared-cosine expression from orthogonality.
2. Identify the interpolation endpoints with the two population directions.
3. Prove strict increase of the interpolated coefficient as a function of probability and strict decrease of the gate logarithm.
4. Derive the differentiated and antisymmetrized expression, including its sign.
5. Obtain strict endpoint improvement and pass from squared cosines to cosines.

Each obligation is explicitly discharged below. No external theorem or unproved paper-specific dependency is required.

## Complete Proof

Write
\[
s_n=\sigma\!\left(\frac{-\log p_n}{\eta}\right),\qquad \lambda_n=\log s_n,
\]
so that \(0<s_n<1\) and \(\lambda_n<0\). For \(t\in[0,1]\), define
\[
q_n(t)=p_n s_n^t,
\quad A(t)=\sum_{n=1}^N a_nq_n(t),
\quad B(t)=\sum_{n=1}^N a_nq_n(t)^2,
\quad C=\sum_{n=1}^N a_n.
\]
Every \(q_n(t)\), \(A(t)\), \(B(t)\), and \(C\) is positive. Orthogonality gives
\[
\cos^2\!\left(\sum_nq_n(t)v_n,\sum_nv_n\right)=\Phi(t):=\frac{A(t)^2}{B(t)C}.
\]
Thus \(\Phi(0)\) is the squared cosine for \(d_{\rm PG}\), and \(\Phi(1)\) is that for \(d_{\rm DG}\).

We first establish the required ordering. For \(p\in(0,1)\), put \(s(p)=\sigma((-\log p)/\eta)\). Since \((-\log p)/\eta>0\), \(1-s(p)<1/2\). Hence, for \(t\in[0,1]\),
\[
\frac{d}{dp}\log\big(p\,s(p)^t\big)
=\frac{1-t(1-s(p))/\eta}{p}>0
\]
because \(\eta>1/2\). Therefore \(p\mapsto p s(p)^t\) is strictly increasing. Also
\[
\frac{d}{dp}\log s(p)=-\frac{1-s(p)}{\eta p}<0,
\]
so \(p\mapsto\lambda(p)\) is strictly decreasing. Consequently, whenever \(p_n>p_m\), we have \(q_n(t)>q_m(t)\) and \(\lambda_n<\lambda_m\).

Since \(q_n'(t)=q_n(t)\lambda_n\), let \(D(t)=\sum_n a_nq_n(t)^2\lambda_n\). Then \(A'(t)=\sum_n a_nq_n(t)\lambda_n\), \(B'(t)=2D(t)\), and
\[
\Phi'(t)=\frac{2A(t)}{B(t)^2C}\big(A'(t)B(t)-A(t)D(t)\big).
\]
Antisymmetrizing the double sum gives
\[
A'B-AD
=\frac12\sum_{n,m}a_na_mq_nq_m\,(q_m-q_n)(\lambda_n-\lambda_m).
\]
All factors outside the last two parentheses are positive. By the ordering just proved, each summand is nonnegative, and it is strictly positive whenever \(p_n\ne p_m\). Because the probabilities are not all equal, at least one such pair exists; hence \(\Phi'(t)>0\) for every \(t\in[0,1]\). Therefore \(\Phi(1)>\Phi(0)\).

All coefficients and norms are positive, so both cosines are positive. Taking square roots yields
\[
\cos(d_{\rm DG},d_{\rm CE})>\cos(d_{\rm PG},d_{\rm CE}),
\]
which is the claimed strict directional improvement.

## Private Source-Contract and Repair Notes

The source's multi-context setting uses correctness-indicator rewards and baseline \(b=0\), so only correct actions contribute to the unnormalized sampled gradient. Its population directions are the three sums explicitly defined in the public task. The expectation is taken before evaluating the cosine; neither an expectation of a cosine nor an expectation of a normalized random update is asserted. The normalized-step motivation adds no hypothesis to this deterministic comparison. The single-context assumption \(b\in(0,1)\) is not inherited by the distinct multi-context setting.

The source explicitly defines \(a_n=\|v_n\|^2\) at L000262. That convention is used in the orthogonality identities at L000274 and L000288 and in this proof. The later shorthand references to norms do not introduce a different weighting convention.

A local source proof error occurs in the footnote at L000295. For
\[
f_t(p)=p(1+p^{1/\eta})^{-t},
\]
the derivative is
\[
f_t'(p)=(1+p^{1/\eta})^{-t-1}\big[1+(1-t/\eta)p^{1/\eta}\big].
\]
The source identifies \(2-1/\eta\) as the worst-case bracketed value. That is not a valid lower bound when \(\eta>1\): for \(\eta=2\), \(t=1\), and \(p=1/4\), the bracket is \(5/4<3/2\). The corrected uniform bound is
\[
1+(1-t/\eta)p^{1/\eta}\geq\min\{1,2-1/\eta\}>0.
\]
Indeed, if \(1-t/\eta\geq0\), the bracket is at least \(1\). If \(1-t/\eta<0\), then \(0<p^{1/\eta}<1\) gives a bracket strictly greater than \(2-t/\eta\geq2-1/\eta>0\). This is a local arithmetic repair with no change to the theorem or its proof architecture. The logarithmic-derivative argument in the complete proof already establishes the required monotonicity without using the erroneous bound.

The attached two-vector lemma has domain \(r>0\), as explicitly stated at L000271. Its weighted cosine formula and derivative are valid with the squared-norm convention. The general-N proof above does not invoke that lemma; its orthogonality calculation and pairwise argument are derived directly. No unresolved private proof obligation remains.
