# Problem

## Setup

Let \(d,n,r\) be positive integers with \(1\le r<d\), and let \(\sigma_G>0\). Draw \(Z\in\mathbb R^{d\times r}\) with independent columns distributed as \(\mathcal N(0,I_d/r)\), and set \(M=ZZ^\top\). Independently draw \(\Xi\in\mathbb R^{d\times n}\) whose columns are independent \(\mathcal N(0,\sigma_G^2I_d)\). Define the randomized mechanism
\[
\mathcal M_2(V)=M(V+\Xi),\qquad V\in\mathbb R^{d\times n}.
\]
The draws are internal randomness of the mechanism and do not depend on its input.

Let \(\mathcal D\subseteq\mathbb R^{d\times n}\) be an input domain equipped with a specified symmetric neighboring relation \(\sim\). Write \(\Delta=V-V'\) and \(s=\min\{d,n\}\). A randomized mechanism \(\mathcal A\) is \((\varepsilon,\delta)\)-differentially private on this domain if the same parameters satisfy, for every measurable output event \(E\) and every \(V\sim V'\),
\[
\Pr[\mathcal A(V)\in E]\le e^\varepsilon\Pr[\mathcal A(V')\in E]+\delta,
\]
and the analogous inequality with \(V,V'\) exchanged. Probabilities are over the internal randomness.

Let \(I_\alpha(a,b)\) denote the regularized Beta CDF for \(a,b>0\). Let \(\Phi\) be the standard normal CDF and define, for \(\varepsilon>0\),
\[
T(\varepsilon;\mu)=
\begin{cases}
\Phi\!\left(\dfrac{-\varepsilon+\mu/2}{\sqrt\mu}\right)+1-\Phi\!\left(\dfrac{\varepsilon+\mu/2}{\sqrt\mu}\right),&\mu>0,\\
0,&\mu=0.
\end{cases}
\]

## Task

Prove that for every fixed neighboring pair \(V,V'\), every \(\varepsilon>0\), and every \(\alpha\in(0,1)\), there exists \(\delta_\alpha(\varepsilon;V,V')\in[0,1]\) such that both inequalities
\[
\Pr[\mathcal M_2(V)\in E]
\le e^\varepsilon\Pr[\mathcal M_2(V')\in E]+\delta_\alpha(\varepsilon;V,V'),
\]
\[
\Pr[\mathcal M_2(V')\in E]
\le e^\varepsilon\Pr[\mathcal M_2(V)\in E]+\delta_\alpha(\varepsilon;V,V')
\]
hold for every measurable \(E\subseteq\mathbb R^{d\times n}\), with
\[
\delta_\alpha(\varepsilon;V,V')\le
T\!\left(\varepsilon;\frac{\alpha\|V-V'\|_F^2}{\sigma_G^2}\right)
+s\left[1-I_\alpha\!\left(\frac r2,\frac{d-r}2\right)\right].
\]
Here \(\|\cdot\|_F\) is the Frobenius norm. This is a pairwise privacy guarantee; a differential-privacy parameter for the whole domain must be valid uniformly over all neighboring pairs.
