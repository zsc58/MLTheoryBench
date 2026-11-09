# Problem

## Setup

Let \(d\ge 1\) be an integer, let \(0<T<\infty\), and let \(E\) be an embedding space. Let \(F:\mathbb R^d\times E\times[0,T]\to\mathbb R^d\) be a fixed predictor. A target concept has embedding \(u\in E\) and is associated with a smooth latent submanifold \(\mathcal S\subset\mathbb R^d\).

Draw \(t\) uniformly from \([0,T]\), and conditionally draw \(z_t\sim p_t(\cdot\mid u)\). In this geometric setup, assume
\[
p_t(\mathcal S\mid u)=1
\quad\text{for almost every }t\in[0,T].
\]
At the sampled point \(z_t\in\mathcal S\), let \(P_N\) denote orthogonal projection onto \((T_{z_t}\mathcal S)^\perp\), the normal complement of the tangent space. All expectations and almost-sure statements below refer to this joint law, with the embeddings held fixed. For an anchor embedding \(a\in E\), define
\[
D_a(z_t,t)=F(z_t,u,t)-F(z_t,a,t).
\]

Suppose the predictor has \(L\ge 1\) cross-attention layers with matrix-valued maps \(H_1,\ldots,H_L\). For each layer, the matrix dimensions are fixed across embeddings. For each fixed \(e\in E\), the maps \((z,t)\mapsto F(z,e,t)\) and \((z,t)\mapsto H_\ell(z,t,e)\), \(1\le\ell\le L\), are measurable. Define the attention-consistency loss
\[
J(a)=\mathbb E\left[
\sum_{\ell=1}^L
\|H_\ell(z_t,t,u)-H_\ell(z_t,t,a)\|_F^2
\right].
\]
For a fixed numerical stabilizer \(\delta>0\) and \(\rho\in[0,1)\), call \(a\) a \(\rho\)-proximal anchor if
\[
\mathbb E\left[
\frac{\|P_ND_a(z_t,t)\|^2}
{\|D_a(z_t,t)\|^2+\delta}
\right]\le \rho^2.
\]

Assume that constants \(C>0\) and \(\eta\ge 0\) satisfy, for every anchor embedding \(a\in E\),
\[
\|P_ND_a(z_t,t)\|
\le C\sum_{\ell=1}^L
\|H_\ell(z_t,t,u)-H_\ell(z_t,t,a)\|_F+\eta
\quad\text{almost surely}.
\]

An optimization procedure returns an anchor embedding \(a_\star\in E\) such that
\[
J(a_\star)\le\gamma,
\qquad
\|D_{a_\star}(z_t,t)\|^2\ge c_{\min}>0
\quad\text{almost surely},
\]
where \(\gamma\ge0\). Define
\[
\rho=
\sqrt{\frac{2C^2L\gamma+2\eta^2}{c_{\min}}},
\]
and assume this value lies in \([0,1)\).

## Task

Prove the integrated guarantee
\[
\mathbb E\|P_ND_{a_\star}(z_t,t)\|^2
\le 2C^2LJ(a_\star)+2\eta^2
\le 2C^2L\gamma+2\eta^2,
\]
and consequently prove that \(a_\star\) is a \(\rho\)-proximal anchor.
