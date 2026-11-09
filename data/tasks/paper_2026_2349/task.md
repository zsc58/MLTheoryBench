# Problem

## Setup

Let \(d\geq1\) be an integer, let \(\tau>0\), and let \(p:\mathbb R^d\to\mathbb R\) be a polynomial. Write its homogeneous decomposition as
\[
p=\sum_{k=0}^m p_k,
\]
where \(m\geq0\) is an integer and \(p_k\) is homogeneous of degree \(k\). Set \(p_k=0\) for \(k>m\), so in particular \(p_1=0\) when \(m=0\). Identify the constant polynomial \(p_0\) with its value.

For \(\alpha\in\mathbb N_0^d\), write \(x^\alpha=\prod_{j=1}^d x_j^{\alpha_j}\) and \(\alpha!=\prod_{j=1}^d\alpha_j!\). For a polynomial \(q(x)=\sum_\alpha c_\alpha x^\alpha\), define its Fischer norm by
\[
\|q\|_F^2=\sum_\alpha\alpha!\,c_\alpha^2.
\]
Let \(\Delta=\sum_{j=1}^d\partial^2/\partial x_j^2\), and put
\[
p_k^{\sharp}=\exp\!\left(-\frac{\tau^2}{2}\Delta\right)p_k
=\sum_{j\geq0}\frac{(-\tau^2/2)^j}{j!}\Delta^j p_k,
\]
where the sum is finite. Let \(\operatorname{ReLU}(t)=\max\{t,0\}\).

For the approximation statement, fix \(\sigma_X>0\). Let \(D\) be the law of a mean-zero random vector \(X\in\mathbb R^d\) such that, for every unit vector \(u\) and every \(t\geq0\),
\[
\Pr(\langle X,u\rangle\geq t)\leq\exp\!\left(-\frac{t^2}{2\sigma_X^2}\right).
\]
Write \(\|h\|_{L^2(D)}=(\mathbb E|h(X)|^2)^{1/2}\). An \(n\)-neuron two-layer ReLU network means a function of the form
\[
a_0+\sum_{i=1}^n a_i\operatorname{ReLU}(\langle v_i,x\rangle-s_i),
\]
with real output weights \(a_i\), vectors \(v_i\in\mathbb R^d\), and \(s_i\geq0\).

Define
\[
K_{d,1}=2^{3/2}\sigma_X\sqrt d,
\]
and, for \(k\geq2\),
\[
K_{d,k}=
\frac{2^{(3k-1)/2}\sigma_X^k\Gamma((k-1)/2)}{(k-2)!}
\left(\frac{\Gamma(k+d/2)}{\Gamma(d/2)}\right)^{1/2},
\]
where \(\Gamma(a)=\int_0^\infty t^{a-1}e^{-t}\,dt\) for \(a>0\). Empty sums are zero.

## Task

Prove the following integrated claim.

For every \(x\in\mathbb R^d\), the polynomial \(p\) admits the Gaussian ReLU integral representation
\[
\begin{aligned}
p(x)=p_0
&+\mathbb E_{V\sim N(0,\tau^2I_d)}\left[
\frac{2p_1^{\sharp}(V)}{\tau^2}\operatorname{ReLU}(\langle x,V\rangle)\right.\\
&\left.\quad+\int_0^\infty
2\sum_{k=2}^m\frac{s^{k-2}p_k^{\sharp}(V)}{(k-2)!\tau^{2k}}
\operatorname{ReLU}(\langle x,V\rangle-s)\,ds\right].
\end{aligned}
\]
Moreover, for every integer \(n\geq1\), there is an \(n\)-neuron two-layer ReLU network \(p_n\) such that
\[
\|p_n-p\|_{L^2(D)}
\leq\frac1{\sqrt n}
\left\{\left(\sum_{k=1}^mK_{d,k}\|p_k\|_F\right)^2
-\|p-p_0\|_{L^2(D)}^2\right\}^{1/2}
\leq\frac1{\sqrt n}\sum_{k=1}^mK_{d,k}\|p_k\|_F.
\]
