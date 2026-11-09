# Problem

## Setup

Fix an integer \(L\geq1\) and positive integer layer widths \(n_0,\ldots,n_L\). Write \(n_x=n_0\) and \(n_y=n_L\), and let \(x\in\mathbb R^{n_x}\) and \(y\in\mathbb R^{n_y}\) be arbitrary input and training-label vectors. All activities and weights are real scalars, and let \(f:\mathbb R\to\mathbb R\) be a fixed differentiable activation applied elementwise.

A feedforward network has activities \(a_i^\ell\), weights \(w_{ij}^{\ell-1}\), clamped input \(a_i^0=x_i\), and recurrence
\[
a_i^\ell=f\!\left(\sum_{j=1}^{n_{\ell-1}}w_{ij}^{\ell-1}a_j^{\ell-1}\right),\qquad \ell=1,\ldots,L,\quad 1\leq i\leq n_\ell.
\]

A layered predictive-coding model uses activities and weights with these same indices, predictions
\[
\mu_i^\ell=f\!\left(\sum_{j=1}^{n_{\ell-1}}w_{ij}^{\ell-1}a_j^{\ell-1}\right),
\]
prediction errors \(\epsilon_i^\ell=a_i^\ell-\mu_i^\ell\), and energy
\[
E_N=\sum_{\ell=1}^L\sum_{i=1}^{n_\ell}(\epsilon_i^\ell)^2.
\]
Inputs are clamped to \(x\); during training outputs are additionally clamped to \(y\). Its activity rule minimizes \(E_N\) over all hidden activities during training and over all non-input activities during testing, with the weights fixed. Its training weight rule minimizes \(E_N\) over the weights, with the activities fixed.

A predictive-coding graph has \(N\) scalar real nodes \(a_\alpha\), indexed by \(1\leq\alpha\leq N\), and disjoint ordered input and output node sets of sizes \(n_x\) and \(n_y\). It has real weights \(\widetilde w_{\alpha\beta}\), predictions
\[
\widetilde\mu_\alpha=f\!\left(\sum_{\beta=1}^N\widetilde w_{\alpha\beta}a_\beta\right),
\]
errors \(\widetilde\epsilon_\alpha=a_\alpha-\widetilde\mu_\alpha\), and energy
\[
E_G=\sum_{\alpha=1}^N(\widetilde\epsilon_\alpha)^2.
\]
Its input nodes are clamped, in their designated order, to \(x\); during training its output nodes are additionally clamped, in their designated order, to \(y\). Its activity rule minimizes \(E_G\) over all unclamped activities with weights fixed. Its training weight rule minimizes \(E_G\) over the weights with activities fixed. Unless a weight family is explicitly prescribed, graph weights are unrestricted.

Here \(\operatorname{argmin}_{u\in D}F(u)\) denotes the set of global minimizers over the stated real domain \(D\); it may be empty. The minimization rules above specify these sets, not a particular iterative algorithm or a general assertion of attainment. When \(L=1\), the hidden-activity domain is the singleton consisting of the empty tuple.

## Task

Prove the following integrated theorem.

1. For every fixed choice of layered weights and input, the test-time argmin of \(E_N\) over all non-input activities consists exactly of the activity tuple given by the feedforward recurrence above for every layer.

2. For every choice of the positive layer widths above satisfying \(\sum_{\ell=0}^L n_\ell=N\), the layered predictive-coding model is an exactly equivalent hierarchical block-sparse specialization of a predictive-coding graph: there are a choice of graph inputs and outputs, a correspondence between graph nodes and layered activities, and a permitted block-sparse graph weight family corresponding to the layered weights such that the graph energy differs from \(E_N\) by a constant depending only on the clamped input, with the activation fixed. Under this correspondence, the training and testing activity argmin sets and the training weight argmin sets over the permitted weights agree. Conclude that predictive-coding graphs contain the layered models as a special case and realize their feedforward testing computations, while more general graph topologies permit additional connections.
