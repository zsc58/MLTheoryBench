# Reference Proof

## Proof Structure

Fix the weights during testing. First establish that the feedforward recurrence supplies a zero-energy activity tuple. At any testing minimizer, the correctly normalized first-order equations force the output error to vanish, and backward induction forces every other non-input error to vanish. Conversely, the recurrence gives a global minimizer. Next partition the graph nodes into layers and restrict its weights to consecutive-layer blocks. The graph energy then equals the layered energy plus a clamped-input constant. A bijective correspondence of optimization domains transfers all specified argmin sets.

## Complete Proof

### 1. Testing equivalence

Fix arbitrary real layered weights and input \(x\). The recurrence defines the activities successively in layers \(1,\ldots,L\). All sums are finite and \(f\) is real-valued on \(\mathbb R\), so this produces a well-defined activity tuple. Every residual at this tuple is zero. Since
\[
E_N=\sum_{\ell=1}^L\sum_{i=1}^{n_\ell}(\epsilon_i^\ell)^2\geq0,
\]
the testing minimum exists and equals zero.

For completeness, the derivative and backward-induction argument is as follows. Put
\[
z_j^{\ell+1}=\sum_{m=1}^{n_\ell}w_{jm}^{\ell}a_m^\ell.
\]
For \(1\leq\ell<L\), the activity \(a_i^\ell\) enters its own residual directly and the next layer's residuals through their predictions. Consequently
\[
\frac12\frac{\partial E_N}{\partial a_i^\ell}
=\epsilon_i^\ell-\sum_{j=1}^{n_{\ell+1}}w_{ji}^{\ell}f'(z_j^{\ell+1})\epsilon_j^{\ell+1}.
\]
There is no layer after the output, so
\[
\frac12\frac{\partial E_N}{\partial a_i^L}=\epsilon_i^L.
\]
The factor \(1/2\) on the left is required because the defined energy is the full sum of squared residuals.

At any testing minimizer all non-input activities, including output activities, are unconstrained real optimization variables. Their derivatives vanish. Thus \(\epsilon^L=0\). If \(\epsilon^{\ell+1}=0\), the equation for layer \(\ell\) gives \(\epsilon^\ell=0\). Descending through \(\ell=L-1,\ldots,1\) proves that every non-input residual vanishes. No stationarity equation is imposed on the clamped input.

Therefore every minimizing tuple satisfies
\[
a_i^\ell=f\!\left(\sum_{j=1}^{n_{\ell-1}}w_{ij}^{\ell-1}a_j^{\ell-1}\right),\qquad \ell=1,\ldots,L.
\]
Conversely, every tuple satisfying these recurrences has zero energy and is a global minimizer. The recurrence determines a unique tuple successively from \(x\), so the testing argmin is precisely the feedforward computation. When \(L=1\), the output equation alone gives the derivative argument.

An alternative proof may omit derivatives entirely: the constructed zero-energy tuple shows that every global minimizer has energy zero, and a finite sum of nonnegative squares is zero exactly when every residual is zero.

### 2. Graph embedding

For the given positive widths with total \(N\), define
\[
s_{-1}=0,\qquad s_\ell=\sum_{r=0}^{\ell}n_r,\qquad
I_\ell=\{s_{\ell-1}+1,\ldots,s_\ell\}\quad(0\leq\ell\leq L).
\]
These sets partition \(\{1,\ldots,N\}\). Identify graph node \(s_{\ell-1}+i\) with activity \(a_i^\ell\), for \(1\leq i\leq n_\ell\). Choose \(I_0\) and \(I_L\), in increasing order, as the input and output sets. Their sizes are \(n_x\) and \(n_y\), respectively, so their clamps agree with the layered clamps.

For every \(\ell=1,\ldots,L\), set
\[
\widetilde w_{s_{\ell-1}+i,\,s_{\ell-2}+j}=w_{ij}^{\ell-1},
\qquad 1\leq i\leq n_\ell,\quad 1\leq j\leq n_{\ell-1},
\]
and fix every other graph weight at zero. For \(\ell=1\), the column index is \(s_{-1}+j=j\), so this formula also covers the first non-input layer. The permitted block entering layer \(\ell\) has \(n_\ell\) rows and \(n_{\ell-1}\) columns. This assignment is a bijection between the layered weight space and the permitted graph weight family; permitted entries may themselves be zero.

For a node in \(I_\ell\), \(\ell\geq1\), its only possibly nonzero incoming weights are from \(I_{\ell-1}\). Thus its graph prediction is exactly
\[
f\!\left(\sum_{j=1}^{n_{\ell-1}}w_{ij}^{\ell-1}a_j^{\ell-1}\right).
\]
Every input row is zero, so each input prediction is \(f(0)\). Therefore, for every corresponding activity and permitted-weight tuple,
\[
E_G=\sum_{i=1}^{n_0}(x_i-f(0))^2+
\sum_{\ell=1}^L\sum_{i=1}^{n_\ell}(\epsilon_i^\ell)^2
=C+E_N,
\qquad C=\sum_{i=1}^{n_0}(x_i-f(0))^2.
\]
For the fixed activation, \(C\) depends only on the clamped input, not on any optimized activity or permitted weight.

### 3. Transfer of optimization rules and inclusion

If \(T:D\to\widetilde D\) is a bijection and \(G(Tu)=F(u)+C\) for every \(u\in D\), then
\[
u\in\operatorname{argmin}_{v\in D}F(v)
\iff F(u)\leq F(v)\text{ for every }v\in D
\iff G(Tu)\leq G(Tv)\text{ for every }v\in D.
\]
Surjectivity of \(T\) makes the last condition equivalent to \(Tu\in\operatorname{argmin}_{\widetilde v\in\widetilde D}G(\widetilde v)\). This proves equality of the corresponding argmin sets even when they are empty.

Apply this observation to the activity identification with weights fixed. During training, both models fix \(x\) and \(y\) and optimize exactly the hidden activities. During testing, both fix only \(x\) and optimize all non-input activities. Apply it also to the weight identification with activities fixed: all permitted blocks vary freely, while every other graph weight remains zero. This proves all three asserted argmin correspondences.

When \(L=1\), the training hidden-activity domain is the singleton consisting of the empty tuple, so its argmin correspondence also holds. No existence claim about general training or unrestricted-graph minimizers is required. The testing argmin for the constructed graph does exist by the first part and the constant-shift identity.

Finally, the unrestricted graph weight space contains the permitted hierarchical family and also allows entries outside its consecutive-layer blocks. Thus the layered models occur as a special case of the graph models, and their testing computations are exactly the feedforward computations established in the first part. This is structural inclusion, not a claim that arbitrary added connections preserve feedforward computations or that predictive-coding training equals backpropagation.
