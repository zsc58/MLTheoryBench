# Reference Proof

## Proof Structure

The key point is that every activated set is ancestral: if it contains an internal vertex, it contains the entire path from the root to that vertex. Tree factorization therefore makes the restricted variational law agree with the full law on every variable needed by an activated local cost. The internal-edge and leaf-parent terms can then be corrected separately by their inclusion probabilities and summed.

## Complete Proof

Fix a realization \(B\) and write \(A=A(B)\). We first establish the required marginal consistency.

Let \(s\in A\), and let
\[
0=v_0,v_1,\ldots,v_k=s
\]
be the unique path from the root to \(s\), omitting \(v_0\) from the list of latent vertices. Since \(A\) is a union of root-to-leaf paths, \(v_1,\ldots,v_k\in A\). Under both \(Q^\theta\) and \(Q_A^\theta\), the joint law along this path is
\[
\delta_{x_0}(dx_{v_0})\prod_{i=1}^k
 Q_{v_i}^\theta(dx_{v_i}\mid x_{v_{i-1}}).
\]
Indeed, in the full product law, all kernels on branches outside this path integrate to one, successively from descendants toward the root. Thus the marginal distribution of \((X_{\operatorname{pa}(s)},X_s)\) under \(Q_A^\theta\) equals its marginal under \(Q^\theta\). Consequently,
\[
\mathbb E_{Q_A^\theta}[C_s^\theta]
 =\mathbb E_{Q^\theta}[C_s^\theta]
 \qquad(s\in A). \tag{1}
\]

Now fix a leaf \(\ell\) such that \(\operatorname{pa}(\ell)\in A_0\). If its parent is the root, that parent state is the same fixed value under both laws. Otherwise, the preceding path argument applied to \(s=\operatorname{pa}(\ell)\) shows that the parent has the same marginal distribution under \(Q_A^\theta\) and \(Q^\theta\). Because \(C_\ell\) depends only on this parent state and the fixed observation \(y_\ell\),
\[
\mathbb E_{Q_A^\theta}[C_\ell]
 =\mathbb E_{Q^\theta}[C_\ell]
 \qquad(\operatorname{pa}(\ell)\in A_0). \tag{2}
\]

For an internal vertex \(s\), use (1) on the event \(\{s\in A(B)\}\). Since \(\pi_s=\mathbb P_\Gamma\{s\in A(B)\}>0\),
\[
\begin{aligned}
\mathbb E_{B\sim\Gamma}\mathbb E_{Q_{A(B)}^\theta}
 \left[\frac{\mathbf 1_{\{s\in A(B)\}}}{\pi_s}C_s^\theta\right]
&=\frac{1}{\pi_s}\mathbb E_{B\sim\Gamma}
 \left[\mathbf 1_{\{s\in A(B)\}}
 \mathbb E_{Q^\theta}[C_s^\theta]\right]\\
&=\mathbb E_{Q^\theta}[C_s^\theta].
\end{aligned} \tag{3}
\]
Summing (3) over the finite set \(S\) gives the internal contribution
\[
\mathbb E_{B\sim\Gamma}\mathbb E_{Q_{A(B)}^\theta}
 \left[\sum_{s\in A(B)}\frac{C_s^\theta}{\pi_s}\right]
=\sum_{s\in S}\mathbb E_{Q^\theta}[C_s^\theta]. \tag{4}
\]

Similarly, for each leaf \(\ell\), equation (2) and
\(\rho_\ell=\mathbb P_\Gamma\{\operatorname{pa}(\ell)\in A_0(B)\}>0\) imply
\[
\begin{aligned}
\mathbb E_{B\sim\Gamma}\mathbb E_{Q_{A(B)}^\theta}
 \left[
 \frac{\mathbf 1_{\{\operatorname{pa}(\ell)\in A_0(B)\}}}{\rho_\ell}C_\ell
 \right]
&=\frac{1}{\rho_\ell}\mathbb E_{B\sim\Gamma}
 \left[\mathbf 1_{\{\operatorname{pa}(\ell)\in A_0(B)\}}
 \mathbb E_{Q^\theta}[C_\ell]\right]\\
&=\mathbb E_{Q^\theta}[C_\ell].
\end{aligned} \tag{5}
\]
Summing over \(L\) yields
\[
\mathbb E_{B\sim\Gamma}\mathbb E_{Q_{A(B)}^\theta}
 \left[
 \sum_{\ell:\operatorname{pa}(\ell)\in A_0(B)}
 \frac{C_\ell}{\rho_\ell}
 \right]
=\sum_{\ell\in L}\mathbb E_{Q^\theta}[C_\ell]. \tag{6}
\]

Adding (4) and (6), and using the definitions of \(\widehat J_B(\theta)\) and \(J(\theta)\), proves
\[
\mathbb E_{B\sim\Gamma}
 \left[\mathbb E_{Q_{A(B)}^\theta}[\widehat J_B(\theta)]\right]
=J(\theta).
\]
