# Problem

## Setup

Let \(d,N,K\) be positive integers with \(N>d+1\). Let \(\Sigma_x\in\mathbb R^{d\times d}\) be positive definite, have operator norm one, and have positive minimum eigenvalue. The rows of \(X\in\mathbb R^{N\times d}\) are independent \(\mathcal N(0,\Sigma_x)\) vectors. There is one main task, indexed by \(m\), and auxiliary tasks indexed by \(k=1,\ldots,K\). Fix vectors \(w_m^*,w_1^*,\ldots,w_K^*\in\mathbb R^d\) and finite variance parameters \(\sigma_t^2\geq 0\) for \(t=m,1,\ldots,K\). The training labels are
\[
Y_t=Xw_t^*+\varepsilon_t,
\]
where the noise vectors are mutually independent and independent of \(X\), and the entries of each \(\varepsilon_t\) are independent \(\mathcal N(0,\sigma_t^2)\) random variables. Choose fixed, nonrandom weights \(\lambda_k\in[0,\infty)\), set \(\Lambda=\sum_k\lambda_k\), and define
\[
\widehat w=\arg\min_{w\in\mathbb R^d}\left\{\|Xw-Y_m\|^2+\sum_{k=1}^K\lambda_k\|Xw-Y_k\|^2\right\}.
\]
Draw \(x\sim\mathcal N(0,\Sigma_x)\) and \(\varepsilon\sim\mathcal N(0,\sigma_m^2)\) independently of each other and of all training quantities, and set \(y_m=x^\top w_m^*+\varepsilon\). Define \(E_K=\mathbb E[(x^\top\widehat w-y_m)^2]\), with expectation over training data, test data, and noises. Let \(E_0\) denote the same quantity with all auxiliary weights zero. When \(\Lambda>0\), define \(\lambda'_k=\lambda_k/\Lambda\) and \(w_a^*=\sum_k\lambda'_kw_k^*\).

## Task

Prove that, for \(\Lambda>0\),
\[
E_K=\frac{\sigma_m^2+\sum_{k=1}^K\lambda_k^2\sigma_k^2}{(1+\Lambda)^2}\frac{d}{N-d-1}
+\left(\frac{\Lambda}{1+\Lambda}\right)^2\left\|\Sigma_x^{1/2}(w_a^*-w_m^*)\right\|^2+\sigma_m^2,
\]
while
\[
E_0=\sigma_m^2\frac{d}{N-d-1}+\sigma_m^2.
\]
Moreover, for \(\Lambda>0\), auxiliary learning improves expected main-task error exactly when
\[
\left(\left[\sum_{k=1}^K(\lambda'_k)^2\sigma_k^2-\sigma_m^2\right]\frac{d}{N-d-1}+\left\|\Sigma_x^{1/2}(w_a^*-w_m^*)\right\|^2\right)\Lambda
<2\sigma_m^2\frac{d}{N-d-1},
\]
that is, \(E_K<E_0\) if and only if this inequality holds.
