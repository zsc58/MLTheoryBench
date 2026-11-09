# Problem

## Setup

Let \(d,p,K\) be positive integers. A shallow quadratic network with \(K\) hidden units and \(p\) outputs has parameters \(\vartheta=((v_j,w_j))_{j=1}^K\), with \(v_j\in\mathbb R^p\) and \(w_j\in\mathbb R^d\setminus\{0\}\), and output
\[
f_\vartheta(x)=\sum_{j=1}^K v_j\,(w_j^\top x)^2.
\]
Let \(\operatorname{Sym}_d\) be the space of real symmetric \(d\times d\) matrices. Identify the network's quadratic coefficient with
\[
\Phi(\vartheta)=\sum_{j=1}^K v_j\otimes(w_jw_j^\top)\in\mathbb R^p\otimes\operatorname{Sym}_d,
\]
and define
\[
A=\{v\otimes ww^\top:v\in\mathbb R^p,\ w\in\mathbb R^d\setminus\{0\}\}.
\]
Write \(S_K\) for the affine K-th secant cone of \(A\), namely the Zariski closure in the coefficient space of the set of sums of \(K\) elements of \(A\).

Fix a parameter point \(\theta^*\) and put \(y^*=\Phi(\theta^*)\). Let \(D(\vartheta)\) be the Kullback--Leibler divergence of a statistical model with regression function \(f_\vartheta\) from a fixed data-generating distribution. Assume \(\theta^*\) is a local minimizer of \(D\), and that the local excess KL loss
\[
\mathcal K(\vartheta)=D(\vartheta)-D(\theta^*)
\]
is finite and real analytic near \(\theta^*\). Use a proper prior density \(\pi\) that is real analytic and strictly positive near \(\theta^*\). The local learning coefficient (LLC) at \(\theta^*\) is the real log-canonical threshold of the germ of \(\mathcal K\), with this prior.

Assume \(\theta^*\) is generic in the algebraic-geometric sense: the parameter choices are generic, every atom is nonzero, the constituent atoms are in general position, and \(y^*\) is a generic smooth point of \(S_K\).

Assume that, on a neighborhood \(M\) of \(y^*\) in the smooth locus of \(S_K\), there is a real-analytic induced KL loss \(\widetilde D\) such that
\[
D(\vartheta)=\widetilde D(\Phi(\vartheta))
\]
for \(\vartheta\) near \(\theta^*\). Assume the induced map \(\Phi\) into \(M\) has surjective differential at \(\theta^*\). Assume the induced identifiable model is regular at \(y^*\): \(\widetilde D\) has a local minimum there and its Hessian in local coordinates on \(M\) is positive definite.

Finally, assume \(S_K\) is non-defective, meaning that its affine dimension is
\[
\dim S_K=\min\{K(p+d-1),\ p\,d(d+1)/2\}.
\]

## Task

Prove that the LLC at \(\theta^*\) is
\[
\lambda=\frac12\min\{K(p+d-1),\ p\,d(d+1)/2\}.
\]
