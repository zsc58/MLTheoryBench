# Problem

## Setup

Let \(\mathcal X\), \(\mathcal R\), and \(\mathcal A\) be measurable spaces of prompts, reasoning paths, and answers, respectively. Assume that the equality relation on \(\mathcal A\) is measurable. Let \((X,T)\) be a random prompt and its correct answer, with \(T\in\mathcal A\).

Fix a measurable extraction function \(b:\mathcal R\to\mathcal A\), a measurable scoring function \(q:\mathcal X\times\mathcal R\to\mathbb R\), and a non-decreasing weight function \(w:\mathbb R\to(0,\infty)\). Conditional on each prompt, sample a fixed positive integer \(m\) of independent reasoning paths \(R_1,\ldots,R_m\) from the same fixed prompt-dependent distribution, without using the true answer \(T\). Define
\[
B_i=b(R_i),\qquad q_i=q(X,R_i),\qquad w_i=w(q_i).
\]
Thus each score uses the prompt and its individual path alone, without access to \(T\).

Define weighted vote totals
\[
V_a=\sum_{i=1}^m w_i\mathbf 1\{B_i=a\},\qquad a\in\mathcal A.
\]
Let \(\hat A\) be an answer maximizing \(V_a\), with a fixed deterministic measurable tie rule, and define the winning weighted share
\[
C=\frac{\max_{a\in\mathcal A}V_a}{\sum_{a\in\mathcal A}V_a}.
\]
For a threshold \(\tau>0\), the policy outputs \(\hat A\) when \(C>\tau\) and abstains otherwise. Write
\[
p=\Pr(\hat A=T),\qquad 0<p<1,
\]
\[
S_1(\tau)=\Pr(C>\tau\mid \hat A=T),\qquad
S_0(\tau)=\Pr(C>\tau\mid \hat A\ne T),
\]
\[
D(\tau)=S_1(\tau)-S_0(\tau),
\]
and, whenever \(\Pr(C>\tau)>0\), define selective accuracy
\[
A(\tau)=\Pr(\hat A=T\mid C>\tau).
\]

## Task

Prove that for every threshold \(\tau\) with \(\Pr(C>\tau)>0\),
\[
A(\tau)-p
=\frac{p(1-p)D(\tau)}{S_1(\tau)-(1-p)D(\tau)}.
\]
Consequently, \(D(\tau)>0\) if and only if abstention strictly improves selective accuracy \(A(\tau)>p\); if \(D(\tau)\le0\), then \(A(\tau)\le p\), with equality exactly when \(D(\tau)=0\). In particular, if \(D(\tau)\le0\) for every positive threshold having positive retained probability, abstention never improves selective accuracy.
