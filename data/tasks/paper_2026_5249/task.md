# Problem

## Setup

Let \(d\ge 1\), \(n\ge 2\), and \(1\le k<n\). Set \(K=[0,1]^d\), and let \(C_{\rm sym}(K^n)\) denote the continuous real-valued functions invariant under every permutation of the \(n\) inputs. For a latent dimension \(M\), consider functions
\[
f(x_1,\ldots,x_n)=\rho\!\left(\sum_{1\le i_1,\ldots,i_k\le n}
\Phi(x_{i_1},\ldots,x_{i_k})\right),
\]
where repeated indices are allowed, \(\Phi:K^k\to\mathbb R^M\) is a shared continuous encoder (in particular, an MLP), and \(\rho:\mathbb R^M\to\mathbb R\) is continuous (in particular, an MLP). Let \(M_{\rm univ}(d,n,k)\) be the smallest \(M\) for which this class is dense in \(C_{\rm sym}(K^n)\) in the uniform norm.

## Task

Prove that, with
\[
s=\left\lceil\bigl(d(n-k)+1\bigr)^{1/k}\right\rceil,
\]
one has
\[
M_{\rm univ}(d,n,k)\ \ge\
\left\lceil\frac{d(n-k)}{s^k-(s-1)^k}\right\rceil.
\]
