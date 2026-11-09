# Reference Proof

## Proof Structure

We first bound the temporal cut for the local-window matrix. For the uniform causal matrix, we compute its cut and volume exactly, then use the possible ordering of the two cut-side volumes to prove the uniform lower bound.

## Complete Proof

Write \(u=H_n-H_t\), where \(H_m=\sum_{r=1}^m 1/r\) and \(H_0=0\).

For \(A^{(w)}\), an edge crossing \(T_t\) must join a left vertex \(L_i\) with \(i\ge t\) to a right vertex \(R_j\) with \(j<t\). The window support forces \(i\in\{t,\ldots,t+w-1\}\). Thus at most \(w\) rows can contribute crossing weight, and every row has total weight one. Hence
\[
 w_G(T_t,T_t^c)\le w.
\]
Each left vertex has degree one. Therefore \(\operatorname{vol}(T_t)\ge t\) and \(\operatorname{vol}(T_t^c)\ge n-t\), which gives
\[
 \phi_G(T_t)\le \frac{w}{\min\{t,n-t\}}.
\]
In particular, if \(n-t\le t\), then \(\phi_G(T_t)\le w/(n-t)\).

Now consider \(A^{(u)}\). The crossing edges are exactly \((L_i,R_j)\) with \(i\ge t\) and \(j<t\). Hence
\[
 w_G(T_t,T_t^c)=\sum_{i=t}^{n-1}\sum_{j=0}^{t-1}\frac1{i+1}
 =t\sum_{r=t+1}^n\frac1r=tu.
\]
The left degrees are one, while the degree of \(R_j\) is
\[
 \sum_{i=j}^{n-1}\frac1{i+1}=H_n-H_j.
\]
Using \(\sum_{j=0}^{t-1}H_j=tH_t-t\), we obtain
\[
 \operatorname{vol}(T_t)
 =t+\sum_{j=0}^{t-1}(H_n-H_j)
 =t(2+u).
\]
The total graph volume is \(2n\), so \(\operatorname{vol}(T_t^c)=2n-t(2+u)\).

If \(\operatorname{vol}(T_t)\le \operatorname{vol}(T_t^c)\), then \(t(2+u)\le n\). Since \(t(2+u)\ge2t\), this implies \(t\le\lfloor n/2\rfloor\). Consequently,
\[
 u=H_n-H_t\ge H_n-H_{\lfloor n/2\rfloor}\ge\frac12.
\]
Thus
\[
 \phi_G(T_t)=\frac{tu}{t(2+u)}=\frac{u}{2+u}\ge\frac15.
\]

It remains to treat \(\operatorname{vol}(T_t)\ge\operatorname{vol}(T_t^c)\). Here the denominator in conductance is \(2n-t(2+u)\). The desired inequality is equivalent to
\[
 \frac{tu}{2n-t(2+u)}\ge\frac15
 \quad\Longleftrightarrow\quad
 t(1+3u)\ge n. \tag{1}
\]
If \(t\le n/2\), then \(u\ge1/2\), so \(1+3u\ge2+u\). The assumed volume ordering gives \(t(2+u)\ge n\), and hence (1).

If \(t>n/2\), the elementary harmonic-tail bound \(u\ge(n-t)/n\) yields, with \(x=t/n\in(1/2,1)\),
\[
 \frac{t(1+3u)}n
 \ge x\bigl(1+3(1-x)\bigr)
 =x(4-3x)\ge1,
\]
because \(x(4-3x)-1=(3x-1)(1-x)\ge0\). Thus (1) also holds in this case. Therefore \(\phi_G(T_t)\ge1/5\) for every \(0<t<n\).

Combining the two bounds proves the stated temporal-cut separation. In particular, on any family of cuts satisfying \(\min\{t,n-t\}\ge c n\) for a fixed \(c>0\), the window bound is at most \(w/(cn)=O(w/n)\), while uniform causal attention retains the \(1/5\) lower bound.
