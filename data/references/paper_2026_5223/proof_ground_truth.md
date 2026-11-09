# Reference Proof

## Proof Structure

For each scale, derive the forgotten least-squares dynamic-regret bound using a one-step identity, a discounted leverage estimate, and a moving-comparator potential calculation. Transfer this bound to the clipped scale predictions. Derive the finite-pool aggregation bound directly from the stated positive-part update, then combine the raw and scale alternatives. All arguments are deterministic, and the comparator path need not be causal.

## Complete Proof

### 1. Initialization, one-step identity, and residual bound

Fix a scale \(h\in H\). Write \(x_t=\widetilde z_t\), \(\gamma=1-1/h\), \(w_t=v_t^{(h)}\), and suppress the scale superscript on \(A_t,b_t\). Then \(\gamma\in[1/2,1)\). Induction in the recursion gives
\[
A_t=\gamma^t\delta I_d+\sum_{s=1}^t\gamma^{t-s}x_sx_s^\top\succ0.
\]
Thus every inverse used by the algorithm exists. Also \(A_{t-1}w_t=b_{t-1}\), including \(t=1\) because both sides are zero. Consequently,
\[
A_t(w_t-w_{t+1})
=\gamma A_{t-1}w_t+x_tx_t^\top w_t-b_t
=(x_t^\top w_t-y_t)x_t.
\]
Let \(\ell_t(w)=(x_t^\top w-y_t)^2\) and \(g_t=2(x_t^\top w_t-y_t)x_t\). Therefore
\[
g_t=2A_t(w_t-w_{t+1}).
\]
For a positive semidefinite matrix \(A\), write \(\|v\|_A^2=v^\top Av\). Expanding squared loss gives, for every \(u\in\mathbb R^d\),
\[
\ell_t(w_t)-\ell_t(u)
=g_t^\top(w_t-u)-\bigl(x_t^\top(w_t-u)\bigr)^2.
\]
The polarization identity and the displayed update give
\[
\begin{aligned}
g_t^\top(w_t-u)
&=\|w_t-u\|_{A_t}^2-\|w_{t+1}-u\|_{A_t}^2
  +\|w_t-w_{t+1}\|_{A_t}^2\\
&=\|w_t-u\|_{A_t}^2-\|w_{t+1}-u\|_{A_t}^2
  +\tfrac14 g_t^\top A_t^{-1}g_t.
\end{aligned}
\]
Since
\[
\|w_t-u\|_{A_t}^2
=\gamma\|w_t-u\|_{A_{t-1}}^2+\bigl(x_t^\top(w_t-u)\bigr)^2,
\]
the curvature terms cancel, yielding
\[
\ell_t(w_t)-\ell_t(u)
=\gamma\|w_t-u\|_{A_{t-1}}^2-\|w_{t+1}-u\|_{A_t}^2
 +\tfrac14 g_t^\top A_t^{-1}g_t. \tag{1}
\]
The assumed prediction-time bound gives
\[
|x_t^\top w_t-y_t|\le B_zR+B_y=D.
\]
The same residual bound holds for each comparator coefficient \(u_t\). In particular,
\[
\tfrac14 g_t^\top A_t^{-1}g_t
=(x_t^\top w_t-y_t)^2x_t^\top A_t^{-1}x_t
\le D^2x_t^\top A_t^{-1}x_t. \tag{2}
\]

### 2. Discounted leverage estimate

Put \(G_t=\gamma A_{t-1}\succ0\) and \(q_t=x_t^\top G_t^{-1}x_t\ge0\). Direct multiplication gives
\[
(G_t+x_tx_t^\top)\frac{G_t^{-1}x_t}{1+q_t}=x_t,
\]
so
\[
x_t^\top A_t^{-1}x_t=\frac{q_t}{1+q_t}.
\]
Factoring \(A_t\) by \(G_t^{1/2}\) also gives
\[
\det A_t=\det G_t\,(1+q_t)=\gamma^d\det A_{t-1}(1+q_t).
\]
Indeed, the intervening matrix is \(I+ss^\top\), where \(s=G_t^{-1/2}x_t\), whose determinant is \(1+\|s\|_2^2=1+q_t\). Thus
\[
\log(1+q_t)=\log\det A_t-\log\det A_{t-1}+d\log(1/\gamma).
\]
For \(q\ge0\), integration of \((1+s)^{-1}\) on \([0,q]\) gives \(\log(1+q)\ge q/(1+q)\). Summing yields
\[
\sum_{t=1}^T x_t^\top A_t^{-1}x_t
\le \log\frac{\det A_T}{\det A_0}+dT\log(1/\gamma). \tag{3}
\]
For every \(t=0,\ldots,T\), the expanded recursion and \(x_sx_s^\top\preceq B_z^2I_d\) imply
\[
A_t\preceq\left(\delta+B_z^2\sum_{j=0}^{t-1}\gamma^j\right)I_d
\preceq(\delta+B_z^2h)I_d.
\]
Consequently,
\[
\log\frac{\det A_T}{\det A_0}
\le d\log\left(1+\frac{B_z^2h}{\delta}\right).
\]
Furthermore,
\[
\log(1/\gamma)=-\log(1-1/h)
\le\frac{1/h}{1-1/h}=\frac1{h-1}\le\frac2h.
\]
Substitution in (3) proves
\[
\sum_{t=1}^T x_t^\top A_t^{-1}x_t
\le d\log\left(1+\frac{B_z^2h}{\delta}\right)+\frac{2dT}{h}. \tag{4}
\]
No monotonicity of \(A_t\) in the positive semidefinite order is used.

### 3. Moving-comparator calculation

Apply (1) with \(u=u_t\) and sum. Let
\[
S=\sum_{t=1}^T\left[\gamma\|w_t-u_t\|_{A_{t-1}}^2
-\|w_{t+1}-u_t\|_{A_t}^2\right].
\]
Shifting the second sum gives the exact expression
\[
\begin{aligned}
S={}&\gamma\|w_1-u_1\|_{A_0}^2-\|w_{T+1}-u_T\|_{A_T}^2\\
&+\sum_{t=2}^T\left[\gamma\|w_t-u_t\|_{A_{t-1}}^2
-\|w_t-u_{t-1}\|_{A_{t-1}}^2\right].
\end{aligned}
\]
The initial term is at most \(\delta R^2\), since \(w_1=0\). The terminal term is nonpositive, so it can be discarded without assuming any bound on \(w_{T+1}\).

For \(t\ge2\), set \(e_t=w_t-u_t\) and \(\Delta_t=u_t-u_{t-1}\). The bracket equals
\[
\begin{aligned}
\gamma\|e_t\|_{A_{t-1}}^2-\|e_t+\Delta_t\|_{A_{t-1}}^2
={}&-(1-\gamma)\|e_t\|_{A_{t-1}}^2
-2\Delta_t^\top A_{t-1}e_t-\|\Delta_t\|_{A_{t-1}}^2\\
\le{}&2|\Delta_t^\top A_{t-1}e_t|\\
\le{}&4R(\delta+B_z^2h)\|\Delta_t\|_2.
\end{aligned}
\]
The last inequality uses \(\|e_t\|_2\le2R\) and the matrix bound from Step 2. Therefore
\[
S\le\delta R^2+4R(\delta+B_z^2h)P_T(u_{1:T}).
\]
Together with (2) and (4), this proves
\[
L_T(a^{(h)})-L_T(u_{1:T})
\le\delta R^2+D^2d\log\left(1+\frac{B_z^2h}{\delta}\right)
+\frac{2D^2dT}{h}+4R(\delta+B_z^2h)P_T(u_{1:T})
=\Psi_h\bigl(T,P_T(u_{1:T})\bigr). \tag{5}
\]
For completeness, under the additional condition \(\delta\le B_z^2h\), the last term is at most \(8RB_z^2hP_T(u_{1:T})\). This optional simplification is not assumed or used in the target inequality.

### 4. Clipping comparison

For any real \(a\) and \(|y|\le B\), clipping does not increase squared loss. If \(a\in[-B,B]\), the losses agree. If \(a>B\), then \(y\le B<a\) and \(|B-y|\le|a-y|\); the case \(a<-B\) is symmetric. Hence
\[
(\operatorname{clip}_B(a)-y)^2\le(a-y)^2.
\]
Applying this at each round to \(a_t^{(h_k)}\) and then using (5) gives
\[
L_T(\widetilde y_{\cdot,M+k})
\le L_T(a^{(h_k)})
\le L_T(u_{1:T})+\Psi_{h_k}\bigl(T,P_T(u_{1:T})\bigr). \tag{6}
\]
Only the separate bound \(|y_t|\le B\) is used here; no ordering of \(B\) and \(B_y\) is required.

### 5. Aggregation bound from the stated update

The weights are nonnegative and sum to one, including when the uniform fallback is used. Thus \(\widehat y_t\), every \(\widetilde y_{t,j}\), and \(y_t\) lie in \([-B,B]\), and
\[
|r_{t,j}|\le2(2B)(2B)=8B^2.
\]
Define \(R_{t,j}=\sum_{s=1}^t r_{s,j}\), \(R_{0,j}=0\), and
\[
\Phi_t=\frac1{2N}\sum_{j=1}^N[R_{t,j}]_+^2.
\]
For real \(s,a\),
\[
[s+a]_+^2-[s]_+^2\le2[s]_+a+a^2. \tag{7}
\]
To verify (7), when \(s\ge0\), use \([s+a]_+^2\le(s+a)^2\). When \(s<0\), either \(s+a\le0\), making the left side zero, or \(0<s+a<a\), making it at most \(a^2\).

Applying (7) coordinatewise gives
\[
\Phi_t-\Phi_{t-1}
\le\frac1N\sum_j[R_{t-1,j}]_+r_{t,j}
+\frac1{2N}\sum_j r_{t,j}^2.
\]
Let \(Q_{t-1}=\sum_j[R_{t-1,j}]_+\). If \(Q_{t-1}=0\), the first sum vanishes. Otherwise it equals
\[
\begin{aligned}
\sum_j[R_{t-1,j}]_+r_{t,j}
&=Q_{t-1}\sum_j p_{t,j}r_{t,j}\\
&=2Q_{t-1}(\widehat y_t-y_t)
\left(\widehat y_t-\sum_jp_{t,j}\widetilde y_{t,j}\right)=0.
\end{aligned}
\]
It follows that
\[
\Phi_t-\Phi_{t-1}\le32B^4,\qquad
\Phi_T\le32B^4T,
\]
and therefore, for every expert \(j\),
\[
R_{T,j}\le[R_{T,j}]_+
\le\left(\sum_i[R_{T,i}]_+^2\right)^{1/2}
=\sqrt{2N\Phi_T}\le8B^2\sqrt{NT}. \tag{8}
\]
Finally, an exact squared-loss expansion gives
\[
(\widehat y_t-y_t)^2-(\widetilde y_{t,j}-y_t)^2
=r_{t,j}-(\widehat y_t-\widetilde y_{t,j})^2\le r_{t,j}.
\]
Summing and using (8) establishes the required bound for every expert:
\[
L_T(\widehat y)\le L_T(\widetilde y_{\cdot,j})+8B^2\sqrt{NT}. \tag{9}
\]
This derivation uses neither an unproved specialized regret theorem nor a stochastic assumption.

### 6. Combining the alternatives

Taking the minimum of (9) over the first \(M\) experts gives
\[
L_T(\widehat y)\le\min_{1\le j\le M}L_T(\widetilde y_{\cdot,j})+8B^2\sqrt{T(M+K)}.
\]
For each \(h_k\in H\), combining (9) with (6) gives
\[
L_T(\widehat y)\le L_T(u_{1:T})
+\Psi_{h_k}\bigl(T,P_T(u_{1:T})\bigr)+8B^2\sqrt{T(M+K)}.
\]
Minimize the latter inequalities over \(H\) and combine with the raw-expert inequality. This is exactly the requested conclusion, with the universal choice \(C=8\).

All calculations remain valid when \(T=1\), so the path-length sum is empty, and when \(P_T=0\), \(R=0\), or \(B=0\). No division by these quantities occurs. The endpoint \(h=2\) is included in the estimates above. The positive integer pool sizes make both displayed minima and the uniform fallback well-defined.
