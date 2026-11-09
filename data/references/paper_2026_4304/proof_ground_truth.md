# Reference Proof

## Proof Structure

For a fixed retrieved region, establish split-conformal validity by conditional exchangeability. Then compare the score distribution in a central cell with the mixture distribution in its retrieved region and transfer the resulting bound through conditioning on the calibration data.

## Complete Proof

Condition throughout on the training objects. Thus the prototypes, the score function, and all sets \(A_k\) are fixed, while the calibration observations and the test observation are i.i.d.

Fix \(k\) with \(\pi_{A_k}>0\), and write \(A=A_k\). Consider the fixed binary grouping \(G(x)={\bf1}\{b(x)\in A\}\). Conditional on the calibration group memberships, the event \(G(X_{n+1})=1\), and the number \(m=|I_A|\), the \(m\) calibration scores in \(I_A\) and the test score are exchangeable. To handle ties, augment each score by an independent continuous tie-breaking variable and order the augmented scores lexicographically. The rank of the test augmented score among the \(m+1\) augmented scores is uniform.

If \(\ell_m\le m\), the event that this rank is at most \(\ell_m\) implies
\[
s(X_{n+1},Y_{n+1})\le q_k.
\]
Its conditional probability is \(\ell_m/(m+1)\ge 1-\alpha\). If \(\ell_m>m\), then \(q_k=+\infty\), so the same conclusion is immediate. Averaging over the conditioning gives
\[
\mathbb P\{s(X_{n+1},Y_{n+1})\le q_k\mid b(X_{n+1})\in A_k\}\ge1-\alpha. \tag{1}
\]

Now let \(k\in K_+\). Since \(k\in A_k\), \(\pi_{A_k}>0\). For every finite \(t\), the mixture identity gives
\[
F_{A_k}(t)=\sum_{j\in A_k\cap K_+}\frac{\pi_j}{\pi_{A_k}}F_j(t).
\]
Consequently,
\[
\begin{aligned}
|F_k(t)-F_{A_k}(t)|
&=\left|\sum_{j\in A_k\cap K_+}\frac{\pi_j}{\pi_{A_k}}\bigl(F_k(t)-F_j(t)\bigr)\right|\\
&\le\sum_{j\in A_k\cap K_+}\frac{\pi_j}{\pi_{A_k}}D(k,j)
=\varepsilon_k.
\end{aligned} \tag{2}
\]
The same inequality holds at \(+\infty\), since both distribution functions equal one there.

The random variable \(q_k\) is measurable with respect to the calibration data and is independent of the test observation. Conditioning on the calibration data and then integrating the test observation yields
\[
\mathbb P\{s(X_{n+1},Y_{n+1})\le q_k\mid b(X_{n+1})=k\}
=\mathbb E[F_k(q_k)]
\]
and
\[
\mathbb P\{s(X_{n+1},Y_{n+1})\le q_k\mid b(X_{n+1})\in A_k\}
=\mathbb E[F_{A_k}(q_k)].
\]
By the pointwise bound (2), the first display is at least the second minus \(\varepsilon_k\). Combining this with (1) gives
\[
\mathbb P\{s(X_{n+1},Y_{n+1})\le q_k\mid b(X_{n+1})=k\}
\ge1-\alpha-\varepsilon_k. \tag{3}
\]

On the event \(b(X_{n+1})=k\), the deployed threshold \(\widehat q\) equals \(q_k\). By the definition of \(C_\alpha\), the score event in (3) is exactly \(\{Y_{n+1}\in C_\alpha(X_{n+1};\widehat q)\}\). This proves the second claim and completes the proof.
