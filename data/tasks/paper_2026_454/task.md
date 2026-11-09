# Problem

## Setup

Let \(\Theta\) and \(\mathcal X\) be measurable Euclidean spaces with their usual reference measures. Let \(\pi(\theta)\) be a probability density on \(\Theta\), and let \((\theta,x)\mapsto r(x\mid\theta)\) be nonnegative and jointly measurable, with \(r(\cdot\mid\theta)\) a probability density on \(\mathcal X\) for \(\pi\)-almost every \(\theta\). Define the base joint density and its data marginal by
\[
P_0(\theta,x)=\pi(\theta)r(x\mid\theta),
\qquad
p_X(x)=\int_\Theta \pi(t)r(x\mid t)\,dt.
\]
For \(\beta\in[1/2,1]\), define the importance weight
\[
w_\beta(\theta,x)=
\begin{cases}
\left(p_X(x)/r(x\mid\theta)\right)^{1-\beta}, & r(x\mid\theta)>0,\\
0, & r(x\mid\theta)=0,
\end{cases}
\]
where a nonnegative quantity to the zeroth power is interpreted as one. Density formulas are understood up to null sets; set \(w_\beta=0\) on any exceptional \(P_0\)-null set where the displayed ratio is undefined.

## Task

Prove that, for every \(\beta\in[1/2,1]\),
\[
\mathbb E_{(\theta,x)\sim P_0}\left[w_\beta(\theta,x)^2\right]\le 1.
\]
Conclude that \(w_\beta\) has finite variance under \(P_0\) for every such \(\beta\).
