# Problem

## Setup

Let \(T\) be a positive integer, let \(\mathcal X\) be a measurable instance space, and let \(\mathcal H\subseteq\{0,1\}^{\mathcal X}\) be a nonempty class of measurable functions with finite VC dimension \(d\).

Before the game, nature fixes laws \(Q,R\) on \(\mathcal X^T\) and a measurable binary labeling function \(g\), and draws \(X_{1:T}\sim Q\). The function \(g\) need not belong to \(\mathcal H\). At round \(t\), the learner observes \(X_t\), predicts \(\widehat Y_t\in\{0,1\}\), and then receives \(Y_t=g(X_t)\). Define
\[
\operatorname{Reg}_T=\sum_{t=1}^T\mathbf 1\{\widehat Y_t\ne Y_t\}-\min_{h\in\mathcal H}\sum_{t=1}^T\mathbf 1\{h(X_t)\ne Y_t\}.
\]

The learner has the following oracle access:

- An agnostic ERM oracle for \(\mathcal H\): on any finite binary-labeled sample, including a sample with repeated points, it returns a hypothesis minimizing the number of mistakes. Any minimizing hypothesis is a valid answer. Oracle calls have unit cost; constructing their input samples costs ordinary computation time, and returned hypotheses can be evaluated efficiently.
- A conditional simulator for \(R\): on any prefix \(x_{1:t}\), including the empty prefix, it returns an unlabeled continuation sampled from \(R(X_{t+1:T}\in\cdot\mid X_{1:t}=x_{1:t})\). These are specified measurable conditional probability kernels; versions on null prefixes are part of the oracle specification. Each call uses fresh randomness independent of nature and the learner. A simulator call has unit oracle cost, with processing its output charged as ordinary computation.

Oracle operations and hypothesis evaluations are measurable. Predictions and oracle queries may depend only on the learner's private randomness, its oracle transcript, and the covariates and labels revealed so far. In particular, the learner is not given \(Q\), \(g\), the actual future covariates, or the divergence between \(Q\) and \(R\); no density-evaluation or ground-truth labeling oracle is supplied.

Use relative entropy in bits:
\[
\mathrm{KL}(Q\|R)=\int\log_2\!\left(\frac{\mathrm dQ}{\mathrm dR}\right)\,\mathrm dQ
\]
when \(Q\ll R\), allowing the value \(+\infty\), and set it to \(+\infty\) otherwise. Expectations below include the covariate draw, learner randomization, and simulator responses.

## Task

Prove that there is a learner, depending on \(T\) and \(\mathcal H\) and using the specified oracles, running in time polynomial in \(T\) in this oracle model, such that simultaneously for every fixed \(Q,R,g\),
\[
\mathbb E_Q[\operatorname{Reg}_T]\le C\sqrt{dT\bigl(1+\mathrm{KL}(Q\|R)\bigr)}
\]
for a universal constant \(C\). For \(d=0\), the claim is that the learner can attain zero regret, including when the divergence is infinite; for \(d\ge1\) and infinite divergence, the displayed upper bound is vacuous.

Moreover, for the threshold class on \([0,1]\),
\[
\mathcal H_{\mathrm{thr}}=\{x\mapsto\mathbf 1\{x\le\theta\}:\theta\in[0,1]\},
\]
prove that there is a universal \(c>0\) such that, for every positive integer \(T\), every \(D\in\{1,\ldots,T\}\), and every learner in the same information model, with no computational restriction, one can choose a fixed oblivious labeling function \(g\) and laws \(Q,R\) satisfying \(\mathrm{KL}(Q\|R)=D\) for which that learner has
\[
\mathbb E_Q[\operatorname{Reg}_T]\ge c\sqrt{DT}.
\]
