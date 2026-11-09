# Problem

## Setup

Let \((\mathcal X,\mathcal F)\) be a measurable feature space, let \(D\) be a probability distribution on it, and let \(X\sim D\). Let \(h:\mathcal X\to\{0,1\}\) be a measurable binary classifier. Let \(A=(A_1,\ldots,A_m)\) be a finite collection of discrete measurable protected attributes on \(\mathcal X\). Let \(\mathcal S_A\) be the class of subgroups formed by conjunctions fixing arbitrary subsets of attribute values, and define
\[
\mathcal S_A^+=\{S\in\mathcal S_A:\Pr_D(S)>0\}.
\]

For \(S\in\mathcal S_A\), define the weighted parity disparity by
\[
\Phi_h(S)=
\begin{cases}
\Pr_D(S)\,\big|\Pr_D(h(X)=1)-\Pr_D(h(X)=1\mid S)\big|,
&\Pr_D(S)>0,\\
0,&\Pr_D(S)=0.
\end{cases}
\]
For probability distributions \(D',D''\) on \((\mathcal X,\mathcal F)\), define
\[
\operatorname{SD}(S;D',D'')=\big|\Pr_{D'}(S)-\Pr_{D''}(S)\big|,
\qquad
\mathsf M(D',D'';A)=\sup_{S\in\mathcal S_A}\operatorname{SD}(S;D',D'').
\]
Assume \(p_1=\Pr_D(h(X)=1)>0\) and \(p_0=\Pr_D(h(X)=0)>0\), and write \(D_1=D(\cdot\mid h(X)=1)\), \(D_0=D(\cdot\mid h(X)=0)\).

## Task

Prove, simultaneously for every \(S\in\mathcal S_A^+\), that
\[
\operatorname{SD}(S;D_1,D_0)=\frac{\Phi_h(S)}{p_1p_0}.
\]
Consequently, prove that the conjunction subgroups maximizing \(\Phi_h\) over \(\mathcal S_A\) and those maximizing \(\operatorname{SD}(\cdot;D_1,D_0)\) over \(\mathcal S_A\) are exactly the same, and that
\[
\mathsf M(D_1,D_0;A)=\frac{1}{p_1p_0}\sup_{S\in\mathcal S_A^+}\Phi_h(S).
\]
In particular, for any \(\gamma\in[0,1]\), if \(\Phi_h(S)\le\gamma\) for every \(S\in\mathcal S_A^+\), prove that \(\mathsf M(D_1,D_0;A)\le\gamma/(p_1p_0)\).
