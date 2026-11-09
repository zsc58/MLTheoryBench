# Reference Proof

## Proof Structure

Fix a set and encode its indicator by a sign-valued function. Apply Gaussian smoothing and Hermite truncation, then square an affine transform of the truncated polynomial. The square gives non-negativity and doubles degree at most. An algebraic decomposition controls the approximation error by the smoothing and truncation errors. Choose the smoothing parameter and truncation degree to split the error budget.

## Complete Proof

Fix $H\in\mathcal H$ and write $h=\mathbf 1_H$ and $f=2h-1$. For $\rho\in[0,1]$, let
\[
g=T_\rho f,\qquad p=\Pi_{\le t}g,
\]
where $t$ is a nonnegative integer. Define
\[
q=\frac{(1+p)^2}{4}.
\]
Then $q(x)\ge 0$ for every $x$, and since $\deg p\le t$, $\deg q\le 2t$.

Because $g$ is an average of values in $\{-1,1\}$, $|g|\le1$. Also $\|g\|_2\le\|f\|_2=1$ by contraction, and orthogonal projection gives $\|p\|_2\le\|g\|_2\le1$. Hence $\|p+g+2\|_2\le\|p\|_2+\|g\|_2+2\le4$.

Insert $(g+1)/2$ between $q$ and $h=(f+1)/2$. Pointwise,
\[
q-\frac{g+1}{2}=\frac{(p-g)(p+g+2)+(g^2-1)}4.
\]
Therefore, by triangle inequality and Cauchy--Schwarz,
\[
\left\|q-\frac{g+1}{2}\right\|_1
\le \|p-g\|_2+\frac14\|g^2-1\|_1.
\]
Since $f^2=1$ and $|f|,|g|\le1$,
\[
\|g^2-1\|_1=\|(g-f)(g+f)\|_1\le2\|g-f\|_1.
\]
Combining this with $\|(g+1)/2-h\|_1=\frac12\|g-f\|_1$ yields
\[
\|q-h\|_1\le \|p-g\|_2+\|f-g\|_1.
\]
The Gaussian smoothing/truncation bounds give
\[
\|f-g\|_1\le2\sqrt\pi\,\Gamma(H)\sqrt{1-\rho},
\qquad
\|g-p\|_2\le\rho^{t+1}.
\]
Thus
\[
\|q-\mathbf1_H\|_1\le \rho^{t+1}+2\sqrt\pi\,\Gamma(H)\sqrt{1-\rho}.
\]
If $\Gamma(H)=0$, take $\rho=t=0$; the displayed bound is zero. Otherwise set
\[
1-\rho=\min\left\{1,\frac{\varepsilon^2}{16\pi\Gamma(H)^2}\right\}.
\]
The smoothing term is then at most $\varepsilon/2$. If $\rho=0$, take $t=0$. If $\rho>0$, choose the least integer $t\ge0$ with $\rho^{t+1}\le\varepsilon/2$. Using $\log(1/\rho)\ge1-\rho$, this choice satisfies
\[
t+1\le 1+\frac{\log(2/\varepsilon)}{1-\rho}
=O\!\left(\Gamma_H^2\varepsilon^{-2}\log(1/\varepsilon)\right),
\]
with the $\rho=0$ case included separately. Hence the truncation term is at most $\varepsilon/2$, the total error is at most $\varepsilon$, and $\deg q\le2t=O(\Gamma_H^2\varepsilon^{-2}\log(1/\varepsilon))$. Since $H$ and $\varepsilon$ were arbitrary, the theorem follows.
