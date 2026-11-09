# Problem

## Setup

Let \(\nu\) be a probability measure on \(\mathbb R\) and define its Stieltjes transform by
\[
m(z)=\int_{\mathbb R}\frac{1}{x-z}\,\nu(dx),\qquad z\in\mathbb C\setminus\mathbb R.
\]
Assume that, away from finitely many singular points, \(m\) is a branch of a nonzero polynomial relation
\[
P(z,m(z))=0,
\]
where
\[
P(z,m)=\sum_{i=0}^{d_z}\sum_{j=0}^{d_m}p_{ij}z^i m^j\in\mathbb C[z,m],
\qquad d_z=\deg_z P,\quad d_m=\deg_m P.
\]
The physical branch means the transform of the specified measure; it has the Herglotz property \(\Im m(z)>0\) for \(\Im z>0\) and is normalized by \(m(z)=-z^{-1}+O(z^{-2})\) as \(|z|\to\infty\).

Define the possibly multivalued R-transform by locally inverting this physical transform near infinity in each half-plane, so that
\[
R(-m(z))=z+\frac1{m(z)}.
\]
Whenever these inverse branches are analytically continued, the branch choices are continued consistently.

For a realizable free decompression factor \(\tau\ge1\) (equivalently \(\tau=e^t\), \(t\ge0\)), let \(\nu_\tau\) be the decompressed probability measure and let
\[
m_\tau(z)=\int_{\mathbb R}\frac1{x-z}\,\nu_\tau(dx),\qquad z\in\mathbb C\setminus\mathbb R,
\]
be its physical Stieltjes transform, with the same Herglotz property and normalization. Decompression is characterized on the corresponding inverse branches near infinity by
\[
R(-\tau m_\tau(z))=z+\frac1{m_\tau(z)}.
\]
Realizability means that such a decompressed probability measure exists for the chosen factor; existence for every \(\tau\ge1\) is not assumed. A regular point of the physical branch means a point of its stated domain where it is finite and holomorphic.

## Task

Prove that the decompressed transform is algebraic and that, at every regular point \(z\in\mathbb C\setminus\mathbb R\) of its physical branch,
\[
P\!\left(z+\frac{\tau-1}{\tau m_\tau(z)},\,\tau m_\tau(z)\right)=0.
\]
Moreover, prove that the expression
\[
Q_\tau(z,m):=m^{d_z}P\!\left(z+\frac{\tau-1}{\tau m},\,\tau m\right),\qquad m\ne0,
\]
extends to a nonzero polynomial in \(\mathbb C[z,m]\), that the graph of \(m_\tau\) satisfies
\[
Q_\tau(z,m_\tau(z))=0,\qquad z\in\mathbb C\setminus\mathbb R,
\]
and derive an explicit finite coefficient formula for \(Q_\tau\) by expanding the powers with the binomial theorem.
