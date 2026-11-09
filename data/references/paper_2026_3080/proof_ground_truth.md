# Reference Proof

## Proof Structure

Write each finite-horizon error as its stationary level plus its finite-horizon excess. Averaging the resulting identity over tasks gives the transfer decomposition. For equal task durations, rescale the excess terms by their cumulative values; individual sublinearity of these cumulative quantities makes their difference negligible compared with a positive stationary gap.

## Complete Proof

Fix a task k and abbreviate the retained procedure by R and the reset procedure by S. By the definition of the transient excess,

\[
E_N^k(A)=r^k(A)+\varepsilon_N^k(A),\qquad A\in\{R,S\}.
\]

Therefore

\[
\begin{aligned}
g_N^k
&=E_N^k(S)-E_N^k(R)\\
&=\bigl(r^k(S)-r^k(R)\bigr)
  +\varepsilon_N^k(S)-\varepsilon_N^k(R)\\
&=-\iota^k+\varepsilon_N^k(S)-\varepsilon_N^k(R),
\end{aligned}
\]

because \(\iota^k=r^k(R)-r^k(S)\). Averaging this equality over \(k=1,\ldots,m\) proves

\[
\bar g_N=-\bar\iota+\bar\varepsilon_N(S)-\bar\varepsilon_N(R).
\]

Since all tasks have duration \(N\), \(\varepsilon_N^k(A)=\Delta_N^k(A)/N\). Hence

\[
\bar\varepsilon_N(S)-\bar\varepsilon_N(R)
=\frac{\bar\Delta_N(S)-\bar\Delta_N(R)}{N}
=\frac{D_N}{N},
\]

which gives the claimed exact equal-duration formula

\[
\bar g_N=-\bar\iota+\frac{D_N}{N}.
\]

By assumption, both \(\bar\Delta_N(S)=o(N)\) and \(\bar\Delta_N(R)=o(N)\). Their difference therefore satisfies \(D_N=o(N)\), so \(D_N/N\to0\). Taking \(\eta=\bar\iota/2\), there is \(N_0\) such that for all \(N\ge N_0\),

\[
\frac{D_N}{N}<\frac{\bar\iota}{2}.
\]

Consequently, for every \(N\ge N_0\),

\[
\bar g_N< -\bar\iota+\frac{\bar\iota}{2}
=-\frac{\bar\iota}{2}<0.
\]

Thus, beyond a sufficiently long common task duration, the retained procedure has larger average error than the reset procedure. Finally, at any breakeven duration \(N_{\mathrm{crit}}\) satisfying \(\bar g_{N_{\mathrm{crit}}}=0\), the exact formula yields

\[
N_{\mathrm{crit}}
=\frac{D_{N_{\mathrm{crit}}}}{\bar\iota}
=\frac{\bar\Delta_{N_{\mathrm{crit}}}(S)-\bar\Delta_{N_{\mathrm{crit}}}(R)}{\bar\iota}.
\]

This is precisely the stated critical-duration ratio, with the cumulative quantities evaluated at the breakeven scale.
