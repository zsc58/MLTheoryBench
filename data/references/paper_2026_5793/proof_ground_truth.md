# Reference Proof

## Proof Structure

First expand the homogeneous network polynomial into its \(d+1\) monomials. After evaluating the two variables through arbitrary coordinate maps, each monomial becomes a rank-one outer product, which yields the width-independent rank bound. Next compute the singular spectrum of the bilinear target by a roots-of-unity orthogonality calculation and apply the best low-rank approximation theorem. Finally, prove coefficient surjectivity with a Vandermonde system and use it to construct suitable coordinate maps for all stated rank-one targets.

## Complete Proof

For each hidden unit, the binomial theorem gives
\[
 (U_{1j}x_1+U_{2j}x_2)^d
 =\sum_{\ell=0}^d {d\choose \ell}U_{1j}^{\ell}U_{2j}^{d-\ell}x_1^{\ell}x_2^{d-\ell}.
\]
Consequently
\[
 F(x_1,x_2)=\sum_{\ell=0}^d \gamma_\ell x_1^\ell x_2^{d-\ell},
 \qquad
 \gamma_\ell={d\choose\ell}\sum_{j=1}^m c_jU_{1j}^{\ell}U_{2j}^{d-\ell}.
\]
After substituting \(x_1=\phi(a)\) and \(x_2=\psi(b)\), define vectors
\[
 u_\ell=(\phi(a)^\ell)_{a\in\mathbb Z_q},
 \qquad
 v_\ell=(\psi(b)^{d-\ell})_{b\in\mathbb Z_q}.
\]
The output matrix therefore has the decomposition
\[
 M=\sum_{\ell=0}^d \gamma_\ell u_\ell v_\ell^{\mathsf T}.
\]
Each summand has rank at most one, so
\[
 \operatorname{rank}(M)\le d+1,
\]
independently of the width and of the coordinate maps. In particular, every representable target matrix must have rank at most \(d+1\).

Now let \(A=K_{f_\times}\), so \(A_{ab}=\zeta^{ab}\). For \(a,a'\in\mathbb Z_q\),
\[
 (AA^*)_{aa'}=\sum_{b\in\mathbb Z_q}\zeta^{(a-a')b}
 =\begin{cases}q,&a=a',\\0,&a\ne a'.\end{cases}
\]
Thus \(AA^*=qI\). Hence \(A/\sqrt q\) is unitary, \(A\) has rank \(q\), and all its \(q\) singular values equal \(\sqrt q\). If \(d<q-1\), then \(d+1<q\), so the rank bound excludes \(A\) from the representable class for every choice of coordinate maps and parameters.

By the best low-rank approximation theorem, for \(r=d+1\),
\[
 \min_{\operatorname{rank}(B)\le r}\|A-B\|_F^2
 =\sum_{i=r+1}^q \sigma_i(A)^2
 =(q-d-1)q.
\]
Moreover, \(\|A\|_F^2=q^2\), since all \(q^2\) entries have modulus one. Therefore
\[
 \min_{\operatorname{rank}(B)\le d+1}
 \frac{\|A-B\|_F^2}{\|A\|_F^2}
 =1-\frac{d+1}{q}.
\]
Every network output has rank at most \(d+1\), so it obeys the same quantity as a lower bound on its normalized error.

It remains to establish the positive representability statements. We first show that when \(m\ge d+1\), any coefficient vector \((\gamma_0,\ldots,\gamma_d)\) can be realized. Set all unused output weights to zero and consider the first \(d+1\) units. Choose pairwise distinct complex numbers \(z_1,\ldots,z_{d+1}\), and put
\[
 U_{1j}=z_j,\qquad U_{2j}=1.
\]
Because every \({d\choose\ell}\) is nonzero, realizing the prescribed coefficients is equivalent to solving
\[
 \sum_{j=1}^{d+1}c_jz_j^\ell
 =\frac{\gamma_\ell}{{d\choose\ell}},
 \qquad 0\le \ell\le d.
\]
This is a square Vandermonde system. Its determinant is nonzero because the \(z_j\)'s are distinct, so it has a solution. In particular, parameters can be chosen so that
\[
 F(x_1,x_2)=x_1x_2^{d-1}.
\]

Since \(q\) is prime and \(2\le d<q\), the element \(d-1\) is invertible modulo \(q\). Choose \(s\in\mathbb Z_q\) such that
\[
 s(d-1)=1\pmod q.
\]
Consider any target which factors as
\[
 K_f(a,b)=g(a)h(b),
\]
where \(g\) and \(h\) take values among the powers of \(\zeta\). Define
\[
 \phi(a)=g(a),\qquad \psi(b)=h(b)^s.
\]
Using the polynomial just constructed, the resulting output is
\[
 F(\phi(a),\psi(b))
 =g(a)h(b)^{s(d-1)}
 =g(a)h(b),
\]
because \(h(b)^q=1\).

For a linear phase \(f(a,b)=ua+vb\), take \(g(a)=\zeta^{ua}\) and \(h(b)=\zeta^{vb}\). The three other targets factor respectively as
\[
 \zeta^{a^2+b}=\zeta^{a^2}\zeta^b,
 \qquad
 \zeta^{a+b^2}=\zeta^a\zeta^{b^2},
 \qquad
 \zeta^{a^2+b^2}=\zeta^{a^2}\zeta^{b^2}.
\]
They are therefore all representable whenever \(m\ge d+1\), completing every clause of the theorem.
