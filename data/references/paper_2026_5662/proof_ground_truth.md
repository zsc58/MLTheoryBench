# Reference Proof

## Proof Structure

Identify the affine-head gradient with a Kronecker product, convert Frobenius products of the two second-moment matrices into the product kernel, identify that kernel with the mean-embedding inner product, and verify that the factored random features preserve the kernel and satisfy the variance bound.

## Complete Proof

Let \(X=(a,e)\sim P_i\) and \(Y=(a',e')\sim P_j\) be independent.  Write \(g(X)=a\otimes e\) and \(g(Y)=a'\otimes e'\).  (For an affine head this follows directly by differentiating each weight entry: the gradient matrix is \(ea^\top\), whose column-major vectorization is \(a\otimes e\).)

The moment assumptions imply \(\mathbb E\|g(X)\|_2^2=\mathbb E[\|a\|_2^2\|e\|_2^2]<\infty\), by Cauchy--Schwarz, so the matrices \(F_i,F_j\) are well defined.  Expanding their Frobenius inner product using independent draws gives
\[
\begin{aligned}
\langle F_i,F_j\rangle_F
&=\operatorname{tr}\!\left(\mathbb E[gg^\top]\,\mathbb E[g'g'^\top]\right)\\
&=\mathbb E_{X,Y}\operatorname{tr}(gg^\top g'g'^\top)
 =\mathbb E_{X,Y}(g^\top g')^2.
\end{aligned}
\]
The Kronecker-product inner-product identity yields
\[
g^\top g'=(a^\top a')(e^\top e'),
\]
and consequently
\[
\langle F_i,F_j\rangle_F
 =\mathbb E_{X,Y}\bigl[(a^\top a')^2(e^\top e')^2\bigr]
 =\mathbb E_{X,Y}k(X,Y). \tag{1}
\]

For the RKHS feature map \(\varphi\), \(\langle\varphi(X),\varphi(Y)\rangle_{\mathcal H}=k(X,Y)\).  Since \(k(X,X)^{1/2}=\|a\|_2^2\|e\|_2^2\) is integrable, the mean embeddings are defined.  Independence and bilinearity of the inner product imply
\[
\langle\mu_i,\mu_j\rangle_{\mathcal H}
=\left\langle\mathbb E\varphi(X),\mathbb E\varphi(Y)\right\rangle_{\mathcal H}
=\mathbb E_{X,Y}k(X,Y).
\]
Together with (1), this proves \(\langle F_i,F_j\rangle_F=\langle\mu_i,\mu_j\rangle_{\mathcal H}\).  Applying the same argument with \(i=j\) shows \(\|F_t\|_F=\|\mu_t\|_{\mathcal H}\) for \(t=i,j\).  The assumed nonzero embedding norms therefore justify division and prove the stated cosine identity.

It remains to verify the random sketch.  For one coordinate, abbreviate
\[
Z=\psi(a,e)\psi(a',e').
\]
The four Rademacher vectors used in \(Z\) are mutually independent.  For an iid Rademacher vector \(r\),
\[
\mathbb E_r[(r^\top u)(r^\top v)]=u^\top v.
\]
Applying this identity independently to the two activation projections and the two error projections gives
\[
\mathbb E Z
=(a^\top a')^2(e^\top e')^2=k((a,e),(a',e')).
\]
Since \(\langle\widehat\varphi_m(a,e),\widehat\varphi_m(a',e')\rangle=m^{-1}\sum_{s=1}^m Z_s\), linearity of expectation proves its unbiasedness.

For the variance, the \(Z_s\) are iid, hence
\[
\operatorname{Var}\!\left(\langle\widehat\varphi_m(a,e),\widehat\varphi_m(a',e')\rangle\right)
=\frac{\operatorname{Var}(Z_1)}{m}
\leq \frac{\mathbb E Z_1^2}{m}.
\]
For each of the four independent projection vectors, the Rademacher fourth-moment inequality gives
\[
\mathbb E[(r^\top u)^2(r^\top v)^2]\leq 3\|u\|_2^2\|v\|_2^2.
\]
Use it twice with \((u,v)=(a,a')\) and twice with \((u,v)=(e,e')\).  Independence of the four projection vectors then yields
\[
\mathbb E Z_1^2
\leq 3^4\|a\|_2^4\|a'\|_2^4\|e\|_2^4\|e'\|_2^4,
\]
which is the claimed \(81/m\) bound.  Finally, every coordinate requires four factored dot products, two in \(\mathbb R^d\) and two in \(\mathbb R^K\), so its evaluation costs \(O(d+K)\), and all \(m\) coordinates cost \(O(m(d+K))\).  No \(dK\)-dimensional gradient or \(K\times K\) error moment is formed.
