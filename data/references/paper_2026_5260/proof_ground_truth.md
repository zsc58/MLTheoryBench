# Reference Proof

## Proof Structure

Identify the expected differentiated estimator with the population gradient, compare the two population gradients through RKHS mean embeddings, bound the embedding and embedding-derivative errors using the shared-noise couplings, and control the centered estimator by U-statistic variance bounds.

## Complete Proof

Fix \(x\), and write \(A=\mathbb E\Phi(g(x,\eta))\), \(B=\mathbb E\Phi(f(x,\eta))\), and \(C=\mathbb E\Phi(T)\), where \(T\sim G\). Thus
\[
 L(x)=\|A-C\|_{\mathcal H}^2,\qquad L_f(x)=\|B-C\|_{\mathcal H}^2.
\]
The stated interchange hypothesis applies to the U-statistic terms and gives
\[
 \mathbb E\nabla_x\widehat L_f(x)=\nabla_x L_f(x).
\]
It also permits differentiation of the displayed mean embeddings below.

Put \(u=B-A\) and \(v=A-C\). Then \(B-C=u+v\), and
\[
 \nabla L_f-\nabla L
 =2(Du)^*(B-C)+2(DA)^*u. \tag{1}
\]
Here \(D\) denotes differentiation with respect to \(x\), with Hilbert--Schmidt norms used for derivatives from the finite-dimensional input space to \(\mathcal H\).

The output coupling and Lipschitz property of \(\Phi\) give
\[
 \|u\|_{\mathcal H}
 \le \mathbb E\|\Phi(f)-\Phi(g)\|_{\mathcal H}
 \le L\,\epsilon_o. \tag{2}
\]
Since \(k(y,y)\le K\), every kernel mean embedding has norm at most \(\sqrt K\). Hence
\[
 \|B-C\|_{\mathcal H}\le2\sqrt K. \tag{3}
\]
Differentiating the embeddings and adding and subtracting \(D\Phi(f)J_g\) yields
\[
 DB-DA
 =\mathbb E\!\left[D\Phi(f)(J_f-J_g)
 +(D\Phi(f)-D\Phi(g))J_g\right].
\]
The explicit assumption \(\|D\Phi(y)\|_{\rm op}\le L\), together with Cauchy--Schwarz, the Jacobian coupling, the output coupling, and the Lipschitz property of \(D\Phi\), implies
\[
 \|DB-DA\|_{\rm HS}
 \le L\epsilon_J+H C_f\epsilon_o. \tag{4}
\]
Similarly,
\[
 \|DA\|_{\rm HS}
 \le \mathbb E\|D\Phi(g)J_g\|_{\rm HS}
 \le L C_f. \tag{5}
\]
Combining (1)--(5) gives the sharper intermediate estimate
\[
 \|\nabla L_f-\nabla L\|
 \le4\sqrt K\,L\epsilon_J+
 (2L^2C_f+4H C_f\sqrt K)\epsilon_o.
\]
In particular it implies the requested stated form
\[
 \|\mathbb E\nabla_x\widehat L_f(x)-\nabla_xL(x)\|
 \le C_J\epsilon_J+C_o\epsilon_o,
\]
with \(C_J=8L\sqrt K\) and \(C_o=2L^2C_f+8HC_f\sqrt K\).

It remains to prove the variance claim. The target-target U-statistic term is independent of \(x\). For the conditional-conditional differentiated kernel, differentiating the RKHS inner product shows that its norm is bounded by
\[
 L\sqrt K\bigl(\|J_f(x,\eta)\|_F+\|J_f(x,\eta')\|_F\bigr).
\]
For the conditional-target differentiated kernel, the corresponding bound is \(L\sqrt K\|J_f(x,\eta)\|_F\). The repaired student-Jacobian moment assumption consequently gives finite second moments for both differentiated kernels, bounded by universal multiples of \(L^2KC_f^2\).

The conditional-conditional term is an order-two one-sample U-statistic, and the conditional-target term is a two-sample U-statistic. The finite-second-moment Hoeffding variance bounds therefore give a universal constant \(c\) such that
\[
 \mathbb E\|\nabla_x\widehat L_f(x)-\mathbb E\nabla_x\widehat L_f(x)\|^2
 \le cL^2KC_f^2\left(\frac1N+\frac1M\right).
\]
Taking \(C_V=cL^2KC_f^2\) proves the result.
