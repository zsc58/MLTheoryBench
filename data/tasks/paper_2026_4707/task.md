# Problem

## Setup

Let \(X=(P,R)\) be a random problem-response pair. Let the binary strong-verification label \(Y\in\{0,1\}\) and weak score \(S\in[0,1]\) be obtained from fixed measurable functions of \(X\). A policy is a Borel-measurable deterministic map \(\pi:[0,1]\to\{\mathsf A,\mathsf R,\mathsf V\}\) that observes only \(S\): \(\mathsf A\) accepts without querying the strong verifier, \(\mathsf R\) rejects without querying it, and \(\mathsf V\) queries the strong verifier and follows \(Y\). Write
\[
\alpha_0=\Pr(Y=0)>0,\qquad \alpha_1=\Pr(Y=1)>0.
\]
Assume calibration: there is a version of the regular conditional distribution for which, for every \(s\in[0,1]\),
\[
\Pr(Y=1\mid S=s)=s.
\]
For weights \(\lambda_1,\lambda_2\in[0,\infty)\), define
\[
J(\pi)=\Pr(\pi(S)=\mathsf V)+\lambda_1\Pr(\pi(S)=\mathsf A\mid Y=0)+\lambda_2\Pr(\pi(S)=\mathsf R\mid Y=1).
\]

## Task

Prove that an optimal policy for minimizing \(J\) can be chosen in two-threshold form: there exist \(0\le t_{\rm low}\le t_{\rm high}\le1\) and an optimal policy \(\pi^\star\) such that
\[
\pi^\star(s)=
\begin{cases}
\mathsf R,&s<t_{\rm low},\\
\mathsf V,&t_{\rm low}<s<t_{\rm high},\\
\mathsf A,&s>t_{\rm high}.
\end{cases}
\]
The actions at the threshold scores are chosen as part of the optimal policy, rather than prescribed by these strict inequalities; ties between optimal boundary choices may be resolved arbitrarily. Equal thresholds are allowed, and strong verification need not be used at their common value, so its region may be empty or degenerate.

Moreover, with \(a=\lambda_1/\alpha_0\) and \(b=\lambda_2/\alpha_1\), prove that
\[
\inf_\pi J(\pi)=\mathbb E\!\left[\min\{1,\,a(1-S),\,bS\}\right],
\]
where the infimum is over the policies defined in the setup.
