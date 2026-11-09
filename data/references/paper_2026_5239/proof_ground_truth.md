# Reference Proof

## Proof Obligations

1. Derive the centered estimator-error decomposition, preserving every factor of the sample size and contraction parameter.
2. Establish the phase and Gaussian second moments and compute the complete linear-block second moment, including its nonzero Gaussian cross term.
3. Prove that the linear and quadratic blocks have zero cross moment.
4. Derive the Gaussian fourth moment and use it to compute the complete centered quadratic-block second moment.
5. Combine the moments and substitute the empirical-statistic definitions to obtain the exact target identity.

All five obligations are discharged below. No paper-specific result is assumed without its derivation.

## Complete Proof

All expectations concern the internal randomness, with the data, parameters, coefficient vector and modulation direction fixed. The phases are bounded after applying cosine, and Gaussian variables have finite polynomial moments, so the finite sums and expectations below are well defined.

### 1. Centered decomposition

Put \(a=1-\alpha\), let \(E\in\mathbb R^{n\times p}\) have rows \(\varepsilon_i^\top\), put \(q=E\beta\), and write
\[
c_i=\cos(\omega\langle x_i,u\rangle+\theta_i),\qquad c=(c_1,\ldots,c_n)^\top.
\]
Thus \(q_i=\varepsilon_i^\top\beta\). Since \(u^\top\beta=0\),
\[
z_i^\top\beta=a x_i^\top\beta+q_i.
\]
Expanding \(z_i(z_i^\top\beta)\), averaging and applying the correction in \(\widehat S\) gives
\[
\widehat S\beta
=\Sigma_x\beta
+\frac{X^\top q+\lambda(c^\top X\beta)u+E^\top X\beta}{na}
+\frac{\lambda(c^\top q)u+E^\top q-n\tau^2\beta}{na^2}.
\]
Here the modulation correction satisfies \(uu^\top\beta=0\). Similarly,
\[
\widehat b=\frac{X^\top y}{n}
+\frac{\lambda(c^\top y)u+E^\top y}{na}.
\]
Since \(\nabla L(\beta)=X^\top r/n\), subtraction yields
\[
H-\nabla L(\beta)=\frac{T_1+T_2}{na}+\frac{T_3}{na^2},
\]
where
\[
\begin{aligned}
T_1&=\lambda(c^\top r)u+E^\top r,\\
T_2&=X^\top q,\\
T_3&=\lambda(c^\top q)u+E^\top q-n\tau^2\beta.
\end{aligned}
\]

### 2. Scalar moments and the linear block

For any fixed real shift \(t\), integrating over a full period gives
\[
\frac1{2\pi}\int_0^{2\pi}\cos(t+s)\,ds=0,
\qquad
\frac1{2\pi}\int_0^{2\pi}\cos^2(t+s)\,ds=\frac12.
\]
Independence of the phases therefore gives
\[
\mathbb E[c_i]=0,\qquad
\mathbb E[c_ic_j]=\tfrac12\mathbf 1_{\{i=j\}}.
\]
The Gaussian rows are independent, centered and have covariance \(\tau^2I_p\). Consequently,
\[
\mathbb E[q_i]=0,\qquad
\mathbb E[q_iq_j]=\tau^2\|\beta\|^2\mathbf 1_{\{i=j\}},
\qquad
\mathbb E[\varepsilon_iq_i]=\mathbb E[\varepsilon_i\varepsilon_i^\top]\beta=\tau^2\beta.
\]
In particular, for every fixed \(b\in\mathbb R^p\),
\[
\mathbb E[q_i\varepsilon_i^\top b]=\tau^2\beta^\top b.
\]
The phase vector is independent of all Gaussian rows. These identities show that \(T_1,T_2,T_3\) are centered: the only nonzero uncentered mean in \(T_3\) is
\[
\mathbb E[E^\top q]=\sum_i\mathbb E[\varepsilon_iq_i]=n\tau^2\beta,
\]
which is canceled by its deterministic correction.

The phase contribution to the linear-block second moment is
\[
\lambda^2\mathbb E(c^\top r)^2=\frac{\lambda^2}{2}\|r\|^2.
\]
The Gaussian row independence and covariance give
\[
\mathbb E\|E^\top r\|^2=p\tau^2\|r\|^2,
\qquad
\mathbb E\|X^\top q\|^2=\tau^2\|\beta\|^2\|X\|_F^2.
\]
The Gaussian cross term does not vanish. Indeed,
\[
\begin{aligned}
\mathbb E[(E^\top r)^\top X^\top q]
&=\sum_{i,j}r_i\mathbb E[q_j\varepsilon_i^\top x_j]\\
&=\tau^2\sum_i r_i\beta^\top x_i
=\tau^2\beta^\top X^\top r.
\end{aligned}
\]
For \(i\ne j\), the terms vanish because \(\varepsilon_i\) and \(q_j\) are independent and centered. Both cross terms between \(\lambda(c^\top r)u\) and the Gaussian linear terms vanish by conditioning on \(E\) and using \(\mathbb E[c]=0\). Thus
\[
\begin{aligned}
\mathbb E\|T_1+T_2\|^2
&=\frac{\lambda^2}{2}\|r\|^2+p\tau^2\|r\|^2
+2\tau^2\beta^\top X^\top r
+\tau^2\|\beta\|^2\|X\|_F^2\\
&=\|r\|^2\left(\frac{\lambda^2}{2}+p\tau^2\right)
+2n\tau^2\beta^\top\Sigma_{rx}
+n\tau^2\|\beta\|^2\operatorname{tr}(\Sigma_x).
\end{aligned}
\]

### 3. Cross-block moment

Write
\[
A=\lambda(c^\top r)u,\qquad B=E^\top r+X^\top q,
\qquad s=c^\top q,\qquad h=E^\top q-n\tau^2\beta.
\]
Then \(T_1+T_2=A+B\) and \(T_3=\lambda s u+h\). For the product of the two phase-containing terms,
\[
\mathbb E[A^\top(\lambda s u)]
=\lambda^2\sum_{i,j}r_i\mathbb E[c_ic_j]\mathbb E[q_j]=0.
\]
The other terms containing a phase factor satisfy
\[
\mathbb E[A^\top h]=0,\qquad
\mathbb E[B^\top(\lambda s u)]=0,
\]
because, conditional on \(E\), all Gaussian quantities are fixed and every remaining phase factor has mean zero.

Finally, the joint Gaussian matrix has the same distribution as \(-E\). Under this transformation \(q\) and \(B\) change sign, while \(h\) does not. Therefore the integrable scalar \(B^\top h\) changes sign without changing its distribution, and its expectation is zero. Combining the four products proves
\[
\mathbb E[(T_1+T_2)^\top T_3]=0.
\]

### 4. Gaussian fourth moment and the quadratic block

We first derive the required fourth moment. A scalar \(Z\sim\mathcal N(0,\tau^2)\) has density
\[
f(t)=\frac{1}{\sqrt{2\pi}\tau}\exp\!\left(-\frac{t^2}{2\tau^2}\right),
\qquad f'(t)=-\frac{t}{\tau^2}f(t).
\]
Integration by parts, with the boundary term vanishing by Gaussian decay, gives
\[
\mathbb E[Z^4]
=-\tau^2\int_{\mathbb R}t^3 f'(t)\,dt
=3\tau^2\int_{\mathbb R}t^2 f(t)\,dt
=3\tau^4.
\]
Odd moments vanish by symmetry. The density of \(\varepsilon_i\sim\mathcal N(0,\tau^2I_p)\) factors across its coordinates. Writing \(\varepsilon_{ib}\) for coordinate \(b\), coordinate independence and these scalar moments imply
\[
\mathbb E[\varepsilon_{ib}\varepsilon_{ic}\varepsilon_{ik}^2]
=\tau^4(\delta_{bc}+2\delta_{bk}\delta_{ck}).
\]
Indeed, the expectation is zero when \(b\ne c\), is \(\tau^4\) when \(b=c\ne k\), and is \(3\tau^4\) when \(b=c=k\). Therefore
\[
\begin{aligned}
\mathbb E[q_i^2\|\varepsilon_i\|^2]
&=\sum_{b,c,k}\beta_b\beta_c
  \mathbb E[\varepsilon_{ib}\varepsilon_{ic}\varepsilon_{ik}^2]\\
&=\tau^4(p+2)\|\beta\|^2.
\end{aligned}
\]

Let \(w=E^\top q=\sum_i\varepsilon_iq_i\). Phase independence and the second moments established above give
\[
\mathbb E[s]=0,
\qquad
\mathbb E[s^2]
=\sum_{i,j}\mathbb E[c_ic_j]\mathbb E[q_iq_j]
=\frac{n\tau^2\|\beta\|^2}{2}.
\]
Since \(w\) is a function of \(E\), conditioning on \(E\) also gives
\[
\mathbb E[s(u^\top w)]=0.
\]
We already have \(\mathbb Ew=n\tau^2\beta\). For distinct rows,
\[
\mathbb E[(\varepsilon_iq_i)^\top(\varepsilon_jq_j)]
=(\mathbb E[\varepsilon_iq_i])^\top\mathbb E[\varepsilon_jq_j]
=\tau^4\|\beta\|^2\qquad(i\ne j).
\]
There are \(n\) diagonal terms and \(n(n-1)\) ordered off-diagonal terms. Hence
\[
\begin{aligned}
\mathbb E\|w\|^2
&=n\tau^4(p+2)\|\beta\|^2+n(n-1)\tau^4\|\beta\|^2,\\
\mathbb E\|w-n\tau^2\beta\|^2
&=\mathbb E\|w\|^2-\|\mathbb Ew\|^2
=n\tau^4(p+1)\|\beta\|^2.
\end{aligned}
\]
Because \(T_3=\lambda s u+(w-n\tau^2\beta)\), \(\|u\|=1\), \(\mathbb E[s]=0\), and \(\mathbb E[s(u^\top w)]=0\), its mixed term has zero expectation. Consequently,
\[
\mathbb E\|T_3\|^2
=n\|\beta\|^2\left(\frac{\lambda^2\tau^2}{2}+(p+1)\tau^4\right).
\]

### 5. Combination and boundary checks

Taking the squared norm of the decomposition and using the zero cross moment gives
\[
\mathbb E\|H-\nabla L(\beta)\|^2
=\frac{\mathbb E\|T_1+T_2\|^2}{n^2a^2}
+\frac{\mathbb E\|T_3\|^2}{n^2a^4}.
\]
Substituting the two block moments, \(\|r\|^2=nR^2\), and \(a=1-\alpha\) yields
\[
\mathbb E\|H-\nabla L(\beta)\|^2
=
\frac{R^2(\lambda^2/2+p\tau^2)+2\tau^2\beta^\top\Sigma_{rx}+\tau^2\|\beta\|^2\operatorname{tr}(\Sigma_x)}{n(1-\alpha)^2}
+\frac{\|\beta\|^2[\lambda^2\tau^2/2+(p+1)\tau^4]}{n(1-\alpha)^4}.
\]

No step divides by \(\|\beta\|\), \(\|r\|\), or a data-covariance eigenvalue. Thus zero coefficients, zero residuals, zero data and rank-deficient designs are included. When \(n=1\), the off-diagonal sum is empty and its stated count is zero. When \(p=1\), the assumed unit-vector orthogonality forces \(\beta=0\), which the proof includes; the task makes no assertion that such a direction exists for an inadmissible coefficient vector. The source parameter domain ensures all estimator denominators are nonzero.
