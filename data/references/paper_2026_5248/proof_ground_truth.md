# Reference Proof

## Proof obligations and parameter convention

All parameters other than the width \(N\) and confidence parameter \(\delta\) are fixed before constants are selected. In particular, constants may depend on the fixed positive \(\gamma\), the admissible \(\alpha\), and the finite horizon \(K\). No uniformity as \(\gamma\downarrow0\) or \(K\to\infty\) is claimed.

The proof closes the following obligations: the limiting spectral estimate; initialization probability and size; a noncircular finite-horizon construction ensuring unique Newton updates; neuron-wise motion; preconditioner and feature stability; unconditional initialization concentration followed by valid conditioning; segment-wise Taylor control; and the uniform trajectory estimate with the stated probability. All calculations involving trained iterates are performed on an event where their existence is established. Failure elsewhere is allowed by the public procedure.

## 1. Limiting kernel and deterministic recursion

Put \(\bar x^m=(x^m,1)\). For a single neuron \(\vartheta=(c,w,\eta)\), let \(s_\vartheta\in\mathbb R^{M\times(d+2)}\) have row
\[
(s_\vartheta)_{m,:}=\bigl(\sigma(w\cdot x^m+\eta),\ c\sigma'(w\cdot x^m+\eta)(\bar x^m)^\top\bigr).
\]
Then \(B=M^{-1}\mathbb E[s_{\theta_0^1}s_{\theta_0^1}^\top]\). In particular,
\[
v^\top Bv=\frac1M\int\Big(\sum_m v_m\sigma(w\cdot x^m+\eta)\Big)^2d\mu_0
+\frac1M\int c^2\Big\|\sum_m v_m\sigma'(w\cdot x^m+\eta)\bar x^m\Big\|_2^2d\mu_0\ge0.
\]
All integrals are finite because the features are bounded.

For completeness, the strict-positivity claim in the indexed source support can be established without relying on its specialized citation. If \(v^\top Bv=0\), continuity and the support assumption give
\[
\sum_m v_m\sigma(w\cdot x^m+\eta)=0\qquad\text{for every }w,\eta.
\]
For \(M=1\), this implies \(v_1=0\), since \(\sigma\) is not identically zero. For \(M\ge2\), convolve in \(\eta\) with a smooth compactly supported approximate identity. The resulting bounded smooth functions \(\sigma_\varepsilon\) satisfy the same identity and converge pointwise to \(\sigma\). Fix \(m\). For every \(j\ne m\), noncollinearity supplies \(u_j\) with \(u_j\cdot x^j=0\) and \(u_j\cdot x^m\ne0\): one may take the nonzero orthogonal projection of \(x^m\) onto \((x^j)^\perp\). Apply \(\prod_{j\ne m}(u_j\cdot\nabla_w)\) to the smoothed identity. Every term except the \(m\)-th vanishes, so
\[
v_m\prod_{j\ne m}(u_j\cdot x^m)\,\sigma_\varepsilon^{(M-1)}(w\cdot x^m+\eta)=0.
\]
If \(v_m\ne0\), each \(\sigma_\varepsilon\) is a polynomial of degree at most \(M-2\). Boundedness makes it constant. Passing to the limit shows that \(\sigma\) is constant, a contradiction. Thus \(v=0\), proving \(B\succ0\).

Diagonalizing \(B\), the eigenvalues of \(Q=B(\gamma I+B)^{-1}\) are \(q=\lambda/(\gamma+\lambda)\). Write \(q_{\min}\) and \(q_{\max}\) for their extremes. The step-size condition implies
\[
0<1-\alpha q_{\min}<1,\qquad
\|I-\alpha Q\|_{\rm op}\le1-\alpha q_{\min}.
\]
Indeed, \(1-\alpha q\le1-\alpha q_{\min}\), while \(1-\alpha q\ge1-\alpha q_{\max}>-(1-\alpha q_{\min})\).

Define privately \(f_0^*=0\) and \(f_{k+1}^*=f_k^*+\alpha Q(y-f_k^*)\). Therefore
\[
\|y-f_K^*\|_2\le(1-\alpha q_{\min})^K\|y\|_2. \tag{1}
\]
The non-strict spectral inequality would also follow from positive semidefiniteness alone; strict positivity is not an additional public assumption.

## 2. Initialization and explicit deterministic control constants

Choose \(b_0<\infty\) such that \(|c_0^i|\le b_0\) almost surely. Centering and independence eliminate cross-neuron terms, giving
\[
\mathbb E\|f_{\theta_0}^N(x)\|_2^2\le M b_0^2\|\sigma\|_\infty^2N^{-(2\beta-1)}.
\]
Choose a positive \(C_0\ge b_0^2\|\sigma\|_\infty^2\). The width hypothesis and Markov's inequality imply
\[
\mathbb P(\Omega_R)\ge1-\delta,\qquad
\Omega_R=\{\|y-f_{\theta_0}^N(x)\|_2\le\sqrt M R\}. \tag{2}
\]
For every nonnegative random variable \(X\),
\[
\mathbb E[X\mid\Omega_R]\le\frac{\mathbb EX}{\mathbb P(\Omega_R)}\le2\mathbb EX. \tag{3}
\]
In particular,
\[
\mathbb E[\|f_{\theta_0}^N(x)\|_2\mid\Omega_R]
\le2\sqrt{MC_0}\,N^{-(\beta-1/2)}. \tag{4}
\]

Here is a noncircular choice of the control constants. Let
\[
T=\sqrt{C_x^2+1},\quad S_j=\|\sigma^{(j)}\|_\infty\ (j=0,1,2),
\]
where \(\sigma^{(0)}=\sigma\), and let \(L_\sigma\) and \(L_{\sigma'}\) be finite Lipschitz constants. For \(a\ge0\), put
\[
a_s(a)=\sqrt{S_0^2+a^2S_1^2T^2},\quad
h(a)=2S_1T+aS_2T^2,\quad
g(a)=S_0+aL_\sigma T.
\]
The feature norm obeys \(\|s_\vartheta\|_{\rm op}\le\sqrt M a_s(a)\) whenever \(|c|\le a\). The unscaled single-neuron output Hessian is
\[
h_\vartheta(x^m)=
\begin{pmatrix}
0&\sigma'(w\cdot x^m+\eta)(\bar x^m)^\top\\
\sigma'(w\cdot x^m+\eta)\bar x^m&c\sigma''(w\cdot x^m+\eta)\bar x^m(\bar x^m)^\top
\end{pmatrix},
\]
and its operator norm is at most \(h(a)\). Also, splitting the change in \(c\sigma(w\cdot x^m+\eta)\) into a weight change and an activation change gives an increment bound \(g(a)\|\vartheta'-\vartheta\|_2\) when the old output weight has magnitude at most \(a\).

Set \(\rho_0=R\). Recursively, for \(0\le j<K\), define
\[
t_j=2a_s(b_j)\rho_j,\qquad
b_{j+1}=b_j+\frac{\alpha t_j}{\gamma},\qquad
\rho_{j+1}=\rho_j+\frac{\alpha g(b_j)t_j}{\gamma}.
\]
Also set \(t_K=2a_s(b_K)\rho_K\). These finite constants are chosen without using \(N\), \(\delta\), or any random trajectory. Choose
\[
C_\gamma=1+2\max_{0\le j\le K}h(b_j)\rho_j. \tag{5}
\]
This has the dependencies permitted by the source. Write \(\epsilon_N=N^{-(1-\beta)}\), so the regularization condition is \(\gamma\ge C_\gamma\epsilon_N\).

## 3. Newton solvability and neuron-wise induction

Let \(r=y-f_\theta^N(x)\), let \(J\) be the output Jacobian, and let \(H_\theta(x^m)\) be the output Hessian. Differentiation gives
\[
\nabla L^N=-M^{-1}J^\top r,\qquad
\nabla^2L^N=M^{-1}J^\top J+S,\qquad
S=-M^{-1}\sum_m r_mH_\theta(x^m).
\]
The Hessian \(H_\theta(x^m)\) is block diagonal with blocks \(N^{-\beta}h_{\theta^i}(x^m)\). Put \(D=\gamma^NI+S\). Its rescaled blocks are
\[
d_i=N^{2\beta-1}D_i
=\gamma I-\epsilon_N M^{-1}\sum_m r_mh_{\theta^i}(x^m). \tag{6}
\]
If \(\max_i|c^i|\le b_j\) and \(\|r\|_2\le\sqrt M\rho_j\), Cauchy-Schwarz gives
\[
\left\|M^{-1}\sum_m r_mh_{\theta^i}(x^m)\right\|_{\rm op}\le h(b_j)\rho_j.
\]
Thus (5) implies \(d_i\succeq(\gamma/2)I\), and hence
\[
D\succ0,\quad D+M^{-1}J^\top J\succ0,\quad
\|D_i^{-1}\|_{\rm op}\le2N^{2\beta-1}/\gamma. \tag{7}
\]
This uses the correct identity \(\lambda_{\min}(\gamma I-U)=\gamma-\lambda_{\max}(U)\) for symmetric \(U\).

Direct multiplication verifies the push-through identity and yields the unique direction
\[
z=M^{-1}D^{-1}J^\top\zeta,\qquad
\zeta=(I+M^{-1}JD^{-1}J^\top)^{-1}r. \tag{8}
\]
The matrix added to \(I\) is positive semidefinite, so \(\|\zeta\|_2\le\|r\|_2\). Since \(J_i=N^{-\beta}s_{\theta^i}\), equations (7)-(8) give
\[
\|z^i\|_2\le\frac{2a_s(b_j)\rho_j}{\gamma}\epsilon_N
=\frac{t_j}{\gamma}\epsilon_N. \tag{9}
\]
At initialization, the induction hypotheses hold on \(\Omega_R\). Since \(\epsilon_N\le1\), (9) gives the next weight bound \(b_{j+1}\). The per-sample output increment satisfies
\[
|f_{\theta_{j+1}}^N(x^m)-f_{\theta_j}^N(x^m)|
\le N^{-\beta}\sum_i\alpha g(b_j)\|z_j^i\|_2
\le\frac{\alpha g(b_j)t_j}{\gamma}.
\]
The triangle inequality therefore gives the next residual bound \(\sqrt M\rho_{j+1}\). This completes the induction, rather than assuming solvability to establish its own hypotheses.

Consequently all required updates succeed on \(\Omega_R\). With \(b=b_K\), \(\rho=\rho_K\), and \(t=\max_{j\le K}t_j\), on that event
\[
\max_{i,j\le K}|c_j^i|\le b,\qquad
\max_{j\le K}\|r_j\|_2\le\sqrt M\rho,\qquad
\max_{i,j\le K}\|z_j^i\|_2\le t\epsilon_N/\gamma,
\]
and
\[
\max_{i,j\le K}\|\theta_j^i-\theta_0^i\|_2\le\alpha Kt\epsilon_N/\gamma. \tag{10}
\]
The extra direction at time \(K\), if considered, is also uniquely defined on this event; it is not required by the public procedure.

## 4. Kernel comparison and conditioning

Define on \(\Omega_R\)
\[
\widehat B_j=\frac1{MN}\sum_i s_{\theta_j^i}s_{\theta_j^i}^\top,\quad
A_j=\frac1{MN}\sum_i s_{\theta_j^i}d_{j,i}^{-1}s_{\theta_j^i}^\top,\quad
\mathcal K_j=A_j(I+A_j)^{-1}.
\]
All \(A_j\) are positive semidefinite. The inverse identity and (6)-(7) imply
\[
\|d_{j,i}^{-1}-\gamma^{-1}I\|_{\rm op}
\le\frac{2h(b)\rho}{\gamma^2}\epsilon_N,
\]
so
\[
\|A_j-\gamma^{-1}\widehat B_j\|_{\rm op}
\le\frac{C_1}{\gamma^2}\epsilon_N. \tag{11}
\]
For output weights bounded by \(b\), the Lipschitz assumptions give
\[
\|s_\vartheta-s_{\widetilde\vartheta}\|_{\rm op}
\le\sqrt M\bigl(L_\sigma T+S_1T+bL_{\sigma'}T^2\bigr)
\|\vartheta-\widetilde\vartheta\|_2.
\]
Insert one mixed product into each difference of feature Gram matrices and use (10). This gives
\[
\|\gamma^{-1}(\widehat B_j-\widehat B_0)\|_{\rm op}
\le\frac{\alpha K C_2}{\gamma^2}\epsilon_N. \tag{12}
\]
The second factor \(\gamma^{-1}\) in (11)-(12) must not be dropped.

For the initialization term put \(Z_i=M^{-1}s_{\theta_0^i}s_{\theta_0^i}^\top-B\). These matrices are independent, centered, and symmetric before conditioning. Their operator norms are bounded by a fixed constant \(L\), since \(\|s_{\theta_0^i}\|_{\rm op}\le\sqrt M a_s(b_0)\) and \(\|B\|_{\rm op}\le\operatorname{tr}B\le a_s(b_0)^2\). Their variance proxy satisfies
\[
\left\|\sum_i\mathbb E Z_i^2\right\|_{\rm op}\le NL^2.
\]
The standard two-sided matrix Bernstein expectation bound says that independent centered self-adjoint matrices bounded by \(L\), with variance proxy \(v\), satisfy
\[
\mathbb E\left\|\sum_i Z_i\right\|_{\rm op}
\le C\bigl(\sqrt{v\log(2M)}+L\log(2M)\bigr),
\]
where \(C\) is numerical. The verified hypotheses therefore give
\[
\mathbb E\|\widehat B_0-B\|_{\rm op}\le C_3\frac{\log(2M)}{\sqrt N}.
\]
Apply (3), not a conditional-independence assertion, to obtain the same bound up to a factor two conditionally on \(\Omega_R\).

Adding (11), (12), and the initialization contribution yields, uniformly for \(0\le j\le K\),
\[
\mathbb E[\|A_j-\gamma^{-1}B\|_{\rm op}\mid\Omega_R]
\le\frac{C_1+\alpha K C_2}{\gamma^2}\epsilon_N
+\frac{C_3}{\gamma}\frac{\log(2M)}{\sqrt N}. \tag{13}
\]
In particular, this does not vanish merely because \(K=0\).

For positive semidefinite \(U,V\), the identity \(U(I+U)^{-1}=I-(I+U)^{-1}\) and the resolvent identity give
\[
\|U(I+U)^{-1}-V(I+V)^{-1}\|_{\rm op}\le\|U-V\|_{\rm op},
\]
since both resolvents have norm at most one. Apply this with \(U=A_j\) and \(V=\gamma^{-1}B\). For \(M\ge2\), \(\log(2M)\le2\log M\); for \(M=1\), \(N^{-1/2}\le\epsilon_N\). Thus, with fixed-parameter constants,
\[
\mathbb E[\|\mathcal K_j-Q\|_{\rm op}\mid\Omega_R]
\le C\left(\epsilon_N+\frac{\log M}{\sqrt N}\right). \tag{14}
\]

## 5. Taylor remainder and trajectory comparison

Every segment between consecutive iterates on \(\Omega_R\) has output weights bounded by \(b\). The block-diagonal output Hessian consequently satisfies
\[
\|H_\theta(x^m)\|_{\rm op}
=N^{-\beta}\max_i\|h_{\theta^i}(x^m)\|_{\rm op}
\le N^{-\beta}h(b)
\]
throughout each segment. This is a bound by the largest absolute eigenvalue, not by the absolute value of the largest signed eigenvalue. Taylor's theorem and (9) give
\[
\|R_j\|_2\le\frac{\alpha^2}{2}\sqrt M N^{-\beta}h(b)\sum_i\|z_j^i\|_2^2
\le\frac{\alpha^2h(b)t^2}{2\gamma^2}\sqrt M\epsilon_N. \tag{15}
\]
Using (8), the Jacobian term equals \(J_jz_j=\mathcal K_jr_j\). Hence
\[
f_{\theta_{j+1}}^N(x)=f_{\theta_j}^N(x)+\alpha\mathcal K_jr_j+R_j.
\]
For \(e_j=f_{\theta_j}^N(x)-f_j^*\), subtraction gives the exact comparison
\[
e_{j+1}=(I-\alpha Q)e_j+\alpha(\mathcal K_j-Q)r_j+R_j.
\]
Since \(\|I-\alpha Q\|_{\rm op}\le1\), on \(\Omega_R\)
\[
\max_{0\le j\le K}\|e_j\|_2
\le\|f_{\theta_0}^N(x)\|_2
+\alpha\sqrt M\rho\sum_{j=0}^{K-1}\|\mathcal K_j-Q\|_{\rm op}
+\sum_{j=0}^{K-1}\|R_j\|_2.
\]
When \(K=0\), both sums are empty and this remains valid. Taking conditional expectations and using (4), (14), and (15), we obtain
\[
\mathbb E\left[\max_{0\le j\le K}\|e_j\|_2\mid\Omega_R\right]
\le C\sqrt M\left(N^{-(\beta-1/2)}+N^{-(1-\beta)}+\frac{\log M}{\sqrt N}\right). \tag{16}
\]
Conditional Markov bounds the probability, within \(\Omega_R\), of exceeding the right-hand side divided by \(\delta\) by \(\delta\). Adding \(\mathbb P(\Omega_R^c)\le\delta\) shows that with probability at least \(1-2\delta\), the procedure succeeds through \(K\) and
\[
\|f_{\theta_K}^N(x)-f_K^*\|_2
\le\frac{C\sqrt M}{\delta}\left(N^{-(\beta-1/2)}+N^{-(1-\beta)}+\frac{\log M}{\sqrt N}\right).
\]
Finally combine this estimate with (1) by the triangle inequality. This proves precisely the public target, including \(K=0\), \(M=1\), zero labels, and a degenerate centered output-weight initialization. No moment assumption on \(w\) or \(\eta\) is needed because all feature and Hessian estimates use bounded activation derivatives.
