# Reference Proof

## Proof Structure

Derive the exact coordinatewise recursions in the singular-vector basis for spectral and ordinary updates. Express the conditional bias as signal and confounding components on the top and complementary singular subspaces. Apply the separated learning-rate and stopping conditions to the four spectral terms, then show ordinary boosting converges to the confounding component.

## Complete Proof

Fix an instance indexed by p and condition on its realized design X_p=U_pD_pV_p^T. Write U=U_p, D=D_p, V=V_p, n=n_p, k=k_p, and let P_X=UU^T and P_H=\sum_{i=1}^q u_i u_i^T. Since f_0=X_p\beta_0 and g_0=X_pb_0, both lie in the column space of X_p.

For spectral boosting, define r_m=Y-\hat f_m^{\mathrm{sp}}. The update gives
\[
r_{m+1}=(I-\nu P_XW)r_m.
\]
Because W=U\operatorname{diag}(w_1,\ldots,w_k)U^T and P_X=UU^T, the operators commute and have eigenvalues w_i on u_i. Starting from \hat f_0=0, therefore
\[
\hat f_m^{\mathrm{sp}}=\sum_{i=1}^k\bigl[1-(1-\nu w_i)^m\bigr]\langle Y,u_i\rangle u_i.
\]
Using E[\varepsilon\mid X_p]=0 and writing f_i=\langle f_0,u_i\rangle, g_i=\langle g_0,u_i\rangle, the conditional bias is
\[
E[\hat f_m^{\mathrm{sp}}\mid X_p]-f_0
= -\sum_{i=1}^k(1-\nu w_i)^m f_i u_i
 +\sum_{i=1}^k\bigl[1-(1-\nu w_i)^m\bigr]g_i u_i.
\]
Split each sum at q. On the bulk signal subspace (i>q), since 0\le \nu w_i<1,
\[
(1-\nu w_i)^m\le e^{-m\nu w_i}\le e^{-m\nu w_M}.
\]
Hence its normalized norm is at most e^{-m\nu w_M}\|f_0\|/\sqrt n, which tends to zero. The top-band signal norm is at most \|P_Hf_0\|/\sqrt n, also tending to zero. On the top-band confounding subspace, the inequality 1-(1-x)^m\le mx for x\in[0,1] gives
\[
1-(1-\nu w_i)^m\le m\nu w_H,
\]
so the normalized norm is at most m\nu w_H\|g_0\|/\sqrt n, tending to zero. The bulk confounding norm is bounded by \|(I-P_H)g_0\|/\sqrt n, which tends to zero. The bounded-energy assumption and the stopping conditions \(m_p\to\infty\), \(m_p\nu w_M\to\infty\), and \(m_p\nu w_H\to0\) thus imply
\[
\frac{\|E[\hat f_{m_p}^{\mathrm{sp}}\mid X_p]-f_0\|_2}{\sqrt{n_p}}\longrightarrow0.
\]

For ordinary boosting, the update is \hat f_{m+1}^{\mathrm{or}}=\hat f_m^{\mathrm{or}}+\nu P_X(Y-\hat f_m^{\mathrm{or}}). The same residual calculation yields
\[
E[\hat f_m^{\mathrm{or}}\mid X_p]-f_0
=-(1-\nu)^m f_0+\bigl[1-(1-\nu)^m\bigr]g_0.
\]
Let b_m=(1-\nu)^m. For any sequence m_p\to\infty, b_{m_p}\to0. By the reverse triangle inequality,
\[
\frac{\|E[\hat f_{m_p}^{\mathrm{or}}\mid X_p]-f_0\|_2}{\sqrt{n_p}}
\ge (1-b_{m_p})\frac{\|g_0\|_2}{\sqrt{n_p}}-b_{m_p}\frac{\|f_0\|_2}{\sqrt{n_p}}.
\]
The bounded signal energy and the assumption \(\liminf_p\|g_0\|_2/\sqrt{n_p}>0\) make the right-hand side bounded away from zero for all sufficiently large p. Thus ordinary boosting's normalized conditional bias does not converge to zero.
