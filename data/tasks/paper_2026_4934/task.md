# Problem

## Setup

Let \(m\ge 2\) be an integer, and let a bin \(B\) contain real responses \(y_1,\dots,y_m\). For any CDF \(F\) of a probability distribution on \(\mathbb R\) with finite first absolute moment and any observation \(y\in\mathbb R\), define
\[
\operatorname{CRPS}(F,y)=\int_{\mathbb R}\bigl(F(t)-\mathbf 1\{t\ge y\}\bigr)^2\,dt.
\]
For each \(k\in\{1,\dots,m\}\), let \(F_{-k}\) be the empirical CDF assigning equal mass \(1/(m-1)\) to the responses \(\{y_\ell:\ell\ne k\}\). Define the bin's leave-one-out cost by
\[
\operatorname{Cost}(B)=\sum_{k=1}^m \operatorname{CRPS}(F_{-k},y_k),
\]
and define the unordered pairwise dispersion
\[
W=\sum_{1\le a<b\le m}|y_a-y_b|.
\]

## Task

Prove that, for every such bin,
\[
\operatorname{Cost}(B)=\frac{m}{(m-1)^2}\,W
=\frac{m}{(m-1)^2}\sum_{1\le a<b\le m}|y_a-y_b|.
\]
