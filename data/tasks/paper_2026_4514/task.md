# Problem

## Setup

Let \(N,K\) be integers with \(1\le K\le N\). Let \(x=(x_1,\ldots,x_N)\in\mathbb R^N\) have components \(x_i=u_iv_i\), where \(u_i\sim\mathrm{Bernoulli}(p_i)\), \(v_i\sim\mathrm{Uniform}(0,1)\), and all these variables are mutually independent. Set
\[
p_i=c\,i^{-a},\qquad a>1,\qquad c=\left(\sum_{i=1}^N i^{-a}\right)^{-1}.
\]
Let \(A\in\mathbb R^{N\times N}\) be diagonal with \(A_{ii}=a_i=i^{-b}\), where \(b\ge0\).

A fixed embedding \(W\in\mathbb R^{K\times N}\) has unit-norm columns. An unrestricted trainable matrix \(B\in\mathbb R^{K\times K}\) produces \(y=W^TBWx\). Its population quadratic loss is
\[
L(B)=\tfrac12\mathbb E_x\|Ax-W^TBWx\|_2^2.
\]
Define \(\sigma_i^2=\mathbb E[x_i^2]=p_i/3\) and \(\Sigma=\operatorname{diag}(\sigma_1^2,\ldots,\sigma_N^2)\). Let \(L_{\mathrm d}\) be the quadratic surrogate obtained from \(L\) by replacing its uncentered second-moment matrix \(\mathbb E_x[xx^T]\) by \(\Sigma\). The dynamics analyzed here are
\[
\dot B=-\eta\nabla_B L_{\mathrm d}(B),\qquad \eta>0,
\]
where the gradient uses the Frobenius inner product, \(t\ge0\), and \(B(0)=B_0\) is any prescribed matrix. Thus the diagonal approximation specifies the objective being analyzed; it is not an assertion that the original input second-moment matrix is diagonal.

For the random-embedding part, the embedding is sampled independently of the input and then held fixed. Write \(\mathbb E_W\) for expectation over its sampling law. Define the **isotropic mean-field approximation** as follows: in the surrogate loss gradient, replace the two factors \(WW^T\) and \(W\Sigma W^T\) multiplying the trainable matrix by their separate embedding-ensemble expectations, while leaving the term independent of the trainable matrix at its realized value. Denote the resulting trajectory, with initial value \(B_0\), by \(B_{\mathrm{mf}}\). This is a prescribed approximation, not a concentration assertion or a definition of \(\mathbb E_W[B(t)]\).

## Task

Prove the following two conclusions.

1. **Hard-cluster case.** Suppose \(\{1,\ldots,N\}\) is partitioned into nonempty clusters \(G_1,\ldots,G_K\), and \(W_{ji}=1\) exactly when \(i\in G_j\), with all other entries zero. Write
\[
n_j=|G_j|,\qquad C_j=\sum_{i\in G_j}\sigma_i^2,\qquad S_j=\sum_{i\in G_j}a_i\sigma_i^2.
\]
Show that the matrix-entry dynamics decouple and that each diagonal latent coefficient has homogeneous exponential relaxation rate \(\eta n_jC_j\). If, for positive scales \(q_j\) and fixed constants \(0<m\le M<\infty\),
\[
mq_j\le\sigma_i^2\le Mq_j\qquad(i\in G_j),
\]
show that this rate is comparable to \(\eta n_j^2q_j\), with comparison constants depending only on \(m,M\). Determine the limiting shared coefficients and the minimum surrogate loss, and explain the collision error associated with a cluster containing more than one feature.

2. **Isotropic-random mean-field case.** Suppose each unit-norm column of \(W\) has a rotationally invariant marginal distribution in \(\mathbb R^K\). Establish
\[
\mathbb E_W[WW^T]=\frac NK I_K,\qquad
\mathbb E_W[W\Sigma W^T]=\frac{\sum_i\sigma_i^2}{K}I_K.
\]
Show that the isotropic mean-field dynamics defined above have the common homogeneous relaxation rate
\[
\eta\left(\frac NK\right)^2\bar\sigma^2,
\qquad \bar\sigma^2=\frac1N\sum_i\sigma_i^2,
\]
in every matrix direction. Thus this approximation replaces feature-specific spectral rates by one shared rate. The mean-field calculation is motivated by the regime \(N\gg K\); no convergence or concentration claim for the sampled projected matrices is requested.
