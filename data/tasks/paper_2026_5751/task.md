# Problem

## Setup

Let \(\mathcal E\) and \(\mathcal A\) be arbitrary sets, let \(\mathcal A^*\) be the set of finite action strings (including the empty string \(\varnothing\)), and set
\[
\mathcal X=\mathcal E\times\mathcal A^*.
\]
For \(x=(e,s)\in\mathcal X\) and \(y\in\mathcal A^*\), write \(x\mathbin{\cdot}y=(e,sy)\).

A stopping rule is a function \(\sigma:\mathcal X\times\mathcal A^*\to\{0,1\}\). Given a local predictor \(h:\mathcal X\to\mathcal A\) and a start state \(x\), define its rollout recursively: begin with \(y_0=\varnothing\); while \(\sigma(x,y_t)=0\), append the action \(h(x\mathbin{\cdot}y_t)\). The resulting terminal string is denoted \(\mathsf R_\sigma(h)(x)\). Assume that every such rollout terminates for every \(h\in\mathcal H\) and every \(x\in\mathcal X\), where \(\mathcal H\subseteq\mathcal A^{\mathcal X}\). Let
\[
\mathsf R_\sigma(\mathcal H)=\{\mathsf R_\sigma(h):h\in\mathcal H\}\subseteq(\mathcal A^*)^{\mathcal X}.
\]
Exact-trace loss is zero-one loss on the entire terminal string.

For a multiclass class \(F\subseteq Y^Z\) and a finite set \(D\subseteq Z\), write \(F|_D=\{f|_D:f\in F\}\). A finite nonempty set \(C\subseteq F|_D\) is a DS pseudo-cube on \(D\) if, for every \(f\in C\) and every \(z\in D\), there is \(g\in C\) such that
\[
 g(z)\ne f(z),\qquad g(u)=f(u)\quad\text{for every }u\in D\setminus\{z\}.
\]
The DS dimension \(\operatorname{DSdim}(F)\) is the supremum of the cardinalities of finite domain sets admitting such a pseudo-cube. Thus a witness of size \(k\) uses \(k\) distinct domain points. Set \(\operatorname{DSdim}(F)=0\) if there is no positive-dimensional witness, including when \(F\) is empty, and set it to \(\infty\) if witness sizes are unbounded.

For \(F\subseteq Y^Z\) with \(Y\ne\varnothing\), let \(n_{\rm PAC}^{\epsilon,\delta}(F)\) be the least integer \(m\geq0\) for which there exists a possibly randomized learner with the following guarantee. The learner may depend on \(F,\epsilon,\delta\), but is chosen independently of the unknown distribution \(P\) and unknown target \(f_*\). For every distribution \(P\) on \(Z\) and every \(f_*\in F\), it receives only the labeled sample
\[
 S=((Z_i,f_*(Z_i)))_{i=1}^m,\qquad Z_1,\ldots,Z_m\ \text{i.i.d. from }P,
\]
and returns a predictor \(\widehat f:Z\to Y\), not necessarily in \(F\), satisfying
\[
 \Pr\!\left[P\{z:\widehat f(z)\ne f_*(z)\}\leq\epsilon\right]\geq1-\delta.
\]
The probability is taken over the i.i.d. input tuple and an independent internal random seed of the learner, with target labels substituted as deterministic values. Throughout, the disagreement sets defining the risk and the displayed success event are assumed measurable in the input space and input-tuple/seed probability space, respectively. No measurable structure on \(Y\), and no separate measurability of the deterministic labeling map or of the complete labeled tuple as a label-valued random variable, is imposed. If no such \(m\) exists, set \(n_{\rm PAC}^{\epsilon,\delta}(F)=\infty\).

## Task

Prove the following integrated optimality theorem.

There is a universal constant \(C>0\) such that, for every pointwise-terminating \((\mathcal H,\sigma)\) and every \(0<\epsilon,\delta<1\),
\[
 n_{\rm PAC}^{\epsilon,\delta}\bigl(\mathsf R_\sigma(\mathcal H)\bigr)
 \leq C\,\frac{\operatorname{DSdim}(\mathcal H)+\log(1/\delta)}{\epsilon}.
\]
In particular, this bound has no dependence on the lengths of the generated traces.

Moreover, the dependence is worst-case optimal: there are universal constants \(c,c_0>0\) such that, for every integer \(d\geq1\) and all \(0<\epsilon,\delta\leq c_0\), one can choose \(\mathcal E,\mathcal A,\mathcal H\), and a pointwise-terminating stopping rule \(\sigma\), with \(\operatorname{DSdim}(\mathcal H)=d\), for which
\[
 n_{\rm PAC}^{\epsilon,\delta}\bigl(\mathsf R_\sigma(\mathcal H)\bigr)
 \geq c\,\frac{d+\log(1/\delta)}{\epsilon}.
\]
