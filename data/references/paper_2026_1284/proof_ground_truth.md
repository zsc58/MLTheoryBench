# Reference Proof

## Proof Structure

Let \(\nu_l\) be the generated laws, \(\mu_l\) their forward transition-pair laws, and \(\mu_l^\leftarrow\) the swapped laws. Vanishing MMD loss first yields convergence to zero of the signed pair differences \(A_l=\mu_l-\mu_l^\leftarrow\) against \(C_0(S^2)\). This varying-measure step is justified by tightness of both pair-law families: continuity and normalization of \(q\) give total-variation continuity of the transition law in its starting point, and the assumed tightness of \(\{\nu_l\}\) then gives pair-law tightness. A compact-cutoff argument using positivity and continuity of the transition density, detailed balance, and tightness transfers this to the target-weighted antisymmetric measures \(B_l=\nu_l\otimes\pi-\pi\otimes\nu_l\). Marginalization then yields \(\nu_l\Rightarrow\pi\).

## Complete Proof

Write \(\rho\) for the density of \(\pi\), and \(f_l\) for the density of \(\nu_l\). Let \(Q_x(dy)=q(x,y)\,dy\). The forward and reverse pair laws have densities
\[
 d\mu_l(x,y)=f_l(x)q(x,y)\,dx\,dy,\qquad d\mu_l^\leftarrow(x,y)=f_l(y)q(y,x)\,dx\,dy.
\]
Set \(A_l=\mu_l-\mu_l^\leftarrow\).

We first justify the pairwise consequence of the MMD hypothesis. Since \(q\) is a transition density, \(\int q(x,y)\,dy=1\) for every \(x\). If \(x_n\to x\), continuity of \(q\) gives pointwise convergence \(q(x_n,y)\to q(x,y)\), and Scheffe's lemma gives \(\|Q_{x_n}-Q_x\|_{\rm TV}\to0\). Thus \(x\mapsto Q_x\) is continuous in total variation. A continuous family of probability measures indexed by a compact set is uniformly tight: cover the compact set by finitely many neighborhoods on which the transition laws are close in total variation, choose a compact set for each center, and take their finite union.

Now use tightness of \(\{\nu_l\}\). For any \(\varepsilon>0\), choose a compact \(K\subset S\) with \(\sup_l\nu_l(K^c)\) small. Uniform tightness of \(\{Q_x:x\in K\}\) gives a compact \(C\subset S\) with \(\sup_{x\in K}Q_x(C^c)\) small. Hence \(\{\mu_l\}\) is tight on \(S^2\), because \(\mu_l(K\times C)\) is uniformly close to one. The swapped family \(\{\mu_l^\leftarrow\}\) is tight as well.

Let \(d_\kappa\) denote MMD. The hypothesis says \(d_\kappa(\mu_l,\mu_l^\leftarrow)\to0\). Consider any subsequence. By tightness, it has a further subsequence, still indexed by \(l\), for which \(\mu_l\Rightarrow\mu\) and \(\mu_l^\leftarrow\Rightarrow\widetilde\mu\). Applying the fixed-limit MMD metrization result to each sequence gives \(d_\kappa(\mu_l,\mu)\to0\) and \(d_\kappa(\mu_l^\leftarrow,\widetilde\mu)\to0\). The triangle inequality therefore gives \(d_\kappa(\mu,\widetilde\mu)=0\), so characteristicness implies \(\mu=\widetilde\mu\). Consequently, along this further subsequence, \(\int\varphi\,dA_l\to0\) for every \(\varphi\in C_0(S^2)\). Since every subsequence has such a further subsequence, the full sequence satisfies
\[
\int\varphi\,dA_l\longrightarrow0\qquad(\varphi\in C_0(S^2)).
\]

Detailed balance and strict positivity also imply that \(\rho\) is continuous. Indeed, choose \(x_0\) with \(\rho(x_0)>0\), which exists because \(\rho\) integrates to one. Then
\[
\rho(y)=\rho(x_0)\frac{q(x_0,y)}{q(y,x_0)},
\]
so \(\rho\) is continuous (and positive).

Fix \(h\in C_b(S^2)\) and \(\varepsilon>0\). Choose a compact \(K\subset S\) such that \(\sup_l\nu_l(K^c)\) and \(\pi(K^c)\) are small enough that
\[
\sup_l\int_{(K\times K)^c}\left|f_l(x)\rho(y)-\rho(x)f_l(y)\right|\,dx\,dy
\le 2\bigl(\sup_l\nu_l(K^c)+\pi(K^c)\bigr)
\]
is less than \(\varepsilon/(2\|h\|_\infty)\) (with the zero function handled trivially). Choose \(\chi\in C_c^\infty(S^2)\) equal to one on \(K\times K\), with \(0\le\chi\le1\), and define
\[
 g(x,y)=\chi(x,y)h(x,y)\frac{\rho(y)}{q(x,y)}.
\]
Then \(g\in C_0(S^2)\). Detailed balance gives
\[
 g\,dA_l=\chi h\,[f_l(x)\rho(y)-\rho(x)f_l(y)]\,dx\,dy
=\chi h\,dB_l,
\]
where \(dB_l(x,y)=[f_l(x)\rho(y)-\rho(x)f_l(y)]\,dx\,dy\). Hence \(\int \chi h\,dB_l\to0\). Since \(\chi=1\) on \(K\times K\), the difference between \(\int h\,dB_l\) and \(\int \chi h\,dB_l\) is supported in \((K\times K)^c\) and is bounded by the displayed tail estimate. Therefore \(\int h\,dB_l\to0\) for every \(h\in C_b(S^2)\).

Finally, for any \(u\in C_b(S)\), take \(h(x,y)=u(x)\). Since both factors are probability measures,
\[
\int h\,dB_l=\int u\,d\nu_l-\int u\,d\pi.
\]
Thus \(\int u\,d\nu_l\to\int u\,d\pi\) for every bounded continuous \(u\), proving \(\nu_l\Rightarrow\pi\).
