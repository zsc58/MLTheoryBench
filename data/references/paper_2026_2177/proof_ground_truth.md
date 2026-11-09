# Reference Proof

## Proof Structure

Establish the finite tensor-product orthonormal basis and reproducing kernel. Then expand the defining signed kernel combination, identify its coefficients, and prove the matrix identity and uniqueness. The definition of h is already supplied; neither a representer theorem nor a derivation of SVM optimality is needed.

## Complete Proof

Let \(\mathcal K=\{0,\ldots,n\}^d\) and \(p_k(x)=\prod_{j=1}^d p_{k_j}(x_j)\). The polynomial factors are square-integrable by the moment assumptions. Moreover, Cauchy–Schwarz gives
\[
\int_I |p_r(t)p_s(t)|\,d\mu(t)\leq 1.
\]
Thus the product integrals below are absolutely integrable, and product-measure integration yields
\[
\langle p_k,p_\ell\rangle
=\prod_{j=1}^d\int_I p_{k_j}(t)p_{\ell_j}(t)\,d\mu(t)
=\delta_{k\ell}.
\]
The functions \(p_k\) are therefore orthonormal. Since their span is \(\mathcal H_n^{(d)}\) by definition, they form an orthonormal basis, and
\[
\dim\mathcal H_n^{(d)}=(n+1)^d.
\]
In particular, for \(f=\sum_k a_kp_k\), one has \(\|f\|^2=\sum_k a_k^2\). The inherited inner product is positive definite on this space of polynomial functions, and the space is complete because it is finite-dimensional. This also identifies it with the tensor product of the one-dimensional truncated polynomial spaces: the products of their basis elements span it, and their inner products factor as required.

Expanding the product of finite sums gives, for every \(x,z\in I^d\),
\[
K_n^{(d)}(x,z)
=\prod_{j=1}^d\left(\sum_{r=0}^n p_r(x_j)p_r(z_j)\right)
=\sum_{k\in\mathcal K}p_k(x)p_k(z).
\]
The kernel is symmetric. For any finite collection \(z_1,\ldots,z_M\in I^d\) and real numbers \(t_1,\ldots,t_M\),
\[
\sum_{a,b=1}^M t_at_bK_n^{(d)}(z_a,z_b)
=\sum_{k\in\mathcal K}\left(\sum_{a=1}^M t_ap_k(z_a)\right)^2\geq0,
\]
so it is positive semidefinite.

For fixed \(z\), the finite kernel expansion places \(K_n^{(d)}(\cdot,z)\) in \(\mathcal H_n^{(d)}\). If \(f=\sum_k a_kp_k\), orthonormality gives
\[
\langle f,K_n^{(d)}(\cdot,z)\rangle
=\sum_k a_kp_k(z)=f(z).
\]
Furthermore,
\[
|f(z)|\leq\|f\|\left(\sum_k p_k(z)^2\right)^{1/2},
\]
so point evaluation is continuous. Hence \(\mathcal H_n^{(d)}\) is an RKHS with reproducing kernel \(K_n^{(d)}\).

By the definition in the task,
\[
h(x)=\sum_{i=1}^N\alpha_i y_iK_n^{(d)}(x_i,x).
\]
Each kernel section belongs to \(\mathcal H_n^{(d)}\), so their finite linear combination h belongs to that space. Substituting the finite kernel expansion and interchanging finite sums gives
\[
\begin{aligned}
h(x)
&=\sum_{i=1}^N\alpha_i y_i\sum_{k\in\mathcal K}p_k(x_i)p_k(x)\\
&=\sum_{k\in\mathcal K}\left(\sum_{i=1}^N\alpha_i y_i p_k(x_i)\right)p_k(x).
\end{aligned}
\]
Thus the claimed expansion holds pointwise on \(I^d\), with
\[
c_k=\sum_{i=1}^N\alpha_i y_i p_k(x_i).
\]
Taking the inner product of any expansion of h with \(p_k\) recovers its k-th coefficient. Therefore the expansion is unique.

With \(P_{i,k}=p_k(x_i)\) and \(s_i=\alpha_i y_i\),
\[
(P^Ts)_k=\sum_{i=1}^N P_{i,k}s_i
=\sum_{i=1}^N p_k(x_i)\alpha_i y_i=c_k.
\]
Consequently \(c=P^Ts\), using the same ordering of \(\mathcal K\) for the columns of P and the entries of c.

The calculations do not require nonzero h, distinct data points, or an invertible design matrix. They also apply when n=0. Optimality of alpha supplies the source's trained-SVM interpretation, but the algebraic expansion itself uses only the displayed definition of h.
