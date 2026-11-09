# Reference Proof

## Proof Structure

Expand each index as a normalized sum of ordinal-agreement indicators. Partition the ordered comparisons according to whether all indices lie in the unchanged set U. The wholly-U contribution is exactly the restricted similarity multiplied by the corresponding falling-factorial ratio; every remaining indicator lies in [0,1]. This gives a common interval for the original and transformed similarities, from which both robustness inequalities follow. Finally, count tuples meeting V to justify the vanishing-fraction conclusion explicitly.

## Complete Proof

Let \(m=|U|\). The real-valued comparison functions make all ordinal predicates well-defined, and \(N\ge m\ge4\) makes all full and restricted denominators positive.

For \(r=3\), write
\[
S_3(X,Y)=\frac{1}{(N)_3}\sum_{(i,j,k)\in[N]^3_{\ne}} I^{(3)}_{ijk},
\]
where
\[
I^{(3)}_{ijk}=\mathbf 1\{O^\Delta_{d_X}(x_i,x_j,x_k)=O^\Delta_{d_Y}(y_i,y_j,y_k)\}.
\]
For \(r=4\), write
\[
S_4(X,Y)=\frac{1}{(N)_4}\sum_{(i,j,k,l)\in[N]^4_{\ne}} I^{(4)}_{ijkl},
\]
where
\[
I^{(4)}_{ijkl}=\mathbf 1\{O_{d_X}(x_i,x_j,x_k,x_l)=O_{d_Y}(y_i,y_j,y_k,y_l)\}.
\]
Thus \(S_3=\operatorname{TSI}\) and \(S_4=\operatorname{QSI}\).

Fix \(r\in\{3,4\}\). Partition the \((N)_r\) ordered distinct index tuples into those entirely contained in U and those meeting \(V=[N]\setminus U\). Exactly \((m)_r\) tuples are entirely contained in U. Since \(X'\) agrees with X on U, their contribution to \(S_r(X',Y)\) is exactly
\[
\frac{(m)_r}{(N)_r}S_r(X_U,Y_U)=c_rS_r(X_U,Y_U).
\]
Every remaining indicator is in \([0,1]\). Hence
\[
c_rS_r(X_U,Y_U)\le S_r(X',Y)\le c_rS_r(X_U,Y_U)+(1-c_r). \tag{1}
\]
The identical reasoning applies to \(S_r(X,Y)\), since X also agrees with X' on U. Therefore both \(S_r(X,Y)\) and \(S_r(X',Y)\) lie in the interval on the right-hand side of (1), whose length is \(1-c_r\). Consequently,
\[
|S_r(X,Y)-S_r(X',Y)|\le 1-c_r.
\]

For the outlier bound, subtract \(S_r(X_U,Y_U)\) from (1). Since every similarity is an average of indicators, \(0\le S_r(X_U,Y_U)\le1\). Thus
\[
-(1-c_r)S_r(X_U,Y_U)
\le S_r(X',Y)-S_r(X_U,Y_U)
\le (1-c_r)(1-S_r(X_U,Y_U)),
\]
and both endpoints are respectively at least \(-(1-c_r)\) and at most \(1-c_r\). Hence
\[
|S_r(X_U,Y_U)-S_r(X',Y)|\le1-c_r.
\]
This proves both conclusions for \(r=3\) and \(r=4\).

To verify convergence, put \(q=|V|\). For each of the \(r\) tuple positions, exactly \(q(N-1)_{r-1}\) ordered distinct tuples have their entry in that position in V: choose that entry in \(q\) ways and fill the other positions with distinct indices from the remaining \(N-1\) indices. Every tuple meeting V is counted in at least one of these \(r\) collections. Therefore
\[
(N)_r-(m)_r\le r q(N-1)_{r-1}.
\]
Dividing by \((N)_r=N(N-1)_{r-1}\) gives
\[
0\le1-c_r\le r\frac{|V|}{N}.
\]
For fixed \(r\), this tends to zero whenever \(|V|/N\to0\), proving the stated convergence without any additional assumption on how N varies.

The argument also includes \(V=\varnothing\), when \(c_r=1\) and both deviations are zero. It never requires distinct representation values, absence of distance ties, injectivity of T, or any metric axiom for the fixed comparison functions.
