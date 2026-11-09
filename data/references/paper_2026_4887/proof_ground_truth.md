# Reference Proof

## Source Contract and Proof Obligations

Acquisition concerns the marginal parameter posterior under the normal–inverse-gamma hierarchy. It does not condition on a revealed variance. The covariance factor V is not the marginal parameter covariance. Positive-weight queries reveal one response each; zero-weight steps reveal none. Query selection is nonanticipating and uses no parameter-dependent information beyond the observed history.

The obligations are: establish the proper posterior and predictive laws; evaluate marginal information without dropping the response expectation; obtain a candidate-independent additive term and the exact maximizing sets, including zero-weight cases; prove the pathwise determinant bound for every admissible sequence; and check empty, singular-design, and asymptotic cases. All are derived below. No claim from the source's malformed batch-information expression is assumed.

## 1. Posterior and Rank-One Update

Fix a realized history. Let n be the number of positive-weight responses it contains. Write
\[
S=\sum_{s<t}\pi_s z_sz_s^\top,\quad V=(I_d+S)^{-1},\quad
h=\sum_{s<t:\pi_s>0}\pi_s z_s y_s,\quad m=Vh,
\]
\[
T=\sum_{s<t:\pi_s>0}\pi_s y_s^2,\qquad R=T-h^\top Vh.
\]
Completing the square gives
\[
\|\theta\|_2^2+\sum_{s<t:\pi_s>0}\pi_s(y_s-z_s^\top\theta)^2
=(\theta-m)^\top V^{-1}(\theta-m)+R.
\]
Also
\[
R=\|m\|_2^2+\sum_{s<t:\pi_s>0}\pi_s(y_s-z_s^\top m)^2\ge0.
\]
Consequently the posterior has
\[
\theta\mid\sigma^2,\mathcal D\sim\mathcal N(m,\sigma^2V),
\qquad
\sigma^2\mid\mathcal D\sim\operatorname{InvGamma}(\alpha,\beta),
\]
where \(\alpha=a_0+n/2>0\), \(\beta=b_0+R/2>0\), and InvGamma denotes the density convention in the task. Sequential selection introduces no extra parameter-dependent likelihood factor because its randomization is independent and its choices use only observed history.

For a positive-weight candidate with \(w=\pi(z)\), its likelihood adds \(wzz^\top\) to the conditional precision factor:
\[
(V^+)^{-1}=V^{-1}+wzz^\top.
\]
For zero weight, no response is observed and no posterior update occurs. These updates establish the stated recursion without requiring S to be nonsingular.

## 2. Audited Entropy Formula

Put \(\nu=2\alpha>0\) and \(\tau^2=\beta/\alpha>0\). The normal–inverse-gamma integration used in the source extends to any dimension k: a Gaussian vector with conditional covariance \(\sigma^2 B\), mixed using the above variance posterior, has Student-t density with degrees of freedom \(\nu\), location \(\mu\), and scale \(\Sigma=\tau^2B\):
\[
f(x)=\frac{\Gamma((\nu+k)/2)}{\Gamma(\nu/2)(\nu\pi)^{k/2}|\Sigma|^{1/2}}
\left(1+\frac{(x-\mu)^\top\Sigma^{-1}(x-\mu)}{\nu}\right)^{-(\nu+k)/2}.
\]
This follows directly from
\[
\int_0^\infty r^{-c-1}e^{-q/r}\,dr=\Gamma(c)q^{-c}\qquad(c,q>0),
\]
using the substitution \(u=q/r\), exactly as in the source's mixture calculations.

Its entropy is
\[
H_k(\nu,\Sigma)=\tfrac12\log|\Sigma|+h_k(\nu),
\]
\[
h_k(\nu)=\log\Gamma(\nu/2)-\log\Gamma((\nu+k)/2)
+\tfrac{k}{2}\log(\nu\pi)
+\tfrac{\nu+k}{2}\left[\psi((\nu+k)/2)-\psi(\nu/2)\right],
\]
where \(\psi=(\log\Gamma)'\). In particular, the digamma contribution is outside the logarithm of the normalizing constant. The source's displayed entropy formula places it inside that logarithm; this is the repaired parenthesis error indexed by theory_012.

For completeness, after whitening, polar integration and the beta integral give
\[
J_k(c)=\int_{\mathbb R^k}(1+\|u\|_2^2/\nu)^{-c}\,du
=(\nu\pi)^{k/2}\frac{\Gamma(c-k/2)}{\Gamma(c)},\qquad c>k/2.
\]
Differentiating its logarithm at \(c=(\nu+k)/2\) shows that the expectation of \(\log(1+\|u\|_2^2/\nu)\) is
\(\psi((\nu+k)/2)-\psi(\nu/2)\). Substitution in the negative log density proves the entropy formula. Differentiation is justified locally by the integrable polynomial tail times a logarithm. All these entropies are finite for every \(\nu>0\); no second-moment assumption is required.

## 3. Marginal One-Step Information

For \(w>0\), put \(q=z^\top Vz\) and \(r=q+1/w\). Conditional on the history and variance, the joint vector \((\theta,Y)\) is Gaussian with location \((m,z^\top m)\) and covariance \(\sigma^2 M\), where
\[
M=\begin{pmatrix}V&Vz\\z^\top V&r\end{pmatrix}.
\]
Its Schur complement is \(1/w>0\), so M is positive definite and
\[
|M|=|V|/w.
\]
Integrating the variance gives a joint Student-t law with degrees of freedom \(\nu\) and scale \(\tau^2M\). The parameter and response marginal scales are \(\tau^2V\) and \(\tau^2r\), respectively.

The acquisition is mutual information under this joint predictive experiment. Because the relevant entropies are finite, the entropy chain identity gives
\[
A_t(z)=H(\theta\mid\mathcal D)+H(Y\mid\mathcal D,z)
-H(\theta,Y\mid\mathcal D,z).
\]
Thus the response expectation is evaluated, not discarded. Substituting the entropy formula yields
\[
A_t(z)=\tfrac12\log(wr)+h_d(\nu)+h_1(\nu)-h_{d+1}(\nu)
=\tfrac12\log(1+wq)+C_{\nu,d},
\]
where
\[
C_{\nu,d}=h_d(\nu)+h_1(\nu)-h_{d+1}(\nu).
\]
This is finite and independent of the candidate, the posterior location, the variance scale, and the weight. Taking \(c_t=C_{\nu,d}\) proves the required characterization. The constant depends only on d and the current posterior degrees of freedom \(\nu=2a_0+n\).

The constant is strictly positive. To see this without any moment assumption, let \((U,E)\) have a \((d+1)\)-dimensional Student-t law with degrees of freedom \(\nu\) and identity scale. Its mutual information is exactly \(C_{\nu,d}\). Its conditional density satisfies
\[
p_{E\mid U}(0\mid u)=
\frac{\Gamma((\nu+d+1)/2)}{\sqrt\pi\,\Gamma((\nu+d)/2)}
\frac{1}{\sqrt{\nu+\|u\|_2^2}},
\]
which varies with u. The continuous joint density therefore does not factor into its marginals. The elementary relative-entropy inequality, obtained from \(\log x\le x-1\), is strict unless those densities agree almost everywhere. Hence \(C_{\nu,d}>0\).

For positive-weight candidates, strict monotonicity of \(x\mapsto\frac12\log(1+x)\) gives the same maximizing set as \(wz^\top Vz\). Every such candidate has acquisition at least \(C_{\nu,d}>0\). Zero-weight candidates have acquisition zero because they reveal nothing. Therefore, whenever \(\mathcal P_+\ne\varnothing\),
\[
\arg\max_{z\in\mathcal P}A_t(z)
=\arg\max_{z\in\mathcal P_+}\pi(z)z^\top Vz.
\]
If \(\mathcal P_+=\varnothing\), all acquisitions are zero. This also covers a positive-weight zero vector and mixed pools whose quadratic scores all vanish.

The source's zero-offset formula is not rescued by treating sigma^2 as fixed: that would change the acquisition experiment. For example, d=1, n0=4, sigma0^2=1, no data, z=0, and w=1 give \(C_{4,1}=41/6-\log(288\pi)>0\). The source's ordering claim nevertheless survives precisely because this missing term is candidate-independent for positive-weight observations.

## 4. Cumulative Weighted Score

Now fix any admissible sequence, without requiring greedy selection, and set
\[
x_s=\pi_s z_s^\top V_{s-1}z_s.
\]
Since \(I_d+S_{s-1}\succeq I_d\), spectral decomposition gives \(0\prec V_{s-1}\preceq I_d\). Hence
\[
0\le x_s\le\pi_s\|z_s\|_2^2\le1.
\]
The matrix determinant lemma states that, for an invertible matrix B,
\[
|B+uv^\top|=|B|(1+v^\top B^{-1}u).
\]
Apply it with \(B=V_{s-1}^{-1}\) and \(u=v=\sqrt{\pi_s}z_s\). All hypotheses hold because B is positive definite, including when \(\pi_s=0\). Thus
\[
\log\frac{|V_{s-1}|}{|V_s|}=\log(1+x_s).
\]
For \(0\le x\le1\), the derivative of \(\log(1+x)-x/2\) is nonnegative, so \(\log(1+x)\ge x/2\). Telescoping and using \(|V_0|=1\) yield
\[
\sum_{s=1}^t x_s\le2\sum_{s=1}^t\log(1+x_s)
=2\log|V_t^{-1}|.
\]
Finally,
\[
\operatorname{tr}(V_t^{-1})
=d+\sum_{s=1}^t\pi_s\|z_s\|_2^2\le d+t.
\]
All eigenvalues of \(V_t^{-1}\) are positive. Their arithmetic-geometric mean inequality gives
\[
|V_t^{-1}|\le\left(\frac{\operatorname{tr}(V_t^{-1})}{d}\right)^d
\le(1+t/d)^d.
\]
Combining these displays proves
\[
\sum_{s=1}^t\pi_s z_s^\top V_{s-1}z_s
\le2d\log(1+t/d).
\]
The empty case t=0 gives equality. Repetitions, zero vectors, zero weights, and singular S_t cause no difficulty. The proof is pathwise, so it also applies to adaptive sequences. For fixed d the bound is O(d log t) as t tends to infinity. The bounded quantity is the displayed quadratic score; it must not be identified term by term with the marginal entropy gain, which includes the additive constant established above.

## Dependency Accounting

The conjugate distributions are recovered from theory_006 and both parts of theory_009. The standard entropy identity indexed by theory_012 is stated correctly and derived above. The determinant lemma indexed by theory_010 is stated with its hypotheses and applied only to positive definite matrices. The source's direct citation of theory_005 is recorded for audit completeness, but neither its batch formula nor its constants are used. No theorem-critical proof obligation remains open.
