# Problem

## Setup

Let \(K,q\) be positive integers. For each class \(k\), let the clean data matrix have rows \(z_i^{\star(k)}\in\mathbb R^q\), \(i=1,\ldots,n_k\), where \(n_k\) is positive. Assume every clean class is in general position: every affine \((q-1)\)-dimensional subspace of \(\mathbb R^q\) contains at most \(q\) of its rows. Let \(x_i^{(k)}\) denote data presented to an estimator after possible replacements. Choose integers
\[
\lfloor n_k/2\rfloor+1\le h_k\le n_k,
\qquad
\beta_0=\min_{1\le k\le K}\frac{n_k-h_k+1}{n_k}.
\]

For each class, \(\Sigma^{(k)}\) is a symmetric positive-definite \(q\times q\) matrix and \(\mu^{(k)}\in\mathbb R^q\). Its shared/class-specific representation is the uniquely normalized decomposition
\[
\Sigma^{(k)}=\Theta\circ\Gamma^{(k)}.
\]
Here \(\circ\) denotes entrywise multiplication. Specifically, for \(i\ne j\), put
\[
\rho_{ij}^{(k)}=\frac{\sigma_{ij}^{(k)}}{\sqrt{\sigma_{ii}^{(k)}\sigma_{jj}^{(k)}}},
\qquad
\theta_{ij}=\left\{\frac1K\sum_{k=1}^K\bigl(\rho_{ij}^{(k)}\bigr)^2\right\}^{1/2},
\qquad \theta_{ii}=1,
\]
and set
\[
\gamma_{ii}^{(k)}=\sigma_{ii}^{(k)},
\qquad
\gamma_{ij}^{(k)}=
\begin{cases}
\sigma_{ij}^{(k)}/\theta_{ij},&\theta_{ij}>0,\\
0,&\theta_{ij}=0.
\end{cases}
\]
For a \(q\times q\) matrix \(A\), define
\[
\|A\|_{1,\mathrm{off}}=\sum_{i\ne j}|A_{ij}|,
\]
with an empty sum equal to zero. Let \(\lambda_1,\lambda_2>0\) and \(a_k>0\).

The joint casewise estimator is any minimizer of
\[
L_{\mathrm{case}}=
\sum_{k=1}^K\sum_{i=1}^{n_k}w_i^{(k)}
\left[\log\det\Sigma^{(k)}+q\log(2\pi)
 +(x_i^{(k)}-\mu^{(k)})^T(\Sigma^{(k)})^{-1}(x_i^{(k)}-\mu^{(k)})\right]
+\lambda_1\|\Theta\|_{1,\mathrm{off}}
+\lambda_2\sum_{k=1}^K\|\Gamma^{(k)}\|_{1,\mathrm{off}},
\]
over binary row weights \(w_i^{(k)}\) satisfying \(\sum_iw_i^{(k)}=h_k\), subject to the normalized covariance representation above and \(\lambda_{\min}(\Sigma^{(k)})\ge a_k\) for every \(k\).

For the joint cellwise estimator, fix constants \(b_j^{(k)}>0\). Its binary mask entries are \(m_{ij}^{(k)}\), and
\[
J_i^{(k)}=\{j:m_{ij}^{(k)}=1\}.
\]
It is any minimizer of
\[
L_{\mathrm{cell}}=
\sum_{k=1}^K\sum_{i=1}^{n_k}
\ell_{J_i^{(k)}}(x_i^{(k)};\mu^{(k)},\Sigma^{(k)})
+\sum_{k=1}^K\sum_{j=1}^q b_j^{(k)}\sum_{i=1}^{n_k}(1-m_{ij}^{(k)})
+\lambda_1\|\Theta\|_{1,\mathrm{off}}
+\lambda_2\sum_{k=1}^K\|\Gamma^{(k)}\|_{1,\mathrm{off}},
\]
subject to binary masks, \(\sum_i m_{ij}^{(k)}\ge h_k\) for every \(j,k\), the normalized covariance representation, and \(\lambda_{\min}(\Sigma^{(k)})\ge a_k\). For nonempty \(J\),
\[
\ell_J(x;\mu,\Sigma)=
\log\det\Sigma_{JJ}+|J|\log(2\pi)
+(x_J-\mu_J)^T\Sigma_{JJ}^{-1}(x_J-\mu_J),
\]
and \(\ell_{\varnothing}=0\).

In the breakdown definitions below, the hats denote an arbitrary fixed choice of exact minimizer for each input sample in the indicated regime. The claims are required for every such choice.

For a count vector \(r=(r_1,\ldots,r_K)\) with integers \(0\le r_k\le n_k\), put
\[
\beta(r)=\max_{1\le k\le K}\frac{r_k}{n_k}.
\]
Let \(\mathcal C_{\mathrm{case}}(r)\) be the set of samples obtained from the clean data by replacing at most \(r_k\) whole rows in class \(k\). Let \(\mathcal C_{\mathrm{cell}}(r)\) be the set of samples obtained by replacing at most \(r_k\) cells in each column of class \(k\).

For \(\mathcal R\in\{\mathrm{case},\mathrm{cell}\}\), define
\[
\epsilon_{\mathcal R,\mu}^*
=\inf\left\{\beta(r):
\sup_{\widetilde Z\in\mathcal C_{\mathcal R}(r)}
\max_k\|\widehat\mu^{(k)}(\widetilde Z)-\widehat\mu^{(k)}(Z^\star)\|_2=\infty\right\},
\]
\[
\epsilon_{\mathcal R,+}
=\inf\left\{\beta(r):
\sup_{\widetilde Z\in\mathcal C_{\mathcal R}(r)}
\max_k\lambda_{\max}(\widehat\Sigma^{(k)}(\widetilde Z))=\infty\right\},
\]
and
\[
\epsilon_{\mathcal R,-}
=\inf\left\{\beta(r):
\inf_{\widetilde Z\in\mathcal C_{\mathcal R}(r)}
\min_k\lambda_{\min}(\widehat\Sigma^{(k)}(\widetilde Z))=0\right\}.
\]
If the set defining one of these values is empty over admissible fractions in \([0,1]\), report that value as \(1\).

## Task

Prove that, for both \(\mathcal R=\mathrm{case}\) and \(\mathcal R=\mathrm{cell}\),
\[
\epsilon_{\mathcal R,-}=1,
\qquad
\epsilon_{\mathcal R,+}\ge\beta_0,
\qquad
\epsilon_{\mathcal R,\mu}^*\ge\beta_0.
\]
Moreover, the common lower bound \(\beta_0\) is sharp: for each regime, at contamination fraction \(\beta_0\), there is a permitted finite replacement sequence for which location breakdown or scatter-explosion breakdown occurs. Hence no larger common lower bound for those two modes is valid.
