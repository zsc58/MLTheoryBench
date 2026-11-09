# Reference Proof

## Proof Structure

For a partition of the source subset, expand the effective-information difference into entropies. The product-uniform intervention makes the source blocks independent, so the difference is conditional total correlation, equivalently an expected KL divergence. This proves nonnegativity, while nonnegativity of mutual information gives the upper bound. A one-block refinement then yields the additive identity by direct cancellation. Iterating such refinements to the singleton partition proves maximality.

## Complete Proof

Fix source and target subsets A and B, write Y=X_{t+1}^B, and let Z_i=X_t^{M_i} for the blocks M_i of P, with Z=(Z_1,...,Z_m). All entropies and mutual informations below are under the interventional law q.

By definition,
\[
\operatorname{Syn}_{P}(A\to B)=I(Z;Y)-\sum_{i=1}^m I(Z_i;Y).
\]
Expanding mutual information gives
\[
\operatorname{Syn}_{P}(A\to B)
=H(Z)-H(Z\mid Y)-\sum_i H(Z_i)+\sum_i H(Z_i\mid Y).
\]
The product-uniform maximum-entropy intervention factorizes over source components, hence also over the blocks of P, and therefore H(Z)=\sum_iH(Z_i). Consequently,
\[
\operatorname{Syn}_{P}(A\to B)=\sum_iH(Z_i\mid Y)-H(Z\mid Y).
\]
For every y with positive q(y), the expression in the last display is
\[
D_{\mathrm{KL}}\!\left(q(z\mid y)\,\middle\|\,\prod_i q(z_i\mid y)\right),
\]
averaged over y. Thus it is a conditional total correlation and is nonnegative by KL nonnegativity. Also, each block effective information is a mutual information and is nonnegative, so from the defining difference,
\[
\operatorname{Syn}_{P}(A\to B)\le I(Z;Y)=\operatorname{EI}(A\to B).
\]
This proves the two bounds.

Now let M_*\in P and let R={R_1,...,R_k} be a partition of M_*. Put P'=(P\setminus\{M_*\})\cup R. Expanding both definitions and adding and subtracting \operatorname{EI}(M_*\to B) gives
\[
\begin{aligned}
\operatorname{Syn}_{P'}(A\to B)
&=\operatorname{EI}(A\to B)-\sum_{M\in P\setminus\{M_*\}}\operatorname{EI}(M\to B)-\sum_{r=1}^k\operatorname{EI}(R_r\to B)\\
&=\operatorname{Syn}_{P}(A\to B)+\left[\operatorname{EI}(M_*\to B)-\sum_{r=1}^k\operatorname{EI}(R_r\to B)\right]\\
&=\operatorname{Syn}_{P}(A\to B)+\operatorname{Syn}_{R}(M_*\to B).
\end{aligned}
\]
Finally, repeatedly split nonsingleton blocks of any partition P until the singleton partition P_fin(A) is reached. At each split, the added term \operatorname{Syn}_{R}(M_*\to B) is nonnegative by the first part (applied to M_*). Hence synergy never decreases along the refinement sequence, and
\[
\operatorname{Syn}_{P}(A\to B)\le \operatorname{Syn}_{P_{\mathrm{fin}}(A)}(A\to B).
\]
