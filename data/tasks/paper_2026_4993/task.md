# Problem

## Setup

Fix integers \(M,K,N,P\ge1\) and a finite observation horizon \(T\in[0,\infty)\). Let \(0\le t_1<\cdots<t_N\le T\) be an ordered event history with marks \(m_i\in\{1,\ldots,M\}\). Assume finite real base rates \(\mu_p\ge0\), interaction coefficients \(\alpha_{p,q,k}\ge0\) for \(p,q\in\{1,\ldots,M\}\) and \(k\in\{1,\ldots,K\}\), and decay rates \(\gamma_k>0\). For \(t\in[0,T]\), define the multivariate linear exponential Hawkes intensities
\[
\lambda_p(t)=\mu_p+\sum_{j:t_j<t}\sum_{k=1}^K\alpha_{p,m_j,k}\gamma_k e^{-\gamma_k(t-t_j)}.
\]
For each kernel let
\[
R_p^k(t)=\sum_{j:t_j<t}\alpha_{p,m_j,k}e^{-\gamma_k(t-t_j)},
\]
and write \(R_i^k=(R_1^k(t_i),\ldots,R_M^k(t_i))^\top\). Define the log-likelihood as an extended-real quantity, using the natural logarithm and \(\log 0=-\infty\):
\[
\ell=\sum_{i=1}^N\log\lambda_{m_i}(t_i)-\sum_{p=1}^M\int_0^T\lambda_p(t)\,dt.
\]
An ordered prefix scan of \(x_1,\ldots,x_N\) under an associative operation returns \(x_i\odot\cdots\odot x_1\) for every \(i\).

Use a shared-memory, unit-cost exact-real arithmetic model with \(P\) processors. Scalar arithmetic, comparisons, exponential evaluations, logarithm evaluations on positive arguments, and single-word memory accesses have constant cost. A real scalar or an index occupies one word. The parameters and history are already available as random-access inputs; concurrent reads are permitted. Exactness refers to this arithmetic model, not to bitwise equality of floating-point implementations. For the resource bounds, put
\[
L_N=\max\{1,\log_2 N\}.
\]

## Task

Prove that the exact state sequence \(\{R_i^k:1\le i\le N,1\le k\le K\}\), all event intensities \(\lambda_p(t_i)\), and the log-likelihood \(\ell\) can be computed by a structured parallel prefix-scan algorithm whose transition combine uses \(O(M)\) operations and storage, with scan time
\[
O\!\left(KM\left(\frac NP+L_N\right)\right),
\]
and whose unbatched compressed-state peak memory is \(O(KMN)\).

For \(N\ge2\), the time bound is \(O(KM(N/P+\log N))\). On any regime satisfying \(L_N\le cN/P\) for a fixed constant \(c>0\), it reduces to \(O(KMN/P)\). Constants in the general bounds must be independent of \(M,K,N,P\), the event times, and the parameter values; the constant in the reduced bound may additionally depend on \(c\).
