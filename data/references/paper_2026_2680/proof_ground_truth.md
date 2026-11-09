# Reference Proof

## Proof Structure

1. Unroll the online recursion and express the resulting predictor through the inverse of a finite upper-triangular operator.
2. Compare this directional operator with the symmetric Gram matrix to identify effective targets for which offline kernel ridge regression reproduces the online predictor.
3. Apply the inverse target transformation and substitute it into the online closed form to obtain exact equality with offline regression on the original targets.

## Complete Proof

Let \(\phi_i=\phi(x_i)\), \(k_{ij}=\phi_i^\top\phi_j\), \(K=(k_{ij})_{i,j=1}^n\), and let \(K^U\) retain \(k_{ij}\) for \(i<j\) and be zero otherwise. Set
\[
A=\eta^{-1}I_n+K^U,\qquad B=\gamma I_n+K.
\]
Since \(K^U\) is strictly upper triangular, \((K^U)^n=0\), so
\[
A^{-1}=\eta\sum_{r=0}^{n-1}(-\eta K^U)^r,
\]
and \(A\) is invertible. Because \(K\) is positive semidefinite and \(\gamma>0\), \(B\) is positive definite and invertible.

We prove the online formula by induction on the number of updates. For the first \(t\) samples let \(A_t=\eta^{-1}I_t+K_t^U\). The claim is \(W_{t+1}\phi(x)=Y_tA_t^{-1}k(X_t,x)\), with the empty case equal to zero. For the induction step, write \(u=(k(x_1,x_{t+1}),\ldots,k(x_t,x_{t+1}))^\top\). Then
\[
A_{t+1}=\begin{pmatrix}A_t&u\\0&\eta^{-1}\end{pmatrix},\quad
A_{t+1}^{-1}=\begin{pmatrix}A_t^{-1}&-\eta A_t^{-1}u\\0&\eta\end{pmatrix}.
\]
The online update gives
\[
f_{t+1}(x)=f_t(x)-\eta\bigl(f_t(x_{t+1})-y_{t+1}\bigr)k(x_{t+1},x),
\]
and the induction hypothesis has \(f_t(x_{t+1})=Y_tA_t^{-1}u\). Substitution therefore yields exactly \(Y_{t+1}A_{t+1}^{-1}k(X_{t+1},x)\). At \(t=n\), this is \(f_{\rm on}(x;X_n,Y)=YA^{-1}k(X_n,x)\).

Define \(Y^e=YA^{-1}B\). Using the offline kernel-ridge formula,
\[
f_{\rm off}(x;X_n,Y^e)=Y^eB^{-1}k(X_n,x)=YA^{-1}BB^{-1}k(X_n,x)=YA^{-1}k(X_n,x)=f_{\rm on}(x;X_n,Y).
\]

Finally define \(Y^c=YB^{-1}A\). Running the online recursion on these targets and using the already proved closed form gives
\[
f_{\rm on}(x;X_n,Y^c)=Y^cA^{-1}k(X_n,x)=YB^{-1}AA^{-1}k(X_n,x)=YB^{-1}k(X_n,x)=f_{\rm off}(x;X_n,Y).
\]
This proves all asserted equalities.
