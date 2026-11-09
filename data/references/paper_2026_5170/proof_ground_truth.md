# Reference Proof

## Proof Structure

Bound the graph operators, derive an O(epsilon) bound for each polynomial filter by a proved matrix-power telescoping identity, propagate this perturbation through the nonlinear network using uniform forward bounds and a layerwise error recursion, and finally factor the Gram-matrix difference through the embedding error. Choose strictly positive final constants even when an intermediate perturbation coefficient vanishes.

## Complete Proof

All constants below depend only on the fixed dimensions, architecture, polynomial coefficients, activation Lipschitz constants and offsets, and the bounds $B_X,B_W,B_L$, not on $\varepsilon$ or the particular admissible graph pair, input, or weights within those bounds.

If depth zero is allowed, then $K=0$ gives $Z=\widetilde Z=X$, and both claims hold with $C_2=C_F=1$. Likewise, if the public operator bound is zero, then $L=\widetilde L=0$; the two networks agree at every layer, and the same choice works. Hence it remains to consider $K\geq1$ and $B_L>0$. The remaining argument does not require positive input norms, nonzero weights, positive activation Lipschitz constants, or nonconstant filters.

### Graph-operator perturbation

Write $A_k=p_k(L)$ and $\widetilde A_k=p_k(\widetilde L)$. The spectral inequalities imply
\[
\|L-\widetilde L\|_2\leq\varepsilon B_L.
\]
Indeed, for every unit vector $u$,
\[
-\varepsilon u^\top Lu\leq u^\top(\widetilde L-L)u\leq\varepsilon u^\top Lu,
\]
so $|u^\top(\widetilde L-L)u|\leq\varepsilon B_L$. For a real symmetric matrix, orthogonal diagonalization shows that both its operator norm and the supremum of its absolute unit-vector quadratic forms equal the largest absolute eigenvalue. Applying this fact to the symmetric matrix $\widetilde L-L$ proves the bound.

### Power identity and polynomial bounds

For square matrices $A,B$ of the same size and every integer $r\geq1$,
\[
A^r-B^r=\sum_{j=0}^{r-1}A^{r-1-j}(A-B)B^j.
\]
To prove this without assuming commutativity, the case $r=1$ is immediate. If the formula holds for $r$, then
\[
A^{r+1}-B^{r+1}=A(A^r-B^r)+(A-B)B^r.
\]
Substitution of the induction hypothesis gives the terms indexed by $j=0,\ldots,r-1$, and the last summand supplies the term $j=r$. This proves the identity by induction.

Consequently, submultiplicativity of the operator norm gives
\[
\begin{aligned}
\|L^r-\widetilde L^r\|_2
&\leq\sum_{j=0}^{r-1}\|L\|_2^{r-1-j}\|L-\widetilde L\|_2\|\widetilde L\|_2^j\\
&\leq rB_L^{r-1}\|L-\widetilde L\|_2
\leq rB_L^r\varepsilon.
\end{aligned}
\]
The constant polynomial terms cancel. Therefore
\[
\|A_k-\widetilde A_k\|_2\leq C_k\varepsilon,
\qquad C_k:=\sum_{r=1}^{d_k^p}|a_{k,r}|rB_L^r.
\]
An empty sum is zero, so this includes constant filters. Also define
\[
Q_k:=\sum_{r=0}^{d_k^p}|a_{k,r}|B_L^r.
\]
Since the zeroth matrix power is the identity, the triangle inequality and submultiplicativity give
\[
\|A_k\|_2,\ \|\widetilde A_k\|_2\leq Q_k.
\]
All these coefficients are finite and independent of $\varepsilon$.

### Uniform forward bounds

The elementary mixed-norm inequality
\[
\|PHW\|_F\leq\|P\|_2\|H\|_F\|W\|_2
\]
follows by applying the defining operator-norm inequality to each column for left multiplication and then using transposition for right multiplication.

For matrices $U,V$ of size $n\times d_{k+1}$, entrywise Lipschitz continuity gives
\[
\|\sigma_k(U)-\sigma_k(V)\|_F^2
\leq L_{\sigma_k}^2\sum_{i,j}|U_{ij}-V_{ij}|^2
=L_{\sigma_k}^2\|U-V\|_F^2.
\]
In particular, with
\[
c_k:=|\sigma_k(0)|\sqrt{n d_{k+1}},
\]
the triangle inequality yields
\[
\|\sigma_k(U)\|_F\leq L_{\sigma_k}\|U\|_F+c_k.
\]
Thus no assumption $\sigma_k(0)=0$ is needed.

Set $R_0=B_X$ and recursively define
\[
R_{k+1}=L_{\sigma_k}Q_kB_WR_k+c_k.
\]
Starting from the common input, the network definitions and the preceding inequalities show by induction that
\[
\|H^{(k)}\|_F,\ \|\widetilde H^{(k)}\|_F\leq R_k
\qquad(0\leq k\leq K).
\]
These bounds are finite and uniform in $\varepsilon$. Their dependence on $n$, the widths, and the activation offsets is explicit.

### Nonlinear perturbation propagation

Let $E_k:=\|H^{(k)}-\widetilde H^{(k)}\|_F$. The shared input gives $E_0=0$. The exact decomposition
\[
A_kH^{(k)}W_k-\widetilde A_k\widetilde H^{(k)}W_k
=(A_k-\widetilde A_k)H^{(k)}W_k
+\widetilde A_k(H^{(k)}-\widetilde H^{(k)})W_k
\]
and the entrywise Lipschitz and mixed-norm inequalities imply
\[
E_{k+1}\leq L_{\sigma_k}B_W\bigl(C_k\varepsilon R_k+Q_kE_k\bigr)
=\alpha_k\varepsilon+\beta_kE_k,
\]
where
\[
\alpha_k=L_{\sigma_k}B_WC_kR_k,
\qquad
\beta_k=L_{\sigma_k}B_WQ_k.
\]
All coefficients are nonnegative. Induction on $m$ now gives
\[
E_m\leq\varepsilon\sum_{i=0}^{m-1}\alpha_i\prod_{j=i+1}^{m-1}\beta_j.
\]
The formula starts with the empty sum at $m=0$. For the induction step, multiplying the preceding sum by $\beta_m$ and adding $\alpha_m\varepsilon$ produces exactly the formula for $m+1$.

Consequently,
\[
\|Z-\widetilde Z\|_F=E_K\leq C_{\rm rep}\varepsilon,
\qquad
C_{\rm rep}:=\sum_{i=0}^{K-1}\alpha_i\prod_{j=i+1}^{K-1}\beta_j.
\]
Empty products equal one. This nonnegative coefficient may be zero; no division by it or by any $\beta_k$ has been used. If a strictly positive representation-bound constant is desired, it can be replaced by $1+C_{\rm rep}$.

### Both Gram-matrix bounds

Put $\Delta=Z-\widetilde Z$. Direct expansion gives
\[
ZZ^\top-\widetilde Z\widetilde Z^\top
=Z\Delta^\top+\Delta\widetilde Z^\top.
\]
For real matrices $P,Q$ with the same number of columns, applying Cauchy–Schwarz to their row inner products and summing gives
\[
\|PQ^\top\|_F^2\leq\|P\|_F^2\|Q\|_F^2.
\]
Also $\|M\|_2\leq\|M\|_F$, as follows by applying Cauchy–Schwarz to each row of $Mx$ for a unit vector $x$. Thus, for each $s\in\{2,F\}$,
\[
\begin{aligned}
\|ZZ^\top-\widetilde Z\widetilde Z^\top\|_s
&\leq(\|Z\|_F+\|\widetilde Z\|_F)\|\Delta\|_F\\
&\leq2R_KC_{\rm rep}\varepsilon.
\end{aligned}
\]
Choose
\[
C_2=C_F=1+2R_KC_{\rm rep}>0.
\]
These constants are independent of $\varepsilon$, including when the sharper nonnegative coefficient vanishes. Both required inequalities follow. They express absolute $O(\varepsilon)$ preservation of the final embedding Gram matrix in the two requested norms, without imposing a nonzero-Gram or relative-error normalization.
