# Reference Proof

## Proof Structure

The proof first centers the loss at prediction zero, eliminating an otherwise uncontrolled loss baseline without changing either the selected weights or any excess-risk comparison. Conditional on each fold's training complement, the fitted dictionary is fixed, so standard Rademacher arguments uniformly control the centered validation risk over its convex hull. A union bound and a fold-size Cauchy-Schwarz inequality yield the stated cross-fitted rate. Empirical minimization then gives the cross-fitted oracle inequality. Finally, the uniform refit gap is applied twice to transfer the comparison to the deployed full-sample ensemble.

## Complete Proof

Put \(A=L_\ell B\). For fold \(k\), define the centered empirical and population functionals
\[
 \widehat H_k(w)=\frac1{n_k}\sum_{i\in I_k}
 \bigl[\ell(g_w^{(-k)}(X_i),Y_i)-\ell(0,Y_i)\bigr],
 \qquad
 H_k(w)=R_k(w)-r_0,
\]
where \(r_0=\mathbb E[\ell(0,Y)]\), which is finite by assumption. Their weighted averages satisfy
\[
 \widehat H_{\mathrm{CV}}(w)=\widehat R_{\mathrm{CV}}(w)
 -\frac1n\sum_{i=1}^n\ell(0,Y_i),
 \qquad
 H_{\mathrm{CF}}(w)=R_{\mathrm{CF}}(w)-r_0.
\]
Consequently, \(\widehat w\) also minimizes \(\widehat H_{\mathrm{CV}}\), and differences between two values of \(H_{\mathrm{CF}}\) equal the corresponding differences of \(R_{\mathrm{CF}}\).

Fix a fold \(k\) and condition on \(D_{-k}=\{Z_i:i\notin I_k\}\). The functions \(g_1^{(-k)},\ldots,g_M^{(-k)}\) are then fixed, while the observations in \(I_k\) remain independent with law \(P\). Let
\[
 \mathcal F_k=\left\{g_w^{(-k)}=\sum_{j=1}^M w_jg_j^{(-k)}:w\in\Delta_M\right\}.
\]
Every member of \(\mathcal F_k\) is bounded in absolute value by \(B\). For each observation \(z=(x,y)\), the map
\[
 t\longmapsto \ell(t,y)-\ell(0,y)
\]
is \(L_\ell\)-Lipschitz, vanishes at zero, and has absolute value at most \(A\) on \([-B,B]\). Thus contraction, invariance of empirical Rademacher complexity under convex hulls, and the finite-class bound give
\[
 \mathfrak R_{n_k}\bigl((\ell-\ell(0))\circ\mathcal F_k\bigr)
 \le c_0 L_\ell B\sqrt{\frac{\log M}{n_k}},
\]
in the conditional setting, for a universal constant \(c_0\). The bounded-class generalization inequality therefore implies that, conditionally on \(D_{-k}\), with failure probability at most \(\delta/K\),
\[
 \sup_{w\in\Delta_M}|\widehat H_k(w)-H_k(w)|
 \le c_1A\sqrt{\frac{\log(MK/\delta)}{n_k}}
 =:\eta_k,
\]
where the confidence and finite-class terms have been combined into a universal constant \(c_1\). Integrating the conditional failure probability gives the same unconditional bound. A union bound makes these events simultaneous for all \(k\), with probability at least \(1-\delta\). No independence between the fitted dictionaries of different folds is needed.

On this simultaneous event,
\[
\begin{aligned}
 \sup_{w\in\Delta_M}
 |\widehat H_{\mathrm{CV}}(w)-H_{\mathrm{CF}}(w)|
 &\le \sum_{k=1}^K\frac{n_k}{n}\eta_k\\
 &\le c_1A\sqrt{\log(MK/\delta)}\,
       \frac1n\sum_{k=1}^K\sqrt{n_k}\\
 &\le c_1A\sqrt{\frac{K\log(MK/\delta)}n}
 =:a_n.
\end{aligned}
\]
The last inequality is Cauchy-Schwarz, since \(\sum_kn_k=n\); it does not require balanced folds.

For any \(w\in\Delta_M\), empirical optimality of \(\widehat w\) now gives
\[
 H_{\mathrm{CF}}(\widehat w)
 \le \widehat H_{\mathrm{CV}}(\widehat w)+a_n
 \le \widehat H_{\mathrm{CV}}(w)+a_n
 \le H_{\mathrm{CF}}(w)+2a_n.
\]
Taking the infimum over \(w\), returning from centered to original risks, and absorbing the factor two into a universal constant \(C\) yields
\[
 R_{\mathrm{CF}}(\widehat w)
 \le \inf_{w\in\Delta_M}R_{\mathrm{CF}}(w)
 +C L_\ell B\sqrt{\frac{K\log(MK/\delta)}n}.
\]
For interpretation, condition on the observed data and independently draw \(J\) with \(\Pr(J=k)=n_k/n\). The risk of \(g_{\widehat w}^{(-J)}\), averaged over \(J\) and an independent test observation, is
\[
 \sum_{k=1}^K\frac{n_k}{n}R_k(\widehat w)
 =R_{\mathrm{CF}}(\widehat w),
\]
so this is exactly the oracle comparison for the randomized cross-fitted aggregate.

It remains to transfer the result to the full-sample refit. From the definition and assumed bound on \(\Gamma_{\mathrm{ref}}\),
\[
 R_{\mathrm{ref}}(\widehat w)
 \le R_{\mathrm{CF}}(\widehat w)+\varepsilon_n.
\]
Moreover, for every \(w\),
\(R_{\mathrm{CF}}(w)\le R_{\mathrm{ref}}(w)+\varepsilon_n\), and hence
\[
 \inf_wR_{\mathrm{CF}}(w)
 \le \inf_wR_{\mathrm{ref}}(w)+\varepsilon_n.
\]
Combining these two inequalities with the cross-fitted oracle bound proves
\[
 R_{\mathrm{ref}}(\widehat w)
 \le \inf_{w\in\Delta_M}R_{\mathrm{ref}}(w)
 +C L_\ell B\sqrt{\frac{K\log(MK/\delta)}n}
 +2\varepsilon_n.
\]
Finally, \(\mathcal W_0\subseteq\Delta_M\). Replacing either unrestricted infimum by the infimum over \(\mathcal W_0\) only increases its right-hand side, proving both prior-free comparator consequences.
