# Reference Proof

## Proof Structure

Work conditionally on the fixed realized base training sample. Decompose every classifier into its signal and orthogonal components. An inverse rescaling of the orthogonal classifier component preserves every training logit and gives a bijection between global-minimizer sets. The same identity preserves every coupled independent-test logit, so the attainable test accuracies and their suprema agree.

## Theorem-Critical Obligations

1. The accuracy supremum is a well-defined number on the stated nonempty-minimizer domain, and the test probability is taken with the training realization fixed.
2. An invertible change of weights preserves the objective for the two amplitude-indexed versions of the same training sample.
3. This change of weights maps the full minimizer sets bijectively, establishing attainment at the compared amplitude as well.
4. Corresponding weights have identical test classification indicators under a coupling of the two test distributions.
5. The nonempty attainable-accuracy sets, and hence their suprema, are equal.

## Complete Proof

Fix the realized training labels and base noise variables specified in the problem, and assume that \(\mathcal M_{\sigma_n}\ne\varnothing\). All probabilities below concern only the independent test draw.

The function \(f:\mathbb R\to\mathbb R\) is finite and convex, so it is continuous. The empirical objective is therefore finite and continuous at every finite weight vector. For each fixed weight vector the test classification event is measurable, and its probability belongs to \([0,1]\). Consequently, the nonempty set of accuracies attained by \(\mathcal M_{\sigma_n}\) has a well-defined real supremum. We do not infer attainment of the empirical minimum from convexity and evenness; it is the explicit domain condition in the problem.

Write every weight vector uniquely as
\[
S=s e_1+w,\qquad w\perp e_1.
\]
For any positive amplitude \(t\), the signed training input is
\[
\widetilde x_i(t)=(\mu_f+y_i\sigma_f\xi_{f,i})e_1+t y_i\xi_{\perp,i}.
\]
Thus
\[
z_i^{(t)}(S)=s(\mu_f+y_i\sigma_f\xi_{f,i})+t w^\top(y_i\xi_{\perp,i}).
\]
The empirical objective is the average of the fixed scalar loss
\[
\ell(z)=(1-\alpha)\log(1+e^{-z})+\alpha f(z),
\]
so it depends on the weights only through these training logits.

Fix \(\beta>0\), put \(t'=\beta\sigma_n\), and define
\[
T_\beta(s e_1+w)=s e_1+\beta^{-1}w.
\]
This map is invertible, with inverse \(T_{\beta^{-1}}\). Because the two training datasets use the same base realization,
\[
\begin{aligned}
z_i^{(t')}(T_\beta S)
&=s(\mu_f+y_i\sigma_f\xi_{f,i})+(\beta\sigma_n)(\beta^{-1}w)^\top(y_i\xi_{\perp,i})\\
&=z_i^{(\sigma_n)}(S).
\end{aligned}
\]
Hence
\[
L_{t'}(T_\beta S)=L_{\sigma_n}(S)
\qquad\text{for every }S\in\mathbb R^d.
\]

To verify the minimizer correspondence explicitly, let \(S\in\mathcal M_{\sigma_n}\) and let \(U\in\mathbb R^d\) be any competing weight at amplitude \(t'\). Write \(V=T_\beta^{-1}U\). Then
\[
L_{t'}(T_\beta S)=L_{\sigma_n}(S)
\le L_{\sigma_n}(V)=L_{t'}(U).
\]
Thus \(T_\beta S\in\mathcal M_{t'}\). Applying the same reasoning with the inverse map gives
\[
\mathcal M_{t'}=T_\beta\mathcal M_{\sigma_n}.
\]
In particular, \(\mathcal M_{t'}\) is nonempty, and this is a bijection of the full minimizer sets. No uniqueness or data-rank assumption is needed.

For the test distributions at the two amplitudes, use one independent base test draw \((y,\xi_f,\xi_\perp)\). This coupling has exactly the required test marginal distribution at each amplitude. The same calculation gives
\[
(T_\beta S)^\top x(t')
=s(y\mu_f+\sigma_f\xi_f)+\sigma_n w^\top\xi_\perp
=S^\top x(\sigma_n).
\]
Multiplication by \(y\) shows that the signed test logits agree pointwise. Therefore
\[
\mathbf 1\{y(T_\beta S)^\top x(t')\ge0\}
=\mathbf 1\{yS^\top x(\sigma_n)\ge0\}.
\]
Taking probability over the independent test draw proves
\[
A_{t'}(T_\beta S)=A_{\sigma_n}(S).
\]
The bijection of minimizer sets now yields equality of the nonempty sets
\[
\{A_{t'}(U):U\in\mathcal M_{t'}\}
=\{A_{\sigma_n}(S):S\in\mathcal M_{\sigma_n}\}.
\]
Their suprema are equal, so
\[
\operatorname{Acc}^*(\beta\sigma_n)=\operatorname{Acc}^*(\sigma_n).
\]
Since \(\beta>0\) was arbitrary, the result holds throughout the positive-amplitude domain.

## Boundary and Dependency Checks

The argument includes \(\sigma_f=0\), \(d=1\), rank-deficient training designs, nonsmooth convex penalties, and nonunique minimizers. It makes no assertion at zero orthogonal amplitude. The fixed-training formulation requires no measurable choice of a training-dependent optimizer and no interchange of a training expectation with a supremum. Gaussianity is retained as a standing source assumption, although the algebraic correspondence does not need it. All theorem-critical obligations are derived above; no external theorem or unresolved private proof dependency is used.
