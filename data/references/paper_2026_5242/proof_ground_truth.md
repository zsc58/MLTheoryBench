# Reference Proof

## Proof Structure

Differentiate the causal log-sum-exp energy, rewrite the derivatives as causal softmax-weighted interactions, factor each interaction matrix into query and key maps, and evaluate one unit descent step at the initialization point. Compare the resulting expression with the explicitly defined causal MHA update to identify the value/key and output/query ties.

## Complete Proof

For each head, set $\beta_{kj}=A_kh_j$. For fixed $i$,
\[
\varepsilon(x_i\mid h_{1:i})=-\tau\sum_{k=1}^K\log\!\left(\sum_{j=1}^i e^{\beta_{kj}^{\mathsf T}x_i/\tau}\right).
\]
The chain rule gives
\[
\nabla_{x_i}\varepsilon=-\sum_{k=1}^K\sum_{j=1}^i\alpha_{ij}^{(k)}\beta_{kj},\qquad
\alpha_{ij}^{(k)}=\frac{e^{\beta_{kj}^{\mathsf T}x_i/\tau}}{\sum_{\ell=1}^i e^{\beta_{k\ell}^{\mathsf T}x_i/\tau}}.
\]
Thus $x_i^+=x_i-\eta\nabla\varepsilon$; with $x_i=h_i$ and $\eta=1$,
\[
h_i^+=h_i+\sum_{k=1}^K\sum_{j=1}^i\alpha_{ij}^{(k)}A_kh_j.
\]
Using $A_k=(W_k^Q)^{\mathsf T}W_k^K$ gives
\[
h_i^+=h_i+\sum_{k=1}^K W_k^{Q\mathsf T}\sum_{j=1}^i\alpha_{ij}^{(k)}W_k^Kh_j,
\]
where
\[
\alpha_{ij}^{(k)}=\operatorname{softmax}_{j\le i}\!\left(\frac{(W_k^Kh_j)^{\mathsf T}(W_k^Qh_i)}{\tau}\right).
\]
Comparing with the defined MHA update, this is obtained by setting $W_k^V=W_k^K$ and $W_k^O=W_k^{Q\mathsf T}$. With the stated projection convention this is exactly tied key/value and query/output parameterization, and choosing $\tau=\sqrt{D_r}$ gives the claimed temperature.
