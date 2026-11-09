# Problem

## Setup

Let \((X_i,Y_i)\), \(i=1,\ldots,n\), be independent and identically distributed with law \(P_0\), and let \(\widetilde X_j\), \(j=1,\ldots,N\), be independent and identically distributed with the marginal law \(P_{0,X}\), independently of the labeled sample. Write \(D_L=\{(X_i,Y_i):1\le i\le n\}\). As \(n\to\infty\), put \(M=n+N\) and assume \(\rho_n=n/M\to\rho_0\in(0,1)\). Assume \(E[Y^2]<\infty\), and define \(\psi_0=E[Y]\) and \(\mu_0(x)=E[Y\mid X=x]\).

For functions \(a\) of \((X,Y)\) and \(b\) of \(X\), define
\[
 P_n^L a=\frac1n\sum_{i=1}^n a(X_i,Y_i),\qquad
 P_N^U b=\frac1N\sum_{j=1}^N b(\widetilde X_j).
\]
A function of \(X\) alone may also be integrated against \(P_n^L\). Write \(P_0a=E[a(X,Y)]\), \(P_{0,X}b=E[b(X)]\), and \(\|b\|_2^2=P_{0,X}(b^2)\).

Let \(m:\mathcal X\to\mathbb R\) be a fixed measurable score with \(E[m(X)^2]<\infty\). Its values are available for every observed covariate. Set \(T=m(X)\), and let \(Q\) be the law of \(T\). Choose a bounded version \(\eta(t)=E[Y\mid T=t]\) having finite total variation on the support of \(Q\), and fix a bounded finite-total-variation extension to \(\mathbb R\). Total variation means the supremum of \(\sum_{k=1}^{r-1}|\eta(t_{k+1})-\eta(t_k)|\) over finite increasing sequences in the domain. Assume that, for some fixed finite \(K>0\),
\[
 E\!\left[\exp\{|Y-\eta(T)|/K\}\mid T\right]\le 2
 \quad\text{almost surely}.
\]
This expresses uniformly sub-exponential conditional tails; uniformly sub-Gaussian conditional tails are included.

Let \(f_n\) be any jointly measurable choice of an isotonic least-squares minimizer,
\[
 f_n\in\mathop{\rm argmin}_{f:\mathbb R\to\mathbb R\ {m measurable,
ondecreasing}}
       \frac1n\sum_{i=1}^n\{Y_i-f(m(X_i))\}^2.
\]
The entire fitted map, including its values away from the observed scores, is chosen using only the labeled score–response pairs. Put \(m_n^*=f_n\circ m\), take square-integrable fitted versions, and assume
\[
 \sup_{x\in\mathcal X}|m_n^*(x)|=O_p(1).
\]
Let \(f_0\) be the \(L^2(Q)\) projection of \(\eta\) onto the cone of square-integrable nondecreasing functions, and put \(m_0=f_0\circ m\). Population projections are understood up to almost-sure equality.

For a square-integrable score \(g\), define
\[
 \widehat\psi(g)=\rho_nP_n^Lg+(1-\rho_n)P_N^Ug+P_n^L(Y-g).
\]
For a labeled-data-dependent score, the same formula denotes evaluation of that fitted function on the indicated observations. Define the calibrated estimator directly by
\[
 \widehat\psi_{\rm iso}=\rho_nP_n^Lm_n^*+(1-\rho_n)P_N^Um_n^*.
\]

Define the population oracle \(\widehat m_0\) using a fresh draw \((X,Y)\sim P_0\) independent of \(D_L\), holding \(D_L\) fixed:
\[
 \widehat m_0(x)=E[Y\mid D_L,\ f_n(m(X))=f_n(m(x))].
\]
Use the following version convention, so that this random population function also has specified values at the training observations. For each nonempty level set \(B_s=\{t:f_n(t)=s\}\), use the conditional average of \(\eta(T)\) over \(B_s\) when \(Q(B_s)>0\). When \(Q(B_s)=0\), use \(\eta(t_s)\) for a measurably selected representative \(t_s\in B_s\); for a singleton, its unique point is used. Representatives use no unlabeled observations. Population norms of random fitted functions integrate a fresh covariate with the training sample held fixed.

An influence pair \((D^L,D^U)\) means a pair of square-integrable, mean-zero functions such that
\[
 \widehat\psi-\psi_0=
 \frac1M\sum_{i=1}^nD^L(X_i,Y_i)
 +\frac1M\sum_{j=1}^ND^U(\widetilde X_j)
 +o_p(M^{-1/2}).
\]
Its asymptotic variance under \(\sqrt M\) scaling is \(\rho_0\operatorname{Var}(D^L)+(1-\rho_0)\operatorname{Var}(D^U)\). Efficiency bounds refer to regular estimation of \(E[Y]\) in the unrestricted two-sample model: the full experiment observes the samples specified above, and the reduced experiment observes only \((m(X_i),Y_i)\) and \(m(\widetilde X_j)\).

## Task

Prove the following integrated theorem:
\[
 \|m_n^*-m_0\|_2^2=O_p(n^{-2/3}),
\]
and
\[
\begin{aligned}
\widehat\psi_{\rm iso}-\psi_0={}&
 \rho_n(P_n^L-P_0)\{m_0-\psi_0+\rho_n^{-1}(Y-m_0)\}\\
&+(1-\rho_n)(P_N^U-P_{0,X})\{m_0-\psi_0\}\\
&+O_p(n^{-2/3})+O_p(n^{-1/3}N^{-1/2}).
\end{aligned}
\]
Consequently, it is asymptotically linear with influence pair
\[
 D^L(X,Y)=m_0(X)-\psi_0+\rho_0^{-1}\{Y-m_0(X)\},\qquad
 D^U(X)=m_0(X)-\psi_0.
\]
Its asymptotic variance is no larger than that of \(\widehat\psi(g)\) for every fixed square-integrable score \(g=\theta\circ m\) with \(\theta\) nondecreasing. If \(m_0=\mu_0\) almost surely, it attains the full-experiment efficiency bound. If the score regression has a nondecreasing version on the support of \(Q\), then \(m_0=\eta\circ m\) almost surely and the estimator attains the reduced-experiment efficiency bound.

Finally, prove
\[
 \|\widehat m_0-m_n^*\|_2^2=O_p(n^{-2/3}),\qquad
 \widehat\psi(\widehat m_0)-\widehat\psi_{\rm iso}
       =o_p(M^{-1/2}).
\]
Thus the estimator has no further first-order gain relative to the population conditional-mean post-processing benchmark based only on its fitted score.
