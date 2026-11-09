# Problem

## Setup

Let \(E\) be an environment variable with distribution \(\pi\). A latent variable \(Z\) has conditional distribution \(p(dz\mid E)\). Given \((Z,E)\), the observed variables \(X\) and \(Y\) are sampled independently from the environment-invariant probability kernels \(p(dx\mid Z)\) and \(p(dy\mid Z)\). Let \(p\) denote the resulting joint law. Assume the regular conditional distributions used below exist. Conditional quantities are understood almost everywhere with respect to their conditioning marginals.

For the label mechanism, let \(p(y\mid z)\) denote a fixed jointly measurable conditional density with respect to a fixed sigma-finite measure \(\lambda_Y\), so that
\[
p(dy\mid z)=p(y\mid z)\,\lambda_Y(dy).
\]
This includes a conditional probability mass function when \(\lambda_Y\) is counting measure.

Let \((e,x,y)\mapsto q_e(dz\mid x,y)\) be a measurable probability kernel. The variational kernels have densities \(q_e(z\mid x,y)\) with respect to one fixed sigma-finite measure \(\lambda_Z\) on the latent space, and the map \((e,x,y,z)\mapsto q_e(z\mid x,y)\) is jointly measurable.

Define the mixtures
\[
\bar q_{xy}(dz\mid x,y):=\int q_e(dz\mid x,y)\,p(de\mid x,y),
\]
\[
q_x^e(dz\mid x):=\int q_e(dz\mid x,y)\,p(dy\mid x,e),
\qquad
\bar q_x(dz\mid x):=\int q_x^e(dz\mid x)\,p(de\mid x).
\]

For probability measures \(\mu,\nu\), let
\[
D(\mu\|\nu):=\int\log\!\left(\frac{d\mu}{d\nu}\right)d\mu
\]
when \(\mu\ll\nu\), and let \(D(\mu\|\nu)=+\infty\) otherwise.

Assume the log likelihood is jointly absolutely integrable:
\[
\int p(dx,dy,de)\int q_e(dz\mid x,y)\,|\log p(y\mid z)|<\infty.
\]
Assume also that the following four nonnegative integrals are finite:
\[
\int p(dx,dy,de)\,
D\!\left(q_e(\cdot\mid x,y)\middle\|q_x^e(\cdot\mid x)\right)<\infty,
\]
\[
\int p(dx,dy)\,
D\!\left(\bar q_{xy}(\cdot\mid x,y)\middle\|\bar q_x(\cdot\mid x)\right)<\infty,
\]
\[
\int p(dx,dy,de)\,
D\!\left(q_e(\cdot\mid x,y)\middle\|\bar q_{xy}(\cdot\mid x,y)\right)<\infty,
\]
\[
\int p(dx,de)\,
D\!\left(q_x^e(\cdot\mid x)\middle\|\bar q_x(\cdot\mid x)\right)<\infty.
\]

Define
\[
\mathcal L_e:=\mathbb E_{p(x,y\mid e)}
\left[
\mathbb E_{q_e(z\mid x,y)}\log p(y\mid z)
-D\!\left(q_e(\cdot\mid x,y)\middle\|q_x^e(\cdot\mid x)\right)
\right],
\]
\[
\mathcal L:=\mathbb E_{p(x,y)}
\left[
\mathbb E_{\bar q_{xy}(z\mid x,y)}\log p(y\mid z)
-D\!\left(\bar q_{xy}(\cdot\mid x,y)\middle\|\bar q_x(\cdot\mid x)\right)
\right],
\]
and
\[
\begin{aligned}
R(q):={}&\mathbb E_{p(x,y)}\mathbb E_{p(e\mid x,y)}
D\!\left(q_e(\cdot\mid x,y)\middle\|\bar q_{xy}(\cdot\mid x,y)\right)\\
&-\mathbb E_{p(x)}\mathbb E_{p(e\mid x)}
D\!\left(q_x^e(\cdot\mid x)\middle\|\bar q_x(\cdot\mid x)\right).
\end{aligned}
\]

## Task

Prove the integrated identity
\[
\boxed{\mathcal L=\mathbb E_{e\sim\pi}[\mathcal L_e]+R(q).}
\]
