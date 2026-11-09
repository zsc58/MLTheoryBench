# Reference Proof

## Proof Structure

Expand the scalar scaling map to first order, express the lifted squared distance through the resulting rank-one metric, symmetrize the expansions at the two endpoints, control the square-root remainder using positive-definiteness, and transfer the distance asymptotic through the radial profile. The noise term is retained exactly.

## Complete Proof

Fix an interior point x and write h=x'-x. Since s is C1,
\[
s(x+h)=s(x)+\nabla s(x)^T h+o(\|h\|_2).
\]
Therefore
\[
(s(x)-s(x'))^2=(\nabla s(x)^T h)^2+o(\|h\|_2^2),
\]
and, with \(G(x)=I_d+\nabla s(x)\nabla s(x)^T\),
\[
\|\Phi(x)-\Phi(x')\|_2^2=h^T G(x)h+o(\|h\|_2^2).
\]
Applying the same argument with the roles of x and x' exchanged gives
\[
\|\Phi(x)-\Phi(x')\|_2^2=h^T G(x')h+o(\|h\|_2^2).
\]
Averaging these two identities yields
\[
\|\Phi(x)-\Phi(x')\|_2^2
=h^T\bar G(x,x')h+o(\|h\|_2^2),
\]
where
\[
\bar G(x,x')=I_d+\tfrac12\bigl(\nabla s(x)\nabla s(x)^T+\nabla s(x')\nabla s(x')^T\bigr).
\]
The matrix \(\bar G\) is symmetric and satisfies \(v^T\bar Gv\ge \|v\|_2^2\). By continuity of \(\nabla s\), it is also locally bounded above. Let \(Q=h^T\bar G h\). Then \(Q\asymp\|h\|_2^2\), and if the squared-distance remainder is \(r=o(\|h\|_2^2)\),
\[
\sqrt{Q+r}-\sqrt Q=\frac{r}{\sqrt{Q+r}+\sqrt Q}=o(\|h\|_2).
\]
Hence
\[
\|\Phi(x)-\Phi(x')\|_2=\sqrt{h^T\bar G(x,x')h}+o(\|h\|_2).
\]
Both arguments of \(\rho(\cdot/\ell)\) in the two expressions below tend to zero as \(x'\to x\). Continuity of \(\rho\) at zero therefore gives
\[
\rho\!\left(\frac{\|\Phi(x)-\Phi(x')\|_2}{\ell}\right)
=\rho\!\left(\frac{\sqrt{h^T\bar G(x,x')h}}{\ell}\right)+o(1).
\]
Multiplying by \(\sigma_f^2\) and adding the exact nugget term \(\sigma_n^2\delta_{xx'}\) proves the claimed covariance expansion.
