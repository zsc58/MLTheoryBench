# Reference Proof

## Audited Obligations

The proof must establish: well-defined updates and finite objective values from the second iterate onward; bounded selected subgradients; the correct one-step composite inequality; telescoping of the changing metrics; the scalar difference-accumulation estimate, including zero cumulative sums; the correction for the lagged inverse weights; constants independent of the horizon; and Jensen averaging. All these obligations are derived below. No specialized convergence theorem is assumed.

## Complete Proof

### 1. Well-definedness and bounded subgradients

Fix $x^\star\in\operatorname*{argmin}F$. The minimum $F_\star$ is finite because $F$ is proper and has a minimizer. For any selected $s\in\partial f(x)$, the subgradient inequality and Lipschitz continuity, applied to $x+ts$ with $t>0$, give
\[
t\|s\|^2\le f(x+ts)-f(x)\le Gt\|s\|.
\]
Consequently $\|s\|\le G$, including when $s=0$.

At every finite iteration the weights are finite and $W_n\succeq\varepsilon I$. The update has a unique minimizer in $\operatorname{dom}g$. Indeed, for its fixed center $v=x^n-\eta W_n^{-1}s^n$, its objective
\[
Q(y)=g(y)+\frac1{2\eta}\|y-v\|_{W_n}^2
\]
is proper and lower-semicontinuous. Since
\[
g(y)=F(y)-f(y)\ge F_\star-f(0)-G\|y\|,
\]
we have
\[
Q(y)\ge F_\star-f(0)-G\|y\|+\frac{\varepsilon}{2\eta}\|y-v\|^2.
\]
Thus its infimum is finite. Moreover, $Q$ is strongly convex with modulus $\varepsilon/\eta$. If $(y_j)$ is a minimizing sequence and $q=\inf Q$, strong convexity gives
\[
\frac{\varepsilon}{8\eta}\|y_j-y_\ell\|^2
\le\frac{Q(y_j)+Q(y_\ell)}2-q.
\]
The sequence is Cauchy, so completeness and lower semicontinuity give a minimizer; strong convexity makes it unique. Its objective is finite, so it belongs to $\operatorname{dom}g$. In particular, $F(x^k)$ is finite for all $k\ge2$, without assuming $x^1\in\operatorname{dom}g$.

Set, for $k\ge1$,
\[
a_i^k=\|s_i^k-s_i^{k-1}\|^2,\qquad
v_i^k=\sqrt{\sum_{j=1}^k a_i^j}=w_i^k-\varepsilon,
\qquad v_i^0=0.
\]
The weights are nondecreasing. Also $\|s^1-s^0\|\le G$ and $\|s^k-s^{k-1}\|\le2G$ for $k\ge2$.

### 2. Correct one-step inequality

For $n\ge1$, let $h^n=x^{n+1}-x^n$. Proximal optimality gives
\[
p^{n+1}:=-s^n-\eta^{-1}W_nh^n\in\partial g(x^{n+1}).
\]
The convex subgradient inequalities at $x^n$ and $x^{n+1}$ imply
\[
\begin{aligned}
F(x^{n+1})-F_\star
&\le \eta^{-1}\langle W_n(x^n-x^{n+1}),x^{n+1}-x^\star\rangle\\
&\quad+f(x^{n+1})-f(x^n)-\langle s^n,h^n\rangle\\
&\le \frac{\|x^n-x^\star\|_{W_n}^2-\|x^{n+1}-x^\star\|_{W_n}^2-\|h^n\|_{W_n}^2}{2\eta}
 +\langle s^{n+1}-s^n,h^n\rangle.
\end{aligned}
\]
For the second inequality, convexity at $x^{n+1}$ gives
\[
f(x^{n+1})-f(x^n)\le\langle s^{n+1},h^n\rangle.
\]
Weighted Young's inequality gives
\[
2\eta\langle s^{n+1}-s^n,h^n\rangle
\le\|h^n\|_{W_n}^2+\eta^2\|s^{n+1}-s^n\|_{W_n^{-1}}^2.
\]
Hence
\[
F(x^{n+1})-F_\star
\le\frac{\|x^n-x^\star\|_{W_n}^2-\|x^{n+1}-x^\star\|_{W_n}^2}{2\eta}
+\frac\eta2\sum_{i=1}^d\frac{a_i^{n+1}}{w_i^n}.
\tag{1}
\]

### 3. Metric telescoping

Boundedness of the iterates and finiteness of $d$ imply
\[
D:=\sup_{k\ge1}\max_{1\le i\le d}\|x_i^k-x_i^\star\|^2<\infty.
\]
For $N\ge2$, telescoping the distance terms in (1) gives
\[
\begin{aligned}
T_N&:=\sum_{n=1}^{N-1}\left(\|x^n-x^\star\|_{W_n}^2-\|x^{n+1}-x^\star\|_{W_n}^2\right)\\
&=\|x^1-x^\star\|_{W_1}^2
+\sum_{k=2}^{N-1}\sum_{i=1}^d(w_i^k-w_i^{k-1})\|x_i^k-x_i^\star\|^2
-\|x^N-x^\star\|_{W_{N-1}}^2\\
&\le\varepsilon\|x^1-x^\star\|^2+D\sum_{i=1}^d v_i^{N-1}.
\end{aligned}
\tag{2}
\]
Here the middle sum is empty when $N=2$. The last bound uses $w_i^k=\varepsilon+v_i^k$ and the nonnegative increments of $v_i^k$.

### 4. Scalar summation and the lagged-denominator correction

For nonnegative numbers $b_1,\ldots,b_M$, let $B_k=\sum_{j=1}^k b_j$ and $B_0=0$. If $B_k=0$, the corresponding summand below is zero. If $B_k>0$, then
\[
\frac{b_k}{\varepsilon+\sqrt{B_k}}
\le\frac{b_k}{\sqrt{B_k}}
=(\sqrt{B_k}-\sqrt{B_{k-1}})\left(1+\frac{\sqrt{B_{k-1}}}{\sqrt{B_k}}\right)
\le2(\sqrt{B_k}-\sqrt{B_{k-1}}).
\]
Therefore
\[
\sum_{k=1}^M\frac{b_k}{\varepsilon+\sqrt{B_k}}\le2\sqrt{B_M}.
\tag{3}
\]
In particular, applying (3) to $b_k=a_i^k$ and dropping its nonnegative first summand yields
\[
\sum_{k=2}^N\frac{a_i^k}{w_i^k}\le2v_i^N.
\]
The actual denominators in (1) are lagged. Exactly,
\[
\frac{a_i^k}{w_i^{k-1}}=\frac{a_i^k}{w_i^k}
+\left(\frac1{w_i^{k-1}}-\frac1{w_i^k}\right)a_i^k.
\]
Since $a_i^k\le4G^2$ for $k\ge2$ and the inverse-weight differences are nonnegative,
\[
\begin{aligned}
\sum_{k=2}^N\frac{a_i^k}{w_i^{k-1}}
&\le2v_i^N+4G^2\sum_{k=2}^N\left(\frac1{w_i^{k-1}}-\frac1{w_i^k}\right)\\
&=2v_i^N+4G^2\left(\frac1{w_i^1}-\frac1{w_i^N}\right)
\le2v_i^N+\frac{4G^2}{w_i^1}.
\end{aligned}
\tag{4}
\]
This argument includes zero differences and never divides by a vanishing cumulative norm.

### 5. Uniform cumulative bound and averaging

Sum (1), use (2) and (4), and note $v_i^{N-1}\le v_i^N$. This gives
\[
\sum_{k=2}^N(F(x^k)-F_\star)
\le\frac{\varepsilon}{2\eta}\|x^1-x^\star\|^2
+\left(\frac D{2\eta}+\eta\right)\sum_{i=1}^d v_i^N
+2\eta G^2\sum_{i=1}^d\frac1{w_i^1}.
\tag{5}
\]
Cauchy-Schwarz across the blocks and the subgradient bounds imply
\[
\sum_{i=1}^d v_i^N
\le\sqrt d\sqrt{\sum_{k=1}^N\|s^k-s^{k-1}\|^2}
\le2G\sqrt{dN}
\le2\sqrt2\,G\sqrt d\,\sqrt{N-1}
\quad(N\ge2).
\]
Thus (5) is at most $A+B\sqrt{N-1}$ with the finite nonnegative constants
\[
A=\frac{\varepsilon}{2\eta}\|x^1-x^\star\|^2+2\eta G^2\sum_{i=1}^d\frac1{w_i^1},
\qquad
B=2\sqrt2\,G\sqrt d\left(\frac D{2\eta}+\eta\right).
\]
They are independent of $N$; in particular $w_i^1\ge\varepsilon>0$.

All averaged points lie in $\operatorname{dom}g$ by convexity. Jensen's inequality gives
\[
F(\bar x^N)-F_\star
\le\frac1{N-1}\sum_{k=2}^N(F(x^k)-F_\star)
\le\frac A{N-1}+\frac B{\sqrt{N-1}}.
\]
The lower bound is immediate from minimality of $F_\star$. Finally, $1/(N-1)\le1/\sqrt{N-1}$ and $N/(N-1)\le2$ for $N\ge2$, so this also proves the stated $O(N^{-1/2})$ rate.
