# Reference Proof

## Proof Structure

1. Condition on the fixed pool and initial information. The admissible proposal maps then give strictly positive probabilities on a finite tree of index histories, ensuring finite second moments for each fixed budget.
2. Derive the running-average representation of LURE, its coefficient normalization, and the conditional-mean identities. Also establish the source's auxiliary uncorrelatedness and variance decomposition, although these are not required conclusions of the public task.
3. Apply generic LURE unbiasedness to the centered proxy and residualized loss arrays.
4. With the proposal process fixed, expand and optimize the control-variate variance quadratic, including all degenerate cases.

## Complete Proof

Fix \(M\), write \(N=N_M\), and condition throughout on the fixed pool and \(H_0\). The proposal maps access labels only through previously queried observations. Since each \(y_i\) is fixed, the queried label history is determined by the index history. Thus each \(Q_m\) is a deterministic function of \((I_1,\ldots,I_{m-1})\), as used in the public filtration \(\mathcal F_m=\sigma(I_1,\ldots,I_m)\).

There are finitely many possible index histories and remaining indices. Strict positivity therefore implies that, for this fixed pool, budget, and proposal process, all positive proposal probabilities have a positive minimum. Consequently the weights and every estimator below for a fixed finite real array have finite second moments. This minimum need not be uniform as \(M\) varies. Also, \(N>M\) makes every denominator involving \(N-m\) strictly positive.

For any fixed real array \(\xi=(\xi_i)_{i=1}^N\), let \(T_{m-1}=\{I_1,\ldots,I_{m-1}\}\) and define
\[
R(\xi)=\frac1N\sum_{i=1}^N\xi_i,\qquad
A_m(\xi)=\frac1N\left(\frac{\xi_{I_m}}{Q_m(I_m)}+\sum_{t<m}\xi_{I_t}\right),
\qquad
\gamma_m=\frac{N(N-M)}{(N-m)(N-m+1)}.
\]
Conditional importance weighting gives
\[
\mathbb E\!\left[\frac{\xi_{I_m}}{Q_m(I_m)}\middle|\mathcal F_{m-1}\right]
=\sum_{i\notin T_{m-1}}Q_m(i)\frac{\xi_i}{Q_m(i)}
=\sum_{i\notin T_{m-1}}\xi_i.
\]
Adding the already sampled terms therefore yields
\[
\mathbb E[A_m(\xi)\mid\mathcal F_{m-1}]=R(\xi).
\]
In particular, \(\mathbb E A_m(\xi)=R(\xi)\).

To establish the representation, collect the coefficient of \(\xi_{I_t}\) in \(\sum_{m=1}^M\gamma_m A_m(\xi)\). It is
\[
\frac{\gamma_t}{NQ_t(I_t)}+\frac1N\sum_{m=t+1}^M\gamma_m.
\]
Using \(1/[k(k+1)]=1/k-1/(k+1)\), the second term equals
\[
(N-M)\sum_{m=t+1}^M\frac1{(N-m)(N-m+1)}
=1-\frac{N-M}{N-t}.
\]
This equality also holds for \(t=M\), when the sum is empty. Hence the collected coefficient is
\[
\frac{N-M}{(N-t)(N-t+1)Q_t(I_t)}+1-\frac{N-M}{N-t}
=1+\frac{N-M}{N-t}\left[\frac1{(N-t+1)Q_t(I_t)}-1\right]
=V_t.
\]
It follows that
\[
\widehat R_{\mathrm{LURE}}(\xi)=\frac1M\sum_{m=1}^M\gamma_m A_m(\xi).
\]
The same telescoping identity gives
\[
\sum_{m=1}^M\gamma_m
=N(N-M)\left(\frac1{N-M}-\frac1N\right)=M.
\]
Consequently,
\[
\mathbb E\widehat R_{\mathrm{LURE}}(\xi)
=\frac1M\sum_{m=1}^M\gamma_m R(\xi)=R(\xi).
\]

For completeness, the auxiliary finite-sample variance identities used in the source follow from the same conditional calculation. The previously sampled sum in \(A_m(\xi)\) is \(\mathcal F_{m-1}\)-measurable, and its conditional mean is the deterministic number \(R(\xi)\). Thus the law of total variance gives
\[
\operatorname{Var}(A_m(\xi))
=\frac1{N^2}\mathbb E\operatorname{Var}\!\left(\frac{\xi_{I_m}}{Q_m(I_m)}\middle|\mathcal F_{m-1}\right).
\]
For \(m<k\), \(A_m(\xi)\) is \(\mathcal F_{k-1}\)-measurable, so
\[
\operatorname{Cov}(A_m(\xi),A_k(\xi))
=\mathbb E\!\left[(A_m(\xi)-R(\xi))\mathbb E[A_k(\xi)-R(\xi)\mid\mathcal F_{k-1}]\right]=0.
\]
Symmetry handles \(k<m\). The deterministic-coefficient representation therefore implies
\[
\operatorname{Var}(\widehat R_{\mathrm{LURE}}(\xi))
=\frac1{M^2}\sum_{m=1}^M\gamma_m^2\operatorname{Var}(A_m(\xi)).
\]
These auxiliary variance identities are not needed for the remaining control-variate calculation.

Now \(c_i=\widetilde\ell_i-\widetilde R_M\) has finite-pool mean zero. For fixed \(\lambda\), the residualized array \(\xi_i=\ell_i-\lambda c_i\) is fixed and has mean \(R_M\). Linearity of the estimator, using the same proposals, indices, and weights, gives
\[
\widehat R_{\mathrm{LURE}}(\xi)=\widehat R_{\mathrm{PPAT}}(\lambda).
\]
Generic LURE unbiasedness therefore proves
\[
\mathbb E\widehat R_{\mathrm{PPAT}}(\lambda)=R_M.
\]
It also gives \(\mathbb E L=R_M\) and \(\mathbb E C=0\), where \(L=\widehat R_{\mathrm{LURE}}(\ell)\) and \(C=\widehat R_{\mathrm{LURE}}(c)\).

Hold the proposal process fixed while varying \(\lambda\). Then \(L\) and \(C\) have a fixed joint law and \(\widehat R_{\mathrm{PPAT}}(\lambda)=L-\lambda C\). Expanding the square of its centered version gives
\[
\operatorname{Var}(L-\lambda C)
=\operatorname{Var}(L)-2\lambda\operatorname{Cov}(L,C)+\lambda^2\operatorname{Var}(C).
\]
If \(v:=\operatorname{Var}(C)>0\), write \(b=\operatorname{Cov}(L,C)\). Completing the square yields
\[
\operatorname{Var}(L-\lambda C)
=\operatorname{Var}(L)-\frac{b^2}{v}+v\left(\lambda-\frac bv\right)^2.
\]
Thus the unique minimizer is \(\lambda^*=b/v\). Moreover,
\[
\operatorname{Var}(L-\lambda C)-\operatorname{Var}(L)
=v\lambda(\lambda-2\lambda^*).
\]
This is negative exactly for \(\min\{0,2\lambda^*\}<\lambda<\max\{0,2\lambda^*\}\), and it is zero at the endpoints. If \(b=0\), the interval is empty and \(\lambda^*=0\) is still the unique minimizer.

If \(\operatorname{Var}(C)=0\), then \(C=\mathbb EC=0\) almost surely. Hence \(\widehat R_{\mathrm{PPAT}}(\lambda)=L\) almost surely for every fixed \(\lambda\); every coefficient minimizes the variance, and none gives strict improvement.
