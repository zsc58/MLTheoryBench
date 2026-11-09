# Problem

## Setup

Fix \(N\ge 2\). Let \(U,V\in\mathbb R^{N\times N}\) be orthogonal matrices, and let \(\alpha_m\in\mathbb R_{\ge0}^N\) for \(m=1,\ldots,4\). Define known input covariance matrices by
\[
X_m=U\operatorname{diag}(\alpha_m)U^T\quad(m=1,2),
\qquad
X_m=V\operatorname{diag}(\alpha_m)V^T\quad(m=3,4).
\]
Assume that every \(\alpha_m\) has pairwise distinct entries, and that
\[
\alpha_{1,i}\alpha_{2,j}\ne\alpha_{1,j}\alpha_{2,i},\qquad
\alpha_{3,i}\alpha_{4,j}\ne\alpha_{3,j}\alpha_{4,i}
\]
for all \(i\ne j\).

Assume also the following transversality condition: for every \(k\in\{1,\ldots,N-1\}\) and every \(I,J\subseteq\{1,\ldots,N\}\) with \(|I|=|J|=k\),
\[
\operatorname{span}\{U_{:,i}:i\in I\}
\ne
\operatorname{span}\{V_{:,j}:j\in J\}.
\]

Let \(H\in\mathbb R^{N\times N}\) be an unknown invertible filter, and suppose the observed output covariance matrices are
\[
Y_m=H X_mH^T,\qquad m=1,\ldots,4.
\]

## Task

Prove that \(H\) is identifiable from the four covariance equations up to a global sign: if a real matrix \(G\) satisfies
\[
Y_m=G X_mG^T,\qquad m=1,\ldots,4,
\]
then \(G=H\) or \(G=-H\).
